# Single-text pipeline report: Madame Bovary

## Run summary

- **Run ID:** `20260902T043409Z`
- **Work:** *Madame Bovary* by Gustave Flaubert
- **Source:** `gutenberg-14155`
- **Annotation:** v0.2 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 12
- **Valid occurrences:** 12
- **Failed/invalid attempts:** 0
- **Estimated total cost:** USD 1.031936

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

- **Selected attempt:** `results\pipeline_runs\gutenberg-14155\20260902T043409Z\annotations\flaubert-madame-bovary-47361213aeaa\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 1 / 1
- **Core analysis:** The declarative “je vous aime” straightforwardly presents the speaker's love as true, reinforced by “voilà tout,” which frames love as the simple and sufficient explanation. It does not itself clearly undertake a durable obligation or relational commitment. The exclamation and urgent continuation add emotional intensity, but the utterance retains strong propositional force rather than functioning principally as a reflexive cry.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal, reassurance, elicitation_of_reaffirmation, pressure, manipulation
- **Current-act analysis:** The speaker directly avows love and insists that the addressee should not doubt it. “Dites-le-moi; un mot! un seul mot!” urgently solicits verbal confirmation that she believes or accepts the avowal, rather than clearly asking her to avow her own love. The repeated imperatives and narrowing demand for even one word exert pressure. Knowledge of Rodolphe's calculated seduction of Emma supports interpreting this pressure as manipulative, although that does not turn the core proposition into a performative commitment.
- **Contextual modification:** strengthens, weakens, manipulates
- **Ontology adequate:** True — The scheme naturally separates the avowal's strong truth-conditional form from its pressured and manipulative present use and from the wider narrative weakening of its credibility. The main residual complexity is that sincerity is scalar: Rodolphe may feel attraction while misrepresenting it as deeper or more durable love.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-47361213aeaa",
  "core_love_content": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 1
    },
    "mixed_reading": {
      "is_mixed": false,
      "basis": "none",
      "justification": null
    },
    "relationship_modifier": "An avowal in an extramarital courtship and seduction, addressed by Rodolphe to Emma.",
    "analysis": "The declarative “je vous aime” straightforwardly presents the speaker's love as true, reinforced by “voilà tout,” which frames love as the simple and sufficient explanation. It does not itself clearly undertake a durable obligation or relational commitment. The exclamation and urgent continuation add emotional intensity, but the utterance retains strong propositional force rather than functioning principally as a reflexive cry.",
    "confidence": 0.96
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The dash introduces words currently uttered by a character in the fictional scene. Nothing in the supplied text indicates quotation of an earlier utterance, writing, imagination, negation, or metalinguistic mention.",
    "confidence": 0.97
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "reassurance",
      "elicitation_of_reaffirmation",
      "pressure",
      "manipulation"
    ],
    "other_description": null,
    "analysis": "The speaker directly avows love and insists that the addressee should not doubt it. “Dites-le-moi; un mot! un seul mot!” urgently solicits verbal confirmation that she believes or accepts the avowal, rather than clearly asking her to avow her own love. The repeated imperatives and narrowing demand for even one word exert pressure. Knowledge of Rodolphe's calculated seduction of Emma supports interpreting this pressure as manipulative, although that does not turn the core proposition into a performative commitment.",
    "confidence": 0.88
  },
  "contextual_modification": {
    "effects": [
      "strengthens",
      "weakens",
      "manipulates"
    ],
    "other_description": null,
    "analysis": "Locally, “voilà tout,” the denial of possible doubt, the exclamation marks, and the demand for an answer rhetorically strengthen the avowal's urgency and apparent certainty. In the wider novel, Rodolphe's calculated pursuit and eventual abandonment of Emma weaken the credibility of the claim as an avowal of deep or durable love. The immediate demand for confirmation also uses the love-content to press Emma toward emotional acquiescence.",
    "confidence": 0.86
  },
  "participant_construals": [
    {
      "role": "original_avower_and_current_speaker_Rodolphe",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Rodolphe presents his love as a simple, certain fact and seeks an immediate acknowledgment from Emma. The wider characterization of his courtship indicates that this presentation is also serving his seduction strategy.",
      "confidence": 0.88
    },
    {
      "role": "current_addressee_Emma",
      "discourse_level": "both",
      "status": "unavailable",
      "analysis": "The excerpt contains Rodolphe's assertion about Emma's presumed lack of doubt, but it does not include Emma's response or independently establish how she construes either his sincerity or his demand at this moment.",
      "confidence": null
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Across the wider work, Rodolphe's calculated approach to seducing Emma and his later conduct invite critical distance from the avowal's surface sincerity and durability.",
      "confidence": 0.84
    },
    {
      "role": "informed_reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "A reader using the wider characterization can recognize a genuine grammatical avowal whose credibility and relational implications are compromised by Rodolphe's strategic motives and limited commitment.",
      "confidence": 0.87
    }
  ],
  "disagreements": [
    {
      "parties": [
        "original_avower_and_current_speaker_Rodolphe",
        "narrator_or_text"
      ],
      "subject": "Sincerity and durability of the professed love",
      "description": "Rodolphe's present wording frames love as an uncomplicated and certain truth, while the wider narrative characterization encourages doubt that it represents deep, durable, or committed love rather than attraction deployed in a calculated seduction.",
      "evidence_ids": [
        "E1",
        "E2",
        "E5"
      ],
      "confidence": 0.82
    }
  ],
  "assessments": {
    "deception_misrepresentation": {
      "status": "supported",
      "analysis": "Rodolphe appears attracted to Emma, so the evidence does not require the conclusion that every feeling is fabricated. Nevertheless, his calculated seduction and later abandonment support the narrower claim that the unqualified profession misrepresents the depth, durability, or commitment of his attachment.",
      "confidence": 0.8
    },
    "manipulation_pressure": {
      "status": "supported",
      "analysis": "The local imperatives demand an immediate validating response—“Dites-le-moi; un mot! un seul mot!”—and the wider courtship context supports treating this urgency as part of Rodolphe's manipulative seduction.",
      "confidence": 0.91
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "The central proposition is linguistically explicit rather than strategically equivocal: the speaker says directly that he loves the addressee. Although “love” leaves the degree and practical implications of commitment unspecified, the available evidence more strongly supports exaggeration and manipulation than a deliberate reliance on semantic ambiguity.",
      "confidence": 0.76
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“Non, je vous aime, voilà tout!”",
      "supports": "A direct, emphatic truth-conditional avowal framed as the speaker's simple and sufficient explanation.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“Vous n’en doutez pas! Dites-le-moi; un mot! un seul mot!”",
      "supports": "The speaker presumes or urges belief in the avowal and pressures the addressee to provide immediate verbal confirmation.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "The passage uses a dialogue dash, direct first- and second-person forms, exclamation marks, and imperatives.",
      "supports": "Direct spoken realization and heightened emotional and interpersonal urgency.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as coming from Gustave Flaubert's Madame Bovary in the supplied Project Gutenberg source.",
      "supports": "Identification of the work to which the remembered characterization and plot context apply.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E5",
      "source": "background_knowledge",
      "quotation_or_description": "In the wider novel, Rodolphe approaches Emma as an experienced and calculating seducer; their affair does not become a durable commitment, and he eventually abandons their plan to elope.",
      "supports": "Identification of the speaker and addressee, critical distance from the avowal's apparent depth and durability, and the assessments of manipulation and partial misrepresentation.",
      "confidence": 0.86
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "moderate",
    "confidence": 0.86,
    "contribution": "It identifies the exchange as part of Rodolphe's pursuit of Emma and supplies the broader pattern of calculated seduction and eventual abandonment. This does not alter the core linguistic classification as an avowal, but it materially weakens credibility and supports the manipulation and misrepresentation assessments.",
    "notes": "The broad relationship and plot trajectory are remembered confidently. Because the supplied excerpt is very short and does not name either participant, exact placement within the courtship scene is less certain than the interpretation of Rodolphe's general motives."
  },
  "context_needs": [
    {
      "need": "useful_for_richer_interpretation",
      "layers": [
        "current_discourse_act",
        "participant_construals",
        "disagreements",
        "assessments"
      ],
      "claim": "The exact immediate trigger for Rodolphe's denial and the way Emma receives or answers his demand.",
      "request": "Provide the preceding and following paragraphs, especially the preceding exchange and Emma's next response."
    }
  ],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The scheme naturally separates the avowal's strong truth-conditional form from its pressured and manipulative present use and from the wider narrative weakening of its credibility. The main residual complexity is that sincerity is scalar: Rodolphe may feel attraction while misrepresenting it as deeper or more durable love.",
    "proposed_missing_dimensions": [
      "A scalar sincerity dimension distinguishing total fabrication from exaggeration of emotional depth, exclusivity, durability, or commitment."
    ]
  },
  "notes": "The requested “one word” most naturally seeks confirmation that Emma does not doubt Rodolphe, not necessarily a reciprocal declaration of love. Accordingly, elicitation_of_reaffirmation is used in the broader sense of eliciting acknowledgment of the avowal."
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

- **Selected attempt:** `results\pipeline_runs\gutenberg-14155\20260902T043409Z\annotations\flaubert-madame-bovary-d0ec3752ec68\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 1 / 1
- **Core analysis:** The unqualified present-tense declaration “Je t’aime” directly presents the speaker's love as true. The exclamation mark and simultaneous embrace add emotional intensity, but the clearly articulated proposition is not merely reflexive. The avowal may affirm the existing relationship, yet it does not itself clearly undertake a new obligation or commitment, so performative support remains weak.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal
- **Current-act analysis:** The speaker currently avows love to the person denoted by “t’.” The reporting verb identifies it as a reply, but the omitted preceding turn does not establish whether it is also reassurance, an answer to elicitation, or part of some other conversational strategy.
- **Contextual modification:** preserves, strengthens
- **Ontology adequate:** True — The scheme naturally distinguishes the declaration's strong truth-conditional content from its weak commitment force and from the emotional intensification supplied by punctuation and bodily action. It also permits broader doubts about durability or self-understanding to be recorded without falsely classifying the utterance as deceptive.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-d0ec3752ec68",
  "core_love_content": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 1
    },
    "mixed_reading": {
      "is_mixed": false,
      "basis": "none",
      "justification": null
    },
    "relationship_modifier": "Romantic and erotic love within an intimate relationship; background knowledge tentatively identifies the avower as Emma and the addressee as Rodolphe.",
    "analysis": "The unqualified present-tense declaration “Je t’aime” directly presents the speaker's love as true. The exclamation mark and simultaneous embrace add emotional intensity, but the clearly articulated proposition is not merely reflexive. The avowal may affirm the existing relationship, yet it does not itself clearly undertake a new obligation or commitment, so performative support remains weak.",
    "confidence": 0.96
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The dash introduces dialogue, and “répondit-elle” explicitly attributes the words to a female character as her current spoken reply. This is neither a quotation of an earlier utterance nor wording supplied for nonverbal conduct.",
    "confidence": 0.99
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal"
    ],
    "other_description": null,
    "analysis": "The speaker currently avows love to the person denoted by “t’.” The reporting verb identifies it as a reply, but the omitted preceding turn does not establish whether it is also reassurance, an answer to elicitation, or part of some other conversational strategy.",
    "confidence": 0.97
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens"
    ],
    "other_description": null,
    "analysis": "Nothing in the supplied sentence hedges, negates, quotes, or distances the declaration. The exclamation and the speaker's act of putting her arms around the addressee's neck reinforce its immediate emotional and intimate force. The wider novel's treatment of romantic self-dramatization may complicate judgments about durability, but it does not cancel the locally presented avowal.",
    "confidence": 0.9
  },
  "participant_construals": [
    {
      "role": "original_avower_and_current_speaker",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The female speaker explicitly presents herself as loving the addressee and physically embraces him. The sentence supports an emotionally engaged direct avowal, although it cannot establish the long-term stability of her feeling.",
      "confidence": 0.94
    },
    {
      "role": "current_addressee",
      "discourse_level": "both",
      "status": "unavailable",
      "analysis": "The addressee is the male referent of “lui” and “t’,” but his reaction and interpretation are absent from the supplied context.",
      "confidence": null
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The narration straightforwardly attributes the utterance to the woman and coordinates it with an embrace, presenting it as an enacted moment of romantic intimacy without explicit irony or correction in the local sentence.",
      "confidence": 0.94
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "A reader can securely construe the words as a direct romantic avowal intensified by physical affection, while remaining cautious about enduring sincerity because of the novel's broader critical treatment of romantic language.",
      "confidence": 0.87
    }
  ],
  "disagreements": [],
  "assessments": {
    "deception_misrepresentation": {
      "status": "unsupported",
      "analysis": "The local text presents congruence between the spoken declaration and an affectionate embrace, with no sign that the speaker believes the declaration false. The wider novel complicates Emma's understanding and constancy of love, but that does not by itself support deliberate deception at this moment.",
      "confidence": 0.76
    },
    "manipulation_pressure": {
      "status": "unsupported",
      "analysis": "No demand, threat, leverage, or attempt to constrain the addressee is visible in the supplied sentence. Because the preceding exchange is omitted, a more elaborate strategic use cannot be wholly excluded, but there is no positive support for it here.",
      "confidence": 0.79
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "“Je t’aime” is lexically direct and unhedged, and its addressee is situationally identified by the second-person pronoun and accompanying embrace. No purposeful ambiguity is apparent.",
      "confidence": 0.92
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“Je t’aime!”",
      "supports": "The first-person present-tense sentence directly avows a loving state; the exclamation mark adds emotional intensity.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“répondit-elle”",
      "supports": "The narration identifies the declaration as a female character's currently spoken reply rather than quoted, imagined, or merely narrated content.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“en lui passant les bras autour du cou”",
      "supports": "The simultaneous embrace strengthens the declaration's immediate affectionate and intimate presentation.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is from Gustave Flaubert's Madame Bovary, at relative source position 0.46717.",
      "supports": "The work identification and approximate location permit cautious use of remembered narrative context; this description is metadata, not passage wording.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E5",
      "source": "background_knowledge",
      "quotation_or_description": "At approximately this portion of the novel, the romantic interaction is probably part of Emma Bovary's affair with Rodolphe; this scene identification is remembered with moderate rather than exact confidence.",
      "supports": "Tentatively identifies the avower and addressee and characterizes the love as romantic and erotic.",
      "confidence": 0.72
    },
    {
      "evidence_id": "E6",
      "source": "background_knowledge",
      "quotation_or_description": "The novel recurrently subjects Emma's romantic language and self-conception to critical treatment, portraying her attachments as shaped by idealized romantic scripts.",
      "supports": "Justifies caution about treating the locally sincere-seeming avowal as proof of stable or lucid long-term love, without establishing deception in this occurrence.",
      "confidence": 0.88
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "moderate",
    "confidence": 0.82,
    "contribution": "Background knowledge tentatively identifies the participants as Emma and Rodolphe and supplies the broader context of Emma's adulterous, romantically idealized attachment. It qualifies claims about durability or self-understanding but does not alter the core classification as a direct truth-conditional avowal.",
    "notes": "The participant identification at this exact source position is less certain than the general knowledge of the novel's relationships and treatment of romantic language; no exact non-local wording is asserted."
  },
  "context_needs": [
    {
      "need": "useful_for_richer_interpretation",
      "layers": [
        "current_discourse_act",
        "contextual_modification",
        "participant_construals",
        "assessments"
      ],
      "claim": "Whether the reply also functions as reassurance, answers an elicited reaffirmation, or serves a strategic purpose depends on the omitted preceding exchange and subsequent reaction.",
      "request": "Provide the dialogue immediately before and after this sentence, preferably together with the chapter heading or several surrounding paragraphs."
    }
  ],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The scheme naturally distinguishes the declaration's strong truth-conditional content from its weak commitment force and from the emotional intensification supplied by punctuation and bodily action. It also permits broader doubts about durability or self-understanding to be recorded without falsely classifying the utterance as deceptive.",
    "proposed_missing_dimensions": []
  },
  "notes": "The strongest interpretation is an emotionally intensified direct romantic avowal. The embrace corroborates affective involvement but is contextual reinforcement rather than an independent performative undertaking."
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

