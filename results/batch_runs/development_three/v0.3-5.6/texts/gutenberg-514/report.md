# Single-text pipeline report: Little Women

## Run summary

- **Run ID:** `gutenberg-514`
- **Work:** *Little Women* by Louisa May Alcott
- **Source:** `gutenberg-514`
- **Annotation:** v0.3 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 4
- **Valid occurrences:** 4
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 2
- **Estimated total cost:** USD 0.221928

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `alcott-little-women-15ef9596ac4e`

- **Exact match:** `I love / you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.2)
- **Source offsets:** 249186–249196
- **Relative position:** 0.242779
- **Chapter/section:** CHAPTER TWELVE
- **Supplied context:** 312 characters (64 before; 238 after)

#### Passage

> “That’s my good girl. You do try to fight off your shyness, and I love
> you for it. Fighting faults isn’t easy, as I know, and a cheery word
> kind of gives a lift. Thank you, Mother,” And Jo gave the thin cheek a
> grateful kiss, more precious to Mrs. March than if it had given back
> the rosy roundness of her youth.

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-514\annotations\alcott-little-women-15ef9596ac4e\attempt-002`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** “I love you for it” is a direct, reason-qualified avowal of maternal love. It presents the speaker’s loving state as true while praising the addressee’s effort to overcome shyness. It neither undertakes a commitment nor has predominantly reflexive or exclamatory force.
- **Ontology fit:** natural — T naturally captures the core avowal. The utterance’s praise and reassurance are contextual functions, not residual core force requiring P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "alcott-little-women-15ef9596ac4e",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.98,
    "analysis": "“I love you for it” is a direct, reason-qualified avowal of maternal love. It presents the speaker’s loving state as true while praising the addressee’s effort to overcome shyness. It neither undertakes a commitment nor has predominantly reflexive or exclamatory force.",
    "ambiguity": "The utterance also encourages and reassures Jo, but those interpersonal effects do not by themselves give it performative undertaking force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Mrs. March directly addresses Jo in dialogue, saying that she loves her for trying to fight her shyness."
  },
  "contextual_interpretation": "Mrs. March combines affectionate praise with encouragement: she identifies Jo’s effort to overcome a fault and offers love as the “cheery word” that can give her a lift. Jo’s grateful thanks and kiss confirm that the statement is received as sincere maternal affirmation. This supportive function remains contextual to a core truth-conditional avowal rather than constituting a new commitment.",
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“You do try to fight off your shyness, and I love you for it.”",
      "supports": "The declarative, reason-qualified wording strongly supports a truth-conditional avowal of love and does not suggest reflex-like exclamation.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“Fighting faults isn’t easy, as I know, and a cheery word kind of gives a lift.”",
      "supports": "The speaker frames the avowal as deliberate encouragement, weakening an exclamatory/reflexive reading without creating an undertaking.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“Thank you, Mother,” followed by Jo giving the speaker’s cheek a grateful kiss.",
      "supports": "Jo receives the utterance as affectionate maternal reassurance; the response supports sincerity and direct interpersonal address, though sincerity is not required for T.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as direct dialogue in Chapter Twelve of Louisa May Alcott’s Little Women.",
      "supports": "Locates the event within the supplied work and chapter and corroborates that the highlighted words belong to a narrated conversational scene.",
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
    "diagnosis": "T naturally captures the core avowal. The utterance’s praise and reassurance are contextual functions, not residual core force requiring P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 2. `alcott-little-women-44ca305cf65a`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.2)
- **Source offsets:** 460098–460108
- **Relative position:** 0.448267
- **Chapter/section:** CHAPTER TWENTY-THREE
- **Supplied context:** 129 characters (76 before; 43 after)

#### Passage

