# *Jane Eyre* v0.1 six-case diagnostic review (Phase B)

## Scope and readiness

This review completes Phase B of the
[next-development-phase handoff](../next_development_phase_handoff.md). It is a
diagnostic assessment of the six extracted *Jane Eyre* occurrences, not a
frequency study and not evidence that the extraction patterns are exhaustive.
It reviews the preserved v0.1 outputs as outputs of one annotation setup; it
does not independently establish the literary interpretations as ground truth.

All files needed for this review are available in the repository:

- the six-record passage inventory in
  `data/development/passages/gutenberg-1260.jsonl` and the corresponding prepared
  classification inputs;
- the unchanged v0.1 prompt and JSON schema in `prompts/annotation/`;
- for every occurrence, the exact request, raw response, parsed output,
  metadata, pricing snapshot, and cost record under
  `results/development_runs/`;
- the validator and the earlier reviews of the quoted-repetition,
  imagined-utterance, and sisterly-love cases.

The inventory contains six unique occurrence IDs, and each has exactly one
reviewed output. The requests all name `gpt-5.6-sol`; their metadata records the
same prompt hash (`bc2806...48587`) and schema hash
(`f2c3f8...a58789`). All six outputs pass the local v0.1 structural validator
against their expected occurrence IDs. This is therefore a complete and
directly comparable v0.1 diagnostic set.

## Method

The review compared each parsed output with its supplied passage, rather than
silently filling gaps from knowledge of the novel. It considered separately:

1. whether T/P/E describes the represented core love-content;
2. how the occurrence is presented or embedded;
3. what the larger, current discourse act does with that content;
4. participant construal, evidence, uncertainty, and context requests; and
5. whether the available schema records those distinctions without relying on
   prose fields to repair an ill-fitting ontology.

“Works naturally” below means that the output gives a useful analysis with the
available evidence. It does not mean that every emitted feature is well
designed. Conversely, a schema failure need not imply that the model's prose
analysis is poor: several outputs diagnose distinctions that their structured
fields cannot encode.

## Case matrix

| Case and occurrence suffix | Supplied occurrence | T/P/E | v0.1 features | More context | Diagnostic judgment |
| --- | --- | --- | --- | --- | --- |
| candour / `d0cd60fde247` | Direct avowal conceded against refusal to flatter | 4/1/1 | `mixed_reading` | no | Core T/P/E is natural; `mixed_reading` overstates weak secondary effects. |
| future life / `9267e616f948` | Direct avowal used as the reason for welcoming shared life | 4/2/0 | `quoted`, `mixed_reading` | yes | Core analysis is useful; ordinary represented dialogue is mislabeled as analytically significant quotation, and avowal versus commitment context needs clearer separation. |
| repetition / `14913cd0a6a4` | Rochester quotes Jane's prior avowal and demands renewal | 4/1/0 | `quoted`, `metalinguistic`, `deceptive_or_manipulative`, `mixed_reading` | yes | Strongest schema failure: T/P/E fits the original content but not its present use as evidence and pressure. |
| imagined / `f221719b1af4` | Narrator verbalizes a look as words explicitly not spoken | 4/1/0 | `quoted` | yes | T/P/E fits attributed content; the schema cannot record non-actual production, attribution, or intended communication. |
| sisterly / `b57472f62694` | Direct avowal qualified by “as a sister” in a refusal | 4/1/0 | `quoted` | yes | T/P/E is natural; relationship type and the avowal's refusal/reassurance function are orthogonal. |
| comparative care / `b94304d3eea5` | Direct avowal compares love across changed care relations | 4/1/0 | `quoted`, `mixed_reading` | yes | Core T/P/E is natural; current reassurance and relational comparison should not manufacture a mixed core reading. |

The unanimity of the dominant result is itself informative but limited: all six
outputs give truth-conditional support 4, performative support only 1 or 2, and
exclamatory/reflexive support 0 except for one score of 1. Thus the set tests
embedding and discourse structure much better than it tests the boundaries
among three strongly competing core readings. v0.2 should preserve T/P/E, but
these cases alone cannot validate its full range.

## B1. Where v0.1 works naturally

### 1. The core scale captures the common semantic center

Across all six cases, the output consistently identifies an avowal or attributed
state of love as the core content. The explanations do not merely repeat the
label: they relate it to concessive syntax (candour), causal syntax (future
life), temporal comparison (comparative care), coordination with other
attitudes (sisterly love), prior wording (quoted repetition), and bodily signs
plus narrator attribution (imagined utterance). Independent 0–4 support scores
allow the annotations to say “primarily truth-conditional, with a weaker
interpersonal effect” without forcing a single exclusive label.

The exclamatory/reflexive category also behaves sensibly in this set. Sustained,
syntactically integrated, reason-giving speech receives no meaningful support;
only the intensified “most dearly” occurrence receives weak support. Nothing is
forced into the third category simply to use the whole typology.

### 2. Evidence and free-text diagnosis often recover the right distinctions

