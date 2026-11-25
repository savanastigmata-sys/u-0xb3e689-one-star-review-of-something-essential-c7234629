"""One-Star Review of Something Essential.

Writes a single-line, deadpan one-star review (at most 160 characters)
of an everyday essential to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

MAX_CHARS = 160

REVIEW = (
    "One star. Sleep demands eight hours a night, every night, "
    "no rollover minutes, and still fines you a headache if you pay late."
)


def resolve_output_dir():
    """Return the grader output dir, falling back to ./output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output"
    )


def validate(text):
    """Enforce the brief: 1-160 chars, one line, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("review must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            "review must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if not text.strip():
        raise ValueError("review must not be only whitespace")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("review must not contain control characters")
    return text


# Fail fast at import time if the review ever breaks the brief.
REVIEW = validate(REVIEW)


def main():
    text = validate(REVIEW)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            raise ValueError("written entry.txt does not match the review")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
