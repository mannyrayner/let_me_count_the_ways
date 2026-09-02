# Single-text pipeline report: Little Women

## Run summary

- **Run ID:** `20260902T043336Z`
- **Work:** *Little Women* by Louisa May Alcott
- **Source:** `gutenberg-514`
- **Annotation:** v0.2 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 4
- **Valid occurrences:** 4
- **Failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.314112

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `alcott-little-women-15ef9596ac4e`

- **Exact match:** `I love / you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.2)
- **Source offsets:** 249186–249196
- **Relative position:** 0.242779
- **Chapter/section:** CHAPTER TWELVE
- **Supplied context:** 312 characters (64 before; 238 after)

#### Passage

> “That’s my good girl. You do try to fight off your shyness, and I love
> you for it. Fighting faults isn’t easy, as I know, and a cheery word
> kind of gives a lift. Thank you, Mother,” And Jo gave the thin cheek a
> grateful kiss, more precious to Mrs. March than if it had given back
> the rosy roundness of her youth.

#### Annotation

- **Selected attempt:** `results\pipeline_runs\gutenberg-514\20260902T043336Z\annotations\alcott-little-women-15ef9596ac4e\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 1 / 0
- **Core analysis:** “I love you for it” directly presents Jo's love for the addressee as true and identifies the addressee's effort against shyness as a reason or occasion for the avowal. Its primary force is truth-conditional. Uttering it also weakly enacts affectionate affirmation, but it does not substantially undertake or renew an obligation or commitment, and it is not framed as a reflexive exclamation.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal, reassurance, explanation, other
- **Current-act analysis:** Jo currently avows love while praising and encouraging the addressee for trying to overcome shyness. “For it” explains the immediate basis of the praise-inflected avowal. The affectionate recognition also has a reassuring effect, but that effect does not turn the core proposition into a strong performative commitment.
- **Contextual modification:** preserves, strengthens, redirects
- **Ontology adequate:** True — The scheme naturally distinguishes the avowal's truth-conditional core from its present use as praise, reassurance, and encouragement. Participant roles also accommodate the unnamed immediate addressee and the later shift of address to Mother.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "alcott-little-women-15ef9596ac4e",
  "core_love_content": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0
    },
    "mixed_reading": {
      "is_mixed": false,
      "basis": "none",
      "justification": null
    },
    "relationship_modifier": "Sisterly love, expressed as praise for the addressee's effort to overcome shyness.",
    "analysis": "“I love you for it” directly presents Jo's love for the addressee as true and identifies the addressee's effort against shyness as a reason or occasion for the avowal. Its primary force is truth-conditional. Uttering it also weakly enacts affectionate affirmation, but it does not substantially undertake or renew an obligation or commitment, and it is not framed as a reflexive exclamation.",
    "confidence": 0.98
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The highlighted words occur within a represented spoken turn. The continuation “Thank you, Mother,” followed by Jo's action attributes the encompassing turn to Jo. The words are neither a quotation of an earlier avowal nor wording narratively supplied for nonverbal conduct.",
    "confidence": 0.96
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "reassurance",
      "explanation",
      "other"
    ],
    "other_description": "Praise and encouragement",
    "analysis": "Jo currently avows love while praising and encouraging the addressee for trying to overcome shyness. “For it” explains the immediate basis of the praise-inflected avowal. The affectionate recognition also has a reassuring effect, but that effect does not turn the core proposition into a strong performative commitment.",
    "confidence": 0.95
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens",
      "redirects"
    ],
    "other_description": null,
    "analysis": "The context preserves the avowal's ordinary literal force. “That's my good girl” and the recognition that the addressee does try strengthen its affectionate and encouraging character. “For it” redirects attention from an unqualified declaration of love to love expressed through approval of a particular moral effort; this is better read as praise than as a claim that love is strictly conditional on success.",
    "confidence": 0.94
  },
  "participant_construals": [
    {
      "role": "current_avower_Jo",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Jo presents herself as genuinely loving the addressee and uses the avowal to recognize, reassure, and encourage her. The end of the quoted turn and the following narration support Jo's identification as speaker.",
      "confidence": 0.96
    },
    {
      "role": "current_addressee_Beth",
      "discourse_level": "both",
      "status": "uncertain",
      "analysis": "The immediate addressee is not named in the supplied extract. Background knowledge that Beth is Jo's notably shy sister makes Beth the strongly probable referent of “you,” but the local passage alone does not conclusively identify her.",
      "confidence": 0.9
    },
    {
      "role": "current_addressee_response",
      "discourse_level": "both",
      "status": "unavailable",
      "analysis": "The supplied passage gives no response from the person addressed by “I love you for it,” so that person's construal of either the avowal or its encouraging purpose cannot be directly established.",
      "confidence": null
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The text presents the speech without irony, distancing, or challenge and surrounds it with affectionate family interaction, supporting a sincere avowal-and-encouragement reading.",
      "confidence": 0.94
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "A reader is strongly guided to construe the statement as a sincere sisterly avowal used to praise effort against shyness rather than as a promise, manipulation, or spontaneous cry.",
      "confidence": 0.94
    }
  ],
  "disagreements": [],
  "assessments": {
    "deception_misrepresentation": {
      "status": "unsupported",
      "analysis": "Nothing in the supplied language or reliably remembered relationship context suggests that Jo is falsely claiming love. The affectionate praise and surrounding family interaction instead support sincerity.",
      "confidence": 0.94
    },
    "manipulation_pressure": {
      "status": "unsupported",
      "analysis": "The statement encourages continued effort, but it does so through praise rather than a threat, demand, guilt tactic, or coercive condition. The wording supplies no substantial evidence of manipulative pressure.",
      "confidence": 0.92
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "Although “for it” can raise a semantic question about whether love itself or its present expression is linked to the addressee's effort, there is no evidence that Jo deliberately exploits that scope ambiguity.",
      "confidence": 0.9
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“I love you for it.”",
      "supports": "A direct truth-conditional avowal of love, with an explicitly stated reason or occasion.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“You do try to fight off your shyness” immediately precedes the highlighted avowal.",
      "supports": "The referent of “it” is the addressee's effort against shyness, making the avowal praise and encouragement rather than an unmotivated exclamation.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“That's my good girl.”",
      "supports": "The avowal occurs in an affectionate, approving, and reassuring frame.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "The quoted turn ends with “Thank you, Mother,” and is followed by “And Jo gave the thin cheek a grateful kiss.”",
      "supports": "The structure strongly identifies Jo as the speaker of the encompassing turn and establishes an affectionate family setting.",
      "confidence": 0.96
    },
    {
      "evidence_id": "E5",
      "source": "local_text",
      "quotation_or_description": "“Fighting faults isn't easy, as I know, and a cheery word kind of gives a lift.”",
      "supports": "Jo explicitly frames her speech as sympathetic encouragement intended to give emotional support.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E6",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as Chapter Twelve of Louisa May Alcott's Little Women.",
      "supports": "Establishes the work context against which remembered character identities and relationships can be cautiously applied.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E7",
      "source": "background_knowledge",
      "quotation_or_description": "In Little Women, Beth March is Jo's sister and is consistently characterized as notably shy.",
      "supports": "Makes Beth the strongly probable addressee of Jo's reference to “your shyness” and supports the sisterly relationship modifier.",
      "confidence": 0.9
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "moderate",
    "confidence": 0.9,
    "contribution": "Background knowledge was used only to identify Beth as the probable unnamed addressee and therefore to characterize the love as sisterly. The primary classification as a sincere truth-conditional avowal used for praise and encouragement follows from the local text.",
    "notes": "The identification of Beth is highly plausible because shyness is her defining trait, but the supplied extract does not itself name the immediate addressee."
  },
  "context_needs": [
    {
      "need": "useful_for_richer_interpretation",
      "layers": [
        "realisation",
        "participant_construals",
        "contextual_modification"
      ],
      "claim": "The immediate addressee is Beth, and Jo is the speaker throughout the quoted turn.",
      "request": "Provide the preceding dialogue and paragraph boundaries so that the speaker transition and the identity of the person addressed about shyness can be confirmed directly."
    }
  ],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The scheme naturally distinguishes the avowal's truth-conditional core from its present use as praise, reassurance, and encouragement. Participant roles also accommodate the unnamed immediate addressee and the later shift of address to Mother.",
    "proposed_missing_dimensions": []
  },
  "notes": "The phrase “for it” should not be overread as making Jo's love strictly conditional. In this context it most naturally marks the admired conduct that prompts the present expression of an established familial affection."
}
```

</details>

### 2. `alcott-little-women-44ca305cf65a`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.2)
- **Source offsets:** 460098–460108
- **Relative position:** 0.448267
- **Chapter/section:** CHAPTER TWENTY-THREE
- **Supplied context:** 129 characters (76 before; 43 after)

#### Passage

> “I won’t trouble you. I only want to know if you care for me a little,
> Meg. I love you so much, dear,” added Mr. Brooke tenderly.

#### Annotation

- **Selected attempt:** `results\pipeline_runs\gutenberg-514\20260902T043336Z\annotations\alcott-little-women-44ca305cf65a\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 1 / 0
- **Core analysis:** Mr. Brooke explicitly presents his intense romantic love for Meg as true. The first-person present-tense wording, intensified by “so much,” strongly supports a truth-conditional avowal. In this courtship setting the declaration has relational consequences, but it does not itself clearly undertake or renew an obligation, so its core performative support remains weak. Its complete proposition and the narrator’s attribution make a substantially reflexive or merely exclamatory reading unsupported.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal, reassurance, other
- **Current-act analysis:** Mr. Brooke directly avows love and assures Meg of its intensity. In conjunction with his request to know whether she cares for him, the avowal also functions as a courtship appeal inviting a reciprocal answer. This is not precisely “elicitation_of_reaffirmation,” because the passage does not establish that Meg has previously affirmed love.
- **Contextual modification:** preserves, strengthens
- **Ontology adequate:** False — The scheme gives a natural account of the core avowal and its direct-speech realization, but the current-act inventory distinguishes elicitation of reaffirmation without offering the more appropriate category of eliciting an initial reciprocal disclosure. Consequently, the courtship appeal must be placed under “other.”

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "alcott-little-women-44ca305cf65a",
  "core_love_content": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0
    },
    "mixed_reading": {
      "is_mixed": false,
      "basis": "none",
      "justification": null
    },
    "relationship_modifier": "Romantic love expressed during courtship",
    "analysis": "Mr. Brooke explicitly presents his intense romantic love for Meg as true. The first-person present-tense wording, intensified by “so much,” strongly supports a truth-conditional avowal. In this courtship setting the declaration has relational consequences, but it does not itself clearly undertake or renew an obligation, so its core performative support remains weak. Its complete proposition and the narrator’s attribution make a substantially reflexive or merely exclamatory reading unsupported.",
    "confidence": 0.98
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The words are represented as being spoken by Mr. Brooke to Meg in the current fictional scene. The attribution “added Mr. Brooke tenderly” confirms direct represented speech rather than quotation of an earlier or hypothetical utterance.",
    "confidence": 0.99
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "reassurance",
      "other"
    ],
    "other_description": "Courtship appeal seeking a reciprocal disclosure of feeling",
    "analysis": "Mr. Brooke directly avows love and assures Meg of its intensity. In conjunction with his request to know whether she cares for him, the avowal also functions as a courtship appeal inviting a reciprocal answer. This is not precisely “elicitation_of_reaffirmation,” because the passage does not establish that Meg has previously affirmed love.",
    "confidence": 0.95
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens"
    ],
    "other_description": null,
    "analysis": "Nothing in the embedding negates, quotes, distances, or challenges the avowal. “So much,” the address “dear,” and the narrator’s description “tenderly” strengthen its emotional intensity and apparent sincerity. The preceding request to know whether Meg cares places the avowal within an appeal for reciprocity without changing its basic assertion of love.",
    "confidence": 0.96
  },
  "participant_construals": [
    {
      "role": "original_avower_and_current_speaker_Mr_Brooke",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Mr. Brooke presents the statement as a sincere declaration of intense romantic love and uses it while asking whether Meg reciprocates.",
      "confidence": 0.97
    },
    {
      "role": "current_addressee_Meg",
      "discourse_level": "both",
      "status": "uncertain",
      "analysis": "The supplied excerpt does not include Meg’s response, so her immediate construal cannot be directly observed. The wider courtship and eventual marriage make it likely that she understands this as a serious romantic avowal, but they do not by themselves establish her precise reaction at this moment.",
      "confidence": 0.76
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The narrator attributes the words directly to Mr. Brooke and characterizes their delivery as tender, framing them as emotionally sincere rather than ironic or detached.",
      "confidence": 0.97
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The local wording and narrator’s tonal cue strongly invite the reader to construe the statement as a sincere romantic avowal embedded in a request for reciprocity.",
      "confidence": 0.95
    }
  ],
  "disagreements": [],
  "assessments": {
    "deception_misrepresentation": {
      "status": "unsupported",
      "analysis": "The local text frames the declaration tenderly and supplies no sign of lying, irony, or concealed contrary feeling. The wider relationship trajectory also supports Mr. Brooke’s continuing attachment to Meg.",
      "confidence": 0.94
    },
    "manipulation_pressure": {
      "status": "unsupported",
      "analysis": "The declaration accompanies a request for Meg to disclose whether she cares, creating some ordinary interpersonal pressure inherent in courtship, but the available evidence does not support manipulation or coercive pressure. “I won’t trouble you” and “I only want to know” explicitly soften the request.",
      "confidence": 0.84
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "“I love you so much” is direct and unhedged about Mr. Brooke’s own feeling. His softer formulation “care for me a little” concerns the answer he seeks from Meg, not an ambiguity in his avowal.",
      "confidence": 0.93
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“I love you so much, dear”",
      "supports": "Strong truth-conditional romantic avowal, intensified affection, and lack of hedging or negation.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“I only want to know if you care for me a little, Meg.”",
      "supports": "The avowal occurs within a courtship appeal seeking disclosure of reciprocal feeling.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“added Mr. Brooke tenderly”",
      "supports": "Identifies Mr. Brooke as the current speaker, establishes that the words are spoken, and frames their delivery as tender and apparently sincere.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "“I won’t trouble you.”",
      "supports": "Shows an explicit attempt to soften the request and weighs against a strong pressure or coercion interpretation.",
      "confidence": 0.94
    },
    {
      "evidence_id": "E5",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as appearing in Louisa May Alcott’s Little Women, Chapter Twenty-Three.",
      "supports": "Links the local passage to the remembered wider courtship narrative used in the background assessment.",
      "confidence": 1.0
    },
    {
      "evidence_id": "E6",
      "source": "background_knowledge",
      "quotation_or_description": "In the wider novel, John Brooke and Meg’s courtship leads to an engagement and later marriage.",
      "supports": "Corroborates the romantic relationship modifier and weighs against interpreting the avowal as deceptive or merely casual.",
      "confidence": 0.91
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "moderate",
    "confidence": 0.91,
    "contribution": "The remembered trajectory of John Brooke and Meg’s courtship, engagement, and marriage supports treating the love as romantic and the avowal as sincere rather than deceptive. The core classification itself is already strongly established by the supplied local text.",
    "notes": "No remembered exact wording outside the supplied passage is relied upon."
  },
  "context_needs": [
    {
      "need": "useful_for_richer_interpretation",
      "layers": [
        "participant_construals",
        "current_discourse_act",
        "assessments"
      ],
      "claim": "Meg’s immediate understanding and response, and the precise degree of interpersonal pressure in the exchange.",
      "request": "Provide the dialogue immediately following the excerpt, including Meg’s response, and enough preceding scene context to show how Mr. Brooke came to ask the question."
    }
  ],
  "ontology_assessment": {
    "adequate": false,
    "diagnosis": "The scheme gives a natural account of the core avowal and its direct-speech realization, but the current-act inventory distinguishes elicitation of reaffirmation without offering the more appropriate category of eliciting an initial reciprocal disclosure. Consequently, the courtship appeal must be placed under “other.”",
    "proposed_missing_dimensions": [
      "Elicitation of reciprocal feeling or initial reciprocal avowal",
      "Courtship appeal or proposal-related relational function distinct from core performative commitment"
    ]
  },
  "notes": "The avowal is relationally consequential because it occurs during courtship, but that consequence should not be inflated into strong core performative force: the sentence principally states Mr. Brooke’s feeling and supports his request for Meg’s answer."
}
```

</details>

### 3. `alcott-little-women-58c41f8731dd`

- **Exact match:** `I love / you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.2)
- **Source offsets:** 514237–514247
- **Relative position:** 0.501014
- **Chapter/section:** CHAPTER TWENTY-FIVE
- **Supplied context:** 467 characters (63 before; 394 after)

