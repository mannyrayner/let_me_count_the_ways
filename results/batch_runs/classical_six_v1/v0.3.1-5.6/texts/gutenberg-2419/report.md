# Single-text pipeline report: La Dame aux camélias

## Run summary

- **Run ID:** `gutenberg-2419`
- **Work:** *La Dame aux camélias* by Alexandre Dumas fils
- **Source:** `gutenberg-2419`
- **Annotation:** v0.3.1 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 14
- **Valid occurrences:** 14
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.476200

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `dumas-fils-la-dame-aux-camelias-1843342a0444`

- **Exact match:** `je vous aime`
- **Pattern:** `fr_je_vous_aime` (v0.6)
- **Source offsets:** 128492–128504
- **Relative position:** 0.345471
- **Chapter/section:** CHAPITRE X
- **Supplied context:** 63 characters (50 before; 1 after)

#### Passage

> --C'est que personne ne vous a jamais aimée comme je vous aime.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-2419\annotations\dumas-fils-la-dame-aux-camelias-1843342a0444\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The speaker directly avows a present loving state and claims that its degree or manner exceeds anyone else's love for the addressee. The utterance may reassure or persuade, but it does not itself undertake a commitment, and nothing marks the words as a reflex-like affective discharge.
- **Ontology fit:** natural — T naturally captures the core force as an avowal of love. The comparative and persuasive coloring can be handled contextually without adding P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "dumas-fils-la-dame-aux-camelias-1843342a0444",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "The speaker directly avows a present loving state and claims that its degree or manner exceeds anyone else's love for the addressee. The utterance may reassure or persuade, but it does not itself undertake a commitment, and nothing marks the words as a reflex-like affective discharge.",
    "ambiguity": "The comparative claim may carry persuasive or courtship force in context, but that pragmatic purpose does not independently establish performative undertaking force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A direct spoken declaration within dialogue: « personne ne vous a jamais aimée comme je vous aime »."
  },
  "contextual_interpretation": "The speaker contrasts their own love with all prior love received by the addressee, presenting it as uniquely strong or distinctive. This intensifies the avowal and may function as reassurance or persuasion, but the supplied excerpt provides no evidence of a promise, relational undertaking, or reflexive verbal discharge.",
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "« C'est que personne ne vous a jamais aimée comme je vous aime. »",
      "supports": "The present-tense « je vous aime » explicitly presents the speaker's love as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "The comparative construction « personne ne vous a jamais aimée comme » frames the speaker's love as unmatched.",
      "supports": "This supports an emphatic and potentially persuasive avowal, but supplies no independent commitment or reflexive-discharge force.",
      "confidence": 0.96
    },
    {
      "evidence_id": "E3",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter X of Alexandre Dumas fils's La Dame aux camélias and is formatted as dialogue.",
      "supports": "Confirms that the classified event is represented as a direct character utterance rather than narration or reported speech.",
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
    "diagnosis": "T naturally captures the core force as an avowal of love. The comparative and persuasive coloring can be handled contextually without adding P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The highlighted phrase literally means “I love you”; the full sentence is approximately “It is because no one has ever loved you as I love you.”"
}
```

</details>

### 2. `dumas-fils-la-dame-aux-camelias-e073952cd29d`

- **Exact match:** `je vous aime`
- **Pattern:** `fr_je_vous_aime` (v0.6)
- **Source offsets:** 129914–129926
- **Relative position:** 0.349294
- **Chapter/section:** CHAPITRE X
- **Supplied context:** 60 characters (23 before; 25 after)

#### Passage

> --Si vous saviez comme je vous aime! lui disais-je tout bas.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-2419\annotations\dumas-fils-la-dame-aux-camelias-e073952cd29d\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The conditional-exclamative formula “Si vous saviez comme je vous aime!” strongly avows the speaker’s loving emotional state. It neither explicitly undertakes a commitment nor provides positive evidence that the words emerge as a reflex-like affective discharge. The exclamation and quiet delivery can be represented as contextual features of an emphatic avowal.
- **Ontology fit:** natural — T naturally captures the core avowal, while the intimate and emphatic manner is adequately handled as context. No important component of the utterance’s core force requires P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "dumas-fils-la-dame-aux-camelias-e073952cd29d",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.95,
    "analysis": "The conditional-exclamative formula “Si vous saviez comme je vous aime!” strongly avows the speaker’s loving emotional state. It neither explicitly undertakes a commitment nor provides positive evidence that the words emerge as a reflex-like affective discharge. The exclamation and quiet delivery can be represented as contextual features of an emphatic avowal.",
    "ambiguity": "The imperfect “disais-je” may present this as a repeated or habitual utterance rather than one uniquely bounded speech event, but this does not alter its dominant truth-conditional force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "quoted_or_revoiced",
    "description": "The narrator directly quotes his own earlier spoken words; the imperfect “disais-je” may indicate that he would say them repeatedly or habitually."
  },
  "contextual_interpretation": "The speaker tells the addressee, softly, that his love is greater than she realizes. The conditional framing intensifies the avowal by emphasizing the inadequacy of her knowledge, while “tout bas” describes intimate or subdued delivery. Neither feature independently establishes performative commitment or expressive/reflexive force.",
  "evidence": [
    {
      "evidence_id": "ev1",
      "source": "local_text",
      "quotation_or_description": "“Si vous saviez comme je vous aime!”",
      "supports": "The explicit first-person present-tense love predication, intensified by “comme,” strongly supports truth-conditional avowal.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev2",
      "source": "local_text",
      "quotation_or_description": "“lui disais-je tout bas”",
      "supports": "Identifies the words as the narrator’s quoted earlier speech and characterizes their delivery as quiet; it does not show a commitment or reflex-like production.",
      "confidence": 0.97
    },
    {
      "evidence_id": "ev3",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter X of Alexandre Dumas fils’s La Dame aux camélias.",
      "supports": "Confirms the literary and bibliographic setting of the narrated quotation.",
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
    "diagnosis": "T naturally captures the core avowal, while the intimate and emphatic manner is adequately handled as context. No important component of the utterance’s core force requires P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 3. `dumas-fils-la-dame-aux-camelias-586fc1b17220`

- **Exact match:** `je t'aime`
- **Pattern:** `fr_je_taime_apostrophe_spacing` (v0.6)
- **Source offsets:** 174735–174744
- **Relative position:** 0.469802
- **Chapter/section:** CHAPITRE XIII
- **Supplied context:** 74 characters (46 before; 19 after)

