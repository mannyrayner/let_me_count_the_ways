# Single-text pipeline report: Little Women

## Run summary

- **Run ID:** `gutenberg-514`
- **Work:** *Little Women* by Louisa May Alcott
- **Source:** `gutenberg-514`
- **Annotation:** v0.3.1 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 4
- **Valid occurrences:** 4
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.140092

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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-514\annotations\alcott-little-women-15ef9596ac4e\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** Mrs. March’s “I love you for it” directly avows her love for Jo while praising Jo’s effort to overcome shyness. It presents an emotional attitude as true. The utterance neither undertakes a commitment nor functions as a reflex-like affective discharge.
- **Ontology fit:** natural — T naturally captures the core force as an avowal of love. The surrounding praise and reassurance are contextual functions and create no residual pressure for P, E, or O.

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
    "confidence": 0.97,
    "analysis": "Mrs. March’s “I love you for it” directly avows her love for Jo while praising Jo’s effort to overcome shyness. It presents an emotional attitude as true. The utterance neither undertakes a commitment nor functions as a reflex-like affective discharge.",
    "ambiguity": "The excerpt’s dialogue segmentation is slightly awkward, but the exchange and Jo’s “Thank you, Mother” make the speaker and addressee sufficiently clear."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Mrs. March directly tells Jo, “I love you for it,” in a face-to-face mother-daughter exchange."
  },
  "contextual_interpretation": "The avowal is embedded in maternal praise and encouragement: Mrs. March commends Jo for trying to fight her shyness. The qualifying phrase “for it” links the declaration to Jo’s effort, while the surrounding affectionate response—a grateful kiss—supports a sincere reading. Its reassuring interpersonal effect does not itself create performative undertaking force.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“You do try to fight off your shyness, and I love you for it.”",
      "supports": "The declarative construction explicitly presents the speaker’s love for the addressee as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“That’s my good girl” and the praise of trying to overcome shyness frame the declaration as maternal approval and affection.",
      "supports": "Supports an affectionate, reassuring avowal rather than a commitment-forming or reflexive utterance.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“Thank you, Mother,” followed by Jo giving Mrs. March a grateful kiss.",
      "supports": "Identifies the exchange as between Jo and her mother and shows that the declaration is received as loving encouragement.",
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
    "diagnosis": "T naturally captures the core force as an avowal of love. The surrounding praise and reassurance are contextual functions and create no residual pressure for P, E, or O.",
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-514\annotations\alcott-little-women-44ca305cf65a\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** Mr. Brooke directly avows that he loves Meg. The wording presents his loving state as true and is therefore strongly truth-conditional. Although spoken during courtship and while seeking evidence of reciprocal affection, the core sentence does not itself clearly undertake a commitment. Tenderness and the intensifier “so much” indicate emotional delivery but provide no independent evidence of expressive/reflex-like discharge.
- **Ontology fit:** natural — T naturally captures the utterance as a direct avowal of love. Its tender courtship context can be described separately, with no residual core force requiring E, P, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "alcott-little-women-44ca305cf65a",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.95,
    "analysis": "Mr. Brooke directly avows that he loves Meg. The wording presents his loving state as true and is therefore strongly truth-conditional. Although spoken during courtship and while seeking evidence of reciprocal affection, the core sentence does not itself clearly undertake a commitment. Tenderness and the intensifier “so much” indicate emotional delivery but provide no independent evidence of expressive/reflex-like discharge.",
    "ambiguity": "The courtship setting gives the avowal relational significance, but that contextual function is insufficient to establish performative undertaking force in the core utterance."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Mr. Brooke directly addresses Meg and says, “I love you so much, dear.”"
  },
  "contextual_interpretation": "The avowal follows Mr. Brooke’s request to know whether Meg cares for him “a little,” so it functions as a sincere-seeming declaration offered while soliciting reciprocal feeling. The narration marks his manner as tender. These features reinforce the emotional avowal but do not independently turn it into either a commitment or a reflexive discharge.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I love you so much, dear,”",
      "supports": "The first-person present-tense declaration explicitly presents Mr. Brooke’s loving emotional state as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“I only want to know if you care for me a little, Meg.”",
      "supports": "The immediately preceding request frames the declaration as courtship and solicitation of reciprocal affection, while supplying no explicit undertaking or promise.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“added Mr. Brooke tenderly”",
      "supports": "Identifies the speaker and indicates tender delivery; this supports emotional intensity but not, by itself, expressive/reflexive core force.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter Twenty-Three of Louisa May Alcott’s Little Women.",
      "supports": "Confirms the work and location of the direct-dialogue event without adding a distinct core-force category.",
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
    "diagnosis": "T naturally captures the utterance as a direct avowal of love. Its tender courtship context can be described separately, with no residual core force requiring E, P, or O.",
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-514\annotations\alcott-little-women-58c41f8731dd\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The speaker directly avows that her love for her mother has not diminished despite her love for John. The core force is truth-conditional reassurance about an enduring emotional state. It does not itself undertake a commitment, and the clinging and tearful delivery do not independently establish expressive/reflexive force.
- **Ontology fit:** natural — T naturally captures the core avowal of an enduring loving state. Emotional delivery and adjacent future assurances are adequately treated as context, leaving no residual pressure for E, P, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "alcott-little-women-58c41f8731dd",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.98,
    "analysis": "The speaker directly avows that her love for her mother has not diminished despite her love for John. The core force is truth-conditional reassurance about an enduring emotional state. It does not itself undertake a commitment, and the clinging and tearful delivery do not independently establish expressive/reflexive force.",
    "ambiguity": "The surrounding promises of continued visits and family closeness have commitment-like force, but that force belongs to adjacent utterances rather than to the classified love clause."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A direct spoken utterance by the daughter to her mother, grammatically embedded under “Don’t feel ... that” but functioning as an avowal of undiminished love."
  },
  "contextual_interpretation": "On her wedding day, the speaker reassures Marmee that loving John and marrying him do not separate her emotionally from her family. The negative-comparative wording—“I love you any the less”—occurs within “Don’t feel ... that” and pragmatically affirms that her love remains undiminished. Her clinging and full eyes indicate emotional intensity, while the following promises concern continued family participation; neither feature changes the core clause from a primarily truth-conditional avowal.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Don’t feel that I am separated from you, Marmee dear, or that I love you any the less for loving John so much”",
      "supports": "The construction explicitly reassures Marmee that the speaker’s love for her remains undiminished, strongly supporting truth-conditional force.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“she said, clinging to her mother, with full eyes for a moment”",
      "supports": "This establishes an emotionally intense and affectionate delivery, but supplies no independent evidence that the words are a reflex-like expressive discharge.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“I shall come every day, Father, and expect to keep my old place in all your hearts, though I am married.”",
      "supports": "The adjacent future-oriented assurance clarifies the wedding-related fear of family separation, while remaining distinct from the core love avowal.",
      "confidence": 0.97
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
    "diagnosis": "T naturally captures the core avowal of an enduring loving state. Emotional delivery and adjacent future assurances are adequately treated as context, leaving no residual pressure for E, P, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-514\annotations\alcott-little-women-f1eab387a74e\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** Amy’s embedded declaration presents the strength and sincerity of her loving emotional state as true. Its placement within her claim that she would marry the addressee without money gives it weak secondary commitment-related force, but the core clause primarily avows love rather than independently undertaking an obligation. The emotional delivery does not supply evidence of reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the core avowal, with at most weak P support inherited from the surrounding marriage affirmation. No independently supported expressive/reflexive force or residual core function requires E or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "alcott-little-women-f1eab387a74e",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "Amy’s embedded declaration presents the strength and sincerity of her loving emotional state as true. Its placement within her claim that she would marry the addressee without money gives it weak secondary commitment-related force, but the core clause primarily avows love rather than independently undertaking an obligation. The emotional delivery does not supply evidence of reflex-like expressive discharge.",
    "ambiguity": "There is slight T/P overlap because the avowal supports Amy’s affirmation of marriage irrespective of wealth, but the commitment force principally belongs to the surrounding statement rather than to “I love you” itself."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Amy directly addresses the beloved, with “I love you” grammatically embedded in “show how much I love you” within her spoken reply."
  },
  "contextual_interpretation": "Amy reassures the addressee that accepting his proposal was not motivated by wealth: she says she forgot he was rich when she said yes and would have married him penniless. The love avowal therefore functions chiefly as a sincere assertion offered to rebut suspicion about her motives. The narrator’s statement that she gave “convincing proofs of the truth of her words” explicitly validates the avowal, while her affectionate response remains contextual confirmation rather than evidence of independent expressive/reflexive force.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“I sometimes wish you were poor that I might show how much I love you.”",
      "supports": "The highlighted clause directly presents Amy’s love, especially its magnitude, as an existing emotional state, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "“I’d have married you if you hadn’t a penny”",
      "supports": "The surrounding counterfactual marriage claim gives weak secondary support to relational commitment while showing that reassurance about motives is the immediate purpose.",
      "confidence": 0.95
    },
    {
      "evidence_id": "local-3",
      "source": "local_text",
      "quotation_or_description": "“Amy ... gave convincing proofs of the truth of her words.”",
      "supports": "The narrator frames Amy’s preceding words as truth-bearing and sincere, reinforcing the truth-conditional interpretation rather than a reflex-like discharge.",
      "confidence": 0.98
    },
    {
      "evidence_id": "metadata-1",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter Forty-Four of Louisa May Alcott’s Little Women and is presented in quoted dialogue.",
      "supports": "Confirms that the classified event is a character’s direct spoken utterance in the novel rather than narration or writing.",
      "confidence": 0.99
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
    "diagnosis": "T naturally captures the core avowal, with at most weak P support inherited from the surrounding marriage affirmation. No independently supported expressive/reflexive force or residual core function requires E or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>
