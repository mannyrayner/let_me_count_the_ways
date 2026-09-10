# Single-text pipeline report: Pan

## Run summary

- **Run ID:** `runeberg-hamsun-pan`
- **Work:** *Pan* by Knut Hamsun
- **Source:** `runeberg-hamsun-pan`
- **Annotation:** v0.3.1 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 4
- **Valid occurrences:** 4
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.166260

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `hamsun-pan-0e1877bfee4c`

- **Exact match:** `Jeg / elsker dig`
- **Pattern:** `no_jeg_elsker_deg_dig_dere` (v0.6)
- **Source offsets:** 48341–48355
- **Relative position:** 0.279542
- **Chapter/section:** Unavailable
- **Supplied context:** 133 characters (115 before; 4 after)

#### Passage

> Det var ikke noget, svarte hun. Det lydde så underlig at
> Gud vilde lønne mig for det. Du sier slikt noget som .... Jeg
> elsker dig så!

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\runeberg-hamsun-pan\annotations\hamsun-pan-0e1877bfee4c\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** “Jeg elsker dig så!” (“I love you so!”) directly avows an intense loving state. The ellipsis, intensifier, and exclamation mark indicate emotional delivery but do not independently establish expressive/reflexive force. Nothing in the supplied passage makes the words a commitment or relational undertaking.
- **Ontology fit:** natural — T naturally captures the core avowal. Its emotional intensity can be recorded contextually without assigning independent E force, and no residual aspect requires O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "hamsun-pan-0e1877bfee4c",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.88,
    "analysis": "“Jeg elsker dig så!” (“I love you so!”) directly avows an intense loving state. The ellipsis, intensifier, and exclamation mark indicate emotional delivery but do not independently establish expressive/reflexive force. Nothing in the supplied passage makes the words a commitment or relational undertaking.",
    "ambiguity": "The narrow excerpt does not explicitly identify the speaker of the final sentence, but this does not materially affect its dominant truth-conditional force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A character directly addresses another with “Jeg elsker dig så!” within the represented dialogue."
  },
  "contextual_interpretation": "The declaration follows a response to the interlocutor’s remark about God rewarding the speaker and appears to answer perceived emotional strangeness with a strong avowal of love. Its abrupt transition, ellipsis, “så,” and exclamation mark convey intensity, but the available text gives no positive evidence that uttering the words is itself a reflex-like affective discharge rather than an impassioned assertion.",
  "evidence": [
    {
      "evidence_id": "ev1",
      "source": "local_text",
      "quotation_or_description": "“Jeg elsker dig så!”",
      "supports": "The first-person present-tense declaration explicitly presents the speaker’s love for the addressee as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev2",
      "source": "local_text",
      "quotation_or_description": "“Du sier slikt noget som .... Jeg elsker dig så!”",
      "supports": "The preceding direct address and continuation into the declaration support classification as a direct interpersonal utterance; the ellipsis marks an emotional transition but does not by itself establish E.",
      "confidence": 0.9
    },
    {
      "evidence_id": "ev3",
      "source": "local_text",
      "quotation_or_description": "The declaration contains the intensifier “så” and ends with an exclamation mark.",
      "supports": "These features support emotionally emphatic delivery while remaining compatible with a purely truth-conditional avowal.",
      "confidence": 0.96
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
    "diagnosis": "T naturally captures the core avowal. Its emotional intensity can be recorded contextually without assigning independent E force, and no residual aspect requires O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 2. `hamsun-pan-b4dcc2848eb5`

- **Exact match:** `jeg elsker dig`
- **Pattern:** `no_jeg_elsker_deg_dig_dere` (v0.6)
- **Source offsets:** 113162–113176
- **Relative position:** 0.654384
- **Chapter/section:** Unavailable
- **Supplied context:** 232 characters (124 before; 94 after)

#### Passage

> Du gode, gode sjæl! utbryter jeg og trykker hende hæftig ind
> til mig. Jeg er sikker på at jeg forgår av kjærlighet til dig,
> jeg elsker dig mere og mere, tilslut blir du med mig når jeg
> reiser. Du skal bare se. Kunde du følge med mig

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\runeberg-hamsun-pan\annotations\hamsun-pan-b4dcc2848eb5\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The direct statement “jeg elsker dig mere og mere” primarily avows an increasingly intense state of love, giving it strong truth-conditional force. The projected journey together does not make the core love utterance an undertaking. Although the speech is introduced as an exclamation and accompanied by an intense embrace, those delivery features do not independently establish expressive/reflexive force beyond an impassioned avowal.
- **Ontology fit:** natural — T/P/E adequately represents the core force as a passionate truth-conditional avowal. Its intensity and courtship setting are contextual features rather than missing dimensions of core force.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "hamsun-pan-b4dcc2848eb5",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.92,
    "analysis": "The direct statement “jeg elsker dig mere og mere” primarily avows an increasingly intense state of love, giving it strong truth-conditional force. The projected journey together does not make the core love utterance an undertaking. Although the speech is introduced as an exclamation and accompanied by an intense embrace, those delivery features do not independently establish expressive/reflexive force beyond an impassioned avowal.",
    "ambiguity": "The verb “utbryter” (“exclaim/burst out”) creates slight pressure toward E, but the passage does not show the love words themselves being produced involuntarily or reflexively rather than as an intense assertion."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "The first-person narrator directly tells the woman that he loves her more and more within an ongoing spoken address."
  },
  "contextual_interpretation": "The avowal is emotionally intense: the speaker calls her a good soul, presses her tightly to himself, and claims he is perishing from love. He then confidently imagines or insists that she will accompany him when he leaves. This supports passionate courtship and a proposed shared future, but the core clause remains an assertion of growing love rather than a commitment or reflex-like discharge.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“jeg elsker dig mere og mere” (“I love you more and more”)",
      "supports": "The grammatical declaration explicitly presents the speaker’s loving state, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“Jeg er sikker på at jeg forgår av kjærlighet til dig” (“I am sure that I am perishing from love for you”)",
      "supports": "The adjacent self-description reinforces the interpretation of the core utterance as an avowal of an intense emotional state.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“utbryter jeg og trykker hende hæftig ind til mig” (“I exclaim and press her forcefully to me”)",
      "supports": "This establishes emphatic, affect-laden delivery but does not by itself show an independently reflexive or discharge-like function for the love words.",
      "confidence": 0.91
    },
    {
      "evidence_id": "e4",
      "source": "local_text",
      "quotation_or_description": "“tilslut blir du med mig når jeg reiser. Du skal bare se.” (“in the end you will come with me when I leave. You will see.”)",
      "supports": "The speaker projects a shared future, but the wording predicts or insists on the addressee’s action rather than undertaking a commitment through the core love utterance.",
      "confidence": 0.9
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
    "diagnosis": "T/P/E adequately represents the core force as a passionate truth-conditional avowal. Its intensity and courtship setting are contextual features rather than missing dimensions of core force.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 3. `hamsun-pan-4dbcad04ce15`

- **Exact match:** `jeg elsker dig`
- **Pattern:** `no_jeg_elsker_deg_dig_dere` (v0.6)
- **Source offsets:** 128907–128921
- **Relative position:** 0.745433
- **Chapter/section:** Unavailable
- **Supplied context:** 21 characters (6 before; 1 after)

#### Passage

> Fordi jeg elsker dig.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\runeberg-hamsun-pan\annotations\hamsun-pan-4dbcad04ce15\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The clause “Fordi jeg elsker dig” (“Because I love you”) presents the speaker’s love as a true emotional state and as the reason for something established outside the extract. Nothing in the supplied fragment independently indicates a relational undertaking or an expressive/reflex-like discharge.
- **Ontology fit:** natural — T naturally captures the core explanatory avowal. The fragment supplies no independent pressure for P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "hamsun-pan-4dbcad04ce15",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.78,
    "analysis": "The clause “Fordi jeg elsker dig” (“Because I love you”) presents the speaker’s love as a true emotional state and as the reason for something established outside the extract. Nothing in the supplied fragment independently indicates a relational undertaking or an expressive/reflex-like discharge.",
    "ambiguity": "The very short context omits the preceding question or claim and any speech attribution, so the precise interaction and speaker are uncertain; this does not materially weaken the dominant truth-conditional reading."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly formulated first-person love avowal presented as the causal answer or explanation “Because I love you”; the truncated extract provides no explicit speech attribution."
  },
  "contextual_interpretation": "The initial “Fordi” (“Because”) makes the avowal explanatory: the speaker invokes love as a reason for an action, attitude, or answer found beyond the supplied context. This framing supports assertion of an emotional state but does not itself create a promise or commitment. There is no positive evidence of reflexive blurting or expressive discharge.",
  "evidence": [
    {
      "evidence_id": "ev-local-1",
      "source": "local_text",
      "quotation_or_description": "“Fordi jeg elsker dig.” (“Because I love you.”)",
      "supports": "The first-person present-tense love predicate directly presents a loving emotional state, strongly supporting T.",
      "confidence": 0.98
    },
    {
      "evidence_id": "ev-local-2",
      "source": "local_text",
      "quotation_or_description": "The sentence begins with the causal conjunction “Fordi” (“Because”).",
      "supports": "The love avowal functions as an explanation or reason; no commitment language or evidence of expressive/reflexive production appears in the fragment.",
      "confidence": 0.92
    },
    {
      "evidence_id": "ev-metadata-1",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as Norwegian text from Knut Hamsun’s Pan, at relative position approximately 0.745 in the supplied source.",
      "supports": "Establishes the work, language, and textual location, but does not resolve the omitted conversational setting.",
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
    "diagnosis": "T naturally captures the core explanatory avowal. The fragment supplies no independent pressure for P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "Classification is intentionally limited to the 21-character supplied context; speaker identity and the antecedent of “Because” are unavailable."
}
```

</details>

### 4. `hamsun-pan-700d90715f3a`

- **Exact match:** `jeg elsker dig`
- **Pattern:** `no_jeg_elsker_deg_dig_dere` (v0.6)
- **Source offsets:** 132047–132061
- **Relative position:** 0.763591
- **Chapter/section:** Unavailable
- **Supplied context:** 151 characters (82 before; 55 after)

#### Passage

> Jeg elsker tre ting, sier jeg så. Jeg elsker en kjærlighetsdrøm
> jeg hadde engang. jeg elsker dig og jeg elsker denne plet jord.
> Og hvad elsker du mest?

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\runeberg-hamsun-pan\annotations\hamsun-pan-700d90715f3a\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** “Jeg elsker dig” directly avows the speaker’s love for the addressee. Its placement in a deliberate enumeration of three loved things strongly supports truth-conditional presentation. Nothing in the supplied passage independently indicates a relational undertaking or an affect-driven reflexive discharge.
- **Ontology fit:** natural — T naturally captures the core utterance as an avowal of love. The supplied context creates no significant residual pressure for P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "hamsun-pan-700d90715f3a",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "“Jeg elsker dig” directly avows the speaker’s love for the addressee. Its placement in a deliberate enumeration of three loved things strongly supports truth-conditional presentation. Nothing in the supplied passage independently indicates a relational undertaking or an affect-driven reflexive discharge.",
    "ambiguity": "The wider scene could qualify the declaration’s sincerity or interpersonal purpose, but that would not materially change its dominant truth-conditional force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly represented spoken declaration by the first-person narrator within dialogue, introduced by “sier jeg så” (“I then say”)."
  },
  "contextual_interpretation": "The speaker presents love for the addressee as one item in a composed list alongside a remembered love-dream and a particular patch of earth, then asks what the addressee loves most. This reflective, comparative framing makes the utterance an avowal rather than a spontaneous expressive discharge; it also supplies no explicit commitment or undertaking.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“jeg elsker dig” (“I love you”).",
      "supports": "The declarative wording directly presents the speaker’s loving state as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“Jeg elsker tre ting, sier jeg så. Jeg elsker en kjærlighetsdrøm jeg hadde engang. jeg elsker dig og jeg elsker denne plet jord.”",
      "supports": "The utterance belongs to a structured enumeration of three objects of love, supporting deliberate avowal and providing no positive evidence for expressive/reflexive force.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“Og hvad elsker du mest?” (“And what do you love most?”).",
      "supports": "The follow-up question frames the exchange as reflective comparison of what each person loves, not as an undertaking or reflex-like outburst.",
      "confidence": 0.94
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
    "diagnosis": "T naturally captures the core utterance as an avowal of love. The supplied context creates no significant residual pressure for P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>
