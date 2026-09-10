# Single-text pipeline report: Adolphe

## Run summary

- **Run ID:** `gutenberg-13861`
- **Work:** *Adolphe* by Benjamin Constant
- **Source:** `gutenberg-13861`
- **Annotation:** v0.3.1 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 1
- **Valid occurrences:** 1
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.047100

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `constant-adolphe-21bd511d198a`

- **Exact match:** `je vous aime`
- **Pattern:** `fr_je_vous_aime` (v0.6)
- **Source offsets:** 101753–101765
- **Relative position:** 0.578523
- **Chapter/section:** CHAPITRE VI
- **Supplied context:** 1508 characters (1000 before; 496 after)

#### Passage

> deux années de notre liaison ne s'effaceront
> pas de ma mémoire; elles seront à jamais l'époque la plus belle de
> ma vie. Mais l'amour, ce transport des sens, cette ivresse
> involontaire, cet oubli de tous les intérêts, de tous les devoirs,
> Ellénore, je ne l'ai plus». J'attendis longtemps sa réponse sans
> lever les yeux sur elle. Lorsque enfin je la regardai, elle était
> immobile; elle contemplait tous les objets comme si elle n'en eût
> reconnu aucun; je pris sa main: je la trouvai froide. Elle me
> repoussa. «Que me voulez-vous? me dit-elle; ne suis-je pas seule,
> seule dans l'univers, seule sans un être qui m'entende? Qu'avez-
> vous encore à me dire? ne m'avez-vous pas tout dit? Tout n'est-il
> pas fini, fini sans retour? Laissez-moi, quittez-moi; n'est-ce pas
> là ce que vous désirez?» Elle voulut s'éloigner, elle chancela;
> j'essayai de la retenir, elle tomba sans connaissance à mes pieds;
> je la relevai, je l'embrassai, je rappelai ses sens. «Ellénore,
> m'écriai-je, revenez à vous, revenez à moi; je vous aime d'amour,
> de l'amour le plus tendre, je vous avais trompée pour que vous
> fussiez plus libre dans votre choix». Crédulités du coeur, vous
> êtes inexplicables! Ces simples paroles, démenties par tant de
> paroles précédentes, rendirent Ellénore à la vie et à la
> confiance; elle me les fit répéter plusieurs fois: elle semblait
> respirer avec avidité. Elle me crut: elle s'enivra de son amour,
> qu'elle prenait pour le nôtre; elle confirma sa réponse au comte
> de P**, et je me vis plus engagé que jamais.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-13861\annotations\constant-adolphe-21bd511d198a\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** The highlighted phrase is centrally an avowal presenting Adolphe's loving state as true, even though the surrounding narration strongly indicates that the avowal is deceptive. Its use during an attempted relational repair gives it weak undertaking force, but reassurance and its consequential effect on Ellénore do not by themselves make it a strong commitment. Although introduced by “m'écriai-je” and uttered during a crisis, it is adequately represented as an urgent, emphatic assertion; there is no independent evidence that the words are a reflex-like discharge.
- **Ontology fit:** natural — T naturally captures the avowal's semantic force despite its likely falsity, while a low P score registers its limited role in renewing the relationship. Emotional urgency, deception, manipulation, and narrative irony are contextual qualifications rather than missing core-force categories. No residual aspect requires O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "constant-adolphe-21bd511d198a",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.92,
    "analysis": "The highlighted phrase is centrally an avowal presenting Adolphe's loving state as true, even though the surrounding narration strongly indicates that the avowal is deceptive. Its use during an attempted relational repair gives it weak undertaking force, but reassurance and its consequential effect on Ellénore do not by themselves make it a strong commitment. Although introduced by “m'écriai-je” and uttered during a crisis, it is adequately represented as an urgent, emphatic assertion; there is no independent evidence that the words are a reflex-like discharge.",
    "ambiguity": "There is limited uncertainty over P: the avowal helps restore the relationship and leaves Adolphe “plus engagé que jamais,” but the wording primarily asserts love rather than explicitly undertaking continued devotion. The crisis delivery could appear spontaneous, yet the text does not establish the independent expressive/reflexive force required for E."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Adolphe directly addresses Ellénore in quoted dialogue within his retrospective first-person narration: “je vous aime d'amour.”"
  },
  "contextual_interpretation": "Adolphe has just told Ellénore that he no longer possesses passionate love for her. After she collapses, he reverses himself and claims that his prior statement was a deception intended to free her choice. The retrospective narrator undercuts this reassurance: the new words are contradicted by his preceding declarations, Ellénore mistakes her own love for a mutual one, and Adolphe finds himself more deeply bound. Thus the utterance has full assertoric avowal form while being narratively framed as false, compassionate, panicked, and consequentially manipulative or self-entangling.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“je vous aime d'amour, de l'amour le plus tendre”",
      "supports": "The explicit declaration presents an intense loving emotional state as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "Immediately beforehand Adolphe says: “Mais l'amour ... Ellénore, je ne l'ai plus.”",
      "supports": "The direct contradiction strongly suggests that the later avowal is false or deceptive, while leaving its truth-conditional mode intact.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“je vous avais trompée pour que vous fussiez plus libre dans votre choix”",
      "supports": "Adolphe explicitly recasts his earlier renunciation as deception, making the present avowal an attempted reassurance and relational repair.",
      "confidence": 0.96
    },
    {
      "evidence_id": "e4",
      "source": "local_text",
      "quotation_or_description": "“Ces simples paroles, démenties par tant de paroles précédentes, rendirent Ellénore à la vie et à la confiance.”",
      "supports": "The narrator marks the declaration as contradicted by prior speech and records its restorative interpersonal effect; this supports deceptive T and weak P pressure rather than O.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e5",
      "source": "local_text",
      "quotation_or_description": "“elle s'enivra de son amour, qu'elle prenait pour le nôtre ... et je me vis plus engagé que jamais”",
      "supports": "Narrative irony denies genuine mutuality while showing that the declaration renews Ellénore's confidence and increases Adolphe's relational entanglement, providing limited support for P.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e6",
      "source": "local_text",
      "quotation_or_description": "The speech is introduced by “m'écriai-je” after Ellénore faints.",
      "supports": "This establishes urgent and emotional delivery, but without additional evidence it does not establish expressive/reflexive core force; E therefore remains zero.",
      "confidence": 0.95
    },
    {
      "evidence_id": "e7",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter VI of Benjamin Constant's French novel Adolphe.",
      "supports": "Identifies the passage as narrated literary dialogue and locates the classified event within the supplied source.",
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
    "diagnosis": "T naturally captures the avowal's semantic force despite its likely falsity, while a low P score registers its limited role in renewing the relationship. Emotional urgency, deception, manipulation, and narrative irony are contextual qualifications rather than missing core-force categories. No residual aspect requires O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The classification distinguishes the utterance's assertoric mode from its sincerity: a deceptive declaration can still receive maximal T support."
}
```

</details>
