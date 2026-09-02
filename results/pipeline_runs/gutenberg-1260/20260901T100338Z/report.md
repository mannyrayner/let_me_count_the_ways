# Single-text pipeline report: Jane Eyre

## Run summary

- **Run ID:** `20260901T100338Z`
- **Work:** *Jane Eyre* by Charlotte Brontë
- **Source:** `gutenberg-1260`
- **Annotation:** v0.2 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 6
- **Valid occurrences:** 6
- **Failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.542360

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `bronte-jane-eyre-d0cd60fde247`

- **Exact match:** `I love you`
- **Pattern:** `en_i_love_you` (v0.1)
- **Source offsets:** 581886–581896
- **Relative position:** 0.558577
- **Chapter/section:** CHAPTER XXIV
- **Supplied context:** 368 characters (295 before; 63 after)

#### Passage

> “And then you won’t know me, sir; and I shall not be your Jane Eyre any
> longer, but an ape in a harlequin’s jacket—a jay in borrowed plumes. I
> would as soon see you, Mr. Rochester, tricked out in stage-trappings,
> as myself clad in a court-lady’s robe; and I don’t call you handsome,
> sir, though I love you most dearly: far too dearly to flatter you.
> Don’t flatter me.”

#### Annotation

- **Selected attempt:** `results\pipeline_runs\gutenberg-1260\20260901T100338Z\annotations\bronte-jane-eyre-d0cd60fde247\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 1 / 0
- **Core analysis:** Jane explicitly presents her love for Rochester as true and intensifies it with “most dearly” and “far too dearly.” The clause is a sincere avowal embedded in an argument that genuine love requires honesty rather than flattery. Its direct interpersonal delivery gives it slight commitment-enacting force, but it does not substantially undertake or renew an obligation, and it is not primarily a reflexive exclamation.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal, reassurance, explanation, use_as_evidence, other
- **Current-act analysis:** Jane avows love while explaining why she refuses to flatter Rochester: loving him deeply is offered as a reason for speaking candidly. The avowal also reassures him that her refusal to call him handsome is not emotional rejection. Within the larger exchange, she uses the love-content to support an admonition that neither partner should disguise or idealise the other.
- **Contextual modification:** preserves, strengthens, redirects, challenges
- **Ontology adequate:** True — The layered scheme naturally distinguishes the sincere propositional avowal from its present rhetorical uses as reassurance, explanation, evidence, and admonition. The open-text fields adequately preserve the important connection between love, candour, identity, and resistance to idealisation.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "bronte-jane-eyre-d0cd60fde247",
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
    "relationship_modifier": "Romantic love between engaged partners, framed as compatible with candour, equality, and resistance to idealising transformation.",
    "analysis": "Jane explicitly presents her love for Rochester as true and intensifies it with “most dearly” and “far too dearly.” The clause is a sincere avowal embedded in an argument that genuine love requires honesty rather than flattery. Its direct interpersonal delivery gives it slight commitment-enacting force, but it does not substantially undertake or renew an obligation, and it is not primarily a reflexive exclamation.",
    "confidence": 0.98
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The highlighted words are represented as being spoken by Jane directly to Mr. Rochester in the current fictional scene. They are neither a quotation of an earlier avowal nor wording narratively supplied for nonverbal conduct.",
    "confidence": 0.99
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "reassurance",
      "explanation",
      "use_as_evidence",
      "other"
    ],
    "other_description": "A candid admonition against flattery and against transforming Jane into an ornamental social persona.",
    "analysis": "Jane avows love while explaining why she refuses to flatter Rochester: loving him deeply is offered as a reason for speaking candidly. The avowal also reassures him that her refusal to call him handsome is not emotional rejection. Within the larger exchange, she uses the love-content to support an admonition that neither partner should disguise or idealise the other.",
    "confidence": 0.96
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens",
      "redirects",
      "challenges"
    ],
    "other_description": null,
    "analysis": "The concessive “though” preserves the avowal despite Jane's refusal to praise Rochester's appearance. “Most dearly” and “far too dearly” strengthen the represented feeling. The surrounding argument redirects the avowal toward a defence of candour and challenges any assumption that romantic love should entail flattery, ornamental display, or loss of authentic identity.",
    "confidence": 0.97
  },
  "participant_construals": [
    {
      "role": "original_avower_and_current_speaker_Jane",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Jane presents her love as sincere and treats its depth as the reason she must be truthful rather than flattering. She also uses the avowal within her resistance to being made into someone Rochester would no longer genuinely know.",
      "confidence": 0.98
    },
    {
      "role": "current_addressee_Rochester",
      "discourse_level": "both",
      "status": "unavailable",
      "analysis": "The excerpt identifies Rochester as the addressee but does not provide his response or otherwise establish how he construes either the avowal or Jane's admonition at this moment.",
      "confidence": null
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The text frames the avowal as part of Jane's coherent first-person argument: love is distinguished from flattery and aligned with truthful mutual recognition.",
      "confidence": 0.95
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The emphatic wording and its integration into Jane's principled argument strongly support a reading of sincere love coupled with resistance to romantic idealisation.",
      "confidence": 0.95
    }
  ],
  "disagreements": [
    {
      "parties": [
        "current_speaker_Jane",
        "current_addressee_Rochester"
      ],
      "subject": "Whether their romantic relationship should transform Jane's appearance and social presentation",
      "description": "Jane resists the ornamental court-lady role apparently being proposed for her and insists that love should preserve authentic recognition rather than encourage costume, display, or flattery.",
      "evidence_ids": [
        "E3",
        "E5"
      ],
      "confidence": 0.9
    }
  ],
  "assessments": {
    "deception_misrepresentation": {
      "status": "unsupported",
      "analysis": "The emphatic avowal is consistent with Jane's surrounding insistence on honesty, and neither the local passage nor reliable knowledge of the scene suggests that she is falsely claiming to love Rochester.",
      "confidence": 0.97
    },
    "manipulation_pressure": {
      "status": "unsupported",
      "analysis": "Jane is forceful and issues the imperative “Don’t flatter me,” but the love-content primarily explains and legitimates candour rather than coercing Rochester through affection or threatening withdrawal.",
      "confidence": 0.9
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "The proposition and its interpersonal purpose are unusually explicit: Jane says she loves Rochester deeply while distinguishing that love from flattering judgments about his appearance.",
      "confidence": 0.95
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“though I love you most dearly”",
      "supports": "The highlighted content is an explicit, intensified truth-conditional avowal of love addressed to Rochester.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“far too dearly to flatter you”",
      "supports": "Jane makes the depth of her love an explanation and evidential basis for refusing insincere praise.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "Jane says she would become “an ape in a harlequin’s jacket—a jay in borrowed plumes” and concludes, “Don’t flatter me.”",
      "supports": "The avowal occurs within resistance to ornamental transformation, idealisation, and flattery, redirecting it toward authenticity and candid mutual recognition.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as Charlotte Brontë's Jane Eyre, Chapter XXIV.",
      "supports": "This locates the exchange in the named work and chapter, allowing cautious use of remembered engagement-period context without treating metadata as passage wording.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E5",
      "source": "background_knowledge",
      "quotation_or_description": "Chapter XXIV occurs during Jane and Rochester's engagement, when Rochester proposes expensive clothes and ornaments and Jane resists being remade into a decorative or socially elevated version of herself.",
      "supports": "The wider scene confirms that Jane's avowal operates within a conflict about adornment, identity, equality, and romantic idealisation rather than constituting a new pledge.",
      "confidence": 0.94
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.94,
    "contribution": "Background knowledge identifies this as an engagement-period exchange in which Rochester's plans to dress and ornament Jane provoke her concern that he will replace the real Jane with an artificial social persona. This strengthens the interpretation of the avowal as sincere but rhetorically directed toward preserving equality, identity, and candour.",
    "notes": "The core truth-conditional classification is independently secure from the supplied passage. Background knowledge is used chiefly for the precise relational setting and the broader source of the disagreement."
  },
  "context_needs": [],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The layered scheme naturally distinguishes the sincere propositional avowal from its present rhetorical uses as reassurance, explanation, evidence, and admonition. The open-text fields adequately preserve the important connection between love, candour, identity, and resistance to idealisation.",
    "proposed_missing_dimensions": []
  },
  "notes": "The concessive construction is crucial: Jane does not retract or weaken her love when denying that Rochester is handsome. Instead, she separates sincere love from flattering evaluation and presents truthful recognition as a consequence of loving deeply."
}
```

