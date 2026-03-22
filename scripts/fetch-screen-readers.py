#!/usr/bin/env python3
"""
Fetch vendor screen reader support docs (NVDA, VoiceOver, TalkBack, JAWS).

Delegates to fetch-standards.py --screen-readers. Additional flags are passed through.

Usage:
  python scripts/fetch-screen-readers.py
  python scripts/fetch-screen-readers.py --delay 3
  python scripts/fetch-screen-readers.py --source nvda-user-guide
"""

import subprocess
import sys
from pathlib import Path

FETCH_STANDARDS = Path(__file__).parent / "fetch-standards.py"


def main():
    args = sys.argv[1:]
    group_flags = {"--all", "--wcag", "--aria", "--w3c-other", "--screen-readers", "--us-gov"}
    has_group = any(a in group_flags for a in args) or any(a == "--source" for a in args)

    if not has_group:
        args = ["--screen-readers"] + args

    result = subprocess.run([sys.executable, str(FETCH_STANDARDS)] + args)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
