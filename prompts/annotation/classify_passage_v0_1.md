# Passage classification prompt v0.1

Analyse the highlighted direct equivalent of “I love you” in the supplied
passage. Base the analysis on textual evidence in the passage. Knowledge of the
wider work may suggest questions, but must not be presented as evidence unless
that context is supplied.

The initial T/P/E typology is a hypothesis, not a forced partition:

- **truth-conditional:** reports or avows a loving emotional or mental state;
- **performative:** undertakes, enacts, renews, or invokes commitment;
- **exclamatory/reflexive:** emotionally triggered production with little clear
  propositional or undertaking force.

A case may strongly support several readings or none. Distinguish the speaker’s,
hearer’s, narrator/text’s, and plausible reader’s construals when the passage
supports doing so. Do not infer authorial intention directly.

Return JSON matching `classification_schema_v0_1.json`. In particular:

1. Score support for each T/P/E reading from 0 to 4; these scores need not sum to
   anything.
2. Quote brief evidence spans from the supplied passage and explain the inference.
3. Mark quotation, negation, metalinguistic mention, conventional scripting,
   deception/manipulation, and strategic ambiguity when supported.
4. Say whether more context is needed and what information would resolve.
5. Decide whether T/P/E gives a natural account. If not, describe the missing
   distinction without forcing a new universal category.
6. Calibrate confidence. Ambiguity and participant disagreement are findings,
   not annotation failures.
