# Annotation scheme v0.2 implementation note

## Review status

The v0.2 prompt, schema and validator implement the combined Phase B design
brief. They are intentionally stopped at the requested review checkpoint. No
*Jane Eyre* v0.2 annotations have been generated.

## Multi-valued embedding and current acts

`realisation.types`, `current_discourse_act.types`, and
`contextual_modification.effects` are unique, non-empty arrays. This permits a
single occurrence to be, for example, revoiced and metalinguistically mentioned
while also being used as evidence and eliciting reaffirmation. The arrays use
small initial enums plus `other`; selecting `other` requires an open-text
description. `actuality` is separate because narratively supplied wording may
look like quotation while being explicitly unspoken.

This design avoids both a single overloaded embedding enum and a large
premature taxonomy. It does mean that the categories can overlap. The required
analysis field is where the annotator explains the relationship among selected
values.

## Evidence provenance and references

Every evidence item has a unique local `evidence_id`, a source type, a quotation
or description, the supported claim, and confidence. Local evidence may quote a
brief span. Metadata and remembered background evidence should ordinarily be
described, preventing them from masquerading as passage wording.

Disagreements can cite evidence IDs. The standard-library validator checks that
those references exist, a cross-record rule that plain JSON Schema does not
conveniently enforce. Evidence references were not added to every prose analysis
in v0.2, because requiring a graph of claim IDs at this stage would overbuild
the six-case ontology. Evidence remains auditable by its explicit `supports`
text.

## Background knowledge

`background_knowledge.familiarity` records general familiarity even when it was
not used. `used` separately records whether background knowledge materially
contributed to the annotation. If it was not used, contribution and confidence
must be null. If it was used, both are required and the validator also requires
at least one `background_knowledge` evidence item. This makes contribution
auditable while permitting uneven familiarity across works.

The prompt permits reliable remembered wider context but forbids invented
events, wording or plot facts. Confidence applies to the remembered knowledge,
not to the whole classification. A description is preferred over a purported
quotation when exact wording is not reliably remembered.

## Operationalising `mixed_reading`

`mixed_reading` is no longer an unqualified feature. A true value must select
one of two bases and provide justification:

- `substantial_multiple_support` requires at least two T/P/E scores of 2 or
  more; the validator enforces this threshold;
- `qualitative_interaction` permits lower scores only when the explanation says
  why interaction among core readings is central.

A false value requires `basis: "none"` and a null justification. This prevents
weak nonzero secondary effects from automatically producing mixture while
retaining an escape from a purely numerical rule. Whether a claimed qualitative
interaction is persuasive remains a research-review judgment rather than
something structural validation can decide.

## Scoped context and confidence

There is no overall confidence field. Core content, realisation, current act and
contextual modification each have confidence, as do construals, disagreements,
pragmatic assessments, evidence and used background knowledge.

`context_needs` is an array rather than a Boolean. Every item states whether the
missing material is required for core classification or merely useful for
richer interpretation, identifies one or more affected layers, states the
unsettled claim, and requests specific evidence. An empty array means no
specific context need, not that further reading could never add interest.

## Participant roles and disagreement

Participant `role` is a non-empty open string because a closed enum could not
reliably distinguish original avower, current quoter, putative source, current
or original addressee, narrator and reader. `discourse_level` supplies a small
structured anchor. For unavailable construals, the analysis explains what
evidence is absent and confidence is null, making the gap explicit without
inventing uptake.

Disagreement is separate from participant uncertainty. Its open subject and
party names allow the scheme to represent conflicts about force, commitment,
production or interpretation without anticipating all future forms.

## Validation and compatibility

`validate_classification.py` remains dependency-free. Its existing `validate`
function and default CLI behavior continue to validate v0.1. `validate_v0_2`
and `--schema-version 0.2` add v0.2 validation, including semantic consistency
checks for mixture, `other` descriptions, unavailable construals, background
evidence, unique evidence IDs and disagreement references.

The JSON Schema is the API response contract; the Python validator adds the
cross-field and cross-reference checks needed before accepting parsed output.
No input-builder changes are included at this checkpoint. The later metadata
input revision should add reproducible title, author, human-readable and
relative location, and supplied-context extent without deleting raw offsets.
