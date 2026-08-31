# Let Me Count the Ways

## Handover: next development phase

### Current status

The project has completed:

- initial corpus acquisition and extraction for *Jane Eyre*;
- six extracted occurrences of direct or embedded forms of “I love you”;
- at least two diagnostic classification runs using annotation prompt/schema v0.1;
- preliminary review showing that the current T/P/E framework is useful but structurally incomplete.

The early results are encouraging but still purely developmental. They are not yet evidence for frequency claims.

The immediate goal is now to complete the first diagnostic cycle, revise the annotation scheme in a principled way, and build lightweight batch infrastructure for running the revised analysis reproducibly.

---

## Research principle for this phase

Do **not** treat the current T/P/E scheme as final.

The current framework distinguishes:

- truth-conditional;
- performative;
- exclamatory/reflexive.

This remains a useful starting hypothesis.

However, the early *Jane Eyre* cases suggest that many occurrences involve additional structure, especially embedding.

A central emerging distinction is between:

1. **the force or construal of the core “I love you” content**, and
2. **the current discourse act created by the larger context in which that content is embedded**.

Examples include:

- direct avowal;
- quotation/repetition of an earlier avowal;
- imagined or attributed utterance;
- hedged forms such as “I think I love you”;
- reported or hypothetical speech;
- metalinguistic mention;
- possible future cases involving negation, irony, conditionality, etc.

The current working hypothesis is that embedding is largely **orthogonal** to T/P/E rather than a replacement for it.

Do not freeze this assumption either. The purpose of the development set is to find out whether it survives further examples.

---

# Phase A: finish Jane Eyre v0.1

## A1. Annotate the remaining two Jane Eyre passages

Run the current v0.1 classification prompt/schema unchanged on the final two extracted *Jane Eyre* occurrences that have not yet been analysed.

Do not modify the prompt or schema before these runs.

The reason is methodological: we want all six *Jane Eyre* cases to form a directly comparable v0.1 diagnostic set.

Preserve:

- exact requests;
- raw responses;
- parsed outputs;
- model identifiers;
- prompt/schema versions;
- timestamps;
- costs;
- failures or retries.

---

# Phase B: review all six Jane Eyre cases

After all six v0.1 annotations exist, perform a structured diagnostic review.

The review should ask:

## B1. Where does v0.1 work naturally?

Identify cases where:

- T/P/E gives a clear and useful account;
- participant construals are handled adequately;
- uncertainty is represented appropriately;
- no important interpretive information is lost.

## B2. Where does v0.1 strain or fail?

Look especially for recurring problems involving:

- quotation;
- revoicing;
- reported speech;
- imagined or attributed utterance;
- hedging;
- participant disagreement;
- current discourse function versus original force;
- manipulation/pressure versus deception;
- overuse of `mixed_reading`;
- context dependence;
- insufficient metadata;
- any phenomena not anticipated in the handoff.

Do not treat every unusual case as requiring a new universal category.

Prefer the smallest set of dimensions that explains several cases.

---

# Phase C: propose annotation scheme v0.2

After reviewing all six cases, propose a revised prompt/schema.

Do not overwrite v0.1.

Create versioned files for v0.2 and a short change log explaining every substantive modification.

The revised scheme should probably investigate the following two changes, but Codex should assess them critically rather than implement them automatically.

---

## C1. Add explicit request metadata

The request should provide useful contextual metadata where available, for example:

- work ID;
- title;
- author;
- language;
- source/edition ID;
- location in work: chapter/section/page or character offset where available;
- extracted occurrence ID;
- exact matched string;
- amount of supplied context.

Important constraint:

**Metadata is orientation, not interpretive evidence.**

The model may use metadata to understand what it is looking at, but claims about force or construal should be justified from supplied textual evidence.

Knowledge of a famous work must not silently replace the passage.

If more context is required, the model should request it.

Do not add manually inferred speaker/addressee information to the request unless it has been obtained reproducibly from the source or a previous annotation stage.

---

## C2. Distinguish core force from current act

The current response schema should probably be extended so that it can represent separately:

### Core love-content analysis

What semantic/pragmatic force does the embedded or represented “I love you” content have?

Possible representation:

- truth-conditional support;
- performative support;
- exclamatory/reflexive support;
- uncertainty;
- mixed interpretation where genuinely warranted.

### Embedding / occurrence status

How does the phrase occur in the present passage?

Possible initial values might include:

- direct;
- quoted;
- reported;
- imagined/attributed;
- hypothetical;
- hedged;
- negated;
- metalinguistic;
- other.

Do not assume these are exhaustive or mutually exclusive.

Include a notes/free-text field and an escape hatch for missing categories.

### Current discourse act

What is the larger utterance or passage doing with the love-content now?

Examples might include:

- direct avowal;
- reassurance;
- repetition;
- elicitation;
- pressure;
- use as evidence;
- distancing;
- manipulation;
- irony;
- rejection;
- other.

