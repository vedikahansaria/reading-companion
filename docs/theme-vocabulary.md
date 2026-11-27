# Theme vocabulary

The `themes` and `leads_to` columns in `data/books.csv` may only use the themes listed below. A shared list is what lets the catalog link books: one book's `leads_to` can match another book's `themes` only if both use exactly the same words.

There are 32 themes in four families. Spell each one exactly as written here, in lowercase.

## Inner life

| Theme | What it means |
|---|---|
| `loneliness` | Feeling cut off from other people, even when they are around. |
| `mental health` | Anxiety, trauma, depression, and the slow work of healing from them. |
| `self-acceptance` | Learning to be kind to yourself and believing you are worth something. |
| `identity` | Working out who you are and who you are becoming. |
| `grief` | Living with death and loss, and carrying them over time. |
| `resilience` | Keeping going and getting back up after things go wrong. |
| `growing up` | Childhood and innocence, and the move into adulthood. |
| `freedom` | Choosing your own path instead of the one set for you. |
| `purpose` | Looking for what makes life feel worth it. |
| `hope` | Believing things can get better, even after the worst. |

## Relationships

| Theme | What it means |
|---|---|
| `friendship` | The bonds we choose, and what they give us. |
| `belonging` | Finding your people and a place where you fit. |
| `family` | Loyalty, conflict, and the ties we are born into, including when to step back from them. |
| `kindness` | Small acts of care, often from strangers, that change things. |
| `forgiveness` | Letting go of hurt and giving people, yourself included, a second chance. |
| `love and betrayal` | Deep love and what happens when it is broken. |
| `empathy` | Understanding people who are not like you, and seeing past first impressions. |

## Society

| Theme | What it means |
|---|---|
| `justice` | Fairness and unfairness, and what happens when systems fail people. |
| `prejudice` | Judging people by race, class, gender, or group instead of who they are. |
| `social convention` | The unwritten rules of a society and the price of breaking them. |
| `moral courage` | Doing the right thing when it is hard, risky or unpopular. |
| `women's voice` | Women claiming the right to speak, choose, and be heard. |
| `culture clash` | What happens when different cultures, places or ways of life meet. |
| `tradition` | Customs and duties passed down, and whether to keep or change them. |
| `history and memory` | How the past shapes the present, and why remembering matters. |
| `power of stories` | How words, books, and stories shape and sustain us. |

## Work and ambition

| Theme | What it means |
|---|---|
| `ambition` | Wanting more, and the drive to get it. |
| `entrepreneurship` | Starting and building something of your own from little. |
| `risk and failure` | Taking chances, failing, and learning from it. |
| `leadership` | Taking responsibility for people and a shared goal. |
| `legacy` | What we build to outlast us, and what gets passed on. |
| `education` | Learning, and how it can change a life. |

## Merged terms

These earlier free-text tags now map to a single theme:

| Earlier tag(s) | Theme |
|---|---|
| trauma and healing, anxiety, abuse | `mental health` |
| self-compassion, self-worth | `self-acceptance` |
| self-invention, myth and identity, the cost of change | `identity` |
| death and loss, grief | `grief` |
| hope after loss | `hope` |
| perseverance | `resilience` |
| childhood, innocence | `growing up` |
| self-determination | `freedom` |
| purpose beyond success | `purpose` |
| connection, community, human connection | `belonging` |
| family loyalty, family conflict, estrangement and boundaries | `family` |
| kindness to strangers | `kindness` |
| second chances | `forgiveness` |
| misunderstanding | `empathy` |
| racial injustice, injustice | `justice` |
| judgment, society, and conformity | `social convention` |
| courage, standing up for others | `moral courage` |
| female agency, speaking up | `women's voice` |
| cultural clash, cross-cultural life | `culture clash` |
| duty versus self, tradition and modernization | `tradition` |
| history, remembrance, humanity in dark times, race and history | `history and memory` |
| power of words | `power of stories` |
| risk, failure | `risk and failure` |
| building something | `entrepreneurship` |
| family business, family and legacy | `legacy` (with `family` and `entrepreneurship` where they fit) |
| learning | `education` |

`classic literature` was dropped: it describes a kind of book, not a theme.

## Moves between themes

`data/theme_journeys.csv` links pairs of themes with one of four moves:

- **stay:** a closely related theme with the same emotional weight. Any theme can always lead to itself as a stay, so those pairs are not listed.
- **deepen:** goes further into the same territory, often harder or more complex.
- **move forward:** the natural next step once a reader is ready.
- **contrast:** a different angle or mood that gives relief or a fresh view.

## Adding a theme

Add a new theme only when none of these fits. When you do, put it in one family with a one-line meaning, and add at least one row for it to `data/theme_journeys.csv`.
