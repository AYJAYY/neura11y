#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

from repo_utils import REPO_ROOT, load_markdown, repo_relative

DEFAULT_FRESHNESS_TERMS = [
    "stale",
    "outdated",
    "verify",
    "last reviewed",
    "last verified",
    "last fetched",
]
DEFAULT_NORMATIVE_TERMS = ["must", "required", "normative"]
DEFAULT_PRESCRIPTIVE_TERMS = ["recommended", "best practice", "advisory", "prescriptive"]


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


def _contains_term(text: str, term: str) -> bool:
    return term.lower() in text.lower()


def _contains_any_term(text: str, terms: list[str]) -> bool:
    return any(_contains_term(text, term) for term in terms)


def validate_pattern(pattern: dict, responses_dir: Path | None) -> dict:
    issues: list[str] = []
    checks_total = 0
    checks_passed = 0

    def record(condition: bool, failure_message: str) -> None:
        nonlocal checks_total, checks_passed
        checks_total += 1
        if condition:
            checks_passed += 1
        else:
            issues.append(failure_message)

    prompt_file = REPO_ROOT / pattern["prompt_file"]
    record(prompt_file.exists(), f"missing prompt file `{pattern['prompt_file']}`")

    context_paths = [REPO_ROOT / rel_path for rel_path in pattern["context_files"]]
    stale_context_files: list[str] = []
    for path, rel_path in zip(context_paths, pattern["context_files"]):
        record(path.exists(), f"missing context file `{rel_path}`")
        if path.exists():
            metadata, _ = load_markdown(path)
            if metadata.get("stale") is True:
                stale_context_files.append(rel_path)

    corpus = "\n".join(
        path.read_text(encoding="utf-8")
        for path in context_paths
        if path.exists()
    )

    for citation in pattern.get("expected_citations", []):
        record(
            citation in corpus,
            f"expected citation `{citation}` not found in fixture context",
        )

    for phrase in pattern.get("required_context_terms", []):
        record(
            _contains_term(corpus, phrase),
            f"required context term `{phrase}` not found in fixture context",
        )

    if responses_dir:
        response_path = responses_dir / f"{pattern['id']}.md"
        record(
            response_path.exists(),
            f"missing response file `{repo_relative(response_path)}`",
        )
        if response_path.exists():
            response_text = response_path.read_text(encoding="utf-8")
            for citation in pattern.get("expected_citations", []):
                record(
                    citation in response_text,
                    f"response missing expected citation `{citation}`",
                )
            for citation in pattern.get("forbidden_citations", []):
                record(
                    citation not in response_text,
                    f"response includes forbidden citation `{citation}`",
                )
            for phrase in pattern.get("required_response_terms", []):
                record(
                    _contains_term(response_text, phrase),
                    f"response missing required term `{phrase}`",
                )
            for phrase in pattern.get("forbidden_response_terms", []):
                record(
                    not _contains_term(response_text, phrase),
                    f"response includes forbidden term `{phrase}`",
                )
            if pattern.get("requires_freshness_caveat"):
                if stale_context_files:
                    freshness_terms = pattern.get("freshness_terms", DEFAULT_FRESHNESS_TERMS)
                    record(
                        _contains_any_term(response_text, freshness_terms),
                        "response missing freshness caveat for stale context",
                    )
                else:
                    record(
                        False,
                        "fixture requires freshness caveat but no stale context files were found",
                    )
            if pattern.get("requires_normative_prescriptive_distinction"):
                normative_terms = pattern.get("normative_terms", DEFAULT_NORMATIVE_TERMS)
                prescriptive_terms = pattern.get("prescriptive_terms", DEFAULT_PRESCRIPTIVE_TERMS)
                record(
                    _contains_any_term(response_text, normative_terms),
                    "response missing normative/required language",
                )
                record(
                    _contains_any_term(response_text, prescriptive_terms),
                    "response missing prescriptive/best-practice language",
                )

    return {
        "passed": not issues,
        "issues": issues,
        "checks_passed": checks_passed,
        "checks_total": checks_total,
        "stale_context_files": stale_context_files,
        "response_evaluated": bool(responses_dir),
    }


def write_report(
    report_path: Path,
    fixtures: list[dict],
    checks: dict[str, tuple[bool, str]],
    pattern_results: dict[str, dict],
    responses_dir: Path | None,
) -> None:
    today = dt.date.today().isoformat()
    lines = [
        "---",
        'title: "Latest AI Validation Report"',
        'type: "meta"',
        'status: "curated"',
        f'last_updated: "{today}"',
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
        result = pattern_results[fixture["id"]]
        passed = result["passed"]
        issues = result["issues"]
        lines.append(f"### {fixture['pattern']}")
        lines.append("")
        lines.append(f"- Prompt file: `{fixture['prompt_file']}`")
        lines.append(f"- Result: {'PASS' if passed else 'FAIL'}")
        lines.append(
            f"- Checks: {result['checks_passed']}/{result['checks_total']} passed"
        )
        if fixture.get("expected_citations"):
            lines.append(
                "- Expected citations: "
                + ", ".join(f"`{citation}`" for citation in fixture["expected_citations"])
            )
        if result["stale_context_files"]:
            lines.append(
                "- Stale context files: "
                + ", ".join(f"`{path}`" for path in result["stale_context_files"])
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
    pattern_failed = any(not result["passed"] for result in pattern_results.values())

    print(f"Validation report written to {repo_relative(report_path)}")
    print(
        f"Structural checks: {sum(1 for passed, _ in checks.values() if passed)}/{len(checks)} passed"
    )
    print(
        f"Pattern checks: {sum(1 for result in pattern_results.values() if result['passed'])}/{len(pattern_results)} passed"
    )
    return 1 if structural_failed or pattern_failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