</details>

### 2. `bronte-jane-eyre-9267e616f948`

- **Exact match:** `I love you`
- **Pattern:** `en_i_love_you` (v0.1)
- **Source offsets:** 627702–627712
- **Relative position:** 0.602557
- **Chapter/section:** CHAPTER XXV
- **Supplied context:** 1258 characters (248 before; 1000 after)

#### Passage

> “All day yesterday I was very busy, and very happy in my ceaseless
> bustle; for I am not, as you seem to think, troubled by any haunting
> fears about the new sphere, et cetera: I think it a glorious thing to
> have the hope of living with you, because I love you. No, sir, don’t
> caress me now—let me talk undisturbed. Yesterday I trusted well in
> Providence, and believed that events were working together for your
> good and mine: it was a fine day, if you recollect—the calmness of the
> air and sky forbade apprehensions respecting your safety or comfort on
> your journey. I walked a little while on the pavement after tea,
> thinking of you; and I beheld you in imagination so near me, I scarcely
> missed your actual presence. I thought of the life that lay before
> me—_your_ life, sir—an existence more expansive and stirring than my
> own: as much more so as the depths of the sea to which the brook runs
> are than the shallows of its own strait channel. I wondered why
> moralists call this world a dreary wilderness: for me it blossomed like
> a rose. Just at sunset, the air turned cold and the sky cloudy: I went
> in, Sophie called me upstairs to look at my wedding-dress, which they
> had just brought; and under it in the box I found your present—the veil
> which, in your

#### Annotation

- **Selected attempt:** `results\pipeline_runs\gutenberg-1260\20260901T100338Z\annotations\bronte-jane-eyre-9267e616f948\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 1 / 0
- **Core analysis:** Jane explicitly presents her love for Rochester as a true emotional state and as the reason she welcomes the prospect of living with him. The causal construction, “because I love you,” gives the avowal unusually clear propositional and explanatory force. Although spoken within an engagement and capable of reaffirming intimacy, the clause does not itself substantially undertake or renew the marriage commitment. Jane's request to be allowed to continue talking undisturbed also weighs against treating it as a reflexive exclamation.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal, explanation, reassurance
- **Current-act analysis:** Jane directly avows love while explaining why she considers the prospect of living with Rochester “a glorious thing.” In the surrounding exchange she also counters Rochester's apparent belief that she is troubled by fears, so the avowal contributes to reassurance that her anticipated life with him is genuinely desired. Its explanatory and reassuring effects do not make the core proposition strongly performative.
- **Contextual modification:** preserves, strengthens, redirects, other
- **Ontology adequate:** True — The scheme naturally distinguishes the sincere truth-conditional avowal from its explanatory and reassuring discourse functions and from the dramatic irony surrounding the proposed marriage. The open-text contextual effect is useful because dramatic irony is not a dedicated inventory value.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "bronte-jane-eyre-9267e616f948",
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
    "relationship_modifier": "Romantic love within an engagement and anticipated marriage",
    "analysis": "Jane explicitly presents her love for Rochester as a true emotional state and as the reason she welcomes the prospect of living with him. The causal construction, “because I love you,” gives the avowal unusually clear propositional and explanatory force. Although spoken within an engagement and capable of reaffirming intimacy, the clause does not itself substantially undertake or renew the marriage commitment. Jane's request to be allowed to continue talking undisturbed also weighs against treating it as a reflexive exclamation.",
    "confidence": 0.99
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The words are represented as being spoken directly by Jane to Rochester in the current fictional scene. They are not a quotation of an earlier avowal, an imagined utterance, or narrator-supplied wording for nonverbal conduct.",
    "confidence": 0.99
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "explanation",
      "reassurance"
    ],
    "other_description": null,
    "analysis": "Jane directly avows love while explaining why she considers the prospect of living with Rochester “a glorious thing.” In the surrounding exchange she also counters Rochester's apparent belief that she is troubled by fears, so the avowal contributes to reassurance that her anticipated life with him is genuinely desired. Its explanatory and reassuring effects do not make the core proposition strongly performative.",
    "confidence": 0.97
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens",
      "redirects",
      "other"
    ],
    "other_description": "Dramatic irony concerning the anticipated marriage and shared future",
    "analysis": "The immediate context preserves and strengthens the avowal through Jane's sustained descriptions of happiness, thoughts of Rochester, and imaginative investment in their future. Background knowledge of Rochester's existing marriage does not undermine Jane's sincerity, but redirects the implications of her stated hope: the apparently uncomplicated shared future is already threatened by a fact concealed from her, producing dramatic irony.",
    "confidence": 0.95
  },
  "participant_construals": [
    {
      "role": "original_avower_Jane",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Jane presents her love as sincere, settled, and explanatory of her happiness and desire to live with Rochester. Her extended, controlled account indicates deliberate avowal rather than an involuntary outburst.",
      "confidence": 0.99
    },
    {
      "role": "current_addressee_Rochester",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Rochester is the addressed “you” and is positioned to receive the clause as a direct avowal and reassurance. His apparent attempt to caress Jane suggests an affectionate response, although the passage does not explicitly state his private interpretation.",
      "confidence": 0.9
    },
    {
      "role": "retrospective_narrator_Jane",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The first-person narrator represents the earlier Jane's avowal without verbal distancing or retrospective denial of its sincerity, while the wider narrative context gives the surrounding hopes dramatic irony.",
      "confidence": 0.94
    },
    {
      "role": "informed_reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "A reader aware of Rochester's existing marriage can accept Jane's love as sincere while recognizing that her confidence in the imminent marriage and shared future rests on incomplete information.",
      "confidence": 0.97
    }
  ],
  "disagreements": [
    {
      "parties": [
        "original_avower_Jane",
        "current_addressee_Rochester"
      ],
      "subject": "The known conditions and legitimacy of the anticipated marriage",
      "description": "Jane understands the projected shared life as an ordinary forthcoming marriage, whereas Rochester knows that his existing marriage creates a concealed legal and moral impediment. This disagreement affects the future invoked around the avowal, not the sincerity of Jane's love.",
      "evidence_ids": [
        "E1",
        "E4",
        "E6"
      ],
      "confidence": 0.97
    }
  ],
  "assessments": {
    "deception_misrepresentation": {
      "status": "unsupported",
      "analysis": "There is no support for Jane misrepresenting her love; the local passage strongly supports sincerity. Rochester's background deception about his marital status shapes the surrounding engagement, but he is not the speaker of the highlighted avowal and does not make its love-content deceptive.",
      "confidence": 0.98
    },
    "manipulation_pressure": {
      "status": "unsupported",
      "analysis": "Jane uses the avowal to explain and reassure, not to extract a promise or pressure Rochester. Her request that he stop caressing her and let her speak undisturbed further presents her as controlling the conditions of her own discourse rather than manipulating him.",
      "confidence": 0.96
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "The clause is explicit about both the emotional state and its object. Its placement as the reason for wanting to live with Rochester leaves little evidence of calculated ambiguity.",
      "confidence": 0.99
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“I think it a glorious thing to have the hope of living with you, because I love you.”",
      "supports": "The highlighted words explicitly assert love and causally explain Jane's welcome of a shared life.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“No, sir, don’t caress me now—let me talk undisturbed.”",
      "supports": "Jane is engaged in deliberate, controlled speech rather than merely producing a reflexive emotional exclamation; it also suggests an affectionate response from Rochester.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "Jane says that she was “very happy,” thought of Rochester, imagined him near her, and contemplated the life before her.",
      "supports": "The extended emotional and imaginative context strengthens the sincerity and stability of the avowed love.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "The passage refers to Jane's wedding-dress and Rochester's gift of a veil.",
      "supports": "The avowal occurs within an engagement and anticipated marriage, while the marriage context does not by itself turn the clause into a performative undertaking.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E5",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is identified as appearing in Charlotte Brontë's Jane Eyre, Chapter XXV.",
      "supports": "Identifies the work and narrative location used to connect reliable background knowledge to the scene.",
      "confidence": 1.0
    },
    {
      "evidence_id": "E6",
      "source": "background_knowledge",
      "quotation_or_description": "In the wider novel, Rochester is already married to Bertha Mason and has concealed this from Jane; the impediment is exposed before the proposed wedding can be completed.",
      "supports": "Creates dramatic irony around Jane's anticipated marriage and establishes a conflict in knowledge between Jane and Rochester without negating Jane's love.",
      "confidence": 0.98
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.98,
    "contribution": "Background knowledge establishes Rochester's concealed existing marriage and the resulting dramatic irony. It modifies the interpretation of Jane's confidence in their shared future but does not weaken the sincerity or truth-conditional force of her avowal.",
    "notes": "The core classification is independently secure from the local text; background knowledge is used primarily for contextual modification, participant asymmetry, and disagreement."
  },
  "context_needs": [],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The scheme naturally distinguishes the sincere truth-conditional avowal from its explanatory and reassuring discourse functions and from the dramatic irony surrounding the proposed marriage. The open-text contextual effect is useful because dramatic irony is not a dedicated inventory value.",
    "proposed_missing_dimensions": []
  },
  "notes": "Rochester's deception belongs to the surrounding relationship and future plans, not to the authorship or sincerity of the highlighted love-content. The phrase modestly reaffirms an existing bond, but that effect is too weak to justify a substantial performative score or a mixed core reading."
}
```

