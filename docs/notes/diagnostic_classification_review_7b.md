# Diagnostic classification review: Step 7B

## Run reviewed

- Case: imagined utterance
- Occurrence: `bronte-jane-eyre-f221719b1af4`
- Created: 2026-08-30T12:58:24.215071Z
- Model alias: `5.6`
- API model: `gpt-5.6-sol`
- Prompt SHA-256:
  `bc28060585a36658bffdcc1d71e8a6e4f6f8bfe65a0972e5bace60c728448587`
- Input SHA-256:
  `f4f4b3a632374d083d73b5f6f2ee44bfe904a9f08920c26117dcc842331ddc7e`
- Schema SHA-256:
  `f2c3f81b241e4b2b8ed7738f428f1ba503db942f2a88ff0a28e48f86a9a58789`
- Estimated cost: USD 0.033964
- Structural validation: passed

## Result and assessment

The model assigned support `4` to truth-conditional, `1` to performative, and
`0` to exclamatory/reflexive. It correctly recognized that the narrator supplies
verbal content for a look and that the words were not spoken aloud. It judged
T/P/E adequate for the represented core content while describing the chief
complication as orthogonal: an inferred verbalization of nonverbal behavior.

This complements 7A. In 7A, T/P/E did not classify Rochester’s present act of
quoting and leveraging Jane’s earlier avowal. In 7B, T/P/E naturally classifies
the imagined proposition, but cannot represent whether an utterance happened,
who supplied its wording, whether communication was intended, or how embedding
changes performative force. Together the cases support three separate layers:

1. classification of the core construction;
2. classification of its embedding or presentation context;
3. effects of that context on speaker, addressee, actuality, commitment, and
   interpretation of the core construction.

The `quoted` feature is not precise enough here: typographic quotation marks are
present, but there was no actual quoted utterance. A future embedding inventory
should distinguish direct speech, quotation of prior speech, reported speech,
hypothetical speech, narratively imagined speech, and verbalization of
nonverbal behavior.

## Context and model familiarity

The request for more context is reasonable for determining her uptake, his
communicative intention, and narrative reliability. Future classification inputs
should also supply explicit bibliographic and location metadata:

- author and title;
- source and edition identifier;
- normalized character offset and total length;
- percentage through the work;
- chapter or section when deterministically available.

Model familiarity with a famous work may help formulate hypotheses, but it must
not silently become textual evidence. A revised prompt should require the model
to distinguish claims supported by the supplied passage or metadata from claims
based on background familiarity, and to request source context for any material
claim that depends on the latter.

## Decision

Accept and preserve 7B. Keep the v0.1 prompt and schema unchanged for 7C so all
three diagnostic cases remain comparable. After 7C, design a v0.2 input and
annotation contract with orthogonal core, embedding, and embedding-effect fields,
plus explicit bibliographic/location metadata and evidence provenance.
