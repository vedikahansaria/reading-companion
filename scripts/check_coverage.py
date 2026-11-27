#!/usr/bin/env python3
"""Count how many books carry each theme in the vocabulary.

Usage:
    python3 scripts/check_coverage.py                 # books.csv only
    python3 scripts/check_coverage.py --with-proposed # books.csv plus docs/proposed-books.md
    python3 scripts/check_coverage.py --min 3         # change the threshold (default 2)
    python3 scripts/check_coverage.py --strict        # exit with an error if any theme is short

Themes with fewer than --min books are flagged. Tags that are not in the
vocabulary are listed too, because they cannot link to anything.
"""
import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VOCAB = ROOT / "docs" / "theme-vocabulary.md"
BOOKS = ROOT / "data" / "books.csv"
PROPOSED = ROOT / "docs" / "proposed-books.md"


def load_vocabulary():
    """Return themes in file order, grouped by family heading."""
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


def split_tags(value):
    return [t.strip() for t in value.split(";") if t.strip()]


def load_books():
    with BOOKS.open(newline="", encoding="utf-8") as f:
        return [(r["title"], split_tags(r["themes"])) for r in csv.DictReader(f)]


def load_proposed():
    """Read the table in proposed-books.md: the 'Title' column and the first column starting with 'Themes'."""
    books, header = [], None
    for line in PROPOSED.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            header = None if not line.strip() else header
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header = [c.lower() for c in cells]
            continue
        if set(line) <= set("|-: "):
            continue
        themes_col = next((i for i, h in enumerate(header) if h.startswith("themes")), None)
        if "title" in header and themes_col is not None:
            title = re.sub(r"[*_]", "", cells[header.index("title")])
            tags = cells[themes_col].replace("`", "").replace(",", ";")
            books.append((title, split_tags(tags)))
    return books


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--min", type=int, default=2, help="minimum books per theme (default 2)")
    parser.add_argument("--with-proposed", action="store_true", help="also count docs/proposed-books.md")
    parser.add_argument("--strict", action="store_true", help="exit 1 if any theme is below --min")
    args = parser.parse_args()

    families = load_vocabulary()
    vocab = {t for themes in families.values() for t in themes}
    books = load_books()
    sources = {"books.csv": books}
    if args.with_proposed:
        sources["proposed"] = load_proposed()

    counts = {name: defaultdict(int) for name in sources}
    unknown = defaultdict(set)
    for name, rows in sources.items():
        for title, themes in rows:
            for t in themes:
                if t in vocab:
                    counts[name][t] += 1
                else:
                    unknown[t].add(title)

    total_books = sum(len(rows) for rows in sources.values())
    print(f"{len(vocab)} themes, {total_books} books "
          + ", ".join(f"({len(r)} from {n})" for n, r in sources.items()))
    print()
    cols = list(sources)
    print(f"{'theme':<22}" + "".join(f"{c:>11}" for c in cols) + f"{'total':>8}")
    short = []
    for family, themes in families.items():
        print(f"-- {family}")
        for t in themes:
            per = [counts[c][t] for c in cols]
            total = sum(per)
            flag = "  <-- needs more" if total < args.min else ""
            if flag:
                short.append((t, total))
            print(f"{t:<22}" + "".join(f"{n:>11}" for n in per) + f"{total:>8}{flag}")

    print()
    if short:
        print(f"{len(short)} theme(s) have fewer than {args.min} books:")
        for t, n in short:
            print(f"  {t} ({n})")
    else:
        print(f"Every theme has at least {args.min} books.")

    if unknown:
        print()
        print("Tags not in the vocabulary:")
        for t, titles in sorted(unknown.items()):
            print(f"  {t!r} in: {', '.join(sorted(titles))}")

    if args.strict and (short or unknown):
        sys.exit(1)


if __name__ == "__main__":
    main()
