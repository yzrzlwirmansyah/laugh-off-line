#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Chosen line: the cleanest single-turn literalization -- "boundaries"
turned into a literal fence. One image, lands instantly on a cold read.
"""

import os
import sys
from pathlib import Path

LINE = "My therapist said to set boundaries, so I put a little fence around my unresolved issues."


def main() -> int:
    # Reject empty, overlong, multi-line, or padded lines: leading/trailing
    # whitespace would pass the other checks yet waste characters and look
    # sloppy, so the line must already be in its stripped form.
    if (
        not LINE.strip()
        or LINE != LINE.strip()
        or len(LINE) > 200
        or "\r" in LINE
        or "\n" in LINE
    ):
        print("invalid line: empty, padded, overlong, or multi-line", file=sys.stderr)
        return 2
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
