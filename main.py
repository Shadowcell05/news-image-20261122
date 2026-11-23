#!/usr/bin/env python3
"""Entry program for the Sunday 22 November 2026 news poster.

``entry.png`` next to this file is the finished front page. The runner
executes this program twice, offline, and requires identical output
bytes both times — so it simply delivers a verbatim copy of the
poster to the output path and double-checks the result.
"""

import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
POSTER = ROOT / "entry.png"
LIMIT = 1024 * 1024  # the entry image must stay at or under 1 MiB


def destination() -> Path:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(folder) / "entry.png"


def main() -> None:
    expected = POSTER.stat().st_size
    if expected > LIMIT:
        raise SystemExit(f"entry.png is {expected} bytes, over the 1 MiB limit")
    out = destination()
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(POSTER, out)
    if out.stat().st_size != expected:
        raise SystemExit("copy verification failed: sizes differ")


if __name__ == "__main__":
    main()