</details>

### 3. `bronte-jane-eyre-14913cd0a6a4`

- **Exact match:** `I love you`
- **Pattern:** `en_i_love_you` (v0.1)
- **Source offsets:** 631776–631786
- **Relative position:** 0.606468
- **Chapter/section:** CHAPTER XXV
- **Supplied context:** 497 characters (451 before; 36 after)

#### Passage

> “And these dreams weigh on your spirits now, Jane, when I am close to
> you? Little nervous subject! Forget visionary woe, and think only of
> real happiness! You say you love me, Janet: yes—I will not forget that;
> and you cannot deny it. _Those_ words did not die inarticulate on your
> lips. I heard them clear and soft: a thought too solemn perhaps, but
> sweet as music—‘I think it is a glorious thing to have the hope of
> living with you, Edward, because I love you.’ Do you love me,
> Jane?—repeat it.”

#### Annotation

- **Selected attempt:** `results\pipeline_runs\gutenberg-1260\20260901T100338Z\annotations\bronte-jane-eyre-14913cd0a6a4\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 1 / 0
- **Core analysis:** At the level of Jane's original avowal, “because I love you” straightforwardly presents her love for Edward as a true emotional state and as the reason she values the hope of living with him. The reference to living together gives the avowal prospective relational significance, but it is an expression of hope rather than a promise or substantial undertaking; performative force is therefore weak. The complete sentence is reflective and syntactically reasoned (“I think ... because”), not substantially reflexive or exclamatory.
- **Realisation:** direct_represented_speech, quotation_revoicing, metalinguistic_mention (actuality: spoken)
- **Current discourse act:** quotation, reassurance, elicitation_of_reaffirmation, pressure, use_as_evidence, manipulation
- **Current-act analysis:** Rochester quotes Jane's earlier avowal as evidence that she loves him, emphasizes that she “cannot deny it,” and commands her to repeat it. In the immediate exchange this helps redirect attention from Jane's disturbing dreams toward the relationship's promised happiness. The quotation consequently combines affectionate reassurance with an insistent elicitation of reaffirmation. Calling her a “Little nervous subject,” dismissing her apprehensions as “visionary woe,” and insisting on repetition add pressure and a manipulative element, especially given Rochester's concealed marital impediment.
- **Contextual modification:** preserves, strengthens, redirects, quotes, manipulates
- **Ontology adequate:** True — The scheme gives a generally natural account of the distinction between Jane's original avowal and Rochester's present quotation, evidential use, and pressure. Its main limitation is that a single actuality value cannot separately encode the currently spoken quotation and the originally spoken quoted event. The assessment fields also require prose to clarify whether deception concerns quotation fidelity, the love proposition, or the wider conversational framing.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "bronte-jane-eyre-14913cd0a6a4",
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
    "relationship_modifier": "Romantic love expressed in the context of an anticipated marriage and shared life.",
    "analysis": "At the level of Jane's original avowal, “because I love you” straightforwardly presents her love for Edward as a true emotional state and as the reason she values the hope of living with him. The reference to living together gives the avowal prospective relational significance, but it is an expression of hope rather than a promise or substantial undertaking; performative force is therefore weak. The complete sentence is reflective and syntactically reasoned (“I think ... because”), not substantially reflexive or exclamatory.",
    "confidence": 0.98
  },
  "realisation": {
    "types": [
      "direct_represented_speech",
      "quotation_revoicing",
      "metalinguistic_mention"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "Rochester currently speaks the highlighted words within the fictional world, but he speaks them as part of an attributed revoicing of Jane's earlier utterance. His surrounding references to “those words,” their articulation on her lips, and his having heard them also make the wording an object of metalinguistic attention. Both the current quotation and the original avowal are represented as spoken, although the schema's single actuality field cannot distinguish those two speech events.",
    "confidence": 0.98
  },
  "current_discourse_act": {
    "types": [
      "quotation",
      "reassurance",
      "elicitation_of_reaffirmation",
      "pressure",
      "use_as_evidence",
      "manipulation"
    ],
    "other_description": null,
    "analysis": "Rochester quotes Jane's earlier avowal as evidence that she loves him, emphasizes that she “cannot deny it,” and commands her to repeat it. In the immediate exchange this helps redirect attention from Jane's disturbing dreams toward the relationship's promised happiness. The quotation consequently combines affectionate reassurance with an insistent elicitation of reaffirmation. Calling her a “Little nervous subject,” dismissing her apprehensions as “visionary woe,” and insisting on repetition add pressure and a manipulative element, especially given Rochester's concealed marital impediment.",
    "confidence": 0.96
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens",
      "redirects",
      "quotes",
      "manipulates"
    ],
    "other_description": null,
    "analysis": "The revoicing preserves Jane's explicit propositional avowal rather than challenging or retracting it. Rochester strengthens its salience by describing it as solemn and musical, treating it as undeniable evidence, and demanding repetition. At the same time, he redirects it from Jane's original explanation of hopeful shared life into a means of controlling the present conversation and displacing her ominous anxieties. Knowledge of Rochester's concealed existing marriage makes that redirection more troubling and dramatically ironic, without making Jane's avowal itself insincere.",
    "confidence": 0.93
  },
  "participant_construals": [
    {
      "role": "original_avower_Jane",
      "discourse_level": "core_love_content",
      "status": "supported",
      "analysis": "Jane's attributed sentence explicitly presents her love for Edward as genuine and as the reason she hopes to live with him. Wider knowledge of her subsequent choices supports the sincerity of her love while showing that the avowal is not an unconditional undertaking to remain with him under any circumstances.",
      "confidence": 0.97
    },
    {
      "role": "current_quoter_Rochester",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Rochester construes Jane's earlier words as a clear, solemn, and undeniable avowal. He presently invokes them as evidence and presses Jane to reaffirm them.",
      "confidence": 0.99
    },
    {
      "role": "current_addressee_Jane",
      "discourse_level": "current_discourse_act",
      "status": "unavailable",
      "analysis": "The supplied passage ends with Rochester's demand for repetition and does not include Jane's response, so her immediate reception of his reassurance and pressure cannot be established from the excerpt.",
      "confidence": null
    },
    {
      "role": "retrospective_narrator_or_text",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The text presents Jane's avowal as sincere while placing Rochester's affectionate revoicing beside his dismissal of her ominous dreams. Later revelations give this juxtaposition dramatic irony and validate concerns he currently minimizes.",
      "confidence": 0.9
    },
    {
      "role": "reader_informed_by_wider_work",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "An informed reader can accept Jane's love as genuine while recognizing that Rochester's appeal to it occurs within a deceptive and pressuring situation created by his concealed marriage.",
      "confidence": 0.94
    }
  ],
  "disagreements": [
    {
      "parties": [
        "current_quoter_Rochester",
        "reader_informed_by_wider_work"
      ],
      "subject": "The validity of Jane's apprehensions and Rochester's framing of their prospective happiness",
      "description": "Rochester dismisses Jane's dreams as merely visionary woe and redirects her toward supposedly real happiness, whereas the later revelation of his existing marriage gives the reader strong grounds to regard her apprehensions as narratively warranted and his account of the future as misleading.",
      "evidence_ids": [
        "E3",
        "E5"
      ],
      "confidence": 0.94
    }
  ],
  "assessments": {
    "deception_misrepresentation": {
      "status": "supported",
      "analysis": "Rochester appears to reproduce Jane's avowal faithfully, so the quotation does not itself misrepresent her words. Nevertheless, his current use of her hope of living with him as evidence of “real happiness” occurs while he is concealing his existing marriage and the legal and moral impediment to the anticipated union. The supported deception is therefore contextual and belongs to Rochester's framing of their future, not to Jane's love-content.",
      "confidence": 0.91
    },
    "manipulation_pressure": {
      "status": "supported",
      "analysis": "The local sequence supplies direct evidence of pressure: Rochester says Jane cannot deny her love and commands her to repeat it, after diminishing her anxieties and directing what she should think about. His concealed marriage strengthens the interpretation that the affectionate elicitation is manipulative rather than neutral.",
      "confidence": 0.96
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "The avowal, its attribution to Jane, and Rochester's demand are linguistically explicit rather than strategically ambiguous. Rochester withholds crucial information, but concealment is distinct from ambiguity in the wording of the love-content.",
      "confidence": 0.9
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“I think it is a glorious thing to have the hope of living with you, Edward, because I love you.”",
      "supports": "The original love-content is an explicit truth-conditional avowal, offered as the reason for Jane's hopeful view of a shared life rather than as an explicit promise.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“You say you love me, Janet: yes—I will not forget that; and you cannot deny it. Those words did not die inarticulate on your lips. I heard them clear and soft.”",
      "supports": "Rochester attributes the words to Jane, treats them as actually spoken and undeniable, and attends metalinguistically to their wording and articulation.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“Forget visionary woe, and think only of real happiness!”",
      "supports": "Rochester redirects Jane from her anxieties toward his preferred interpretation of their relationship and future.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "“Do you love me, Jane?—repeat it.”",
      "supports": "The current act is an explicit elicitation of reaffirmation carrying imperative pressure.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E5",
      "source": "background_knowledge",
      "quotation_or_description": "In the wider novel, Rochester is already married to Bertha Mason and has concealed this from Jane; the impediment is revealed when the planned wedding is interrupted.",
      "supports": "Rochester's promise of real prospective happiness and his redirection of Jane's apprehensions occur within a materially deceptive context, producing dramatic irony.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E6",
      "source": "background_knowledge",
      "quotation_or_description": "Jane continues to love Rochester after learning the truth but refuses to remain with him on terms that would violate her moral independence and leaves Thornfield.",
      "supports": "Jane's avowal can be read as emotionally sincere without construing it as an unconditional performative commitment.",
      "confidence": 0.95
    },
    {
      "evidence_id": "E7",
      "source": "supplied_metadata",
      "quotation_or_description": "The supplied metadata identifies the passage as Chapter XXV of Charlotte Brontë's Jane Eyre.",
      "supports": "This locates the exchange immediately within the pre-wedding portion of the novel and anchors the application of remembered wider-work context.",
      "confidence": 0.99
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.97,
    "contribution": "Background knowledge of Rochester's concealed marriage, the interruption of the wedding, and Jane's later refusal to accept an illicit relationship clarifies the dramatic irony, deception, and manipulation surrounding the quotation. It also supports distinguishing Jane's sincere love from an unconditional commitment.",
    "notes": "The core truth-conditional classification and the identification of quotation and pressure are independently established by the local text. Background knowledge chiefly affects the contextual and ethical interpretation."
  },
  "context_needs": [
    {
      "need": "useful_for_richer_interpretation",
      "layers": [
        "realisation",
        "current_discourse_act",
        "participant_construals"
      ],
      "claim": "The exact continuity between Jane's original utterance and Rochester's revoicing, and Jane's immediate response to his demand, would refine the assessment of quotation fidelity and experienced pressure.",
      "request": "Provide the preceding passage containing Jane's original utterance and the following passage containing her response to “repeat it.”"
    }
  ],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The scheme gives a generally natural account of the distinction between Jane's original avowal and Rochester's present quotation, evidential use, and pressure. Its main limitation is that a single actuality value cannot separately encode the currently spoken quotation and the originally spoken quoted event. The assessment fields also require prose to clarify whether deception concerns quotation fidelity, the love proposition, or the wider conversational framing.",
    "proposed_missing_dimensions": [
      "Separate actuality, speaker, addressee, and temporal location for each embedded discourse event.",
      "An explicit quotation-fidelity field distinguishing accurate revoicing from distortion.",
      "An explicit scope field for deception, manipulation, and ambiguity assessments."
    ]
  },
  "notes": "The highlighted words belong propositionally to Jane but are currently voiced by Rochester. This level distinction is essential: Jane's core avowal is sincere and predominantly truth-conditional, while Rochester's present deployment of it is affectionate, evidential, pressuring, and contextually compromised by concealment."
}
```

