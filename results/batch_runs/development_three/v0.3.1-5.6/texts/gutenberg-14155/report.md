# Single-text pipeline report: Madame Bovary

## Run summary

- **Run ID:** `gutenberg-14155`
- **Work:** *Madame Bovary* by Gustave Flaubert
- **Source:** `gutenberg-14155`
- **Annotation:** v0.3.1 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 12
- **Valid occurrences:** 12
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.442656

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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-47361213aeaa\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** “Je vous aime” is presented straightforwardly as an avowal of the speaker’s loving state. “Voilà tout” frames that state as the speaker’s decisive explanation, while the request for confirmation that the addressee believes it reinforces its assertive force. The passage supplies no independent evidence that the words enact a commitment or arise as a reflex-like expressive discharge.
- **Ontology fit:** natural — T/P/E/O naturally represents the core event as a strong truth-conditional avowal. Its emphatic, pressuring delivery is contextual information and creates no residual core-force dimension requiring O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-47361213aeaa",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.94,
    "analysis": "“Je vous aime” is presented straightforwardly as an avowal of the speaker’s loving state. “Voilà tout” frames that state as the speaker’s decisive explanation, while the request for confirmation that the addressee believes it reinforces its assertive force. The passage supplies no independent evidence that the words enact a commitment or arise as a reflex-like expressive discharge.",
    "ambiguity": "The emphatic punctuation and urgent requests convey emotional intensity and interpersonal pressure, but they do not independently establish expressive/reflexive or undertaking force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A character directly addresses another in dialogue: “Non, je vous aime, voilà tout!”"
  },
  "contextual_interpretation": "The declaration is emphatic and insistent. The speaker not only avows love but presses the addressee to acknowledge believing the avowal: “Vous n’en doutez pas! Dites-le-moi.” This may have persuasive or courtship force in the interaction, but the core love utterance remains adequately represented as truth-conditional rather than as a commitment or reflexive discharge.",
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“je vous aime”",
      "supports": "Directly presents the speaker as having love for the addressee, strongly supporting truth-conditional force.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“voilà tout!”",
      "supports": "Frames the avowed love as the speaker’s complete or decisive explanation, reinforcing assertion rather than undertaking force.",
      "confidence": 0.94
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“Vous n’en doutez pas! Dites-le-moi; un mot! un seul mot!”",
      "supports": "Shows insistence that the addressee confirm belief or acknowledgment; it supplies contextual urgency but no independent evidence of a commitment or reflex-like discharge.",
      "confidence": 0.93
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
    "diagnosis": "T/P/E/O naturally represents the core event as a strong truth-conditional avowal. Its emphatic, pressuring delivery is contextual information and creates no residual core-force dimension requiring O.",
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-d0ec3752ec68\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The direct reply “Je t’aime!” straightforwardly avows that the speaker loves the addressee. Neither the words nor the supplied context independently establish a commitment or relational undertaking. The exclamation mark and accompanying embrace indicate affective intensity but do not show that the words are a reflex-like expressive discharge rather than an emphatic avowal.
- **Ontology fit:** natural — T naturally captures the core utterance as an avowal of love. The embrace and exclamatory punctuation can remain contextual features of delivery without requiring P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-d0ec3752ec68",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.92,
    "analysis": "The direct reply “Je t’aime!” straightforwardly avows that the speaker loves the addressee. Neither the words nor the supplied context independently establish a commitment or relational undertaking. The exclamation mark and accompanying embrace indicate affective intensity but do not show that the words are a reflex-like expressive discharge rather than an emphatic avowal.",
    "ambiguity": "The very short extract does not establish the avowal’s sincerity or broader interpersonal purpose, but those uncertainties do not alter its strongly truth-conditional force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A female character directly says “Je t’aime!” to the person around whose neck she then puts her arms; the narrator presents it as her spoken reply."
  },
  "contextual_interpretation": "The speech tag “répondit-elle” frames the utterance as an answer, while her embrace reinforces its affectionate and emotionally emphatic delivery. The extract provides no independent evidence of promising, undertaking an obligation, or involuntarily blurting out the words. Any possible sincerity, manipulation, or narrative irony remains unresolved by the supplied context.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“Je t’aime!”",
      "supports": "The conventional propositional content directly presents the speaker’s love for the addressee as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "“répondit-elle”",
      "supports": "The narrator identifies the utterance as her direct spoken reply, supporting direct status and an avowal-like reading.",
      "confidence": 0.97
    },
    {
      "evidence_id": "local-3",
      "source": "local_text",
      "quotation_or_description": "“en lui passant les bras autour du cou”",
      "supports": "The accompanying embrace supports affectionate intensity but supplies no independent evidence for performative undertaking or reflex-like expressive force.",
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
    "diagnosis": "T naturally captures the core utterance as an avowal of love. The embrace and exclamatory punctuation can remain contextual features of delivery without requiring P, E, or O.",
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-8c91fb38ed76\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 2 / 0
- **Core analysis:** The mother directly avows the strength of her love for the child. The marked degree-exclamative construction “Comme je t’aime,” its immediate repetition, and its emergence while she rushes to embrace the addressee provide moderate independent support for expressive discharge as well as strong truth-conditional avowal. Nothing indicates a commitment or relational undertaking beyond the affection expressed.
- **Ontology fit:** natural — T captures the avowal of maternal love and E captures the moderately supported exclamatory discharge. The surrounding tenderness and physical embrace are contextual features rather than evidence of a missing core-force category.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-8c91fb38ed76",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 2,
      "other": 0
    },
    "confidence": 0.88,
    "analysis": "The mother directly avows the strength of her love for the child. The marked degree-exclamative construction “Comme je t’aime,” its immediate repetition, and its emergence while she rushes to embrace the addressee provide moderate independent support for expressive discharge as well as strong truth-conditional avowal. Nothing indicates a commitment or relational undertaking beyond the affection expressed.",
    "ambiguity": "The exclamative syntax and affective action support E, but the narration does not explicitly present the words as involuntary or pre-reflective; they could also be understood primarily as an intensely delivered avowal."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "The highlighted first “je t’aime” occurs in the mother’s directly represented speech to the child; the same exclamative is then repeated."
  },
  "contextual_interpretation": "The maternal speaker rushes to embrace the addressee and twice exclaims how much she loves her, calling her “ma pauvre enfant.” The scene presents tender, pity-inflected maternal affection. The embrace and repetition intensify and partly externalize that affection, but do not establish any undertaking in the performative sense.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Comme je t’aime, ma pauvre enfant!”",
      "supports": "The explicit love predicate strongly supports T; the degree-exclamative form provides some independent support for E.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“dit sa mère se précipitant pour l’embrasser”",
      "supports": "The maternal relationship and immediate movement to embrace the addressee corroborate an affectively expressive context.",
      "confidence": 0.95
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "The clause “comme je t’aime!” is immediately repeated.",
      "supports": "Repetition strengthens the presentation of affective overflow, while remaining compatible with emphatic avowal.",
      "confidence": 0.9
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
    "diagnosis": "T captures the avowal of maternal love and E captures the moderately supported exclamatory discharge. The surrounding tenderness and physical embrace are contextual features rather than evidence of a missing core-force category.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The classification targets the first matched occurrence; the immediately repeated second occurrence is used as local contextual evidence."
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-06903c63a2d7\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 2 / 0
- **Core analysis:** The mother directly avows intense maternal love. The exclamative construction “Comme je t’aime!” and its immediate repetition provide some independent expressive force: the words appear partly to discharge overflowing affection, while still centrally presenting her love as true. Nothing indicates a relational undertaking or commitment.
- **Ontology fit:** natural — T naturally captures the avowal, while E captures the supported expressive component. P and O are unnecessary; the emotional and maternal context does not create a commitment force or any residual core function outside T/P/E.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-06903c63a2d7",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 2,
      "other": 0
    },
    "confidence": 0.9,
    "analysis": "The mother directly avows intense maternal love. The exclamative construction “Comme je t’aime!” and its immediate repetition provide some independent expressive force: the words appear partly to discharge overflowing affection, while still centrally presenting her love as true. Nothing indicates a relational undertaking or commitment.",
    "ambiguity": "The exclamative syntax, repetition, and impetuous embrace support E, but they could also be interpreted simply as the intense delivery of a T-dominant avowal; hence E is moderate rather than maximal."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "The highlighted second “comme je t’aime!” is spoken directly by the mother to her child, immediately repeating the same declaration."
  },
  "contextual_interpretation": "The mother calls for her child, rushes to embrace her, addresses her compassionately as “ma pauvre enfant,” and twice exclaims how much she loves her. This frames the utterance as an affectionate, consoling maternal avowal with a partially expressive outpouring, not as a promise or undertaking.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“dit sa mère se précipitant pour l’embrasser”",
      "supports": "The maternal attribution and rush to embrace support a direct, affectively charged avowal of love.",
      "confidence": 0.98
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "“Comme je t’aime, ma pauvre enfant! comme je t’aime!”",
      "supports": "The explicit love predication strongly supports T; the degree-exclamative form and immediate repetition provide moderate evidence that saying it also functions as expressive discharge.",
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
    "diagnosis": "T naturally captures the avowal, while E captures the supported expressive component. P and O are unnecessary; the emotional and maternal context does not create a commitment force or any residual core function outside T/P/E.",
    "candidate_recurrent_dimension": null
  },
  "notes": "Classification targets the highlighted second occurrence in the immediately repeated pair."
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-fc563b7babfd\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The embedded clause “je t’aime” is presented as an already established fact that the addressee knows, and it serves as a direct avowal and reassurance. Nothing in the passage makes it an undertaking or promise. Although the speaker is startled and the situation is urgent, the controlled appeal “Tu sais bien que…” gives no independent evidence that the words are an expressive or reflex-like discharge.
- **Ontology fit:** natural — T/P/E/O represents the core naturally as a strong truth-conditional avowal used for reassurance. Urgent delivery and surrounding directives are adequately treated as context, with no residual core force requiring E or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-fc563b7babfd",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.95,
    "analysis": "The embedded clause “je t’aime” is presented as an already established fact that the addressee knows, and it serves as a direct avowal and reassurance. Nothing in the passage makes it an undertaking or promise. Although the speaker is startled and the situation is urgent, the controlled appeal “Tu sais bien que…” gives no independent evidence that the words are an expressive or reflex-like discharge.",
    "ambiguity": "The utterance may have strategic or soothing interpersonal purposes, but these do not alter its predominantly truth-conditional core force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A male speaker directly tells the addressee “Tu sais bien que je t’aime,” with the love proposition embedded under an appeal to her existing knowledge."
  },
  "contextual_interpretation": "The speaker is responding to the addressee’s apparent distress or agitation: he repeatedly asks what is wrong, urges her to calm herself, reassures her that she knows he loves her, and then calls her to come. The reassurance is situationally instrumental, but the local text neither establishes deception nor supplies commitment-making or reflexive expressive force.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Tu sais bien que je t’aime!”",
      "supports": "The factive-style appeal to what the addressee already knows strongly supports a truth-conditional avowal of love.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“Qu’as-tu? qu’as-tu? répétait-il stupéfait. Calme-toi! reprends-toi!”",
      "supports": "The surrounding speech frames the avowal as reassurance intended to steady a distressed addressee; surprise and urgency concern the situation but do not independently establish expressive/reflexive force.",
      "confidence": 0.95
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "The separate imperative “viens!” follows the love avowal.",
      "supports": "The speaker also directs the addressee to act, but this imperative does not turn “je t’aime” itself into a relational undertaking or promise.",
      "confidence": 0.93
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
    "diagnosis": "T/P/E/O represents the core naturally as a strong truth-conditional avowal used for reassurance. Urgent delivery and surrounding directives are adequately treated as context, with no residual core force requiring E or O.",
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-8fe83e2776a5\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** “Mais oui, je t’aime!” is framed as an answer confirming that the speaker has loving feelings. Nothing in the excerpt independently presents it as undertaking a commitment or as a reflex-like affective discharge; the exclamation mark alone does not support E.
- **Ontology fit:** natural — T naturally captures the core force as an affirmative avowal. Any uncertainty concerns sincerity and interpersonal purpose rather than a missing category in the ontology.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-8fe83e2776a5",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "“Mais oui, je t’aime!” is framed as an answer confirming that the speaker has loving feelings. Nothing in the excerpt independently presents it as undertaking a commitment or as a reflex-like affective discharge; the exclamation mark alone does not support E.",
    "ambiguity": "The narrow excerpt does not establish whether the avowal is sincere, habitual, impatient, or reassuring, but those possibilities do not alter its strongly truth-conditional mode."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A character’s spoken French utterance is presented directly in dialogue and attributed by the narrator with “répondait-il.”"
  },
  "contextual_interpretation": "The prefatory “Mais oui” and the reporting clause “répondait-il” frame the utterance as an affirmative response, likely to a question or doubt about love. Its possible interpersonal role as reassurance does not by itself make it performative, and its emphatic punctuation does not establish expressive/reflexive force.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“Mais oui, je t’aime!”",
      "supports": "The affirmative “oui” and the proposition “je t’aime” strongly support a truth-conditional avowal of love.",
      "confidence": 0.99
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "“répondait-il”",
      "supports": "The narrator explicitly frames the words as his answer, reinforcing their responsive assertoric force and their status as direct speech.",
      "confidence": 0.98
    },
    {
      "evidence_id": "local-3",
      "source": "local_text",
      "quotation_or_description": "The utterance ends with an exclamation mark, but there is no description of blurting, involuntary speech, or affect producing the words.",
      "supports": "Intensity is possible, but there is no positive evidence for independent expressive/reflexive force.",
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
    "diagnosis": "T naturally captures the core force as an affirmative avowal. Any uncertainty concerns sincerity and interpersonal purpose rather than a missing category in the ontology.",
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-400a3aed5a88\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** The highlighted “je t’aime” primarily avows the speaker’s loving state, which she immediately elaborates as dependence, jealousy, and intense admiration. The wider speech weakly suggests relational self-commitment through declarations of service and submission, but the core utterance does not clearly undertake an obligation. Its exclamatory, passionate delivery does not independently establish reflex-like expressive force.
- **Ontology fit:** natural — T captures the central avowal, with slight P support for the relational submission developed around it. Emotional intensity is contextual and does not require E or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-400a3aed5a88",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.93,
    "analysis": "The highlighted “je t’aime” primarily avows the speaker’s loving state, which she immediately elaborates as dependence, jealousy, and intense admiration. The wider speech weakly suggests relational self-commitment through declarations of service and submission, but the core utterance does not clearly undertake an obligation. Its exclamatory, passionate delivery does not independently establish reflex-like expressive force.",
    "ambiguity": "The surrounding claims “Je suis ta servante et ta concubine” give limited support to a performative reading, though they more naturally characterize the avowed love than make “je t’aime” itself a commitment."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly spoken declaration in narrated dialogue; the highlighted occurrence is the first “je t’aime,” introduced by “Oh! c’est que” and followed by a repeated declaration."
  },
  "contextual_interpretation": "The declaration belongs to an extended, highly emotional profession of dependence, jealousy, devotion, and idealization. Repetition, exclamations, and hyperbole intensify the avowal, while “reprenait-elle” presents it as continued discourse rather than an involuntary blurt. Whatever the sincerity or durability of these feelings, the utterance presents love as true and is adequately represented mainly by T.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Oh! c’est que je t’aime! reprenait-elle, je t’aime à ne pouvoir me passer de toi”",
      "supports": "The speaker directly and repeatedly avows love and describes it as an inability to do without the addressee, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“J’ai quelquefois des envies de te revoir où toutes les colères de l’amour me déchirent.”",
      "supports": "The speaker explicitly attributes longing and emotional torment to love, reinforcing the truth-conditional presentation of an affective state.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“Je suis ta servante et ta concubine! Tu es mon roi, mon idole!”",
      "supports": "These declarations frame the love as relational devotion and self-subordination, supplying weak support for commitment-like force but not clearly making the highlighted words an undertaking.",
      "confidence": 0.9
    },
    {
      "evidence_id": "e4",
      "source": "local_text",
      "quotation_or_description": "The narration uses “reprenait-elle” before a sustained sequence of articulated claims, questions, and comparisons.",
      "supports": "The speech is presented as resumed and elaborated discourse; emotional punctuation alone does not provide positive evidence that “je t’aime” is a reflex-like verbal discharge, supporting E=0.",
      "confidence": 0.89
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
    "diagnosis": "T captures the central avowal, with slight P support for the relational submission developed around it. Emotional intensity is contextual and does not require E or O.",
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-acc8280ba5f0\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** The highlighted “je t’aime” primarily avows the speaker’s loving emotional state. Its continuation—declared dependence, jealousy, and claims of superior love—reinforces truth-conditional presentation. The surrounding self-positioning as servant and concubine gives the declaration slight relationally enactive force, but the core words do not clearly undertake a commitment. Although emphatic and repeated, the utterance is not represented as an involuntary or reflex-like discharge, so intensity alone does not support E.
- **Ontology fit:** natural — T captures the dominant avowal, while a low P score records the declaration’s slight role in invoking the lovers’ relationship. Emotional intensity, repetition, and idealization are adequately handled as context and delivery, without E or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-acc8280ba5f0",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.93,
    "analysis": "The highlighted “je t’aime” primarily avows the speaker’s loving emotional state. Its continuation—declared dependence, jealousy, and claims of superior love—reinforces truth-conditional presentation. The surrounding self-positioning as servant and concubine gives the declaration slight relationally enactive force, but the core words do not clearly undertake a commitment. Although emphatic and repeated, the utterance is not represented as an involuntary or reflex-like discharge, so intensity alone does not support E.",
    "ambiguity": "There is minor uncertainty between P=0 and P=1: the broader speech invokes an asymmetrical lover relationship, but the highlighted declaration itself contains no explicit undertaking."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly represented spoken declaration by the female speaker, embedded in narration; “reprenait-elle” indicates that she resumes or reiterates it."
  },
  "contextual_interpretation": "The speaker elaborates the declaration through dependence, jealous imaginings, requests for reassurance, self-abasement, and idealizing praise. This makes the avowal rhetorically intense and potentially reassurance-seeking, but those contextual functions do not displace its core presentation of love as true or independently establish expressive/reflexive force.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Oh! c’est que je t’aime!”",
      "supports": "The causal formulation “c’est que” presents love as an asserted explanation, strongly supporting T; the exclamation supplies intensity but not independently E.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“je t’aime à ne pouvoir me passer de toi”",
      "supports": "The repeated declaration and claim that she cannot do without the addressee elaborate the purported loving state, supporting T.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“J’ai quelquefois des envies de te revoir où toutes les colères de l’amour me déchirent.”",
      "supports": "Longing and the torments of love are offered as evidence of the emotional state being avowed.",
      "confidence": 0.94
    },
    {
      "evidence_id": "e4",
      "source": "local_text",
      "quotation_or_description": "“Je suis ta servante et ta concubine! Tu es mon roi, mon idole!”",
      "supports": "The speaker invokes and dramatizes a relational posture, providing limited secondary support for P while primarily contextualizing the avowal.",
      "confidence": 0.88
    },
    {
      "evidence_id": "e5",
      "source": "local_text",
      "quotation_or_description": "The declaration is introduced and then repeated with exclamations, but the narration does not say that the words escaped involuntarily or preceded reflection.",
      "supports": "Supports E=0 under the narrow calibration: emotional delivery and repetition alone do not establish expressive/reflexive core force.",
      "confidence": 0.92
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
    "diagnosis": "T captures the dominant avowal, while a low P score records the declaration’s slight role in invoking the lovers’ relationship. Emotional intensity, repetition, and idealization are adequately handled as context and delivery, without E or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The classification applies to the first highlighted occurrence of “je t’aime,” while using the immediately repeated phrase and ensuing speech as contextual evidence."
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-97b0baa4e5cf\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The highlighted “je t’aime” is an emphatic avowal presenting the speaker’s love as true. The exclamative “Si je t’aime!”, repetition, and escalation to “je t’adore” intensify that avowal but do not independently show a commitment-making force or a reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the core force as an emphatic avowal. Delivery and intensification can remain contextual features without requiring E, while no undertaking or residual non-T/P/E force is evident.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-97b0baa4e5cf",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "The highlighted “je t’aime” is an emphatic avowal presenting the speaker’s love as true. The exclamative “Si je t’aime!”, repetition, and escalation to “je t’adore” intensify that avowal but do not independently show a commitment-making force or a reflex-like expressive discharge.",
    "ambiguity": "The fragment does not identify the speaker or broader conversational motive, but that uncertainty does not materially affect the dominant truth-conditional force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly represented spoken declaration, specifically the first occurrence of “je t’aime” in the repeated exclamative sequence."
  },
  "contextual_interpretation": "The French exclamative construction “Si je t’aime!” strongly affirms love, and its immediate repetition followed by “mais je t’adore, mon amour” heightens and amplifies the declaration. Nothing in the supplied fragment establishes that the words undertake a relational commitment, and intensity alone does not warrant expressive/reflexive classification.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Si je t’aime! si je t’aime!”",
      "supports": "The repeated exclamative construction supports a forceful truth-conditional avowal of love; repetition and punctuation indicate emphasis but do not independently establish E.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“mais je t’adore, mon amour!”",
      "supports": "The immediate escalation from loving to adoring reinforces the interpretation of the highlighted words as an intensified declaration of an emotional state.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e3",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is a French-language match for “je t’aime” in Gustave Flaubert’s Madame Bovary.",
      "supports": "Confirms the linguistic and literary identification of the highlighted core utterance.",
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
    "diagnosis": "T naturally captures the core force as an emphatic avowal. Delivery and intensification can remain contextual features without requiring E, while no undertaking or residual non-T/P/E force is evident.",
    "candidate_recurrent_dimension": null
  },
  "notes": "Classification is limited to the highlighted first occurrence, interpreted within its short repeated sequence."
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-b0502164917d\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The highlighted “je t’aime” is an emphatic avowal of a loving state, reinforced by its repetition and by “mais je t’adore, mon amour.” It contains no substantial relational undertaking. Although the delivery is highly exclamatory, the supplied text gives no independent evidence that the words are a reflex-like affective discharge rather than an intensely expressed assertion.
- **Ontology fit:** natural — T naturally captures the central avowal. The turn’s rhetorical intensity can remain contextual delivery information; there is no residual core force requiring E or O, and no explicit undertaking supporting P.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-b0502164917d",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.93,
    "analysis": "The highlighted “je t’aime” is an emphatic avowal of a loving state, reinforced by its repetition and by “mais je t’adore, mon amour.” It contains no substantial relational undertaking. Although the delivery is highly exclamatory, the supplied text gives no independent evidence that the words are a reflex-like affective discharge rather than an intensely expressed assertion.",
    "ambiguity": "The narrow excerpt does not establish the speaker’s sincerity or immediate conversational motive, but either uncertainty is compatible with a predominantly truth-conditional classification."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Direct dialogue representing a character’s spoken declaration; the highlighted occurrence is the first “je t’aime” in a repeated, escalating turn."
  },
  "contextual_interpretation": "The construction “Si je t’aime!” reads as an emphatic response or confirmation, approximately “Do I love you!/Indeed I love you,” followed by repetition and the stronger “je t’adore.” This supports forceful reassurance or avowal. Repetition, exclamation marks, and the endearment intensify the delivery but do not independently establish expressive/reflexive force or a commitment.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Si je t’aime! si je t’aime!”",
      "supports": "The repeated first-person love predication strongly supports truth-conditional avowal; its punctuation and repetition indicate emphasis but do not by themselves support E.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“mais je t’adore, mon amour!”",
      "supports": "The escalation from loving to adoring and the direct endearment reinforce the avowal and intimate reassurance, without specifying an undertaking or obligation.",
      "confidence": 0.96
    },
    {
      "evidence_id": "e3",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is extracted as French dialogue from Gustave Flaubert’s Madame Bovary.",
      "supports": "Confirms that the phrase is represented within a literary dialogue context rather than supplied as an isolated grammatical example.",
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
    "diagnosis": "T naturally captures the central avowal. The turn’s rhetorical intensity can remain contextual delivery information; there is no residual core force requiring E or O, and no explicit undertaking supporting P.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The classification concerns the highlighted first occurrence while treating the immediately repeated declaration and escalation as evidence from the same speech turn."
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-5396f984c871\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** The direct declaration “je vous aime” primarily avows a loving emotional state. Its placement after a plea to remain gives it a weak relational or commitment-invoking force, but it does not itself clearly undertake an obligation. The exclamation and urgency indicate intensity, not independently expressive/reflexive core force.
- **Ontology fit:** natural — T captures the avowal, while a small P score captures its limited use in pressing a relational appeal. Delivery and urgency can be handled contextually without E or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-5396f984c871",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.9,
    "analysis": "The direct declaration “je vous aime” primarily avows a loving emotional state. Its placement after a plea to remain gives it a weak relational or commitment-invoking force, but it does not itself clearly undertake an obligation. The exclamation and urgency indicate intensity, not independently expressive/reflexive core force.",
    "ambiguity": "The narrow excerpt does not establish whether the avowal is sincere or strategically intended to prevent departure, but either reading remains principally truth-conditional in mode."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A character directly addresses another in represented dialogue: “De grâce, restez! je vous aime!”"
  },
  "contextual_interpretation": "The love avowal follows and reinforces an urgent request that the addressee stay. It may therefore function persuasively or as reassurance, but the local text does not show a distinct promise, relational undertaking, or reflex-like loss of verbal control. Sincerity and broader motives remain unresolved by the supplied excerpt.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“je vous aime!”",
      "supports": "The conventional first-person declaration directly presents the speaker's love as true, strongly supporting T.",
      "confidence": 0.98
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "“De grâce, restez!” immediately precedes the declaration.",
      "supports": "The avowal is used to support an urgent plea that the addressee remain, giving limited support to relational invocation but not a clear undertaking.",
      "confidence": 0.94
    },
    {
      "evidence_id": "local-3",
      "source": "local_text",
      "quotation_or_description": "The utterance is exclamatory and occurs in an urgent appeal.",
      "supports": "This establishes emotional intensity and emphatic delivery, but supplies no independent evidence that the words are a reflex-like expressive discharge.",
      "confidence": 0.92
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
    "diagnosis": "T captures the avowal, while a small P score captures its limited use in pressing a relational appeal. Delivery and urgency can be handled contextually without E or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "Classification is intentionally based only on the short supplied passage and metadata, without identifying the speaker or importing wider plot context."
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

- **Selected attempt:** `results\batch_runs\development_three\v0.3.1-5.6\texts\gutenberg-14155\annotations\flaubert-madame-bovary-1e7d6742e45b\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 2 / 0 / 0
- **Core analysis:** “Je t’aime” primarily avows a present loving state. In this apologetic sequence, the adjacent promise of lasting love gives the avowal some commitment-renewing force, though it does not clearly constitute a full relational undertaking. The exclamations and emotional urgency indicate intense delivery but provide no independent evidence that the words are a reflex-like affective discharge.
- **Ontology fit:** natural — T naturally captures the central avowal, while P captures the limited commitment pressure created by the apology and assurance of lasting love. Delivery intensity can remain contextual, so neither E nor O is required.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-1e7d6742e45b",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 2,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.91,
    "analysis": "“Je t’aime” primarily avows a present loving state. In this apologetic sequence, the adjacent promise of lasting love gives the avowal some commitment-renewing force, though it does not clearly constitute a full relational undertaking. The exclamations and emotional urgency indicate intense delivery but provide no independent evidence that the words are a reflex-like affective discharge.",
    "ambiguity": "The degree of performative force is uncertain: “je t’aimerai toujours” may be either a pledge of constancy or an emphatic prediction/reassurance about continued feeling."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A character directly addresses another with “Je t’aime” as part of an apology and attempted reassurance."
  },
  "contextual_interpretation": "The speaker seeks forgiveness, admits having been foolish and cruel, asserts the addressee’s uniqueness, avows present love, and promises continued love. This framing makes the utterance both an assertion of feeling and, to a lesser extent, an attempt to repair or reaffirm the relationship. The excerpt alone does not establish whether the avowal is sincere, strategic, or self-deceived, but those possibilities do not alter its presented T/P force.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Je t’aime”",
      "supports": "Directly presents the speaker’s current love as true, strongly supporting truth-conditional force.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“pardonne-moi! … J’ai été imbécile et méchant!”",
      "supports": "Frames the avowal as part of an apology and attempted relational repair, lending some support to performative force.",
      "confidence": 0.94
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“tu es la seule qui me plaise”",
      "supports": "Reinforces the avowal by asserting the addressee’s unique emotional importance.",
      "confidence": 0.96
    },
    {
      "evidence_id": "e4",
      "source": "local_text",
      "quotation_or_description": "“je t’aimerai toujours!”",
      "supports": "Adds an assurance or possible pledge of enduring love, supporting moderate rather than merely present-state force.",
      "confidence": 0.96
    },
    {
      "evidence_id": "e5",
      "source": "local_text",
      "quotation_or_description": "The passage uses repeated exclamation marks and urgent questions, including “Qu’as-tu? dis-le donc!”",
      "supports": "Shows emotional urgency, but does not independently establish expressive/reflexive core force.",
      "confidence": 0.93
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
    "diagnosis": "T naturally captures the central avowal, while P captures the limited commitment pressure created by the apology and assurance of lasting love. Delivery intensity can remain contextual, so neither E nor O is required.",
    "candidate_recurrent_dimension": null
  },
  "notes": "Classification is based on the supplied local excerpt and metadata, without relying on wider plot context."
}
```

</details>