#### Passage

> “Don’t feel that I am separated from you, Marmee dear, or that I love
> you any the less for loving John so much,” she said, clinging to her
> mother, with full eyes for a moment. “I shall come every day, Father,
> and expect to keep my old place in all your hearts, though I am
> married. Beth is going to be with me a great deal, and the other girls
> will drop in now and then to laugh at my housekeeping struggles. Thank
> you all for my happy wedding day. Good-by, good-by!”

#### Annotation

- **Selected attempt:** `results\pipeline_runs\gutenberg-514\20260902T043336Z\annotations\alcott-little-women-58c41f8731dd\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 1 / 0
- **Core analysis:** Although the words occur inside the negative directive “Don’t feel ... that I love you any the less,” the speaker is not denying love; she strongly avows that her love for her mother has not diminished. The principal content is therefore truth-conditional. The surrounding promises of continued visits and family belonging give slight commitment-like resonance, but the love-content itself does not substantially undertake a new obligation or relationship.
- **Realisation:** direct_represented_speech, negated (actuality: spoken)
- **Current discourse act:** direct_avowal, reassurance, explanation
- **Current-act analysis:** The speaker avows continuing love while reassuring her mother that marriage and intense love for John do not separate her emotionally from her family. “For loving John so much” explains the circumstance that might otherwise prompt fear of diminished filial attachment. The subsequent statements about daily visits and retaining her old place in the family's hearts reinforce this reassurance.
- **Contextual modification:** preserves, strengthens, redirects
- **Ontology adequate:** True — The scheme naturally distinguishes the affirmative core avowal from its negative-comparative embedding and from its present discourse function as reassurance. The multi-valued realisation and contextual-effect fields adequately capture that apparent negation actually rejects diminished love.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "alcott-little-women-58c41f8731dd",
  "core_love_content": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0
    },
    "mixed_reading": {
      "is_mixed": false,
      "basis": "none",
      "justification": null
    },
    "relationship_modifier": "Filial love from a daughter to her mother, explicitly presented as undiminished by the daughter's marital love for John.",
    "analysis": "Although the words occur inside the negative directive “Don’t feel ... that I love you any the less,” the speaker is not denying love; she strongly avows that her love for her mother has not diminished. The principal content is therefore truth-conditional. The surrounding promises of continued visits and family belonging give slight commitment-like resonance, but the love-content itself does not substantially undertake a new obligation or relationship.",
    "confidence": 0.98
  },
  "realisation": {
    "types": [
      "direct_represented_speech",
      "negated"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The narrator explicitly attributes the quoted words to the speaker with “she said,” so this is current spoken dialogue in the fictional world. Negation operates at the level of the directive and comparative proposition: the mother is told not to believe that the speaker loves her less. Thus the embedding reverses a possible diminished-love inference rather than negating the existence of love.",
    "confidence": 0.99
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "reassurance",
      "explanation"
    ],
    "other_description": null,
    "analysis": "The speaker avows continuing love while reassuring her mother that marriage and intense love for John do not separate her emotionally from her family. “For loving John so much” explains the circumstance that might otherwise prompt fear of diminished filial attachment. The subsequent statements about daily visits and retaining her old place in the family's hearts reinforce this reassurance.",
    "confidence": 0.98
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens",
      "redirects"
    ],
    "other_description": null,
    "analysis": "The negative-comparative frame preserves the affirmative love-content by rejecting diminution: she loves her mother no less than before. “Marmee dear,” physical clinging, tearful eyes, and plans for continued contact strengthen the sincerity and emotional salience of the avowal. The context redirects a generic declaration into a specific reassurance that marital love will not displace filial love or family membership.",
    "confidence": 0.97
  },
  "participant_construals": [
    {
      "role": "current_speaker_and_original_avower (Meg)",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Meg presents her filial love as continuing undiminished and uses that avowal to reassure her mother at the moment of her marriage.",
      "confidence": 0.97
    },
    {
      "role": "current_addressee (Marmee)",
      "discourse_level": "both",
      "status": "unavailable",
      "analysis": "The passage identifies Marmee as the addressee but does not provide her verbal response or interior reaction, so her actual construal of the reassurance is unavailable.",
      "confidence": null
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The narration frames the speech with clinging and full eyes, supporting an earnest, emotionally affected reassurance rather than an ironic or merely formulaic declaration.",
      "confidence": 0.96
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "A reader is strongly guided to understand the clause as an avowal of undiminished filial love and as reassurance about continuity of family bonds after marriage.",
      "confidence": 0.97
    }
  ],
  "disagreements": [],
  "assessments": {
    "deception_misrepresentation": {
      "status": "unsupported",
      "analysis": "Nothing in the supplied passage suggests that the speaker is falsely representing her affection. Her emotional behaviour and concrete plans for continued family contact support sincerity.",
      "confidence": 0.95
    },
    "manipulation_pressure": {
      "status": "unsupported",
      "analysis": "The imperative “Don’t feel” directs the mother's interpretation, but its evident function is affectionate reassurance rather than coercion, pressure, or exploitative manipulation.",
      "confidence": 0.94
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "The comparative construction is semantically indirect but pragmatically clear: marital love for John has not reduced the speaker's love for her mother. There is no supported indication that ambiguity is being maintained for strategic purposes.",
      "confidence": 0.96
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“Don’t feel that I am separated from you, Marmee dear, or that I love you any the less for loving John so much”",
      "supports": "The love-content is an avowal of undiminished filial love embedded in a directive intended to reassure the mother despite the speaker's marital love.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“she said, clinging to her mother, with full eyes for a moment”",
      "supports": "The words are represented as actually spoken, and the accompanying emotional behaviour supports earnestness and affective intensity.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“I shall come every day, Father, and expect to keep my old place in all your hearts, though I am married.”",
      "supports": "The wider discourse act reassures the family that marriage will not end emotional belonging or regular contact.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "The speaker calls the occasion “my happy wedding day” and says goodbye to her family.",
      "supports": "The avowal occurs during a marital transition that could prompt concern about separation, explaining its continuity-focused form.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E5",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is in Louisa May Alcott's Little Women, Chapter Twenty-Five.",
      "supports": "This identifies the work and chapter context without treating the metadata as passage wording.",
      "confidence": 1.0
    },
    {
      "evidence_id": "E6",
      "source": "background_knowledge",
      "quotation_or_description": "In Little Women, Chapter Twenty-Five concerns Meg March's wedding to John Brooke; Marmee is the March sisters' mother.",
      "supports": "This identifies the otherwise unnamed female speaker as Meg and clarifies John as her new husband and the love contrast as marital versus filial.",
      "confidence": 0.97
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.97,
    "contribution": "Background knowledge identifies the speaker as Meg March and John as John Brooke, her husband, confirming that the passage occurs at Meg's wedding and contrasts marital with filial love.",
    "notes": "The core classification does not depend on this knowledge because the local text already establishes a daughter addressing her mother on her wedding day; background knowledge mainly supplies names and wider-work continuity."
  },
  "context_needs": [],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The scheme naturally distinguishes the affirmative core avowal from its negative-comparative embedding and from its present discourse function as reassurance. The multi-valued realisation and contextual-effect fields adequately capture that apparent negation actually rejects diminished love.",
    "proposed_missing_dimensions": []
  },
  "notes": "The phrase “I love you” should not be isolated from “Don’t feel ... any the less”: the construction communicates continued, undiminished love rather than either a simple unqualified declaration or a denial of love."
}
```

