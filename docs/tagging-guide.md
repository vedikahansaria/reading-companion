# Tagging guide

This guide explains each column in `data/books.csv`. It is for anyone adding or checking a book.

The catalog exists so we can suggest a reader's next book based on where they are emotionally, and not only on books like the one they just read. From any book, the next one can:

- **stay** on the same theme
- **go deeper** into it
- **move the reader forward** to something new
- **offer a contrast**

Most of the fields below exist to make these moves possible.

## General rules

- One row per book
- If a field holds several values, separate them with semicolons (`;`), for example `loneliness;friendship;healing`
- Keep tags short and lowercase, except for names (places, people, events)
- Use an existing tag before inventing a new one, e.g., use `loneliness` everywhere, never `loneliness` in one row and `being alone` in another
- If you're not sure about a tag, still fill it in, then mark it in `confidence` and `confidence_notes`

## Fields

### id
A short, unique name for the book, in lowercase with hyphens, such as `the-book-thief`. It never changes, even if the title is corrected later.

### title
The title as published in English.

### author
The author's name as it appears on the cover. For a translated book, use the original author, not the translator.

### year
The year the book was first published, in any language. If the English edition came later, put that year in `confidence_notes`.

### genre
One short label for the kind of book, such as `contemporary fiction`, `historical fiction`, `memoir`, `classic novella` or `business history`.

### fiction_or_nonfiction
Either `fiction` or `nonfiction`.

### themes
3 to 5 subjects the book is really about. These are what it explores, not its plot. Examples: `loneliness`, `belonging`, `resilience`, `family loyalty`, `moral courage`.

### tone
How the book feels to read. Use 2 to 4 words, such as `warm`, `heavy`, `funny`, `hopeful`, `lyrical`, `ironic`, or `bittersweet`. A book can be both `heavy` and `hopeful`.

### needs
What the book can give a reader right now. Choose one or more of these six:

| Need | Pick it when the book… |
|---|---|
| `comfort` | feels safe and kind, and leaves you feeling better |
| `escape` | takes you somewhere else entirely |
| `perspective` | helps you see your life, or other people's, differently |
| `meaning` | helps you make sense of loss, pain or big questions |
| `inspiration` | makes you want to act, build or change something |
| `laughter` | makes you laugh out loud |

Keep to this list so that books can be matched on it.

### leads_from
What a reader might be going through when this book is the right one to pick up, written as short situations. Examples: `feeling isolated or invisible`, `grieving a loss`, `restless in your career`.

This is the most important field for matching a reader to a book.

### leads_to
Themes a reader might be ready for after finishing this book. These are what connect one book to the next. A `leads_to` tag that matches another book's `themes` means that book could **go deeper** or **move forward**. A matching book with a very different `tone` could **offer a contrast**.

### pace
How quickly the book moves:
- `slow`: reflective, with dense prose or a lot of interior thought
- `steady`: moves along at an even pace
- `fast`: hard to put down

### length
- `short`: under about 250 pages
- `medium`: about 250 to 450 pages
- `long`: over about 450 pages

Page counts vary between editions, so treat these as rough guides.

### content_notes
Heavy topics a reader may want to be warned about before starting, such as `suicide`, `childhood abuse`, `racism and racial slurs` or `war violence`. Name the topic plainly, without spoilers where possible. Leave it empty only if there is truly nothing to flag.

### confidence
Either `high` or `low`:
- `high`: every tag in the row is well known or has been checked
- `low`: at least one tag is a guess. Name it in `confidence_notes`

### confidence_notes
Free text. Say which tags are uncertain and why. Also use it for anything a later reviewer should know, such as a translation date or a corrected title.

## Checking a row

Before adding a row, check:

1. Does it have 3 to 5 themes?
2. Do its needs come only from the six listed above?
3. Are `leads_from` entries written as situations a reader is in, and not as themes?
4. Have you listed the content notes?
5. If you guessed anything, does `confidence_notes` say so?
