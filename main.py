"""One-liner laugh for make.fun's "One-Liner Laugh Lab" (v1).

Writes one funny line to /output/entry.txt: the robot vacuum's excuse
after eating a sock, framed as a relationship problem. The vacuum and the
sock are in couples therapy, and the sock's complaint is that the vacuum
"swallowed its boundaries" -- a deadpan twist that lands at the very end:
personal boundaries, taken literally, by a machine that eats things off
the floor. Short (78 characters, 15 words), one everyday truth (couples
therapy language everyone recognises), and a fresh angle, not the
first excuse anyone would think of.
"""

import os

TEXT = (
    "The sock and I are in couples therapy now. "
    "It says I swallowed its boundaries."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters, got %d" % len(TEXT)
    assert "\n" not in TEXT, "entry must be a single line"
    # No trailing newline: the gate counts every character of entry.txt,
    # so the file holds exactly the line, nothing else.
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
