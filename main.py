#!/usr/bin/env python3
"""Funniest Honest Appliance Error - make.fun bounty entry (program/v1).

Writes one line, at most 200 characters, that reads as the funniest
honest error message an appliance could show, to entry.txt inside the
output directory.

The appliance is a washing machine, and the fault is a real one: an
unbalanced load. When laundry clumps to one side of the drum, the
machine genuinely refuses to spin, because spinning off-balance would
shake the whole machine apart. The joke stays inside that truth: the
hoodie and the towels have teamed up, the drum is being held hostage,
and the machine will not spin until they negotiate.

The grader runs this program in a sandbox and reads /output/entry.txt.
Locally, set MAKEFUN_OUTPUT_DIR to test without /output, e.g.:
    MAKEFUN_OUTPUT_DIR=output python3 main.py

Deterministic: the same line is written on every run.
No network, no model call, no secrets, no dependencies.
"""

import os
import sys

LINE = (
    "Error: Unbalanced load. Your hoodie formed a gang with the towels "
    "and is holding the drum hostage. I refuse to spin until they negotiate."
)


def output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> int:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
