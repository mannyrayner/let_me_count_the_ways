# Initial corpus pipeline

## Recommendation

The proposed four-stage pipeline is a good first experiment. It should remain
small, inspectable, and reversible: the first 100–200 occurrences are a
development set for discovering weaknesses in the analysis, not evidence for a
final frequency claim.

Two safeguards are important from the start:

1. Model familiarity with a famous work is useful metadata, but must not replace
   the words surrounding an occurrence. Each classification must cite evidence
   in the stored passage and be allowed to request more context.
2. A model-suggested title is only a candidate. Availability, edition, language,
   copyright, download URL, and reuse terms must be verified before acquisition.

## Stage 1: propose and approve targets

Use `prompts/ontology_development/target_discovery_v0_1.md` to request a ranked
candidate list in English, Swedish, French, Norwegian, Danish, German, and
Italian. Save the untouched API response with model and request metadata under
`results/development/target_discovery/`.

A human then reviews candidates and promotes approved editions into an
acquisition manifest. Approval should consider:

- lawful availability of a specific edition, not just the abstract work;
- likely presence of relevant phrases;
- genre, period, language, and relationship diversity;
- whether the text is machine-readable enough for extraction;
- model familiarity without selecting only canonical Western novels;
- independence from the later evaluation sample.

The model must not invent URLs or licence claims. Discovery and verification are
separate steps.

## Stage 2: define search patterns

The versioned starting patterns are in
`data/development/search_patterns_v0_1.json`. They deliberately cover direct
first-person declarations, including formal or plural addressees, while avoiding
broader forms such as “she loved him”.

Before extraction, test every pattern against positive and negative examples
from its language. Record pattern version with every match. Searches should be
Unicode-aware and preserve the original matched spelling.

Patterns find candidates; they do not define the linguistic phenomenon. Missed
forms, OCR errors, interrupted speech, emphatic spellings, negation, quotation,
and reported speech should be logged during development and used to revise the
pattern set.

## Stage 3: acquire and extract

For each approved text:

1. Record a provenance entry containing source URL or catalogue identifier,
   edition, language, rights statement, retrieval time, and file checksum.
2. Keep the unmodified download under `data/raw/` only when its reuse terms allow
   repository storage. Otherwise keep it outside Git and retain metadata plus
   permitted derived data.
3. Convert to normalized UTF-8 plain text without overwriting the raw file.
4. Search all patterns declared for that language.
5. Store one JSON Lines record per occurrence under `data/development/passages/`.

Each passage record should contain at least:

- stable occurrence, work, edition, and source identifiers;
- language and pattern version;
- exact match and character offsets in the normalized text;
- context before and after the match;
- a larger-context pointer or location;
- provenance and rights references;
- extraction timestamp and script version.

Start with paragraph-bounded context plus approximately 1,000 characters on
each side. The classifier may return `needs_more_context`; expansion should then
be deterministic and recorded. Keep multiple occurrences from one work linked,
and prevent a prolific work from silently dominating the sample.

## Stage 4: classify and diagnose the ontology

Use `prompts/annotation/classify_passage_v0_1.md` and its companion JSON schema.
The initial response is multi-label rather than forced-choice. It records a
strength for each truth-conditional, performative, and exclamatory reading, plus:

- mixed or participant-dependent construal;
- evidence spans and a short rationale;
- uncertainty and a request for more context;
- strategic, deceptive, conventional, quoted, negated, or metalinguistic use;
- whether the T/P/E scheme is adequate;
- proposed missing dimensions or categories.

Save the exact request, raw response, parsed response, model identifier,
parameters, prompt hash, timestamps, and errors. Do not overwrite reruns.

## First development run

A practical first run is:

1. Generate 30–50 target candidates.
2. Human-approve 10–20 works across at least four languages and several genres.
3. Acquire a small number of clearly reusable editions.
4. Extract all direct matches, then stratify at most 20 occurrences per work.
5. Draw 100–200 occurrences with a fixed random seed.
6. Classify them once, expanding context only when requested.
7. Human-review every `typology_adequate = false` case, all high-uncertainty
   cases, and a random sample of the remainder.
8. Report provisional label strengths and overlap, but emphasize the catalogue
   of failure modes over headline percentages.
9. Revise the patterns, prompt, and ontology under new version numbers.

## Interpretation limits

This development sample will be purposive and conditioned on searchable surface
forms, available texts, chosen languages, and famous works. Its proportions are
pipeline diagnostics, not estimates of how people generally use “I love you”. A
later quantitative claim will require a defined sampling frame, deduplication,
work-level weighting or hierarchical analysis, held-out validation, and human
annotation.
