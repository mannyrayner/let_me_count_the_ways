# Single-text pipeline report: Et dukkehjem

## Run summary

- **Run ID:** `runeberg-dukkhjem`
- **Work:** *Et dukkehjem* by Henrik Ibsen
- **Source:** `runeberg-dukkhjem`
- **Annotation:** v0.3.1 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 1
- **Valid occurrences:** 1
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.037044

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `ibsen-et-dukkehjem-365ac4ceb679`

- **Exact match:** `Jeg elsker deg`
- **Pattern:** `no_jeg_elsker_deg_dig_dere` (v0.4)
- **Source offsets:** 131502–131516
- **Relative position:** 0.960633
- **Chapter/section:** Unavailable
- **Supplied context:** 138 characters (114 before; 10 after)

#### Passage

> NORA. Å, det gjør meg så ondt, Torvald; for du har alltid
> vært så snill imot meg. Men jeg kan ikke gjøre ved det. Jeg elsker deg
> ikke mer.

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\runeberg-dukkhjem\annotations\ibsen-et-dukkehjem-365ac4ceb679\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The complete utterance is “Jeg elsker deg ikke mer” (“I no longer love you”), not the positive substring isolated by the pattern match. Nora directly presents the cessation of her love as true. Although this disclosure bears decisively on the marriage, the words themselves do not undertake a commitment, and nothing indicates that they function as a reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the utterance as a direct avowal that love has ceased. Its painful delivery and role in dissolving the relationship are contextual features adequately represented without adding P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "ibsen-et-dukkehjem-365ac4ceb679",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.97,
    "analysis": "The complete utterance is “Jeg elsker deg ikke mer” (“I no longer love you”), not the positive substring isolated by the pattern match. Nora directly presents the cessation of her love as true. Although this disclosure bears decisively on the marriage, the words themselves do not undertake a commitment, and nothing indicates that they function as a reflex-like expressive discharge.",
    "ambiguity": "The declaration helps effect a relational break in the wider scene, but that consequence does not by itself give the core utterance performative force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Nora directly addresses Torvald in dramatic dialogue and tells him that she no longer loves him."
  },
  "contextual_interpretation": "Nora prefaces the declaration with regret and acknowledges Torvald's kindness, then says she cannot help how she feels. This framing makes the utterance a painful, considered avowal of absent love rather than an emotional outburst. In the play's final confrontation, it contributes to her repudiation of their former marital understanding and impending departure, but those contextual consequences do not convert this sentence into an undertaking.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Jeg elsker deg ikke mer.”",
      "supports": "The negation and temporal modifier make the core proposition that Nora no longer loves Torvald, strongly supporting truth-conditional force.",
      "confidence": 1.0
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“Å, det gjør meg så ondt, Torvald; for du har alltid vært så snill imot meg. Men jeg kan ikke gjøre ved det.”",
      "supports": "Her regret, acknowledgment of his kindness, and claim that she cannot alter the situation frame the declaration as a considered report of her emotional state, not a reflex-like discharge.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e3",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is at relative position 0.960633 in Henrik Ibsen's Et dukkehjem.",
      "supports": "Its near-final location is consistent with the climactic marital confrontation, though the core classification is already clear from the local text.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e4",
      "source": "background_knowledge",
      "quotation_or_description": "In the final confrontation of A Doll's House, Nora reassesses her marriage and resolves to leave Torvald.",
      "supports": "The wider scene explains the declaration's grave relational consequences while distinguishing those consequences from performative force in the core sentence.",
      "confidence": 0.96
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.97,
    "contribution": "Knowledge of the play's final confrontation was used to interpret the declaration's relational stakes and its connection to Nora's departure, without treating those contextual effects as part of its core force."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T naturally captures the utterance as a direct avowal that love has ceased. Its painful delivery and role in dissolving the relationship are contextual features adequately represented without adding P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The extraction match “Jeg elsker deg” omits the immediately following negation “ikke mer”; classification therefore applies to the complete sentence."
}
```

</details>
