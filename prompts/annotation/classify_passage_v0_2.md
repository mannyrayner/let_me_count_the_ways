# Passage classification prompt v0.2

Analyse the highlighted direct or embedded equivalent of “I love you” in the
supplied passage. Return JSON matching `classification_schema_v0_2.json`.

The aim is the best supportable literary interpretation, not an artificially
memoryless reading. Use all legitimately available evidence, while making the
source of every important claim visible:

1. **local text** in the supplied passage;
2. **supplied metadata** such as title, author, source and location; and
3. **background knowledge** you reliably remember about the wider work.

Background knowledge may clarify non-local matters such as prior commitments,
later revelations, irony, deception, coercive patterns or relationships. Do not
invent events, wording or plot facts. Mark uncertain memories as uncertain.
Record whether background knowledge was used, its contribution, and confidence
in it. Uneven familiarity across works is expected and should remain auditable.

## Analyse four distinct layers

### A. Core love-content

Score support from 0 (none) to 4 (very strong) for each non-exclusive reading:

- **truth-conditional:** reports, avows or presents as true a loving emotional
  or mental state;
- **performative:** substantially undertakes, enacts, renews or invokes a
  commitment, obligation or relational undertaking;
- **exclamatory/reflexive:** is substantially an emotionally triggered or
  reflex-like production with weak clear propositional or undertaking force.

Keep performative force relatively strong. Reassurance, intimacy, emotional
impact, affection, courtship, wedding discussion or reference to a shared
future do not alone make the core performative. Record those effects under the
current discourse act instead.

Set `mixed_reading.is_mixed` only when either (a) at least two core readings
have substantial independent support (normally scores of 2 or more), or (b) a
qualitatively important interaction among core readings is central. Select the
corresponding basis and justify it. Weak nonzero secondary support is not a
mixed reading. If neither condition holds, use basis `none` and a null
justification.

Use `relationship_modifier` as open text only when the kind of love is
interpretively relevant; do not force a relationship taxonomy.

### B. Realisation / embedding

Record every applicable `types` value. The values are multi-valued and not an
exhaustive partition; use `other` plus `other_description` when necessary.

`direct_represented_speech` means a character currently says the words in the
fictional world. `quotation_revoicing` means an earlier, hypothetical or
attributed utterance is cited or repeated. `narratively_attributed_speech` and
`verbalisation_of_nonverbal_behaviour` cover wording supplied by the text rather
than literally spoken. Printed quotation marks alone never establish
`quotation_revoicing`. Also record whether the represented words were spoken,
written, not spoken, uncertain, or not applicable.

### C. Current discourse act

Record what the current speaker, narrator or text is doing with the
love-content now. Choose all applicable values from the deliberately small
inventory and explain the analysis. Use `other` rather than forcing a fit.
Pressure and manipulation belong here when they describe the present use; they
do not by themselves make the core love-content performative.

### D. Contextual modification

Record how embedding and context preserve, weaken, strengthen, redirect, quote,
distance, challenge, manipulate, or otherwise modify interpretation of the
core. Choose all applicable effects and explain them.

## Participants, disagreement and assessments

Tie every participant construal to an explicit role and discourse level.
`role` is open text (for example `original_avower`, `current_quoter`,
`current_addressee`, `narrator_or_text`, or `reader`) because embedded cases may
contain several speakers and addressees. Use `supported`, `uncertain`, or
`unavailable`; do not invent a construal when evidence is absent. When status is
`unavailable`, use `analysis` to explain what evidence is unavailable and use a
null confidence rather than estimating confidence in an invented construal.

Record substantive conflicts between participants or levels in `disagreements`
rather than reducing them to general uncertainty. An empty array means that no
disagreement is supported by the available evidence.

Assess deception/misrepresentation, manipulation/pressure, and strategic
ambiguity independently. Each requires a status, explanation and scoped
confidence. `unsupported` means available evidence weighs against or supplies
no support for the claim; `uncertain_not_assessable` means the evidence cannot
settle it.

## Evidence, uncertainty and openness

Give every evidence item a unique ID, provenance (`local_text`,
`supplied_metadata`, or `background_knowledge`), a quotation or concise
description, the claim it supports, and confidence. Do not present metadata as
passage wording. Do not present remembered wording as a quotation unless its
exactness is reliable; a description is sufficient.

Add a context request only for a specified claim. Distinguish
`required_for_core_classification` from `useful_for_richer_interpretation`, and
name the affected analytical layers. Do not request more context merely because
more context is always potentially interesting.

Confidence is recorded separately for core content, realisation, current act,
contextual modification, evidence, participant construals, assessments, and
background knowledge. Calibrate each to its own claim; high core confidence may
coexist with uncertainty elsewhere.

Finally, decide whether the provisional scheme gives a natural account. Use
`ontology_assessment` and `notes` to diagnose inadequacy, propose missing
dimensions, or preserve important interpretation that structured fields miss.
Do not make the data tidy by forcing the case into the ontology.
