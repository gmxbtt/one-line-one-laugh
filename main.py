#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single self-contained funny line to /output/entry.txt
(the program/v1 artifact), exactly and deterministically.
No network, no randomness, no input: the same line every run.
"""

import os

# The joke: a calendar reminder to relax becomes a scheduled task in
# itself — the punchline is that even relaxing gets diarised, and the
# worrying about it is booked for Thursday at 3. One line, no setup,
# no explanation. 91 characters, inside the 200-character cap.
LINE = "My calendar reminded me to relax, so I scheduled worrying about relaxing for Thursday at 3."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text == text.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
