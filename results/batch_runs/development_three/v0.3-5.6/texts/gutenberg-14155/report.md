# Single-text pipeline report: Madame Bovary

## Run summary

- **Run ID:** `gutenberg-14155`
- **Work:** *Madame Bovary* by Gustave Flaubert
- **Source:** `gutenberg-14155`
- **Annotation:** v0.3 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 12
- **Valid occurrences:** 12
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 7
- **Estimated total cost:** USD 0.772052

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `flaubert-madame-bovary-47361213aeaa`

- **Exact match:** `je vous aime`
- **Pattern:** `fr_je_vous_aime` (v0.2)
- **Source offsets:** 313772–313784
- **Relative position:** 0.446283
- **Chapter/section:** Unavailable
- **Supplied context:** 89 characters (7 before; 70 after)

#### Passage

> — Non, je vous aime, voilà tout! Vous n’en doutez pas! Dites-le-moi; un
> mot! un seul mot!

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-47361213aeaa\attempt-002`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 1 / 0
- **Core analysis:** “Je vous aime” is an emphatic direct avowal presented as true of the speaker’s emotional state. Its excited delivery gives it limited exclamatory force, but it neither clearly undertakes a relational obligation nor requires a category beyond T/P/E.
- **Ontology fit:** natural — T naturally captures the emphatic avowal, while a low E score records its excited delivery. The passage supplies no clear undertaking force and no residual core feature requiring O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-47361213aeaa",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 1,
      "other": 0
    },
    "confidence": 0.95,
    "analysis": "“Je vous aime” is an emphatic direct avowal presented as true of the speaker’s emotional state. Its excited delivery gives it limited exclamatory force, but it neither clearly undertakes a relational obligation nor requires a category beyond T/P/E.",
    "ambiguity": "The exclamation and urgent surrounding appeals create some E pressure, but the utterance retains strong, explicit propositional force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A character directly addresses another in dialogue: “je vous aime.”"
  },
  "contextual_interpretation": "The speaker emphatically rejects or corrects something with “Non,” reduces the explanation to love alone (“voilà tout”), insists that the addressee must not doubt it, and urgently requests verbal confirmation. This makes the avowal emotionally intense and responsive, but the request for “un mot” belongs to the surrounding exchange rather than turning the core declaration into an undertaking.",
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“Non, je vous aime, voilà tout!”",
      "supports": "The first-person present-tense declaration explicitly presents the speaker’s love as true, strongly supporting T; “Non” and the exclamation mark add limited emotional or exclamatory force.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“Vous n’en doutez pas! Dites-le-moi; un mot! un seul mot!”",
      "supports": "The urgent demand for reassurance shows emotional intensity and confirms that the declaration is addressed directly to an interlocutor, while providing no clear evidence that the core utterance itself enacts a commitment.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E3",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as French dialogue in Gustave Flaubert’s Madame Bovary, with the matched phrase “je vous aime.”",
      "supports": "Confirms the work, language, and precise expression being classified without adding unsupported plot assumptions.",
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
    "diagnosis": "T naturally captures the emphatic avowal, while a low E score records its excited delivery. The passage supplies no clear undertaking force and no residual core feature requiring O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 2. `flaubert-madame-bovary-d0ec3752ec68`

- **Exact match:** `Je t’aime`
- **Pattern:** `fr_je_taime` (v0.2)
- **Source offsets:** 328457–328466
- **Relative position:** 0.467170
- **Chapter/section:** Unavailable
- **Supplied context:** 65 characters (2 before; 54 after)

#### Passage

> — Je t’aime! répondit-elle en lui passant les bras autour du cou.

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-d0ec3752ec68\attempt-002`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 1 / 0
- **Core analysis:** “Je t’aime!” is primarily a direct avowal presented as true: the speaker answers with a declaration of her loving state. The exclamation mark and simultaneous embrace add emotional intensity, but the framing as a reply gives it clear propositional force. No distinct commitment or relational undertaking is expressed.
- **Ontology fit:** natural — T naturally captures the dominant avowal, while a low E score records the emotionally emphatic delivery. P is unnecessary because neither the words nor the immediate framing establish a commitment or obligation, and no residual core force requires O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-d0ec3752ec68",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 1,
      "other": 0
    },
    "confidence": 0.94,
    "analysis": "“Je t’aime!” is primarily a direct avowal presented as true: the speaker answers with a declaration of her loving state. The exclamation mark and simultaneous embrace add emotional intensity, but the framing as a reply gives it clear propositional force. No distinct commitment or relational undertaking is expressed.",
    "ambiguity": "The exclamation and embrace provide limited support for E, but the brief context does not show that the utterance is predominantly reflex-like rather than an intelligible avowal."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly uttered line of dialogue within the narrated scene, followed by the narrator’s description of the speaker embracing the addressee."
  },
  "contextual_interpretation": "The utterance is an emphatic response accompanied by putting her arms around the addressee’s neck. This bodily gesture reinforces affectionate engagement and emotional intensity. Nothing in the supplied passage establishes irony, deception, coercion, or an undertaking extending beyond the present avowal.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Je t’aime!”",
      "supports": "The conventional first-person declaration explicitly presents the speaker’s love as true, strongly supporting T; the exclamation mark gives slight support to E.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“répondit-elle”",
      "supports": "The speech is framed as an answer, supporting a deliberate propositional avowal rather than a purely reflexive exclamation.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“en lui passant les bras autour du cou”",
      "supports": "The simultaneous embrace reinforces affectionate and emotionally engaged delivery, while not by itself creating an undertaking.",
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
    "diagnosis": "T naturally captures the dominant avowal, while a low E score records the emotionally emphatic delivery. P is unnecessary because neither the words nor the immediate framing establish a commitment or obligation, and no residual core force requires O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 3. `flaubert-madame-bovary-8c91fb38ed76`