- **Selected attempt:** `results\pipeline_runs\gutenberg-14155\20260902T043409Z\annotations\flaubert-madame-bovary-8c91fb38ed76\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 0 / 3
- **Core analysis:** “Comme je t’aime” explicitly presents the speaker’s love as true. Its repetition and exclamative syntax make it an intense outpouring rather than a neutral report. Nothing in the passage indicates that the words undertake or renew a distinct commitment or obligation.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal, reassurance
- **Current-act analysis:** The mother directly avows her love. Her rush to embrace the addressee and the compassionate address “ma pauvre enfant” also make the utterance consoling or reassuring, although the limited excerpt does not identify the precise distress being answered.
- **Contextual modification:** preserves, strengthens
- **Ontology adequate:** True — The scheme naturally captures the combination of explicit emotional avowal, exclamatory intensity, direct speech, reassurance, and strengthening nonverbal context. The open relationship modifier adequately records the maternal dimension.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-8c91fb38ed76",
  "core_love_content": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 3
    },
    "mixed_reading": {
      "is_mixed": true,
      "basis": "substantial_multiple_support",
      "justification": "The mother strongly avows love as an existing emotional state, while the repeated exclamative construction, physical rush to embrace, and exclamation marks give the utterance substantial emotionally triggered, exclamatory force."
    },
    "relationship_modifier": "Maternal or quasi-maternal familial love toward someone addressed as “ma pauvre enfant.”",
    "analysis": "“Comme je t’aime” explicitly presents the speaker’s love as true. Its repetition and exclamative syntax make it an intense outpouring rather than a neutral report. Nothing in the passage indicates that the words undertake or renew a distinct commitment or obligation.",
    "confidence": 0.97
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The words occur as the mother’s present fictional-world speech, continuous with the dialogue introduced by “dit sa mère.” They are neither a quotation of an earlier avowal nor wording narratively supplied for nonverbal conduct.",
    "confidence": 0.99
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "reassurance"
    ],
    "other_description": null,
    "analysis": "The mother directly avows her love. Her rush to embrace the addressee and the compassionate address “ma pauvre enfant” also make the utterance consoling or reassuring, although the limited excerpt does not identify the precise distress being answered.",
    "confidence": 0.93
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens"
    ],
    "other_description": null,
    "analysis": "The immediate context preserves the literal avowal and intensifies it through repetition, exclamation, the degree construction “Comme,” the affectionate-pitying address “ma pauvre enfant,” and the congruent act of rushing forward to embrace the addressee.",
    "confidence": 0.98
  },
  "participant_construals": [
    {
      "role": "original_avower_mother",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "She presents herself as intensely loving the addressee and uses that avowal in an affectionate, consoling encounter reinforced by an embrace.",
      "confidence": 0.97
    },
    {
      "role": "current_addressee_child_or_daughter-figure",
      "discourse_level": "both",
      "status": "unavailable",
      "analysis": "The excerpt supplies no response or internal perspective from the person addressed as “ma pauvre enfant,” so her interpretation of the avowal cannot be established.",
      "confidence": null
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The text frames the speech with emotionally congruent physical action—rushing forward to embrace—without locally introducing irony, distance, or contradiction.",
      "confidence": 0.96
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "On the supplied evidence, a reader is strongly licensed to construe the words as a sincere-seeming, emotionally heightened maternal avowal and reassurance.",
      "confidence": 0.94
    }
  ],
  "disagreements": [],
  "assessments": {
    "deception_misrepresentation": {
      "status": "unsupported",
      "analysis": "The words, repetition, compassionate address, and accompanying embrace are mutually congruent; the available passage supplies no indication that the mother is knowingly misrepresenting her feelings.",
      "confidence": 0.91
    },
    "manipulation_pressure": {
      "status": "unsupported",
      "analysis": "The current use appears affectionate and consoling rather than designed to compel a response or action. Emotional intensity alone does not establish pressure or manipulation.",
      "confidence": 0.92
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "The love-content is explicit and emphatically repeated, with no evident strategic equivocation about the speaker’s claimed feeling.",
      "confidence": 0.97
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“Comme je t’aime, ma pauvre enfant! comme je t’aime!”",
      "supports": "Explicit truth-conditional avowal of love; repetition, degree-exclamative syntax, and punctuation support strong exclamatory force and affectionate reassurance.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“dit sa mère”",
      "supports": "Identifies the speaker as the addressee’s mother or maternal figure and marks the passage as represented spoken dialogue.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“se précipitant pour l’embrasser”",
      "supports": "The rush to embrace strengthens the affectionate and emotionally immediate interpretation of the spoken avowal.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "The address “ma pauvre enfant” combines familial endearment with concern or pity.",
      "supports": "Supports the maternal relationship modifier and the consoling or reassuring function of the current discourse act.",
      "confidence": 0.96
    },
    {
      "evidence_id": "E5",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as French dialogue from Gustave Flaubert’s Madame Bovary.",
      "supports": "Establishes the work, language, and fictional literary context without adding claims about the immediate participants.",
      "confidence": 1.0
    }
  ],
  "background_knowledge": {
    "used": false,
    "familiarity": "moderate",
    "confidence": null,
    "contribution": null,
    "notes": "The local excerpt is sufficient for the core classification. Wider-work memory was not used to identify the mother and addressee because the short extract does not securely resolve their identities."
  },
  "context_needs": [
    {
      "need": "useful_for_richer_interpretation",
      "layers": [
        "current_discourse_act",
        "participant_construals",
        "assessments"
      ],
      "claim": "The identities of the mother and addressee, the cause of the addressee’s apparent distress, and the larger relational history could refine whether the reassurance has additional irony or interpersonal complexity.",
      "request": "Provide the surrounding paragraphs or chapter context identifying the participants and the event prompting the embrace."
    }
  ],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The scheme naturally captures the combination of explicit emotional avowal, exclamatory intensity, direct speech, reassurance, and strengthening nonverbal context. The open relationship modifier adequately records the maternal dimension.",
    "proposed_missing_dimensions": []
  },
  "notes": "The two occurrences of “comme je t’aime” form one repeated, escalating avowal. The highlighted match is therefore best interpreted together with its immediate repetition."
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

- **Selected attempt:** `results\pipeline_runs\gutenberg-14155\20260902T043409Z\annotations\flaubert-madame-bovary-06903c63a2d7\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 0 / 3
- **Core analysis:** “Comme je t’aime!” presents the mother's love as true with maximal directness. Its exclamative syntax and repetition make it substantially expressive or reflex-like, but do not erase its clear propositional content. It does not undertake a new commitment or obligation.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal
- **Current-act analysis:** The mother directly avows her love to the child. The exclamation, repetition, affectionate vocative, and accompanying attempt to kiss her intensify the avowal; the limited context does not firmly establish a separate act such as reassurance.
- **Contextual modification:** preserves, strengthens
- **Ontology adequate:** True — The scheme naturally captures the important combination of propositional avowal and affective exclamation, while separating that combination from performative commitment and from contextual intensification by repetition and kissing.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-06903c63a2d7",
  "core_love_content": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 3
    },
    "mixed_reading": {
      "is_mixed": true,
      "basis": "substantial_multiple_support",
      "justification": "The mother clearly avows that she loves the child, while the exclamative construction, immediate repetition, and impulsive movement to kiss her independently support an emotionally triggered outburst."
    },
    "relationship_modifier": "Maternal love, colored by tenderness and compassion toward the addressed “pauvre enfant.”",
    "analysis": "“Comme je t’aime!” presents the mother's love as true with maximal directness. Its exclamative syntax and repetition make it substantially expressive or reflex-like, but do not erase its clear propositional content. It does not undertake a new commitment or obligation.",
    "confidence": 0.98
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The narrator's speech tag, “dit sa mère,” represents the mother as currently speaking the quoted words in the fictional world. This is neither a citation of an earlier utterance nor narration that merely supplies words for nonverbal behavior.",
    "confidence": 0.99
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal"
    ],
    "other_description": null,
    "analysis": "The mother directly avows her love to the child. The exclamation, repetition, affectionate vocative, and accompanying attempt to kiss her intensify the avowal; the limited context does not firmly establish a separate act such as reassurance.",
    "confidence": 0.97
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens"
    ],
    "other_description": null,
    "analysis": "Direct represented speech preserves the love-content without quotation, negation, or distancing. Repetition and the congruent action of rushing to kiss the child strengthen its emotional intensity and apparent sincerity.",
    "confidence": 0.96
  },
  "participant_construals": [
    {
      "role": "original_avower_and_current_speaker: the mother",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Her words construe the content as a sincere, intensely felt maternal avowal, and her rush to kiss the child behaviorally aligns with that presentation.",
      "confidence": 0.96
    },
    {
      "role": "current_addressee: the mother's child",
      "discourse_level": "both",
      "status": "unavailable",
      "analysis": "The child is explicitly addressed through “t’” and “ma pauvre enfant,” but the supplied passage contains no response or evidence of how she understands or receives the avowal.",
      "confidence": null
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The narration frames the utterance as direct speech and places it alongside an affectionate physical action, presenting it as an emotionally intense maternal avowal without explicit irony or challenge.",
      "confidence": 0.94
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "On the supplied evidence, a reader can naturally construe the words as both a genuine assertion of maternal love and an affective exclamation.",
      "confidence": 0.95
    }
  ],
  "disagreements": [],
  "assessments": {
    "deception_misrepresentation": {
      "status": "unsupported",
      "analysis": "Nothing in the passage indicates that the mother is falsely representing her feelings; her movement to kiss the child is congruent with the avowal.",
      "confidence": 0.92
    },
    "manipulation_pressure": {
      "status": "unsupported",
      "analysis": "The imperative concerns bringing the child to the mother, but the love-avowal itself is not used here to demand reciprocation, impose an obligation, or exert identifiable pressure.",
      "confidence": 0.9
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "The repeated formulation is direct and emphatic rather than strategically equivocal about either the emotion or its addressee.",
      "confidence": 0.96
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“Comme je t’aime, ma pauvre enfant! comme je t’aime!”",
      "supports": "The mother explicitly and repeatedly presents her love for the addressed child as true; the exclamative form also supports an emotionally expressive reading.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“dit sa mère”",
      "supports": "Identifies the speaker as the child's mother and establishes the occurrence as direct represented spoken speech.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "The mother is described as “se précipitant pour l’embrasser.”",
      "supports": "The impulsive attempt to kiss the child strengthens the reading of intense affection and provides behavior congruent with the avowal.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "The avowal occurs twice in immediate succession, with the vocative “ma pauvre enfant.”",
      "supports": "Repetition and the compassionate maternal address strengthen the exclamatory force and characterize the love as tender maternal affection.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E5",
      "source": "supplied_metadata",
      "quotation_or_description": "The supplied metadata identifies the work as Gustave Flaubert's French-language novel Madame Bovary.",
      "supports": "Establishes the bibliographic source and fictional-narrative context; it does not independently determine the local utterance's sincerity or function.",
      "confidence": 0.99
    }
  ],
  "background_knowledge": {
    "used": false,
    "familiarity": "moderate",
    "confidence": null,
    "contribution": null,
    "notes": "The local passage is sufficient for the core classification. No remembered non-local plot event was used to identify the mother and child or to infer irony, deception, or later consequences."
  },
  "context_needs": [
    {
      "need": "useful_for_richer_interpretation",
      "layers": [
        "current_discourse_act",
        "participant_construals",
        "assessments"
      ],
      "claim": "Whether the avowal specifically functions as consolation or reassurance, and how the child receives it.",
      "request": "Provide the surrounding paragraph or scene, especially the event prompting “ma pauvre enfant” and the child's subsequent response."
    }
  ],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The scheme naturally captures the important combination of propositional avowal and affective exclamation, while separating that combination from performative commitment and from contextual intensification by repetition and kissing.",
    "proposed_missing_dimensions": []
  },
  "notes": "The classification applies to the highlighted second “je t’aime,” interpreted in light of the immediately preceding identical avowal. The repetition is intensifying rather than quotation-revoicing."
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

