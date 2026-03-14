#!/usr/bin/env python3
"""
Fetch WCAG standards (2.1, 2.2, 3.0 overview, quick refs, techniques, understanding docs).

Delegates to fetch-standards.py --wcag. Additional flags are passed through.

Usage:
  python scripts/fetch-wcag.py
  python scripts/fetch-wcag.py --delay 3
  python scripts/fetch-wcag.py --source wcag-2.2

See meta/update-schedule.md for cadence.
See meta/standards-registry.md for source URLs and target files.
"""

import subprocess
import sys
from pathlib import Path

FETCH_STANDARDS = Path(__file__).parent / "fetch-standards.py"


def main():
    # If no flag that overrides the group is given, inject --wcag
    args = sys.argv[1:]
    group_flags = {"--all", "--aria", "--w3c-other", "--us-gov"}
    has_group = any(a in group_flags for a in args) or any(a == "--source" for a in args)

    if not has_group:
        args = ["--wcag"] + args

    result = subprocess.run(
        [sys.executable, str(FETCH_STANDARDS)] + args
    )
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