> “I won’t trouble you. I only want to know if you care for me a little,
> Meg. I love you so much, dear,” added Mr. Brooke tenderly.

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-514\annotations\alcott-little-women-44ca305cf65a\attempt-002`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** Mr. Brooke directly avows the intensity of his love for Meg. The utterance primarily presents his emotional state as true. Its courtship setting gives it slight undertaking force, but the words themselves do not clearly establish or renew a commitment, and the tender, deliberate delivery is not substantially reflex-like or exclamatory.
- **Ontology fit:** natural — T/P/E naturally represents the utterance as predominantly truth-conditional, with at most weak performative force from its relational setting and no important residual aspect requiring O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "alcott-little-women-44ca305cf65a",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.94,
    "analysis": "Mr. Brooke directly avows the intensity of his love for Meg. The utterance primarily presents his emotional state as true. Its courtship setting gives it slight undertaking force, but the words themselves do not clearly establish or renew a commitment, and the tender, deliberate delivery is not substantially reflex-like or exclamatory.",
    "ambiguity": "The declaration may help enact a courtship appeal, but that contextual relational function provides only weak support for P beyond the dominant T force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Mr. Brooke speaks the declaration directly to Meg in narrated dialogue."
  },
  "contextual_interpretation": "The declaration follows Mr. Brooke's request to know whether Meg cares for him even a little, so it functions as a sincere-seeming confession intended to invite reciprocation. “So much” intensifies the avowal, while “tenderly” presents the delivery as controlled affection rather than a reflexive outburst. The surrounding courtship appeal adds limited performative pressure but does not by itself turn the declaration into a clear undertaking.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I only want to know if you care for me a little, Meg. I love you so much, dear”",
      "supports": "The request for reciprocal feeling and the explicit declaration strongly support a truth-conditional avowal in a courtship context.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“added Mr. Brooke tenderly”",
      "supports": "The narration attributes the utterance directly to Mr. Brooke and characterizes its delivery as tender rather than strongly exclamatory or reflexive.",
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
    "diagnosis": "T/P/E naturally represents the utterance as predominantly truth-conditional, with at most weak performative force from its relational setting and no important residual aspect requiring O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 3. `alcott-little-women-58c41f8731dd`

- **Exact match:** `I love / you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.2)
- **Source offsets:** 514237–514247
- **Relative position:** 0.501014
- **Chapter/section:** CHAPTER TWENTY-FIVE
- **Supplied context:** 467 characters (63 before; 394 after)

#### Passage