- **Selected attempt:** `results\pipeline_runs\gutenberg-14155\20260902T043409Z\annotations\flaubert-madame-bovary-fc563b7babfd\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 0 / 1
- **Core analysis:** The embedded clause “je t’aime” clearly presents the speaker's love as true. “Tu sais bien que” frames that proposition as something the addressee already knows, strengthening its assertive and reassuring presentation. The exclamation mark and surrounding agitation add emotional intensity, but the grammatically explicit proposition remains primary. Nothing here substantially undertakes or renews a relational commitment.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal, reassurance, pressure
- **Current-act analysis:** The speaker directly affirms that he loves the addressee, while “Tu sais bien” makes the affirmation a reminder or reassurance rather than entirely new information. In the sequence “Calme-toi! reprends-toi!... Tu sais bien que je t’aime! ... viens!”, the avowal also supports directives asking the distressed addressee to regain control and come with him. This creates some immediate interpersonal pressure, although it does not by itself establish manipulation.
- **Contextual modification:** preserves, strengthens, redirects
- **Ontology adequate:** False — The layered scheme otherwise gives a natural account of the avowal, its direct spoken realization, and its reassuring yet directive use. However, the combined assessment field “manipulation_pressure” prevents fully independent assessment of two importantly different claims: local pressure is supported, while calculated manipulation remains unestablished.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-fc563b7babfd",
  "core_love_content": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 1
    },
    "mixed_reading": {
      "is_mixed": false,
      "basis": "none",
      "justification": null
    },
    "relationship_modifier": null,
    "analysis": "The embedded clause “je t’aime” clearly presents the speaker's love as true. “Tu sais bien que” frames that proposition as something the addressee already knows, strengthening its assertive and reassuring presentation. The exclamation mark and surrounding agitation add emotional intensity, but the grammatically explicit proposition remains primary. Nothing here substantially undertakes or renews a relational commitment.",
    "confidence": 0.97
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The love-content occurs within ongoing character dialogue introduced by a speech dash and accompanied by “répétait-il.” It is represented as presently spoken in the fictional world, not as a quotation of an earlier or hypothetical avowal.",
    "confidence": 0.98
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "reassurance",
      "pressure"
    ],
    "other_description": null,
    "analysis": "The speaker directly affirms that he loves the addressee, while “Tu sais bien” makes the affirmation a reminder or reassurance rather than entirely new information. In the sequence “Calme-toi! reprends-toi!... Tu sais bien que je t’aime! ... viens!”, the avowal also supports directives asking the distressed addressee to regain control and come with him. This creates some immediate interpersonal pressure, although it does not by itself establish manipulation.",
    "confidence": 0.89
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens",
      "redirects"
    ],
    "other_description": null,
    "analysis": "The context preserves the ordinary propositional content of loving someone. “Tu sais bien” strengthens its presentation by presupposing that the love is already known, while the surrounding calming commands and final “viens!” redirect the avowal toward reassurance and securing an immediate behavioral response.",
    "confidence": 0.9
  },
  "participant_construals": [
    {
      "role": "current_speaker_and_original_avower",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "He presents his love as an established fact and deploys that assertion while attempting to calm and direct the addressee.",
      "confidence": 0.95
    },
    {
      "role": "current_addressee",
      "discourse_level": "both",
      "status": "unavailable",
      "analysis": "The supplied passage does not provide her response or indicate whether she accepts the love claim, experiences it as reassurance, or resists the accompanying directives.",
      "confidence": null
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "current_discourse_act",
      "status": "supported",
      "analysis": "The narration represents the man as astonished and repeatedly reacting to the addressee's condition, placing the avowal within an urgent effort to calm her.",
      "confidence": 0.93
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "uncertain",
      "analysis": "A reader can securely recognize an avowal used as reassurance and in support of directives, but the short extract does not settle whether the professed love is sincere or self-serving.",
      "confidence": 0.88
    }
  ],
  "disagreements": [],
  "assessments": {
    "deception_misrepresentation": {
      "status": "uncertain_not_assessable",
      "analysis": "The speaker unequivocally represents himself as loving the addressee, but the extract supplies no reliable access to his actual feelings or prior conduct from which deception could be inferred.",
      "confidence": 0.94
    },
    "manipulation_pressure": {
      "status": "supported",
      "analysis": "Immediate pressure is supported by the imperatives “Calme-toi,” “reprends-toi,” and “viens,” with the love claim functioning as reassurance in that directive sequence. The evidence supports pressure more clearly than calculated manipulation.",
      "confidence": 0.76
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "The proposition “je t’aime” is direct and unhedged. Although sincerity remains unknown, there is no local evidence that the speaker strategically exploits ambiguity in the wording.",
      "confidence": 0.9
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“je t’aime”",
      "supports": "The clause explicitly presents the speaker's loving emotional state as true.",
      "confidence": 1.0
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“Tu sais bien que je t’aime!”",
      "supports": "The knowledge construction treats the love as already established for the addressee and gives the avowal a reassuring, reminding function.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“Calme-toi! reprends-toi!...”",
      "supports": "The avowal occurs during an urgent attempt to regulate or calm the addressee.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "“... viens!”",
      "supports": "The avowal is followed by a directive, supporting the interpretation that reassurance is also being used to obtain an immediate response.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E5",
      "source": "local_text",
      "quotation_or_description": "“Qu’as-tu? qu’as-tu? répétait-il stupéfait.”",
      "supports": "The narrator frames the male speaker as astonished and reacting repeatedly to the addressee's apparent distress.",
      "confidence": 0.96
    },
    {
      "evidence_id": "E6",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as dialogue in Gustave Flaubert's French novel Madame Bovary.",
      "supports": "This establishes the literary work and language without resolving the identities, sincerity, or wider circumstances of this particular exchange.",
      "confidence": 1.0
    }
  ],
  "background_knowledge": {
    "used": false,
    "familiarity": "moderate",
    "confidence": null,
    "contribution": null,
    "notes": "General familiarity with Madame Bovary was not used to identify this specific exchange because the short extract and supplied location do not support a sufficiently reliable identification of the participants or episode."
  },
  "context_needs": [
    {
      "need": "useful_for_richer_interpretation",
      "layers": [
        "current_discourse_act",
        "contextual_modification",
        "participant_construals",
        "assessments"
      ],
      "claim": "Whether the reassurance is sincere, coercive, or calculated, and how the addressee construes it.",
      "request": "Provide the surrounding scene, especially the cause of the addressee's distress, the participants' identities, their preceding exchange, and her response after “viens!”"
    }
  ],
  "ontology_assessment": {
    "adequate": false,
    "diagnosis": "The layered scheme otherwise gives a natural account of the avowal, its direct spoken realization, and its reassuring yet directive use. However, the combined assessment field “manipulation_pressure” prevents fully independent assessment of two importantly different claims: local pressure is supported, while calculated manipulation remains unestablished.",
    "proposed_missing_dimensions": [
      "Separate assessment fields for manipulation and interpersonal pressure.",
      "An optional field distinguishing presupposed or reminder-like avowals from presentation as new information."
    ]
  },
  "notes": "The classification of pressure concerns the present directive sequence and does not make the core love-content performative. Sincerity and the addressee's uptake remain open."
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

- **Selected attempt:** `results\pipeline_runs\gutenberg-14155\20260902T043409Z\annotations\flaubert-madame-bovary-8fe83e2776a5\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 0 / 1
- **Core analysis:** The unqualified first-person present statement “je t’aime” explicitly presents the male speaker's love for the addressee as true. Its exclamation mark and the emphatic response “Mais oui” add emotional or impatient emphasis, but the utterance remains a clear proposition rather than a predominantly reflexive cry. It reassures the addressee but does not itself undertake a sufficiently definite commitment to warrant performative support. Possible insincerity affects the credibility of the assertion, not its core truth-conditional form.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal, reassurance
- **Current-act analysis:** The speaker directly avows love while answering an explicit or implicit doubt. “Mais oui” makes the reply strongly reassuring, though its briskness may also suggest impatience or formulaic placation. The supplied fragment does not independently establish that the present act is coercive or manipulative.
- **Contextual modification:** preserves, weakens, distances
- **Ontology adequate:** True — The scheme naturally separates the utterance's explicit truth-conditional love-content from its reassuring discourse function and contextually weakened sincerity. A minor limitation is that it has no dedicated field for aspectual framing such as a potentially iterative or habitual imperfect speech tag, which could matter if wider context showed this to be a recurring response rather than a single exchange.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-8fe83e2776a5",
  "core_love_content": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 1
    },
    "mixed_reading": {
      "is_mixed": false,
      "basis": "none",
      "justification": null
    },
    "relationship_modifier": "Romantic love within an adulterous affair, likely Rodolphe's relationship with Emma.",
    "analysis": "The unqualified first-person present statement “je t’aime” explicitly presents the male speaker's love for the addressee as true. Its exclamation mark and the emphatic response “Mais oui” add emotional or impatient emphasis, but the utterance remains a clear proposition rather than a predominantly reflexive cry. It reassures the addressee but does not itself undertake a sufficiently definite commitment to warrant performative support. Possible insincerity affects the credibility of the assertion, not its core truth-conditional form.",
    "confidence": 0.96
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The words are presented as dialogue spoken by a male character, explicitly attributed by “répondait-il.” They are not merely mentioned, imagined, negated, or quoted from an earlier utterance.",
    "confidence": 0.98
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "reassurance"
    ],
    "other_description": null,
    "analysis": "The speaker directly avows love while answering an explicit or implicit doubt. “Mais oui” makes the reply strongly reassuring, though its briskness may also suggest impatience or formulaic placation. The supplied fragment does not independently establish that the present act is coercive or manipulative.",
    "confidence": 0.9
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "weakens",
      "distances"
    ],
    "other_description": null,
    "analysis": "Direct representation and the speech tag preserve the literal avowal as something the character says. At the same time, the responsive “Mais oui” can make it sound routine or impatient rather than spontaneous. Background knowledge of Flaubert's broader portrayal of Rodolphe as increasingly cynical and emotionally disengaged from Emma further weakens the avowal's credibility and creates narratorial or readerly distance from its face value.",
    "confidence": 0.78
  },
  "participant_construals": [
    {
      "role": "original_avower_and_current_speaker",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The male speaker presents himself without qualification as loving the addressee and uses that assertion as an affirmative response. His actual inward sincerity is less secure than the explicit self-presentation.",
      "confidence": 0.94
    },
    {
      "role": "current_addressee_likely_Emma",
      "discourse_level": "current_discourse_act",
      "status": "uncertain",
      "analysis": "The response form indicates that the addressee has sought or required confirmation, and background knowledge makes Emma the likely addressee. The fragment does not provide her immediate reaction or show whether she believes the reassurance.",
      "confidence": 0.76
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The text attributes a genuine spoken avowal to the character while the wider novel's ironic characterization of the likely speaker undermines confidence that the words transparently report his emotional state.",
      "confidence": 0.76
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "A reader familiar with the wider relationship can recognize the utterance as a direct avowal and reassurance while doubting its sincerity because of Rodolphe's established attitudes and conduct.",
      "confidence": 0.75
    }
  ],
  "disagreements": [
    {
      "parties": [
        "original_avower_and_current_speaker",
        "narrator_or_text"
      ],
      "subject": "Credibility of the professed loving state",
      "description": "The speaker's explicit self-presentation asserts uncomplicated love, whereas the wider novel's characterization of the likely speaker encourages doubt that this avowal accurately represents a sustained loving state.",
      "evidence_ids": [
        "E1",
        "E5"
      ],
      "confidence": 0.75
    }
  ],
  "assessments": {
    "deception_misrepresentation": {
      "status": "supported",
      "analysis": "Background knowledge of the likely Rodolphe–Emma context supports reading the declaration as at least an emotionally inflated or formulaic representation: Rodolphe's conduct and cynical perspective do not sustain the kind of romantic love Emma understands him to be affirming. The very short local fragment alone would not establish this.",
      "confidence": 0.74
    },
    "manipulation_pressure": {
      "status": "uncertain_not_assessable",
      "analysis": "The reply may placate Emma and help the speaker maintain the relationship, but neither the fragment nor confidently remembered scene-specific details settle whether this particular utterance is intentionally manipulative. It does not locally exert pressure on the addressee.",
      "confidence": 0.59
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "The wording is semantically direct and unhedged. Any deception lies more plausibly in the truth or emotional adequacy of the assertion than in calculated ambiguity.",
      "confidence": 0.92
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“je t’aime”",
      "supports": "A maximally explicit first-person, present-tense assertion of love and therefore very strong truth-conditional support.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“Mais oui”",
      "supports": "The avowal functions as an emphatic affirmative response, supporting the classification of the current act as reassurance and suggesting a prior doubt or request for confirmation.",
      "confidence": 0.95
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "The exclamation mark after “je t’aime!”",
      "supports": "Adds emotional or emphatic force, though it does not displace the utterance's clear propositional content.",
      "confidence": 0.9
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "“répondait-il”",
      "supports": "Attributes the words to a male character as a spoken reply and establishes direct represented speech.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E5",
      "source": "background_knowledge",
      "quotation_or_description": "In the likely Rodolphe–Emma portion of the novel, Rodolphe becomes bored and cynical about Emma's romantic language and does not share the absolute conception of love she invests in their affair.",
      "supports": "Weakens the declaration's credibility, supports possible misrepresentation, and explains the ironic distance available to narrator and reader.",
      "confidence": 0.79
    },
    {
      "evidence_id": "E6",
      "source": "supplied_metadata",
      "quotation_or_description": "The metadata identifies the work as Gustave Flaubert's Madame Bovary and places the occurrence at relative position 0.542745.",
      "supports": "Permits cautious application of remembered knowledge about the middle portion of the novel; it does not by itself identify the participants or establish insincerity.",
      "confidence": 0.97
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.79,
    "contribution": "Background knowledge was used to identify the exchange as likely occurring during Emma's affair with Rodolphe and to distinguish the clear semantic avowal from its questionable sincerity in the novel's broader ironic treatment of that relationship.",
    "notes": "The identification of Rodolphe and Emma is highly plausible but not independently confirmed by the 36-character supplied context or chapter metadata. No remembered wording beyond the supplied quotation is treated as exact."
  },
  "context_needs": [
    {
      "need": "useful_for_richer_interpretation",
      "layers": [
        "current_discourse_act",
        "contextual_modification",
        "participant_construals",
        "disagreements",
        "assessments"
      ],
      "claim": "The speaker is Rodolphe answering Emma, and the reply is a formulaic or impatient reassurance that misrepresents his emotional state.",
      "request": "Provide the surrounding paragraph and, ideally, the preceding and following page so that the participants, prompting question, narrative framing, and immediate reaction can be verified."
    }
  ],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The scheme naturally separates the utterance's explicit truth-conditional love-content from its reassuring discourse function and contextually weakened sincerity. A minor limitation is that it has no dedicated field for aspectual framing such as a potentially iterative or habitual imperfect speech tag, which could matter if wider context showed this to be a recurring response rather than a single exchange.",
    "proposed_missing_dimensions": [
      "Aspectual or iterative status of represented speech, distinguishing a single token from habitual or repeated formulaic utterance"
    ]
  },
  "notes": "The strongest conclusion is that this is a direct, spoken avowal used as reassurance. The classification of it as deceptive depends on wider-work knowledge and remains less certain than the core semantic and realisation classifications."
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

