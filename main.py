"""Monday, Reviewed in One Line — entry program.

Writes a single one-line review of my own Monday to entry.txt under
MAKEFUN_OUTPUT_DIR (default /output). Deterministic, pure stdlib, no
network, no randomness. The line is validated against the sealed gate
before it is written: UTF-8 text, 1 to 200 characters, a single line,
not only white space.
"""

import os

# The entry: a one-line review of my own Monday (151 characters).
ENTRY = (
    "Monday deserves one star: the elevator broke, the coffee machine "
    "filed for divorce, and my 9 a.m. was moved to 8:45 by someone "
    "who hates me personally."
)


def validate(line: str) -> None:
    """Raise ValueError unless the line passes the competition gate."""
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} chars, over the 200-char gate")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")  # raises if not valid UTF-8 text


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the line: no trailing newline, UTF-8, deterministic.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read the file back and confirm what landed on disk is exactly the
    # validated line — a silent write failure must never reach the gate.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("entry.txt on disk does not match the validated line")
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