- **Exact match:** `je / t’aime`
- **Pattern:** `fr_je_taime` (v0.2)
- **Source offsets:** 346780–346789
- **Relative position:** 0.493231
- **Chapter/section:** Unavailable
- **Supplied context:** 113 characters (68 before; 36 after)

#### Passage

> — Amenez-la-moi! dit sa mère se précipitant pour l’embrasser. Comme je
> t’aime, ma pauvre enfant! comme je t’aime!

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-8c91fb38ed76\attempt-002`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 4 / 0
- **Core analysis:** The mother's “Comme je t’aime” strongly avows her loving emotional state while also functioning as an emotionally triggered exclamation. Her rush to embrace the addressee, the exclamatory syntax, and the immediate repetition reinforce E without weakening the clear T force. Nothing indicates a commitment or relational undertaking beyond the expression of affection.
- **Ontology fit:** natural — The combination of strong T and strong E naturally captures the utterance as an exclamatory avowal of maternal love. No important aspect of its core force falls outside T/P/E.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-8c91fb38ed76",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 4,
      "other": 0
    },
    "confidence": 0.97,
    "analysis": "The mother's “Comme je t’aime” strongly avows her loving emotional state while also functioning as an emotionally triggered exclamation. Her rush to embrace the addressee, the exclamatory syntax, and the immediate repetition reinforce E without weakening the clear T force. Nothing indicates a commitment or relational undertaking beyond the expression of affection.",
    "ambiguity": "T and E are simultaneously strong: the utterance is both a genuine avowal and an exclamation, rather than clearly reducible to only one mode."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A mother directly addresses her child in spoken dialogue while rushing to embrace her; the highlighted occurrence is the first of two immediately repeated declarations."
  },
  "contextual_interpretation": "The declaration occurs amid an urgent request to have the child brought to her and a movement to embrace her. “Comme” and the exclamation mark present the love as emotionally overflowing, while “ma pauvre enfant” adds tenderness and concern. The local passage supplies no evidence of deception, irony, or an undertaking with commitment force.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Comme je t’aime, ma pauvre enfant!”",
      "supports": "The explicit first-person declaration presents maternal love as true (T), while “Comme” and the exclamation mark strongly support exclamatory force (E).",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“dit sa mère se précipitant pour l’embrasser”",
      "supports": "The speaker is identified as the addressee's mother, and her rushing to embrace the child supports an emotionally activated, affectionate delivery.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "The declaration is immediately repeated: “comme je t’aime!”",
      "supports": "The emphatic repetition strengthens the reading of emotionally overflowing avowal and exclamation rather than a distinct undertaking.",
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
    "diagnosis": "The combination of strong T and strong E naturally captures the utterance as an exclamatory avowal of maternal love. No important aspect of its core force falls outside T/P/E.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 4. `flaubert-madame-bovary-06903c63a2d7`

- **Exact match:** `je t’aime`
- **Pattern:** `fr_je_taime` (v0.2)
- **Source offsets:** 346815–346824
- **Relative position:** 0.493281
- **Chapter/section:** Unavailable
- **Supplied context:** 113 characters (103 before; 1 after)

#### Passage

> — Amenez-la-moi! dit sa mère se précipitant pour l’embrasser. Comme je
> t’aime, ma pauvre enfant! comme je t’aime!

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-06903c63a2d7\attempt-002`
- **State:** `valid`
- **Core T/P/E/O support:** 3 / 0 / 4 / 0
- **Core analysis:** The mother's repeated « comme je t’aime ! » both avows her love and, more prominently, expresses it in an emotionally heightened, exclamatory outburst. Nothing indicates that the utterance undertakes a commitment or has force outside T/E.
- **Ontology fit:** natural — A combination of strong E and substantial T naturally captures the core force; no residual aspect requires O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-06903c63a2d7",
  "core_classification": {
    "label_support": {
      "truth_conditional": 3,
      "performative": 0,
      "exclamatory_reflexive": 4,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "The mother's repeated « comme je t’aime ! » both avows her love and, more prominently, expresses it in an emotionally heightened, exclamatory outburst. Nothing indicates that the utterance undertakes a commitment or has force outside T/E.",
    "ambiguity": "The main overlap is between a sincere truth-conditional avowal and an exclamation whose intensified form foregrounds immediate emotion; both forces are substantially present."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "The highlighted words are the mother's second directly spoken « comme je t’aime ! », addressed to her daughter and repeated in the same speech turn."
  },
  "contextual_interpretation": "The mother calls for her daughter, rushes to embrace her, addresses her compassionately as « ma pauvre enfant », and repeats the declaration with exclamation marks. The embrace, repetition, and « comme » construction strongly frame the utterance as an immediate surge of maternal affection, while its ordinary assertion of love remains intact. The passage supplies no distinct undertaking or promise.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "« Comme je t’aime, ma pauvre enfant! comme je t’aime! »",
      "supports": "The literal declaration supports truth-conditional avowal, while repetition, exclamation marks, and the intensifying « comme » strongly support exclamatory/reflexive force.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "« dit sa mère se précipitant pour l’embrasser »",
      "supports": "The mother's rush to embrace her daughter presents the words as an emotionally activated expression of maternal affection rather than a relational undertaking.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e3",
      "source": "supplied_metadata",
      "quotation_or_description": "The matched span is the final « je t’aime » in the supplied French context from Gustave Flaubert's Madame Bovary.",
      "supports": "Identifies the classified occurrence as the second declaration in a repeated direct utterance.",
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
    "diagnosis": "A combination of strong E and substantial T naturally captures the core force; no residual aspect requires O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The highlighted match is the second « je t’aime » in the repeated exclamation."
}
```

</details>

### 5. `flaubert-madame-bovary-fc563b7babfd`

- **Exact match:** `je t’aime`
- **Pattern:** `fr_je_taime` (v0.2)
- **Source offsets:** 373246–373255
- **Relative position:** 0.530874
- **Chapter/section:** Unavailable
- **Supplied context:** 111 characters (90 before; 12 after)

#### Passage

> — Qu’as-tu? qu’as-tu? répétait-il stupéfait. Calme-toi!
> reprends-toi!... Tu sais bien que je t’aime! ... viens!

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-fc563b7babfd\attempt-002`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 1 / 0
- **Core analysis:** “Tu sais bien que je t’aime” explicitly presents the speaker’s love as an already established and supposedly known emotional state. Its urgent delivery adds limited exclamatory force, but the clear avowal remains dominant. It reassures rather than undertaking a new commitment.
- **Ontology fit:** natural — T captures the explicit avowal, while a low E score captures its urgent emotional delivery. P is unnecessary because reassurance and an adjacent command do not establish undertaking force, and no residual core feature requires O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-fc563b7babfd",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 1,
      "other": 0
    },
    "confidence": 0.93,
    "analysis": "“Tu sais bien que je t’aime” explicitly presents the speaker’s love as an already established and supposedly known emotional state. Its urgent delivery adds limited exclamatory force, but the clear avowal remains dominant. It reassures rather than undertaking a new commitment.",
    "ambiguity": "The exclamation marks and crisis-like exchange give the avowal some emotionally triggered force, but not enough to weaken its clear propositional content."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A character directly tells another character, “Tu sais bien que je t’aime,” within spoken dialogue."
  },
  "contextual_interpretation": "The speaker is astonished by the addressee’s distress and repeatedly urges them to calm down. The love avowal functions as immediate reassurance and as an appeal to something the addressee is said already to know; the following “viens!” reinforces the urgency. Nothing in the supplied excerpt establishes a distinct promise or relational undertaking, regardless of the speaker’s possible sincerity outside this context.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Tu sais bien que je t’aime!”",
      "supports": "The complement “que je t’aime” clearly avows a loving state, while “tu sais bien” frames that state as established and already known, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“Qu’as-tu? qu’as-tu? répétait-il stupéfait. Calme-toi! reprends-toi!”",
      "supports": "The repeated questions, astonishment, and urgent imperatives establish an emotionally charged situation, giving limited support to E and showing the reassuring function of the avowal.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "The avowal is followed by “viens!”",
      "supports": "The adjacent imperative confirms urgency, but because it is grammatically separate from the love statement, it does not by itself turn that statement into a commitment or undertaking.",
      "confidence": 0.95
    },
    {
      "evidence_id": "e4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is extracted from Gustave Flaubert’s French novel Madame Bovary and matched as “je t’aime.”",
      "supports": "Confirms the language, work, and identified core expression without adding unsupported plot assumptions.",
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
    "diagnosis": "T captures the explicit avowal, while a low E score captures its urgent emotional delivery. P is unnecessary because reassurance and an adjacent command do not establish undertaking force, and no residual core feature requires O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 6. `flaubert-madame-bovary-8fe83e2776a5`

- **Exact match:** `je t’aime`
- **Pattern:** `fr_je_taime` (v0.2)
- **Source offsets:** 381592–381601
- **Relative position:** 0.542745
- **Chapter/section:** Unavailable
- **Supplied context:** 36 characters (12 before; 15 after)

#### Passage

> — Mais oui, je t’aime! répondait-il.

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-8fe83e2776a5\attempt-002`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 1 / 0
- **Core analysis:** Rodolphe directly presents his love for Emma as true in response to her demand for reassurance. The exclamation mark and emphatic “Mais oui” add affective emphasis, but the utterance remains a clear avowal rather than a primarily reflexive exclamation. It does not itself undertake a commitment or obligation.
- **Ontology fit:** natural — T naturally captures the explicit avowal, with minor E support for emphatic delivery. No substantial undertaking force or residual core function requires P or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-8fe83e2776a5",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 1,
      "other": 0
    },
    "confidence": 0.91,
    "analysis": "Rodolphe directly presents his love for Emma as true in response to her demand for reassurance. The exclamation mark and emphatic “Mais oui” add affective emphasis, but the utterance remains a clear avowal rather than a primarily reflexive exclamation. It does not itself undertake a commitment or obligation.",
    "ambiguity": "The emphatic form gives limited E support, while the wider relationship raises doubts about sincerity; neither factor displaces the utterance's dominant truth-conditional force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Direct dialogue spoken by Rodolphe to Emma, embedded in narration; the imperfect “répondait-il” presents it as a characteristic or repeated response."
  },
  "contextual_interpretation": "The reply functions as reassurance when Emma seeks confirmation of Rodolphe's love. “Mais oui” can sound mildly impatient or formulaic as well as emphatic, and the wider novel casts doubt on the depth and durability of Rodolphe's declarations. Possible insincerity, habituation, or manipulation concerns the reliability and context of the avowal, not its core T/P/E force.",
  "evidence": [
    {
      "evidence_id": "ev1-local-avowal",
      "source": "local_text",
      "quotation_or_description": "“Mais oui, je t’aime!”",
      "supports": "The first-person present-tense declaration explicitly presents the speaker's love for the addressee as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev2-local-response",
      "source": "local_text",
      "quotation_or_description": "“répondait-il”",
      "supports": "Marks the declaration as a spoken reply; the imperfect also suggests a recurring or characteristic reassurance rather than a singular new undertaking.",
      "confidence": 0.93
    },
    {
      "evidence_id": "ev3-local-emphasis",
      "source": "local_text",
      "quotation_or_description": "The emphatic opening “Mais oui” and exclamation mark.",
      "supports": "Provides limited E support through emphatic, emotionally marked delivery, though clear propositional force remains dominant.",
      "confidence": 0.9
    },
    {
      "evidence_id": "ev4-background-relationship",
      "source": "background_knowledge",
      "quotation_or_description": "In the surrounding Rodolphe–Emma affair, Emma repeatedly seeks assurances while Rodolphe's conduct and Flaubert's framing undermine confidence in the depth or durability of his professed passion.",
      "supports": "Explains the reply's reassuring and potentially formulaic or insincere context without converting that contextual doubt into O or eliminating T.",
      "confidence": 0.86
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.86,
    "contribution": "Used to identify the speaker and addressee as Rodolphe and Emma and to interpret the declaration as recurrent reassurance within an affair whose sincerity is narratively questioned."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T naturally captures the explicit avowal, with minor E support for emphatic delivery. No substantial undertaking force or residual core function requires P or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 7. `flaubert-madame-bovary-400a3aed5a88`

- **Exact match:** `je t’aime`
- **Pattern:** `fr_je_taime` (v0.2)
- **Source offsets:** 381853–381862
- **Relative position:** 0.543116
- **Chapter/section:** Unavailable
- **Supplied context:** 506 characters (16 before; 481 after)

#### Passage

> — Oh! c’est que je t’aime! reprenait-elle, je t’aime à ne pouvoir me
> passer de toi, sais-tu bien? J’ai quelquefois des envies de te revoir
> où toutes les colères de l’amour me déchirent. Je me demande: «Où
> est-il? Peut-être il parle à d’autres femmes? Elles lui sourient, il
> s’approche...» Oh! non, n’est-ce pas, aucune ne te plaît? Il y en a de
> plus belles; mais, moi, je sais mieux aimer! Je suis ta servante et
> ta concubine! Tu es mon roi, mon idole! tu es bon! tu es beau! tu es
> intelligent! tu es fort!

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-400a3aed5a88\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 3 / 0
- **Core analysis:** The core event is Emma's emphatic avowal, “Oh! c’est que je t’aime!”, immediately repeated and explained as an inability to live without the addressee. It strongly presents her love as true and is simultaneously staged as an emotionally overflowing exclamation. Despite the surrounding language of devotion and relational subordination, the core utterance does not clearly undertake or renew an obligation or commitment.
- **Ontology fit:** natural — T and E naturally capture the important core forces: an explicit avowal of a loving state delivered as an emotional outburst. The surrounding romantic scripting, jealousy, repetition, and narrative irony affect interpretation but do not reveal a core-force dimension left unrepresented by T/P/E.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-400a3aed5a88",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 3,
      "other": 0
    },
    "confidence": 0.93,
    "analysis": "The core event is Emma's emphatic avowal, “Oh! c’est que je t’aime!”, immediately repeated and explained as an inability to live without the addressee. It strongly presents her love as true and is simultaneously staged as an emotionally overflowing exclamation. Despite the surrounding language of devotion and relational subordination, the core utterance does not clearly undertake or renew an obligation or commitment.",
    "ambiguity": "The imperfect reporting frame and highly stylised romantic language suggest a recurrent or rehearsed mode of expression, which slightly complicates how reflex-like the outburst is; nevertheless, its presented exclamatory force is substantial."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Direct oral speech represented by the narrator, though “reprenait-elle” places it in an iterative or recurrent narrative frame rather than fixing it as a uniquely bounded occasion."
  },
  "contextual_interpretation": "Emma intensifies the avowal through repetition, jealousy, longing, idealisation, and declarations of submission: she cannot do without him, imagines rival women, and calls herself his servant and concubine. This makes the utterance an emotionally charged profession of love rather than a distinct promise. In the wider novel, Emma's expression draws on romantic absolutism while her relationship with Rodolphe is markedly asymmetrical; that narrative irony bears on sincerity, self-understanding, and reception, but it does not prevent the utterance itself from combining truth-conditional avowal with exclamatory force.",
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“Oh! c’est que je t’aime! reprenait-elle, je t’aime à ne pouvoir me passer de toi”",
      "supports": "The explicit repetition and explanatory continuation strongly support truth-conditional avowal: the speaker presents love and dependence as her actual emotional state.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "The speech begins with “Oh!”, uses exclamation marks, and expands into jealousy, longing, and extravagant praise: “mon roi, mon idole”.",
      "supports": "The punctuation, interjection, repetition, and escalating language support substantial exclamatory and emotionally overflowing force.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“Je suis ta servante et ta concubine!”",
      "supports": "This invokes an existing relationship and dramatizes submission, but it does not clearly make a new commitment; accordingly it provides little support for classifying the core love avowal as performative.",
      "confidence": 0.9
    },
    {
      "evidence_id": "E4",
      "source": "supplied_metadata",
      "quotation_or_description": "The supplied metadata identifies the source as Gustave Flaubert's French novel Madame Bovary and locates the occurrence at approximately 54.3% of the source text.",
      "supports": "This establishes the bibliographic and narrative provenance used to connect the passage with the wider fictional context without treating metadata as passage wording.",
      "confidence": 1.0
    },
    {
      "evidence_id": "E5",
      "source": "background_knowledge",
      "quotation_or_description": "In the wider episode, Emma is addressing her lover Rodolphe; their affair is asymmetrical, and Flaubert frames Emma's absolutist romantic discourse with narrative irony and Rodolphe's comparatively detached response.",
      "supports": "This helps explain the stylised, recurrent character of the avowal and the possibility of unequal reception while leaving its core avowing and exclamatory force intact.",
      "confidence": 0.91
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.91,
    "contribution": "Background knowledge identifies Emma and Rodolphe and supplies the affair's asymmetrical, ironically framed context. The numerical classification remains primarily grounded in the supplied local text."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T and E naturally capture the important core forces: an explicit avowal of a loving state delivered as an emotional outburst. The surrounding romantic scripting, jealousy, repetition, and narrative irony affect interpretation but do not reveal a core-force dimension left unrepresented by T/P/E.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 8. `flaubert-madame-bovary-acc8280ba5f0`

- **Exact match:** `je t’aime`
- **Pattern:** `fr_je_taime` (v0.2)
- **Source offsets:** 381880–381889
- **Relative position:** 0.543155
- **Chapter/section:** Unavailable
- **Supplied context:** 506 characters (43 before; 454 after)

#### Passage

> — Oh! c’est que je t’aime! reprenait-elle, je t’aime à ne pouvoir me
> passer de toi, sais-tu bien? J’ai quelquefois des envies de te revoir
> où toutes les colères de l’amour me déchirent. Je me demande: «Où
> est-il? Peut-être il parle à d’autres femmes? Elles lui sourient, il
> s’approche...» Oh! non, n’est-ce pas, aucune ne te plaît? Il y en a de
> plus belles; mais, moi, je sais mieux aimer! Je suis ta servante et
> ta concubine! Tu es mon roi, mon idole! tu es bon! tu es beau! tu es
> intelligent! tu es fort!

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-acc8280ba5f0\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 2 / 0
- **Core analysis:** The highlighted “je t’aime” is primarily an emphatic avowal of the speaker’s love, immediately elaborated as emotional dependence and jealous longing. The interjection, exclamation marks, repetition, and escalating praise give it substantial exclamatory force, but its propositional avowal remains clear. It does not itself undertake a commitment or create an obligation.
- **Ontology fit:** natural — T and E naturally capture the declaration’s clear avowal and its emotionally heightened delivery. P is unnecessary because neither the declaration nor its elaboration clearly creates or renews an undertaking. No important aspect of the core force remains outside T/P/E.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-acc8280ba5f0",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 2,
      "other": 0
    },
    "confidence": 0.92,
    "analysis": "The highlighted “je t’aime” is primarily an emphatic avowal of the speaker’s love, immediately elaborated as emotional dependence and jealous longing. The interjection, exclamation marks, repetition, and escalating praise give it substantial exclamatory force, but its propositional avowal remains clear. It does not itself undertake a commitment or create an obligation.",
    "ambiguity": "The highly emotional delivery creates some overlap between truth-conditional avowal and exclamatory expression, but there is little evidence of performative undertaking force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly represented spoken declaration in dialogue, introduced by the speech tag “reprenait-elle”; the highlighted occurrence is followed by an immediate repetition."
  },
  "contextual_interpretation": "The speaker presents her love as overwhelming dependence, jealousy, and idealisation: she cannot do without the addressee, imagines him approaching other women, and calls herself his servant and concubine while calling him her king and idol. This extravagant rhetoric may be theatrical and is situated within the novel’s unequal, ultimately disenchanted adulterous relationship, but it still functions locally as an intelligible avowal rather than as a semantically empty token. The surrounding declarations of submission intensify the relationship rhetoric without turning the core “je t’aime” into a clear commitment-making act.",
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“Oh! c’est que je t’aime! reprenait-elle, je t’aime à ne pouvoir me passer de toi”",
      "supports": "The explicit declaration and its paraphrase as inability to live without the addressee strongly support truth-conditional avowal; “Oh!”, repetition, and exclamation marks support secondary exclamatory force.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "The speaker describes “toutes les colères de l’amour,” imagines the addressee speaking to other women, and anxiously asks whether any of them pleases him.",
      "supports": "The jealousy and emotional agitation contextualise the declaration as an intense, affectively triggered expression while preserving its clear claim of love.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“Je suis ta servante et ta concubine! Tu es mon roi, mon idole!”",
      "supports": "These hyperbolic relational and devotional formulations reinforce dependence and idealisation. They provide context for the declaration but do not establish that the highlighted core utterance performs a definite undertaking.",
      "confidence": 0.96
    },
    {
      "evidence_id": "E4",
      "source": "supplied_metadata",
      "quotation_or_description": "The supplied metadata identifies the passage as French dialogue from Gustave Flaubert’s Madame Bovary, approximately 54.3% through the Gutenberg source.",
      "supports": "This establishes the work, language, and narrative location used when relating the local declaration to the novel’s broader treatment of romantic rhetoric.",
      "confidence": 1.0
    },
    {
      "evidence_id": "E5",
      "source": "background_knowledge",
      "quotation_or_description": "In the wider novel, Emma’s adulterous love rhetoric is marked by romantic idealisation, while her lover’s perspective increasingly exposes an asymmetry between her emotional investment and his more jaded response.",
      "supports": "This helps explain the declaration’s extravagant and potentially conventionalised language without displacing its local force as an avowal. The exact immediate addressee is not independently established by the supplied excerpt alone.",
      "confidence": 0.86
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.88,
    "contribution": "Knowledge of the novel’s adulterous relationships and its ironic treatment of romantic language supports reading the speech as intensely idealising and relationally asymmetrical, while the T/P/E scores remain chiefly grounded in the supplied text."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T and E naturally capture the declaration’s clear avowal and its emotionally heightened delivery. P is unnecessary because neither the declaration nor its elaboration clearly creates or renews an undertaking. No important aspect of the core force remains outside T/P/E.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 9. `flaubert-madame-bovary-97b0baa4e5cf`

- **Exact match:** `je t’aime`
- **Pattern:** `fr_je_taime` (v0.2)
- **Source offsets:** 396464–396473
- **Relative position:** 0.563898
- **Chapter/section:** Unavailable
- **Supplied context:** 57 characters (5 before; 43 after)

#### Passage

> — Si je t’aime! si je t’aime! mais je t’adore, mon amour!

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-97b0baa4e5cf\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 4 / 0
- **Core analysis:** The highlighted first “je t’aime” is an emphatic avowal of love and therefore has strong truth-conditional force. Its rhetorical construction, repetition, exclamation marks, and escalation to “je t’adore” also give it very strong exclamatory force. Nothing in the supplied text indicates that the utterance itself undertakes or renews a commitment.
- **Ontology fit:** natural — A strong combination of T and E naturally captures both the explicit avowal and its highly exclamatory delivery. No important core-force residue requires O, and the passage provides no undertaking force sufficient for P.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-97b0baa4e5cf",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 4,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "The highlighted first “je t’aime” is an emphatic avowal of love and therefore has strong truth-conditional force. Its rhetorical construction, repetition, exclamation marks, and escalation to “je t’adore” also give it very strong exclamatory force. Nothing in the supplied text indicates that the utterance itself undertakes or renews a commitment.",
    "ambiguity": "The exclamatory delivery does not erase the clear avowal: T and E are both strongly supported. The wider sincerity or strategic purpose of the declaration cannot be determined from the short extract."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "The highlighted phrase is the first directly spoken “je t’aime” in the dialogue line “Si je t’aime! si je t’aime! mais je t’adore, mon amour!”"
  },
  "contextual_interpretation": "The French construction “Si je t’aime!” functions here as an emphatic response akin to “Do I love you!” rather than as an unresolved condition. Immediate repetition and the stronger continuation “mais je t’adore, mon amour!” intensify the declaration. The excerpt supplies no secure evidence about sincerity, deception, manipulation, or any concrete relational undertaking, and those issues are not needed to represent the core force as combined T and E.",
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“Si je t’aime!”",
      "supports": "The highlighted utterance explicitly presents the speaker's love as true while using an emphatic exclamatory construction.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“si je t’aime! mais je t’adore, mon amour!”",
      "supports": "Repetition, exclamation marks, direct address, and escalation from loving to adoring strongly support exclamatory intensity while reinforcing the avowal.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence metadata identifies the match as French “je t’aime” in Gustave Flaubert's Madame Bovary and locates it within direct-dialogue punctuation.",
      "supports": "Confirms the language, work, and exact highlighted occurrence without adding unsupported plot claims.",
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
    "diagnosis": "A strong combination of T and E naturally captures both the explicit avowal and its highly exclamatory delivery. No important core-force residue requires O, and the passage provides no undertaking force sufficient for P.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The classification targets the first highlighted “je t’aime”; the immediate repetition is treated as evidence about its force."
}
```

</details>

### 10. `flaubert-madame-bovary-b0502164917d`

- **Exact match:** `je t’aime`
- **Pattern:** `fr_je_taime` (v0.2)
- **Source offsets:** 396478–396487
- **Relative position:** 0.563918
- **Chapter/section:** Unavailable
- **Supplied context:** 57 characters (19 before; 29 after)

#### Passage

> — Si je t’aime! si je t’aime! mais je t’adore, mon amour!

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-b0502164917d\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 3 / 0
- **Core analysis:** The highlighted « je t’aime » occurs within the emphatic construction « Si je t’aime! », presenting the speaker's love as true while also functioning as an emotionally charged exclamation. Repetition and escalation to « je t’adore » strengthen both the avowal and its exclamatory delivery. Nothing in the supplied passage establishes an undertaking or relational commitment.
- **Ontology fit:** natural — T and E naturally capture the utterance as a clear avowal delivered in an emphatic, emotionally heightened manner. P is unnecessary because no commitment or obligation is enacted, and there is no residual core force requiring O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-b0502164917d",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 3,
      "other": 0
    },
    "confidence": 0.94,
    "analysis": "The highlighted « je t’aime » occurs within the emphatic construction « Si je t’aime! », presenting the speaker's love as true while also functioning as an emotionally charged exclamation. Repetition and escalation to « je t’adore » strengthen both the avowal and its exclamatory delivery. Nothing in the supplied passage establishes an undertaking or relational commitment.",
    "ambiguity": "The exclamatory form is prominent, but it does not displace the utterance's clear propositional avowal; the precise balance between T and E is therefore somewhat gradient."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A character directly addresses another with the spoken declaration « Si je t’aime! », repeated and intensified by « mais je t’adore, mon amour! »."
  },
  "contextual_interpretation": "The idiomatic « Si je t’aime! » is an emphatic confirmation, plausibly answering or resisting doubt about the speaker's love. Repetition, exclamation marks, direct second-person address, and the escalation from loving to adoring make the delivery highly affective. The narrow extract does not identify the participants or establish whether the declaration is sincere, deceptive, or strategically reassuring, but those possibilities do not alter its presented T/E force.",
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "« Si je t’aime! si je t’aime! »",
      "supports": "The repeated idiomatic assertion emphatically presents the speaker's love as true, supporting strong truth-conditional force and substantial exclamatory force.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "« mais je t’adore, mon amour! »",
      "supports": "The escalation from « je t’aime » to « je t’adore », together with the endearment and exclamation mark, reinforces emotional intensity without clearly undertaking a commitment.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E3",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as French dialogue in Gustave Flaubert's Madame Bovary, from Project Gutenberg source 14155.",
      "supports": "Confirms the linguistic and literary-dialogue setting in which the French construction is interpreted; it does not by itself determine sincerity or speaker identity.",
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
    "diagnosis": "T and E naturally capture the utterance as a clear avowal delivered in an emphatic, emotionally heightened manner. P is unnecessary because no commitment or obligation is enacted, and there is no residual core force requiring O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The classification is based on the supplied extract; no wider-scene identification or assumptions about sincerity were required."
}
```

</details>

### 11. `flaubert-madame-bovary-5396f984c871`

- **Exact match:** `je vous aime`
- **Pattern:** `fr_je_vous_aime` (v0.2)
- **Source offsets:** 597385–597397
- **Relative position:** 0.849671
- **Chapter/section:** Unavailable
- **Supplied context:** 33 characters (20 before; 1 after)

#### Passage

> — De grâce, restez! je vous aime!

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-5396f984c871\attempt-002`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 3 / 0
- **Core analysis:** The speaker directly avows love as the reason for an urgent plea that the addressee remain. The declaration strongly presents a loving state as true and, through its exclamatory placement after “restez!”, also has substantial emotionally triggered force. It does not clearly undertake or renew a commitment.
- **Ontology fit:** natural — T and E naturally capture the declaration’s avowal of love and its urgent exclamatory delivery. No important aspect of the core force requires O, and the adjacent plea does not by itself establish performative commitment.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-5396f984c871",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 3,
      "other": 0
    },
    "confidence": 0.91,
    "analysis": "The speaker directly avows love as the reason for an urgent plea that the addressee remain. The declaration strongly presents a loving state as true and, through its exclamatory placement after “restez!”, also has substantial emotionally triggered force. It does not clearly undertake or renew a commitment.",
    "ambiguity": "The very short extract does not establish how spontaneous or strategically persuasive the declaration is, but that uncertainty lies between truth-conditional and exclamatory force rather than outside T/P/E."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly spoken love declaration in dialogue, immediately following an urgent request that the addressee stay."
  },
  "contextual_interpretation": "“De grâce, restez!” frames “je vous aime!” as an urgent appeal against departure: the speaker invokes an asserted emotional state to persuade the addressee to remain. The exclamation marks and compressed sequence support emotional intensity, while the available passage does not justify a firm conclusion about sincerity, calculation, or the broader relationship.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“je vous aime!”",
      "supports": "The conventional declarative wording strongly supports truth-conditional avowal, while the exclamation mark supports heightened exclamatory force.",
      "confidence": 0.98
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "“De grâce, restez! je vous aime!”",
      "supports": "The declaration functions as an emotionally urgent reason for asking the addressee to stay, without explicitly creating a commitment or obligation.",
      "confidence": 0.95
    },
    {
      "evidence_id": "metadata-1",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as French dialogue in Gustave Flaubert’s Madame Bovary, matching the pattern fr_je_vous_aime.",
      "supports": "Confirms that the highlighted event is an embedded direct French equivalent of “I love you” in a literary dialogue context.",
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
    "diagnosis": "T and E naturally capture the declaration’s avowal of love and its urgent exclamatory delivery. No important aspect of the core force requires O, and the adjacent plea does not by itself establish performative commitment.",
    "candidate_recurrent_dimension": null
  },
  "notes": "Classification is intentionally based on the supplied local text and metadata; no wider-scene identification is assumed."
}
```

</details>

### 12. `flaubert-madame-bovary-1e7d6742e45b`

- **Exact match:** `Je t’aime`
- **Pattern:** `fr_je_taime` (v0.2)
- **Source offsets:** 610512–610521
- **Relative position:** 0.868342
- **Chapter/section:** Unavailable
- **Supplied context:** 139 characters (80 before; 50 after)

#### Passage

> — Ah! pardonne-moi! tu es la seule qui me plaise. J’ai été imbécile et
> méchant! Je t’aime, je t’aimerai toujours!... Qu’as-tu? dis-le donc!

#### Annotation

- **Selected attempt:** `results\batch_runs\development_three\v0.3-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-1e7d6742e45b\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 2 / 2 / 0
- **Core analysis:** The direct declaration “Je t’aime” primarily avows a present loving state. Its placement within an urgent apology and beside “je t’aimerai toujours” gives it a secondary function of reassurance and relational recommitment. The exclamations and rapid sequence lend emotional spontaneity, but the utterance retains clear propositional force.
- **Ontology fit:** natural — T/P/E naturally captures the utterance as chiefly an avowal, with secondary relational-repair and emotionally heightened force. Questions about sincerity or manipulation belong to contextual interpretation rather than indicating an unrepresented core-force category.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-1e7d6742e45b",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 2,
      "exclamatory_reflexive": 2,
      "other": 0
    },
    "confidence": 0.89,
    "analysis": "The direct declaration “Je t’aime” primarily avows a present loving state. Its placement within an urgent apology and beside “je t’aimerai toujours” gives it a secondary function of reassurance and relational recommitment. The exclamations and rapid sequence lend emotional spontaneity, but the utterance retains clear propositional force.",
    "ambiguity": "The future-tense continuation can be heard either as a prediction of enduring feeling or as a promise-like undertaking, so the precise degree of performative force is uncertain."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A male speaker directly addresses a female interlocutor in represented dialogue, declaring “Je t’aime” as part of an apology and reassurance."
  },
  "contextual_interpretation": "The speaker asks forgiveness, calls himself foolish and cruel, asserts that the addressee is the only woman who pleases him, and then declares present and lasting love. This makes the declaration strongly avowal-like while also using it to repair a strained interaction. The local passage does not establish whether the profession is sincere, calculated, or durable; those questions do not alter its principally truth-conditional and secondarily commitment-invoking force.",
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“Je t’aime”",
      "supports": "The unhedged first-person present declaration directly presents the speaker's loving emotional state as true.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“Ah! pardonne-moi! ... J’ai été imbécile et méchant!”",
      "supports": "The declaration occurs within an emotionally heightened apology and attempted relational repair, supporting some exclamatory and reassurance-related force.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“tu es la seule qui me plaise”",
      "supports": "The claim that the addressee is uniquely pleasing reinforces the declaration as an avowal directed specifically to her.",
      "confidence": 0.96
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "“je t’aimerai toujours!”",
      "supports": "The immediately following claim of permanent future love gives the sequence limited promise-like or recommitting force, although it can also be read simply as a prediction about emotion.",
      "confidence": 0.92
    },
    {
      "evidence_id": "E5",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as French dialogue from Gustave Flaubert's Madame Bovary in Project Gutenberg source 14155.",
      "supports": "This establishes the bibliographic provenance and confirms that the highlighted French wording is being assessed as a represented fictional utterance.",
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
    "diagnosis": "T/P/E naturally captures the utterance as chiefly an avowal, with secondary relational-repair and emotionally heightened force. Questions about sincerity or manipulation belong to contextual interpretation rather than indicating an unrepresented core-force category.",
    "candidate_recurrent_dimension": null
  },
  "notes": "Scores apply to the highlighted declaration while treating its immediately adjacent apology and future-tense repetition as evidence of pragmatic force."
}
```

</details>