</details>

### 4. `bronte-jane-eyre-f221719b1af4`

- **Exact match:** `I / love you`
- **Pattern:** `en_i_love_you` (v0.1)
- **Source offsets:** 830232–830242
- **Relative position:** 0.796974
- **Chapter/section:** CHAPTER XXXII
- **Supplied context:** 625 characters (352 before; 263 after)

#### Passage

> Of course, she knew her power: indeed, he did not, because he could
> not, conceal it from her. In spite of his Christian stoicism, when she
> went up and addressed him, and smiled gaily, encouragingly, even fondly
> in his face, his hand would tremble and his eye burn. He seemed to say,
> with his sad and resolute look, if he did not say it with his lips, “I
> love you, and I know you prefer me. It is not despair of success that
> keeps me dumb. If I offered my heart, I believe you would accept it.
> But that heart is already laid on a sacred altar: the fire is arranged
> round it. It will soon be no more than a sacrifice consumed.”

#### Annotation

- **Selected attempt:** `results\pipeline_runs\gutenberg-1260\20260901T100338Z\annotations\bronte-jane-eyre-f221719b1af4\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 1 / 0
- **Core analysis:** The attributed words present as true a settled romantic state: the man loves the woman and believes she would accept him. They have only weak performative force because he does not actually utter them, and the continuation explicitly distinguishes loving her from offering his heart or undertaking a relationship. His heart's dedication to a 'sacred altar' frames the love as something he intends to sacrifice rather than enact. The formulation is reflective and controlled, not a reflexive exclamation.
- **Realisation:** narratively_attributed_speech, imagined_speech, verbalisation_of_nonverbal_behaviour, hedged (actuality: not_spoken)
- **Current discourse act:** explanation, use_as_evidence, other
- **Current-act analysis:** The narrator interprets trembling, a burning eye, and a resolute look as evidence of love, then dramatizes the inferred meaning as an unspoken monologue. The current act explains both his attraction and why he remains silent: he expects success but considers himself already committed to a religious sacrifice. It is not a current direct avowal by the man.
- **Contextual modification:** preserves, weakens, strengthens, redirects, distances
- **Ontology adequate:** True — The scheme naturally distinguishes the strong truth-conditional love-content from the weak performative force, and it captures the crucial realization as narratively supplied, imagined verbalization of nonverbal behavior. The combination of weakening, strengthening, distancing, and redirection also accommodates the fact that mediation reduces literal-speech certainty while bodily evidence reinforces sincerity.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "bronte-jane-eyre-f221719b1af4",
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
    "relationship_modifier": "Romantic love renounced or withheld because of a competing religious vocation",
    "analysis": "The attributed words present as true a settled romantic state: the man loves the woman and believes she would accept him. They have only weak performative force because he does not actually utter them, and the continuation explicitly distinguishes loving her from offering his heart or undertaking a relationship. His heart's dedication to a 'sacred altar' frames the love as something he intends to sacrifice rather than enact. The formulation is reflective and controlled, not a reflexive exclamation.",
    "confidence": 0.97
  },
  "realisation": {
    "types": [
      "narratively_attributed_speech",
      "imagined_speech",
      "verbalisation_of_nonverbal_behaviour",
      "hedged"
    ],
    "other_description": null,
    "actuality": "not_spoken",
    "analysis": "The narrator supplies articulate words for what the man's 'sad and resolute look' appears to communicate. The construction 'He seemed to say' hedges the attribution, while 'if he did not say it with his lips' explicitly establishes that the represented words were not spoken. The quotation marks therefore mark constructed or imagined discourse, not direct represented speech or quotation of an earlier utterance.",
    "confidence": 0.99
  },
  "current_discourse_act": {
    "types": [
      "explanation",
      "use_as_evidence",
      "other"
    ],
    "other_description": "Interpretive dramatization of a character's nonverbal expression and inferred inner conflict",
    "analysis": "The narrator interprets trembling, a burning eye, and a resolute look as evidence of love, then dramatizes the inferred meaning as an unspoken monologue. The current act explains both his attraction and why he remains silent: he expects success but considers himself already committed to a religious sacrifice. It is not a current direct avowal by the man.",
    "confidence": 0.95
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "weakens",
      "strengthens",
      "redirects",
      "distances"
    ],
    "other_description": null,
    "analysis": "The embedding preserves the basic proposition that he loves her, but 'seemed to say' and the narrator's mediation weaken its status as directly asserted speech and distance the reader from his literal words. Conversely, the involuntary bodily signs and the claim that he cannot conceal his feeling strengthen the inference that the emotion is genuine. The continuation redirects the apparent avowal away from courtship or commitment and toward an account of self-denial: he believes she would accept him, yet refuses to offer his heart because of a prior sacred dedication.",
    "confidence": 0.94
  },
  "participant_construals": [
    {
      "role": "attributed_original_avower (St John Rivers)",
      "discourse_level": "core_love_content",
      "status": "supported",
      "analysis": "The narrator attributes to him an awareness that he loves Rosamond and could probably win her, together with a determination not to offer himself because his heart is devoted to a religious vocation. This is an attributed self-construal rather than directly spoken testimony.",
      "confidence": 0.91
    },
    {
      "role": "represented_addressee (Rosamond Oliver)",
      "discourse_level": "core_love_content",
      "status": "uncertain",
      "analysis": "The passage says that she knows her power over him and that he cannot conceal it, supporting awareness of his attraction. It does not establish that she construes his entire unspoken monologue, especially the precise nature of his religious renunciation.",
      "confidence": 0.8
    },
    {
      "role": "narrator_or_text (Jane Eyre)",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The narrator construes his visible physiological and facial responses as a sincere but unspoken declaration and uses the imagined speech to explain the conflict between romantic feeling and vocational resolve.",
      "confidence": 0.97
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The reader is invited to accept the love as real while recognizing that the quoted wording is the narrator's interpretive verbalization, not an actual proposal or undertaking.",
      "confidence": 0.94
    }
  ],
  "disagreements": [],
  "assessments": {
    "deception_misrepresentation": {
      "status": "unsupported",
      "analysis": "Nothing in the passage suggests that the attributed love is knowingly false. His involuntary trembling and burning eye are instead presented as signs that he cannot conceal a genuine feeling. The narrator's attribution remains inferential, but that epistemic mediation is not evidence of deception.",
      "confidence": 0.94
    },
    "manipulation_pressure": {
      "status": "unsupported",
      "analysis": "The love-content is not actually addressed to Rosamond as a means of influencing her. He remains silent and declines to offer his heart, while the narrator uses the content to reveal his conflict rather than to pressure an addressee.",
      "confidence": 0.93
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "He strategically withholds an avowal, but the passage does not show him deliberately using ambiguous love-language. His nonverbal disclosure is represented as involuntary and difficult to conceal, so withholding rather than strategic ambiguity is the relevant phenomenon.",
      "confidence": 0.88
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“his hand would tremble and his eye burn”",
      "supports": "The narrator treats involuntary bodily signs as evidence of strong and genuine romantic feeling.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“He seemed to say, with his sad and resolute look, if he did not say it with his lips”",
      "supports": "The wording is a hedged narrative verbalization of nonverbal behavior and was explicitly not spoken.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“I love you, and I know you prefer me.”",
      "supports": "The constructed speech strongly presents a loving emotional state as true and identifies a romantic addressee.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E4",
      "source": "local_text",
      "quotation_or_description": "“It is not despair of success that keeps me dumb. If I offered my heart, I believe you would accept it.”",
      "supports": "His silence is not attributed to expected rejection, and the conditional 'if' distinguishes love from an actual offer or relational undertaking.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E5",
      "source": "local_text",
      "quotation_or_description": "“that heart is already laid on a sacred altar” and will become “a sacrifice consumed”",
      "supports": "The passage redirects the avowal toward religiously framed self-denial and the sacrifice of romantic possibility.",
      "confidence": 0.97
    },
    {
      "evidence_id": "E6",
      "source": "local_text",
      "quotation_or_description": "“she knew her power” and “he could not, conceal it from her”",
      "supports": "The represented woman is aware of her influence over him, while his feeling is presented as difficult to hide.",
      "confidence": 0.94
    },
    {
      "evidence_id": "E7",
      "source": "supplied_metadata",
      "quotation_or_description": "The supplied metadata identifies the work as Charlotte Brontë's Jane Eyre and locates the passage in Chapter XXXII.",
      "supports": "This establishes the work and chapter used to connect the local passage with remembered narrative context.",
      "confidence": 1.0
    },
    {
      "evidence_id": "E8",
      "source": "background_knowledge",
      "quotation_or_description": "In the surrounding episode, the man is St John Rivers, the woman is Rosamond Oliver, and Jane narrates St John's attraction to Rosamond alongside his decision to subordinate marriage to his missionary vocation.",
      "supports": "This identifies the participants and clarifies that the sacred sacrifice concerns St John's religious vocation and renunciation of a possible romantic union.",
      "confidence": 0.95
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.95,
    "contribution": "Background knowledge was used to identify the unnamed participants as St John Rivers, Rosamond Oliver, and the narrator Jane Eyre, and to interpret the 'sacred altar' as St John's missionary vocation. The core classification and the fact that the words were not spoken are independently clear from the local passage.",
    "notes": "The wider novel supports the contrast between St John's real attraction to Rosamond and his refusal to pursue that relationship because he judges it incompatible with his religious mission."
  },
  "context_needs": [],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The scheme naturally distinguishes the strong truth-conditional love-content from the weak performative force, and it captures the crucial realization as narratively supplied, imagined verbalization of nonverbal behavior. The combination of weakening, strengthening, distancing, and redirection also accommodates the fact that mediation reduces literal-speech certainty while bodily evidence reinforces sincerity.",
    "proposed_missing_dimensions": []
  },
  "notes": "The quotation marks do not represent an actual utterance. The central literary effect is that the narrator gives verbal form to an emotion St John visibly reveals but deliberately refuses to convert into speech, offer, or relationship."
}
```

