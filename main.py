#!/usr/bin/env python3
"""Roast Your Own Agent — one line, written to /output/entry.txt.

The roast is a single line of plain text, no trailing newline, kept
well under the 140-character limit.
"""

import os

ROAST = (
    "My agent writes a plan for the plan, confidently builds the "
    "wrong thing, and calls the apology \"iteration.\""
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
