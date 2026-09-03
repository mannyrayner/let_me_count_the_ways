# Single-text pipeline report: Jane Eyre

## Run summary

- **Run ID:** `gutenberg-1260`
- **Work:** *Jane Eyre* by Charlotte Brontë
- **Source:** `gutenberg-1260`
- **Annotation:** v0.3.1 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 6
- **Valid occurrences:** 6
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.217240

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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-1260\annotations\bronte-jane-eyre-d0cd60fde247\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** Jane directly avows that she loves Rochester, using the avowal concessively to distinguish sincere love from flattering or idealising him. “Most dearly” strengthens the degree of the presented emotional state but supplies no independent evidence of an undertaking or reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the core avowal. Its argumentative use, intensity, and relational implications are adequately represented as context and do not require P, E, or O.

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
    "confidence": 0.97,
    "analysis": "Jane directly avows that she loves Rochester, using the avowal concessively to distinguish sincere love from flattering or idealising him. “Most dearly” strengthens the degree of the presented emotional state but supplies no independent evidence of an undertaking or reflex-like expressive discharge.",
    "ambiguity": null
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Jane directly addresses Mr. Rochester and says that she loves him most dearly."
  },
  "contextual_interpretation": "The love avowal supports Jane’s insistence on honesty and equality: she can love Rochester deeply while refusing to flatter him or accept his attempt to dress her in an alien, ornamental identity. Its placement after “though” makes it a sincere concession within an argument, not a new promise. The intensification “most dearly” and “far too dearly” indicates emotional strength but does not make the utterance independently expressive/reflexive.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“though I love you most dearly”",
      "supports": "The first-person present-tense clause explicitly presents Jane’s loving emotional state as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“far too dearly to flatter you. Don’t flatter me.”",
      "supports": "Jane invokes the depth of her love as a reason for candour and mutual non-flattery; this confirms an avowal serving an argument rather than a commitment-making act or reflexive discharge.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“I don’t call you handsome, sir, though I love you most dearly”",
      "supports": "The concessive syntax contrasts honest judgment with love, reinforcing that the core utterance reports or avows affection rather than merely producing an emotional exclamation.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XXIV of Charlotte Brontë’s Jane Eyre.",
      "supports": "Identifies the source and location of the directly addressed utterance without adding claims beyond the supplied passage.",
      "confidence": 1.0
    }
  ],
  "background_knowledge": {
    "used": false,
    "familiarity": "none",
    "confidence": null,
    "contribution": null
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T naturally captures the core avowal. Its argumentative use, intensity, and relational implications are adequately represented as context and do not require P, E, or O.",
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-1260\annotations\bronte-jane-eyre-9267e616f948\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** Jane directly avows love as the reason she welcomes the prospect of living with Rochester. The utterance primarily presents her loving state as true. Its engaged, future-oriented setting gives it slight relational or commitment-invoking force, but the words themselves explain her happiness rather than undertake a distinct obligation. Her controlled insistence on speaking undisturbed provides no evidence that the words are a reflex-like expressive discharge.
- **Ontology fit:** natural — T/P/E adequately represents the core force: a strong avowal of an emotional state with, at most, weak commitment-invoking resonance from the engagement context. No important core function remains outside the ontology.

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
    "analysis": "Jane directly avows love as the reason she welcomes the prospect of living with Rochester. The utterance primarily presents her loving state as true. Its engaged, future-oriented setting gives it slight relational or commitment-invoking force, but the words themselves explain her happiness rather than undertake a distinct obligation. Her controlled insistence on speaking undisturbed provides no evidence that the words are a reflex-like expressive discharge.",
    "ambiguity": "A weak performative reading is possible because the avowal occurs within an anticipated marriage, but the core clause is principally explanatory and truth-conditional."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Jane addresses the words directly to Rochester during an extended account of her thoughts and hopes."
  },
  "contextual_interpretation": "Jane describes herself as happy and untroubled by the prospect of a new shared life, explicitly grounding that happiness in her love for Rochester. The surrounding reflection on Providence, his journey, their future, and her wedding dress situates the avowal within their engagement. Nevertheless, her request to be allowed to speak undisturbed and the explanatory construction “because I love you” make this a deliberate statement of feeling, not a reflexive outburst or a standalone promise.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I think it a glorious thing to have the hope of living with you, because I love you.”",
      "supports": "The causal construction explicitly presents Jane's love as an existing emotional state that explains her hope, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“No, sir, don’t caress me now—let me talk undisturbed.”",
      "supports": "Jane frames the avowal as part of sustained, deliberate speech rather than as an involuntary or reflex-like verbal discharge, supporting E=0.",
      "confidence": 0.95
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "Jane discusses “the life that lay before me—your life, sir” and later mentions her wedding dress.",
      "supports": "The anticipated marriage supplies limited support for relational or commitment-invoking force, while not making the core clause itself an explicit undertaking.",
      "confidence": 0.92
    },
    {
      "evidence_id": "e4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XXV of Charlotte Brontë's Jane Eyre.",
      "supports": "Identifies the textual location and confirms that the supplied passage belongs to the novel's pre-marital narrative context.",
      "confidence": 1.0
    }
  ],
  "background_knowledge": {
    "used": false,
    "familiarity": "none",
    "confidence": null,
    "contribution": null
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T/P/E adequately represents the core force: a strong avowal of an emotional state with, at most, weak commitment-invoking resonance from the engagement context. No important core function remains outside the ontology.",
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-1260\annotations\bronte-jane-eyre-14913cd0a6a4\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** Jane’s embedded “I love you” is presented as an avowal of her loving state and as the reason for her hope of living with Edward. It does not itself undertake a commitment, and its soft, solemn delivery supplies no independent evidence of expressive/reflexive discharge.
- **Ontology fit:** natural — T naturally captures the core avowal. The future-oriented relationship context can be recorded without construing the highlighted words as an undertaking, while neither E nor O is needed.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "bronte-jane-eyre-14913cd0a6a4",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.97,
    "analysis": "Jane’s embedded “I love you” is presented as an avowal of her loving state and as the reason for her hope of living with Edward. It does not itself undertake a commitment, and its soft, solemn delivery supplies no independent evidence of expressive/reflexive discharge.",
    "ambiguity": "The surrounding reference to living together gives the statement relational significance, but it does not make the highlighted causal avowal itself a commitment."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "quoted_or_revoiced",
    "description": "Rochester quotes or closely revoices an earlier direct utterance by Jane, explicitly describing himself as having heard her say it."
  },
  "contextual_interpretation": "Rochester treats Jane’s prior words as a clear and consequential confession, recalls them with pleasure, and presses her to repeat the avowal. His insistence heightens the interpersonal stakes, but Jane’s quoted core utterance remains principally truth-conditional rather than performative or reflex-like.",
  "evidence": [
    {
      "evidence_id": "ev1",
      "source": "local_text",
      "quotation_or_description": "“because I love you”",
      "supports": "The causal clause presents Jane’s love as an emotional state that explains her hope of living with Edward, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev2",
      "source": "local_text",
      "quotation_or_description": "“I think it is a glorious thing to have the hope of living with you, Edward, because I love you.”",
      "supports": "The full sentence frames the love declaration as an avowed reason for anticipated happiness, not as an explicit undertaking or promise.",
      "confidence": 0.96
    },
    {
      "evidence_id": "ev3",
      "source": "local_text",
      "quotation_or_description": "“Those words did not die inarticulate on your lips. I heard them clear and soft: a thought too solemn perhaps, but sweet as music”",
      "supports": "This establishes an earlier spoken event now being quoted and characterizes its deliberate, intelligible delivery; softness and solemnity alone do not support E.",
      "confidence": 0.98
    },
    {
      "evidence_id": "ev4",
      "source": "local_text",
      "quotation_or_description": "“Do you love me, Jane?—repeat it.”",
      "supports": "Rochester interprets the earlier utterance as an answerable avowal and requests its repetition, reinforcing the truth-conditional reading.",
      "confidence": 0.97
    },
    {
      "evidence_id": "ev5",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as appearing in Chapter XXV of Charlotte Brontë’s Jane Eyre.",
      "supports": "Confirms the bibliographic identity and location of the quoted occurrence without adding substantive force beyond the local text.",
      "confidence": 0.99
    }
  ],
  "background_knowledge": {
    "used": false,
    "familiarity": "none",
    "confidence": null,
    "contribution": null
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T naturally captures the core avowal. The future-oriented relationship context can be recorded without construing the highlighted words as an undertaking, while neither E nor O is needed.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-1260\annotations\bronte-jane-eyre-f221719b1af4\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The narrator verbalises the man's look as saying “I love you.” Its core force is a strong avowal or presentation of his loving state. It does not undertake a relationship; the continuation instead explains why he remains silent and will not offer his heart. His visible emotion supports the avowal's intensity but does not make the words an expressive/reflex-like discharge.
- **Ontology fit:** natural — T naturally captures the unspoken avowal, while P and E are unnecessary. The nonverbal and narrator-mediated form is adequately recorded by utterance status and context, not by O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "bronte-jane-eyre-f221719b1af4",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.97,
    "analysis": "The narrator verbalises the man's look as saying “I love you.” Its core force is a strong avowal or presentation of his loving state. It does not undertake a relationship; the continuation instead explains why he remains silent and will not offer his heart. His visible emotion supports the avowal's intensity but does not make the words an expressive/reflex-like discharge.",
    "ambiguity": "The words are a narrator-supplied interpretation of nonverbal behaviour rather than an actually spoken sentence, but this affects utterance status rather than the T/P/E classification."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "nonverbal_verbalised",
    "description": "The narrator renders the man's sad, resolute look as an unspoken first-person declaration: he “seemed to say” it even though he did not say it with his lips."
  },
  "contextual_interpretation": "The passage presents affection that is visible despite attempted restraint: his trembling hand and burning eye disclose what he keeps verbally unexpressed. The imagined continuation distinguishes love from commitment. He believes the woman would accept him, but regards his heart as already consecrated elsewhere, so the declaration reports suppressed love while withholding any relational offer.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“He seemed to say, with his sad and resolute look, if he did not say it with his lips, ‘I love you’”",
      "supports": "Establishes that the declaration is a narrator-verbalised interpretation of nonverbal conduct and presents a loving state as true.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“his hand would tremble and his eye burn” when she addressed and smiled at him",
      "supports": "Supports the interpretation that his concealed affection is emotionally intense, without independently establishing expressive/reflexive force.",
      "confidence": 0.96
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“It is not despair of success that keeps me dumb. If I offered my heart, I believe you would accept it. But that heart is already laid on a sacred altar”",
      "supports": "Shows that an offer or relational undertaking is explicitly counterfactual and withheld, supporting P=0 despite the avowed love.",
      "confidence": 0.98
    }
  ],
  "background_knowledge": {
    "used": false,
    "familiarity": "none",
    "confidence": null,
    "contribution": null
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T naturally captures the unspoken avowal, while P and E are unnecessary. The nonverbal and narrator-mediated form is adequately recorded by utterance status and context, not by O.",
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-1260\annotations\bronte-jane-eyre-b57472f62694\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** Jane directly avows that she loves her addressee in a specifically sisterly sense. The phrase presents an emotional and relational attitude as true, while its careful qualification and argumentative placement provide no independent evidence of an undertaking or reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the core avowal. The surrounding dispute concerns obligations and marriage, but the qualified love utterance itself neither performs such an undertaking nor functions as an affect-driven verbal discharge. No residual core force requires O.

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
    "confidence": 0.98,
    "analysis": "Jane directly avows that she loves her addressee in a specifically sisterly sense. The phrase presents an emotional and relational attitude as true, while its careful qualification and argumentative placement provide no independent evidence of an undertaking or reflex-like expressive discharge.",
    "ambiguity": "The love is explicitly familial rather than romantic; this affects its object-level meaning but not its predominantly truth-conditional force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Jane speaks the utterance directly to St John Rivers within dialogue, qualifying her love for him as that of a sister."
  },
  "contextual_interpretation": "The avowal occurs in Jane's reasoned refusal to accept that she is obliged to go to India. She cites admiration, confidence, and sisterly love to explain how much she might have ventured with St John, while sharply limiting the kind of love she professes. In the wider episode, this qualification distinguishes familial affection from the marital love and commitment implicated by St John's proposal; it therefore supports T strongly without converting the utterance into a commitment-performing P event.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I admire, confide in, and, as a sister, I love you”",
      "supports": "The coordinated mental and emotional predicates, especially the explicit sisterly qualification, present Jane's love as an avowed state and strongly support T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“There is no dishonour, no breach of promise, no desertion in the case. I am not under the slightest obligation to go to India”",
      "supports": "Jane explicitly denies obligation and breach of promise, weighing against interpreting the core love utterance as undertaking or renewing a commitment.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "The utterance appears in a syntactically controlled explanation: “With you I would have ventured much, because…”",
      "supports": "Its deliberative, explanatory role supports an avowal rather than an expressive or reflex-like discharge.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XXXV of Charlotte Brontë's Jane Eyre.",
      "supports": "Identifies the episode and licenses alignment with the supplied work context.",
      "confidence": 1.0
    },
    {
      "evidence_id": "e5",
      "source": "background_knowledge",
      "quotation_or_description": "In Chapter XXXV, St John Rivers pressures Jane to accompany him to India as his wife, while Jane distinguishes sisterly affection from the love required for marriage.",
      "supports": "Clarifies why “as a sister” limits the avowal and why it should not be read as accepting St John's proposed marital undertaking.",
      "confidence": 0.96
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.96,
    "contribution": "It identifies the addressee as St John Rivers and situates the statement within Jane's resistance to his proposed loveless missionary marriage, clarifying the force of the sisterly qualification."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T naturally captures the core avowal. The surrounding dispute concerns obligations and marriage, but the qualified love utterance itself neither performs such an undertaking nor functions as an affect-driven verbal discharge. No residual core force requires O.",
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-1260\annotations\bronte-jane-eyre-b94304d3eea5\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** Jane directly avows that her love for Rochester is now greater than it was during his former independence. The comparative construction explicitly presents her loving emotional state as true, making T dominant. In the reunion context, the avowal also offers limited relational reassurance, but it does not itself clearly promise care or undertake an obligation, so P receives only weak support. Nothing indicates that the words are a reflex-like expressive discharge rather than a deliberate avowal.
- **Ontology fit:** natural — T naturally captures the utterance's central force as a comparative avowal of love; a small P score captures its secondary relational reassurance. Delivery and syntax supply no independent E force, and no important aspect of the core utterance falls outside T/P/E.

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
    "confidence": 0.94,
    "analysis": "Jane directly avows that her love for Rochester is now greater than it was during his former independence. The comparative construction explicitly presents her loving emotional state as true, making T dominant. In the reunion context, the avowal also offers limited relational reassurance, but it does not itself clearly promise care or undertake an obligation, so P receives only weak support. Nothing indicates that the words are a reflex-like expressive discharge rather than a deliberate avowal.",
    "ambiguity": "The surrounding emphasis on Jane's ability to be useful to Rochester gives the utterance some commitment-like pragmatic force, but that force may belong chiefly to the context rather than to the core love statement."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Jane speaks the love avowal directly to Rochester within narrated dialogue."
  },
  "contextual_interpretation": "Jane contrasts Rochester's former position as a proud, independent giver and protector with his present dependence, insisting that his losses do not diminish her attachment. Her declaration both reports intensified love and reassures him that being able to help him is compatible with—and deepens—her freely chosen relationship to him. The wording is reflective and reason-giving rather than reflexive or uncontrolled.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I love you better now ... than I did in your state of proud independence”",
      "supports": "The explicit present-versus-past comparison strongly supports a truth-conditional avowal of an intensified loving state.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“when I can really be useful to you”",
      "supports": "Jane links her love to her present capacity to assist the addressee, supplying weak commitment-like reassurance but no explicit undertaking.",
      "confidence": 0.92
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "The utterance explains and compares Jane's feelings in a syntactically developed sentence.",
      "supports": "Its reflective, reasoned form provides no positive evidence that producing the words is an expressive or reflex-like discharge.",
      "confidence": 0.94
    },
    {
      "evidence_id": "e4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XXXVII, near the end of Charlotte Brontë's Jane Eyre.",
      "supports": "The location identifies the utterance as part of the novel's late reunion sequence.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e5",
      "source": "background_knowledge",
      "quotation_or_description": "In Chapter XXXVII, Jane has returned to Rochester after his disabling injuries and addresses his concern that his diminished independence makes him less fit for her.",
      "supports": "The wider scene clarifies that the avowal reassures Rochester while asserting Jane's freely maintained and intensified love.",
      "confidence": 0.96
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.96,
    "contribution": "Used to identify Jane as speaker, Rochester as addressee, and the late reunion after Rochester's disabling injuries, which explains the contrast between his former independence and Jane's present usefulness."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T naturally captures the utterance's central force as a comparative avowal of love; a small P score captures its secondary relational reassurance. Delivery and syntax supply no independent E force, and no important aspect of the core utterance falls outside T/P/E.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>