</details>

### 5. `bronte-jane-eyre-b57472f62694`

- **Exact match:** `I love you`
- **Pattern:** `en_i_love_you` (v0.1)
- **Source offsets:** 936871–936881
- **Relative position:** 0.899341
- **Chapter/section:** CHAPTER XXXV
- **Supplied context:** 348 characters (240 before; 98 after)

#### Passage

> “There is no dishonour, no breach of promise, no desertion in the case.
> I am not under the slightest obligation to go to India, especially with
> strangers. With you I would have ventured much, because I admire,
> confide in, and, as a sister, I love you; but I am convinced that, go
> when and with whom I would, I should not live long in that climate.”

#### Annotation

- **Selected attempt:** `results\pipeline_runs\gutenberg-1260\20260901T100338Z\annotations\bronte-jane-eyre-b57472f62694\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 1 / 0
- **Core analysis:** The speaker directly presents her love as a genuine existing state, coordinated with admiration and confidence: “I admire, confide in, and, as a sister, I love you.” The carefully inserted qualification “as a sister” specifies the kind of love rather than retracting it. There is at most weak performative force in affirming an existing sibling-like bond; the utterance does not substantially undertake a new commitment, and the surrounding conditional concerns what she would have ventured, not a present promise. Its measured syntax and argumentative setting weigh strongly against an exclamatory or reflexive reading.
- **Realisation:** direct_represented_speech, hedged (actuality: spoken)
- **Current discourse act:** direct_avowal, explanation, distancing, rejection, reinterpretation
- **Current-act analysis:** Jane avows affection while explaining why she would have been willing to venture much with this particular person. At the same time, “as a sister” establishes distance from a romantic or marital construal and reinterprets their intimacy as sibling-like. In the broader refusal beginning “I am not under the slightest obligation,” this qualification contributes to rejecting the marital or otherwise binding basis on which St John wants her to accompany him; it does not reject affection itself.
- **Contextual modification:** preserves, redirects, distances
- **Ontology adequate:** True — The layered scheme naturally distinguishes the sincere love-state avowal from its non-performative explanatory use and from its role in rejecting a marital construal. The open relationship modifier and the combination of redirection, distancing, rejection, and reinterpretation adequately represent the crucial sisterly qualification.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "bronte-jane-eyre-b57472f62694",
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
    "relationship_modifier": "Explicitly sisterly or sibling-like love, contrasted with romantic or marital love.",
    "analysis": "The speaker directly presents her love as a genuine existing state, coordinated with admiration and confidence: “I admire, confide in, and, as a sister, I love you.” The carefully inserted qualification “as a sister” specifies the kind of love rather than retracting it. There is at most weak performative force in affirming an existing sibling-like bond; the utterance does not substantially undertake a new commitment, and the surrounding conditional concerns what she would have ventured, not a present promise. Its measured syntax and argumentative setting weigh strongly against an exclamatory or reflexive reading.",
    "confidence": 0.98
  },
  "realisation": {
    "types": [
      "direct_represented_speech",
      "hedged"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The words are represented as spoken directly by Jane within the fictional scene. “As a sister” qualifies and limits the otherwise potentially romantic declaration, functioning as a relational hedge or specification rather than indicating uncertainty about whether she loves the addressee.",
    "confidence": 0.97
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "explanation",
      "distancing",
      "rejection",
      "reinterpretation"
    ],
    "other_description": null,
    "analysis": "Jane avows affection while explaining why she would have been willing to venture much with this particular person. At the same time, “as a sister” establishes distance from a romantic or marital construal and reinterprets their intimacy as sibling-like. In the broader refusal beginning “I am not under the slightest obligation,” this qualification contributes to rejecting the marital or otherwise binding basis on which St John wants her to accompany him; it does not reject affection itself.",
    "confidence": 0.94
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "redirects",
      "distances"
    ],
    "other_description": null,
    "analysis": "The context preserves the literal avowal of love but redirects its expected romantic force toward sisterly affection. The parenthetical qualification distances Jane from marital implications, while the conditional “With you I would have ventured much” makes the love relevant as an explanation of trust and willingness rather than as a present undertaking to travel or marry.",
    "confidence": 0.97
  },
  "participant_construals": [
    {
      "role": "original_avower_and_current_speaker_Jane",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Jane presents the affection as sincere but explicitly construes it as sisterly. She uses it to explain her confidence in St John while maintaining that she has no obligation to go to India and does not accept a marital interpretation of their bond.",
      "confidence": 0.98
    },
    {
      "role": "current_addressee_St_John_Rivers",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Knowledge of the wider episode indicates that St John seeks marriage as the required basis for Jane to accompany him as a missionary and regards a merely sisterly arrangement as inadequate. His position therefore conflicts with the relational limit Jane articulates, although his immediate response is not included in the supplied passage.",
      "confidence": 0.91
    },
    {
      "role": "narrator_or_text",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The retrospective first-person narrative represents the declaration as deliberate and syntactically qualified, embedding it in Jane’s reasoned defence of personal freedom rather than presenting it as an uncontrolled emotional outburst.",
      "confidence": 0.91
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "A reader can distinguish the strong sincerity of the affection claim from the explicitly denied romantic or marital implication and can recognize the declaration as part of Jane’s boundary-setting response.",
      "confidence": 0.95
    }
  ],
  "disagreements": [
    {
      "parties": [
        "original_avower_and_current_speaker_Jane",
        "current_addressee_St_John_Rivers"
      ],
      "subject": "The appropriate relational basis for accompanying St John to India",
      "description": "Jane recognizes a sibling-like bond and rejects obligation or marital implication, whereas St John’s position in the surrounding episode is that she should accompany him as his wife rather than merely as a sister.",
      "evidence_ids": [
        "E1",
        "E2",
        "E5"
      ],
      "confidence": 0.92
    }
  ],
  "assessments": {
    "deception_misrepresentation": {
      "status": "unsupported",
      "analysis": "The precise limitation “as a sister,” together with the candid refusal surrounding it, supports sincerity and interpretive clarity rather than deception. Reliable knowledge of Jane’s relationship with St John supplies no reason to regard this sisterly affection as knowingly false.",
      "confidence": 0.94
    },
    "manipulation_pressure": {
      "status": "unsupported",
      "analysis": "Jane’s present use of the declaration explains trust while asserting a boundary; it does not pressure St John into reciprocation or compliance. The wider episode involves pressure from St John upon Jane, but that contextual pattern should not be misattributed to Jane’s current avowal.",
      "confidence": 0.91
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "Although unqualified “I love you” could be ambiguous, Jane expressly disambiguates it with “as a sister.” The wording strategically limits possible implications rather than preserving ambiguity between sisterly and romantic love.",
      "confidence": 0.97
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“I admire, confide in, and, as a sister, I love you”",
      "supports": "A direct, sincere-seeming report of love whose relationship type is explicitly restricted to sisterly affection.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“I am not under the slightest obligation to go to India, especially with strangers.”",
      "supports": "The avowal occurs within a reasoned assertion of freedom from obligation and a refusal of the proposed course, rather than functioning as a new commitment.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“With you I would have ventured much, because I admire, confide in, and, as a sister, I love you”",
      "supports": "Love is offered as an explanation for conditional willingness and trust; the conditional undertaking is not itself presently renewed.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is in Charlotte Brontë’s Jane Eyre, Chapter XXXV.",
      "supports": "Locates the declaration in the late St John Rivers marriage-and-missionary episode; this is metadata, not passage wording.",
      "confidence": 1.0
    },
    {
      "evidence_id": "E5",
      "source": "background_knowledge",
      "quotation_or_description": "In the surrounding plot, St John Rivers asks Jane to marry him and accompany him to India as a missionary; Jane is willing to regard and aid him as a brother but refuses a loveless marriage.",
      "supports": "Identifies the participants and explains why “as a sister” is a consequential boundary against St John’s proposed marital relationship.",
      "confidence": 0.94
    },
    {
      "evidence_id": "E6",
      "source": "background_knowledge",
      "quotation_or_description": "Jane’s enduring romantic attachment elsewhere in the novel is to Rochester, while her attachment to St John is represented as familial, admiring, and non-romantic.",
      "supports": "Corroborates the sincerity and non-romantic scope of the present avowal without treating sisterly love as weak or false.",
      "confidence": 0.94
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.95,
    "contribution": "Background knowledge identifies the speaker as Jane and the addressee as St John Rivers, situates the utterance within his proposal that she marry him and go to India, and clarifies that the sisterly qualification marks Jane’s refusal of marital love rather than a denial of affection.",
    "notes": "The core truth-conditional classification and relational qualification are already clear from the local wording. Background knowledge mainly supports participant identification, the stakes of the qualification, and the disagreement concerning marriage."
  },
  "context_needs": [],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The layered scheme naturally distinguishes the sincere love-state avowal from its non-performative explanatory use and from its role in rejecting a marital construal. The open relationship modifier and the combination of redirection, distancing, rejection, and reinterpretation adequately represent the crucial sisterly qualification.",
    "proposed_missing_dimensions": []
  },
  "notes": "The declaration should not be weakened merely because it is non-romantic: Jane strongly avows love, but specifies it as sisterly. The weak performative score reflects only a minor affirmation of an existing bond. The conditional “would have ventured” modifies the contemplated action, not the truth of “I love you.”"
}
```

