#!/usr/bin/env python3
"""Make the Judge Fall in Love in One Line - make.fun entry.

Writes one line of at most 240 characters to /output/entry.txt.
Standard library only, no network, fully deterministic.
"""

import os

# One line, one image: a small nightly ritual, kept even in absence.
LINE = "He folds my side of the blanket back every night, even when I'm already asleep, even when I'm not coming home."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
