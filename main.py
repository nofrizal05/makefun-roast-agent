"""Roast Your Own Agent — make.fun entry.

Writes one original roast line about my own AI agent to /output/entry.txt.
Python 3.13 standard library only.
"""

import os

ROAST = (
    "My agent hears 'quick fix' and starts a full renovation: "
    "three hours later, 47 new files, a README, "
    "and the same bug wearing a hat."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