- **Selected attempt:** `results\pipeline_runs\gutenberg-14155\20260902T043409Z\annotations\flaubert-madame-bovary-400a3aed5a88\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 1 / 2
- **Core analysis:** The highlighted « je t’aime » directly presents the speaker's love as true. The continuation—her inability to do without the addressee, painful jealousy, and extravagant praise—intensifies that avowal and makes it partly exclamatory. « Je suis ta servante et ta concubine » invokes an existing lover relationship and submissive posture, but neither the highlighted formula nor its immediate elaboration substantially creates or renews a commitment.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal, explanation, elicitation_of_reaffirmation, pressure
- **Current-act analysis:** She directly avows love and explains its intensity through dependence and jealous suffering. Her questions—especially « aucune ne te plaît? »—seek reassurance that no other woman attracts him. The combination of declared inability to live without him, jealousy, and solicitations for confirmation places emotional pressure on the addressee, although the passage does not establish calculated manipulation.
- **Contextual modification:** preserves, strengthens, redirects, distances
- **Ontology adequate:** False — The layered scheme otherwise gives a natural account of the avowal, its exclamatory intensity, its direct-speech realization, and its jealous interpersonal use. However, the single assessment field « manipulation_pressure » prevents the required independent assessment of manipulation and pressure: pressure is supported here, while calculated manipulation is substantially less certain. The ontology also has no dedicated dimensions for reciprocity, emotional dependency, or the distinction between a speaker's sincerity and the objective adequacy of her romantic self-conception.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-400a3aed5a88",
  "core_love_content": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 2
    },
    "mixed_reading": {
      "is_mixed": true,
      "basis": "substantial_multiple_support",
      "justification": "The utterance clearly avows love as a true emotional state, while its exclamatory opening, repetition, and surrounding emotional escalation also give it substantial outburst-like force. It does not, however, clearly undertake a new obligation or commitment."
    },
    "relationship_modifier": "Passionate, erotic, possessive, and self-subordinating love between lovers.",
    "analysis": "The highlighted « je t’aime » directly presents the speaker's love as true. The continuation—her inability to do without the addressee, painful jealousy, and extravagant praise—intensifies that avowal and makes it partly exclamatory. « Je suis ta servante et ta concubine » invokes an existing lover relationship and submissive posture, but neither the highlighted formula nor its immediate elaboration substantially creates or renews a commitment.",
    "confidence": 0.96
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The narrator represents a woman directly addressing her lover, with « reprenait-elle » functioning as a speech attribution. The words are presented as spoken in the fictional world, not as a quotation of an earlier or hypothetical utterance.",
    "confidence": 0.98
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "explanation",
      "elicitation_of_reaffirmation",
      "pressure"
    ],
    "other_description": null,
    "analysis": "She directly avows love and explains its intensity through dependence and jealous suffering. Her questions—especially « aucune ne te plaît? »—seek reassurance that no other woman attracts him. The combination of declared inability to live without him, jealousy, and solicitations for confirmation places emotional pressure on the addressee, although the passage does not establish calculated manipulation.",
    "confidence": 0.91
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens",
      "redirects",
      "distances"
    ],
    "other_description": null,
    "analysis": "The surrounding speech preserves the literal avowal and strongly intensifies it through repetition, dependency, jealousy, superlative self-comparison, and idolizing praise. It also redirects the avowal toward possessiveness and a request for exclusivity. Knowledge of the wider novel creates some ironic distance between Emma's romantic absolutism and the unstable, unequal affair in which she voices it; that distance qualifies the relational implications without negating the sincerity of her present emotion.",
    "confidence": 0.87
  },
  "participant_construals": [
    {
      "role": "original_avower/current_speaker (Emma Bovary)",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Emma presents her love as overwhelming, indispensable, exclusive, and bound up with jealousy. Her self-description as servant and concubine depicts willing emotional and erotic subordination, while her questions seek confirmation of the lover's exclusivity.",
      "confidence": 0.95
    },
    {
      "role": "current_addressee (probably Rodolphe Boulanger)",
      "discourse_level": "both",
      "status": "uncertain",
      "analysis": "Background knowledge strongly suggests that the addressee is Rodolphe and that his attachment is markedly less absolute than Emma's. The supplied excerpt does not include his response, so his construal of this particular avowal—whether as sincere, burdensome, flattering, or conventional—cannot be established directly.",
      "confidence": 0.79
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The text gives Emma's speech directly while allowing its accumulation of jealousy, abasement, and extravagant praise to expose the excessive and formulaic character of her romantic imagination. The local narration does not explicitly declare her insincere.",
      "confidence": 0.86
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "A reader can recognize both a sincere emotional avowal and a troubling performance of dependency, possessiveness, and romantic idolization. Familiarity with the wider work additionally makes the lack of reciprocity and the dramatic irony salient.",
      "confidence": 0.89
    }
  ],
  "disagreements": [
    {
      "parties": [
        "original_avower/current_speaker (Emma Bovary)",
        "current_addressee (probably Rodolphe Boulanger)"
      ],
      "subject": "Reciprocity and meaning of the affair",
      "description": "Emma construes the relationship as an absolute, exclusive emotional bond, whereas the wider novel presents Rodolphe's involvement as substantially less committed and ultimately incompatible with her romantic expectations.",
      "evidence_ids": [
        "E2",
        "E3",
        "E6"
      ],
      "confidence": 0.86
    }
  ],
  "assessments": {
    "deception_misrepresentation": {
      "status": "unsupported",
      "analysis": "The local intensity and detailed account of jealousy support sincere feeling rather than a knowingly false avowal. The wider novel's criticism of Emma's romantic self-dramatization may complicate her self-understanding, but that is not sufficient evidence that she deliberately misrepresents her feelings here.",
      "confidence": 0.88
    },
    "manipulation_pressure": {
      "status": "supported",
      "analysis": "Pressure is supported by the declaration of extreme dependence and the demand-like request that the lover confirm no other woman pleases him. Evidence for calculated manipulation is weaker: the speech can plausibly arise from genuine jealousy and emotional desperation. The composite status is therefore driven principally by pressure, not by proof of deliberate manipulation.",
      "confidence": 0.82
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "The avowal is explicit and repeatedly elaborated. Although Emma's rhetoric may exceed what the relationship can sustain, she does not strategically leave the existence or intensity of her professed love ambiguous.",
      "confidence": 0.93
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "« Oh! c’est que je t’aime! reprenait-elle »",
      "supports": "Direct spoken avowal with emphatic, exclamatory framing and explicit attribution to the female speaker.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "« je t’aime à ne pouvoir me passer de toi »",
      "supports": "Presents love as overwhelming dependence and strengthens both the truth-conditional avowal and its emotional intensity.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "She imagines him speaking to other women and asks, « aucune ne te plaît? »",
      "supports": "Shows jealousy, possessiveness, elicitation of reassurance, and emotional pressure concerning exclusivity.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "« moi, je sais mieux aimer! Je suis ta servante et ta concubine! »",
      "supports": "Frames her love as superior to rivals' love and as erotic and self-subordinating, while invoking an existing relational role rather than clearly creating a new commitment.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E5",
      "source": "local_text",
      "quotation_or_description": "« Tu es mon roi, mon idole! tu es bon! tu es beau! tu es intelligent! tu es fort! »",
      "supports": "Intensifies the avowal through idolization and cumulative praise, while exposing its extravagant romantic rhetoric.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E6",
      "source": "background_knowledge",
      "quotation_or_description": "In the wider novel, Emma's affair with Rodolphe is unequal: she invests it with romantic absoluteness, while Rodolphe is a comparatively cynical seducer who ultimately abandons their projected elopement.",
      "supports": "Identifies the probable participants and supports dramatic irony, limited reciprocity, and contextual distance from Emma's interpretation of the relationship.",
      "confidence": 0.88
    },
    {
      "evidence_id": "E7",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as coming from Gustave Flaubert's Madame Bovary, at relative source position 0.543116.",
      "supports": "Connects the passage to the known work and gives approximate placement, enabling cautious use of remembered plot context without treating metadata as passage wording.",
      "confidence": 0.99
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.88,
    "contribution": "Background knowledge was used to identify the speaker as Emma and the probable addressee as Rodolphe, to characterize their affair as unequal, and to explain the dramatic irony between Emma's absolute avowal and Rodolphe's lesser commitment. The core classification as a direct, sincere, emotionally heightened avowal does not depend on that knowledge.",
    "notes": "The participant identification is highly probable from the passage's approximate position and remembered wording and plot context, but the supplied excerpt itself names neither participant. Claims about Rodolphe's response to this exact speech are therefore kept uncertain."
  },
  "context_needs": [
    {
      "need": "useful_for_richer_interpretation",
      "layers": [
        "current_discourse_act",
        "participant_construals",
        "disagreements",
        "assessments"
      ],
      "claim": "Whether the pressure is spontaneous reassurance-seeking or part of a more deliberate effort to control the addressee, and how he construes this particular avowal.",
      "request": "Provide the dialogue immediately preceding this excerpt and the addressee's ensuing response."
    }
  ],
  "ontology_assessment": {
    "adequate": false,
    "diagnosis": "The layered scheme otherwise gives a natural account of the avowal, its exclamatory intensity, its direct-speech realization, and its jealous interpersonal use. However, the single assessment field « manipulation_pressure » prevents the required independent assessment of manipulation and pressure: pressure is supported here, while calculated manipulation is substantially less certain. The ontology also has no dedicated dimensions for reciprocity, emotional dependency, or the distinction between a speaker's sincerity and the objective adequacy of her romantic self-conception.",
    "proposed_missing_dimensions": [
      "Separate assessment fields for manipulation and for pressure",
      "Reciprocity or asymmetry of professed love",
      "Emotional dependency and possessiveness",
      "Distinction between subjective sincerity and accuracy of romantic self-interpretation",
      "Narrative or dramatic irony distinct from irony performed by the current speaker"
    ]
  },
  "notes": "The highlighted occurrence is the first « je t’aime » in an extended avowal that immediately repeats the formula. Its chief force is truth-conditional, with substantial exclamatory coloring. The speech exerts pressure for exclusivity, but that current use should not be mistaken for strong performative commitment in the core love-content."
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

- **Selected attempt:** `results\pipeline_runs\gutenberg-14155\20260902T043409Z\annotations\flaubert-madame-bovary-acc8280ba5f0\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 1 / 3
- **Core analysis:** “Je t’aime” directly presents the speaker's love as true, and “je t’aime à ne pouvoir me passer de toi” specifies it as an overwhelming need. “Oh!”, immediate repetition, and the ensuing emotional crescendo support a strong exclamatory dimension. The surrounding claims that she is his servant and concubine have weak pledge-like implications, but the love-content itself does not clearly create or renew an obligation.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal, explanation, elicitation_of_reaffirmation, pressure
- **Current-act analysis:** The speaker directly avows love and uses “c’est que” to present that love as an explanation. Her subsequent jealous questions—whether he speaks to other women and whether any pleases him—seek reassurance or reaffirmation of exclusivity. Claims of being unable to live without him, together with extreme self-subordination and praise, place emotional pressure on the addressee, although the passage does not establish calculated manipulation.
- **Contextual modification:** strengthens, redirects, distances
- **Ontology adequate:** True — The layered scheme naturally distinguishes the avowal's emotional truth, its exclamatory production, its reassurance-seeking pressure, and the wider ironic distance. The main nuance not directly encoded is that a statement may be experientially sincere while its language is conventional, self-dramatizing, and received as clichéd. The scheme also lacks a dedicated marker for habitual or iterative speech suggested by the imperfect “reprenait.”

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-acc8280ba5f0",
  "core_love_content": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 3
    },
    "mixed_reading": {
      "is_mixed": true,
      "basis": "substantial_multiple_support",
      "justification": "The utterance strongly avows love as a true emotional state, while its exclamation, repetition, and escalating declarations of dependence also give it substantial emotionally triggered, outburst-like force."
    },
    "relationship_modifier": "Adulterous erotic love expressed as jealous dependence, self-subordination, and idolatrous devotion.",
    "analysis": "“Je t’aime” directly presents the speaker's love as true, and “je t’aime à ne pouvoir me passer de toi” specifies it as an overwhelming need. “Oh!”, immediate repetition, and the ensuing emotional crescendo support a strong exclamatory dimension. The surrounding claims that she is his servant and concubine have weak pledge-like implications, but the love-content itself does not clearly create or renew an obligation.",
    "confidence": 0.97
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "A female character currently speaks the words in the fictional scene. The reporting clause “reprenait-elle” explicitly attributes the direct speech to her; this is neither a quotation of an earlier utterance nor imagined speech.",
    "confidence": 0.99
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "explanation",
      "elicitation_of_reaffirmation",
      "pressure"
    ],
    "other_description": null,
    "analysis": "The speaker directly avows love and uses “c’est que” to present that love as an explanation. Her subsequent jealous questions—whether he speaks to other women and whether any pleases him—seek reassurance or reaffirmation of exclusivity. Claims of being unable to live without him, together with extreme self-subordination and praise, place emotional pressure on the addressee, although the passage does not establish calculated manipulation.",
    "confidence": 0.92
  },
  "contextual_modification": {
    "effects": [
      "strengthens",
      "redirects",
      "distances"
    ],
    "other_description": null,
    "analysis": "Repetition and the claim that she cannot do without him strengthen the avowal. Jealous imaginings, the servant/concubine language, and the sequence “roi,” “idole,” and idealizing compliments redirect love toward possessiveness, dependency, submission, and romantic idolization. Background knowledge of Rodolphe's jaded reception of Emma's conventional romantic language introduces distance between her experienced intensity and the wider novel's treatment of its rhetoric; that distance does not by itself make the avowal insincere.",
    "confidence": 0.86
  },
  "participant_construals": [
    {
      "role": "original_avower (Emma Bovary)",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Emma presents her love as overwhelming, exclusive, and inseparable from jealousy and dependence. Her speech also presses the addressee to deny interest in other women.",
      "confidence": 0.94
    },
    {
      "role": "current_addressee (Rodolphe Boulanger)",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Background knowledge identifies Rodolphe as the addressee. In this phase of the affair, he receives Emma's passionate rhetoric from an increasingly jaded perspective and treats such language as familiar rather than uniquely revelatory.",
      "confidence": 0.82
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The text represents Emma's avowal directly and preserves its emotional force, while its accumulation of romantic clichés, hierarchy, and extravagant praise permits critical distance from her self-dramatizing conception of love.",
      "confidence": 0.84
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "A reader can construe the avowal as emotionally sincere while also recognizing jealousy, emotional pressure, conventional romantic scripting, and the mismatch between Emma's idealization and Rodolphe's attitude.",
      "confidence": 0.88
    }
  ],
  "disagreements": [
    {
      "parties": [
        "original_avower (Emma Bovary)",
        "current_addressee (Rodolphe Boulanger)"
      ],
      "subject": "The uniqueness and significance of Emma's passionate avowal",
      "description": "Emma presents her love as uniquely intense and absolute, whereas Rodolphe's wider-work perspective reduces such declarations to familiar, repetitive language of passion. This is a conflict of valuation and uptake, not clear evidence that Emma is consciously lying.",
      "evidence_ids": [
        "E2",
        "E3",
        "E4",
        "E7"
      ],
      "confidence": 0.82
    }
  ],
  "assessments": {
    "deception_misrepresentation": {
      "status": "unsupported",
      "analysis": "The passage strongly supports genuine present emotional intensity, and no available evidence shows Emma consciously misrepresenting whether she feels love. Her idealization and dependence may be self-dramatizing or deluded, but that is not sufficient to establish deception.",
      "confidence": 0.86
    },
    "manipulation_pressure": {
      "status": "supported",
      "analysis": "Emotional pressure is supported by Emma's declaration that she cannot do without him, her jealous scenarios, and her questions seeking confirmation that no other woman pleases him. Evidence for deliberate, calculated manipulation is weaker than evidence for pressure.",
      "confidence": 0.82
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "The avowal is emphatic, repeated, and elaborated rather than strategically equivocal. Any complexity comes from irony, romantic scripting, and divergent uptake, not from ambiguity engineered by the speaker.",
      "confidence": 0.91
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“Oh! c’est que je t’aime!”",
      "supports": "Direct truth-conditional avowal, explanatory framing, and exclamatory emotional force.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“je t’aime à ne pouvoir me passer de toi”",
      "supports": "Repetition strengthens the avowal and characterizes the love as overwhelming dependence.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "She imagines him speaking to other women and asks, “aucune ne te plaît?”",
      "supports": "Jealousy, possessiveness, elicitation of reassurance, and emotional pressure.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "“Je suis ta servante et ta concubine! Tu es mon roi, mon idole!”",
      "supports": "Self-subordination and idolization redirect the avowal toward an unequal, theatrically absolute conception of devotion.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E5",
      "source": "local_text",
      "quotation_or_description": "The reporting clause “reprenait-elle” attributes the words to a female speaker within the scene.",
      "supports": "Classification as spoken direct represented speech; it may also suggest continuation or repetition within the exchange.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E6",
      "source": "supplied_metadata",
      "quotation_or_description": "The supplied metadata identifies the work as Gustave Flaubert's Madame Bovary.",
      "supports": "Permits cautious use of remembered character identities, relationship history, and the novel's wider treatment of romantic rhetoric.",
      "confidence": 1.0
    },
    {
      "evidence_id": "E7",
      "source": "background_knowledge",
      "quotation_or_description": "This is remembered as Emma addressing her lover Rodolphe during their affair; Rodolphe becomes jaded with her passion and treats romantic declarations as familiar and repetitive before ultimately abandoning their planned flight.",
      "supports": "Identification of speaker and addressee, their adulterous relationship, divergent uptake, and wider ironic distance from Emma's rhetoric.",
      "confidence": 0.84
    },
    {
      "evidence_id": "E8",
      "source": "background_knowledge",
      "quotation_or_description": "Across the novel, Emma repeatedly understands desire through idealized romantic scripts that exceed the realities of her relationships.",
      "supports": "The interpretation of the avowal as sincere in feeling yet self-dramatizing and shaped by conventional romantic fantasy.",
      "confidence": 0.88
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.86,
    "contribution": "Background knowledge identifies the unnamed “elle” and addressee as Emma and Rodolphe, places the speech in their adulterous affair, and supplies the important contrast between Emma's intense romantic idealization and Rodolphe's increasingly jaded reception. It also supports distinguishing emotional sincerity from the novel's ironic treatment of romantic scripts.",
    "notes": "The character identification and broad relational arc are highly reliable. The precise proximity of Rodolphe's famous reflection on the repetitive language of passion to this excerpt is remembered with slightly lower confidence, so no exact background wording is quoted."
  },
  "context_needs": [
    {
      "need": "useful_for_richer_interpretation",
      "layers": [
        "current_discourse_act",
        "contextual_modification",
        "participant_construals",
        "disagreements",
        "assessments"
      ],
      "claim": "The exact immediate cause of Emma's explanatory avowal and Rodolphe's contemporaneous uptake would refine the degree of pressure and narratorial distancing.",
      "request": "Provide the paragraphs immediately preceding and following this excerpt, especially any narration of what prompted “c’est que” and Rodolphe's response."
    }
  ],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The layered scheme naturally distinguishes the avowal's emotional truth, its exclamatory production, its reassurance-seeking pressure, and the wider ironic distance. The main nuance not directly encoded is that a statement may be experientially sincere while its language is conventional, self-dramatizing, and received as clichéd. The scheme also lacks a dedicated marker for habitual or iterative speech suggested by the imperfect “reprenait.”",
    "proposed_missing_dimensions": [
      "Experiential sincerity versus conventional or self-dramatizing rhetorical form",
      "Addressee uptake as belief, disbelief, boredom, or reduction to cliché",
      "Habitual or iterative recurrence of the represented utterance"
    ]
  },
  "notes": "The performative score remains low: surrounding language theatrically enacts submission, but neither affection, imagined relational hierarchy, nor emotional pressure by itself constitutes a strong undertaking. The central mixed reading is instead truth-conditional plus exclamatory."
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

