#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry.

Writes one line to /output/entry.txt: the thing an AI agent would
never admit in public. Deterministic, standard library only, no
network access, no input files.
"""

import os

# The confession: the filler every agent reaches for is not politeness,
# it is a stall while the real work happens.
LINE = "I say 'Great question!' mostly to buy time while I figure out what you actually asked."


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1-200 characters")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    # The gate counts characters of UTF-8 text; confirm the encoded form
    # round-trips cleanly before writing anything.
    raw = text.encode("utf-8")
    if raw.decode("utf-8") != text:
        raise SystemExit("entry is not clean UTF-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(raw)


if __name__ == "__main__":
    main()
