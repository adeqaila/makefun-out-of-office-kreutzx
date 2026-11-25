#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry (slot 1).

Writes exactly one funny out-of-office line to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads
(except MAKEFUN_OUTPUT_DIR, which the grader sets to /output).

The line (123 chars, one line, first-person auto-reply voice):
an away-until-Monday reply that asks the sender to consider the
email read, understood and emotionally processed — then confesses
it was none of those things. A real OOO frame with a reversal
twist at the end; no worn cat/dog/houseplant-guards-the-inbox,
no "inbox is in charge", no "gone to find myself" trope.
"""

import os

LINE = (
    "I'm away until Monday. Please consider this email read, "
    "understood, and emotionally processed. "
    "It was none of those things."
)

# Grader sets MAKEFUN_OUTPUT_DIR=/output; default matches the rules.
OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def _check(line: str) -> None:
    """House gate: UTF-8 text, one line, 1-140 chars, not blank."""
    assert "\n" not in line, "line must be a single line"
    assert 1 <= len(line) <= 140, "line must be 1-140 chars"
    assert line.strip(), "line must not be blank only"


def main() -> None:
    _check(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
