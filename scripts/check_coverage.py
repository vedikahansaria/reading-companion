#!/usr/bin/env python3
"""Count how many books in data/books.csv carry each theme in the vocabulary.

Usage:
    python3 scripts/check_coverage.py           # flag themes with fewer than 2 books
    python3 scripts/check_coverage.py --min 3   # change the threshold
    python3 scripts/check_coverage.py --strict  # exit with an error if any theme is short

Tags that are not in docs/theme-vocabulary.md are listed too, because they
cannot link to anything.
"""
import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOCAB = ROOT / "docs" / "theme-vocabulary.md"
BOOKS = ROOT / "data" / "books.csv"


def load_vocabulary():
    """Return {family: [themes]} in the order they appear in the vocabulary."""
    families, current = {}, None
    for line in VOCAB.read_text(encoding="utf-8").splitlines():
        heading = re.match(r"^## (.+)", line)
        if heading:
            current = heading.group(1).strip()
            continue
        row = re.match(r"^\| `([^`]+)` \|", line)
        if row and current:
            families.setdefault(current, []).append(row.group(1))
    return families


def load_books():
    with BOOKS.open(newline="", encoding="utf-8") as f:
        return [
            (r["title"], [t.strip() for t in r["themes"].split(";") if t.strip()])
            for r in csv.DictReader(f)
        ]


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--min", type=int, default=2, help="minimum books per theme (default 2)")
    parser.add_argument("--strict", action="store_true", help="exit 1 if any theme is below --min")
    args = parser.parse_args()

    families = load_vocabulary()
    vocab = {t for themes in families.values() for t in themes}
    books = load_books()

    counts, unknown = Counter(), defaultdict(set)
    for title, themes in books:
        for t in themes:
            if t in vocab:
                counts[t] += 1
            else:
                unknown[t].add(title)

    print(f"{len(vocab)} themes, {len(books)} books\n")
    print(f"{'theme':<22}{'books':>6}")
    short = []
    for family, themes in families.items():
        print(f"-- {family}")
        for t in themes:
            flag = ""
            if counts[t] < args.min:
                flag = "  <-- needs more"
                short.append(t)
            print(f"{t:<22}{counts[t]:>6}{flag}")

    print()
    if short:
        print(f"{len(short)} theme(s) have fewer than {args.min} books: {', '.join(short)}")
    else:
        print(f"Every theme has at least {args.min} books.")

    if unknown:
        print("\nTags not in the vocabulary:")
        for t, titles in sorted(unknown.items()):
            print(f"  {t!r} in: {', '.join(sorted(titles))}")

    if args.strict and (short or unknown):
        sys.exit(1)


if __name__ == "__main__":
    main()