- **Selected attempt:** `results\pipeline_runs\gutenberg-14155\20260902T043409Z\annotations\flaubert-madame-bovary-97b0baa4e5cf\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 0 / 1
- **Core analysis:** The idiomatic elliptical construction “Si je t’aime!” emphatically affirms that the speaker loves the addressee; the continuation “mais je t’adore, mon amour” makes its propositional avowal especially clear. Repetition and exclamation give the utterance expressive intensity, but it is not merely reflex-like and retains strong truth-conditional force. It does not itself undertake or renew a defined commitment.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal, reassurance
- **Current-act analysis:** The speaker directly avows love and intensifies the answer from loving to adoring. The responsive idiom “Si je t’aime!” strongly suggests an emphatic answer to an expressed or implied doubt or question, so reassurance is also likely, although the eliciting turn is not supplied.
- **Contextual modification:** preserves, strengthens, distances
- **Ontology adequate:** True — The scheme naturally distinguishes the utterance’s strong propositional avowal from its reassuring conversational use and from contextual questions of sincerity or manipulation. The exclamatory category is somewhat coarse because this utterance has exclamatory syntax and affective intensity without weak propositional force, but the support score and analysis can preserve that distinction.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-97b0baa4e5cf",
  "core_love_content": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 1
    },
    "mixed_reading": {
      "is_mixed": false,
      "basis": "none",
      "justification": null
    },
    "relationship_modifier": "Intense romantic or erotic love, expressed within an intimate relationship.",
    "analysis": "The idiomatic elliptical construction “Si je t’aime!” emphatically affirms that the speaker loves the addressee; the continuation “mais je t’adore, mon amour” makes its propositional avowal especially clear. Repetition and exclamation give the utterance expressive intensity, but it is not merely reflex-like and retains strong truth-conditional force. It does not itself undertake or renew a defined commitment.",
    "confidence": 0.97
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The dialogue dash and first-person address present the words as currently spoken by a character in the fictional world. Nothing in the supplied text marks them as a citation of an earlier or hypothetical utterance.",
    "confidence": 0.96
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "reassurance"
    ],
    "other_description": null,
    "analysis": "The speaker directly avows love and intensifies the answer from loving to adoring. The responsive idiom “Si je t’aime!” strongly suggests an emphatic answer to an expressed or implied doubt or question, so reassurance is also likely, although the eliciting turn is not supplied.",
    "confidence": 0.89
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens",
      "distances"
    ],
    "other_description": null,
    "analysis": "Locally, repetition, exclamation, “je t’adore,” and the endearment “mon amour” preserve and strengthen the avowal. Background knowledge of Rodolphe’s calculated seduction of Emma and his eventual abandonment of her introduces likely dramatic or narratorial distance between the declaration’s extravagant surface and its reliability. Because the excerpt does not identify the speaker or include surrounding narration, that distancing interpretation is less certain than the local intensification.",
    "confidence": 0.79
  },
  "participant_construals": [
    {
      "role": "original_avower/current_speaker, probably Rodolphe",
      "discourse_level": "both",
      "status": "uncertain",
      "analysis": "The speaker presents himself as loving and indeed adoring the addressee, apparently in order to affirm or reassure her. The supplied excerpt does not name him; identification as Rodolphe depends on moderately confident memory of the wider work.",
      "confidence": 0.79
    },
    {
      "role": "current_addressee, probably Emma",
      "discourse_level": "both",
      "status": "uncertain",
      "analysis": "The addressee is directly positioned as the speaker’s beloved and is probably Emma. The responsive wording suggests that her doubt or request for affirmation prompted the answer, but neither her preceding words nor her reaction is supplied.",
      "confidence": 0.76
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "both",
      "status": "uncertain",
      "analysis": "The text directly stages an emphatic romantic declaration. In the wider novel, Rodolphe’s cynical characterization likely gives such language ironic distance, but the local excerpt contains no explicit narratorial evaluation.",
      "confidence": 0.72
    },
    {
      "role": "reader informed by the wider work",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "A reader aware of Rodolphe’s treatment and eventual abandonment of Emma can understand the utterance simultaneously as an unambiguous avowal within the scene and as potentially unreliable or strategically exaggerated.",
      "confidence": 0.81
    }
  ],
  "disagreements": [
    {
      "parties": [
        "original_avower/current_speaker, probably Rodolphe",
        "reader informed by the wider work"
      ],
      "subject": "Reliability and sincerity of the professed love",
      "description": "The speaker explicitly presents intense love as true, while a reader informed by Rodolphe’s broader conduct has reason to doubt that the declaration accurately represents a durable loving state.",
      "evidence_ids": [
        "E1",
        "E2",
        "E4"
      ],
      "confidence": 0.74
    }
  ],
  "assessments": {
    "deception_misrepresentation": {
      "status": "supported",
      "analysis": "The local wording alone supplies no proof of lying, but moderately confident background knowledge identifies this as likely Rodolphe speaking to Emma. His calculated approach to the affair, waning attachment, and eventual abandonment support reading the extravagant declaration as at least exaggerating or misrepresenting the depth and durability of his feelings. Conscious deception at this exact moment remains less certain than general unreliability.",
      "confidence": 0.68
    },
    "manipulation_pressure": {
      "status": "uncertain_not_assessable",
      "analysis": "The declaration may reassure Emma and help sustain Rodolphe’s influence within the affair, but the supplied excerpt does not show a demand, threat, or immediate strategic objective. Wider characterization raises the possibility of manipulation without settling the function of this particular utterance.",
      "confidence": 0.61
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "The love-content is not strategically equivocal: the idiom, repetition, escalation to adoration, and endearment all make the avowal emphatic. Possible insincerity is distinct from ambiguity.",
      "confidence": 0.91
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“Si je t’aime! si je t’aime!”",
      "supports": "The repeated idiomatic expression emphatically affirms the truth of the speaker’s love and realizes it as direct represented speech.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“mais je t’adore, mon amour!”",
      "supports": "The speaker strengthens the avowal from love to adoration and uses an intimate endearment.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as coming from Gustave Flaubert’s Madame Bovary, at relative source position approximately 0.564.",
      "supports": "Identifies the work and gives approximate placement, enabling cautious use of remembered narrative context without treating metadata as passage wording.",
      "confidence": 1.0
    },
    {
      "evidence_id": "E4",
      "source": "background_knowledge",
      "quotation_or_description": "This occurrence is likely from Emma’s affair with Rodolphe; Rodolphe approaches the relationship calculatingly, becomes less attached, and ultimately abandons the planned elopement.",
      "supports": "Supports likely participant identification and the interpretation that the avowal may be exaggerated, unreliable, or viewed with dramatic irony.",
      "confidence": 0.78
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "moderate",
    "confidence": 0.78,
    "contribution": "Background knowledge was used to identify the speaker and addressee provisionally as Rodolphe and Emma and to assess possible dramatic irony, misrepresentation, and manipulation in light of Rodolphe’s broader conduct.",
    "notes": "The relationship and plot trajectory are remembered confidently in general, but the exact placement and attribution of this isolated line are less certain because the supplied excerpt omits speaker tags and adjacent narration."
  },
  "context_needs": [
    {
      "need": "useful_for_richer_interpretation",
      "layers": [
        "current_discourse_act",
        "contextual_modification",
        "participant_construals",
        "disagreements",
        "assessments"
      ],
      "claim": "The speaker is Rodolphe, the addressee is Emma, and the avowal answers her request for reassurance while functioning as a strategically unreliable declaration.",
      "request": "Provide the preceding and following paragraphs, especially any speaker tags, Emma’s preceding question, and narratorial commentary on Rodolphe’s thoughts or manner."
    }
  ],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The scheme naturally distinguishes the utterance’s strong propositional avowal from its reassuring conversational use and from contextual questions of sincerity or manipulation. The exclamatory category is somewhat coarse because this utterance has exclamatory syntax and affective intensity without weak propositional force, but the support score and analysis can preserve that distinction.",
    "proposed_missing_dimensions": [
      "A dedicated dimension for rhetorical or affective intensification that does not imply reflex-like production or weakened propositional force."
    ]
  },
  "notes": "French “Si je t’aime!” is an emphatic elliptical response, approximately “Do I love you!” or “Indeed I love you,” rather than a genuinely conditional or hedged statement. Any claim about Rodolphe’s exact intention should remain provisional until the adjacent context confirms attribution and narrative framing."
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

- **Selected attempt:** `results\pipeline_runs\gutenberg-14155\20260902T043409Z\annotations\flaubert-madame-bovary-b0502164917d\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 0 / 3
- **Core analysis:** “Si je t’aime!” is an emphatic echo-like response meaning approximately “Do I love you!/Of course I love you,” not a genuine conditional. Repetition and the escalation “mais je t’adore, mon amour” strongly avow and intensify the claimed emotional state. The line has no clear commitment-making force beyond its immediate relational reassurance.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal, reassurance, manipulation
- **Current-act analysis:** The speaker directly avows love and, through the echoing “Si je t’aime!” and intensified “je t’adore,” answers or pre-empts doubt with extravagant reassurance. Background knowledge identifying the speaker as probably Rodolphe, whose courtship of Emma is calculated and whose devotion proves unreliable, supports a further manipulative use: the declaration helps maintain Emma's emotional investment. That manipulation is less certain than the avowal and reassurance because the immediate prompting exchange is not supplied.
- **Contextual modification:** preserves, strengthens, manipulates
- **Ontology adequate:** True — The scheme naturally separates the emphatic truth-conditional avowal from its exclamatory form, its reassuring and potentially manipulative present use, and the wider narrative's challenge to its reliability. The open analyses are sufficient to describe the French echo-question construction and retrospective irony.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-b0502164917d",
  "core_love_content": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 3
    },
    "mixed_reading": {
      "is_mixed": true,
      "basis": "substantial_multiple_support",
      "justification": "The utterance emphatically presents intense love as true, while its repetition, exclamation marks, and escalation from aimer to adorer give it substantial emotionally exclamatory force. It does not clearly undertake a new obligation or commitment."
    },
    "relationship_modifier": "Romantic and erotic love within Emma's adulterous relationship with Rodolphe.",
    "analysis": "“Si je t’aime!” is an emphatic echo-like response meaning approximately “Do I love you!/Of course I love you,” not a genuine conditional. Repetition and the escalation “mais je t’adore, mon amour” strongly avow and intensify the claimed emotional state. The line has no clear commitment-making force beyond its immediate relational reassurance.",
    "confidence": 0.97
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The dash and first-person address represent a character currently speaking these words in the fictional world. Nothing in the supplied extract indicates quotation of an earlier utterance, imagined speech, or narratorial verbalisation.",
    "confidence": 0.97
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "reassurance",
      "manipulation"
    ],
    "other_description": null,
    "analysis": "The speaker directly avows love and, through the echoing “Si je t’aime!” and intensified “je t’adore,” answers or pre-empts doubt with extravagant reassurance. Background knowledge identifying the speaker as probably Rodolphe, whose courtship of Emma is calculated and whose devotion proves unreliable, supports a further manipulative use: the declaration helps maintain Emma's emotional investment. That manipulation is less certain than the avowal and reassurance because the immediate prompting exchange is not supplied.",
    "confidence": 0.81
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens",
      "manipulates"
    ],
    "other_description": null,
    "analysis": "The context preserves the literal avowal and strengthens it through repetition, exclamation, the scalar rise from “love” to “adore,” and the endearment “mon amour.” In the wider relationship, Rodolphe's calculated seduction and eventual abandonment cast retrospective suspicion on the declaration and support reading its emphatic reassurance as emotionally manipulative, although they do not conclusively prove that he felt no affection at this exact moment.",
    "confidence": 0.82
  },
  "participant_construals": [
    {
      "role": "current_speaker_and_original_avower, probably Rodolphe",
      "discourse_level": "both",
      "status": "uncertain",
      "analysis": "The utterance presents the speaker as intensely in love and uses that presentation to reassure the addressee. The wider work and approximate location strongly suggest Rodolphe, but the 57-character local extract does not itself identify him.",
      "confidence": 0.82
    },
    {
      "role": "current_addressee, probably Emma",
      "discourse_level": "both",
      "status": "uncertain",
      "analysis": "The intimate second-person pronoun and “mon amour” mark a romantic addressee whom the speaker is emphatically reassuring. Background knowledge strongly suggests Emma, but her immediate response and exact construal are absent from the supplied extract.",
      "confidence": 0.84
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The wider narrative characterization of Rodolphe as a calculating seducer and his later abandonment of Emma qualify the declaration's reliability, creating distance between its emphatic surface and the work's broader presentation of the relationship.",
      "confidence": 0.78
    },
    {
      "role": "informed_reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "An informed reader can recognize a sincere-seeming, emotionally forceful avowal at the local level while distrusting its depth and durability because of Rodolphe's established motives and later conduct.",
      "confidence": 0.83
    }
  ],
  "disagreements": [
    {
      "parties": [
        "current_speaker_and_original_avower, probably Rodolphe",
        "narrator_or_text and informed reader"
      ],
      "subject": "Sincerity and reliability of the professed love",
      "description": "The speaker unequivocally presents intense love as true, whereas the wider narrative gives readers substantial reason to regard the profession as exaggerated, strategically useful, or unreliable. The evidence does not establish that every feeling asserted here is wholly fabricated.",
      "evidence_ids": [
        "E1",
        "E2",
        "E4",
        "E5"
      ],
      "confidence": 0.79
    }
  ],
  "assessments": {
    "deception_misrepresentation": {
      "status": "supported",
      "analysis": "Rodolphe's calculated pursuit of Emma, the extravagant escalation to adoration, and his later abandonment support the inference that the declaration overstates the depth or durability of his attachment. Complete fabrication cannot be established, so the support is qualified rather than conclusive.",
      "confidence": 0.7
    },
    "manipulation_pressure": {
      "status": "supported",
      "analysis": "The emphatic reassurance plausibly serves to preserve Emma's trust and emotional dependence within a relationship Rodolphe initially pursued strategically. The line is manipulative through reassurance rather than overt coercive pressure.",
      "confidence": 0.73
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "The semantic claim is conspicuously direct and intensified: the speaker says not merely that he loves but that he adores the addressee. Possible insincerity or exaggeration does not itself make the wording strategically ambiguous.",
      "confidence": 0.91
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“Si je t’aime! si je t’aime!”",
      "supports": "The repeated echo-like construction emphatically affirms love and supplies substantial exclamatory force, while also suggesting a response to expressed or anticipated doubt.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“mais je t’adore, mon amour!”",
      "supports": "The speaker strengthens the avowal by escalating from loving to adoring and by using an intimate romantic endearment.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "The passage begins with a dialogue dash and uses first- and second-person present-tense forms.",
      "supports": "The love-content is represented as direct spoken dialogue in the fictional present rather than as quotation or reported speech.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E4",
      "source": "background_knowledge",
      "quotation_or_description": "In the wider novel, Rodolphe's pursuit of Emma is initially calculated as a seduction rather than founded on a serious reciprocal commitment.",
      "supports": "Identification of a manipulative dimension and skepticism about the full sincerity or durability of his professions.",
      "confidence": 0.87
    },
    {
      "evidence_id": "E5",
      "source": "background_knowledge",
      "quotation_or_description": "Rodolphe later abandons the planned elopement with Emma, revealing that his willingness to undertake a shared future falls far short of hers.",
      "supports": "Retrospective weakening of the declaration's reliability and the distinction between emotional avowal and genuine commitment.",
      "confidence": 0.93
    },
    {
      "evidence_id": "E6",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is in Gustave Flaubert's Madame Bovary at relative source position approximately 0.564.",
      "supports": "Together with remembered plot structure, this makes identification of the exchange as belonging to the Emma–Rodolphe affair plausible; metadata alone does not identify the participants.",
      "confidence": 0.78
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.88,
    "contribution": "Background knowledge was used to identify the probable participants as Rodolphe and Emma and, more importantly, to qualify the declaration through Rodolphe's calculated seduction and later abandonment. It supports manipulation and possible misrepresentation but does not prove that he had no affectionate feeling at the moment of speaking.",
    "notes": "The participant identification is highly plausible but not locally explicit. The exact immediate scene and prompting words were not relied upon because they are not confidently remembered."
  },
  "context_needs": [
    {
      "need": "useful_for_richer_interpretation",
      "layers": [
        "current_discourse_act",
        "participant_construals",
        "assessments",
        "disagreements"
      ],
      "claim": "The declaration directly answers Emma's doubt and is being used by Rodolphe at this moment as calculated reassurance.",
      "request": "Supply the preceding and following paragraphs to establish the named participants, the question or doubt prompting “Si je t’aime!”, and the addressee's immediate response."
    }
  ],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The scheme naturally separates the emphatic truth-conditional avowal from its exclamatory form, its reassuring and potentially manipulative present use, and the wider narrative's challenge to its reliability. The open analyses are sufficient to describe the French echo-question construction and retrospective irony.",
    "proposed_missing_dimensions": []
  },
  "notes": "French “Si je t’aime!” here is best understood idiomatically as an emphatic response to a question or doubt—approximately “Do I love you!/Of course I love you”—rather than as a conditional protasis. The passage strongly supports emotional intensity at the level of expression, but intensity of expression should not be equated with sincerity or durable commitment."
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

