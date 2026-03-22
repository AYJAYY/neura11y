#!/usr/bin/env python3
"""
Fetch WAI-ARIA standards (WAI-ARIA 1.2, ARIA in HTML, AccName, Core-AAM, HTML-AAM).

Large sources such as Core-AAM and HTML-AAM generate split canonical files plus raw full captures.

Delegates to fetch-standards.py --aria. Additional flags are passed through.

Usage:
  python scripts/fetch-aria.py
  python scripts/fetch-aria.py --delay 3
  python scripts/fetch-aria.py --source wai-aria-1.2

See meta/update-schedule.md for cadence.
See meta/standards-registry.md for source URLs and target files.
"""

import subprocess
import sys
from pathlib import Path

FETCH_STANDARDS = Path(__file__).parent / "fetch-standards.py"


def main():
    args = sys.argv[1:]
    group_flags = {"--all", "--wcag", "--w3c-other", "--screen-readers", "--us-gov"}
    has_group = any(a in group_flags for a in args) or any(a == "--source" for a in args)

    if not has_group:
        args = ["--aria"] + args

    result = subprocess.run(
        [sys.executable, str(FETCH_STANDARDS)] + args
    )
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
