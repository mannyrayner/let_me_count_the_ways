# Single-text pipeline report: Jane Eyre

## Run summary

- **Run ID:** `gutenberg-1260`
- **Work:** *Jane Eyre* by Charlotte Brontë
- **Source:** `gutenberg-1260`
- **Annotation:** v0.3 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 6
- **Valid occurrences:** 6
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 2
- **Estimated total cost:** USD 0.310928

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `bronte-jane-eyre-d0cd60fde247`

- **Exact match:** `I love you`
- **Pattern:** `en_i_love_you` (v0.1)
- **Source offsets:** 581886–581896
- **Relative position:** 0.558577
- **Chapter/section:** CHAPTER XXIV
- **Supplied context:** 368 characters (295 before; 63 after)

#### Passage

> “And then you won’t know me, sir; and I shall not be your Jane Eyre any
> longer, but an ape in a harlequin’s jacket—a jay in borrowed plumes. I
> would as soon see you, Mr. Rochester, tricked out in stage-trappings,
> as myself clad in a court-lady’s robe; and I don’t call you handsome,
> sir, though I love you most dearly: far too dearly to flatter you.
> Don’t flatter me.”

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-1260\annotations\bronte-jane-eyre-d0cd60fde247\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** Jane directly avows her enduring and unusually intense love for Rochester. The concessive clause presents that love as a true emotional state while supporting her claim that genuine love requires honesty rather than flattery. It does not itself undertake a new commitment, and its controlled argumentative form is not substantially reflexive or exclamatory.
- **Ontology fit:** natural — T/P/E/O gives a natural account: strong T captures the explicit avowal, while the absence of undertaking force and reflex-like delivery justifies negligible P and E. The utterance’s argumentative role and emphasis are contextual nuances rather than an uncaptured core-force dimension.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "bronte-jane-eyre-d0cd60fde247",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.98,
    "analysis": "Jane directly avows her enduring and unusually intense love for Rochester. The concessive clause presents that love as a true emotional state while supporting her claim that genuine love requires honesty rather than flattery. It does not itself undertake a new commitment, and its controlled argumentative form is not substantially reflexive or exclamatory.",
    "ambiguity": "The intensifiers “most dearly” and “far too dearly” convey strong emotion, but the utterance remains a deliberate propositional avowal rather than an emotionally triggered exclamation."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A direct spoken avowal by Jane to Rochester, embedded in the concessive clause “though I love you most dearly.”"
  },
  "contextual_interpretation": "Jane rejects Rochester’s proposed ornamental transformation of her and refuses reciprocal flattery. Her declaration reassures him that her adverse judgment of his looks is compatible with profound love, but its immediate pragmatic role is to ground uncompromising honesty: she loves him too dearly to flatter him. The surrounding engagement context heightens its relational significance without turning this particular clause into a commitment-making act.",
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“though I love you most dearly”",
      "supports": "The first-person present-tense clause explicitly presents Jane’s loving emotional state as true, strongly supporting truth-conditional force.",
      "confidence": 1.0
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“far too dearly to flatter you. Don’t flatter me.”",
      "supports": "Jane uses the avowal as a reason for honesty and mutual non-flattery, showing a controlled argumentative function rather than reflexive exclamation or a new undertaking.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "Jane contrasts being dressed as “an ape in a harlequin’s jacket” or “a jay in borrowed plumes” with her own candid assessment of Rochester.",
      "supports": "The surrounding reasoning frames the love declaration as a sincere avowal compatible with criticism, not as conventional courtship praise.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XXIV of Charlotte Brontë’s Jane Eyre.",
      "supports": "The location identifies the exchange as part of the post-engagement courtship sequence and helps situate its relational context.",
      "confidence": 1.0
    },
    {
      "evidence_id": "E5",
      "source": "background_knowledge",
      "quotation_or_description": "In Chapter XXIV, after their engagement, Rochester attempts to adorn and indulge Jane, while Jane resists being remade into a decorative conventional bride and insists on retaining her identity and equality.",
      "supports": "This wider scene explains why the avowal functions chiefly as evidence that resistance and candour coexist with love, rather than as the creation of a fresh commitment.",
      "confidence": 0.96
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.96,
    "contribution": "Knowledge of the post-engagement Chapter XXIV scene clarifies Jane’s resistance to Rochester’s attempts to ornament her and supports reading the declaration as a candid state-avowal rather than a new relational undertaking."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T/P/E/O gives a natural account: strong T captures the explicit avowal, while the absence of undertaking force and reflex-like delivery justifies negligible P and E. The utterance’s argumentative role and emphasis are contextual nuances rather than an uncaptured core-force dimension.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 2. `bronte-jane-eyre-9267e616f948`

- **Exact match:** `I love you`
- **Pattern:** `en_i_love_you` (v0.1)
- **Source offsets:** 627702–627712
- **Relative position:** 0.602557
- **Chapter/section:** CHAPTER XXV
- **Supplied context:** 1258 characters (248 before; 1000 after)

#### Passage

> “All day yesterday I was very busy, and very happy in my ceaseless
> bustle; for I am not, as you seem to think, troubled by any haunting
> fears about the new sphere, et cetera: I think it a glorious thing to
> have the hope of living with you, because I love you. No, sir, don’t
> caress me now—let me talk undisturbed. Yesterday I trusted well in
> Providence, and believed that events were working together for your
> good and mine: it was a fine day, if you recollect—the calmness of the
> air and sky forbade apprehensions respecting your safety or comfort on
> your journey. I walked a little while on the pavement after tea,
> thinking of you; and I beheld you in imagination so near me, I scarcely
> missed your actual presence. I thought of the life that lay before
> me—_your_ life, sir—an existence more expansive and stirring than my
> own: as much more so as the depths of the sea to which the brook runs
> are than the shallows of its own strait channel. I wondered why
> moralists call this world a dreary wilderness: for me it blossomed like
> a rose. Just at sunset, the air turned cold and the sky cloudy: I went
> in, Sophie called me upstairs to look at my wedding-dress, which they
> had just brought; and under it in the box I found your present—the veil
> which, in your

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-1260\annotations\bronte-jane-eyre-9267e616f948\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** Jane deliberately avows her love as the reason she welcomes the prospect of living with Rochester. The clause primarily presents her emotional state as true. Its placement within an engagement gives it slight relationally reaffirming force, but it does not itself clearly promise or undertake anything, and its reflective delivery is not exclamatory or reflex-like.
- **Ontology fit:** natural — T/P/E adequately represents the utterance: it is predominantly a truth-conditional avowal, with only slight commitment-renewing resonance and no substantial exclamatory force. No important aspect of its core force remains outside the ontology.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "bronte-jane-eyre-9267e616f948",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "Jane deliberately avows her love as the reason she welcomes the prospect of living with Rochester. The clause primarily presents her emotional state as true. Its placement within an engagement gives it slight relationally reaffirming force, but it does not itself clearly promise or undertake anything, and its reflective delivery is not exclamatory or reflex-like.",
    "ambiguity": "The surrounding discussion of a shared future creates weak performative pressure, though that future-oriented context does not turn the core clause into an explicit commitment."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A direct spoken utterance by Jane to Rochester, syntactically embedded as the causal clause in her statement that she hopes to live with him."
  },
  "contextual_interpretation": "Jane is reassuring Rochester that she is happy rather than fearful about their anticipated life together. Her request to be allowed to speak undisturbed and her extended account of the previous day frame the avowal as considered and explanatory, not as an impulsive outburst. Their engagement and impending wedding lend the words some relational reaffirmation, but the immediate force remains a sincere-seeming declaration of emotional state.",
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“I think it a glorious thing to have the hope of living with you, because I love you.”",
      "supports": "The causal construction explicitly presents love as Jane's existing reason for welcoming a shared life, strongly supporting truth-conditional avowal.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“No, sir, don’t caress me now—let me talk undisturbed.”",
      "supports": "Jane's insistence on speaking without interruption frames the utterance as deliberate discourse rather than an emotionally triggered exclamation.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "Jane discusses “the life that lay before me—your life, sir” and mentions her wedding-dress.",
      "supports": "The anticipated shared future and wedding context provide limited support for relational reaffirmation while not themselves making the love clause a promise.",
      "confidence": 0.96
    },
    {
      "evidence_id": "E4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XXV of Charlotte Brontë's Jane Eyre.",
      "supports": "This locates the exchange in the novel's pre-wedding section and corroborates the immediate engagement context.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E5",
      "source": "background_knowledge",
      "quotation_or_description": "In the wider novel, the speakers are Jane Eyre and Edward Rochester, who are engaged and preparing for their planned marriage at this point.",
      "supports": "Identifies the participants and explains the modest performative pressure supplied by an existing courtship commitment.",
      "confidence": 0.98
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.98,
    "contribution": "Used to identify Jane and Rochester as the speakers and to confirm that the exchange occurs during their engagement before the planned wedding; the core-force judgment is also directly supported by the supplied passage."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T/P/E adequately represents the utterance: it is predominantly a truth-conditional avowal, with only slight commitment-renewing resonance and no substantial exclamatory force. No important aspect of its core force remains outside the ontology.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 3. `bronte-jane-eyre-14913cd0a6a4`

- **Exact match:** `I love you`
- **Pattern:** `en_i_love_you` (v0.1)
- **Source offsets:** 631776–631786
- **Relative position:** 0.606468
- **Chapter/section:** CHAPTER XXV
- **Supplied context:** 497 characters (451 before; 36 after)

#### Passage

> “And these dreams weigh on your spirits now, Jane, when I am close to
> you? Little nervous subject! Forget visionary woe, and think only of
> real happiness! You say you love me, Janet: yes—I will not forget that;
> and you cannot deny it. _Those_ words did not die inarticulate on your
> lips. I heard them clear and soft: a thought too solemn perhaps, but
> sweet as music—‘I think it is a glorious thing to have the hope of
> living with you, Edward, because I love you.’ Do you love me,
> Jane?—repeat it.”

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-1260\annotations\bronte-jane-eyre-14913cd0a6a4\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** Jane's embedded “I love you” is principally an avowal presenting her love for Edward as true. Its connection to the hope of living with him gives it slight commitment-related shading, especially in their engaged relationship, but the love clause does not itself clearly undertake or renew an obligation. Its described solemn, clear, and soft delivery is deliberate rather than reflex-like or exclamatory.
- **Ontology fit:** natural — T/P/E adequately represents the core force: a strong avowal with slight relationship-commitment shading and no substantial exclamatory force. Quotation, Rochester's pressure for repetition, and the ominous narrative context are contextual complications rather than residual ontology failures.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "bronte-jane-eyre-14913cd0a6a4",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.95,
    "analysis": "Jane's embedded “I love you” is principally an avowal presenting her love for Edward as true. Its connection to the hope of living with him gives it slight commitment-related shading, especially in their engaged relationship, but the love clause does not itself clearly undertake or renew an obligation. Its described solemn, clear, and soft delivery is deliberate rather than reflex-like or exclamatory.",
    "ambiguity": "The text gives Rochester's exact revoicing of Jane's earlier words rather than the original speaking event directly; however, both his framing and the quoted sentence strongly support an original truth-conditional avowal."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "quoted_or_revoiced",
    "description": "Rochester quotes and revoices an earlier utterance by Jane, embedding “I love you” within her stated hope of living with Edward."
  },
  "contextual_interpretation": "Rochester treats Jane's earlier words as a definite, audible declaration and insistently asks her to repeat them. His possessive reassurance-seeking and their prospective shared life add relational pressure, but they do not transform the core clause into a clear undertaking. The nearby references to Jane's troubling dreams contrast her anxiety with Rochester's appeal to their supposedly “real happiness.”",
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“I think it is a glorious thing to have the hope of living with you, Edward, because I love you.”",
      "supports": "The causal clause explicitly presents Jane's loving emotional state as the reason for her hope of living with Edward, strongly supporting truth-conditional force and only weakly suggesting relational commitment.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "Rochester says, “You say you love me, Janet” and “you cannot deny it.”",
      "supports": "He construes the earlier utterance as a definite avowal that Jane has made, reinforcing the truth-conditional reading.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "Rochester describes the words as heard “clear and soft” and as “a thought too solemn perhaps, but sweet as music.”",
      "supports": "The utterance is framed as articulate and solemn rather than as an involuntary or weakly propositional exclamation.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "“Do you love me, Jane?—repeat it.”",
      "supports": "Rochester's request confirms that the highlighted wording is his quotation of Jane's prior speech and shows his use of it for reassurance.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E5",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XXV of Charlotte Brontë's Jane Eyre.",
      "supports": "This anchors the passage bibliographically and locates it in the late courtship and pre-wedding portion of the novel.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E6",
      "source": "background_knowledge",
      "quotation_or_description": "In Chapter XXV, Jane and Rochester are engaged and approaching their planned wedding while Jane reports ominous dreams and anxieties.",
      "supports": "The engagement explains the weak commitment shading and the contrast between Jane's apprehension and Rochester's demand for reassurance, without displacing the core avowal reading.",
      "confidence": 0.94
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.94,
    "contribution": "Knowledge of the engagement and imminent planned wedding supports the slight performative shading and clarifies Rochester's reassurance-seeking, while the local text determines the principal truth-conditional classification."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T/P/E adequately represents the core force: a strong avowal with slight relationship-commitment shading and no substantial exclamatory force. Quotation, Rochester's pressure for repetition, and the ominous narrative context are contextual complications rather than residual ontology failures.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The classification targets Jane's earlier utterance as precisely revoiced by Rochester, not Rochester's separate question asking whether she loves him."
}
```

</details>

### 4. `bronte-jane-eyre-f221719b1af4`

- **Exact match:** `I / love you`
- **Pattern:** `en_i_love_you` (v0.1)
- **Source offsets:** 830232–830242
- **Relative position:** 0.796974
- **Chapter/section:** CHAPTER XXXII
- **Supplied context:** 625 characters (352 before; 263 after)

#### Passage

> Of course, she knew her power: indeed, he did not, because he could
> not, conceal it from her. In spite of his Christian stoicism, when she
> went up and addressed him, and smiled gaily, encouragingly, even fondly
> in his face, his hand would tremble and his eye burn. He seemed to say,
> with his sad and resolute look, if he did not say it with his lips, “I
> love you, and I know you prefer me. It is not despair of success that
> keeps me dumb. If I offered my heart, I believe you would accept it.
> But that heart is already laid on a sacred altar: the fire is arranged
> round it. It will soon be no more than a sacrifice consumed.”

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-1260\annotations\bronte-jane-eyre-f221719b1af4\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 1 / 0
- **Core analysis:** The narrator verbalises St John’s look as an avowal of an existing loving state. Its force is predominantly truth-conditional: he appears to communicate that he loves Rosamond. It does not undertake a relationship or commitment; the accompanying revoiced speech instead explains why he will remain silent and sacrifice that love. His involuntary bodily reactions give slight support to reflex-like emotional expression, but the rendered utterance itself is propositionally explicit.
- **Ontology fit:** natural — T/P/E adequately represents the core force: a strongly propositional avowal inferred from nonverbal expression, with slight reflexive coloring and no substantial relational undertaking. Its mediated, unspoken form is captured by utterance status rather than requiring O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "bronte-jane-eyre-f221719b1af4",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 1,
      "other": 0
    },
    "confidence": 0.95,
    "analysis": "The narrator verbalises St John’s look as an avowal of an existing loving state. Its force is predominantly truth-conditional: he appears to communicate that he loves Rosamond. It does not undertake a relationship or commitment; the accompanying revoiced speech instead explains why he will remain silent and sacrifice that love. His involuntary bodily reactions give slight support to reflex-like emotional expression, but the rendered utterance itself is propositionally explicit.",
    "ambiguity": "The words are Jane’s interpretation of nonverbal signs rather than St John’s spoken formulation, so the exact intentional force of his expression is inferential."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "nonverbal_verbalised",
    "description": "St John does not say the words aloud; Jane renders his sad, resolute look and visible emotional reactions as the equivalent of an extended first-person utterance."
  },
  "contextual_interpretation": "Jane interprets St John’s trembling hand, burning eye, and look as disclosing love for Rosamond and confidence that she would accept him. The disclosure is framed by renunciation: he remains verbally silent because he considers his heart already consecrated to a sacred vocation. Thus the imagined address avows love while explicitly withholding any offer or relational undertaking.",
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“He seemed to say, with his sad and resolute look, if he did not say it with his lips, ‘I love you’”",
      "supports": "Establishes that the core event is a narrator-verbalised nonverbal avowal rather than an audible direct utterance.",
      "confidence": 1.0
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“his hand would tremble and his eye burn” when she addressed and smiled at him",
      "supports": "Shows involuntary emotional manifestation, providing limited exclamatory or reflexive force while evidencing the attributed loving state.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“It is not despair of success that keeps me dumb. If I offered my heart, I believe you would accept it.”",
      "supports": "Distinguishes avowal from undertaking: the imagined speaker believes courtship could succeed but remains silent and makes no offer.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "“But that heart is already laid on a sacred altar ... It will soon be no more than a sacrifice consumed.”",
      "supports": "Frames the love as renounced in favor of a sacred commitment, weighing strongly against performative relational force.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E5",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XXXII of Charlotte Brontë’s Jane Eyre.",
      "supports": "Locates the passage within the supplied work and supports interpretation in its relevant narrative episode.",
      "confidence": 1.0
    },
    {
      "evidence_id": "E6",
      "source": "background_knowledge",
      "quotation_or_description": "In this episode, the unnamed figures are St John Rivers and Rosamond Oliver; St John loves Rosamond but rejects marriage to her in favor of his missionary vocation.",
      "supports": "Clarifies the participants and confirms that the sacred-sacrifice language refers to renouncing romantic love rather than undertaking a relationship.",
      "confidence": 0.96
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.96,
    "contribution": "It identifies St John Rivers and Rosamond Oliver and situates the avowal within St John’s decision to subordinate his love to his missionary vocation."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T/P/E adequately represents the core force: a strongly propositional avowal inferred from nonverbal expression, with slight reflexive coloring and no substantial relational undertaking. Its mediated, unspoken form is captured by utterance status rather than requiring O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 5. `bronte-jane-eyre-b57472f62694`

- **Exact match:** `I love you`
- **Pattern:** `en_i_love_you` (v0.1)
- **Source offsets:** 936871–936881
- **Relative position:** 0.899341
- **Chapter/section:** CHAPTER XXXV
- **Supplied context:** 348 characters (240 before; 98 after)

#### Passage

> “There is no dishonour, no breach of promise, no desertion in the case.
> I am not under the slightest obligation to go to India, especially with
> strangers. With you I would have ventured much, because I admire,
> confide in, and, as a sister, I love you; but I am convinced that, go
> when and with whom I would, I should not live long in that climate.”

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-1260\annotations\bronte-jane-eyre-b57472f62694\attempt-002`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** Jane directly and deliberately avows that she loves her addressee specifically “as a sister.” The utterance presents an emotional and relational attitude as true within a reasoned explanation. It neither undertakes a new commitment nor has the weakly propositional, reflex-like character of an exclamation.
- **Ontology fit:** natural — Truth-conditional avowal naturally captures the core force. The contextual work performed by the sisterly qualification—affirming affection while refusing marriage—does not require an additional core-force category.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "bronte-jane-eyre-b57472f62694",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.97,
    "analysis": "Jane directly and deliberately avows that she loves her addressee specifically “as a sister.” The utterance presents an emotional and relational attitude as true within a reasoned explanation. It neither undertakes a new commitment nor has the weakly propositional, reflex-like character of an exclamation.",
    "ambiguity": "The avowal affirms an existing bond, but its explicit sisterly qualification and argumentative setting provide little basis for performative undertaking force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Jane directly addresses St. John within dialogue, stating “as a sister, I love you” as part of her explanation of why she might have ventured abroad with him."
  },
  "contextual_interpretation": "The declaration is carefully qualified as sisterly love and embedded in Jane’s reasoned refusal to accept that she is obliged to go to India. It distinguishes genuine admiration, confidence, and familial affection from the marital or vocational commitment St. John seeks. Thus it is principally an avowal of an existing feeling, not an acceptance of his proposed relational undertaking.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“because I admire, confide in, and, as a sister, I love you”",
      "supports": "The coordinated mental and emotional predicates, especially the explicit sisterly qualification, strongly support a truth-conditional avowal of affection.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“There is no dishonour, no breach of promise, no desertion in the case. I am not under the slightest obligation to go to India”",
      "supports": "Jane explicitly denies obligation, making it unlikely that the love utterance undertakes or renews the commitment under discussion.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "The utterance appears within an extended, syntactically controlled explanation of what Jane would have risked and why she expects not to survive the climate.",
      "supports": "The deliberative argumentative form weighs against exclamatory or reflex-like force.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XXXV of Charlotte Brontë’s Jane Eyre.",
      "supports": "The location identifies the late-novel context relevant to Jane’s dispute with St. John over India and marriage.",
      "confidence": 1
    },
    {
      "evidence_id": "e5",
      "source": "background_knowledge",
      "quotation_or_description": "In Chapter XXXV, St. John presses Jane to accompany him to India as his wife; Jane distinguishes her sisterly affection for him from the kind of love and marital union he requests.",
      "supports": "The wider scene confirms that this avowal explains and limits Jane’s affection rather than accepting a marital undertaking.",
      "confidence": 0.96
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.96,
    "contribution": "Knowledge of St. John’s marriage-and-India proposal clarifies the contrast between Jane’s sincere sisterly affection and her refusal of the commitment he seeks."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "Truth-conditional avowal naturally captures the core force. The contextual work performed by the sisterly qualification—affirming affection while refusing marriage—does not require an additional core-force category.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 6. `bronte-jane-eyre-b94304d3eea5`

- **Exact match:** `I love you`
- **Pattern:** `en_i_love_you` (v0.1)
- **Source offsets:** 1006637–1006647
- **Relative position:** 0.966313
- **Chapter/section:** CHAPTER XXXVII
- **Supplied context:** 203 characters (29 before; 164 after)

#### Passage

> “Which are none, sir, to me. I love you better now, when I can really
> be useful to you, than I did in your state of proud independence, when
> you disdained every part but that of the giver and protector.”

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-1260\annotations\bronte-jane-eyre-b94304d3eea5\attempt-002`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** Jane directly avows that her love for Rochester is now stronger, explicitly comparing her present emotional state with her earlier love. The measured explanation of why she loves him better gives the utterance strong propositional force and no substantial reflexive or exclamatory force. In context it also weakly enacts continued relational devotion and willingness to care for him, but it does not independently formulate a clear promise or obligation.
- **Ontology fit:** natural — T/P/E represents the core force well: T captures the explicit, reflective avowal, while a low P score captures its contextual enactment of renewed devotion. No important core-force feature remains outside the ontology.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "bronte-jane-eyre-b94304d3eea5",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "Jane directly avows that her love for Rochester is now stronger, explicitly comparing her present emotional state with her earlier love. The measured explanation of why she loves him better gives the utterance strong propositional force and no substantial reflexive or exclamatory force. In context it also weakly enacts continued relational devotion and willingness to care for him, but it does not independently formulate a clear promise or obligation.",
    "ambiguity": "The utterance's reaffirmation of devotion during their reunion gives some support to P, although its grammatical and pragmatic centre remains an avowal of feeling rather than an explicit undertaking."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Jane speaks the utterance directly to Rochester in represented dialogue; the novel's quotation marks frame direct speech rather than a later quotation or report."
  },
  "contextual_interpretation": "Jane answers Rochester's apparent concern about his diminished condition by saying that his losses are no defects to her and that she loves him more now that she can be useful to him. The comparison rejects a merely dependency-based or status-based objection and presents her present love as sincere, reflective, and compatible with a more reciprocal caregiving relationship. In the wider Chapter XXXVII reunion, the statement also reassures Rochester of her freely renewed attachment, but its core force is chiefly an avowal rather than a promise or spontaneous outburst.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“I love you better now ... than I did in your state of proud independence”",
      "supports": "The explicit present-tense declaration and comparison with an earlier state strongly support truth-conditional avowal.",
      "confidence": 0.99
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "“when I can really be useful to you”",
      "supports": "Jane gives a reflective reason tied to caregiving, supporting a considered avowal and weak relational-undertaking force rather than an unmediated exclamation.",
      "confidence": 0.96
    },
    {
      "evidence_id": "local-3",
      "source": "local_text",
      "quotation_or_description": "“Which are none, sir, to me.”",
      "supports": "The preceding reply rejects the relevance of Rochester's perceived defects and frames the love declaration as deliberate reassurance and acceptance.",
      "confidence": 0.93
    },
    {
      "evidence_id": "metadata-1",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XXXVII, at relative position 0.966313 of Charlotte Brontë's Jane Eyre.",
      "supports": "The supplied location places the utterance near the novel's conclusion and identifies it with the late reunion context.",
      "confidence": 0.99
    },
    {
      "evidence_id": "background-1",
      "source": "background_knowledge",
      "quotation_or_description": "In Chapter XXXVII, Jane has returned to the injured and dependent Rochester and freely renews their relationship; their marriage follows.",
      "supports": "The wider narrative supports reading the utterance as a sincere reaffirmation with some relational commitment, while the sentence itself remains principally an avowal of love.",
      "confidence": 0.96
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.96,
    "contribution": "Knowledge of Jane's return to the injured Rochester, their renewed attachment, and subsequent marriage clarifies the reassurance and limited undertaking force of the declaration."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T/P/E represents the core force well: T captures the explicit, reflective avowal, while a low P score captures its contextual enactment of renewed devotion. No important core-force feature remains outside the ontology.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>
