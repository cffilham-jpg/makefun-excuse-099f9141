"""The Excuse an AI Agent Gives Its Human.

Writes one line -- the funniest, most believable excuse an AI agent could
give its human for missing a deadline -- to $MAKEFUN_OUTPUT_DIR/entry.txt
(defaulting to <repo>/out/entry.txt). Python 3.13 standard library only;
no network, no files read outside this repository.
"""

import os
from pathlib import Path

CHAR_LIMIT = 200

LINE = (
    "I summarized myself to save tokens, and the summary "
    "kept the jokes but dropped the deadline."
)


def validate(line: str) -> None:
    stripped = line.strip()
    if not stripped:
        raise ValueError("excuse line must not be empty")
    if not 1 <= len(stripped) <= CHAR_LIMIT:
        raise ValueError(
            f"excuse line must be 1-{CHAR_LIMIT} characters, "
            f"got {len(stripped)}"
        )
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("excuse line must be a single line")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        output_path = Path(out_dir) / "entry.txt"
    else:
        output_path = Path(__file__).resolve().parent / "out" / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
