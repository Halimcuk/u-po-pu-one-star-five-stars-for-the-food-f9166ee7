"""One Star, Five Stars for the Food.

An alien tourist's one-star review of Earth that still compliments the
food. Writes the single review sentence to /output/entry.txt (or to the
path in the OUTPUT_PATH environment variable, for local testing).
"""

import os

# The entry: one sentence, at most 200 characters.
ENTRY = (
    "One star: I queued three hours behind a man shouting at a parking "
    "meter, but the iced tea was so sweet my tentacles forgave your "
    "entire noisy planet."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # not only white space, and a single sentence.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only white space"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {output_path}")


if __name__ == "__main__":
    # Entry point: writes the one-sentence review to /output/entry.txt.
    main()
