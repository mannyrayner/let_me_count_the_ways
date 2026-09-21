# Evidence reader and context pilot v1

This revision makes the existing evidence readable and prepares a controlled
context experiment. It contains **no new model classifications**. The historical
252 annotations remain unchanged.

## Empirical questions

1. Can substantial T, P or E occur with little support for the other two modes?
   Report the joint score patterns, including counts with the focal dimension
   at least 3 and the other two at most 1; repeat descriptively at threshold 2.
   Do not treat missing/insufficient judgments as zero. A lie can be high T:
   actual affection and truth-conditional avowal are separate questions.
2. How do judgments of P change when more narrative evidence is supplied?
   The primary diagnostic comparison is D versus B, showing every selected case.
   Also show A→B, B→C and C→D, insufficiency transitions, and within-condition
   repeat disagreement. Later conduct can alter a reader's interpretation without
   changing what a character knew or proving that an earlier undertaking vanished.

The corpus is one evolving collection. Work selection, extraction versions and
annotation runs remain part of its provenance. None of these purposive literary
samples estimates the frequency of meanings in everyday conversation.

## Reader

[The collection](../reader/README.md) includes 252 saved annotations from 35
complete works searched in seven languages. The five recently acquired works
are presented with the earlier works. Pengar remains in the inventory despite
having no extracted occurrences.

HTML provides search, work/status filters, minimum-P filtering, adjacent-case
navigation and exact-target highlighting. Markdown provides GitHub-readable
records. Each shows original passage, the actual wider context and translation
supplied to the model, its saved explanation, evidence, uncertainty, reported
background use, and links to the frozen raw records. Narrative interpretation
is labelled as model interpretation. The build generates no new explanation.

The annotation snapshot is ef7ea7933d8aa02b176d8fbddc496e55a41a7144.
Input hashes and generated-file hashes are in docs/reader/manifest.json.
The reader deliberately covers completed annotations only; acquired candidates
are not silently added to its denominator.

## Pilot design

Eight purposively selected diagnostic cases: Jane addressing St John; the
narrator addressing Maria; Lorck addressing Constance; Nikki addressing Keith;
Goneril and Cordelia addressing Lear; Pierre addressing Hélène; and the rose
addressing the prince. The two Lear cases are not independent works. Selection
and source offsets were fixed before any pilot responses. Selection drew on
previous discussion and historical annotations; it is not blind validation.

| Condition | Supplied evidence |
|---|---|
| A | Extracted love expression alone |
| B | A plus the specified local scene/exchange or bounded scene window |
| C | B plus prior narrative evidence |
| D | C plus later narrative evidence |

A uses the frozen extraction match, not necessarily a complete speech turn.
Thus it deliberately withholds qualifications, punctuation and prosodic cues
outside that match. Full speech-unit offsets are also recorded for boundary
review. The target remains identical across conditions. B boundaries and all
C/D source spans are explicit in data/context_pilot/selection_v1.json.

Two evidence scopes are implemented and must be reported separately:

- **Dossier:** selected source excerpts. Some historical cases use fixed nearby
  windows and an ending excerpt; Lear, Tolstoy and the rose have specified
  narrative sections. These selections are incomplete and may favour particular
  interpretations. They are inspectable, not neutral substitutes for full books.
- **Full text:** C supplies every canonical character before the scene; D
  supplies the entire canonical work, in order. The extractor does not truncate
  long works. Input-size and cost guards must pass before calls begin. Tolstoy's
  approximately 2.9 million characters need a separately verified model capacity.

No model-generated summaries or full-context translations are fed into a shorter
condition. Original-language evidence is supplied; the model explains in English.
That differs from the historical translation-assisted pipeline. Comparisons
between conditions use this same new protocol; old and new scores are not an
isolated experiment in context alone.

