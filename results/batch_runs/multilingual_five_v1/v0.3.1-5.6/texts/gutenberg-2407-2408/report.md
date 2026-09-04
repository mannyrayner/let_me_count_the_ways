# Single-text pipeline report: Die Leiden des jungen Werther

## Run summary

- **Run ID:** `gutenberg-2407-2408`
- **Work:** *Die Leiden des jungen Werther* by Johann Wolfgang von Goethe
- **Source:** `gutenberg-2407-2408`
- **Annotation:** v0.3.1 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 1
- **Valid occurrences:** 1
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.044188

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `goethe-die-leiden-des-jungen-werther-42853519d465`

- **Exact match:** `ich dich liebe`
- **Pattern:** `de_ich_dich_euch_liebe_subordinate` (v0.4)
- **Source offsets:** 226036–226050
- **Relative position:** 0.936591
- **Chapter/section:** Unavailable
- **Supplied context:** 639 characters (110 before; 515 after)

#### Passage

> Und was ist das, daß Albert dein Mann ist?  Mann!  Das wäre denn für
> diese Welt—und für diese Welt Sünde, daß ich dich liebe, daß ich
> dich aus seinen Armen in die meinigen reißen möchte?  Sünde?  Gut,
> und ich strafe mich dafür; ich habe sie in ihrer ganzen Himmelswonne
> geschmeckt, diese Sünde, habe Lebensbalsam und Kraft in mein Herz
> gesaugt.  Du bist von diesem Augenblicke mein!  Mein, o Lotte!  Ich
> gehe voran!  Gehe zu meinem Vater, zu deinem Vater.  Dem will ich's
> klagen, und er wird mich trösten, bis du kommst, und ich fliege dir
> entgegen und fasse dich und bleibe bei dir vor dem Angesichte des
> Unendlichen in ewigen Umarmungen.

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\gutenberg-2407-2408\annotations\goethe-die-leiden-des-jungen-werther-42853519d465\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The embedded clause “daß ich dich liebe” presents Werther's love for Lotte as an established fact while rhetorically disputing whether that love is sinful. It is therefore a strong truth-conditional avowal. The clause itself neither undertakes a relational commitment nor shows positive evidence of reflex-like verbal discharge; the surrounding intensity and fantasy do not independently establish P or E.
- **Ontology fit:** natural — T adequately captures the core avowal. The passage's transgression, possessiveness, emotional extremity, and death-oriented fantasy are contextual features rather than residual dimensions of the love utterance's core force.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "goethe-die-leiden-des-jungen-werther-42853519d465",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.95,
    "analysis": "The embedded clause “daß ich dich liebe” presents Werther's love for Lotte as an established fact while rhetorically disputing whether that love is sinful. It is therefore a strong truth-conditional avowal. The clause itself neither undertakes a relational commitment nor shows positive evidence of reflex-like verbal discharge; the surrounding intensity and fantasy do not independently establish P or E.",
    "ambiguity": "The surrounding claims of possession and eternal union have commitment-like implications, but these belong to the broader passage rather than to the core love clause."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "written",
    "description": "A written avowal addressed to Lotte, embedded in a rhetorical question in Werther's final letter; the hypothetical framing concerns whether loving her is sinful, not whether he loves her."
  },
  "contextual_interpretation": "Werther treats his love as undeniable despite Lotte's marriage to Albert. He names it a possible “sin,” associates it with wanting to take her from Albert, and folds it into possessive and eschatological fantasies of permanent union. The extremity of this final written address intensifies the avowal but does not convert its core force into a performative undertaking or an expressive/reflexive discharge.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“Das wäre denn für diese Welt—und für diese Welt Sünde, daß ich dich liebe”",
      "supports": "The rhetorical construction presupposes or emphatically asserts Werther's love while questioning its classification as worldly sin, strongly supporting T.",
      "confidence": 0.98
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "“daß ich dich aus seinen Armen in die meinigen reißen möchte”",
      "supports": "Connects the avowed love to desire for Lotte despite her marriage to Albert; this clarifies the transgressive context without changing the core clause into P.",
      "confidence": 0.97
    },
    {
      "evidence_id": "local-3",
      "source": "local_text",
      "quotation_or_description": "“Du bist von diesem Augenblicke mein! Mein, o Lotte! ... bleibe bei dir ... in ewigen Umarmungen.”",
      "supports": "Shows possessive, future-oriented, and highly emotional framing. These features explain the passage's intensity but do not supply independent evidence that “daß ich dich liebe” is itself performative or reflex-like.",
      "confidence": 0.95
    },
    {
      "evidence_id": "background-1",
      "source": "background_knowledge",
      "quotation_or_description": "In the wider novel, this passage belongs to Werther's final written address to Lotte in the period immediately preceding his suicide.",
      "supports": "Supports the written status and explains the passage's terminal, self-punitive, and imagined-eternal-union framing.",
      "confidence": 0.94
    },
    {
      "evidence_id": "metadata-1",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located at relative position 0.936591 in Goethe's Die Leiden des jungen Werther.",
      "supports": "Corroborates that the passage occurs near the novel's end, consistently with the final-letter context.",
      "confidence": 0.99
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.94,
    "contribution": "Identified the passage as part of Werther's final written address to Lotte before his suicide, helping determine utterance status and terminal narrative framing."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T adequately captures the core avowal. The passage's transgression, possessiveness, emotional extremity, and death-oriented fantasy are contextual features rather than residual dimensions of the love utterance's core force.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>