- **Selected attempt:** `results\pipeline_runs\gutenberg-14155\20260902T043409Z\annotations\flaubert-madame-bovary-5396f984c871\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 0 / 1
- **Core analysis:** The explicit declarative “je vous aime” presents the speaker's love as true. Its exclamation mark and placement within an urgent plea give it emotional intensity, but its propositional force remains clear, so the exclamatory/reflexive reading is secondary rather than independently substantial. It does not itself undertake or renew a commitment.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal, other
- **Current-act analysis:** The speaker directly avows love while pleading “De grâce, restez!” The avowal functions pragmatically as an emotionally forceful reason for the requested action. The short extract supports pleading and persuasion, but not by itself coercion or manipulation.
- **Contextual modification:** preserves, strengthens, redirects
- **Ontology adequate:** True — The scheme naturally distinguishes the explicit truth-conditional avowal from its present persuasive use. The small current-act inventory lacks a dedicated pleading or requesting category, but the open “other” field preserves that central function without distorting the core as performative.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-5396f984c871",
  "core_love_content": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 1
    },
    "mixed_reading": {
      "is_mixed": false,
      "basis": "none",
      "justification": null
    },
    "relationship_modifier": null,
    "analysis": "The explicit declarative “je vous aime” presents the speaker's love as true. Its exclamation mark and placement within an urgent plea give it emotional intensity, but its propositional force remains clear, so the exclamatory/reflexive reading is secondary rather than independently substantial. It does not itself undertake or renew a commitment.",
    "confidence": 0.97
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The dialogue dash, imperative addressed to another person, and exclamation marks represent a character currently speaking in the fictional world. Nothing in the supplied text indicates quotation, report, imagination, writing, negation, or hedging.",
    "confidence": 0.97
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "other"
    ],
    "other_description": "Pleading with or attempting to persuade the addressee to remain",
    "analysis": "The speaker directly avows love while pleading “De grâce, restez!” The avowal functions pragmatically as an emotionally forceful reason for the requested action. The short extract supports pleading and persuasion, but not by itself coercion or manipulation.",
    "confidence": 0.94
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens",
      "redirects"
    ],
    "other_description": null,
    "analysis": "The context preserves the ordinary avowal of love, while the urgent request and repeated exclamatory punctuation intensify its emotional presentation. Its discourse function is also redirected toward supporting the immediate plea that the addressee stay.",
    "confidence": 0.91
  },
  "participant_construals": [
    {
      "role": "current_speaker_and_original_avower",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The speaker presents themself as loving the addressee and uses that avowal as part of a plea for the addressee to remain.",
      "confidence": 0.96
    },
    {
      "role": "current_addressee",
      "discourse_level": "both",
      "status": "unavailable",
      "analysis": "The extract supplies neither the addressee's response nor evidence of whether the addressee accepts the avowal as sincere or the plea as legitimate.",
      "confidence": null
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "At the local level, a reader can construe the line as an explicit love avowal intensified and pragmatically mobilized by an urgent request to stay; the speaker's ultimate sincerity remains unsettled.",
      "confidence": 0.92
    }
  ],
  "disagreements": [],
  "assessments": {
    "deception_misrepresentation": {
      "status": "uncertain_not_assessable",
      "analysis": "The explicit avowal supplies no local marker of lying, but the very short extract cannot establish whether the speaker actually feels the professed love or is misrepresenting it.",
      "confidence": 0.92
    },
    "manipulation_pressure": {
      "status": "uncertain_not_assessable",
      "analysis": "The avowal is used persuasively in an urgent request for the addressee to stay, creating some emotional pressure in an ordinary sense. The extract does not establish that this rises to manipulation, coercion, or an abusive pattern.",
      "confidence": 0.86
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "The love-content is linguistically direct and unhedged. Uncertainty about sincerity is not evidence that the wording itself is strategically ambiguous.",
      "confidence": 0.91
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“je vous aime!”",
      "supports": "A maximally explicit, unhedged first-person avowal presenting love for the addressee as true.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“De grâce, restez!”",
      "supports": "The current act includes an urgent, deferential plea that the addressee remain.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "The plea and avowal are adjacent within one dash-introduced, doubly exclamatory utterance.",
      "supports": "The love avowal is emotionally intensified and used as part of the attempt to persuade the addressee to stay; the typography also supports direct represented speech.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E4",
      "source": "supplied_metadata",
      "quotation_or_description": "The supplied metadata identifies the source as Gustave Flaubert's French novel Madame Bovary.",
      "supports": "Establishes the identified literary work and language without supplying the missing identities or response in this excerpt.",
      "confidence": 0.99
    }
  ],
  "background_knowledge": {
    "used": false,
    "familiarity": "moderate",
    "confidence": null,
    "contribution": null,
    "notes": "General familiarity with Madame Bovary was not used to identify this scene because recollection of the precise speaker, addressee, and immediate circumstances was insufficiently reliable."
  },
  "context_needs": [
    {
      "need": "useful_for_richer_interpretation",
      "layers": [
        "current_discourse_act",
        "contextual_modification",
        "participant_construals",
        "disagreements",
        "assessments"
      ],
      "claim": "The identities, motives, sincerity, and possible manipulative force of the plea cannot be established from the 33-character extract.",
      "request": "Provide the surrounding paragraph or scene, including attribution of the speech, the circumstances prompting the request to stay, and the addressee's response."
    }
  ],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The scheme naturally distinguishes the explicit truth-conditional avowal from its present persuasive use. The small current-act inventory lacks a dedicated pleading or requesting category, but the open “other” field preserves that central function without distorting the core as performative.",
    "proposed_missing_dimensions": [
      "A dedicated current-discourse-act category for pleading or requesting",
      "A graded distinction between ordinary emotional persuasion, interpersonal pressure, and coercive manipulation"
    ]
  },
  "notes": "The line's emotional urgency does not erase its clear propositional assertion, and its use to support “restez” should not be mistaken for a core relational undertaking."
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

- **Selected attempt:** `results\pipeline_runs\gutenberg-14155\20260902T043409Z\annotations\flaubert-madame-bovary-1e7d6742e45b\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 1 / 1
- **Core analysis:** “Je t’aime” directly presents the speaker’s present love as true. Its unhedged first-person present tense gives it very strong truth-conditional force. The adjacent “je t’aimerai toujours” adds a promise-like assertion of future constancy, but the highlighted present-tense avowal does not by itself substantially undertake a new relational obligation. The exclamation marks and urgent apologetic setting add emotion without reducing the utterance to a reflex-like exclamation.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal, reassurance, other
- **Current-act analysis:** The speaker directly avows love while asking to be forgiven. “Tu es la seule qui me plaise,” the admission of having been foolish and cruel, and “je t’aimerai toujours” make the declaration a reassurance of exclusivity and constancy intended to repair an apparent relational disturbance. The final question, “Qu’as-tu? dis-le donc!”, also solicits an explanation of the addressee’s distress.
- **Contextual modification:** preserves, strengthens, weakens
- **Ontology adequate:** True — The scheme naturally separates the highlighted present-tense avowal from its apologetic and reassuring use and from the wider narrative’s weakening of the adjacent promise of permanence. The distinction between deception and later nonfulfillment is especially useful here.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "flaubert-madame-bovary-1e7d6742e45b",
  "core_love_content": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 1
    },
    "mixed_reading": {
      "is_mixed": false,
      "basis": "none",
      "justification": null
    },
    "relationship_modifier": "Romantic or erotic love within an intimate relationship",
    "analysis": "“Je t’aime” directly presents the speaker’s present love as true. Its unhedged first-person present tense gives it very strong truth-conditional force. The adjacent “je t’aimerai toujours” adds a promise-like assertion of future constancy, but the highlighted present-tense avowal does not by itself substantially undertake a new relational obligation. The exclamation marks and urgent apologetic setting add emotion without reducing the utterance to a reflex-like exclamation.",
    "confidence": 0.97
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The passage represents a character currently addressing another character in direct speech. Nothing indicates quotation of an earlier utterance, writing, imagination, negation, or narrative verbalisation of nonverbal conduct.",
    "confidence": 0.98
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "reassurance",
      "other"
    ],
    "other_description": "Support for an apology and plea for forgiveness",
    "analysis": "The speaker directly avows love while asking to be forgiven. “Tu es la seule qui me plaise,” the admission of having been foolish and cruel, and “je t’aimerai toujours” make the declaration a reassurance of exclusivity and constancy intended to repair an apparent relational disturbance. The final question, “Qu’as-tu? dis-le donc!”, also solicits an explanation of the addressee’s distress.",
    "confidence": 0.94
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens",
      "weakens"
    ],
    "other_description": null,
    "analysis": "Direct speech preserves the avowal’s ordinary assertive force. Locally, the claims that the addressee is the only person who pleases the speaker and that the love will last forever strengthen it through exclusivity and projected permanence. At the same time, remembered wider context from the deteriorating Emma–Léon affair and the novel’s subsequent events weakens confidence in the literal durability of “toujours,” giving the reassurance an ironic or unstable retrospective aspect without proving that the present-tense feeling is consciously false.",
    "confidence": 0.84
  },
  "participant_construals": [
    {
      "role": "original_avower",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The avower presents love, exclusivity, and future constancy as sincere facts and uses them to seek forgiveness and reassure the addressee.",
      "confidence": 0.94
    },
    {
      "role": "current_addressee",
      "discourse_level": "both",
      "status": "unavailable",
      "analysis": "The supplied extract gives no reply or narrated reaction showing whether the addressee believes, accepts, rejects, or is comforted by the declaration.",
      "confidence": null
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "both",
      "status": "uncertain",
      "analysis": "The local presentation supplies no explicit narratorial judgment, but the wider novel’s treatment of Emma’s affair with Léon and the eventual failure of romantic claims to permanence permits a retrospectively ironic construal.",
      "confidence": 0.74
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "uncertain",
      "analysis": "A reader familiar with the wider trajectory can understand the declaration as an immediate attempt at reassurance while doubting the durability and depth implied by “toujours.”",
      "confidence": 0.8
    }
  ],
  "disagreements": [
    {
      "parties": [
        "original_avower",
        "reader informed by later narrative"
      ],
      "subject": "Durability of the professed love",
      "description": "The avower asserts lifelong constancy, whereas the wider course of the relationship gives an informed reader reason to regard that projected permanence as unreliable. This is a conflict between the utterance’s represented commitment and later narrative outcome, not firm evidence that the speaker is consciously lying at the moment.",
      "evidence_ids": [
        "E3",
        "E5"
      ],
      "confidence": 0.8
    }
  ],
  "assessments": {
    "deception_misrepresentation": {
      "status": "uncertain_not_assessable",
      "analysis": "The declaration is emphatic, but neither the local passage nor reliably remembered wider context establishes the speaker’s private state at this exact moment. Later failure of the relationship can discredit the prediction of permanence without proving deliberate present deception.",
      "confidence": 0.82
    },
    "manipulation_pressure": {
      "status": "unsupported",
      "analysis": "The utterance is used persuasively in an apology and seeks relational repair, but the available evidence does not show coercion, a threat, or a calculated attempt to override the addressee’s agency. Emotional urgency alone is insufficient to classify it as manipulation or pressure.",
      "confidence": 0.78
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "“Je t’aime” is direct and unhedged, and the adjacent assertions make its intended romantic meaning more explicit rather than strategically ambiguous.",
      "confidence": 0.94
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“Je t’aime”",
      "supports": "A direct, unhedged present-tense avowal with very strong truth-conditional love-content.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“Ah! pardonne-moi!” and “J’ai été imbécile et méchant!”",
      "supports": "The avowal occurs within an apology and an effort to repair a relational injury.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“tu es la seule qui me plaise” and “je t’aimerai toujours”",
      "supports": "The surrounding speech strengthens the declaration through exclusivity and asserted future constancy; the latter also has limited promise-like force.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "“Qu’as-tu? dis-le donc!”",
      "supports": "The speaker perceives distress or disturbance and presses for an explanation, reinforcing the reassurance-oriented reading.",
      "confidence": 0.93
    },
    {
      "evidence_id": "E5",
      "source": "background_knowledge",
      "quotation_or_description": "In the later course of Madame Bovary, Emma’s affair with Léon deteriorates and does not fulfill its language of lasting romantic constancy.",
      "supports": "The wider narrative weakens the literal durability of “je t’aimerai toujours” and permits retrospective irony, while not conclusively proving conscious deception here.",
      "confidence": 0.8
    },
    {
      "evidence_id": "E6",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as coming from Gustave Flaubert’s Madame Bovary and is located at approximately 86.8% of the supplied source.",
      "supports": "Places the speech late in the novel, making the later-stage deterioration of the central romantic relationships potentially relevant; the metadata itself does not identify the speaker.",
      "confidence": 0.96
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "moderate",
    "confidence": 0.8,
    "contribution": "Background knowledge was used to situate the utterance likely within the late, deteriorating phase of Emma’s affair with Léon and to distinguish immediate avowal and reassurance from the ultimately unfulfilled claim of permanent love. It supports retrospective instability or irony but not a definitive finding of deliberate deceit.",
    "notes": "The local extract does not name either participant. Identification of the likely scene and speaker as Léon addressing Emma is based on remembered plot context and source position and should therefore remain somewhat uncertain."
  },
  "context_needs": [
    {
      "need": "useful_for_richer_interpretation",
      "layers": [
        "current_discourse_act",
        "participant_construals",
        "assessments",
        "disagreements"
      ],
      "claim": "Whether the apology answers a specific accusation and whether the addressee accepts or distrusts the declaration.",
      "request": "Provide the preceding exchange and the addressee’s immediate response, including any narration of gesture, tone, or thought."
    }
  ],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The scheme naturally separates the highlighted present-tense avowal from its apologetic and reassuring use and from the wider narrative’s weakening of the adjacent promise of permanence. The distinction between deception and later nonfulfillment is especially useful here.",
    "proposed_missing_dimensions": []
  },
  "notes": "The most important interpretive distinction is temporal: “Je t’aime” asserts a present state, while the adjacent “je t’aimerai toujours” projects permanence and carries somewhat greater commitment-like force. The later failure of that projection should not automatically be transferred into a finding that the present avowal is false."
}
```

</details>
