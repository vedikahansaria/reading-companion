## Reading companion
Most book recommenders recommend books similar to what you just read. This one asks a different question: where are you now, and what do you need next?

In some cases, it’s more of the same. Sometimes, it is the next step in your journey.

## Status
Public build. Phase 1: seed catalogue of books tagged by theme, tone and reader need served by each book.

## How the catalog works
- **`data/books.csv`**: one row per book. Each row describes:
  - what the book is about (`themes`)
  - how it feels to read (`tone`)
  - what it gives a reader (`needs`)
  - where a reader might be before picking it up (`leads_from`)
  - which themes they might be ready for after it (`leads_to`)
- **`docs/theme-vocabulary.md`**: the fixed list of themes. `themes` and `leads_to` use only these words, so books can be linked to each other.
- **`data/theme_journeys.csv`**: links one theme to another, with the kind of move (stay, deepen, move forward or contrast) and a one-line reason.
- **`docs/tagging-guide.md`**: explains every field and how to tag a new book.
- **`scripts/check_coverage.py`**: counts how many books carry each theme and flags themes with fewer than 2. Run `python3 scripts/check_coverage.py`, or add `--with-proposed` to include `docs/proposed-books.md`.

To find a next book, start from the book a reader just finished. Look up its `leads_to` themes, or follow a journey from one of its themes. Then pick books whose `themes` match, and use `needs`, `tone` and `content_notes` to choose the one that fits where the reader is now.

## Why I'm building this
46 readers answered my survey. For most of them, the hard part isn’t choosing a book. It's life getting in the way. Write up to follow.