Again, do not freeze this as a final ontology yet.

### Interaction between core and context

Add an explicit field describing how the embedding/context modifies, preserves, weakens, quotes, redirects, or otherwise changes the interpretation of the core phrase.

This is especially important for cases such as:

- quotation of an earlier avowal;
- “I think I love you”;
- imagined speech;
- participant disagreement.

---

## C3. Reconsider `mixed_reading`

The first diagnostic runs suggest that `mixed_reading` may currently be triggered too easily.

A case with:

- T=4;
- P=1;
- E=0 or 1

should not automatically count as genuinely mixed merely because speech acts have secondary interpersonal effects.

Review whether `mixed_reading` should require:

- substantial support for more than one core reading; or
- a qualitatively important interaction between interpretations.

Document the decision.

---

## C4. Separate manipulation from deception

The current feature `deceptive_or_manipulative` may conflate distinct phenomena.

For example, a speaker may pressure or strategically exploit another person without making a deceptive assertion.

Consider separating:

- deceptive;
- manipulative/pressuring;
- strategically ambiguous.

Only do this if the six-case review supports the distinction.

---

## C5. Preserve ontology escape hatches

v0.2 must still be able to say that the revised typology is inadequate.

Retain or improve fields equivalent to:

- `typology_adequate`;
- `typology_diagnosis`;
- `proposed_missing_dimensions`;
- `needs_more_context`;
- `context_request`;
- confidence/uncertainty.

The development phase should reward the model for identifying inadequacies rather than forcing every case into the available structure.

---

# Phase D: build a text-level batch runner

Once v0.2 has been designed, implement a lightweight batch runner.

The first version should process **all extracted occurrences from one text**.

Do not yet build the final multi-corpus orchestration layer.

The command should approximately:

1. take a source/work or extracted-passages file;
2. iterate through every occurrence;
3. run the selected annotation prompt/schema version;
4. store each request/response separately;
5. preserve failures;
6. support resume/restart;
7. avoid overwriting previous runs;
8. record model, prompt/schema hashes, timestamps and costs;
9. create a simple summary index for the run.

A resumable design is strongly preferred.

Do not require a database unless clearly necessary.

JSON/JSONL and directory-based run records are sufficient for now.

---

# Phase E: reannotate Jane Eyre using v0.2

Use the batch runner to classify all six *Jane Eyre* passages with the revised scheme.

Then produce a concise comparison report:

## v0.1 versus v0.2

For each occurrence, report:

- whether the main interpretation changed;
- whether the revised schema captured structure that v0.1 missed;
- whether ambiguity became clearer;
- whether any new field proved unnecessary or confusing;
- whether the model still reports missing dimensions;
- whether `mixed_reading` behaviour improved;
- any regressions.

The purpose is not to show that v0.2 is “better” by definition.

The purpose is to test whether the changes actually improve the analysis of the cases that motivated them.

---

# Phase F: move to two additional texts

If v0.2 performs reasonably on *Jane Eyre*, acquire and analyse two more works:

1. one additional English-language text;
2. one text in French, Swedish or Norwegian.

French is particularly attractive because Barthes’s analysis concerns *je t’aime* specifically.

However, source legality, machine readability, suitable occurrences and corpus diversity should also influence selection.

Use the same pipeline:

- verified source;
- provenance;
- extraction;
- batch annotation;
- diagnostic review.

Do not yet make population-level frequency claims.

---

# Phase G: review before scaling further

After:

- Jane Eyre v0.1;
- Jane Eyre v0.2;
- one new English work;
- one French/Swedish/Norwegian work,

pause again.

At that point ask:

- Which dimensions recur across texts?
- Which were peculiar to one work?
- Is the core-force/current-act distinction holding up?
- Are embedding types stabilising?
- Does T/P/E still look useful?
- Are important new categories emerging?
- How frequently is more context requested?
- Are there systematic language-specific issues?
- Is the schema becoming too complicated?
- Which fields are actually useful for later quantitative analysis?

Only after this review should we consider a larger multi-text runner or larger development corpus.

---

# Desired artefacts from this phase

Please create or update:

- v0.1 diagnostic outputs for all six Jane Eyre cases;
- a six-case diagnostic review document;
- annotation prompt/schema v0.2;
- a v0.1 → v0.2 change log;
- a resumable text-level batch runner;
- Jane Eyre v0.2 batch results;
- a v0.1/v0.2 comparison report;
- runbooks for acquiring and processing the next two texts.

Preserve all prior artefacts.

---

# Research stance

The key principle remains:

**Do not use the annotation scheme to make the data tidy. Use the data to discover what the annotation scheme needs to represent.**

The project is still in ontology-development mode.

The fact that the scheme may become fairly complex is not itself a failure.

Likewise, ambiguity, disagreement, quotation, hedging and participant-dependent interpretation are potentially central findings rather than noise.

The immediate objective is to build a better empirical representation of the phenomenon before attempting large-scale quantitative claims.