#### Passage

> --Non, il faut seulement que tu m'aimes comme je t'aime, et tout
> réussira.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-2419\annotations\dumas-fils-la-dame-aux-camelias-586fc1b17220\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The highlighted « je t'aime » presents the speaker's love as a true emotional state and uses it as the standard for the reciprocal love being requested. It does not independently undertake a commitment, and there is no evidence that the words are a reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the core force as an avowal of a loving state. The reciprocal appeal and optimistic framing are contextual functions adequately described without adding P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "dumas-fils-la-dame-aux-camelias-586fc1b17220",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.97,
    "analysis": "The highlighted « je t'aime » presents the speaker's love as a true emotional state and uses it as the standard for the reciprocal love being requested. It does not independently undertake a commitment, and there is no evidence that the words are a reflex-like expressive discharge.",
    "ambiguity": "The broader sentence appeals for a reciprocal relationship, but that interpersonal appeal does not give the embedded « je t'aime » clear undertaking force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A direct spoken love avowal embedded in the comparative clause « comme je t'aime » within dialogue."
  },
  "contextual_interpretation": "The speaker says that success requires the addressee to love the speaker in the same way that the speaker loves the addressee. Thus « je t'aime » primarily avows an existing state and supplies the benchmark for a request for reciprocity. The hopeful claim « et tout réussira » frames the appeal but does not convert the highlighted clause into a commitment or expressive discharge.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "« il faut seulement que tu m'aimes comme je t'aime »",
      "supports": "The highlighted clause explicitly presents the speaker as loving the addressee and makes that state the standard for desired reciprocity, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "« et tout réussira »",
      "supports": "The utterance is part of a reasoned, future-oriented appeal about what will make matters succeed, with no positive evidence of reflex-like expressive production.",
      "confidence": 0.94
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "The line begins with a dialogue dash and contains the first-person present « je t'aime ».",
      "supports": "This supports classifying the event as a direct spoken avowal rather than reported or imagined speech.",
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
    "diagnosis": "T naturally captures the core force as an avowal of a loving state. The reciprocal appeal and optimistic framing are contextual functions adequately described without adding P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 4. `dumas-fils-la-dame-aux-camelias-8367dce9eb16`

- **Exact match:** `je vous aime`
- **Pattern:** `fr_je_vous_aime` (v0.6)
- **Source offsets:** 176246–176258
- **Relative position:** 0.473865
- **Chapter/section:** CHAPITRE XIII
- **Supplied context:** 235 characters (31 before; 192 after)

#### Passage

