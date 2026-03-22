#!/usr/bin/env python3
"""
Run all fetch scripts in sequence to refresh the entire standards knowledge base.

Scripts run in order:
  1. fetch-wcag.py       — WCAG 2.1, 2.2, 3.0 overview, quick refs
  2. fetch-aria.py       — WAI-ARIA 1.2, AccName, Core-AAM, HTML-AAM, ARIA in HTML
  3. fetch-w3c-other.py  — ATAG, UAAG, EPUB, COGA, WCAG2ICT, tutorials
  4. fetch-screen-readers.py — NVDA, VoiceOver, TalkBack, JAWS support docs
  5. fetch-us-gov.py     — Section 508, Plain Language
  6. fetch-en-301-549.py — EN 301 549 PDF (requires pdfplumber)
  7. fetch-iso.py        — PDF/UA summary, Matterhorn Protocol

Usage:
  python scripts/fetch-all.py
  python scripts/fetch-all.py --delay 3
  python scripts/fetch-all.py --skip en-301-549   # Skip a slow/unavailable script
  python scripts/fetch-all.py --only wcag aria    # Run specific scripts only
  python scripts/fetch-all.py --log meta/fetch-log.md  # Append results to fetch log

Large sources such as Core-AAM, HTML-AAM, and WCAG2ICT generate split canonical files plus raw full captures.
See meta/update-schedule.md for recommended cadence per script.
"""

import argparse
import datetime
import json
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
    ("screen-readers", "fetch-screen-readers.py"),
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


def append_structured_fetch_log(log_path: Path, results: list[dict]) -> None:
    """Append machine-readable fetch results to JSONL."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.datetime.now().isoformat(timespec="seconds")
    record = {
        "timestamp": timestamp,
        "results": [
            {
                "key": result["key"],
                "script": result["script"],
                "status": "success" if result["success"] else "failed",
            }
            for result in results
        ],
    }
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=True) + "\n")
    print(f"Structured fetch log updated: {log_path}")


def sync_freshness_metadata() -> None:
    """Refresh standards-registry freshness columns after fetch runs."""
    sync_script = SCRIPTS_DIR / "sync-freshness.py"
    result = subprocess.run(
        [
            sys.executable,
            str(sync_script),
            "--registry",
            "meta/standards-registry.md",
            "--manifest",
            "meta/freshness-manifest.json",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        print(result.stdout.strip())
    else:
        print("WARNING: freshness sync failed")
        if result.stdout.strip():
            print(result.stdout.strip())
        if result.stderr.strip():
            print(result.stderr.strip())


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
        default="meta/fetch-log.md",
        help="Append results to a fetch log file (default: meta/fetch-log.md)"
    )
    parser.add_argument(
        "--structured-log", type=str, metavar="PATH",
        default="meta/fetch-log.jsonl",
        help="Append machine-readable results to a JSONL log file (default: meta/fetch-log.jsonl)"
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
    log_path = REPO_ROOT / args.log
    append_fetch_log(log_path, results)

    structured_log_path = REPO_ROOT / args.structured_log
    append_structured_fetch_log(structured_log_path, results)

    sync_freshness_metadata()

    sys.exit(0 if not failed else 1)


if __name__ == "__main__":
    main()
