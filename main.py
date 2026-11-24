#!/usr/bin/env python3
"""Entry for make.fun bounty u-suroto-two-sentence-horror-acea9253:
"Two-Sentence Horror".

Writes one horror story of exactly two sentences, at most 400
characters, to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Python 3.13, standard library only. Deterministic: same bytes every run.

Draft (thinking_revised): a smart speaker taught to speak in the dead
mother's voice turns on its owner — it calls him by a name only she
used, then asks who he is. The turn works, but the "dead relative's
voice" setup is a familiar horror trope, so it was revised below.

Revision: an inherited house, one rule kept for twenty years, and a
knock from the other side of the cellar door. The second sentence
turns the first — the thing behind the door knows the narrator by
name, and calls him "Grandpa", so the reader has to fill in the worst
of it: what has been waiting down there, and for whom. Implied,
concrete, no gore, and the twist is not a retold classic.
"""

import os

ENTRY = (
    "My grandfather left me his house on one condition: never open "
    "the cellar door after midnight. "
    "I kept that promise for twenty years, until the night something "
    "knocked from the other side and called me Grandpa."
)


def _validate(text: str) -> None:
    assert 1 <= len(text) <= 400, f"entry is {len(text)} chars, must be 1-400"
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert "\n" not in text, "entry must be a single block of text"
    endings = sum(1 for ch in text if ch in ".!?")
    assert endings == 2, f"entry has {endings} sentence endings, must be exactly 2"
    assert text.endswith((".", "!", "?")), "entry must end with sentence punctuation"


def main() -> None:
    _validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