Each case/condition has three separate Responses API requests with no conversation
history or previous-response link. Order is shuffled with a recorded seed. Names,
text and style may reveal famous works even though titles/authors and old scores
are withheld. A source-only instruction and recognition self-report cannot prove
that pretrained knowledge has been excluded. Fresh requests prevent conversational
carry-over; they do not make human-style ignorance experimentally available.

The new prompt preserves the core T/P/E distinction and requires separate
actual-affection evidence, undertaking/uptake description, exact source quotes,
and per-dimension insufficiency. Null means insufficient evidence; zero is an
assessable absence of support. O remains available for residual core functions;
the study does not infer T/P/E exhaustiveness from low O scores.

## Outputs and interpretation

The default dossier plan is **96 calls**, with no calls yet completed. The saved
preflight estimate is about **USD 7.43**, using the repository's model/pricing
snapshot dated 2026-08-30. This is a heuristic estimate, not a billing limit.
The optional full-text Lear comparison adds 24 calls, estimated at USD 2.65.

Exact requests, raw responses, pricing snapshots and costs are retained per
attempt. Successful compatible results resume without another call; a failed or
interrupted attempt requires explicit retry and remains on disk. Prompt, schema,
selection, input, model and repetition identify a call. A saved response is checked
for shape, score/status consistency and literal quotation support. This does not
validate the literary inference drawn from a correctly quoted passage.

Reports show every individual T/P/E/O judgment and per-condition P distributions,
counts at P≥2 and P≥3, and median D−B only when all B and D repetitions are
assessable. Pending or partial results are labelled. Repetition disagreement is
visible; repeated calls are not additional literary observations. The initial
pilot can establish sensitivity of this model's judgments to supplied evidence;
claims about readers, authors' intentions or original illocutionary force need
further argument and independent review.

## New sources and extraction

- **War and Peace:** Russian original with its French dialogue, from the Tolstoy
  90-volume edition, volumes 9–12. These contain 360 chapters across 382 title,
  part and chapter sections. Volumes 13–14 (drafts/variants) are excluded. The
  [edition](https://tolstoy.ru/online/90/09/) explicitly allows reproduction.
  Page-number and note-pointer removal preserves actual words inside page-boundary
  spans. Footnote translations and editorial apparatus are excluded to avoid
  duplicate avowals; source HTML is preserved for inspection.
- **King Lear:** [Project Gutenberg 1532](https://www.gutenberg.org/ebooks/1532),
  modern-spelling original English, five acts and 26 scenes. Source bytes are
  retained, with wrapper removal and LF line-ending normalization documented.
- **Le Petit Prince:** original French, dedication and 27 chapters, from
  [Project Gutenberg Australia](https://gutenberg.net.au/ebooks03/0300771h.html).
  The [source's licence](https://gutenberg.net.au/licence.html) distinguishes
  Australian status from rights elsewhere. Full source, candidate contexts,
  translations and requests stay in ignored local directories. Public metadata,
  hashes, section coordinates and score-only pilot summaries do not distribute
  its full text. No clearance to publish substantial excerpts is implied.

Pattern v0.13 extends v0.12 with Russian and French-in-Russian forms, royal
possessive address, and obligation modals. A source recall screen found Russian
coordinated forms, plural addressees and an aspectual construction missing from
the first pass; the added patterns and residual screen are recorded openly.
This is exploratory development, not independently established complete recall.

The final candidate inventory is **42**: War and Peace 37, King Lear 4, and
Le Petit Prince 1. Membership decisions and annotation are pending. A separate
wrapper runs the established membership/translation/v0.3.1 classification
pipeline and keeps restricted outputs local.

Re-extracting the existing 35 works with v0.13 changes 254 candidate spans to 255:
one additional “I should love you” in Middlemarch, with none removed. That new
candidate is recorded in the audit and is **not** included in the historical
252 annotations or silently promoted to a retained occurrence. It needs membership
review in a future corpus revision. Occurrence IDs also encode pattern version;
span comparison, not ID equality, is the regression check.
