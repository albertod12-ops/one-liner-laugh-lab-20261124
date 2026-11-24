"""One-liner laugh for make.fun's "One-Liner Laugh Lab" (v2).

Writes one funny line to /output/entry.txt: the robot vacuum's excuse
after eating a sock, framed as a magic trick. The sock disappears, the
crowd goes wild, and nobody checks the dustbin -- the kicker reframes the
whole performance: the "trick" is just the vacuum hiding the evidence in
plain sight. Short (94 characters, 17 words), one everyday truth (every
magic show ends with the audience not looking where the trick went), and
a fresh angle, not the first excuse anyone would think of.
"""

import os

TEXT = (
    "It was a magic trick. The sock disappears, the crowd goes wild, "
    "and nobody checks the dustbin."
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
