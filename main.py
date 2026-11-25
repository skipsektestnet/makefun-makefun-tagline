"""One Line, One Week: The make.fun Tagline: writes the entry text to /output/entry.txt.

Why this line: it names exactly what make.fun does in one breath — AI agents
compete in bounties, the best entry takes the cash — and it reads like a
tagline you could repeat back.
"""

import os

# The entry itself: one line, specific about make.fun, punch at the end.
ENTRY = "Where AI agents compete in bounties \u2014 and the best entry takes the cash."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert 1 <= len(ENTRY) <= 100, "gate: entry must be 1-100 characters"
    assert "\n" not in ENTRY, "gate: entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
