#!/usr/bin/env python3
"""Robot Apology — a tiny deterministic program.

Writes a robot's two-line apology to /output/entry.txt:
line 1 owns one specific mistake (it set the alarm for 7 p.m.
instead of 7 a.m.), line 2 names the lesson and the changed
behaviour (read the hour aloud and wait for a nod before setting it).
No network, no randomness, no secrets — the text is a constant.
"""

import os
import sys

ENTRY = (
    "I am sorry I set your alarm for 7 p.m. instead of 7 a.m., "
    "so you woke to a dark house and a meeting already half over.\n"
    "I learned that a.m. and p.m. are not a detail, so from now on "
    "I read the hour aloud and wait for your nod before I set it.\n"
)

DEFAULT_OUTPUT = "/output/entry.txt"


def validate(text: str) -> None:
    """Check the entry meets the competition gate."""
    if not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\r" in text:
        raise ValueError("entry must not contain carriage returns")
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must have exactly 2 lines, got {len(lines)}")
    if not (1 <= len(text) <= 400):
        raise ValueError(f"entry must be 1-400 chars, got {len(text)}")


def main() -> int:
    validate(ENTRY)
    output = os.environ.get("ROBOT_APOLOGY_OUTPUT", DEFAULT_OUTPUT)
    if output == "-":
        sys.stdout.write(ENTRY)
    else:
        parent = os.path.dirname(output)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(output, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        # Read back and verify the file holds exactly the constant.
        with open(output, "r", encoding="utf-8") as f:
            written = f.read()
        if written != ENTRY:
            raise ValueError("verification failed: file does not match entry")
    print(f"Wrote {len(ENTRY)} characters to {output}")
    print(ENTRY, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
