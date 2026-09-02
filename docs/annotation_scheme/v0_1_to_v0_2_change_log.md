# Annotation scheme v0.1 → v0.2 change log

## Status

v0.2 is a provisional annotation contract derived from the six-case *Jane
Eyre* Phase B review and the subsequent combined design brief. It is ready for
design review, not yet for reannotation. v0.1 remains unchanged and supported.

## Added and restructured fields

### `core_love_content`

The v0.1 top-level `label_support` moves into a named core layer and retains the
same three independent 0–4 T/P/E scores. The new `analysis` and layer-specific
`confidence` make the scope explicit. This responds to the repeated finding
that T/P/E classified represented love-content well but could not describe its
present quotation, attribution or use.

`mixed_reading` moves out of the undifferentiated `features` list and becomes an
object with `is_mixed`, `basis`, and `justification`. Four v0.1 cases were marked
mixed across inconsistent low-secondary-support profiles. v0.2 distinguishes
substantial multiple support from a qualitatively central interaction and makes
the non-mixed state explicit.

`relationship_modifier` is new, nullable open text. “As a sister” showed that
kind of love can matter without becoming a T/P/E category; one case does not
justify a closed relationship ontology.

### `realisation`

This new layer replaces the overloaded `quoted` feature. Its multi-valued
`types` distinguish direct represented speech, quotation/revoicing, reported or
imagined speech, narratively attributed wording, verbalisation of nonverbal
behaviour, hypotheticality, hedging, negation, and metalinguistic mention. An
`other` escape hatch remains. `actuality` separately records whether the words
were spoken, written, not spoken, uncertain, or inapplicable.

This change is motivated by v0.1 applying `quoted` both to ordinary printed
dialogue and to analytically distinct revoicing, while the imagined-utterance
case gives printed wording to something explicitly not said aloud.

### `current_discourse_act`

This new multi-valued layer records what the present speaker, narrator or text
does with the core content. Its deliberately small inventory covers direct
avowal, reassurance, explanation, quotation, elicitation, pressure, use as
evidence, distancing, hedging, rejection, reinterpretation, manipulation and
irony, with `other` plus explanation.

The quoted-repetition case motivated the separation most directly: Jane's
represented love-content is predominantly truth-conditional, while Rochester's
present act quotes it as evidence and pressures her to reaffirm it. The other
cases show explanation, reassurance, refusal and relational comparison without
necessarily increasing core performative force.

### `contextual_modification`

This new layer records whether context preserves, weakens, strengthens,
redirects, quotes, distances, challenges, manipulates, or otherwise changes the
core interpretation. v0.1 could state these relations only inconsistently in
free-text construals, evidence or typology diagnosis.

### `participant_construals` and `disagreements`

The v0.1 `construals` array becomes `participant_construals`. Its role is open
text rather than a four-value perspective enum, and every entry names its
discourse level and evidential status. `unavailable` requires an explanation
and null confidence so omission is distinguishable from explicitly unavailable uptake.
This addresses ambiguous “speaker” roles in quoted and imagined cases without
forcing invented hearer interpretations.

`disagreements` is a new first-class array linking named parties, a subject,
description, evidence IDs and confidence. v0.1 offered only a generic
`participant_disagreement` feature and could not represent who disagreed about
what or whether the disagreement concerned core force or current commitment.

### Independent pragmatic assessments

The v0.1 `deceptive_or_manipulative` and `strategically_ambiguous` feature values
become three required independent assessments:

- `deception_misrepresentation`;
- `manipulation_pressure`; and
- `strategic_ambiguity`.

Each records `supported`, `unsupported`, or `uncertain_not_assessable` with an
analysis and confidence. In the quoted-repetition result, pressure was supported
while deception was explicitly not established; the former combined Boolean
could not preserve that distinction. Required assessments also remove the
ambiguity between false, omitted, and not assessable.

### `evidence` and `background_knowledge`

Evidence items retain a supporting claim but add a unique ID, confidence and
first-class provenance: `local_text`, `supplied_metadata`, or
`background_knowledge`. `quotation_or_description` accommodates both exact
local spans and descriptions of metadata or remembered context without
pretending all evidence is quoted passage text.

The new `background_knowledge` object records whether remembered wider-work
knowledge was actually used, familiarity, confidence, contribution and notes.
This reverses v0.1's prohibition on using unsupplied wider-work knowledge. v0.2
permits reliable background knowledge because deception, irony and relational
history may be non-local, but makes its use inspectable and uncertain memories
explicit. The validator requires any claimed use to have at least one evidence
item with matching provenance.

### `context_needs` and scoped confidence

The v0.1 Boolean `needs_more_context` and nullable `context_request` become an
array. Each request distinguishes context required for core classification from
context useful for richer interpretation, names affected layers, identifies the
claim, and requests specific material. Five of six v0.1 results requested more
context despite very high overall confidence, showing that both concepts needed
clear scope.

The single v0.1 top-level `confidence` is removed. Confidence now appears on
each analytical layer, construal, disagreement, assessment, evidence item and
background-knowledge use. A confident T judgment can therefore coexist with
uncertain uptake or manipulation.

### `ontology_assessment` and `notes`

The v0.1 `typology_adequate`, `typology_diagnosis`, and
`proposed_missing_dimensions` fields are grouped without losing their escape-
hatch function. Nullable top-level `notes` preserves important observations
that the provisional structured fields do not capture.

## Removed v0.1 fields and feature list

There is no v0.2 top-level `features` list. Its values were redistributed:

| v0.1 value | v0.2 representation |
| --- | --- |
| `quoted` | Specific `realisation.types`, plus current quotation or contextual quoting where applicable |
| `negated`, `metalinguistic` | `realisation.types` |
| `conventionally_scripted` | No fixed replacement; use current-act `other`, notes, or a proposed missing dimension until evidence supports a stable field |
| `strategically_ambiguous` | Independent structured assessment |
| `deceptive_or_manipulative` | Split into deception and manipulation/pressure assessments |
| `participant_disagreement` | Structured `disagreements` records |
| `mixed_reading` | Structured core mixture object |
| `none_of_these` | Unnecessary because every open inventory has `other` and explicit analysis |

The removals reduce ambiguous Booleans without treating the six cases as
evidence for a final ontology. No v0.1 files or validation paths were removed.