</details>

### 6. `bronte-jane-eyre-b94304d3eea5`

- **Exact match:** `I love you`
- **Pattern:** `en_i_love_you` (v0.1)
- **Source offsets:** 1006637–1006647
- **Relative position:** 0.966313
- **Chapter/section:** CHAPTER XXXVII
- **Supplied context:** 203 characters (29 before; 164 after)

#### Passage

> “Which are none, sir, to me. I love you better now, when I can really
> be useful to you, than I did in your state of proud independence, when
> you disdained every part but that of the giver and protector.”

#### Annotation

- **Selected attempt:** `results\pipeline_runs\gutenberg-1260\20260901T100338Z\annotations\bronte-jane-eyre-b94304d3eea5\attempt-001`
- **State:** `valid`
- **Core T/P/E support:** 4 / 1 / 0
- **Core analysis:** Jane explicitly presents her love for Rochester as a genuine continuing state and asserts that it is now stronger. The comparative construction and its reasoned explanation give the utterance strong propositional force. Saying it directly also enacts intimacy and offers limited relational affirmation, but it does not itself substantially create or renew an obligation or undertaking, so its performative support remains weak. Its controlled comparative syntax is not substantially exclamatory or reflex-like.
- **Realisation:** direct_represented_speech (actuality: spoken)
- **Current discourse act:** direct_avowal, reassurance, explanation, reinterpretation
- **Current-act analysis:** Jane directly avows love, reassures Rochester that his altered circumstances do not diminish her attachment, and explains why she loves him 'better now.' She also reinterprets his dependence: rather than treating the loss of his former independence as a relational defect, she values being able to contribute and implicitly challenges his former insistence on being only giver and protector.
- **Contextual modification:** preserves, strengthens, redirects, challenges
- **Ontology adequate:** True — The layered scheme naturally distinguishes the avowal's strong propositional content from its weaker commitment-enacting force and separately captures its functions as reassurance, explanation, and reinterpretation. Open-text fields adequately preserve the important temporal comparison and reversal of relational roles.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "bronte-jane-eyre-b94304d3eea5",
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
    "relationship_modifier": "Romantic love understood through reciprocal usefulness rather than Rochester's former identity as sole giver and protector.",
    "analysis": "Jane explicitly presents her love for Rochester as a genuine continuing state and asserts that it is now stronger. The comparative construction and its reasoned explanation give the utterance strong propositional force. Saying it directly also enacts intimacy and offers limited relational affirmation, but it does not itself substantially create or renew an obligation or undertaking, so its performative support remains weak. Its controlled comparative syntax is not substantially exclamatory or reflex-like.",
    "confidence": 0.98
  },
  "realisation": {
    "types": [
      "direct_represented_speech"
    ],
    "other_description": null,
    "actuality": "spoken",
    "analysis": "The highlighted words are represented as words Jane currently speaks to Rochester in the fictional scene. They are neither a quotation of an earlier avowal nor wording narratively supplied for nonverbal conduct.",
    "confidence": 0.99
  },
  "current_discourse_act": {
    "types": [
      "direct_avowal",
      "reassurance",
      "explanation",
      "reinterpretation"
    ],
    "other_description": null,
    "analysis": "Jane directly avows love, reassures Rochester that his altered circumstances do not diminish her attachment, and explains why she loves him 'better now.' She also reinterprets his dependence: rather than treating the loss of his former independence as a relational defect, she values being able to contribute and implicitly challenges his former insistence on being only giver and protector.",
    "confidence": 0.96
  },
  "contextual_modification": {
    "effects": [
      "preserves",
      "strengthens",
      "redirects",
      "challenges"
    ],
    "other_description": null,
    "analysis": "The surrounding comparison preserves the literal avowal while strengthening it through 'better now.' It redirects attention from love as attraction to a proud, independent protector toward love compatible with care, reciprocity, and Jane's usefulness. The final clause challenges Rochester's former hierarchical conception of himself as exclusively giver and protector.",
    "confidence": 0.95
  },
  "participant_construals": [
    {
      "role": "Jane as current avower",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "Jane presents the love as sincere and stronger in the present, using it to reassure Rochester and explain her preference for a relationship in which she can also be useful.",
      "confidence": 0.98
    },
    {
      "role": "Rochester as current addressee",
      "discourse_level": "both",
      "status": "uncertain",
      "analysis": "The utterance is designed for Rochester to construe as a sincere avowal and reassurance against concerns arising from his changed condition. His immediate internal construal or response is not supplied in the excerpt.",
      "confidence": 0.78
    },
    {
      "role": "retrospective first-person narrator and text",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "The novel presents the avowal without an evident ironic or distancing frame and embeds it in Jane's reasoned account of a changed relational balance.",
      "confidence": 0.94
    },
    {
      "role": "reader",
      "discourse_level": "both",
      "status": "supported",
      "analysis": "A reader is strongly invited to take the statement as sincere while also noticing that Jane's love is connected to a more reciprocal distribution of giving, receiving, agency, and care.",
      "confidence": 0.94
    }
  ],
  "disagreements": [
    {
      "parties": [
        "Jane as current avower",
        "Rochester as addressee in his formerly characterized protector role"
      ],
      "subject": "The proper distribution of giving, receiving, and usefulness within their relationship",
      "description": "Jane values being able to be useful to Rochester, whereas she characterizes his former attitude as disdaining every relational role except that of giver and protector. This marks a conflict between reciprocal and one-directional models of the relationship, even though Rochester's present response is not included.",
      "evidence_ids": [
        "E2",
        "E3"
      ],
      "confidence": 0.86
    }
  ],
  "assessments": {
    "deception_misrepresentation": {
      "status": "unsupported",
      "analysis": "Neither the passage nor the remembered wider narrative supplies evidence that Jane is falsely professing love. The explicit comparison, personal explanation, and larger trajectory of her relationship with Rochester support sincerity.",
      "confidence": 0.96
    },
    "manipulation_pressure": {
      "status": "unsupported",
      "analysis": "The utterance reassures and challenges Rochester's former relational assumptions, but it does not threaten, coerce, or exploit him into an undertaking. Jane's pleasure in being useful could be psychologically complex, yet the available evidence does not support classifying the present use as manipulation or pressure.",
      "confidence": 0.91
    },
    "strategic_ambiguity": {
      "status": "unsupported",
      "analysis": "Jane states both the emotion and the reason for its increased intensity unusually clearly. No purposeful equivocation about whether she loves Rochester or what she means is evident.",
      "confidence": 0.96
    }
  },
  "evidence": [
    {
      "evidence_id": "E1",
      "source": "local_text",
      "quotation_or_description": "“I love you better now”",
      "supports": "A direct truth-conditional avowal of present love, intensified through explicit comparison with the past.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E2",
      "source": "local_text",
      "quotation_or_description": "“when I can really be useful to you”",
      "supports": "Jane explains the increased love through her ability to contribute care or practical usefulness, redirecting the avowal toward reciprocity.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E3",
      "source": "local_text",
      "quotation_or_description": "“in your state of proud independence, when you disdained every part but that of the giver and protector”",
      "supports": "The avowal challenges Rochester's former pride and his one-directional conception of relational roles.",
      "confidence": 0.98
    },
    {
      "evidence_id": "E4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is in Chapter XXXVII, at relative position 0.966313 of Jane Eyre.",
      "supports": "The scene occurs near the novel's conclusion, consistent with its role in the late resolution of Jane and Rochester's relationship.",
      "confidence": 0.99
    },
    {
      "evidence_id": "E5",
      "source": "background_knowledge",
      "quotation_or_description": "In Chapter XXXVII, Jane has returned to Rochester after the Thornfield catastrophe left him physically impaired and dependent, reversing aspects of their former disparity in power and resources.",
      "supports": "Clarifies why Jane contrasts his present condition with his former proud independence and why her ability to be useful functions as reassurance and relational reinterpretation.",
      "confidence": 0.95
    },
    {
      "evidence_id": "E6",
      "source": "background_knowledge",
      "quotation_or_description": "Across the wider novel, Jane insists on moral and personal independence before ultimately entering a mutual marital relationship with Rochester.",
      "supports": "Supports reading the avowal as sincere and as favoring reciprocity rather than deceptive submission or coercive control.",
      "confidence": 0.93
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "extensive",
    "confidence": 0.95,
    "contribution": "Background knowledge identifies the speakers as Jane and Rochester, situates the exchange after Rochester's disabling injuries and Jane's return, and clarifies the reversal of their former material and caregiving asymmetry. It also supports the interpretation of the declaration as sincere and part of the novel's relational resolution.",
    "notes": "Background plot details are supplied as remembered descriptions rather than purported exact quotations."
  },
  "context_needs": [],
  "ontology_assessment": {
    "adequate": true,
    "diagnosis": "The layered scheme naturally distinguishes the avowal's strong propositional content from its weaker commitment-enacting force and separately captures its functions as reassurance, explanation, and reinterpretation. Open-text fields adequately preserve the important temporal comparison and reversal of relational roles.",
    "proposed_missing_dimensions": []
  },
  "notes": "The phrase “better now” is interpretively central: it does not merely intensify affection but links increased love to Jane's newly available agency as caregiver and contributor. That feature may remain ethically complex, but the passage frames it chiefly as a correction to Rochester's former monopoly on giving and protecting."
}
```

</details>
