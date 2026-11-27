# Decisions

A log of product decisions and why they were made. Newest decisions are at the bottom. Add a row whenever a decision changes what the catalog holds or how it works.

## Catalog format

| Date | Decision | Why |
|---|---|---|
| 2026-11-27 | Keep the catalog in one CSV file, `data/books.csv`, with one row per book. | Easy to edit by hand or in a spreadsheet, and easy for code to read later. |
| 2026-11-27 | Separate multiple values in a field with semicolons. | Commas already separate the CSV columns. |
| 2026-11-27 | Give every book a stable `id` in lowercase with hyphens. | Titles can be corrected later without breaking links to the book. |
| 2026-11-27 | Record the year of first publication in any language, and put translation dates in `confidence_notes`. | One clear rule for every book, translated or not. |
| 2026-11-27 | Use the published title, *The Forest of Enchantments* (plural), not the title as first requested. | The catalog should match what readers will find in a shop. |
| 2026-11-27 | Mark each row `high` or `low` confidence, and say which tags are uncertain in `confidence_notes`. | Tags were filled in before every book was checked. Low-confidence rows show where to check first. |
| 2026-11-27 | Limit `needs` to six values: comfort, escape, perspective, meaning, inspiration, laughter. | A fixed list lets books be matched on what a reader needs. |
| 2026-11-27 | Set rough length bands: short is under about 250 pages, medium 250 to 450, long over 450. | Page counts vary by edition, so bands are more useful than exact numbers. |
| 2026-11-27 | Name heavy topics in `content_notes`, and leave it empty only if there is truly nothing to flag. | Readers in a hard place need to know what a book contains before they start. |

## Themes

| Date | Decision | Why |
|---|---|---|
| 2026-11-27 | Replace free-text themes with a fixed vocabulary of 32 themes in four families (inner life, relationships, society, work and ambition), in `docs/theme-vocabulary.md`. | Free-text tags did not match each other, so books could not be linked. |
| 2026-11-27 | Merge near duplicates, such as *trauma and healing*, *anxiety* and *abuse* into `mental health`. | Fewer, broader themes give more links between books. |
| 2026-11-27 | Drop `classic literature` as a theme. | It describes a kind of book, not what the book is about. |
| 2026-11-27 | `themes` and `leads_to` use only vocabulary words. `leads_from` stays free text. | `leads_from` describes the reader's situation, not a theme, so it needs its own words. |

## Theme map

| Date | Decision | Why |
|---|---|---|
| 2026-11-27 | Link themes in `data/theme_journeys.csv` with one of four moves: stay, deepen, move forward, contrast. | The next book can stay on the same ground, go deeper, take the next step or offer a contrast. The map makes each option explicit. |
| 2026-11-27 | Don't list a theme leading to itself. | A theme can always stay with itself, so those rows add nothing. |
| 2026-11-27 | Change `loneliness` to `family` from contrast to move forward. | Reconnecting with family is a next step out of loneliness, not a change of subject. |
| 2026-11-27 | **Revise the move definitions after review.** Stay rows work in both directions. Contrast is kept only when the change of subject is the point, because a change in how a book feels is handled by tone. | The first definitions mixed up subject and feeling, and several rows were labelled with the wrong move. |
| 2026-11-27 | Add an optional `ready_when` column: a short sign that a reader is ready for a move, such as `feels boxed in by expectations`. | Moving a reader forward only works when they are ready. This gives the recommendation logic something to listen for. |
| 2026-11-27 | Apply the revised definitions to the map:<br>• Merge the two `history and memory` and `power of stories` rows into one stay row.<br>• Change `grief` to `kindness` from stay to move forward.<br>• Change `freedom` to `social convention` and `belonging` to `culture clash` from contrast to deepen.<br>• Change `tradition` to `freedom` from contrast to move forward.<br>• Change `ambition` to `purpose`, `kindness` to `justice`, and `women's voice` to `identity` to move forward.<br>• Delete `ambition` to `kindness`, `forgiveness` to `justice`, and `identity` to `tradition`.<br>• Keep `mental health` to `ambition` as the one contrast. | Each row now matches the revised definitions. |

## Coverage and books

| Date | Decision | Why |
|---|---|---|
| 2026-11-27 | Every theme should have at least 2 books, checked by `scripts/check_coverage.py`. | A theme with one book is a dead end for recommendations. |
| 2026-11-27 | Grow the catalog from 9 to 41 books. The 32 new books were AI suggested and approved by the owner. *Five Point Someone* was dropped from the proposal. | Brings every theme to at least 2 books, with a mix of fiction and nonfiction, Indian authors, light reads and lengths. |
| 2026-11-27 | Add a `source` column: `my pick`, `interviewee` or `AI suggested`. The first 9 books are `my pick`. | Shows where each recommendation came from, so AI suggestions can be told apart from the owner's and interviewees' picks. |
| 2026-11-27 | Delete the proposal file and the script's option for reading it once the books were added. | The books are now in the catalog, and keeping the proposal would mean two lists to maintain. |
| 2026-11-27 | Any book with dark, violent or bleak content must include `heavy` or `dark` in `tone`, even if it is fast or satirical. Nine books were updated. | A funny or fast tone should never hide a hard book from a reader who needs to know. |

## Working rules

| Date | Decision | Why |
|---|---|---|
| 2026-11-27 | Keep the repo to `data/`, `docs/` and `scripts/` (plus `README.md` and `CLAUDE.md`). Use plain language and no em dashes. Log product decisions here. Rules are in `CLAUDE.md`. | Keeps the project easy to read and easy to pick up again. |
