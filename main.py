#!/usr/bin/env python3
"""Warning Label for Humans — one-line safety warning label entry.

Writes the label to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to an
output/ directory next to this script when the variable is unset), so the
grader can read it in its read-only sandbox.
"""

import os

LABEL = "CAUTION: Do not shake. Contents settle emotionally, leak from the eyes if tilted, and may explode if asked 'are you okay?' twice."

def main() -> None:
    text = LABEL.strip()
    if not 1 <= len(text) <= 160:
        raise SystemExit(f"entry must be 1-160 characters, got {len(text)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
