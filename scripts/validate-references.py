#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from repo_utils import REPO_ROOT, extract_internal_refs, iter_markdown_files, repo_relative


def resolve_reference(current_file: Path, candidate: str) -> Path:
    candidate_path = Path(candidate)
    if "*" in candidate:
        return REPO_ROOT / "__wildcard_ignored__"
    if candidate_path.is_absolute():
        return candidate_path
    repo_relative_target = REPO_ROOT / candidate_path
    if repo_relative_target.exists():
        return repo_relative_target
    if "/" not in candidate:
        matches = [path for path in REPO_ROOT.rglob(candidate) if ".git" not in path.parts]
        if len(matches) == 1:
            return matches[0]
    return (current_file.parent / candidate_path).resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate markdown file references in the repository")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON output")
    parser.add_argument(
        "--include-fetched",
        action="store_true",
        help="Include raw *-fetched.md files in validation",
    )
    args = parser.parse_args()

    missing: dict[str, list[str]] = defaultdict(list)

    for path in iter_markdown_files(include_fetched=args.include_fetched):
        text = path.read_text(encoding="utf-8")
        for ref in extract_internal_refs(text):
            if "*" in ref:
                continue
            if ref.endswith((".json", ".jsonl")) and ref.startswith("meta/") and ref in {
                "meta/chunk-manifest.jsonl",
                "meta/chunk-manifest-summary.json",
                "meta/fetch-log.jsonl",
                "meta/freshness-manifest.json",
            }:
                continue
            target = resolve_reference(path, ref)
            if not target.exists():
                missing[repo_relative(path)].append(ref)

    if args.json:
        print(json.dumps(missing, indent=2, sort_keys=True))
    elif missing:
        print("Reference validation failed:\n")
        for rel_path, refs in missing.items():
            print(rel_path)
            for ref in sorted(set(refs)):
                print(f"  - missing `{ref}`")
    else:
        print("Reference validation passed.")

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