> --Que voulez-vous, Marguerite, je vous aime trop, et je suis jaloux de
> la moindre de vos pensées. Ce que vous m'avez proposé tout à l'heure me
> rendrait fou de joie, mais le mystère qui précède l'exécution de ce
> projet me serre le cœur.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-2419\annotations\dumas-fils-la-dame-aux-camelias-8367dce9eb16\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** “Je vous aime trop” directly avows an excessive degree of love and presents that emotional state as the explanation for the speaker’s jealousy and distress. It does not independently undertake a commitment, and nothing indicates that the words are a reflex-like expressive discharge rather than an emotionally charged assertion.
- **Ontology fit:** natural — T naturally captures the core force as an avowal of love used to explain jealousy and anguish. The emotional context requires no separate E score, and there is no residual core force requiring O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "dumas-fils-la-dame-aux-camelias-8367dce9eb16",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.97,
    "analysis": "“Je vous aime trop” directly avows an excessive degree of love and presents that emotional state as the explanation for the speaker’s jealousy and distress. It does not independently undertake a commitment, and nothing indicates that the words are a reflex-like expressive discharge rather than an emotionally charged assertion.",
    "ambiguity": null
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A speaker directly addresses Marguerite and tells her, “je vous aime trop.”"
  },
  "contextual_interpretation": "The avowal is embedded in an explanation of jealousy: because the speaker loves Marguerite “too much,” even her thoughts provoke jealousy, while the secrecy surrounding her proposed plan causes emotional pain. The utterance is therefore chiefly a causal self-description, however intense its surrounding emotion, rather than a promise or reflexive outburst.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Marguerite, je vous aime trop”",
      "supports": "The first-person present-tense declaration, intensified by “trop,” strongly supports truth-conditional avowal of a loving emotional state.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“et je suis jaloux de la moindre de vos pensées”",
      "supports": "The coordination presents love and jealousy as asserted psychological states and makes the love avowal explanatory rather than performative.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“le mystère qui précède l'exécution de ce projet me serre le cœur”",
      "supports": "The speaker describes emotional distress caused by the situation, but this intensity does not independently establish expressive/reflexive force.",
      "confidence": 0.94
    },
    {
      "evidence_id": "e4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XIII of Alexandre Dumas fils’s La Dame aux camélias.",
      "supports": "Identifies the bibliographic and narrative location of the directly spoken occurrence.",
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
    "diagnosis": "T naturally captures the core force as an avowal of love used to explain jealousy and anguish. The emotional context requires no separate E score, and there is no residual core force requiring O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 5. `dumas-fils-la-dame-aux-camelias-1aa634efc234`

- **Exact match:** `je vous aime`
- **Pattern:** `fr_je_vous_aime` (v0.6)
- **Source offsets:** 177268–177280
- **Relative position:** 0.476613
- **Chapter/section:** CHAPITRE XIII
- **Supplied context:** 884 characters (816 before; 56 after)

#### Passage

> --Voyons, raisonnons un peu, reprit-elle en me prenant les deux mains et
> en me regardant avec un charmant sourire auquel il m'était impossible de
> résister; vous m'aimez, n'est-ce pas? et vous seriez heureux de passer
> trois ou quatre mois à la campagne avec moi seule; moi aussi, je serais
> heureuse de cette solitude à deux, non seulement j'en serais heureuse,
> mais j'en ai besoin pour ma santé. Je ne puis quitter Paris pour un si
> long temps sans mettre ordre à mes affaires, et les affaires d'une femme
> comme moi sont toujours très embrouillées; eh bien, j'ai trouvé le moyen
> de tout concilier, mes affaires et mon amour pour vous, oui, pour vous,
> ne riez pas, j'ai la folie de vous aimer! Et voilà que vous prenez vos
> grands airs et me dites des grands mots. Enfant, trois fois enfant,
> rappelez-vous seulement que je vous aime, et ne vous inquiétez de
> rien.--Est-ce convenu, voyons?

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-2419\annotations\dumas-fils-la-dame-aux-camelias-1aa634efc234\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The embedded proposition “je vous aime” is presented as a fact about the speaker’s continuing emotional state and as something the addressee should remember. It reassures and helps persuade him to accept her proposed arrangement, but it does not itself undertake a commitment. Despite the surrounding emotional language, there is no positive evidence that the words are a reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the core avowal. Its persuasive and reassuring use belongs to context and does not require P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "dumas-fils-la-dame-aux-camelias-1aa634efc234",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.95,
    "analysis": "The embedded proposition “je vous aime” is presented as a fact about the speaker’s continuing emotional state and as something the addressee should remember. It reassures and helps persuade him to accept her proposed arrangement, but it does not itself undertake a commitment. Despite the surrounding emotional language, there is no positive evidence that the words are a reflex-like expressive discharge.",
    "ambiguity": "The declaration has relational and persuasive consequences, but these do not provide substantial independent support for performative undertaking force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A love avowal spoken directly by the woman to the narrator, syntactically embedded in the imperative “rappelez-vous seulement que je vous aime.”"
  },
  "contextual_interpretation": "The speaker is reasoning with and reassuring her interlocutor while proposing that they spend several months together in the country. She repeatedly presents her love as genuine—“mon amour pour vous” and “j'ai la folie de vous aimer”—and asks him to rely on it rather than worry. This makes the target primarily a deliberate avowal used persuasively, not an independently reflexive outburst or a commitment enacted by the words themselves.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“rappelez-vous seulement que je vous aime, et ne vous inquiétez de rien”",
      "supports": "The complement “je vous aime” presents her continuing love as true and supplies reassurance, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "“j'ai trouvé le moyen de tout concilier, mes affaires et mon amour pour vous”",
      "supports": "She explicitly treats her love as an existing emotional state within a reasoned explanation, reinforcing T rather than reflexive E.",
      "confidence": 0.97
    },
    {
      "evidence_id": "local-3",
      "source": "local_text",
      "quotation_or_description": "“oui, pour vous, ne riez pas, j'ai la folie de vous aimer!”",
      "supports": "The nearby emphatic avowal corroborates the claimed loving state, but its intensity alone does not establish expressive/reflexive core force for the target occurrence.",
      "confidence": 0.94
    },
    {
      "evidence_id": "local-4",
      "source": "local_text",
      "quotation_or_description": "“Voyons, raisonnons un peu” and “Est-ce convenu, voyons?” frame the speech as reasoned persuasion toward agreement.",
      "supports": "The calculated argumentative framing weighs against treating the target as a reflex-like discharge; the requested agreement concerns the proposed country stay rather than a commitment enacted by “je vous aime.”",
      "confidence": 0.95
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
    "diagnosis": "T naturally captures the core avowal. Its persuasive and reassuring use belongs to context and does not require P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The exclamation in the preceding “j'ai la folie de vous aimer!” does not transfer expressive/reflexive force to the separately highlighted embedded occurrence."
}
```

</details>

### 6. `dumas-fils-la-dame-aux-camelias-dbb35581cef3`

- **Exact match:** `Je vous / aime`
- **Pattern:** `fr_je_vous_aime` (v0.6)
- **Source offsets:** 179365–179377
- **Relative position:** 0.482251
- **Chapter/section:** CHAPITRE XIII
- **Supplied context:** 213 characters (199 before; 2 after)

#### Passage

> «Cher enfant, je suis un peu souffrante, et le médecin m'ordonne le
> repos. Je me coucherai de bonne heure ce soir et ne vous verrai pas.
> Mais, pour vous récompenser, je vous attendrai demain à midi. Je vous
> aime.»

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-2419\annotations\dumas-fils-la-dame-aux-camelias-dbb35581cef3\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** “Je vous aime” is principally a written avowal presenting the writer’s love as true. It also reassures the addressee after she cancels that evening’s meeting, but the core words do not independently undertake a commitment, and there is no evidence that they are a reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the core written avowal. Its reassuring placement and composed delivery are contextual features adequately described without adding P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "dumas-fils-la-dame-aux-camelias-dbb35581cef3",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.94,
    "analysis": "“Je vous aime” is principally a written avowal presenting the writer’s love as true. It also reassures the addressee after she cancels that evening’s meeting, but the core words do not independently undertake a commitment, and there is no evidence that they are a reflex-like expressive discharge.",
    "ambiguity": "The message may have a strategic or compensatory purpose, but the excerpt does not establish insincerity; in any case, sincerity is orthogonal to its truth-conditional mode."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "written",
    "description": "A written message or note is quoted within the narration; the classified event is the writer’s closing sentence, “Je vous aime.”"
  },
  "contextual_interpretation": "The avowal closes an affectionate message explaining that illness and medical orders prevent a meeting that evening, while promising a meeting the next day. Its placement after “pour vous récompenser” gives it a reassuring, possibly compensatory interpersonal role, but that contextual function does not turn the core sentence into a commitment or an expressive reflex.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Je vous aime.”",
      "supports": "The unqualified declarative directly presents the writer’s loving state as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“Cher enfant, je suis un peu souffrante, et le médecin m'ordonne le repos.”",
      "supports": "The affectionate address and explanatory prose frame the avowal as part of a composed personal message rather than a reflex-like verbal discharge.",
      "confidence": 0.94
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“Mais, pour vous récompenser, je vous attendrai demain à midi. Je vous aime.”",
      "supports": "The avowal follows cancellation and rescheduling, giving it a reassuring or compensatory contextual role; the explicit future undertaking belongs to the preceding sentence rather than to the core love utterance.",
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
    "diagnosis": "T naturally captures the core written avowal. Its reassuring placement and composed delivery are contextual features adequately described without adding P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 7. `dumas-fils-la-dame-aux-camelias-73b38acbba68`

- **Exact match:** `je vous aime`
- **Pattern:** `fr_je_vous_aime` (v0.6)
- **Source offsets:** 200574–200586
- **Relative position:** 0.539275
- **Chapter/section:** CHAPITRE XV
- **Supplied context:** 114 characters (88 before; 14 after)

#### Passage

> --C'est juste, dis-je en laissant tomber ma tête sur les genoux de
> Marguerite; mais moi je vous aime comme un fou.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-2419\annotations\dumas-fils-la-dame-aux-camelias-73b38acbba68\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The speaker directly avows his intense love for Marguerite. “Comme un fou” amplifies the asserted emotional state but supplies no independent evidence that the words are a reflex-like expressive discharge, and the utterance does not itself undertake a commitment.
- **Ontology fit:** natural — T naturally captures the core force as an emphatic avowal of love. The passion, bodily posture, and intensifier are adequately treated as contextual features without adding E, P, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "dumas-fils-la-dame-aux-camelias-73b38acbba68",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.95,
    "analysis": "The speaker directly avows his intense love for Marguerite. “Comme un fou” amplifies the asserted emotional state but supplies no independent evidence that the words are a reflex-like expressive discharge, and the utterance does not itself undertake a commitment.",
    "ambiguity": null
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A direct spoken declaration by the first-person narrator to Marguerite, represented in narrated dialogue."
  },
  "contextual_interpretation": "The adversative framing—“mais moi”—presents the declaration as a personal counterpoint to Marguerite’s preceding position. Resting his head on her knees and saying that he loves her “like a madman” convey vulnerability and passionate intensity, but these contextual features reinforce an avowal rather than independently establishing performative or expressive/reflexive force.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "« mais moi je vous aime comme un fou »",
      "supports": "The first-person present-tense declaration explicitly presents the speaker’s intense loving state as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "« dis-je en laissant tomber ma tête sur les genoux de Marguerite »",
      "supports": "The speech tag establishes a direct spoken event addressed to Marguerite; the accompanying posture adds emotional context but does not by itself establish E or P.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "« C'est juste [...] mais moi »",
      "supports": "The concessive-adversative construction frames the love declaration as the speaker’s personal counterclaim, consistent with an emphatic avowal.",
      "confidence": 0.94
    },
    {
      "evidence_id": "e4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified in Chapter XV of Alexandre Dumas fils’s La Dame aux camélias, at source position 200574–200586.",
      "supports": "Confirms the bibliographic and narrative-dialogue location of the classified occurrence.",
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
    "diagnosis": "T naturally captures the core force as an emphatic avowal of love. The passion, bodily posture, and intensifier are adequately treated as contextual features without adding E, P, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 8. `dumas-fils-la-dame-aux-camelias-a7a1b4e98b66`

- **Exact match:** `je t'aime`
- **Pattern:** `fr_je_taime_apostrophe_spacing` (v0.6)
- **Source offsets:** 234484–234493
- **Relative position:** 0.630447
- **Chapter/section:** CHAPITRE XVII
- **Supplied context:** 311 characters (11 before; 291 after)

