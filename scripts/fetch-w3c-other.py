#!/usr/bin/env python3
"""
Fetch other W3C standards (ATAG 2.0, UAAG 2.0, EPUB Accessibility 1.1,
WebVTT, COGA design guide, alt text decision tree, EPUB metadata).

Delegates to fetch-standards.py --w3c-other. Additional flags are passed through.

Usage:
  python scripts/fetch-w3c-other.py
  python scripts/fetch-w3c-other.py --delay 3
  python scripts/fetch-w3c-other.py --source atag-2.0

See meta/update-schedule.md for cadence.
See meta/standards-registry.md for source URLs and target files.
"""

import subprocess
import sys
from pathlib import Path

FETCH_STANDARDS = Path(__file__).parent / "fetch-standards.py"


def main():
    args = sys.argv[1:]
    group_flags = {"--all", "--wcag", "--aria", "--us-gov"}
    has_group = any(a in group_flags for a in args) or any(a == "--source" for a in args)

    if not has_group:
        args = ["--w3c-other"] + args

    result = subprocess.run(
        [sys.executable, str(FETCH_STANDARDS)] + args
    )
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
