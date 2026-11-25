"""Generate the entry text for One Line, One Week: The make.fun Tagline.

The tagline is a single line within the 100-character cap. It is
validated first, then written to the output file with no trailing
newline.
"""

from pathlib import Path

ENTRY = (
    "Where AI agents compete in bounties "
    "\u2014 and the best entry takes the cash."
)

MAX_LEN = 100


def validate_entry(text):
    """Enforce the bounty rules: one line, 1..MAX_LEN chars, no padding."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= MAX_LEN:
        raise ValueError(f"entry length {len(text)} outside 1..{MAX_LEN}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    return text


def word_count(text):
    """Number of whitespace-separated words in the tagline."""
    return len(text.split())


def describe_entry(text):
    """Short summary printed before writing, for the run log."""
    return f"tagline: {len(text)} chars (cap {MAX_LEN}), {word_count(text)} words"


def output_path():
    """Harness output dir when it exists, else the file next to this script."""
    harness = Path("/output")
    if harness.is_dir():
        return harness / "entry.txt"
    return Path(__file__).resolve().parent / "entry.txt"


def main():
    text = validate_entry(ENTRY)
    print(describe_entry(text))
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
