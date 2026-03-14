#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

from repo_utils import iter_markdown_files, load_markdown, repo_relative

ROOT_AND_META_FILES = {"README.md", "INDEX.md", "AI-USAGE-GUIDE.md", "GLOSSARY.md"}
DATE_FIELDS = {"last_fetched", "last_verified", "last_reviewed", "last_updated"}


def _is_iso_date(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _classify(rel_path: str) -> str:
    if rel_path in ROOT_AND_META_FILES or rel_path.startswith("meta/"):
        return "repository-meta"
    if rel_path.startswith("legal-and-compliance/"):
        return "legal"
    if rel_path.startswith("domains/social-media/platforms/"):
        return "platform"
    if rel_path.startswith("ai-prompts/"):
        return "prompt"
    return "content"


def _schema_for(rel_path: str) -> dict:
    file_class = _classify(rel_path)
    if file_class == "repository-meta":
        return {
            "required": {"title", "type", "status", "ai_context", "last_updated"},
            "date_fields": {"last_updated"},
            "optional": {"tags", "standard", "source_url", "domain"},
        }
    if file_class == "legal":
        return {
            "required": {
                "title",
                "standard",
                "source_url",
                "domain",
                "last_fetched",
                "last_reviewed",
                "status",
                "tags",
                "ai_context",
            },
            "date_fields": {"last_fetched", "last_reviewed"},
            "optional": {"type", "stale"},
        }
    if file_class == "platform":
        return {
            "required": {
                "title",
                "standard",
                "source_url",
                "domain",
                "last_verified",
                "status",
                "tags",
                "ai_context",
            },
            "date_fields": {"last_verified", "last_fetched"},
            "optional": {"last_fetched", "type", "stale"},
        }
    return {
        "required": {
            "title",
            "standard",
            "source_url",
            "domain",
            "status",
            "tags",
            "ai_context",
            "last_fetched",
        },
        "date_fields": {"last_fetched"},
        "optional": {"type", "last_reviewed", "last_verified", "stale", "last_updated"},
    }


def validate_file(path: Path) -> list[str]:
    rel_path = repo_relative(path)
    metadata, _ = load_markdown(path)
    schema = _schema_for(rel_path)
    issues: list[str] = []

    for field in sorted(schema["required"]):
        if field not in metadata:
            issues.append(f"missing required field `{field}`")

    if "domain" in schema["required"]:
        domain = metadata.get("domain")
        if not isinstance(domain, list):
            issues.append("`domain` must be a YAML list")

    if "tags" in schema["required"]:
        tags = metadata.get("tags")
        if not isinstance(tags, list):
            issues.append("`tags` must be a YAML list")

    stale = metadata.get("stale")
    if stale is not None and not isinstance(stale, bool):
        issues.append("`stale` must be true or false when present")

    for field in DATE_FIELDS:
        if field in metadata and metadata[field] and not _is_iso_date(metadata[field]):
            issues.append(f"`{field}` must use YYYY-MM-DD")

    if rel_path.startswith("legal-and-compliance/") and "last_reviewed" not in metadata:
        issues.append("legal files must include `last_reviewed`")

    if rel_path.startswith("domains/social-media/platforms/") and "last_verified" not in metadata:
        issues.append("platform guides must include `last_verified`")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate repository frontmatter schemas")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON output")
    parser.add_argument(
        "--include-fetched",
        action="store_true",
        help="Include raw *-fetched.md files in validation",
    )
    args = parser.parse_args()

    results: dict[str, list[str]] = {}
    for path in iter_markdown_files(include_fetched=args.include_fetched):
        issues = validate_file(path)
        if issues:
            results[repo_relative(path)] = issues

    if args.json:
        print(json.dumps(results, indent=2, sort_keys=True))
    elif results:
        print("Frontmatter validation failed:\n")
        for rel_path, issues in results.items():
            print(rel_path)
            for issue in issues:
                print(f"  - {issue}")
    else:
        print("Frontmatter validation passed.")

    return 1 if results else 0


if __name__ == "__main__":
    raise SystemExit(main())