The `evidence` array is one of v0.1's strongest components. Brief spans are
paired with explicit inferential claims, making it possible to audit whether a
score or contextual interpretation is passage-supported. In particular, the
quoted-repetition output uses the surrounding references to “words,” hearing,
denial, and repetition to establish revoicing and pressure. The imagined case
uses “seemed to say” and “if he did not say it with his lips” to distinguish
represented content from an actual utterance.

The ontology escape hatches also work. `typology_adequate`,
`typology_diagnosis`, and `proposed_missing_dimensions` let the
quoted-repetition output reject T/P/E at the present discourse level, while the
imagined output can call its production problem orthogonal to an otherwise
adequate core classification. That is preferable to inventing a fourth peer of
T/P/E for every kind of embedding.

### 3. Participant perspectives add real interpretive value

The construal records productively distinguish the putative speaker, hearer,
narrator/text, and reader. The clearest successes are the quoted case, where the
current speaker is not the referent of the quoted “I,” and the imagined case,
where the narrator supplies detailed wording that the apparent hearer may not
have recovered. The outputs also generally avoid manufacturing a hearer
response when none is supplied.

The sisterly qualifier demonstrates another useful result: a relationship
construal can constrain what kind of love is asserted without changing its
core T/P/E force. Likewise, love can motivate candour, shared-life hope, or care
without those surrounding functions becoming the meaning of the core clause.

### 4. Uncertainty is usually localized in the prose

The outputs commonly distinguish a confident core judgment from uncertainty
about reception, sincerity, intended communication, or the wider exchange.
The no-context-needed decision for the candour passage is especially well
calibrated because the supplied text settles the requested core analysis. The
other context requests name concrete missing evidence rather than invoking
general familiarity with *Jane Eyre*.

## B2. Where v0.1 strains or fails

### 1. One level of T/P/E is asked to cover two different analytical objects

The major recurring problem is not a missing fourth core force. It is the lack
of separate fields for the **core represented love-content** and the **current
act that presents or uses it**.

- In quoted repetition, Jane's earlier words are a predominantly
  truth-conditional avowal, while Rochester's current act quotes them as
  evidence, constrains retraction, and elicits or pressures a repetition.
- In the imagined case, the attributed proposition describes love, but the
  current text is the narrator's verbalization of a look rather than the man's
  actual speech act.
- In the sisterly case, a direct avowal also helps refuse a journey or romantic
  construal while preserving affiliation.
- In the candour, future-life, and comparative-care cases, the love-content is
  respectively used to license honesty, explain hope, and contrast relational
  circumstances.

v0.1 can describe these facts only in `construals`, `evidence`, or
`typology_diagnosis`. Consequently, equivalent observations are not available
as consistently queryable data. The smallest useful repair is layered rather
than proliferative: retain core T/P/E, add occurrence/embedding status, add the
current discourse act, and explicitly state the effect of the latter two on the
core analysis.

### 2. `quoted` collapses typography, represented dialogue, and revoicing

Five outputs have `quoted`, including ordinary direct dialogue, genuine
quotation of prior words, and narrator-supplied imaginary wording. The only
unflagged case is also typographically presented as dialogue. This makes the
flag both inconsistent and analytically underdetermined.

At minimum, the representation needs to distinguish:

- present direct speech represented by the novel;
- present quotation or repetition of a prior utterance;
- narratively attributed or imagined wording, including verbalization of
  nonverbal behavior; and
- actual production versus non-production or uncertain production.

These may be multi-valued properties, not a single mutually exclusive enum.
For example, the imagined occurrence is typographically direct quotation but
not an actual spoken utterance. `metalinguistic` remains useful in the
repetition case, but does not replace a representation of revoicing.

### 3. `mixed_reading` is over-triggered and internally inconsistent

Four outputs are marked mixed even though their support profiles are 4/1/1,
4/2/0, 4/1/0, and 4/1/0. Meanwhile, the imagined and sisterly 4/1/0 cases are
not mixed. No prompt or schema rule explains the difference.

Secondary interpersonal consequences of making an avowal do not by themselves
show substantial support for more than one **core** reading. On these results,
the candour and comparative-care cases should not be mixed. The future-life
case may warrant discussion because of its wedding and shared-future context,
but the output itself calls the phrase an explanation rather than a promise.
The repetition case genuinely combines analytical levels, not necessarily core
T/P/E readings; its pressure belongs in the current-act layer.

For v0.2, either derive `mixed_reading` from a documented threshold or require a
short justification of a qualitatively important interaction between core
readings. Do not use it merely because `performative` or
`exclamatory_reflexive` is nonzero. The six cases favor the latter, more
interpretive rule, because a numerical threshold alone cannot distinguish a
core mixture from embedding-level complexity.

### 4. Manipulation and deception are wrongly coupled

The quoted-repetition output uses `deceptive_or_manipulative` because the
speaker pressures the prior avower, while explicitly noting that the passage
does not establish deception. A combined Boolean therefore asserts a
disjunction too coarse to preserve the actual finding. The six-case evidence
supports separating `deceptive` from `manipulative_or_pressuring`.

