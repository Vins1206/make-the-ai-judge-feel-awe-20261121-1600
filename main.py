"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt. The text was chosen by
drafting six candidates and scoring each against the judge brief in
the kit RULES.txt (a relaxation judge: relaxes, shows rather than
instructs, craft/rhythm, dwarfs the reader, freshness). The winner
is a slow tide image: concrete, unhurried, no instructions, and a
thought that keeps growing after the last line.
"""

import os

TEXT = (
    "The tide comes in over the flat sand, a thin sheet of light "
    "that erases each footprint as it goes. Gulls settle. The sea "
    "has done this a thousand evenings, and will do it a thousand "
    "more. The shore keeps no count."
)


def main() -> None:
    # Gate: the entry must be 1-280 Unicode code points, not only whitespace.
    if not (1 <= len(TEXT) <= 280 and TEXT.strip()):
        raise ValueError("entry text outside 1-280 character gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
