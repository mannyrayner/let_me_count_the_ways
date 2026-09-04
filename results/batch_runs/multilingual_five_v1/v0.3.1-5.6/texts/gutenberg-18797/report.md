# Single-text pipeline report: La Princesse de Clèves

## Run summary

- **Run ID:** `gutenberg-18797`
- **Work:** *La Princesse de Clèves* by Madame de La Fayette
- **Source:** `gutenberg-18797`
- **Annotation:** v0.3.1 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 1
- **Valid occurrences:** 1
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.034432

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `lafayette-la-princesse-de-cleves-125bbc0f4d0e`

- **Exact match:** `je vous aime`
- **Pattern:** `fr_je_vous_aime` (v0.4)
- **Source offsets:** 265526–265538
- **Relative position:** 0.786846
- **Chapter/section:** Unavailable
- **Supplied context:** 900 characters (573 before; 315 after)

#### Passage

> --Je vous en fais pourtant, Madame, répliqua-t-il, et ils sont bien
> fondés: Pourquoi ne le pas voir s'il ne vous a rien dit? Mais, Madame,
> il vous a parlé; si son silence seul vous avait témoigné sa passion,
> elle n'aurait pas fait en vous une si grande impression. Vous n'avez pu
> me dire la vérité tout entière; vous m'en avez caché la plus grande
> partie; vous vous êtes repentie même du peu que vous m'avez avoué et
> vous n'avez pas eu la force de continuer. Je suis plus malheureux que je
> ne l'ai cru, et je suis le plus malheureux de tous les hommes. Vous êtes
> ma femme, je vous aime comme ma maîtresse, et je vous en vois aimer un
> autre. Cet autre est le plus aimable de la cour, et il vous voit tous
> les jours, il sait que vous l'aimez. Eh! j'ai pu croire, s'écria-t-il,
> que vous surmonteriez la passion que vous avez pour lui. Il faut que
> j'aie perdu la raison pour avoir cru qu'il fût possible.

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\gutenberg-18797\annotations\lafayette-la-princesse-de-cleves-125bbc0f4d0e\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The husband directly avows his romantic love for his wife: “je vous aime comme ma maîtresse.” Its principal force is truth-conditional, presenting his love as a fact that explains his jealousy and suffering. Although marriage frames the exchange, these words do not themselves undertake or renew a commitment. The emotional intensity remains part of an avowal rather than independently evidenced expressive/reflexive discharge.
- **Ontology fit:** natural — T naturally captures the core avowal. The surrounding jealousy, marital claim, and anguish are contextual features and do not require P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "lafayette-la-princesse-de-cleves-125bbc0f4d0e",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "The husband directly avows his romantic love for his wife: “je vous aime comme ma maîtresse.” Its principal force is truth-conditional, presenting his love as a fact that explains his jealousy and suffering. Although marriage frames the exchange, these words do not themselves undertake or renew a commitment. The emotional intensity remains part of an avowal rather than independently evidenced expressive/reflexive discharge.",
    "ambiguity": "The marital and accusatory setting gives the avowal relational weight, but there is insufficient evidence that the core utterance itself enacts an undertaking."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A husband directly addresses his wife during a jealous and anguished confrontation."
  },
  "contextual_interpretation": "The speaker contrasts his own romantic love for his wife with her love for another man: “Vous êtes ma femme, je vous aime comme ma maîtresse, et je vous en vois aimer un autre.” The avowal grounds his claim to be profoundly unhappy and intensifies his accusation. The phrase “comme ma maîtresse” distinguishes passionate or erotic love from merely formal marital attachment. His distress and the later “s'écria-t-il” establish emotional delivery, but they do not show that “je vous aime” functions as a reflex-like discharge rather than an emphatic assertion.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Vous êtes ma femme, je vous aime comme ma maîtresse”",
      "supports": "The speaker explicitly presents his romantic love for the addressee as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“et je vous en vois aimer un autre”",
      "supports": "The contrast between his love and her love for another makes the avowal part of a reasoned jealous complaint rather than an independent expressive discharge.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“Je suis plus malheureux que je ne l'ai cru, et je suis le plus malheureux de tous les hommes.”",
      "supports": "His avowed love functions as an explanation for his suffering and jealousy; the passage is emotionally intense, but intensity alone does not support E.",
      "confidence": 0.95
    },
    {
      "evidence_id": "e4",
      "source": "local_text",
      "quotation_or_description": "The passage identifies the addressee as “ma femme” immediately before the love avowal.",
      "supports": "Marriage supplies relational context, but the utterance does not explicitly promise, undertake, or renew an obligation, weighing against substantial P support.",
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
    "diagnosis": "T naturally captures the core avowal. The surrounding jealousy, marital claim, and anguish are contextual features and do not require P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>
