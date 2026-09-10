# Single-text pipeline report: The Age of Innocence

## Run summary

- **Run ID:** `gutenberg-541`
- **Work:** *The Age of Innocence* by Edith Wharton
- **Source:** `gutenberg-541`
- **Annotation:** v0.3.1 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 1
- **Valid occurrences:** 1
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.036000

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `wharton-age-of-innocence-64e6f2454e5c`

- **Exact match:** `I do love / you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.6)
- **Source offsets:** 132760–132773
- **Relative position:** 0.229533
- **Chapter/section:** Unavailable
- **Supplied context:** 383 characters (336 before; 34 after)

#### Passage

> He stood silent, beating his stick nervously against his boot-top;
> and feeling that she had indeed found the right way of closing the
> discussion, she went on light-heartedly: "Oh, did I tell you that I
> showed Ellen my ring? She thinks it the most beautiful setting she ever
> saw. There's nothing like it in the rue de la Paix, she said. I do love
> you, Newland, for being so artistic!"

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-541\annotations\wharton-age-of-innocence-64e6f2454e5c\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The speaker directly avows affectionate love for Newland, specifically praising his artistic choice of the ring. The utterance presents her loving feeling as true. It does not independently undertake a commitment, and its light-hearted, emphatic delivery does not establish expressive/reflexive force beyond an animated avowal.
- **Ontology fit:** natural — T naturally captures the core avowal. The tension-management, praise, and possible conventional hyperbole belong to contextual interpretation and leave no important residual core force requiring P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "wharton-age-of-innocence-64e6f2454e5c",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.94,
    "analysis": "The speaker directly avows affectionate love for Newland, specifically praising his artistic choice of the ring. The utterance presents her loving feeling as true. It does not independently undertake a commitment, and its light-hearted, emphatic delivery does not establish expressive/reflexive force beyond an animated avowal.",
    "ambiguity": "The phrasing may be partly conventional or hyperbolic gratitude for Newland's taste, but it still presents affection as the speaker's actual attitude."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly spoken utterance by the woman addressing Newland within narrated dialogue."
  },
  "contextual_interpretation": "After an uncomfortable discussion, the speaker changes to the safer subject of her ring and speaks light-heartedly. Her declaration combines affection with praise and gratitude for Newland's artistic taste. Its conversational function may include easing tension, but that contextual role does not alter the core force from a truth-conditional avowal or create a distinct performative undertaking.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I do love you, Newland, for being so artistic!”",
      "supports": "The first-person present-tense declaration explicitly presents love for Newland as true, while the reason clause frames it as affectionate praise.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "The narration says that she “went on light-heartedly” after feeling she had found the right way to close the preceding discussion.",
      "supports": "The declaration helps redirect and lighten the conversation, but this framing supplies no independent evidence of commitment or reflex-like verbal discharge.",
      "confidence": 0.95
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "She has just reported showing Ellen her ring and Ellen's admiration of its setting.",
      "supports": "The immediate trigger is appreciation of Newland's artistic choice, supporting an affectionate, complimentary avowal rather than a relational undertaking.",
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
    "diagnosis": "T naturally captures the core avowal. The tension-management, praise, and possible conventional hyperbole belong to contextual interpretation and leave no important residual core force requiring P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>