#### Passage

> --Oh! oui, je t'aime, mon Armand! murmura-t-elle en enlaçant ses deux
> bras autour de mon cou, je t'aime comme je n'aurais pas cru pouvoir
> aimer. Nous serons heureux, nous vivrons tranquilles, et je dirai un
> éternel adieu à cette vie dont je rougis maintenant. Jamais tu ne me
> reprocheras le passé, n'est-ce pas?

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-2419\annotations\dumas-fils-la-dame-aux-camelias-a7a1b4e98b66\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 2 / 0 / 0
- **Core analysis:** Marguerite's “je t'aime” is principally a direct avowal presenting her love for Armand as true. Its repetition and elaboration (“comme je n'aurais pas cru pouvoir aimer”) strongly reinforce T. The surrounding declarations about their future and her abandonment of her former life give the avowal some relationally undertaking force, but much of that commitment is expressed by the following sentences rather than by “je t'aime” alone. “Oh!”, murmuring, repetition, and the embrace indicate emotional intensity but do not independently establish reflex-like expressive force.
- **Ontology fit:** natural — T naturally captures the avowal, while P captures its limited participation in a commitment-laden relational exchange. Emotional delivery can remain contextual because the passage gives no independent evidence for E, and no residual core force requires O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "dumas-fils-la-dame-aux-camelias-a7a1b4e98b66",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 2,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.92,
    "analysis": "Marguerite's “je t'aime” is principally a direct avowal presenting her love for Armand as true. Its repetition and elaboration (“comme je n'aurais pas cru pouvoir aimer”) strongly reinforce T. The surrounding declarations about their future and her abandonment of her former life give the avowal some relationally undertaking force, but much of that commitment is expressed by the following sentences rather than by “je t'aime” alone. “Oh!”, murmuring, repetition, and the embrace indicate emotional intensity but do not independently establish reflex-like expressive force.",
    "ambiguity": "The main uncertainty is the degree of P: the utterance participates in a commitment-laden declaration of a shared future, although the explicit undertakings occur chiefly after the core words."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A spoken utterance by Marguerite to Armand, represented as direct dialogue within Armand's first-person narration."
  },
  "contextual_interpretation": "Marguerite emphatically affirms and elaborates her love while embracing Armand. She immediately projects a happy, tranquil life with him, promises a permanent break with a life of which she is now ashamed, and seeks reassurance that he will not reproach her past. This makes the avowal emotionally intense and embeds it in a prospective relational commitment, without showing that the words themselves are an involuntary or reflex-like discharge.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Oh! oui, je t'aime, mon Armand!”",
      "supports": "The explicit first-person avowal strongly supports T; the affirmative framing and direct address identify Armand as its addressee.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“je t'aime comme je n'aurais pas cru pouvoir aimer”",
      "supports": "The repeated and comparative elaboration presents an unusually strong loving state as true, reinforcing T rather than independently establishing E.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“murmura-t-elle en enlaçant ses deux bras autour de mon cou”",
      "supports": "The murmured delivery and embrace establish affectionate intensity and intimacy, but supply no clear evidence that producing the words is reflex-like.",
      "confidence": 0.95
    },
    {
      "evidence_id": "e4",
      "source": "local_text",
      "quotation_or_description": "“Nous serons heureux, nous vivrons tranquilles, et je dirai un éternel adieu à cette vie”",
      "supports": "The projected shared future and promised change of life provide moderate contextual support for performative or undertaking force.",
      "confidence": 0.93
    },
    {
      "evidence_id": "e5",
      "source": "local_text",
      "quotation_or_description": "“Jamais tu ne me reprocheras le passé, n'est-ce pas?”",
      "supports": "Her request for reassurance connects the avowal to expectations governing their relationship, while also showing that the commitment is negotiated in the surrounding speech.",
      "confidence": 0.91
    },
    {
      "evidence_id": "e6",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XVII of Alexandre Dumas fils's La Dame aux camélias, at source offsets 234484–234493.",
      "supports": "Identifies the classified occurrence and its supplied textual location.",
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
    "diagnosis": "T naturally captures the avowal, while P captures its limited participation in a commitment-laden relational exchange. Emotional delivery can remain contextual because the passage gives no independent evidence for E, and no residual core force requires O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 9. `dumas-fils-la-dame-aux-camelias-d74dd7d57c75`

- **Exact match:** `je t'aime`
- **Pattern:** `fr_je_taime_apostrophe_spacing` (v0.6)
- **Source offsets:** 234567–234576
- **Relative position:** 0.630670
- **Chapter/section:** CHAPITRE XVII
- **Supplied context:** 311 characters (94 before; 208 after)

#### Passage

> --Oh! oui, je t'aime, mon Armand! murmura-t-elle en enlaçant ses deux
> bras autour de mon cou, je t'aime comme je n'aurais pas cru pouvoir
> aimer. Nous serons heureux, nous vivrons tranquilles, et je dirai un
> éternel adieu à cette vie dont je rougis maintenant. Jamais tu ne me
> reprocheras le passé, n'est-ce pas?

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-2419\annotations\dumas-fils-la-dame-aux-camelias-d74dd7d57c75\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 2 / 0 / 0
- **Core analysis:** Marguerite directly and emphatically avows that she loves Armand. The repetition and comparison with what she had thought possible strongly present her love as a true emotional state. The surrounding promises to pursue a shared life and renounce her former way of living give the avowal some commitment-enacting force, though the words “je t’aime” remain primarily truth-conditional. The murmur, embrace, exclamation, and repetition indicate emotional intensity but do not independently establish reflex-like expressive force.
- **Ontology fit:** natural — T naturally captures the avowal, while P captures the commitment pressure supplied by the tightly connected promises. Delivery and intensity can remain contextual because there is no positive evidence for reflexive E, and no important aspect of core force falls outside T/P/E.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "dumas-fils-la-dame-aux-camelias-d74dd7d57c75",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 2,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.94,
    "analysis": "Marguerite directly and emphatically avows that she loves Armand. The repetition and comparison with what she had thought possible strongly present her love as a true emotional state. The surrounding promises to pursue a shared life and renounce her former way of living give the avowal some commitment-enacting force, though the words “je t’aime” remain primarily truth-conditional. The murmur, embrace, exclamation, and repetition indicate emotional intensity but do not independently establish reflex-like expressive force.",
    "ambiguity": "The principal uncertainty is how much of the explicit future-oriented commitment in the immediately following sentences should be attributed to the core love utterance itself; this supports moderate rather than dominant P."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "The matched first “je t’aime” is represented as Marguerite’s direct spoken reply to Armand within narrated dialogue; it is followed shortly by a repetition of the same avowal."
  },
  "contextual_interpretation": "Marguerite answers affirmatively, names Armand, embraces him, and repeats that she loves him beyond what she had believed herself capable of feeling. She then projects their happiness and quiet life together, promises to leave behind a life of which she is now ashamed, and seeks reassurance that Armand will not reproach her past. This frames the avowal as sincere-seeming emotional disclosure joined to a prospective relational undertaking. Nothing in the supplied passage establishes expressive/reflexive production rather than an emotionally intense avowal.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“Oh! oui, je t’aime, mon Armand!”",
      "supports": "The affirmative response and direct address strongly support a truth-conditional avowal of love.",
      "confidence": 0.99
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "“je t’aime comme je n’aurais pas cru pouvoir aimer”",
      "supports": "The repetition and explicit comparison present the depth of her loving state as true, reinforcing T.",
      "confidence": 0.98
    },
    {
      "evidence_id": "local-3",
      "source": "local_text",
      "quotation_or_description": "“Nous serons heureux, nous vivrons tranquilles, et je dirai un éternel adieu à cette vie”",
      "supports": "The projected shared future and promise to abandon her former life provide independent contextual support for commitment or relational-undertaking force, hence moderate P.",
      "confidence": 0.95
    },
    {
      "evidence_id": "local-4",
      "source": "local_text",
      "quotation_or_description": "She murmurs the words while putting both arms around Armand’s neck.",
      "supports": "This establishes intimate and affectively intense delivery, but supplies no clear evidence that the words are a reflex-like expressive discharge; it therefore does not warrant E above zero.",
      "confidence": 0.96
    },
    {
      "evidence_id": "metadata-1",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XVII of Alexandre Dumas fils’s La Dame aux camélias, in the supplied Project Gutenberg source.",
      "supports": "Identifies the represented dialogue event and its bibliographic location without adding substantive force beyond the local passage.",
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
    "diagnosis": "T naturally captures the avowal, while P captures the commitment pressure supplied by the tightly connected promises. Delivery and intensity can remain contextual because there is no positive evidence for reflexive E, and no important aspect of core force falls outside T/P/E.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The classification targets the first matched “je t’aime”; the immediate repetition is used as local evidence for its force."
}
```

</details>

### 10. `dumas-fils-la-dame-aux-camelias-697fbf6647d5`

- **Exact match:** `je t'aime`
- **Pattern:** `fr_je_taime_apostrophe_spacing` (v0.6)
- **Source offsets:** 241276–241285
- **Relative position:** 0.648708
- **Chapter/section:** CHAPITRE XVIII
- **Supplied context:** 45 characters (35 before; 1 after)

