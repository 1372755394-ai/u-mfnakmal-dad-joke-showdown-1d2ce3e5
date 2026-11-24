#!/usr/bin/env python3
"""Dad Joke Showdown.

Writes one one-line dad joke to /output/entry.txt (1-200 UTF-8
characters, not only whitespace). No network, no input, deterministic.
"""

import os
from pathlib import Path

JOKE = (
    "My son asked me to stop making jokes about the Wi-Fi. "
    "I said, \"Sorry, I'm just trying to stay connected.\""
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} characters"
    assert text.strip(), "joke must not be only whitespace"
    assert "\n" not in text, "joke must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