> “Don’t feel that I am separated from you, Marmee dear, or that I love
> you any the less for loving John so much,” she said, clinging to her
> mother, with full eyes for a moment. “I shall come every day, Father,
> and expect to keep my old place in all your hearts, though I am
> married. Beth is going to be with me a great deal, and the other girls
> will drop in now and then to laugh at my housekeeping struggles. Thank
> you all for my happy wedding day. Good-by, good-by!”

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-514\annotations\alcott-little-women-58c41f8731dd\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 1 / 0
- **Core analysis:** Meg's embedded statement that she does not love Marmee any less strongly avows the continued truth of her filial love. Although emotionally delivered, it is a deliberate reassurance rather than primarily a reflexive exclamation. The core does not itself undertake a commitment; the promises and plans about visiting occur in the surrounding speech.
- **Ontology fit:** natural — T/P/E adequately represents the core as a strongly truth-conditional avowal with slight emotional-exclamatory coloring and no substantial undertaking force. The relational reassurance and wedding context require open contextual description but create no residual ontology pressure.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "alcott-little-women-58c41f8731dd",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 1,
      "other": 0
    },
    "confidence": 0.95,
    "analysis": "Meg's embedded statement that she does not love Marmee any less strongly avows the continued truth of her filial love. Although emotionally delivered, it is a deliberate reassurance rather than primarily a reflexive exclamation. The core does not itself undertake a commitment; the promises and plans about visiting occur in the surrounding speech.",
    "ambiguity": "Her clinging and full eyes give the utterance some exclamatory coloring, but its controlled syntax and reassurance function make truth-conditional force dominant."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly spoken but grammatically embedded equivalent of “I love you”: Meg tells Marmee not to think that her love has diminished."
  },
  "contextual_interpretation": "On her wedding day, Meg reassures her mother that loving and marrying John does not separate her emotionally from her family or reduce her love for Marmee. Her physical clinging and momentarily full eyes mark strong feeling. Her subsequent plans to visit and retain her place in the family's hearts reinforce the reassurance, but those future-oriented statements should not be transferred into performative force for the core love avowal itself.",
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“Don’t feel that I am separated from you, Marmee dear, or that I love you any the less for loving John so much”",
      "supports": "The negative comparative construction avows that Meg's love for Marmee continues undiminished, strongly supporting truth-conditional force.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "She speaks while “clinging to her mother, with full eyes for a moment.”",
      "supports": "The emotional physical presentation supplies limited exclamatory or affect-triggered coloring without displacing the utterance's clear propositional content.",
      "confidence": 0.96
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "Meg says, “I shall come every day” and expects “to keep my old place in all your hearts, though I am married.”",
      "supports": "The surrounding speech frames the love avowal as reassurance about continued family attachment; it also locates explicit future-oriented undertaking force outside the core clause.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter Twenty-Five of Louisa May Alcott's Little Women.",
      "supports": "This identifies the bibliographic and chapter location of the directly presented wedding-day exchange.",
      "confidence": 1.0
    }
  ],
  "background_knowledge": {
    "used": false,
    "familiarity": "moderate",
    "confidence": null,
    "contribution": null
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T/P/E adequately represents the core as a strongly truth-conditional avowal with slight emotional-exclamatory coloring and no substantial undertaking force. The relational reassurance and wedding context require open contextual description but create no residual ontology pressure.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The classification applies specifically to “I love you any the less” under the negated instruction not to think Meg's love has diminished."
}
```

</details>

### 4. `alcott-little-women-f1eab387a74e`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.2)
- **Source offsets:** 939298–939308
- **Relative position:** 0.915145
- **Chapter/section:** CHAPTER FORTY-FOUR
- **Supplied context:** 322 characters (192 before; 120 after)

#### Passage

> “Oh, my dearest boy, don’t, don’t say that! I forgot you were rich when
> I said ‘Yes’. I’d have married you if you hadn’t a penny, and I
> sometimes wish you were poor that I might show how much I love you.”
> And Amy, who was very dignified in public and very fond in private,
> gave convincing proofs of the truth of her words.

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-514\annotations\alcott-little-women-f1eab387a74e\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 1 / 0
- **Core analysis:** The core event is Amy's spoken, grammatically embedded avowal in “how much I love you.” It presents her love as an existing emotional state and emphasizes its degree. Although emotionally charged, it remains a deliberate assertion rather than a predominantly reflexive exclamation. It reassures her addressee about her motives, but the core clause does not itself undertake or renew a commitment.
- **Ontology fit:** natural — T/P/E adequately represents the core force: it is principally an avowal of a loving state, with slight affective emphasis and no substantial undertaking force. The surrounding reassurance, hypothetical framing, and narrative validation require contextual explanation but create no residual ontology pressure.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "alcott-little-women-f1eab387a74e",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 1,
      "other": 0
    },
    "confidence": 0.97,
    "analysis": "The core event is Amy's spoken, grammatically embedded avowal in “how much I love you.” It presents her love as an existing emotional state and emphasizes its degree. Although emotionally charged, it remains a deliberate assertion rather than a predominantly reflexive exclamation. It reassures her addressee about her motives, but the core clause does not itself undertake or renew a commitment.",
    "ambiguity": "The emphatic “how much” and the emotional surrounding speech give slight exclamatory force, but not enough to compete substantially with the clear truth-conditional avowal."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Amy directly speaks the love avowal to its addressee, although “I love you” is grammatically embedded within “show how much I love you” and a hypothetical wish."
  },
  "contextual_interpretation": "Amy is rebutting the implication that wealth motivated her acceptance. Her claims that she forgot he was rich and would have married him penniless frame the love avowal as sincere reassurance about her emotional state and marital motives. The narrator's statement that she gave “convincing proofs” explicitly endorses the truth of her words. This validating and affectionate context strengthens T but does not turn the embedded avowal itself into a distinct commitment-performing act.",
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“I sometimes wish you were poor that I might show how much I love you.”",
      "supports": "The embedded clause directly presents Amy's love and its degree as an existing emotional fact, strongly supporting truth-conditional force; “how much” adds limited emotional emphasis.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“I forgot you were rich when I said ‘Yes’. I’d have married you if you hadn’t a penny”",
      "supports": "The avowal functions contextually as reassurance that love rather than wealth motivated Amy, while the marriage claims remain surrounding evidence rather than commitment force encoded by the core clause.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "The narrator says Amy “gave convincing proofs of the truth of her words.”",
      "supports": "The narration explicitly treats Amy's speech as truth-evaluable and validates its sincerity, reinforcing the truth-conditional reading.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as spoken narrative dialogue in Chapter Forty-Four of Louisa May Alcott's Little Women, Project Gutenberg source 514.",
      "supports": "Establishes the bibliographic and narrative location of the classified occurrence without adding independent semantic force.",
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
    "diagnosis": "T/P/E adequately represents the core force: it is principally an avowal of a loving state, with slight affective emphasis and no substantial undertaking force. The surrounding reassurance, hypothetical framing, and narrative validation require contextual explanation but create no residual ontology pressure.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>
