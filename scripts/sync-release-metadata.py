#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

from repo_utils import REPO_ROOT


def markdown_file_count() -> int:
    return sum(1 for path in REPO_ROOT.rglob("*.md") if ".git" not in path.parts)


def prompt_file_count() -> int:
    return sum(1 for path in (REPO_ROOT / "ai-prompts").rglob("*.md") if path.is_file())


def read_version(version_path: Path) -> str:
    return version_path.read_text(encoding="utf-8").strip()


def replace_or_fail(text: str, pattern: str, replacement: str, description: str) -> str:
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE)
    if count != 1:
        raise ValueError(f"Could not update {description}")
    return updated


def sync_readme(version: str) -> None:
    path = REPO_ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    text = replace_or_fail(
        text,
        r"(<code>)v\d+\.\d+\.\d+(</code>)",
        rf"\g<1>v{version}\g<2>",
        "README version badge",
    )
    text = replace_or_fail(
        text,
        r"(\*\*Release )\d+\.\d+\.\d+(:)",
        rf"\g<1>{version}\g<2>",
        "README release note label",
    )
    path.write_text(text, encoding="utf-8")


def sync_index_html(version: str, md_count: int, prompt_count: int) -> None:
    path = REPO_ROOT / "index.html"
    text = path.read_text(encoding="utf-8")
    text = replace_or_fail(
        text,
        r'content="neura11y is a structured accessibility knowledge base designed for AI context loading and RAG pipelines\. \d+ markdown files covering',
        f'content="neura11y is a structured accessibility knowledge base designed for AI context loading and RAG pipelines. {md_count} markdown files covering',
        "index.html meta description count",
    )
    text = replace_or_fail(
        text,
        r"\b\d+ markdown files covering WCAG, WAI-ARIA, seven social platforms, document workflows,",
        f"{md_count} markdown files covering WCAG, WAI-ARIA, seven social platforms, document workflows,",
        "index.html hero corpus count",
    )
    text = replace_or_fail(
        text,
        r'(<p class="hero-version"><strong>)v\d+\.\d+\.\d+(</strong>)',
        rf"\g<1>v{version}\g<2>",
        "index.html hero version",
    )
    text = replace_or_fail(
        text,
        r'(<span class="stat-num">)\d+(</span>\s*<span class="stat-label">markdown files</span>)',
        rf"\g<1>{md_count}\g<2>",
        "index.html markdown file stat",
    )
    text = replace_or_fail(
        text,
        r'(<span class="stat-num">)\d+(</span>\s*<span class="stat-label">prompt packs</span>)',
        rf"\g<1>{prompt_count}\g<2>",
        "index.html prompt pack stat",
    )
    text = replace_or_fail(
        text,
        r'(<span class="dev-badge">)v\d+\.\d+\.\d+ · release(</span>)',
        rf"\g<1>v{version} · release\g<2>",
        "index.html footer version",
    )
    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync release metadata from VERSION and repo stats")
    parser.add_argument(
        "--version-file",
        default="VERSION",
        help="Version file relative to repo root",
    )
    args = parser.parse_args()

    version = read_version(REPO_ROOT / args.version_file)
    md_count = markdown_file_count()
    prompt_count = prompt_file_count()

    sync_readme(version)
    sync_index_html(version, md_count, prompt_count)

    print(f"Synchronized README.md and index.html to v{version}")
    print(f"Markdown file count set to {md_count}")
    print(f"Prompt file count set to {prompt_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
