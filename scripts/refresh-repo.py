#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from repo_utils import REPO_ROOT

SCRIPTS_DIR = REPO_ROOT / "scripts"


def run_step(label: str, command: list[str]) -> None:
    print(f"\n{'=' * 60}")
    print(label)
    print(f"{'=' * 60}")
    result = subprocess.run(command, cwd=REPO_ROOT)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Refresh repository metadata, exports, and validation artifacts"
    )
    parser.add_argument(
        "--with-fetch",
        action="store_true",
        help="Run fetch-all.py before syncing local artifacts",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=2.0,
        help="Delay passed to fetch-all.py when --with-fetch is used",
    )
    parser.add_argument(
        "--include-fetched",
        action="store_true",
        help="Include raw *-fetched.md files in export and validation where supported",
    )
    args = parser.parse_args()

    if args.with_fetch:
        run_step(
            "Fetch all sources",
            [sys.executable, str(SCRIPTS_DIR / "fetch-all.py"), "--delay", str(args.delay)],
        )

    run_step(
        "Sync freshness metadata",
        [sys.executable, str(SCRIPTS_DIR / "sync-freshness.py")],
    )
    run_step(
        "Sync release metadata",
        [sys.executable, str(SCRIPTS_DIR / "sync-release-metadata.py")],
    )

    export_command = [sys.executable, str(SCRIPTS_DIR / "export-ai-context.py")]
    if args.include_fetched:
        export_command.append("--include-fetched")
    run_step("Export AI context", export_command)

    validation_command = [sys.executable, str(SCRIPTS_DIR / "validate-ai-suite.py")]
    run_step("Validate AI suite", validation_command)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
