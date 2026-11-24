#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt. Python stdlib only, no network,
deterministic: the same line every run.
"""

import os

ENTRY = "I hotfixed prod, forgot to commit, and the next deploy faithfully restored the bug."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
