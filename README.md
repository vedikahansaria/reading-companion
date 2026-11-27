## Reading companion
Most book recommenders recommend books similar to what you just read. This one asks a different question: where are you now, and what do you need next?

In some cases, it’s more of the same. Sometimes, it is the next step in your journey.

## Status
Public build.

- **Done:** a catalog of 41 books, each tagged by theme, tone, reader need and content notes.
- **Done:** a theme map that links the 32 themes to each other.
- **Next:** recommendation logic that uses the catalog and the theme map to suggest a reader's next book.

## The four moves
From any book, the next one can make one of four moves:

- **Stay:** more of what you just read. A book on the same emotional ground, through a closely related theme.
- **Deepen:** go further into the same subject. Often harder, or more complex.
- **Move forward:** the next step, for when you're ready. For example, from loneliness to finding your people.
- **Contrast:** a change of subject on purpose, to give you relief or a fresh view.

## How the catalog works
To find a next book, start from the book a reader just finished. Look up its `leads_to` themes, or follow a journey from one of its themes. Then pick books whose `themes` match. Use `needs`, `tone` and `content_notes` to choose the one that fits where the reader is now.

## What's in each folder
- **`data/`**
  - `books.csv`: the catalog, one row per book. Each row covers what the book is about (`themes`), how it feels (`tone`), what it gives a reader (`needs`), where a reader might be before it (`leads_from`), what they might be ready for after it (`leads_to`), content notes, and who picked it (`source`).
  - `theme_journeys.csv`: the theme map. Each row links one theme to another, with the move, when a reader is ready for it (`ready_when`) and a one-line reason.
- **`docs/`**
  - `theme-vocabulary.md`: the fixed list of 32 themes. `themes` and `leads_to` use only these words, so books can be linked.
  - `tagging-guide.md`: what every field means, the four moves, and how to tag a new book.
  - `decisions.md`: a log of product decisions and why they were made.
- **`scripts/`**
  - `check_coverage.py`: counts how many books carry each theme and flags any with fewer than 2. Run `python3 scripts/check_coverage.py`.

## Why I'm building this
46 readers answered my survey. For most of them, the hard part isn’t choosing a book. It's life getting in the way. Write up to follow.
