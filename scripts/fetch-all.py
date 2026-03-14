#!/usr/bin/env python3
"""
Run all fetch scripts in sequence to refresh the entire standards knowledge base.

Scripts run in order:
  1. fetch-wcag.py       — WCAG 2.1, 2.2, 3.0 overview, quick refs
  2. fetch-aria.py       — WAI-ARIA 1.2, ARIA in HTML
  3. fetch-w3c-other.py  — ATAG, UAAG, EPUB, COGA, alt text tree
  4. fetch-us-gov.py     — Section 508, Plain Language
  5. fetch-en-301-549.py — EN 301 549 PDF (requires pdfplumber)
  6. fetch-iso.py        — PDF/UA summary, Matterhorn Protocol

Usage:
  python scripts/fetch-all.py
  python scripts/fetch-all.py --delay 3
  python scripts/fetch-all.py --skip en-301-549   # Skip a slow/unavailable script
  python scripts/fetch-all.py --only wcag aria    # Run specific scripts only
  python scripts/fetch-all.py --log meta/fetch-log.md  # Append results to fetch log

See meta/update-schedule.md for recommended cadence per script.
"""

import argparse
import datetime
import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent
REPO_ROOT = SCRIPTS_DIR.parent

# Ordered list of (key, script filename)
ALL_SCRIPTS = [
    ("wcag",         "fetch-wcag.py"),
    ("aria",         "fetch-aria.py"),
    ("w3c-other",    "fetch-w3c-other.py"),
    ("us-gov",       "fetch-us-gov.py"),
    ("en-301-549",   "fetch-en-301-549.py"),
    ("iso",          "fetch-iso.py"),
]


def run_script(key: str, script: str, delay: float) -> tuple[bool, str]:
    """Run a single fetch script. Returns (success, output)."""
    script_path = SCRIPTS_DIR / script
    if not script_path.exists():
        return False, f"Script not found: {script_path}"

    cmd = [sys.executable, str(script_path), "--delay", str(delay)]
    print(f"\n{'─' * 60}")
    print(f"Running: {script}")
    print(f"{'─' * 60}")

    result = subprocess.run(cmd, capture_output=False)
    success = result.returncode == 0
    return success, script


def append_fetch_log(log_path: Path, results: list[dict]) -> None:
    """Append fetch results to meta/fetch-log.md."""
    if not log_path.exists():
        print(f"  WARNING: Log file not found: {log_path}")
        return

    timestamp = datetime.datetime.now().isoformat(timespec="seconds")
    lines = [f"\n### fetch-all run — {timestamp}\n"]
    for r in results:
        status = "success" if r["success"] else "failed"
        lines.append(f"| {r['key']:15s} | {r['script']:25s} | {status} | — |")

    with log_path.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"\nFetch log updated: {log_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Run all accessibility standards fetch scripts"
    )
    parser.add_argument(
        "--delay", type=float, default=2.0,
        help="Delay between HTTP requests in seconds (default: 2)"
    )
    parser.add_argument(
        "--skip", nargs="+", metavar="KEY",
        choices=[k for k, _ in ALL_SCRIPTS],
        help="Skip one or more scripts by key (e.g. --skip en-301-549 iso)"
    )
    parser.add_argument(
        "--only", nargs="+", metavar="KEY",
        choices=[k for k, _ in ALL_SCRIPTS],
        help="Run only specific scripts by key (e.g. --only wcag aria)"
    )
    parser.add_argument(
        "--log", type=str, metavar="PATH",
        help="Append results to a fetch log file (e.g. meta/fetch-log.md)"
    )
    parser.add_argument(
        "--list", action="store_true",
        help="List all scripts that will be run"
    )
    args = parser.parse_args()

    # Resolve script list
    scripts_to_run = ALL_SCRIPTS[:]
    if args.only:
        scripts_to_run = [(k, s) for k, s in scripts_to_run if k in args.only]
    if args.skip:
        scripts_to_run = [(k, s) for k, s in scripts_to_run if k not in args.skip]

    if args.list:
        print("Scripts to run:")
        for key, script in scripts_to_run:
            path = SCRIPTS_DIR / script
            exists = "✓" if path.exists() else "✗ (missing)"
            print(f"  {key:15s}  {script}  {exists}")
        return

    print(f"fetch-all: running {len(scripts_to_run)} script(s) with {args.delay}s delay")
    print(f"Started: {datetime.datetime.now().isoformat(timespec='seconds')}")

    results = []
    for key, script in scripts_to_run:
        success, info = run_script(key, script, args.delay)
        results.append({"key": key, "script": script, "success": success})

    # Summary
    succeeded = [r for r in results if r["success"]]
    failed = [r for r in results if not r["success"]]

    print(f"\n{'=' * 60}")
    print(f"fetch-all complete: {len(succeeded)} succeeded, {len(failed)} failed")
    if failed:
        print(f"Failed scripts: {', '.join(r['key'] for r in failed)}")
        print("Re-run individual scripts to diagnose. See meta/fetch-log.md.")

    # Optional log update
    if args.log:
        log_path = REPO_ROOT / args.log
        append_fetch_log(log_path, results)

    sys.exit(0 if not failed else 1)


if __name__ == "__main__":
    main()