</details>

### 4. `alcott-little-women-f1eab387a74e`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.2)
- **Source offsets:** 939298–939308
- **Relative position:** 0.915145
- **Chapter/section:** CHAPTER FORTY-FOUR
- **Supplied context:** 322 characters (192 before; 120 after)

#### Passage

> “Oh, my dearest boy, don’t, don’t say that! I forgot you were rich when
> I said ‘Yes’. I’d have married you if you hadn’t a penny, and I
> sometimes wish you were poor that I might show how much I love you.”
> And Amy, who was very dignified in public and very fond in private,
> gave convincing proofs of the truth of her words.

#### Annotation

- **Selected attempt:** `results\pipeline_runs\gutenberg-514\20260902T043336Z\annotations\alcott-little-women-f1eab387a74e\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 1 / 0
- **Core analysis:** Amy presents her love for the addressee as an existing and substantial emotional state. The degree construction “how much I love you” presupposes or asserts love while emphasizing its magnitude. Although saying this also reassures and relationally reaffirms the addressee, it does not substantially create or undertake a new commitment, so its performative support is weak. The utterance is emotionally emphatic but remains propositionally controlled rather than reflex-like.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal, reassurance, explanation
- **Current-act analysis:** Amy directly avows love while reassuring the addressee that his wealth did not motivate her acceptance. Her willingness to have married him penniless and her wish for an opportunity to prove her love explain and support that reassurance.
- **Contextual modification:** preserves, strengthens
- **Ontology adequate:** True — The scheme naturally distinguishes the proposition that Amy loves the addressee from her present acts of reassurance and explanation, and contextual strengthening captures the narrator’s explicit corroboration. The degree emphasis in “how much” is important but can be preserved in analysis without forcing an exclamatory/reflexive classification.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "alcott-little-women-f1eab387a74e",
  "core_love_content": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0
    },
    "mixed_reading": {
      "is_mixed": false,
      "basis": "none",
      "justification": null
    },
    "relationship_modifier": "Romantic and marital love, explicitly contrasted with financial interest.",
    "analysis": "Amy presents her love for the addressee as an existing and substantial emotional state. The degree construction “how much I love you” presupposes or asserts love while emphasizing its magnitude. Although saying this also reassures and relationally reaffirms the addressee, it does not substantially create or undertake a new commitment, so its performative support is weak. The utterance is emotionally emphatic but remains propositionally controlled rather than reflex-like.",
    "confidence": 0.98
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The matched words occur within Amy’s presently represented spoken dialogue. The imagined poverty concerns circumstances in which she could demonstrate her love; it does not make the love itself hypothetical. The printed quotation around “Yes” revoices an earlier acceptance, but the matched love-content is not that quotation.",
    "confidence": 0.99
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "reassurance",
      "explanation"
    ],
    "other_description": null,
    "analysis": "Amy directly avows love while reassuring the addressee that his wealth did not motivate her acceptance. Her willingness to have married him penniless and her wish for an opportunity to prove her love explain and support that reassurance.",
    "confidence": 0.97
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens"
    ],
    "other_description": null,
    "analysis": "The wish construction redirects hypothetical force toward an imagined opportunity to demonstrate love, while preserving the love as a present reality. Amy’s claim that she would have married him without money strengthens the avowal by excluding mercenary motivation. The narrator further strengthens it by describing her subsequent affectionate behavior as “convincing proofs of the truth of her words.”",
    "confidence": 0.99
  },
  "participant_construals": [
    {
      "role": "original_avower_and_current_speaker_Amy",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Amy presents herself as genuinely loving the addressee and uses that avowal to deny that wealth motivated her acceptance.",
      "confidence": 0.99
    },
    {
      "role": "current_addressee_Laurie",
      "discourse_level": "both",
      "status": "unavailable",
      "analysis": "Background knowledge identifies the addressee as Laurie, but the supplied passage does not include his response or establish exactly how he construes Amy’s avowal and reassurance.",
      "confidence": null
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The narrator explicitly endorses Amy’s words as truthful and treats her private affection as behavioral proof of them.",
      "confidence": 0.99
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The reader is strongly guided to accept both Amy’s love and the sincerity of her reassurance because the narrator supplies explicit corroboration.",
      "confidence": 0.97
    }
  ],
  "disagreements": [],
  "assessments": {
    "deception_misrepresentation": {
      "status": "unsupported",
      "analysis": "The passage weighs directly against deception: Amy offers a counterfactual test of her motives, and the narrator calls her subsequent behavior convincing proof that her words are true.",
      "confidence": 0.99
    },
    "manipulation_pressure": {
      "status": "unsupported",
      "analysis": "Amy is responding emphatically to a concern and seeking to reassure the addressee, but the available text provides no support for coercion, pressure, or manipulative use of the avowal.",
      "confidence": 0.96
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "The referent, emotional claim, and argumentative purpose are comparatively explicit. The degree phrase intensifies love rather than strategically obscuring its meaning.",
      "confidence": 0.97
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“how much I love you”",
      "supports": "The matched expression presents Amy’s loving emotional state as real and emphasizes its degree.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“I forgot you were rich when I said ‘Yes’.”",
      "supports": "Amy denies that awareness of the addressee’s wealth motivated her acceptance and frames the love-avowal as reassurance and explanation.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“I’d have married you if you hadn’t a penny”",
      "supports": "The counterfactual claim strengthens the avowal by presenting Amy’s romantic commitment as independent of wealth.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "“I sometimes wish you were poor that I might show how much I love you.”",
      "supports": "The hypothetical poverty concerns an opportunity to demonstrate love rather than the actuality of the love itself.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E5",
      "source": "local_text",
      "quotation_or_description": "“Amy, who was very dignified in public and very fond in private, gave convincing proofs of the truth of her words.”",
      "supports": "The narrator explicitly corroborates Amy’s sincerity and strengthens the truth-conditional interpretation.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E6",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is in Louisa May Alcott’s Little Women, Chapter Forty-Four, near relative position 0.915.",
      "supports": "The metadata locates the exchange late in the novel and identifies the work and author; it does not itself supply passage wording.",
      "confidence": 1.0
    },
    {
      "evidence_id": "E7",
      "source": "background_knowledge",
      "quotation_or_description": "In the wider novel, Amy’s romantic partner and eventual husband is Theodore “Laurie” Laurence; Chapter Forty-Four concerns their relationship after their union.",
      "supports": "This identifies the otherwise unnamed addressee and supports describing the love as romantic and marital.",
      "confidence": 0.93
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.93,
    "contribution": "Background knowledge was used to identify Amy’s addressee as Laurie and to characterize their relationship as romantic and marital. The core classification and sincerity judgment do not depend on this knowledge because the local passage itself supplies strong evidence.",
    "notes": "The precise legal or chronological stage of the marriage at this sentence is not needed for classification; the local references to accepting him and marrying him already establish the romantic context."
  },
  "context_needs": [],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The scheme naturally distinguishes the proposition that Amy loves the addressee from her present acts of reassurance and explanation, and contextual strengthening captures the narrator’s explicit corroboration. The degree emphasis in “how much” is important but can be preserved in analysis without forcing an exclamatory/reflexive classification.",
    "proposed_missing_dimensions": []
  },
  "notes": "The sentence contains counterfactual material, but its scope is crucial: poverty and the opportunity to demonstrate love are imagined, whereas Amy’s love is represented as presently true. The narrator’s immediate behavioral authentication makes this an unusually explicit case of narratively endorsed sincerity."
}
```

</details>
