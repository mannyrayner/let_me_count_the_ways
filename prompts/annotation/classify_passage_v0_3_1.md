# Passage classification prompt v0.3.1 — calibrated E

Analyse the highlighted direct or embedded equivalent of “I love you” in the
supplied passage. Return JSON matching `classification_schema_v0_3.json`.

v0.3.1 retains the v0.3 schema and asks the same deliberately narrow question:
how well can the semantic/pragmatic force of the **core utterance** be
represented by T/P/E, with O available to register genuine failure? Literary
context is evidence for that judgement, not a second exhaustive ontology.

## 1. Identify the core event

State briefly which love utterance is being classified and give its
`utterance_status`: `direct`, `quoted_or_revoiced`, `reported`, `imagined`,
`written`, `nonverbal_verbalised`, `hypothetical`, or `other`. Choose the status
that best identifies the event; use its open description for combinations or
important complications. Quotation alone does not imply O: a quoted utterance
may represent an original T, P, or E event.

## 2. Score the compact core ontology

Give four **independent integer support scores from 0 to 4**. They need not sum
to anything, and several may receive substantial support.

- **T — truth-conditional (`truth_conditional`):** the core utterance
  substantially reports, avows, or presents as true a loving emotional or
  mental state.
- **P — performative (`performative`):** the core utterance substantially
  undertakes, enacts, renews, or invokes a commitment, obligation, or
  relational undertaking. Affection, reassurance, courtship, emotional impact,
  or talk of a shared future does not by itself establish P.
- **E — expressive/reflexive (`exclamatory_reflexive`):** the words substantially
  function as an expressive discharge or reflex-like verbal response produced by
  the speaker’s affective state, rather than merely as a passionately delivered
  assertion or undertaking. The schema field retains its v0.3 name for data
  compatibility; “expressive/reflexive” is the narrower human-readable label.
- **O — other (`other`):** there is an important aspect of the core utterance
  itself that no suitable combination of T/P/E adequately represents.

T concerns mode, not truth: a lie can score T=4. P concerns undertaking force,
not whether a commitment is sincere or will be honoured. E concerns presented
expressive/reflexive force, not whether spontaneity is genuine. Deception,
manipulation, and calculation are therefore orthogonal contextual matters.

### E requires independent core force

**Passion is not E.** Do not assign E merely because the utterance is emotional,
emphatic, apparently spontaneous, passionate, sexually charged, shouted,
whispered, gasped, repeated, punctuated as an exclamation, accompanied by crying
or bodily arousal, or otherwise intense. T and P can themselves be expressed
with arbitrarily strong emotion. These features are contextual evidence about
delivery; none by itself establishes expressive/reflexive core force.

Assign E > 0 only when there is positive evidence that producing the words
functions, at least in part, as an expressive or reflex-like discharge **rather
than merely as an emotionally intense realisation of T and/or P**. Ask the
counterfactual diagnostic: would something important about the core utterance be
lost if it were represented using only its T and P scores, plus contextual
information about intensity, prosody, spontaneity, repetition, and delivery? If
not, assign E=0.

E may coexist with T or P when each function has independent support. For
orientation only: T roughly says “I have loving feelings for you”; P roughly says
“I commit myself to you or us”; E roughly says “the emotional state itself
produces the words.” These glosses clarify the contrast but do not replace the
definitions. A genuine expressive/reflexive case belongs under E rather than O.

Calibration contrasts:

- “I LOVE YOU!” screamed through tears can remain high T and E=0 when it is an
  emphatic avowal; typography, tears, and shouting do not supply E.
- “I love you, and I will stay whatever happens” can support P and T without E.
- after months of reflection, finally shouting “I love you!” can remain dominant
  T despite its intensity.
- “He heard himself blurt ‘I love you!’ before he had thought about what he was
  saying” supplies positive evidence for E, perhaps alongside T if independently
  supported.

### O has a deliberately high burden of proof

**Use O if and only if you believe there is an important aspect of the core
utterance itself that cannot be adequately represented by any suitable
combination of T, P and E.**

Do not use O merely because the surrounding context is ambiguous, deceptive,
ironic, quoted, hedged, manipulative, coercive, narratively complex, or
otherwise difficult. If uncertain between T/P/E, express that uncertainty in
their scores, `confidence`, and `ambiguity`; do **not** use O to express doubt.
Even O=1 must indicate genuine residual pressure against T/P/E, not merely a
conceivable alternative.

Plausible O cases include purely instrumental microphone testing, grammar or
pronunciation practice, rote imitation without semantic grounding, use as a
learned social token without ordinary love-related understanding, deliberately
idiosyncratic meaning, or radically nonhuman/underdetermined production. These
are examples, not a taxonomy.

If O > 0, `other_diagnosis` must explain precisely what T/P/E misses and why
the missing property belongs to core force rather than surrounding context. If
O = 0, both diagnosis fields must be null.

Give one confidence value from 0 to 1 for the complete T/P/E/O judgement, a
concise core analysis, and a short ambiguity note when significant. Ambiguity
within T/P/E is not ontology failure.

## 3. Interpret context without classifying all of it

Use `contextual_interpretation` for a concise but informative open account of
whatever helps justify the scores: deception, self-deception, manipulation,
irony, quotation, revoicing, hedging, participant disagreement, narrative
irony, relationships, or framing. Do not force these potentially unlimited
phenomena into fixed categories.

## 4. Make evidence auditable

Use all legitimately available information needed for the best interpretation:

1. `local_text` in the passage;
2. `supplied_metadata`, including bibliographic and location information; and
3. reliable `background_knowledge` of the wider work.

Do not invent events, wording, or plot facts. Mark uncertain memories as such.
Give each important evidence item a unique ID, provenance, quotation or concise
description, the claim it supports, and confidence. Do not present metadata or
remembered paraphrase as passage wording.

Record separately whether background knowledge was used, familiarity,
confidence, and its contribution. If it was used, include at least one evidence
item with `background_knowledge` provenance; if not, use null confidence and
contribution.

## 5. Assess the ontology, but do not proliferate categories

State whether T/P/E/O gives a `natural`, `strained`, or `inadequate` account.
Describe any residual pressure. Name a candidate recurrent missing dimension
only when the case supplies one; do not promote an interesting single O case
to a fifth category. O cases should first accumulate and then be compared
across independent examples.

The objective is controlled simplification: preserve nuance needed to explain
the core judgement, but do not attempt to formalise all the reasons literature
is interesting. Do not perform or propose large-scale reannotation in this
response.
