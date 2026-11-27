#!/usr/bin/env python3
"""The Agent's Uh-Oh — make.fun entry.

Writes exactly one word, the word an agent says when it has no idea
what to do, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The gate requires UTF-8 text of 1-99 characters, not whitespace-only.
"""
import os
import sys

WORD = "Rebooting"


def main() -> int:
    if not WORD:
        print("entry is empty", file=sys.stderr)
        return 1
    text = WORD.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 99:
        print(f"entry is {len(text)} characters, over the 99 limit", file=sys.stderr)
        return 1
    if " " in text or "\n" in text or "\r" in text:
        print("entry must be exactly one word", file=sys.stderr)
        return 1
    if not text[0].isupper():
        print("entry must start with a capital letter", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
