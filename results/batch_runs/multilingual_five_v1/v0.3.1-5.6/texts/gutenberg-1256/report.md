# Single-text pipeline report: Cyrano de Bergerac

## Run summary

- **Run ID:** `gutenberg-1256`
- **Work:** *Cyrano de Bergerac* by Edmond Rostand
- **Source:** `gutenberg-1256`
- **Annotation:** v0.3.1 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 14
- **Valid occurrences:** 14
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.579588

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `rostand-cyrano-de-bergerac-89c2617e9b1b`

- **Exact match:** `Je vous aime`
- **Pattern:** `fr_je_vous_aime` (v0.4)
- **Source offsets:** 66674–66686
- **Relative position:** 0.275049
- **Chapter/section:** Unavailable
- **Supplied context:** 87 characters (70 before; 5 after)

#### Passage

> CYRANO (écrivant, à part,--on l'entend murmurer de temps en temps):
>   Je vous aime. . .

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\gutenberg-1256\annotations\rostand-cyrano-de-bergerac-89c2617e9b1b\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** Cyrano's written and murmured “Je vous aime” is principally an avowal presenting his love as true. Its placement in a love letter gives it communicative and courtship significance, but the words themselves do not clearly undertake a commitment or obligation. Writing privately and murmuring intermittently do not establish reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the declaration's central avowal force. Its written, private, and romantically mediated circumstances can be represented contextually without adding P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "rostand-cyrano-de-bergerac-89c2617e9b1b",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.94,
    "analysis": "Cyrano's written and murmured “Je vous aime” is principally an avowal presenting his love as true. Its placement in a love letter gives it communicative and courtship significance, but the words themselves do not clearly undertake a commitment or obligation. Writing privately and murmuring intermittently do not establish reflex-like expressive discharge.",
    "ambiguity": "The event combines writing with audible murmuring, but this affects utterance status more than core force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "written",
    "description": "Cyrano is composing the declaration in writing while also murmuring it aloud from time to time; the written declaration is the primary event."
  },
  "contextual_interpretation": "Cyrano is privately composing a declaration of love associated with Roxane. His aside and murmured delivery expose to the audience a sincere feeling that he has difficulty communicating openly. The romantic purpose of the letter supplies courtship context, but “Je vous aime” remains chiefly an avowal rather than an explicit relational undertaking or reflexive outburst.",
  "evidence": [
    {
      "evidence_id": "ev-local-1",
      "source": "local_text",
      "quotation_or_description": "“CYRANO (écrivant, à part,--on l'entend murmurer de temps en temps): Je vous aime. . .”",
      "supports": "The stage direction identifies the declaration as being written and intermittently murmured; the wording directly avows love, supporting high T and written status without positive evidence of reflex-like E.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev-meta-1",
      "source": "supplied_metadata",
      "quotation_or_description": "The supplied metadata identifies the passage as French text from Edmond Rostand's Cyrano de Bergerac.",
      "supports": "Establishes the work and linguistic context used to interpret “Je vous aime” as the formal/polite equivalent of “I love you.”",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev-bg-1",
      "source": "background_knowledge",
      "quotation_or_description": "In the wider play, Cyrano loves Roxane and composes declarations that articulate feelings he struggles to express directly under his own name.",
      "supports": "Supports reading this line as a sincere avowal embedded in concealed or difficult courtship rather than as practice, meaningless recitation, or another O-type use.",
      "confidence": 0.94
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.94,
    "contribution": "Identified Roxane as the object of Cyrano's love and situated the writing within his broader pattern of indirectly expressing sincere feelings."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T naturally captures the declaration's central avowal force. Its written, private, and romantically mediated circumstances can be represented contextually without adding P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 2. `rostand-cyrano-de-bergerac-fcb8f2f7f81a`

- **Exact match:** `je vous aime`
- **Pattern:** `fr_je_vous_aime` (v0.4)
- **Source offsets:** 77920–77932
- **Relative position:** 0.321442
- **Chapter/section:** Unavailable
- **Supplied context:** 342 characters (15 before; 315 after)

#### Passage

> ROXANE:
>   Oh ! je vous aime bien. Il faut que je m'en aille.
>   (Elle remet vivement son masque, une dentelle sur son front, et,
>   distraitement):
>   Mais vous ne m'avez pas raconté la bataille
>   De cette nuit. Vraiment ce dut être inouï !. . .
>   --Dites-lui qu'il m'écrive.
>   (Elle lui envoie un petit baiser de la main):
>   Oh ! je vous aime !

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\gutenberg-1256\annotations\rostand-cyrano-de-bergerac-fcb8f2f7f81a\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** Roxane directly presents her affection for Cyrano as true. The idiom “je vous aime bien” is most naturally an avowal of fondness rather than a relational undertaking. Neither the initial “Oh !” nor the affectionate staging independently shows that the words function as a reflex-like emotional discharge.
- **Ontology fit:** natural — T naturally captures the utterance as an avowal of affection. The surrounding emotional warmth and dramatic irony require contextual explanation but introduce no core force beyond T/P/E.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "rostand-cyrano-de-bergerac-fcb8f2f7f81a",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.95,
    "analysis": "Roxane directly presents her affection for Cyrano as true. The idiom “je vous aime bien” is most naturally an avowal of fondness rather than a relational undertaking. Neither the initial “Oh !” nor the affectionate staging independently shows that the words function as a reflex-like emotional discharge.",
    "ambiguity": "French “aimer bien” can range from liking to warm affection and is weaker than an unqualified romantic declaration; this affects the kind or degree of feeling avowed, not its predominantly truth-conditional force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "The classified event is Roxane’s directly spoken “Oh ! je vous aime bien” addressed to Cyrano, not the later repeated “Oh ! je vous aime !” in the supplied context."
  },
  "contextual_interpretation": "Roxane expresses warm affection toward Cyrano while preparing to leave and asking him to tell another man to write to her. In the wider dramatic situation, that other man is Christian, the object of her romantic love, so her words to Cyrano convey fondness and gratitude rather than a new romantic commitment. Her haste, “Oh !,” and affectionate gesture make the scene emotionally warm but do not establish independent expressive/reflexive force.",
  "evidence": [
    {
      "evidence_id": "ev-local-1",
      "source": "local_text",
      "quotation_or_description": "“ROXANE: Oh ! je vous aime bien. Il faut que je m'en aille.”",
      "supports": "The declarative construction explicitly avows Roxane’s affection, strongly supporting T; “bien” qualifies it as fondness or liking.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev-local-2",
      "source": "local_text",
      "quotation_or_description": "“Dites-lui qu'il m'écrive.”",
      "supports": "Roxane’s request concerning an absent male distinguishes her affection for Cyrano from the romantic attachment organizing the immediate conversation; it supplies no undertaking toward Cyrano.",
      "confidence": 0.94
    },
    {
      "evidence_id": "ev-local-3",
      "source": "local_text",
      "quotation_or_description": "The passage includes “Oh !,” hurried masking, and later a small kiss sent by hand.",
      "supports": "These details indicate warmth and animated delivery, but they do not independently establish reflex-like production of the matched words.",
      "confidence": 0.93
    },
    {
      "evidence_id": "ev-background-1",
      "source": "background_knowledge",
      "quotation_or_description": "In the play’s established plot, Roxane is romantically attracted to Christian and uses Cyrano as an intermediary, while Cyrano secretly loves her.",
      "supports": "This dramatic configuration supports reading “je vous aime bien” to Cyrano as sincere familial or friendly fondness rather than a romantic pledge.",
      "confidence": 0.96
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.96,
    "contribution": "The wider plot identifies Christian as the man from whom Roxane wants a letter and clarifies the contrast between her romantic love for Christian and her affectionate regard for Cyrano."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T naturally captures the utterance as an avowal of affection. The surrounding emotional warmth and dramatic irony require contextual explanation but introduce no core force beyond T/P/E.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The exact matched occurrence at source offsets 77920–77932 is the first phrase “je vous aime” within “je vous aime bien”; the later unqualified repetition is contextual evidence rather than the classified occurrence."
}
```

</details>

### 3. `rostand-cyrano-de-bergerac-4f3fb98d5ffc`

- **Exact match:** `je vous aime`
- **Pattern:** `fr_je_vous_aime` (v0.4)
- **Source offsets:** 78233–78245
- **Relative position:** 0.322733
- **Chapter/section:** Unavailable
- **Supplied context:** 342 characters (328 before; 2 after)

#### Passage

> ROXANE:
>   Oh ! je vous aime bien. Il faut que je m'en aille.
>   (Elle remet vivement son masque, une dentelle sur son front, et,
>   distraitement):
>   Mais vous ne m'avez pas raconté la bataille
>   De cette nuit. Vraiment ce dut être inouï !. . .
>   --Dites-lui qu'il m'écrive.
>   (Elle lui envoie un petit baiser de la main):
>   Oh ! je vous aime !

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\gutenberg-1256\annotations\rostand-cyrano-de-bergerac-4f3fb98d5ffc\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** Roxane directly avows affection for Cyrano. In this scene the phrase primarily presents her loving fondness as true; it does not itself undertake a commitment. The exclamation, repetition, departing gesture, and lively delivery make the avowal emphatic but do not independently establish reflex-like expressive force.
- **Ontology fit:** natural — T naturally captures the direct avowal of affection. The scene's effusiveness, gratitude, gesture, and distinction between friendly or familial and romantic love are contextual nuances rather than unrepresented core forces.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "rostand-cyrano-de-bergerac-4f3fb98d5ffc",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.9,
    "analysis": "Roxane directly avows affection for Cyrano. In this scene the phrase primarily presents her loving fondness as true; it does not itself undertake a commitment. The exclamation, repetition, departing gesture, and lively delivery make the avowal emphatic but do not independently establish reflex-like expressive force.",
    "ambiguity": "The principal ambiguity concerns the kind of love avowed—warm familial or friendly affection and gratitude rather than romantic love—not the utterance's predominantly truth-conditional force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Roxane directly says “Oh ! je vous aime !” to Cyrano during their conversation."
  },
  "contextual_interpretation": "Roxane is leaving after discussing another man and asking Cyrano to tell him to write to her. Her hand-kiss and repeated affectionate wording frame the line as an effusive expression of fondness and gratitude toward Cyrano, while the wider dramatic situation distinguishes that fondness from her romantic attachment to Christian. These relational circumstances qualify what kind of love she avows but do not alter the core T classification.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“Oh ! je vous aime !”",
      "supports": "The unhedged first-person present-tense statement directly presents Roxane's affection as true, strongly supporting T.",
      "confidence": 0.98
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "Roxane first says “je vous aime bien” and shortly afterward repeats “je vous aime” while sending a small kiss with her hand.",
      "supports": "The repetition and affectionate gesture support a warm, emphatic avowal, but do not by themselves establish independent E force or a relational undertaking.",
      "confidence": 0.94
    },
    {
      "evidence_id": "local-3",
      "source": "local_text",
      "quotation_or_description": "“Dites-lui qu'il m'écrive.”",
      "supports": "Her request that Cyrano tell another man to write contextualizes the addressed affection as distinct from her romantic interest in that absent man.",
      "confidence": 0.91
    },
    {
      "evidence_id": "background-1",
      "source": "background_knowledge",
      "quotation_or_description": "In the play's central love triangle, Roxane is romantically attracted to Christian and treats Cyrano as a trusted relative and confidant at this stage.",
      "supports": "Supports interpreting the line to Cyrano as affectionate gratitude or familial/friendly love rather than a romantic commitment.",
      "confidence": 0.9
    },
    {
      "evidence_id": "metadata-1",
      "source": "supplied_metadata",
      "quotation_or_description": "The supplied metadata identifies the work as Edmond Rostand's French play Cyrano de Bergerac.",
      "supports": "Establishes the dramatic source used to connect the local exchange with the wider character relationships.",
      "confidence": 0.99
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.9,
    "contribution": "The wider love triangle clarifies that Roxane's affection for Cyrano here is not equivalent to her romantic attachment to Christian."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T naturally captures the direct avowal of affection. The scene's effusiveness, gratitude, gesture, and distinction between friendly or familial and romantic love are contextual nuances rather than unrepresented core forces.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The semantic range of French “aimer” permits several kinds and degrees of affection; that lexical and relational nuance does not require O."
}
```

</details>

### 4. `rostand-cyrano-de-bergerac-9bde0e07d6fe`

- **Exact match:** `Je vous aime`
- **Pattern:** `fr_je_vous_aime` (v0.4)
- **Source offsets:** 117879–117891
- **Relative position:** 0.486283
- **Chapter/section:** Unavailable
- **Supplied context:** 74 characters (61 before; 1 after)

#### Passage

> CHRISTIAN (s'assied près d'elle, sur le banc. Un silence):
>   Je vous aime.

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\gutenberg-1256\annotations\rostand-cyrano-de-bergerac-9bde0e07d6fe\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** Christian directly avows to Roxane that he loves her. The line primarily presents his loving state as true. Although it occurs during courtship, neither the words nor the immediate staging independently enact a commitment or relational undertaking. The preceding silence and simple delivery provide no positive evidence that the words are a reflex-like expressive discharge.
- **Ontology fit:** natural — T/P/E/O represents the core utterance naturally as a strong truth-conditional avowal. The dramatic irony and Cyrano's role belong to contextual interpretation rather than revealing any missing dimension of core force.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "rostand-cyrano-de-bergerac-9bde0e07d6fe",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.94,
    "analysis": "Christian directly avows to Roxane that he loves her. The line primarily presents his loving state as true. Although it occurs during courtship, neither the words nor the immediate staging independently enact a commitment or relational undertaking. The preceding silence and simple delivery provide no positive evidence that the words are a reflex-like expressive discharge.",
    "ambiguity": "The declaration is part of a courtship encounter and therefore has relational consequences, but courtship context alone is insufficient to give it performative force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Christian speaks the line directly to Roxane during their face-to-face dramatic interaction."
  },
  "contextual_interpretation": "Christian's blunt declaration is a sincere-seeming but rhetorically inadequate avowal during his attempt to court Roxane in his own words. In the wider play, Roxane associates Christian with eloquence substantially supplied by Cyrano; that deception complicates her understanding of the speaker she loves but does not alter this line's core truth-conditional force. Its simplicity, following a silence, contrasts with the elaborate language Roxane expects.",
  "evidence": [
    {
      "evidence_id": "ev-local-1",
      "source": "local_text",
      "quotation_or_description": "“CHRISTIAN (s'assied près d'elle, sur le banc. Un silence): Je vous aime.”",
      "supports": "The explicit first-person declaration directly presents Christian's love for his addressee as true; the stage direction identifies a deliberate face-to-face utterance rather than a report or quotation.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev-metadata-1",
      "source": "supplied_metadata",
      "quotation_or_description": "The supplied metadata identifies the work as Edmond Rostand's French play Cyrano de Bergerac and locates the line near the middle of the text.",
      "supports": "Establishes the dramatic source and supports reading the speaker label and stage direction as an enacted direct utterance.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev-background-1",
      "source": "background_knowledge",
      "quotation_or_description": "In the surrounding episode, Christian attempts to speak to Roxane without relying on Cyrano's eloquence, while Roxane expects the verbal brilliance she attributes to Christian.",
      "supports": "Explains the line's conspicuous bluntness and the broader deception surrounding the courtship without converting the core avowal into O, P, or E.",
      "confidence": 0.9
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.9,
    "contribution": "Used knowledge of Christian, Roxane, and Cyrano's mediated courtship to interpret the declaration as a blunt personal avowal embedded in a larger deception about authorship and eloquence."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T/P/E/O represents the core utterance naturally as a strong truth-conditional avowal. The dramatic irony and Cyrano's role belong to contextual interpretation rather than revealing any missing dimension of core force.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 5. `rostand-cyrano-de-bergerac-bafeacc6bf4b`

- **Exact match:** `Je t'aime`
- **Pattern:** `fr_je_taime_apostrophe_spacing` (v0.4)
- **Source offsets:** 117962–117971
- **Relative position:** 0.486626
- **Chapter/section:** Unavailable
- **Supplied context:** 23 characters (13 before; 1 after)

#### Passage

> CHRISTIAN:
>   Je t'aime.

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\gutenberg-1256\annotations\rostand-cyrano-de-bergerac-bafeacc6bf4b\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** Christian's “Je t'aime” is principally a direct avowal that presents his love for Roxane as true. Its courtship function does not independently constitute a commitment or relational undertaking, and there is no positive evidence that the words emerge as a reflex-like expressive discharge rather than as a deliberately stated declaration.
- **Ontology fit:** natural — T naturally captures the core force. Christian's rhetorical limitations, courtship strategy, and Roxane's dissatisfaction are contextual features rather than evidence of P, E, or an unrepresented core category.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "rostand-cyrano-de-bergerac-bafeacc6bf4b",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.93,
    "analysis": "Christian's “Je t'aime” is principally a direct avowal that presents his love for Roxane as true. Its courtship function does not independently constitute a commitment or relational undertaking, and there is no positive evidence that the words emerge as a reflex-like expressive discharge rather than as a deliberately stated declaration.",
    "ambiguity": "The minimal extracted context does not show tone or immediate response. The wider scene gives the line a persuasive courtship purpose, but that purpose does not by itself establish performative force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Christian directly addresses the love declaration to Roxane within the dramatic action."
  },
  "contextual_interpretation": "In the wider scene, Christian attempts to woo Roxane without Cyrano's eloquence and falls back on the blunt, repeated formula “Je t'aime.” The declaration appears sincere but rhetorically inadequate for Roxane's expectations. Its strategic courtship setting and resulting conversational failure affect its reception, not its basic truth-conditional force.",
  "evidence": [
    {
      "evidence_id": "ev1-local-utterance",
      "source": "local_text",
      "quotation_or_description": "“CHRISTIAN: Je t'aime.”",
      "supports": "The explicit first-person declaration strongly supports truth-conditional avowal and identifies Christian as the direct speaker.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev2-metadata-work",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as dialogue from Edmond Rostand's French play Cyrano de Bergerac.",
      "supports": "The dramatic attribution supports treating the line as a character's direct spoken utterance rather than narration or reported speech.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev3-wider-scene",
      "source": "background_knowledge",
      "quotation_or_description": "In the surrounding courtship episode, Christian tries to speak to Roxane in his own words and relies on a bare declaration of love, which she finds insufficiently elaborated.",
      "supports": "This supports sincere avowal with a persuasive courtship purpose, while providing no independent evidence of commitment-making or reflex-like discharge.",
      "confidence": 0.9
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.9,
    "contribution": "Knowledge of Christian's unsuccessful attempt to woo Roxane without Cyrano's verbal artistry clarifies the declaration as blunt and rhetorically inadequate but still semantically ordinary and sincere."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T naturally captures the core force. Christian's rhetorical limitations, courtship strategy, and Roxane's dissatisfaction are contextual features rather than evidence of P, E, or an unrepresented core category.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 6. `rostand-cyrano-de-bergerac-54e96b0c7005`

- **Exact match:** `Je t'aime`
- **Pattern:** `fr_je_taime_apostrophe_spacing` (v0.4)
- **Source offsets:** 118079–118088
- **Relative position:** 0.487109
- **Chapter/section:** Unavailable
- **Supplied context:** 28 characters (13 before; 6 after)

#### Passage

> CHRISTIAN:
>   Je t'aime tant.

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\gutenberg-1256\annotations\rostand-cyrano-de-bergerac-54e96b0c7005\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** Christian's direct “Je t'aime tant” (“I love you so much”) primarily avows the strength of his loving feelings. Its use in courtship gives it slight relational or undertaking force, but it does not itself articulate a commitment. Neither the wording nor the scene supplies positive evidence that the words are a reflex-like expressive discharge.
- **Ontology fit:** natural — T/P/E adequately represents the core utterance as a strong avowal with minor courtship-related undertaking force and no independently evidenced expressive/reflexive function. The surrounding comic and dramatic irony requires contextual description but creates no residual ontology failure.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "rostand-cyrano-de-bergerac-54e96b0c7005",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.91,
    "analysis": "Christian's direct “Je t'aime tant” (“I love you so much”) primarily avows the strength of his loving feelings. Its use in courtship gives it slight relational or undertaking force, but it does not itself articulate a commitment. Neither the wording nor the scene supplies positive evidence that the words are a reflex-like expressive discharge.",
    "ambiguity": "The courtship setting gives weak support for P, but romantic address and intended emotional effect alone do not establish a substantial undertaking."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Christian directly addresses Roxane with the spoken declaration “Je t'aime tant.”"
  },
  "contextual_interpretation": "In the balcony courtship scene, Christian tries to speak to Roxane without Cyrano's eloquent prompting and falls back on a plain, repeated declaration of love. Roxane finds such formulaic language insufficiently developed. That dramatic inadequacy concerns Christian's eloquence, not the utterance's core semantic force: it remains chiefly a sincere-seeming avowal rather than an expressive reflex or explicit commitment.",
  "evidence": [
    {
      "evidence_id": "e1-local-wording",
      "source": "local_text",
      "quotation_or_description": "“CHRISTIAN: Je t'aime tant.”",
      "supports": "The first-person present-tense declaration, intensified by “tant,” strongly supports truth-conditional avowal of a loving state.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2-metadata-form",
      "source": "supplied_metadata",
      "quotation_or_description": "The supplied excerpt identifies the speaker as CHRISTIAN in Edmond Rostand's French play Cyrano de Bergerac.",
      "supports": "Supports treating this as a character's direct dramatic utterance rather than narration or reported speech.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e3-wider-scene",
      "source": "background_knowledge",
      "quotation_or_description": "In the balcony scene, Christian attempts to woo Roxane in his own words and repeatedly offers simple declarations of love, which she regards as insufficiently eloquent; Cyrano elsewhere supplies the elaborate language.",
      "supports": "Supports dominant T, weak courtship-related P, and E=0: the line is a deliberate but verbally limited avowal, not presented as an involuntary verbal discharge.",
      "confidence": 0.92
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.92,
    "contribution": "The wider balcony scene clarifies that Christian is deliberately attempting an unaided declaration during courtship and that the line's repetition reflects limited eloquence rather than reflex-like production."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T/P/E adequately represents the core utterance as a strong avowal with minor courtship-related undertaking force and no independently evidenced expressive/reflexive function. The surrounding comic and dramatic irony requires contextual description but creates no residual ontology failure.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 7. `rostand-cyrano-de-bergerac-9299dcd45fdf`

- **Exact match:** `Je t'aime`
- **Pattern:** `fr_je_taime_apostrophe_spacing` (v0.4)
- **Source offsets:** 118591–118600
- **Relative position:** 0.489221
- **Chapter/section:** Unavailable
- **Supplied context:** 24 characters (13 before; 2 after)

#### Passage

> CHRISTIAN:
>   Je t'aime !

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\gutenberg-1256\annotations\rostand-cyrano-de-bergerac-9299dcd45fdf\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** Christian's direct “Je t'aime !” primarily avows as true his loving feeling toward Roxane. Although uttered in a courtship scene, it does not independently undertake a commitment or obligation. The exclamation mark and emotional situation do not establish expressive/reflexive force, and nothing important in the core utterance falls outside T/P/E.
- **Ontology fit:** natural — T/P/E/O naturally represents the core utterance as a strong truth-conditional avowal. Its courtship purpose and rhetorical inadequacy are adequately handled as context, without P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "rostand-cyrano-de-bergerac-9299dcd45fdf",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.94,
    "analysis": "Christian's direct “Je t'aime !” primarily avows as true his loving feeling toward Roxane. Although uttered in a courtship scene, it does not independently undertake a commitment or obligation. The exclamation mark and emotional situation do not establish expressive/reflexive force, and nothing important in the core utterance falls outside T/P/E.",
    "ambiguity": "The declaration pragmatically advances Christian's courtship, but courtship and desired relational effect alone do not supply performative undertaking force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Christian directly addresses the love declaration to Roxane within the dramatic action."
  },
  "contextual_interpretation": "In the wider balcony-scene context, Christian attempts to woo Roxane in his own words rather than relying on Cyrano's eloquence. His blunt, repetitive declaration is sincere as an avowal but fails to satisfy Roxane's demand for elaborated language. That dramatic inadequacy concerns rhetorical execution, not a core force beyond truth-conditional avowal.",
  "evidence": [
    {
      "evidence_id": "ev-local-1",
      "source": "local_text",
      "quotation_or_description": "“CHRISTIAN: Je t'aime !”",
      "supports": "The explicit first-person declaration, assigned directly to Christian, strongly supports truth-conditional avowal and direct utterance status.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev-meta-1",
      "source": "supplied_metadata",
      "quotation_or_description": "The supplied metadata identifies the source as Edmond Rostand's French play Cyrano de Bergerac.",
      "supports": "Confirms that the speaker label and line constitute staged dramatic dialogue rather than narrator report.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev-bg-1",
      "source": "background_knowledge",
      "quotation_or_description": "In the surrounding balcony episode, Christian tries to speak to Roxane without Cyrano's verbal assistance; Roxane finds his bare declarations rhetorically insufficient and asks for greater elaboration.",
      "supports": "Reinforces that the line functions as a direct, blunt avowal in courtship rather than as a commitment or reflex-like verbal discharge.",
      "confidence": 0.93
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.93,
    "contribution": "Identified the line's place in the balcony courtship episode and the contrast between Christian's sincere but ineloquent avowal and Roxane's demand for eloquence."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T/P/E/O naturally represents the core utterance as a strong truth-conditional avowal. Its courtship purpose and rhetorical inadequacy are adequately handled as context, without P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 8. `rostand-cyrano-de-bergerac-c724091d5f24`

- **Exact match:** `je vous aime`
- **Pattern:** `fr_je_vous_aime` (v0.4)
- **Source offsets:** 126591–126603
- **Relative position:** 0.522223
- **Chapter/section:** Unavailable
- **Supplied context:** 758 characters (127 before; 619 after)

#### Passage

> CYRANO:
>   Tous ceux, tous ceux, tous ceux
>   Qui me viendront, je vais vous les jeter, en touffe,
>   Sans les mettre en bouquet: je vous aime, j'étouffe,
>   Je t'aime, je suis fou, je n'en peux plus, c'est trop;
>   Ton nom est dans mon cœur comme dans un grelot,
>   Et comme tout le temps, Roxane, je frissonne,
>   Tout le temps, le grelot s'agite, et le nom sonne !
>   De toi, je me souviens de tout, j'ai tout aimé:
>   Je sais que l'an dernier, un jour, le douze mai,
>   Pour sortir le matin tu changeas de coiffure !
>   J'ai tellement pris pour clarté ta chevelure
>   Que, comme lorsqu'on a trop fixé le soleil,
>   On voit sur toute chose ensuite un rond vermeil,
>   Sur tout, quand j'ai quitté les feux dont tu m'inondes,
>   Mon regard ébloui pose des taches blondes !

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\gutenberg-1256\annotations\rostand-cyrano-de-bergerac-c724091d5f24\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 3 / 0
- **Core analysis:** Cyrano’s “je vous aime” is principally a sincere avowal of his loving state. It also has substantial expressive/reflexive force: he describes himself as throwing out whatever words come to him without arranging them, and the declaration immediately spills into “je t’aime,” “j’étouffe,” and “je n’en peux plus.” This provides evidence of affect producing the words, beyond passionate delivery alone. Its role in courtship gives slight performative support, but the utterance does not clearly undertake a commitment or obligation.
- **Ontology fit:** natural — T and E naturally capture the sincere avowal and the explicitly represented affective outpouring. A small P score registers its limited relational enactment within courtship, while the concealed proxy arrangement is adequately handled as context rather than as a missing core-force category.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "rostand-cyrano-de-bergerac-c724091d5f24",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 3,
      "other": 0
    },
    "confidence": 0.93,
    "analysis": "Cyrano’s “je vous aime” is principally a sincere avowal of his loving state. It also has substantial expressive/reflexive force: he describes himself as throwing out whatever words come to him without arranging them, and the declaration immediately spills into “je t’aime,” “j’étouffe,” and “je n’en peux plus.” This provides evidence of affect producing the words, beyond passionate delivery alone. Its role in courtship gives slight performative support, but the utterance does not clearly undertake a commitment or obligation.",
    "ambiguity": "Because Cyrano speaks in a concealed proxy role, the declaration simultaneously advances Christian’s courtship as Roxane understands it and expresses Cyrano’s own love. This complicates speaker attribution and uptake but does not require O."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly spoken declaration by Cyrano to Roxane, complicated by his concealed role as Christian’s proxy: Roxane receives the voice and words as part of Christian’s courtship, while Cyrano voices his own feelings."
  },
  "contextual_interpretation": "The declaration occurs in an escalating, deliberately unpolished outpouring. Cyrano moves from formal “vous” to intimate “tu” and surrounds the avowal with images of choking, madness, trembling, and involuntary resonance. In the wider balcony scene, he is speaking from concealment for Christian; nevertheless, the emotional content is Cyrano’s own sincere love. The proxy deception changes Roxane’s understanding of who avows the love, not the core utterance’s strong T and E forces.",
  "evidence": [
    {
      "evidence_id": "ev1",
      "source": "local_text",
      "quotation_or_description": "“je vous aime, j’étouffe, / Je t’aime, je suis fou, je n’en peux plus, c’est trop”",
      "supports": "Strong T support from the explicit avowal; the rapid repetition, pronoun shift, and presentation of emotional overflow contribute to E when read with the preceding account of words arriving unarranged.",
      "confidence": 0.98
    },
    {
      "evidence_id": "ev2",
      "source": "local_text",
      "quotation_or_description": "“Tous ceux… / Qui me viendront, je vais vous les jeter, en touffe, / Sans les mettre en bouquet”",
      "supports": "Positive independent evidence for E: Cyrano presents the words as coming to him and being released in an unarranged mass, rather than solely as a composed assertion.",
      "confidence": 0.94
    },
    {
      "evidence_id": "ev3",
      "source": "local_text",
      "quotation_or_description": "“Ton nom est dans mon cœur comme dans un grelot… le grelot s’agite, et le nom sonne !”",
      "supports": "Portrays Roxane’s name as sounding through an affect-driven, quasi-involuntary response, reinforcing expressive/reflexive force and the sincerity of the avowed state.",
      "confidence": 0.9
    },
    {
      "evidence_id": "ev4",
      "source": "background_knowledge",
      "quotation_or_description": "In the balcony scene, Cyrano speaks from concealment as Christian’s verbal proxy, while the eloquence and love he expresses are his own; Roxane attributes the address to Christian.",
      "supports": "Explains the direct-but-proxied status, the mismatch in participant understanding, and why the utterance can sincerely avow Cyrano’s state while functioning contextually in Christian’s courtship.",
      "confidence": 0.95
    },
    {
      "evidence_id": "ev5",
      "source": "supplied_metadata",
      "quotation_or_description": "The supplied metadata identifies the work as Edmond Rostand’s French play “Cyrano de Bergerac” and locates the match around relative position 0.522.",
      "supports": "Supports attribution and general placement of the occurrence; it does not independently determine the core force.",
      "confidence": 1.0
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.95,
    "contribution": "Used to identify the balcony-scene proxy arrangement: Cyrano speaks under cover for Christian, Roxane misattributes the declaration, and Cyrano’s words nevertheless express his own love."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T and E naturally capture the sincere avowal and the explicitly represented affective outpouring. A small P score registers its limited relational enactment within courtship, while the concealed proxy arrangement is adequately handled as context rather than as a missing core-force category.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The high E score rests not on exclamation, repetition, or passion alone, but on the passage’s explicit representation of words arriving spontaneously and being released without rhetorical arrangement."
}
```

</details>

### 9. `rostand-cyrano-de-bergerac-1c7571f33a3e`

- **Exact match:** `Je t'aime`
- **Pattern:** `fr_je_taime_apostrophe_spacing` (v0.4)
- **Source offsets:** 126618–126627
- **Relative position:** 0.522334
- **Chapter/section:** Unavailable
- **Supplied context:** 758 characters (154 before; 595 after)

#### Passage

> CYRANO:
>   Tous ceux, tous ceux, tous ceux
>   Qui me viendront, je vais vous les jeter, en touffe,
>   Sans les mettre en bouquet: je vous aime, j'étouffe,
>   Je t'aime, je suis fou, je n'en peux plus, c'est trop;
>   Ton nom est dans mon cœur comme dans un grelot,
>   Et comme tout le temps, Roxane, je frissonne,
>   Tout le temps, le grelot s'agite, et le nom sonne !
>   De toi, je me souviens de tout, j'ai tout aimé:
>   Je sais que l'an dernier, un jour, le douze mai,
>   Pour sortir le matin tu changeas de coiffure !
>   J'ai tellement pris pour clarté ta chevelure
>   Que, comme lorsqu'on a trop fixé le soleil,
>   On voit sur toute chose ensuite un rond vermeil,
>   Sur tout, quand j'ai quitté les feux dont tu m'inondes,
>   Mon regard ébloui pose des taches blondes !

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\gutenberg-1256\annotations\rostand-cyrano-de-bergerac-1c7571f33a3e\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 3 / 0
- **Core analysis:** “Je t’aime” strongly avows a loving state and also forms part of an affective verbal outpouring. Cyrano explicitly frames his words as arriving spontaneously and being thrown forth without arrangement, while “j’étouffe” and “je n’en peux plus” present speech as a release of overwhelming feeling; this supplies independent support for E beyond mere passionate delivery. The declaration participates weakly in courtship, but it does not itself clearly undertake a commitment or obligation.
- **Ontology fit:** natural — T and E naturally capture the utterance’s joint force as a sincere avowal and an explicitly represented overflow of affect; a small P score captures its participation in courtship. The assumed identity and split attribution are contextual complications rather than missing dimensions of core force.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "rostand-cyrano-de-bergerac-1c7571f33a3e",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 3,
      "other": 0
    },
    "confidence": 0.91,
    "analysis": "“Je t’aime” strongly avows a loving state and also forms part of an affective verbal outpouring. Cyrano explicitly frames his words as arriving spontaneously and being thrown forth without arrangement, while “j’étouffe” and “je n’en peux plus” present speech as a release of overwhelming feeling; this supplies independent support for E beyond mere passionate delivery. The declaration participates weakly in courtship, but it does not itself clearly undertake a commitment or obligation.",
    "ambiguity": "The utterance advances a romantic relationship while Cyrano speaks under Christian’s identity, which gives some possible performative force; nevertheless, its dominant forces are avowal and expressive discharge."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly spoken declaration by Cyrano to Roxane, complicated by his speaking in the balcony scene under Christian’s identity and ostensibly on Christian’s behalf."
  },
  "contextual_interpretation": "The immediate language presents an unpolished overflow of Cyrano’s feelings: he will cast out whatever words come, “sans les mettre en bouquet,” and places “Je t’aime” amid claims of choking, madness, and being unable to endure more. In the wider dramatic situation, Roxane understands the voice as expressing Christian’s love, whereas Cyrano is voicing his own genuine and highly observant love through that assumed identity. This interpersonal deception affects attribution and courtship consequences but does not prevent the utterance from functioning as a sincere avowal and expressive release for Cyrano.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“je vous aime, j’étouffe, / Je t’aime, je suis fou, je n’en peux plus, c’est trop”",
      "supports": "The explicit declaration and surrounding first-person descriptions strongly support T; the representation of emotional pressure and release also supports E.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“Tous ceux… / Qui me viendront, je vais vous les jeter, en touffe, / Sans les mettre en bouquet”",
      "supports": "Cyrano describes casting out the words as they come rather than arranging them, positive evidence that their production functions as spontaneous expressive discharge rather than only an intense assertion.",
      "confidence": 0.96
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“Ton nom est dans mon cœur comme dans un grelot… le grelot s’agite, et le nom sonne !”",
      "supports": "The image represents Roxane’s name as involuntarily sounding within him, reinforcing reflexive or affect-driven verbal expression while also elaborating the claimed loving state.",
      "confidence": 0.9
    },
    {
      "evidence_id": "e4",
      "source": "local_text",
      "quotation_or_description": "Cyrano recalls Roxane’s changed hairstyle on a specific date and describes her hair as a dazzling light that colors his subsequent vision.",
      "supports": "Detailed, sustained attention to Roxane supports interpretation of “Je t’aime” as a substantive avowal rather than an empty token.",
      "confidence": 0.94
    },
    {
      "evidence_id": "e5",
      "source": "background_knowledge",
      "quotation_or_description": "In the play’s balcony scene, Cyrano speaks to Roxane while she takes the declarations to be Christian’s, allowing Cyrano to express his own love through Christian’s assumed role.",
      "supports": "Explains the divided attribution, the deceptive courtship setting, and the limited P support without treating those contextual complications as ontology failure.",
      "confidence": 0.94
    },
    {
      "evidence_id": "e6",
      "source": "supplied_metadata",
      "quotation_or_description": "The supplied metadata identifies the passage as Edmond Rostand’s French play “Cyrano de Bergerac.”",
      "supports": "Grounds the use of work-level knowledge concerning Cyrano, Roxane, Christian, and the dramatic impersonation.",
      "confidence": 1.0
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.94,
    "contribution": "Used to identify the excerpt as the balcony-scene declaration in which Cyrano speaks under Christian’s identity, clarifying who voices the words, whose feelings they express, and how Roxane understands them."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T and E naturally capture the utterance’s joint force as a sincere avowal and an explicitly represented overflow of affect; a small P score captures its participation in courtship. The assumed identity and split attribution are contextual complications rather than missing dimensions of core force.",
    "candidate_recurrent_dimension": null
  },
  "notes": "E is supported not simply by intensity or exclamatory language, but by the passage’s explicit metapragmatic presentation of words arriving unarranged and being cast forth under emotional pressure."
}
```

</details>

### 10. `rostand-cyrano-de-bergerac-12e4a608d4b9`

- **Exact match:** `je t'aime`
- **Pattern:** `fr_je_taime_apostrophe_spacing` (v0.4)
- **Source offsets:** 128515–128524
- **Relative position:** 0.530160
- **Chapter/section:** Unavailable
- **Supplied context:** 94 characters (44 before; 41 after)

#### Passage

> ROXANE:
>   Oui, je tremble, et je pleure, et je t'aime, et suis tienne !
>   Et tu m'as enivrée !

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\gutenberg-1256\annotations\rostand-cyrano-de-bergerac-12e4a608d4b9\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 2 / 0 / 0
- **Core analysis:** Roxane directly avows her love as a present emotional truth. The coordinated declaration “et suis tienne” (“and am yours”) gives the avowal some relational-undertaking force, though the highlighted “je t’aime” remains primarily truth-conditional. Trembling, weeping, intoxication imagery, exclamation, and cumulative syntax establish intense delivery but do not independently show that the words function as a reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the explicit avowal, while P captures the undertaking pressure supplied by “suis tienne.” The surrounding affect can be represented as contextual intensity without assigning E, and no important aspect of the core force requires O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "rostand-cyrano-de-bergerac-12e4a608d4b9",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 2,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.91,
    "analysis": "Roxane directly avows her love as a present emotional truth. The coordinated declaration “et suis tienne” (“and am yours”) gives the avowal some relational-undertaking force, though the highlighted “je t’aime” remains primarily truth-conditional. Trembling, weeping, intoxication imagery, exclamation, and cumulative syntax establish intense delivery but do not independently show that the words function as a reflex-like expressive discharge.",
    "ambiguity": "Performative support depends on treating the highlighted avowal together with its immediately coordinated continuation, “et suis tienne”; considered in isolation, “je t’aime” would have weaker P support."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A direct dramatic utterance by Roxane to the man she takes herself to be addressing as Christian, although the balcony scene’s concealed-voice situation creates dramatic irony about whose eloquence has moved her."
  },
  "contextual_interpretation": "Roxane presents the love as sincere and overwhelming, coupling it with bodily signs of emotion and the declaration that she is his. In the wider balcony-scene context, she believes she is responding to Christian, while Cyrano has covertly supplied the eloquent language that intoxicates her. This mistaken attribution complicates the intended addressee and the audience’s interpretation, but it does not alter the core avowal into quotation, deception, or an ontological remainder outside T/P/E.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“ROXANE: Oui, je tremble, et je pleure, et je t'aime”",
      "supports": "The named speaker directly presents loving the addressee as true; the surrounding first-person affect descriptions establish emotional intensity.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“et suis tienne !”",
      "supports": "The immediately coordinated claim “and am yours” adds relational surrender or undertaking force, supporting P alongside the dominant avowal.",
      "confidence": 0.94
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“Et tu m'as enivrée !”",
      "supports": "Roxane portrays herself as emotionally overwhelmed or intoxicated by the addressee, supporting sincerity and intensity but not independently establishing expressive/reflexive core force.",
      "confidence": 0.96
    },
    {
      "evidence_id": "e4",
      "source": "supplied_metadata",
      "quotation_or_description": "The supplied source identifies the passage as French dramatic dialogue from Edmond Rostand’s Cyrano de Bergerac, with the match attributed to ROXANE.",
      "supports": "Supports reading the line as a character’s direct staged speech rather than narration or reported discourse.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e5",
      "source": "background_knowledge",
      "quotation_or_description": "In the balcony scene, Roxane believes she is hearing Christian’s courtship, while Cyrano covertly provides the eloquent speech that moves her.",
      "supports": "Explains the dramatic irony and mistaken attribution surrounding Roxane’s otherwise sincere direct avowal.",
      "confidence": 0.95
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.95,
    "contribution": "Used to identify the balcony scene’s concealed-voice arrangement and explain why Roxane’s sincere avowal has a dramatically complicated intended and overhearing audience."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T naturally captures the explicit avowal, while P captures the undertaking pressure supplied by “suis tienne.” The surrounding affect can be represented as contextual intensity without assigning E, and no important aspect of the core force requires O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 11. `rostand-cyrano-de-bergerac-d7654d72f26a`

- **Exact match:** `Je t'aime`
- **Pattern:** `fr_je_taime_apostrophe_spacing` (v0.4)
- **Source offsets:** 134381–134390
- **Relative position:** 0.554359
- **Chapter/section:** Unavailable
- **Supplied context:** 1095 characters (86 before; 1000 after)

#### Passage

> ROXANE:
>   Oh ! mais il ne va pas m'importuner toujours !
>   (Décachetant la lettre):
>   Je t'aime, et si. . .
>   (A la lueur de la lanterne de Ragueneau, elle lit, à l'écart, à voix basse):
>   Mademoiselle,
>   Les tambours
>   Battent; mon régiment boucle sa soubreveste;
>   Il part; moi, l'on me croit déjà parti: je reste.
>   Je vous désobéis. Je suis dans ce couvent.
>   Je vais venir, et vous le mande auparavant
>   Par un religieux simple comme une chèvre
>   Qui ne peut rien comprendre à ceci. Votre lèvre
>   M'a trop souri tantôt: j'ai voulu la revoir.
>   Éloignez un chacun, et daignez recevoir
>   L'audacieux déjà pardonné, je l'espère,
>   Qui signe votre très. . .et caetera. . .
>   (Au capucin):
>   Mon Père,
>   Voici ce que me dit cette lettre. Écoutez:
>   (Tous se rapprochent, elle lit à haute voix):
>   Mademoiselle,
>   Il faut souscrire aux volontés
>   Du cardinal, si dur que cela vous puisse être.
>   C'est la raison pourquoi j'ai fait choix, pour remettre
>   Ces lignes en vos mains charmantes, d'un très saint,
>   D'un très intelligent et discret capucin;
>   Nous voulons qu'il vous donne, et dans votr

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\gutenberg-1256\annotations\rostand-cyrano-de-bergerac-d7654d72f26a\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The written “Je t'aime” straightforwardly presents the letter writer's love for Roxane as true. Neither the phrase itself nor its delivery independently enacts a commitment or functions as a reflex-like affective discharge.
- **Ontology fit:** natural — T naturally captures the phrase as a written avowal. The letter's courtship context, quiet revoicing, and Roxane's subsequent manipulation require no additional core-force category.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "rostand-cyrano-de-bergerac-d7654d72f26a",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "The written “Je t'aime” straightforwardly presents the letter writer's love for Roxane as true. Neither the phrase itself nor its delivery independently enacts a commitment or functions as a reflex-like affective discharge.",
    "ambiguity": "The sentence is interrupted by “et si...,” so its continuation is initially withheld; this does not materially obscure the avowal force of “Je t'aime.” The writer's sincerity is not established, but sincerity is orthogonal to T."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "written",
    "description": "A love avowal inscribed in a letter and briefly read aloud by Roxane; her voice revoices the letter writer's utterance."
  },
  "contextual_interpretation": "Roxane first reads the letter's private declaration and plans quietly. She then presents the capuchin with a substantially altered version of the letter, falsely attributing instructions to the cardinal. That later manipulation affects the scene's framing but does not change the highlighted written phrase's core force as an avowal of love.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "Roxane unseals the letter and reads: “Je t'aime, et si. . .”",
      "supports": "The explicit first-person declaration strongly supports truth-conditional avowal and establishes that the core event is written language being revoiced.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "The letter continues with the writer's plans to remain nearby and come to see Roxane, but the highlighted clause itself contains no promise or relational undertaking.",
      "supports": "The surrounding courtship and intended visit do not independently give the core “Je t'aime” performative force.",
      "confidence": 0.94
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "Roxane reads the letter quietly (“à voix basse”) and subsequently substitutes a different text when reading aloud to the capuchin.",
      "supports": "There is no positive evidence that the highlighted words are an expressive or reflex-like discharge; the later deception belongs to context rather than the core force.",
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
    "diagnosis": "T naturally captures the phrase as a written avowal. The letter's courtship context, quiet revoicing, and Roxane's subsequent manipulation require no additional core-force category.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 12. `rostand-cyrano-de-bergerac-e261412cd46c`

- **Exact match:** `je t'aime`
- **Pattern:** `fr_je_taime_apostrophe_spacing` (v0.4)
- **Source offsets:** 185292–185301
- **Relative position:** 0.764381
- **Chapter/section:** Unavailable
- **Supplied context:** 110 characters (99 before; 2 after)

#### Passage

> ROXANE:
>   Eh bien ! toi-même enfin l'emporte sur toi-même,
>   Et ce n'est plus que pour ton âme que je t'aime !

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\gutenberg-1256\annotations\rostand-cyrano-de-bergerac-e261412cd46c\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** Roxane directly avows as true that she now loves the addressee solely for his soul. The utterance defines the object and basis of her love rather than undertaking a commitment. Its exclamatory delivery does not independently indicate reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the core utterance as an avowal of love. Its emphasis, relational significance, and dramatic irony are adequately represented as contextual features; no independent P, E, or residual O force is required.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "rostand-cyrano-de-bergerac-e261412cd46c",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "Roxane directly avows as true that she now loves the addressee solely for his soul. The utterance defines the object and basis of her love rather than undertaking a commitment. Its exclamatory delivery does not independently indicate reflex-like expressive discharge.",
    "ambiguity": "The declaration has relational consequences and may reassure the addressee, but the text supplies no distinct commitment or undertaking sufficient for P."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Roxane directly addresses her interlocutor in dramatic dialogue and says that she loves him for his soul alone."
  },
  "contextual_interpretation": "The contrast between “toi-même” and “ton âme” presents Roxane's love as having shifted from physical attraction to devotion to the addressee's inner self. In the wider play, this is dramatically ironic: Roxane addresses Christian while the soul and eloquence she has come to love are substantially manifested through Cyrano's words, which she still attributes to Christian. That mistaken attribution affects the declaration's object and dramatic meaning but not its predominantly truth-conditional force as a sincere avowal of her understood emotional state.",
  "evidence": [
    {
      "evidence_id": "ev1",
      "source": "local_text",
      "quotation_or_description": "“Et ce n'est plus que pour ton âme que je t'aime !”",
      "supports": "The explicit first-person present-tense declaration strongly supports T: Roxane avows love and specifies that its basis is the addressee's soul.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev2",
      "source": "local_text",
      "quotation_or_description": "“toi-même enfin l'emporte sur toi-même”",
      "supports": "The preceding contrast frames the declaration as a considered claim about the addressee's inner self prevailing over outward appearance, not as an unmediated verbal reflex.",
      "confidence": 0.94
    },
    {
      "evidence_id": "ev3",
      "source": "local_text",
      "quotation_or_description": "The line ends with an exclamation mark and follows “Eh bien !”",
      "supports": "These features establish emphatic delivery but, without evidence of involuntary blurting or affective discharge, do not independently support E.",
      "confidence": 0.96
    },
    {
      "evidence_id": "ev4",
      "source": "background_knowledge",
      "quotation_or_description": "In the wider plot, Roxane believes she is responding to Christian's soul and eloquence, although Cyrano has supplied much of the language through which that apparent soul was revealed.",
      "supports": "This supplies the declaration's dramatic irony and explains why its sincere avowal can rest on a mistaken attribution without ceasing to be T.",
      "confidence": 0.94
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.94,
    "contribution": "Knowledge of Cyrano's authorship of Christian's love language clarifies the declaration's dramatic irony and mistaken attribution while leaving its core force as Roxane's sincere avowal intact."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T naturally captures the core utterance as an avowal of love. Its emphasis, relational significance, and dramatic irony are adequately represented as contextual features; no independent P, E, or residual O force is required.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 13. `rostand-cyrano-de-bergerac-c2ee2ff59ecc`

- **Exact match:** `Je vous aime`
- **Pattern:** `fr_je_vous_aime` (v0.4)
- **Source offsets:** 219634–219646
- **Relative position:** 0.906051
- **Chapter/section:** Unavailable
- **Supplied context:** 31 characters (10 before; 9 after)

#### Passage

> ROXANE:
>   Je vous aime, vivez !

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\gutenberg-1256\annotations\rostand-cyrano-de-bergerac-c2ee2ff59ecc\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** Roxane directly avows that she loves Cyrano. The adjoining imperative “vivez” makes the avowal an urgent reason for him to live, but it does not turn the highlighted words into a substantial commitment or undertaking. Their urgency and emotional intensity do not independently establish expressive/reflexive force.
- **Ontology fit:** natural — T naturally captures the core avowal, while a low P score preserves the slight force of relational recognition. Emotional urgency belongs in contextual delivery and does not require E or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "rostand-cyrano-de-bergerac-c2ee2ff59ecc",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.93,
    "analysis": "Roxane directly avows that she loves Cyrano. The adjoining imperative “vivez” makes the avowal an urgent reason for him to live, but it does not turn the highlighted words into a substantial commitment or undertaking. Their urgency and emotional intensity do not independently establish expressive/reflexive force.",
    "ambiguity": "The declaration may weakly enact belated relational recognition, supporting P=1, but the scene offers little prospect of a future undertaking and T remains clearly dominant."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Roxane directly addresses Cyrano in dramatic dialogue: “Je vous aime, vivez !”"
  },
  "contextual_interpretation": "In the play’s final recognition scene, Roxane understands that Cyrano was the true source of the loving language she had associated with Christian. Her declaration is therefore a sincere, belated avowal directed to Cyrano and an urgent appeal that he remain alive. The tragic timing intensifies its force without making it reflex-like or creating a substantial future commitment.",
  "evidence": [
    {
      "evidence_id": "e1-local-avowal",
      "source": "local_text",
      "quotation_or_description": "“ROXANE: Je vous aime, vivez !”",
      "supports": "The first-person present-tense declaration directly presents Roxane’s love as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2-local-appeal",
      "source": "local_text",
      "quotation_or_description": "The love declaration is immediately followed by the imperative “vivez” (“live”).",
      "supports": "The declaration functions as a reason within an urgent appeal, but the imperative supplies urgency rather than independent evidence of expressive/reflexive discharge or a relational undertaking.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e3-metadata-position",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is at relative position 0.906051 in Edmond Rostand’s Cyrano de Bergerac.",
      "supports": "Its late position is consistent with the climactic final-scene context, though position alone does not determine core force.",
      "confidence": 0.9
    },
    {
      "evidence_id": "e4-background-recognition",
      "source": "background_knowledge",
      "quotation_or_description": "In the final scene, Roxane recognizes Cyrano’s authorship or animating voice behind the letters and words through which she had loved Christian, while Cyrano is mortally wounded.",
      "supports": "This explains the declaration as a belated sincere avowal and life-saving plea, with only weak performative pressure and no need for O.",
      "confidence": 0.94
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.94,
    "contribution": "Knowledge of the final recognition and Cyrano’s mortal condition clarifies the addressee, sincerity, belated recognition, and the purpose of “vivez.”"
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T naturally captures the core avowal, while a low P score preserves the slight force of relational recognition. Emotional urgency belongs in contextual delivery and does not require E or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The classification applies to the highlighted “Je vous aime,” while treating the adjacent “vivez” as contextual evidence."
}
```

</details>

### 14. `rostand-cyrano-de-bergerac-ec44985258b2`

- **Exact match:** `Je t'aime`
- **Pattern:** `fr_je_taime_apostrophe_spacing` (v0.4)
- **Source offsets:** 219718–219727
- **Relative position:** 0.906397
- **Chapter/section:** Unavailable
- **Supplied context:** 197 characters (61 before; 127 after)

#### Passage

> CYRANO:
>   Non ! car c'est dans le conte
>   Que lorsqu'on dit: Je t'aime ! au prince plein de honte,
>   Il sent sa laideur fondre à ces mots de soleil. . .
>   Mais tu t'apercevrais que je reste pareil.

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\gutenberg-1256\annotations\rostand-cyrano-de-bergerac-ec44985258b2\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The represented “Je t'aime !” is a conventional avowal that presents the speaker's love for the prince as true. The passage supplies no undertaking or obligation beyond that avowal, and its exclamation mark and transformative emotional effect do not independently establish expressive/reflexive force.
- **Ontology fit:** natural — T naturally captures the represented declaration as an avowal. Its hypothetical quotation and fairy-tale framing are adequately recorded as utterance status and context; they create no residual core-force pressure requiring O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "rostand-cyrano-de-bergerac-ec44985258b2",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "The represented “Je t'aime !” is a conventional avowal that presents the speaker's love for the prince as true. The passage supplies no undertaking or obligation beyond that avowal, and its exclamation mark and transformative emotional effect do not independently establish expressive/reflexive force.",
    "ambiguity": "The fairy-tale declaration may carry a weak relational or courtship implication, but nothing in the excerpt establishes commitment-level performative force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "hypothetical",
    "description": "Cyrano cites a generic utterance within a fairy-tale scenario—“lorsqu'on dit: Je t'aime !”—rather than directly saying it to his present interlocutor."
  },
  "contextual_interpretation": "Cyrano invokes the declaration as part of a fairy-tale convention in which words of love make a shame-filled prince's ugliness disappear, then contrasts that magical result with his own unchanged appearance. This framing makes the occurrence hypothetical and metanarrative, but the represented declaration itself remains a truth-conditional avowal of love.",
  "evidence": [
    {
      "evidence_id": "ev1",
      "source": "local_text",
      "quotation_or_description": "“c'est dans le conte / Que lorsqu'on dit: Je t'aime !”",
      "supports": "The conditional-generic construction and explicit reference to a tale establish that the occurrence is a hypothetical, cited declaration.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev2",
      "source": "local_text",
      "quotation_or_description": "“au prince plein de honte”",
      "supports": "The represented words are addressed to a prince within the tale, supporting interpretation as an interpersonal avowal rather than Cyrano's direct present speech.",
      "confidence": 0.98
    },
    {
      "evidence_id": "ev3",
      "source": "local_text",
      "quotation_or_description": "“Il sent sa laideur fondre à ces mots de soleil. . . / Mais tu t'apercevrais que je reste pareil.”",
      "supports": "Cyrano contrasts the imagined transformative effect of the love words with reality; this supplies narrative framing but no independent evidence for performative or reflexive force in the core utterance.",
      "confidence": 0.97
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
    "diagnosis": "T naturally captures the represented declaration as an avowal. Its hypothetical quotation and fairy-tale framing are adequately recorded as utterance status and context; they create no residual core-force pressure requiring O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>