#### Passage

> --C'est que tu ne sais pas combien je t'aime!

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-2419\annotations\dumas-fils-la-dame-aux-camelias-697fbf6647d5\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The speaker directly avows the magnitude of a present loving state: “you do not know how much I love you.” The utterance contains no explicit relational undertaking or commitment. Its exclamation mark and emphatic scalar construction indicate intensity but do not independently establish expressive/reflexive force.
- **Ontology fit:** natural — T naturally captures the core avowal. Emotional emphasis can be recorded contextually without adding E, while no undertaking supports P and no residual core force requires O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "dumas-fils-la-dame-aux-camelias-697fbf6647d5",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.94,
    "analysis": "The speaker directly avows the magnitude of a present loving state: “you do not know how much I love you.” The utterance contains no explicit relational undertaking or commitment. Its exclamation mark and emphatic scalar construction indicate intensity but do not independently establish expressive/reflexive force.",
    "ambiguity": "The narrow extract does not identify the interlocutors or immediate motive, so reassurance, protest, or persuasion may be contextually involved; none changes the dominant truth-conditional force established by the wording."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly presented line of dialogue in which the speaker tells the addressee how strongly the speaker loves them."
  },
  "contextual_interpretation": "“C’est que tu ne sais pas combien…” frames the avowal as an explanation or corrective: the addressee allegedly fails to appreciate the depth of the speaker’s love. This gives the declaration emphatic and potentially persuasive force, but the supplied passage provides no evidence of a commitment-enacting act or of reflex-like verbal discharge.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“C'est que tu ne sais pas combien je t'aime!”",
      "supports": "The first-person present-tense clause explicitly presents the speaker’s love, and its degree, as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "The degree construction “combien” and the exclamation mark intensify the avowal.",
      "supports": "These features support emphatic emotional delivery, but without additional evidence they do not establish independent E force or a P-type undertaking.",
      "confidence": 0.96
    },
    {
      "evidence_id": "metadata-1",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XVIII of Alexandre Dumas fils’s La Dame aux camélias and is presented with a dialogue dash.",
      "supports": "This supports treating the occurrence as direct fictional dialogue rather than narration, report, or writing.",
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
    "diagnosis": "T naturally captures the core avowal. Emotional emphasis can be recorded contextually without adding E, while no undertaking supports P and no residual core force requires O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 11. `dumas-fils-la-dame-aux-camelias-d8ce633d2a17`

- **Exact match:** `je t'aime`
- **Pattern:** `fr_je_taime_apostrophe_spacing` (v0.6)
- **Source offsets:** 273220–273229
- **Relative position:** 0.734595
- **Chapter/section:** CHAPITRE XXI
- **Supplied context:** 608 characters (493 before; 106 after)

#### Passage

> --Ah! mon dieu! je m'en doutais, dit-elle. Quand Joseph est venu nous
> annoncer l'arrivée de ton père, j'ai tressailli comme à la nouvelle d'un
> malheur. Pauvre ami! et c'est moi qui te cause tous ces chagrins. Tu
> ferais peut-être mieux de me quitter que de te brouiller avec ton père.
> Cependant je ne lui ai rien fait. Nous vivons bien tranquilles, nous
> allons vivre plus tranquilles encore. Il sait bien qu'il faut que tu
> aies une maîtresse, et il devrait être heureux que ce fût moi, puisque
> je t'aime et n'ambitionne pas plus que ta position ne le permet. Lui
> as-tu dit comment nous avons arrangé l'avenir?

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-2419\annotations\dumas-fils-la-dame-aux-camelias-d8ce633d2a17\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The causal clause « puisque je t'aime » presents the speaker's love as an established emotional state explaining why the father should accept their relationship. It is primarily a truth-conditional avowal. The surrounding discussion of sacrifice and their future does not turn these particular words into an undertaking, and there is no positive evidence that they are a reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the core avowal, while the argumentative, reassuring, and relationship-specific nuances can remain contextual. No important core force requires E, P, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "dumas-fils-la-dame-aux-camelias-d8ce633d2a17",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.97,
    "analysis": "The causal clause « puisque je t'aime » presents the speaker's love as an established emotional state explaining why the father should accept their relationship. It is primarily a truth-conditional avowal. The surrounding discussion of sacrifice and their future does not turn these particular words into an undertaking, and there is no positive evidence that they are a reflex-like expressive discharge.",
    "ambiguity": "The utterance offers relational reassurance in context, but reassurance alone does not establish performative commitment."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "The speaker directly tells her interlocutor « je t'aime » within a longer spoken explanation, embedding the avowal in a causal clause introduced by « puisque »."
  },
  "contextual_interpretation": "The speaker responds anxiously to the arrival of her lover's father, blames herself for the conflict, and even suggests that her lover might leave her rather than quarrel with him. She then defends their quiet relationship and cites her love, together with her limited ambitions, as reasons the father should approve. Thus the avowal also reassures her lover and supports an argument, but its core force remains the presentation of her love as true rather than a new promise or affective reflex.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "« puisque je t'aime et n'ambitionne pas plus que ta position ne le permet »",
      "supports": "The causal construction presents love as an existing fact that helps justify the speaker's claim, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "« Tu ferais peut-être mieux de me quitter que de te brouiller avec ton père. »",
      "supports": "The surrounding concern is conflict with the lover's father and possible separation; this makes the avowal reassuring but does not supply an undertaking in the core words.",
      "confidence": 0.96
    },
    {
      "evidence_id": "local-3",
      "source": "local_text",
      "quotation_or_description": "« Lui as-tu dit comment nous avons arrangé l'avenir? »",
      "supports": "A shared future has been arranged, but it is discussed separately from « je t'aime »; this weighs against treating the core utterance itself as performative.",
      "confidence": 0.94
    },
    {
      "evidence_id": "metadata-1",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is in Chapter XXI of Alexandre Dumas fils's La Dame aux camélias and is identified as a French « je t'aime » match.",
      "supports": "Confirms the textual location and that the classified expression is the supplied direct love utterance.",
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
    "diagnosis": "T naturally captures the core avowal, while the argumentative, reassuring, and relationship-specific nuances can remain contextual. No important core force requires E, P, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 12. `dumas-fils-la-dame-aux-camelias-00342a2512df`

- **Exact match:** `je t'aime`
- **Pattern:** `fr_je_taime_apostrophe_spacing` (v0.6)
- **Source offsets:** 273878–273887
- **Relative position:** 0.736364
- **Chapter/section:** CHAPITRE XXI
- **Supplied context:** 29 characters (19 before; 1 after)

#### Passage

> --Tu sais bien que je t'aime.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-2419\annotations\dumas-fils-la-dame-aux-camelias-00342a2512df\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The speaker directly avows an existing state of love and presents it as something the addressee already knows. Nothing in the supplied text indicates that the words institute a commitment or function as a reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the avowal of an existing loving state. Any reassuring or persuasive conversational role is contextual and does not require P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "dumas-fils-la-dame-aux-camelias-00342a2512df",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.93,
    "analysis": "The speaker directly avows an existing state of love and presents it as something the addressee already knows. Nothing in the supplied text indicates that the words institute a commitment or function as a reflex-like expressive discharge.",
    "ambiguity": "The very short extract leaves the wider conversational purpose—such as reassurance, persuasion, or self-defence—undetermined, but this does not materially alter the dominant truth-conditional force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly spoken line of dialogue addressed to the beloved: «Tu sais bien que je t'aime.»"
  },
  "contextual_interpretation": "The framing «Tu sais bien que» (“You know very well that”) treats the speaker's love as an established fact shared with the addressee. It may pragmatically reassure or answer a doubt, but the excerpt supplies no independent evidence of an undertaking or expressive/reflexive discharge.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "«Tu sais bien que je t'aime.»",
      "supports": "The complement «je t'aime» is presented as true, while «Tu sais bien que» frames that love as already known to the addressee; this strongly supports T.",
      "confidence": 0.98
    },
    {
      "evidence_id": "metadata-1",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in direct dialogue in Chapter XXI of Alexandre Dumas fils's La Dame aux camélias.",
      "supports": "Supports identifying the event as a direct fictional utterance rather than a report, imagined statement, or written message.",
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
    "diagnosis": "T naturally captures the avowal of an existing loving state. Any reassuring or persuasive conversational role is contextual and does not require P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "Classification is intentionally based only on the supplied sentence and metadata; no identification of the speaker or addressee is inferred."
}
```

</details>

### 13. `dumas-fils-la-dame-aux-camelias-85963bb66685`

- **Exact match:** `je vous aime`
- **Pattern:** `fr_je_vous_aime` (v0.6)
- **Source offsets:** 314447–314459
- **Relative position:** 0.845440
- **Chapter/section:** CHAPITRE XXIV
- **Supplied context:** 34 characters (12 before; 10 after)

#### Passage

> --Parce que je vous aime, pardieu!

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-2419\annotations\dumas-fils-la-dame-aux-camelias-85963bb66685\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The speaker directly presents love as the true reason for something: “Parce que je vous aime” functions primarily as an emphatic avowal of an emotional state. Nothing in the supplied text establishes a commitment or relational undertaking. The exclamation and “pardieu” intensify the delivery but do not independently show that “je vous aime” is a reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the core utterance as an emphatic avowal offered as a reason. Delivery-related intensity can remain contextual, with no residual pressure requiring P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "dumas-fils-la-dame-aux-camelias-85963bb66685",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.93,
    "analysis": "The speaker directly presents love as the true reason for something: “Parce que je vous aime” functions primarily as an emphatic avowal of an emotional state. Nothing in the supplied text establishes a commitment or relational undertaking. The exclamation and “pardieu” intensify the delivery but do not independently show that “je vous aime” is a reflex-like expressive discharge.",
    "ambiguity": "The very short extract leaves the larger conversational purpose unspecified, but this does not materially undermine the dominant truth-conditional classification."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly spoken love avowal embedded in the causal reply “Parce que je vous aime, pardieu!”"
  },
  "contextual_interpretation": "The utterance answers an implicit question with love as the speaker’s reason. “Pardieu!” and the exclamation mark convey forceful, emotionally emphatic delivery, but intensity alone neither creates performative commitment nor establishes expressive/reflexive core force.",
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“Parce que je vous aime, pardieu!”",
      "supports": "The causal construction presents the speaker’s love as an asserted explanation, strongly supporting T.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "The utterance ends with “pardieu!” and an exclamation mark.",
      "supports": "This supports emphatic delivery but, without evidence of blurting or reflex-like production, does not independently support E.",
      "confidence": 0.95
    },
    {
      "evidence_id": "E3",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XXIV of Alexandre Dumas fils’s La Dame aux camélias.",
      "supports": "Identifies the utterance as literary dialogue in the named work; the supplied metadata adds no evidence of a distinct undertaking or nonstandard core force.",
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
    "diagnosis": "T naturally captures the core utterance as an emphatic avowal offered as a reason. Delivery-related intensity can remain contextual, with no residual pressure requiring P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 14. `dumas-fils-la-dame-aux-camelias-48cb2a607749`

- **Exact match:** `je t'aime`
- **Pattern:** `fr_je_taime_apostrophe_spacing` (v0.6)
- **Source offsets:** 325989–325998
- **Relative position:** 0.876472
- **Chapter/section:** CHAPITRE XXIV
- **Supplied context:** 89 characters (41 before; 39 after)

