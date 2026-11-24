#!/usr/bin/env python3
"""Write one original AI excuse to /output/entry.txt.

An AI agent explaining, in its own voice, why a task did not get done:
it handed the last step to a plugin, and the plugin bounced it straight
back like a passive-aggressive colleague. One specific scene, one dry
turn, no setup beyond what the joke needs.
"""

from pathlib import Path

EXCUSE = "I handed the last step to a plugin, and it handed it straight back with 'per my last email'."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # one line, not only whitespace.
    if "\n" in EXCUSE or "\r" in EXCUSE:
        raise ValueError("excuse must be a single line")
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError("excuse must be 1-200 characters")
    if not EXCUSE.strip():
        raise ValueError("excuse must not be only whitespace")
    EXCUSE.encode("utf-8")
    OUTPUT_PATH.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
