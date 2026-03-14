#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from repo_utils import REPO_ROOT, repo_relative


def run_subprocess(script_name: str) -> tuple[bool, str]:
    script_path = REPO_ROOT / "scripts" / script_name
    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    output = (result.stdout + result.stderr).strip()
    return result.returncode == 0, output


def load_fixture(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_pattern(pattern: dict, responses_dir: Path | None) -> tuple[bool, list[str]]:
    issues: list[str] = []

    prompt_file = REPO_ROOT / pattern["prompt_file"]
    if not prompt_file.exists():
        issues.append(f"missing prompt file `{pattern['prompt_file']}`")

    context_paths = [REPO_ROOT / rel_path for rel_path in pattern["context_files"]]
    for path, rel_path in zip(context_paths, pattern["context_files"]):
        if not path.exists():
            issues.append(f"missing context file `{rel_path}`")

    corpus = "\n".join(
        path.read_text(encoding="utf-8")
        for path in context_paths
        if path.exists()
    )

    for citation in pattern.get("expected_citations", []):
        if citation not in corpus:
            issues.append(f"expected citation `{citation}` not found in fixture context")

    if responses_dir:
        response_path = responses_dir / f"{pattern['id']}.md"
        if not response_path.exists():
            issues.append(f"missing response file `{repo_relative(response_path)}`")
        else:
            response_text = response_path.read_text(encoding="utf-8")
            for citation in pattern.get("expected_citations", []):
                if citation not in response_text:
                    issues.append(f"response missing expected citation `{citation}`")
            for citation in pattern.get("forbidden_citations", []):
                if citation in response_text:
                    issues.append(f"response includes forbidden citation `{citation}`")

    return not issues, issues


def write_report(
    report_path: Path,
    fixtures: list[dict],
    checks: dict[str, tuple[bool, str]],
    pattern_results: dict[str, tuple[bool, list[str]]],
    responses_dir: Path | None,
) -> None:
    lines = [
        "---",
        'title: "Latest AI Validation Report"',
        'type: "meta"',
        'status: "curated"',
        'last_updated: "2026-03-14"',
        'ai_context: "Most recent AI validation run against repository fixtures and structural checks."',
        "---",
        "",
        "# Latest AI Validation Report",
        "",
        f"Responses evaluated: {'yes' if responses_dir else 'no (preflight only)'}",
        "",
        "## Structural Checks",
        "",
    ]

    for name, (passed, output) in checks.items():
        lines.append(f"- `{name}` — {'PASS' if passed else 'FAIL'}")
        if output:
            lines.append(f"  Output: {output.splitlines()[0]}")

    lines.extend(["", "## Pattern Checks", ""])
    for fixture in fixtures:
        passed, issues = pattern_results[fixture["id"]]
        lines.append(f"### {fixture['pattern']}")
        lines.append("")
        lines.append(f"- Prompt file: `{fixture['prompt_file']}`")
        lines.append(f"- Result: {'PASS' if passed else 'FAIL'}")
        if fixture.get("expected_citations"):
            lines.append(
                "- Expected citations: "
                + ", ".join(f"`{citation}`" for citation in fixture["expected_citations"])
            )
        if issues:
            lines.append("- Issues:")
            for issue in issues:
                lines.append(f"  - {issue}")
        lines.append("")

    report_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate AI usage patterns against repository fixtures")
    parser.add_argument(
        "--fixtures",
        default="meta/ai-validation-fixtures.json",
        help="Fixture file relative to repo root",
    )
    parser.add_argument(
        "--report",
        default="meta/latest-ai-validation-report.md",
        help="Markdown report output path",
    )
    parser.add_argument(
        "--responses-dir",
        help="Optional directory of model responses named <pattern-id>.md",
    )
    args = parser.parse_args()

    fixtures_path = REPO_ROOT / args.fixtures
    report_path = REPO_ROOT / args.report
    report_path.parent.mkdir(parents=True, exist_ok=True)

    fixtures = load_fixture(fixtures_path)
    responses_dir = (REPO_ROOT / args.responses_dir) if args.responses_dir else None

    checks = {
        "validate-frontmatter.py": run_subprocess("validate-frontmatter.py"),
        "validate-references.py": run_subprocess("validate-references.py"),
    }

    pattern_results = {
        fixture["id"]: validate_pattern(fixture, responses_dir)
        for fixture in fixtures
    }

    write_report(report_path, fixtures, checks, pattern_results, responses_dir)

    structural_failed = any(not passed for passed, _ in checks.values())
    pattern_failed = any(not passed for passed, _ in pattern_results.values())

    print(f"Validation report written to {repo_relative(report_path)}")
    print(
        f"Structural checks: {sum(1 for passed, _ in checks.values() if passed)}/{len(checks)} passed"
    )
    print(
        f"Pattern checks: {sum(1 for passed, _ in pattern_results.values() if passed)}/{len(pattern_results)} passed"
    )
    return 1 if structural_failed or pattern_failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