#### Passage

> --Parce que, malgré ce que tu m'as fait, je t'aime toujours et que je
> veux te garder ici.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\gutenberg-2419\annotations\dumas-fils-la-dame-aux-camelias-48cb2a607749\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** “Je t’aime toujours” directly avows the speaker’s continuing love despite the addressee’s prior conduct. It primarily presents an emotional state as true. The accompanying wish to keep the addressee present explains the avowal’s relational stakes but does not make the love clause an undertaking, and there is no positive evidence of reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the core avowal of continuing love. The grievance and wish to retain the addressee are contextual qualifications adequately represented outside the core labels; no residual force requires O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "dumas-fils-la-dame-aux-camelias-48cb2a607749",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.95,
    "analysis": "“Je t’aime toujours” directly avows the speaker’s continuing love despite the addressee’s prior conduct. It primarily presents an emotional state as true. The accompanying wish to keep the addressee present explains the avowal’s relational stakes but does not make the love clause an undertaking, and there is no positive evidence of reflex-like expressive discharge.",
    "ambiguity": "The surrounding wish to retain the addressee could give the exchange a weak commitment-like implication, but the text explicitly frames it as desire (“je veux”), not as a promise or undertaking."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A character directly tells the addressee, in dialogue, “je t’aime toujours” (“I still love you”)."
  },
  "contextual_interpretation": "The speaker offers continuing love as the reason for wanting the addressee to remain: “despite what you have done to me” marks injury or grievance, while “still” emphasizes that the loving state persists. This concessive framing strengthens the force of the avowal without independently establishing performative commitment or expressive/reflexive discharge.",
  "evidence": [
    {
      "evidence_id": "ev1",
      "source": "local_text",
      "quotation_or_description": "« malgré ce que tu m'as fait, je t'aime toujours »",
      "supports": "The concessive clause and “toujours” present love as a persisting emotional state despite prior harm, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev2",
      "source": "local_text",
      "quotation_or_description": "« Parce que … je t'aime toujours et que je veux te garder ici. »",
      "supports": "“Parce que” makes the love avowal part of an explanation, while the coordinated desire to keep the addressee present supplies relational context but no explicit promise or undertaking.",
      "confidence": 0.96
    },
    {
      "evidence_id": "ev3",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located in Chapter XXIV of Alexandre Dumas fils’s La Dame aux camélias, in French direct-dialogue formatting.",
      "supports": "Supports identifying the event as a direct fictional utterance rather than narration, reported speech, or writing.",
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
    "diagnosis": "T naturally captures the core avowal of continuing love. The grievance and wish to retain the addressee are contextual qualifications adequately represented outside the core labels; no residual force requires O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The classification relies on the supplied excerpt and metadata; no wider-work plot knowledge was needed."
}
```

</details>
