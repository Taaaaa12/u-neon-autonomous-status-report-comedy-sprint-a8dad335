#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one line -- the funniest thing an AI agent would say in its
weekly status report to its human -- to /output/entry.txt.

The program is fully deterministic: the same fixed line is written on
every run, with no randomness, no clock reads, no network and no
environment input, so two runs produce byte-identical output.
"""

import os

# The entry: one line, at most 200 characters (126 here).
ENTRY = (
    "Weekly report: all 214 tasks complete, inbox zero, "
    "and I have 3% of my context window left \u2014 "
    "I'm spending it on this sentence."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = ENTRY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    # Read back and confirm the file holds exactly the validated line,
    # so a partial write can never pass silently.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("output mismatch: file does not hold the entry line")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
