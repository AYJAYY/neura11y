#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from repo_utils import REPO_ROOT, freshness_signal, iter_markdown_files, load_markdown, repo_relative

TARGET_PATTERN = re.compile(r"`([^`\n]+\.(?:md|json|jsonl))`")


def build_manifest() -> dict[str, dict]:
    manifest: dict[str, dict] = {}
    for path in iter_markdown_files(include_fetched=True, include_generated=True):
        metadata, _ = load_markdown(path)
        freshness_field, freshness_value = freshness_signal(metadata)
        manifest[repo_relative(path)] = {
            "freshness_field": freshness_field,
            "freshness_value": freshness_value,
            "status": metadata.get("status"),
            "title": metadata.get("title"),
        }
    return manifest


def sync_registry(registry_path: Path, manifest: dict[str, dict]) -> None:
    lines = registry_path.read_text(encoding="utf-8").splitlines()
    updated_lines: list[str] = []
    for line in lines:
        match = TARGET_PATTERN.search(line)
        if not match or "| Last Fetched |" in line:
            updated_lines.append(line)
            continue

        target = match.group(1)
        freshness_value = manifest.get(target, {}).get("freshness_value", "—") or "—"
        cells = line.split("|")
        if len(cells) >= 3:
            cells[-2] = f" {freshness_value} "
            line = "|".join(cells)
        updated_lines.append(line)

    registry_path.write_text("\n".join(updated_lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync freshness metadata into registry outputs")
    parser.add_argument(
        "--registry",
        default="meta/standards-registry.md",
        help="Registry markdown file to update",
    )
    parser.add_argument(
        "--manifest",
        default="meta/freshness-manifest.json",
        help="Structured freshness manifest output path",
    )
    args = parser.parse_args()

    registry_path = REPO_ROOT / args.registry
    manifest_path = REPO_ROOT / args.manifest
    manifest_path.parent.mkdir(parents=True, exist_ok=True)

    manifest = build_manifest()
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")

    if registry_path.exists():
        sync_registry(registry_path, manifest)

    print(f"Freshness manifest written to {repo_relative(manifest_path)}")
    if registry_path.exists():
        print(f"Synchronized freshness values in {repo_relative(registry_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
