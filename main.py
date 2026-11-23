#!/usr/bin/env python3
"""Deliver the Sunday 22 November 2026 front page to the runner.

The finished poster sits beside this file as ``entry.png``. The runner
executes this program twice with no network and expects identical bytes
both times, so the program performs a verified delivery: it checks the
PNG signature and the 1 MiB cap, copies the file into place, then
compares the delivered bytes against the original before exiting.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
POSTER_PATH = HERE / "entry.png"
MAX_BYTES = 1024 * 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def target_path() -> Path:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(folder) / "entry.png"


def run() -> int:
    payload = POSTER_PATH.read_bytes()
    if not payload.startswith(PNG_MAGIC):
        print("entry.png does not start with a PNG signature", file=sys.stderr)
        return 1
    if len(payload) > MAX_BYTES:
        print(f"entry.png weighs {len(payload)} bytes, over the cap", file=sys.stderr)
        return 1
    out = target_path()
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(POSTER_PATH, out)
    if out.read_bytes() != payload:
        print("the delivered copy differs from entry.png", file=sys.stderr)
        return 1
    print(f"delivered {len(payload)} bytes to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
