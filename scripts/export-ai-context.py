#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from repo_utils import GENERATED_DATA_FILES, REPO_ROOT, chunk_markdown_file, iter_markdown_files, repo_relative


def main() -> int:
    parser = argparse.ArgumentParser(description="Export chunked AI context for RAG ingestion")
    parser.add_argument(
        "--output",
        default="meta/chunk-manifest.jsonl",
        help="JSONL output path relative to repo root",
    )
    parser.add_argument(
        "--summary",
        default="meta/chunk-manifest-summary.json",
        help="Summary JSON output path relative to repo root",
    )
    parser.add_argument("--min-tokens", type=int, default=100, help="Minimum chunk size")
    parser.add_argument("--max-tokens", type=int, default=512, help="Maximum chunk size")
    parser.add_argument("--overlap", type=int, default=50, help="Overlap between chunk splits")
    parser.add_argument(
        "--include-fetched",
        action="store_true",
        help="Include raw *-fetched.md files",
    )
    args = parser.parse_args()

    output_path = REPO_ROOT / args.output
    summary_path = REPO_ROOT / args.summary
    output_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.parent.mkdir(parents=True, exist_ok=True)

    chunks: list[dict] = []
    files_processed = 0
    status_counts: Counter[str] = Counter()
    top_level_counts: Counter[str] = Counter()

    for path in iter_markdown_files(include_fetched=args.include_fetched):
        rel_path = repo_relative(path)
        if rel_path in GENERATED_DATA_FILES:
            continue
        file_chunks = chunk_markdown_file(
            path,
            min_tokens=args.min_tokens,
            max_tokens=args.max_tokens,
            overlap_tokens=args.overlap,
        )
        if not file_chunks:
            continue
        files_processed += 1
        top_level_counts[Path(rel_path).parts[0]] += 1
        status_counts[file_chunks[0]["status"] or "unknown"] += 1
        chunks.extend(file_chunks)

    with output_path.open("w", encoding="utf-8") as handle:
        for chunk in chunks:
            handle.write(json.dumps(chunk, ensure_ascii=True) + "\n")

    summary = {
        "files_processed": files_processed,
        "chunks_exported": len(chunks),
        "min_tokens": args.min_tokens,
        "max_tokens": args.max_tokens,
        "overlap": args.overlap,
        "status_counts": dict(sorted(status_counts.items())),
        "top_level_counts": dict(sorted(top_level_counts.items())),
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")

    print(
        f"Exported {len(chunks)} chunks from {files_processed} files to {repo_relative(output_path)}"
    )
    print(f"Summary written to {repo_relative(summary_path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
