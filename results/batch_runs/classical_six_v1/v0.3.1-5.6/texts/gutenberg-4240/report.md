# Single-text pipeline report: Women in Love

## Run summary

- **Run ID:** `gutenberg-4240`
- **Work:** *Women in Love* by D. H. Lawrence
- **Source:** `gutenberg-4240`
- **Annotation:** v0.3.1 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 9
- **Valid occurrences:** 9
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.328256

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `lawrence-women-in-love-9231790d35a8`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.6)
- **Source offsets:** 311710–311720
- **Relative position:** 0.304540
- **Chapter/section:** CHAPTER XIII.
- **Supplied context:** 81 characters (1 before; 70 after)

#### Passage

> “I love you right enough,” he said, grimly. “But I want it to be
> something else.”

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-4240\annotations\lawrence-women-in-love-9231790d35a8\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The speaker directly avows that he does love the addressee. “Right enough” confirms the truth of that state, while the adversative continuation distinguishes this acknowledged love from the different kind of relation he wants. Nothing in the wording undertakes a commitment, and “grimly” describes delivery without making the words an expressive or reflex-like discharge.
- **Ontology fit:** natural — T naturally captures the core as an avowal of an existing loving state. The dissatisfaction and grimness belong to contextual framing, and no residual core force requires P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "lawrence-women-in-love-9231790d35a8",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "The speaker directly avows that he does love the addressee. “Right enough” confirms the truth of that state, while the adversative continuation distinguishes this acknowledged love from the different kind of relation he wants. Nothing in the wording undertakes a commitment, and “grimly” describes delivery without making the words an expressive or reflex-like discharge.",
    "ambiguity": "The unspecified “something else” complicates the speaker’s desired relationship but does not materially obscure the force of the love utterance itself."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly spoken first-person avowal in dialogue, followed by the speaker’s qualification of what he wants the relationship to become."
  },
  "contextual_interpretation": "The avowal is reluctant or dissatisfied rather than celebratory: the speaker concedes that he loves the addressee but immediately says that love, as presently conceived, is not the relational condition he wants. The grim delivery and contrastive “But” frame the statement as a sober acknowledgment, not a promise or affective outburst.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I love you right enough”",
      "supports": "The explicit first-person assertion, reinforced by “right enough,” strongly supports truth-conditional avowal.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“he said, grimly”",
      "supports": "The narration indicates a severe or reluctant manner of delivery, but supplies no independent evidence of reflex-like expressive force.",
      "confidence": 0.94
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“But I want it to be something else.”",
      "supports": "The speaker contrasts acknowledged love with a desired alternative relational form; this supports reading the core utterance as an admission rather than an undertaking.",
      "confidence": 0.96
    },
    {
      "evidence_id": "e4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as direct dialogue in Chapter XIII of D. H. Lawrence’s Women in Love.",
      "supports": "Confirms the bibliographic and narrative location of the classified event without altering its core-force analysis.",
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
    "diagnosis": "T naturally captures the core as an avowal of an existing loving state. The dissatisfaction and grimness belong to contextual framing, and no residual core force requires P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 2. `lawrence-women-in-love-62544ed4b4fe`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.6)
- **Source offsets:** 312294–312304
- **Relative position:** 0.305110
- **Chapter/section:** CHAPTER XIII.
- **Supplied context:** 105 characters (54 before; 41 after)

#### Passage

> “Yes,—my love, yes,—my love. Let love be enough then. I love you then—I
> love you. I’m bored by the rest.”

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-4240\annotations\lawrence-women-in-love-62544ed4b4fe\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 2 / 0 / 0
- **Core analysis:** The highlighted “I love you” directly avows a loving state and therefore strongly supports T. In conjunction with “Let love be enough then” and the repeated avowal, it also helps accept or affirm love as the basis of the relationship, giving moderate support to P. The repetition and emotional setting do not independently show that the words are a reflex-like affective discharge, so E receives no support.
- **Ontology fit:** natural — T naturally captures the avowal, while P captures the limited relational-settlement force supplied by the immediate wording. No independently expressive/reflexive or residual core force requires E or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "lawrence-women-in-love-62544ed4b4fe",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 2,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.91,
    "analysis": "The highlighted “I love you” directly avows a loving state and therefore strongly supports T. In conjunction with “Let love be enough then” and the repeated avowal, it also helps accept or affirm love as the basis of the relationship, giving moderate support to P. The repetition and emotional setting do not independently show that the words are a reflex-like affective discharge, so E receives no support.",
    "ambiguity": "The main uncertainty is how much undertaking force belongs to the highlighted sentence itself rather than to the preceding proposal, “Let love be enough then.”"
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A character directly addresses another with the highlighted spoken avowal, immediately followed by its repetition."
  },
  "contextual_interpretation": "The repeated avowal is framed by “Let love be enough then,” making it sound like a deliberative or concessive settlement: the speaker affirms love and dismisses whatever further relational theory, conditions, or discussion constitutes “the rest.” This framing adds some commitment-like force, but the core remains primarily an assertion or avowal of love. Nothing in the excerpt establishes reflexive or uncontrolled production.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I love you then—I love you.”",
      "supports": "The explicit first-person present-tense avowal strongly supports truth-conditional force; repetition reinforces the avowal but does not by itself establish expressive/reflexive force.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“Let love be enough then.”",
      "supports": "Frames the avowal as acceptance of love as a sufficient relational basis, providing moderate support for performative or undertaking force.",
      "confidence": 0.88
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“I’m bored by the rest.”",
      "supports": "Suggests the speaker is dismissing additional discussion or requirements and settling on the affirmation of love, while also making the precise scope of the undertaking somewhat ambiguous.",
      "confidence": 0.82
    },
    {
      "evidence_id": "e4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XIII of D. H. Lawrence’s Women in Love, in Project Gutenberg ebook 4240.",
      "supports": "Identifies the utterance as dialogue within the supplied literary work and establishes its documented location.",
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
    "diagnosis": "T naturally captures the avowal, while P captures the limited relational-settlement force supplied by the immediate wording. No independently expressive/reflexive or residual core force requires E or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 3. `lawrence-women-in-love-34699c42511c`

- **Exact match:** `I / love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.6)
- **Source offsets:** 312310–312320
- **Relative position:** 0.305126
- **Chapter/section:** CHAPTER XIII.
- **Supplied context:** 105 characters (70 before; 25 after)

#### Passage

> “Yes,—my love, yes,—my love. Let love be enough then. I love you then—I
> love you. I’m bored by the rest.”

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-4240\annotations\lawrence-women-in-love-34699c42511c\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 2 / 0 / 0
- **Core analysis:** The repeated “I love you” directly avows a loving state, giving strong truth-conditional support. In conjunction with “Let love be enough then,” it also has some force as acceptance of a relationship defined by love, but it does not clearly undertake a specific commitment or obligation. Repetition and emotional emphasis alone do not establish expressive/reflexive force.
- **Ontology fit:** natural — T naturally captures the avowal, while P captures the weaker contextual suggestion of relational assent. Delivery and repetition can remain contextual features, so neither E nor O is needed.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "lawrence-women-in-love-34699c42511c",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 2,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.88,
    "analysis": "The repeated “I love you” directly avows a loving state, giving strong truth-conditional support. In conjunction with “Let love be enough then,” it also has some force as acceptance of a relationship defined by love, but it does not clearly undertake a specific commitment or obligation. Repetition and emotional emphasis alone do not establish expressive/reflexive force.",
    "ambiguity": "The immediate context supports a relational assent reading, but it is unclear how substantial an undertaking the speaker means by “Let love be enough then.”"
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A character directly addresses another with the repeated spoken avowal “I love you then—I love you.”"
  },
  "contextual_interpretation": "The speaker appears to accept love as sufficient while dismissing other considerations as tiresome: “I’m bored by the rest.” The utterance therefore combines a clear avowal with a limited element of relational assent. Nothing in the excerpt establishes that the words escape reflexively rather than serving as an emphatic declaration.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I love you then—I love you.”",
      "supports": "The direct and repeated first-person declaration strongly supports truth-conditional avowal; repetition supplies emphasis but not independently expressive/reflexive force.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“Let love be enough then.”",
      "supports": "Frames the avowal as an assent to making love sufficient, providing moderate but nonspecific performative or relational-undertaking support.",
      "confidence": 0.84
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“I’m bored by the rest.”",
      "supports": "Shows dismissal of considerations beyond love and helps explain the qualified relational-settlement reading without altering the core avowal's T/P/E classification.",
      "confidence": 0.9
    },
    {
      "evidence_id": "e4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XIII of D. H. Lawrence's Women in Love.",
      "supports": "Identifies the literary and chapter context of the direct dialogue without adding unsupported plot claims.",
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
    "diagnosis": "T naturally captures the avowal, while P captures the weaker contextual suggestion of relational assent. Delivery and repetition can remain contextual features, so neither E nor O is needed.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 4. `lawrence-women-in-love-834fba776e38`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.6)
- **Source offsets:** 529379–529389
- **Relative position:** 0.517201
- **Chapter/section:** CHAPTER XIX.
- **Supplied context:** 90 characters (12 before; 68 after)

#### Passage

> “Yes, I do. I love you, and I know it’s final. It is final, so why say
> any more about it.”

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-4240\annotations\lawrence-women-in-love-834fba776e38\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** The speaker directly and unequivocally avows love as a settled fact. Calling it “final” weakly suggests enduring relational commitment, but the utterance principally presents the speaker’s emotional state as true rather than explicitly undertaking an obligation. Nothing indicates that the words are a reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the decisive avowal, while a low P score records the limited commitment-like resonance of “final.” No independent expressive/reflexive or residual other force requires recognition.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "lawrence-women-in-love-834fba776e38",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.94,
    "analysis": "The speaker directly and unequivocally avows love as a settled fact. Calling it “final” weakly suggests enduring relational commitment, but the utterance principally presents the speaker’s emotional state as true rather than explicitly undertaking an obligation. Nothing indicates that the words are a reflex-like expressive discharge.",
    "ambiguity": "“Final” may carry a commitment-like implication, but it can also refer only to the speaker’s settled certainty about the truth of the feeling."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly spoken avowal within dialogue, reinforced by the immediately preceding confirmation “Yes, I do.”"
  },
  "contextual_interpretation": "The surrounding phrasing frames the avowal as decisive and no longer open to discussion: the speaker confirms the love, claims certainty about its finality, and dismisses further verbal elaboration. This deliberative, settled framing supports dominant truth-conditional force and provides little basis for expressive/reflexive force.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“Yes, I do. I love you”",
      "supports": "The affirmative lead-in and explicit declaration strongly support a direct truth-conditional avowal.",
      "confidence": 0.99
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "“and I know it’s final. It is final”",
      "supports": "The speaker represents the love as certain and settled; this reinforces T and gives limited support to an enduring commitment-like implication.",
      "confidence": 0.94
    },
    {
      "evidence_id": "local-3",
      "source": "local_text",
      "quotation_or_description": "“so why say any more about it”",
      "supports": "The refusal of further elaboration presents the matter as conclusively established rather than as an uncontrolled expressive discharge.",
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
    "diagnosis": "T naturally captures the decisive avowal, while a low P score records the limited commitment-like resonance of “final.” No independent expressive/reflexive or residual other force requires recognition.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 5. `lawrence-women-in-love-55f289758551`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.6)
- **Source offsets:** 779642–779652
- **Relative position:** 0.761708
- **Chapter/section:** CHAPTER XXVII.
- **Supplied context:** 165 characters (1 before; 154 after)

#### Passage

> “I love you,” he whispered as he kissed her, and trembled with pure
> hope, like a man who is born again to a wonderful, lively hope far
> exceeding the bounds of death.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-4240\annotations\lawrence-women-in-love-55f289758551\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** The direct declaration primarily avows the speaker’s loving emotional state. The kiss and imagery of renewed hope give the declaration relational significance, but the excerpt provides little evidence that the words themselves undertake a definite commitment. Whispering and trembling indicate intense affective delivery without independently showing that the words are a reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the core avowal, while a low P score records limited relational-enactment potential. Delivery and bodily emotion can be described contextually without assigning E, and no important residual core force requires O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "lawrence-women-in-love-55f289758551",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.92,
    "analysis": "The direct declaration primarily avows the speaker’s loving emotional state. The kiss and imagery of renewed hope give the declaration relational significance, but the excerpt provides little evidence that the words themselves undertake a definite commitment. Whispering and trembling indicate intense affective delivery without independently showing that the words are a reflex-like expressive discharge.",
    "ambiguity": "There is slight performative potential because the avowal occurs during an intimate, apparently relationship-renewing moment, but no explicit undertaking is stated."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A character directly says “I love you” to the woman he is kissing."
  },
  "contextual_interpretation": "The narration frames the avowal as sincere and intensely hopeful: he kisses her, trembles, and experiences hope likened to rebirth. These features strongly reinforce an emotionally consequential avowal, while remaining contextual evidence of intensity rather than establishing expressive/reflexive force. The passage suggests relational renewal but does not itself specify an obligation or promise.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I love you,”",
      "supports": "The declarative wording directly presents the speaker’s love as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“he whispered as he kissed her”",
      "supports": "The intimate delivery supports the sincerity and relational importance of the avowal, with only weak support for an enacted relational undertaking.",
      "confidence": 0.9
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“trembled with pure hope, like a man who is born again”",
      "supports": "The narration establishes great emotional intensity and renewed hope, but does not by itself establish reflex-like E force.",
      "confidence": 0.95
    },
    {
      "evidence_id": "e4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XXVII of D. H. Lawrence’s Women in Love.",
      "supports": "Identifies the declaration as character dialogue in the supplied literary context; it does not independently alter the force classification.",
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
    "diagnosis": "T naturally captures the core avowal, while a low P score records limited relational-enactment potential. Delivery and bodily emotion can be described contextually without assigning E, and no important residual core force requires O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 6. `lawrence-women-in-love-ad79781ee68c`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.6)
- **Source offsets:** 781013–781023
- **Relative position:** 0.763047
- **Chapter/section:** CHAPTER XXVII.
- **Supplied context:** 788 characters (485 before; 293 after)

#### Passage

> All this she could not know. She wanted to be made much of, to be
> adored. There were infinite distances of silence between them. How
> could he tell her of the immanence of her beauty, that was not form, or
> weight, or colour, but something like a strange, golden light! How
> could he know himself what her beauty lay in, for him. He said “Your
> nose is beautiful, your chin is adorable.” But it sounded like lies,
> and she was disappointed, hurt. Even when he said, whispering with
> truth, “I love you, I love you,” it was not the real truth. It was
> something beyond love, such a gladness of having surpassed oneself, of
> having transcended the old existence. How could he say ‘I’ when he was
> something new and unknown, not himself at all? This I, this old formula
> of the age, was a dead letter.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-4240\annotations\lawrence-women-in-love-ad79781ee68c\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The repeated utterance is principally a sincere avowal presenting the speaker's love as true. The narration's claim that it is "not the real truth" concerns the formula's inability to capture an experience said to exceed ordinary love and stable selfhood; it does not remove the utterance's truth-conditional mode. No commitment is undertaken, and whispering, repetition, and intense gladness do not independently establish expressive/reflexive force.
- **Ontology fit:** natural — T/P/E adequately represents the core force as a strong truth-conditional avowal. The passage creates residual philosophical pressure concerning whether conventional first-person love language can express transformed selfhood, but that pressure concerns the adequacy of the proposition and its narrative interpretation, not an additional recurrent force of the core utterance.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "lawrence-women-in-love-ad79781ee68c",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.94,
    "analysis": "The repeated utterance is principally a sincere avowal presenting the speaker's love as true. The narration's claim that it is \"not the real truth\" concerns the formula's inability to capture an experience said to exceed ordinary love and stable selfhood; it does not remove the utterance's truth-conditional mode. No commitment is undertaken, and whispering, repetition, and intense gladness do not independently establish expressive/reflexive force.",
    "ambiguity": "The narration simultaneously calls the words truthful and radically inadequate. This complicates their content and contextual interpretation, but the core speech act remains best classified as an avowal rather than as a performative undertaking or reflex-like discharge."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly spoken, twice-repeated utterance represented in quoted dialogue: \"I love you, I love you.\""
  },
  "contextual_interpretation": "The speaker whispers the avowal \"with truth,\" contrasting it with compliments that sounded like lies. Yet the narrator immediately qualifies it as \"not the real truth\": his experience is described as a glad transcendence of his former existence, so that both ordinary \"love\" and the pronoun \"I\" are inadequate formulas. This is narrative-philosophical reframing of a sincere avowal, not evidence that the utterance undertakes a commitment or erupts involuntarily from affect.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "\"Even when he said, whispering with truth, ‘I love you, I love you,’\"",
      "supports": "Explicitly characterizes the spoken words as truthful, strongly supporting truth-conditional avowal; it also establishes direct, repeated, whispered delivery.",
      "confidence": 0.99
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "\"it was not the real truth. It was something beyond love, such a gladness of having surpassed oneself\"",
      "supports": "Shows that the narration regards the conventional proposition as inadequate to the speaker's larger experience, while not supplying independent performative or reflex-like force.",
      "confidence": 0.97
    },
    {
      "evidence_id": "local-3",
      "source": "local_text",
      "quotation_or_description": "\"How could he say ‘I’ when he was something new and unknown, not himself at all? This I, this old formula of the age, was a dead letter.\"",
      "supports": "Locates the residual difficulty in the narration's critique of ordinary selfhood and linguistic formulation rather than in a distinct core speech-act force outside T/P/E.",
      "confidence": 0.96
    },
    {
      "evidence_id": "local-4",
      "source": "local_text",
      "quotation_or_description": "His earlier praise—\"Your nose is beautiful, your chin is adorable\"—\"sounded like lies,\" whereas the love utterance is delivered \"with truth.\"",
      "supports": "The local contrast reinforces the sincerity and avowal-like presentation of the love utterance.",
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
    "diagnosis": "T/P/E adequately represents the core force as a strong truth-conditional avowal. The passage creates residual philosophical pressure concerning whether conventional first-person love language can express transformed selfhood, but that pressure concerns the adequacy of the proposition and its narrative interpretation, not an additional recurrent force of the core utterance.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 7. `lawrence-women-in-love-d183a7d77a95`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.6)
- **Source offsets:** 781025–781035
- **Relative position:** 0.763059
- **Chapter/section:** CHAPTER XXVII.
- **Supplied context:** 788 characters (497 before; 281 after)

#### Passage

> All this she could not know. She wanted to be made much of, to be
> adored. There were infinite distances of silence between them. How
> could he tell her of the immanence of her beauty, that was not form, or
> weight, or colour, but something like a strange, golden light! How
> could he know himself what her beauty lay in, for him. He said “Your
> nose is beautiful, your chin is adorable.” But it sounded like lies,
> and she was disappointed, hurt. Even when he said, whispering with
> truth, “I love you, I love you,” it was not the real truth. It was
> something beyond love, such a gladness of having surpassed oneself, of
> having transcended the old existence. How could he say ‘I’ when he was
> something new and unknown, not himself at all? This I, this old formula
> of the age, was a dead letter.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-4240\annotations\lawrence-women-in-love-d183a7d77a95\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The repeated utterance is centrally an avowal presenting the speaker's love as true; the narration explicitly says that he speaks "with truth." It does not independently undertake a commitment, and neither whispering, repetition, nor intense gladness establishes expressive/reflexive force. The narrator's claim that the formula fails to capture a state "beyond love" qualifies the adequacy of its content but does not change the utterance's core force into something outside T/P/E.
- **Ontology fit:** natural — T naturally represents the utterance's core avowal force. The passage strongly questions whether ordinary first-person love language can capture the underlying transformed experience, but that residual literary and metaphysical pressure concerns representational adequacy rather than an additional core-force category.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "lawrence-women-in-love-d183a7d77a95",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.92,
    "analysis": "The repeated utterance is centrally an avowal presenting the speaker's love as true; the narration explicitly says that he speaks \"with truth.\" It does not independently undertake a commitment, and neither whispering, repetition, nor intense gladness establishes expressive/reflexive force. The narrator's claim that the formula fails to capture a state \"beyond love\" qualifies the adequacy of its content but does not change the utterance's core force into something outside T/P/E.",
    "ambiguity": "The phrase is locally called truthful yet \"not the real truth\": it truthfully avows love while remaining an inadequate conventional description of the speaker's transformed experience."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Narrated direct speech: he whispers the repeated avowal \"I love you, I love you.\""
  },
  "contextual_interpretation": "The speaker sincerely uses the conventional language of love, but the narrator treats that language as metaphysically inadequate. What he experiences is described as gladness in transcending his former self and existence, so both the predicate \"love\" and the old identity designated by \"I\" fail to express the whole experience. This narrative qualification concerns the avowal's descriptive adequacy, not deception, performative commitment, or reflex-like verbal discharge.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "\"he said, whispering with truth, ‘I love you, I love you’\"",
      "supports": "Explicitly identifies a sincere direct avowal, strongly supporting truth-conditional force.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "\"it was not the real truth. It was something beyond love\"",
      "supports": "Shows that the conventional avowal is presented as an incomplete description of the speaker's experience, creating ambiguity about content adequacy without displacing its T force.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "\"such a gladness of having surpassed oneself, of having transcended the old existence\"",
      "supports": "Explains the affective and metaphysical context, but supplies no clear evidence that saying the words is itself a reflex-like discharge or relational undertaking.",
      "confidence": 0.94
    },
    {
      "evidence_id": "e4",
      "source": "local_text",
      "quotation_or_description": "\"How could he say ‘I’ when he was something new and unknown, not himself at all? This I, this old formula of the age, was a dead letter.\"",
      "supports": "Establishes narrative pressure against the formula's adequacy while leaving the recognizable speech-act force as an avowal.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e5",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in D. H. Lawrence's Women in Love, Chapter XXVII, in Project Gutenberg ebook 4240.",
      "supports": "Identifies the work and location of the classified occurrence.",
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
    "diagnosis": "T naturally represents the utterance's core avowal force. The passage strongly questions whether ordinary first-person love language can capture the underlying transformed experience, but that residual literary and metaphysical pressure concerns representational adequacy rather than an additional core-force category.",
    "candidate_recurrent_dimension": null
  },
  "notes": "Repetition and whispered delivery are treated as contextual features, not independent evidence for E."
}
```

</details>

### 8. `lawrence-women-in-love-5ab672887915`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.6)
- **Source offsets:** 781615–781625
- **Relative position:** 0.763635
- **Chapter/section:** CHAPTER XXVII.
- **Supplied context:** 611 characters (297 before; 304 after)

#### Passage

> In the new, superfine bliss, a peace superseding knowledge, there was
> no I and you, there was only the third, unrealised wonder, the wonder
> of existing not as oneself, but in a consummation of my being and of
> her being in a new one, a new, paradisal unit regained from the
> duality. Nor can I say “I love you,” when I have ceased to be, and you
> have ceased to be: we are both caught up and transcended into a new
> oneness where everything is silent, because there is nothing to answer,
> all is perfect and at one. Speech travels between the separate parts.
> But in the perfect One there is perfect silence of bliss.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-4240\annotations\lawrence-women-in-love-5ab672887915\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 0 / 0 / 0 / 4
- **Core analysis:** “I love you” is mentioned as a possible form of speech whose applicability the narrator explicitly denies. It is neither an avowal of a loving state, a relational undertaking, nor an affect-driven verbal discharge; its core function here is metalinguistic and philosophical, illustrating speech that presupposes separate speakers.
- **Ontology fit:** natural — O naturally captures this non-use of the formula: it is cited within a philosophical denial of its applicability, not instantiated with T, P, or E force.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "lawrence-women-in-love-5ab672887915",
  "core_classification": {
    "label_support": {
      "truth_conditional": 0,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 4
    },
    "confidence": 0.97,
    "analysis": "“I love you” is mentioned as a possible form of speech whose applicability the narrator explicitly denies. It is neither an avowal of a loving state, a relational undertaking, nor an affect-driven verbal discharge; its core function here is metalinguistic and philosophical, illustrating speech that presupposes separate speakers.",
    "ambiguity": "The conventional phrase carries the idea of a love avowal in the background, but the passage does not represent anyone actually making that avowal."
  },
  "other_diagnosis": {
    "tpe_failure": "T/P/E classify uses that avow, undertake, or express love, whereas this occurrence mentions the formula in order to deny that it can be uttered under the imagined condition of transcendent oneness.",
    "core_not_context": "The residual property belongs to the embedded construction itself: “Nor can I say” places the quoted words under explicit negation of their sayability, making them a metalinguistically considered but unrealized utterance rather than a love speech act."
  },
  "utterance_status": {
    "status": "hypothetical",
    "description": "A quoted potential utterance embedded under the negated modal construction “Nor can I say”; no original act of saying “I love you” is represented as occurring."
  },
  "contextual_interpretation": "The narrator imagines a consummated union in which the distinction between “I” and “you” has disappeared. Because speech operates between separate beings, the familiar love formula is presented as impossible or conceptually inapplicable within this silent oneness. The surrounding prose conveys intense union, but that intensity does not give the quoted formula T, P, or E force.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“Nor can I say ‘I love you,’ when I have ceased to be, and you have ceased to be”",
      "supports": "The phrase is embedded as an explicitly unrealizable utterance rather than performed as an avowal, undertaking, or expressive discharge.",
      "confidence": 0.99
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "“Speech travels between the separate parts. But in the perfect One there is perfect silence of bliss.”",
      "supports": "The passage uses the formula metalinguistically to contrast interpersonal speech with a condition imagined to transcend separate speakers.",
      "confidence": 0.98
    },
    {
      "evidence_id": "metadata-1",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is in Chapter XXVII of D. H. Lawrence’s Women in Love.",
      "supports": "Identifies the bibliographic and chapter location of the classified occurrence.",
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
    "diagnosis": "O naturally captures this non-use of the formula: it is cited within a philosophical denial of its applicability, not instantiated with T, P, or E force.",
    "candidate_recurrent_dimension": "Metalinguistic mention or explicit denial of an utterance formula’s applicability"
  },
  "notes": null
}
```

</details>

### 9. `lawrence-women-in-love-9452b40305b4`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.6)
- **Source offsets:** 935591–935601
- **Relative position:** 0.914069
- **Chapter/section:** CHAPTER XXX.
- **Supplied context:** 101 characters (11 before; 80 after)

#### Passage

> “Why don’t I love you?” he asked, as if admitting the truth of her
> accusation, yet hating her for it.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-4240\annotations\lawrence-women-in-love-9452b40305b4\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The core utterance is the direct question “Why don’t I love you?”, which presupposes or strongly concedes that the speaker does not love the addressee and asks for an explanation. Its principal force is truth-conditional: it presents the absence of love as true. It neither undertakes a relational commitment nor functions as a reflex-like affective discharge.
- **Ontology fit:** natural — The truth-conditional category naturally captures the utterance’s apparent concession that love is absent. Negation and interrogative framing are ordinary variations within propositional force and create no residual need for O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "lawrence-women-in-love-9452b40305b4",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "The core utterance is the direct question “Why don’t I love you?”, which presupposes or strongly concedes that the speaker does not love the addressee and asks for an explanation. Its principal force is truth-conditional: it presents the absence of love as true. It neither undertakes a relational commitment nor functions as a reflex-like affective discharge.",
    "ambiguity": "The interrogative form formally asks for a reason rather than directly asserting non-love, but the narration explicitly frames it as an apparent admission of the accusation’s truth."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly spoken interrogative containing a negated love predication: “Why don’t I love you?”"
  },
  "contextual_interpretation": "The question is framed by the narrator as if it concedes the addressee’s accusation that the speaker does not love her. His simultaneous hatred complicates his attitude toward her but does not alter the utterance’s dominant force as an avowal or presentation of a non-loving state. The matched words “I love you” cannot be interpreted independently of the governing negation and why-question.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Why don’t I love you?”",
      "supports": "The why-question takes the speaker’s failure to love the addressee as its apparent premise, strongly supporting truth-conditional force concerning an absence of love.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“he asked, as if admitting the truth of her accusation”",
      "supports": "The narrator explicitly interprets the question as an apparent admission, reinforcing the high truth-conditional score.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“yet hating her for it”",
      "supports": "The surrounding affect is hostility rather than an enacted commitment or a reflexive discharge of love; it contextualizes but does not create a separate core force.",
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
    "diagnosis": "The truth-conditional category naturally captures the utterance’s apparent concession that love is absent. Negation and interrogative framing are ordinary variations within propositional force and create no residual need for O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The extraction match is only the substring “I love you”; classification properly applies to the complete utterance, including “Why don’t,” which reverses the polarity."
}
```

</details>