`strategically_ambiguous` should remain separate rather than being inferred
from either. None of these passages supplies positive evidence of deception or
strategic ambiguity. The revised scheme should permit `unknown` or
`not_assessable`, rather than making absence from a feature list ambiguously
mean false, unsupported, or simply unmentioned.

### 5. Construals are useful but structurally loose

The schema allows any number of construals, duplicated perspectives, and
omission without explanation. The sisterly output omits a hearer construal;
other outputs sensibly state that the hearer's response is unavailable. Those
two practices become indistinguishable in downstream data. Furthermore,
“speaker” becomes ambiguous in embedded cases: original avower, current
quoter, putative source of an imagined utterance, and narrator are different
roles.

v0.2 should key construals to an explicit discourse level or participant role,
and allow a status such as `supported`, `uncertain`, or `not_available`. It
should not require invented analyses for every perspective. No participant
disagreement is demonstrated in this set, but quoted repetition shows how
uptake and pressure could differ from the original speaker's construal; the
scheme should be able to record such divergence without equating it with core
ambiguity.

### 6. Context need and confidence have no declared scope

Five outputs request more context, often to learn a hearer's response or test
sincerity, while still assigning overall confidence from 0.94 to 0.95. This is
not logically inconsistent—the core classification can be confident while the
current act is uncertain—but the schema does not say what `confidence` scopes
over. Nor does `needs_more_context` distinguish context required to classify
the occurrence from context merely useful for enriching the interpretation.

The future-life and comparative-care requests illustrate a risk of routine
context appetite: almost any passage could benefit from a subsequent response.
The revised contract should distinguish `required_for_core_analysis` from
`useful_for_contextual_analysis`, identify the affected field or claim, and
give confidence per layer or explicitly define one overall scope.

### 7. Input metadata is reproducible but insufficiently orienting

The prepared inputs already preserve work ID, source ID, language, extraction
pattern, exact match, source character offsets, context bounds, and extraction
timestamp. They do not provide title, author, source length or relative
position, chapter/section, or an explicit context-size description. The raw
offsets are reproducible but hard to interpret in isolation.

v0.2 should add deterministic bibliographic and location metadata where
available, plus left/right or total supplied context. Metadata must remain
orientation rather than interpretive evidence. Speaker and addressee identities
should not be manually supplied unless a reproducible source or prior
annotation stage produced them.

### 8. Several distinctions remain untested

This set contains no clear negation, hypothetical “I love you,” ironic use,
conventional script, strategic ambiguity, established deception, or overt
participant disagreement. It offers little support for E and only weak support
for P. The absence of those phenomena is a reason to preserve ontology escape
hatches and test new texts, not a reason to remove the categories. Likewise,
the six cases support relationship type as an orthogonal note or dimension,
but only one explicitly marks sisterly love; that is not enough to freeze a
universal relationship ontology.

## Minimal design conclusions for Phase C

The six-case review supports the following bounded conclusions, to be turned
into a separately versioned v0.2 proposal rather than edits to v0.1:

1. **Retain T/P/E as scored core-force hypotheses.** The framework works
   naturally for the represented content in all six cases, even when it fails
   to describe the present use.
2. **Add three orthogonal layers:** occurrence/embedding status, current
   discourse act, and an explicit account of how context affects the core.
3. **Make production and attribution explicit.** Record whether words were
   spoken, quoted from prior speech, reported, narratively imagined, or supplied
   as a verbalization of nonverbal behavior; allow combinations and an `other`
   escape hatch.
4. **Tighten mixedness.** Require substantial multi-reading support or a stated
   qualitative interaction at the core level; do not infer it from weak
   interpersonal effects.
5. **Split pressure from deception.** Keep manipulation/pressure, deception,
   and strategic ambiguity independently assessable, with evidential status.
6. **Scope construal, uncertainty, confidence, and context requests.** Tie them
   to discourse level and affected claim, and distinguish necessary context
   from context that would merely enrich the record.
7. **Add reproducible orientation metadata without turning it into evidence.**
8. **Preserve open text and inadequacy fields.** The next schema should not
   pretend its initial embedding and current-act inventories are exhaustive.

These are the smallest recurring dimensions warranted by the set. A dedicated
relationship-type field is plausible but not yet compelled; free text or an
open modifier field is safer until further texts show recurrence. Similarly,
the current cases do not warrant new universal categories for candour,
caregiving, refusal, or shared-life hope. Those are candidate current acts or
contextual effects to test, not additions to the core T/P/E partition.

## Overall Phase B assessment

v0.1 succeeds as a diagnostic instrument precisely because its evidence,
perspective, context, and inadequacy fields expose where its compact feature
inventory fails. It gives a clear and useful account of the core love-content
in all six passages. Its principal failure is structural: it conflates the
force of represented “I love you” content with the larger act that quotes,
attributes, qualifies, explains with, or otherwise deploys that content.

The evidence therefore supports the handoff's working hypothesis that embedding
is largely orthogonal to T/P/E. It does not yet prove that the distinction will
generalize, and it does not justify freezing an exhaustive embedding ontology.
Phase C should implement the layered hypothesis conservatively, preserve v0.1
unchanged, and use these six cases as explicit regression examples.
