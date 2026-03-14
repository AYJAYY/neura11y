#!/usr/bin/env python3
"""
Fetch US government accessibility standards (Section 508 technical standards,
Section 508 overview, Federal Plain Language Guidelines).

Delegates to fetch-standards.py --us-gov. Additional flags are passed through.

Usage:
  python scripts/fetch-us-gov.py
  python scripts/fetch-us-gov.py --delay 3
  python scripts/fetch-us-gov.py --source section-508-tech

See meta/update-schedule.md for cadence.
See meta/standards-registry.md for source URLs and target files.
"""

import subprocess
import sys
from pathlib import Path

FETCH_STANDARDS = Path(__file__).parent / "fetch-standards.py"


def main():
    args = sys.argv[1:]
    group_flags = {"--all", "--wcag", "--aria", "--w3c-other"}
    has_group = any(a in group_flags for a in args) or any(a == "--source" for a in args)

    if not has_group:
        args = ["--us-gov"] + args

    result = subprocess.run(
        [sys.executable, str(FETCH_STANDARDS)] + args
    )
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
