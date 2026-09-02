# Annotation scheme v0.2 → v0.3 change log

## Why v0.3 is intentionally simpler

v0.2 was designed as a rich ontology-development instrument. The completed
*Jane Eyre*, *Little Women*, and *Madame Bovary* work showed that its contextual
layers are interpretively useful, but also that formally classifying each form
of deception, pressure, ambiguity, participant construal, and embedding risks
making the surrounding literary situation the quantitative object of study.

v0.3 is a controlled simplification. Its primary quantitative target is now
the force of the core love utterance. Context remains evidence and remains
visible, but is mostly represented in open qualitative prose.

## Core classification

- The independent 0–4 T/P/E scores are retained unchanged in meaning.
- `other` (O), also scored independently from 0–4, is added as a high-burden
  ontology escape hatch. It tests whether T/P/E is adequate rather than assuming
  adequacy by construction.
- A core-wide confidence, concise analysis, and optional ambiguity note are
  retained. Ambiguity among T/P/E must not be encoded as O.
- `mixed_reading` is removed from primary annotation. Mixedness is already
  recoverable from the independent scores and can be derived downstream.
- `relationship_modifier` moves into open contextual interpretation when it is
  relevant.

## O diagnosis and ontology development

When O is nonzero, two explanations are mandatory: what T/P/E fails to capture,
and why that failure belongs to the core utterance rather than its context. When
O is zero, both are null. A single O case is preserved for later comparison; it
does not create a fifth core category. `ontology_assessment` now records whether
the compact account is natural, strained, or inadequate and permits at most an
open candidate recurrent dimension.

## Context and embedding

The v0.2 structured `current_discourse_act`, `contextual_modification`,
`participant_construals`, `disagreements`, and independent deception,
manipulation, and ambiguity assessments are replaced by one required
`contextual_interpretation`. This field can still discuss all those phenomena,
but does not imply that they form an exhaustive taxonomy. In particular,
truth/sincerity is explicitly separated from T/P/E mode.

The multi-valued v0.2 `realisation` layer is replaced by compact
`utterance_status`: one best identifying status plus an open description. It
preserves awareness of direct, quoted/revoiced, reported, imagined, written,
nonverbal-verbalised, and hypothetical events without rebuilding a contextual
ontology.

## Evidence and background knowledge

Evidence IDs, the three provenance values (`local_text`, `supplied_metadata`,
and `background_knowledge`), support statements, and scoped confidence are
retained. Background knowledge remains allowed and auditable. v0.3 keeps the
v0.2 consistency rule that using it requires both a contribution and a
background-knowledge evidence item.

## Validation and compatibility

The dependency-free validator and single-text pipeline now accept explicit
version `0.3`. Existing v0.1 and v0.2 prompt, schema, validation paths, and
annotations are unchanged. No existing annotations are migrated or
reannotated as part of this proposal.

## Deferred validation

After review, a small regression set should be drawn from the three annotated
novels, alongside synthetic O cases (such as microphone testing, grammar
practice, and rote imitation) and ambiguous genuine love utterances that should
not receive O merely because they are difficult. Large-scale reannotation is
explicitly deferred until v0.3 is approved.
