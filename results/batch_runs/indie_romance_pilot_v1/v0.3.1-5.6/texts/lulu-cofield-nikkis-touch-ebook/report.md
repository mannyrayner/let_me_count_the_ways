# Single-text pipeline report: Nikki's Touch

## Run summary

- **Run ID:** `lulu-cofield-nikkis-touch-ebook`
- **Work:** *Nikki's Touch* by Ania Cofield
- **Source:** `lulu-cofield-nikkis-touch-ebook`
- **Annotation:** v0.3.1 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 10
- **Valid occurrences:** 10
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.315292

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `cofield-nikkis-touch-d95397b735d0`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.5)
- **Source offsets:** 227229–227239
- **Relative position:** 0.618408
- **Chapter/section:** Unavailable
- **Supplied context:** 191 characters (109 before; 72 after)

#### Passage

> 	As they lay in bed afterward, Keith traced lazy circles on Nikki’s arm. She turned to him, her heart full. “I love you,” she said suddenly, the words spilling out before she could stop them.

#### Annotation

- **Selected attempt:** `results\batch_runs\indie_romance_pilot_v1\v0.3.1-5.6\texts\lulu-cofield-nikkis-touch-ebook\annotations\cofield-nikkis-touch-d95397b735d0\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 4 / 0
- **Core analysis:** Nikki directly avows a loving emotional state, strongly supporting T. The narration also explicitly presents the words as an involuntary affective discharge—said suddenly and “spilling out before she could stop them”—which independently gives strong support to E. Nothing in the excerpt indicates that the utterance undertakes or renews a commitment, so P is unsupported.
- **Ontology fit:** natural — T and E naturally capture the utterance’s dual force as both an avowal of love and an affect-driven verbal discharge. Contextual intimacy is adequately handled as evidence and does not require O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "cofield-nikkis-touch-d95397b735d0",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 4,
      "other": 0
    },
    "confidence": 0.98,
    "analysis": "Nikki directly avows a loving emotional state, strongly supporting T. The narration also explicitly presents the words as an involuntary affective discharge—said suddenly and “spilling out before she could stop them”—which independently gives strong support to E. Nothing in the excerpt indicates that the utterance undertakes or renews a commitment, so P is unsupported.",
    "ambiguity": "The intimate setting may give the avowal relational significance, but it does not independently establish performative commitment."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Nikki directly says “I love you” to Keith while they are lying together in bed."
  },
  "contextual_interpretation": "The post-intimacy setting and Nikki’s “heart full” frame the utterance as a sincere-seeming avowal. More decisively for E, the narration depicts its production as sudden and difficult to inhibit: the words emerge before she can stop them. This is positive evidence of reflex-like expressive force rather than mere passionate delivery. No promise, obligation, or relational undertaking is stated or invoked.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“She turned to him, her heart full. ‘I love you,’”",
      "supports": "The description of Nikki’s affective state and her direct address strongly support a truth-conditional avowal of love.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“she said suddenly, the words spilling out before she could stop them”",
      "supports": "This explicitly characterizes the utterance as an unplanned, difficult-to-inhibit expressive discharge, independently supporting E.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“As they lay in bed afterward, Keith traced lazy circles on Nikki’s arm.”",
      "supports": "The intimate interpersonal setting supports an affectionate reading, while supplying no clear evidence of a commitment or undertaking.",
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
    "diagnosis": "T and E naturally capture the utterance’s dual force as both an avowal of love and an affect-driven verbal discharge. Contextual intimacy is adequately handled as evidence and does not require O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 2. `cofield-nikkis-touch-e622228c1fdb`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.5)
- **Source offsets:** 227343–227353
- **Relative position:** 0.618718
- **Chapter/section:** Unavailable
- **Supplied context:** 85 characters (30 before; 45 after)

#### Passage

> 	Keith stilled, then smiled. “I love you too,” he said, his voice steady and sincere.

#### Annotation

- **Selected attempt:** `results\batch_runs\indie_romance_pilot_v1\v0.3.1-5.6\texts\lulu-cofield-nikkis-touch-ebook\annotations\cofield-nikkis-touch-e622228c1fdb\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** Keith's direct reply primarily avows as true that he reciprocates the addressee's love. “Too” makes the utterance responsive and reciprocal, while the steady, sincere delivery strongly favors a considered assertion over reflex-like expressive discharge. The exchange has minor relational-confirming force, but the excerpt does not establish a substantial commitment or undertaking.
- **Ontology fit:** natural — T naturally captures the reciprocal avowal, with slight P support for relational affirmation. Delivery and sincerity are adequately represented as context, and no independent E or residual O dimension is needed.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "cofield-nikkis-touch-e622228c1fdb",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.94,
    "analysis": "Keith's direct reply primarily avows as true that he reciprocates the addressee's love. “Too” makes the utterance responsive and reciprocal, while the steady, sincere delivery strongly favors a considered assertion over reflex-like expressive discharge. The exchange has minor relational-confirming force, but the excerpt does not establish a substantial commitment or undertaking.",
    "ambiguity": "The immediately preceding declaration is omitted, so the precise relationship and stakes are unavailable; this limits confidence about performative force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Keith directly says “I love you too” to an interlocutor in narrated dialogue."
  },
  "contextual_interpretation": "Keith first stills and then smiles before answering. His reciprocating “too,” together with the narrator's explicit characterization of his voice as steady and sincere, presents the reply as a genuine, controlled avowal rather than an impulsive verbal discharge. It may reassure the interlocutor and affirm their relationship, but those effects do not by themselves make it a strong performative undertaking.",
  "evidence": [
    {
      "evidence_id": "ev1",
      "source": "local_text",
      "quotation_or_description": "“I love you too,”",
      "supports": "The canonical love declaration strongly supports truth-conditional avowal; “too” marks reciprocal response to another declaration.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev2",
      "source": "local_text",
      "quotation_or_description": "“his voice steady and sincere”",
      "supports": "The narration explicitly presents the avowal as genuine and controlled, supporting T and weighing against an expressive/reflex-like E reading.",
      "confidence": 0.97
    },
    {
      "evidence_id": "ev3",
      "source": "local_text",
      "quotation_or_description": "“Keith stilled, then smiled.”",
      "supports": "The pause-like bodily response and subsequent smile frame the declaration as affectively meaningful, but do not independently establish E or a substantial undertaking.",
      "confidence": 0.86
    },
    {
      "evidence_id": "ev4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is located at relative position 0.618718 in Ania Cofield's Nikki's Touch; only an 85-character context window is supplied.",
      "supports": "The limited extraction explains why broader relational stakes and any stronger performative implications cannot be established from the supplied material.",
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
    "diagnosis": "T naturally captures the reciprocal avowal, with slight P support for relational affirmation. Delivery and sincerity are adequately represented as context, and no independent E or residual O dimension is needed.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 3. `cofield-nikkis-touch-09370a771321`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.5)
- **Source offsets:** 254738–254748
- **Relative position:** 0.693274
- **Chapter/section:** Unavailable
- **Supplied context:** 232 characters (194 before; 28 after)

#### Passage

> 	“Nikki, it’s me,” Keith’s voice came through, heavy with concern. “I woke up, and you were gone. Please, just...call me. I need to know you’re okay. If I did something to upset you, I’m sorry. I love you, Nikki. Don’t shut me out.”

#### Annotation

- **Selected attempt:** `results\batch_runs\indie_romance_pilot_v1\v0.3.1-5.6\texts\lulu-cofield-nikkis-touch-ebook\annotations\cofield-nikkis-touch-09370a771321\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** Keith's “I love you, Nikki” is principally an avowal of his loving emotional state. It also reassures Nikki and supports his appeal for renewed contact, but neither reassurance nor the appeal establishes an independent commitment or relational undertaking. His concern and urgency describe the delivery and context, not expressive/reflexive core force.
- **Ontology fit:** natural — T naturally captures the core avowal. The surrounding urgency, reassurance, apology, and appeal are contextual functions adequately described without adding P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "cofield-nikkis-touch-09370a771321",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.94,
    "analysis": "Keith's “I love you, Nikki” is principally an avowal of his loving emotional state. It also reassures Nikki and supports his appeal for renewed contact, but neither reassurance nor the appeal establishes an independent commitment or relational undertaking. His concern and urgency describe the delivery and context, not expressive/reflexive core force.",
    "ambiguity": "The excerpt strongly suggests a voicemail or recorded phone message, though the precise medium is not explicitly named."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "quoted_or_revoiced",
    "description": "Keith's utterance is represented as direct quoted speech, apparently heard through a phone or recorded message; “Please, just...call me” suggests that Nikki is not participating in a live exchange."
  },
  "contextual_interpretation": "Keith is distressed by Nikki's unexplained absence and uses the avowal amid concern, apology, and pleas for contact. The declaration functions as sincere-seeming reassurance and as emotional support for “Don't shut me out,” but the passage provides no positive evidence that it itself performs a commitment or erupts as a reflex-like discharge.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I love you, Nikki.”",
      "supports": "The explicit first-person declaration strongly supports truth-conditional avowal directed specifically to Nikki.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“I woke up, and you were gone. Please, just...call me. I need to know you're okay.”",
      "supports": "Keith's concern and request for contact explain the declaration's reassuring and persuasive context without independently establishing performative commitment.",
      "confidence": 0.96
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“If I did something to upset you, I'm sorry. I love you, Nikki. Don't shut me out.”",
      "supports": "The apology and plea frame the avowal as an attempt to preserve communication and closeness; they do not supply evidence of reflex-like verbal discharge.",
      "confidence": 0.96
    },
    {
      "evidence_id": "e4",
      "source": "local_text",
      "quotation_or_description": "“Keith's voice came through” together with “call me”",
      "supports": "This supports classifying the represented event as quoted or revoiced speech, probably a phone message rather than a live exchange.",
      "confidence": 0.88
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
    "diagnosis": "T naturally captures the core avowal. The surrounding urgency, reassurance, apology, and appeal are contextual functions adequately described without adding P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 4. `cofield-nikkis-touch-80d5409e184d`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.5)
- **Source offsets:** 309700–309710
- **Relative position:** 0.842854
- **Chapter/section:** Unavailable
- **Supplied context:** 181 characters (42 before; 129 after)

#### Passage

> 	“I can’t stop thinking about you, Nikki. I love you. I know it’s complicated, but I want to be with you. I’m not asking you to make a decision now, but please, just… call me back.”

#### Annotation

- **Selected attempt:** `results\batch_runs\indie_romance_pilot_v1\v0.3.1-5.6\texts\lulu-cofield-nikkis-touch-ebook\annotations\cofield-nikkis-touch-80d5409e184d\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** “I love you” primarily avows the speaker’s loving emotional state. In context it also contributes to a relational appeal, giving weak performative support, but it does not clearly undertake a commitment. Nothing indicates that the words are a reflex-like expressive discharge rather than an emotionally significant avowal.
- **Ontology fit:** natural — T naturally captures the principal avowal, with low P representing its limited role in a relational bid. Delivery and surrounding emotional pressure require no independent E or O classification.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "cofield-nikkis-touch-80d5409e184d",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.9,
    "analysis": "“I love you” primarily avows the speaker’s loving emotional state. In context it also contributes to a relational appeal, giving weak performative support, but it does not clearly undertake a commitment. Nothing indicates that the words are a reflex-like expressive discharge rather than an emotionally significant avowal.",
    "ambiguity": "The surrounding wish to be together gives the declaration some courtship or commitment-invoking force, but the speaker explicitly avoids demanding an immediate decision, so substantial P force is uncertain."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A directly represented spoken declaration, apparently part of a message to Nikki, as suggested by the request that she call the speaker back."
  },
  "contextual_interpretation": "The declaration occurs between admissions of persistent thought and a stated desire to be with Nikki. The speaker acknowledges complications, postpones any demand for a decision, and asks for a return call. This frames “I love you” chiefly as an avowal intended to disclose feelings and support a cautious relational appeal, not as a reflexive outburst or definite undertaking.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I can’t stop thinking about you, Nikki. I love you.”",
      "supports": "The declaration is presented as an avowal of an ongoing emotional state, strongly supporting T.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“I know it’s complicated, but I want to be with you.”",
      "supports": "The avowal is embedded in a relational appeal, supplying limited support for P while not itself stating a firm commitment.",
      "confidence": 0.93
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“I’m not asking you to make a decision now, but please, just… call me back.”",
      "supports": "The speaker seeks renewed contact while withholding an immediate relational demand; this limits P and suggests a recorded or otherwise unanswered message.",
      "confidence": 0.9
    },
    {
      "evidence_id": "e4",
      "source": "local_text",
      "quotation_or_description": "The passage provides no description of blurting, involuntary speech, or words functioning as affective discharge.",
      "supports": "Supports E=0: emotional significance and the ellipsis elsewhere do not independently establish expressive/reflexive core force.",
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
    "diagnosis": "T naturally captures the principal avowal, with low P representing its limited role in a relational bid. Delivery and surrounding emotional pressure require no independent E or O classification.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 5. `cofield-nikkis-touch-a498e457b1ec`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.5)
- **Source offsets:** 310583–310593
- **Relative position:** 0.845257
- **Chapter/section:** Unavailable
- **Supplied context:** 140 characters (93 before; 37 after)

#### Passage

> 	“You don’t know how much I need you, Nikki. I’ve been a fool. But please don’t shut me out. I love you. I need you. Just give me a chance.”

#### Annotation

- **Selected attempt:** `results\batch_runs\indie_romance_pilot_v1\v0.3.1-5.6\texts\lulu-cofield-nikkis-touch-ebook\annotations\cofield-nikkis-touch-a498e457b1ec\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** The speaker directly avows love as part of a plea for Nikki not to end or exclude them from the relationship. The utterance strongly presents a loving state as true. Its placement within a request for another chance gives it weak commitment-invoking force, but it does not itself clearly promise or undertake anything. Nothing indicates that the words are a reflex-like expressive discharge rather than an emotionally charged avowal.
- **Ontology fit:** natural — T/P/E naturally represents the core utterance as a strong avowal with slight relationship-invoking force and no independently evidenced expressive/reflexive discharge. No residual core-force dimension requires O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "cofield-nikkis-touch-a498e457b1ec",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.93,
    "analysis": "The speaker directly avows love as part of a plea for Nikki not to end or exclude them from the relationship. The utterance strongly presents a loving state as true. Its placement within a request for another chance gives it weak commitment-invoking force, but it does not itself clearly promise or undertake anything. Nothing indicates that the words are a reflex-like expressive discharge rather than an emotionally charged avowal.",
    "ambiguity": "The reconciliation plea creates limited uncertainty about performative force: the declaration may help renew the relationship, but the explicit undertaking remains weak."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A speaker directly tells Nikki, “I love you,” during an appeal not to be shut out and to be given another chance."
  },
  "contextual_interpretation": "The declaration is embedded in a remorseful, persuasive appeal: the speaker acknowledges having been foolish, emphasizes need, asks Nikki not to shut them out, and requests another chance. This supports reading the words principally as an avowal offered to justify reconciliation. The passage does not establish whether the avowal is sincere, manipulative, or successful, and those contextual possibilities do not alter its dominant truth-conditional mode.",
  "evidence": [
    {
      "evidence_id": "ev1",
      "source": "local_text",
      "quotation_or_description": "“I love you.”",
      "supports": "The unhedged first-person declaration strongly supports truth-conditional avowal of a loving emotional state.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev2",
      "source": "local_text",
      "quotation_or_description": "“I’ve been a fool. But please don’t shut me out. I love you. I need you. Just give me a chance.”",
      "supports": "The surrounding remorse and requests frame the declaration as part of a reconciliation plea, supplying weak performative or relationship-renewing pressure but no explicit commitment.",
      "confidence": 0.95
    },
    {
      "evidence_id": "ev3",
      "source": "local_text",
      "quotation_or_description": "The narration supplies no description such as blurting, speaking involuntarily, or hearing oneself say the words.",
      "supports": "There is no positive evidence for independent expressive/reflexive force; emotional urgency alone does not support E.",
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
    "diagnosis": "T/P/E naturally represents the core utterance as a strong avowal with slight relationship-invoking force and no independently evidenced expressive/reflexive discharge. No residual core-force dimension requires O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 6. `cofield-nikkis-touch-62a21616b980`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.5)
- **Source offsets:** 343811–343821
- **Relative position:** 0.935688
- **Chapter/section:** Unavailable
- **Supplied context:** 289 characters (105 before; 174 after)

#### Passage

> 	Franco squeezed her hand, and she turned to look at him. His expression was soft, yet full of emotion. “I love you, Nikki,” he whispered, his voice steady and sincere. “I’ve loved you for a while now. I just— I needed to make sure I didn’t rush this. But now... I know. I know it’s real.”

#### Annotation

- **Selected attempt:** `results\batch_runs\indie_romance_pilot_v1\v0.3.1-5.6\texts\lulu-cofield-nikkis-touch-ebook\annotations\cofield-nikkis-touch-62a21616b980\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** Franco directly and deliberately avows that he loves Nikki, then explicitly presents the feeling as longstanding and now verified as real. The declaration may carry a weak relational or courtship implication, but it does not clearly undertake a specific commitment. Its measured, reflective presentation provides no independent evidence of expressive/reflex-like discharge.
- **Ontology fit:** natural — T naturally captures the central considered avowal, while a low P score registers its limited relational force. E is unnecessary because deliberation and controlled delivery explain the event without positing expressive/reflexive discharge; no important core force remains outside T/P/E.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "cofield-nikkis-touch-62a21616b980",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "Franco directly and deliberately avows that he loves Nikki, then explicitly presents the feeling as longstanding and now verified as real. The declaration may carry a weak relational or courtship implication, but it does not clearly undertake a specific commitment. Its measured, reflective presentation provides no independent evidence of expressive/reflex-like discharge.",
    "ambiguity": "The declaration may help establish or advance their relationship, giving weak support to P, but the passage primarily frames it as a considered avowal of an emotional state."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Franco directly addresses Nikki and says, “I love you, Nikki,” in the narrated scene."
  },
  "contextual_interpretation": "The hand squeeze, soft emotional expression, whisper, and stated sincerity frame the declaration as intimate and earnest. More decisively, Franco says he has loved Nikki “for a while,” delayed speaking to avoid rushing, and now knows the feeling is real. This makes the utterance a reflective disclosure rather than a reflexive outburst; emotional delivery alone does not establish E.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I love you, Nikki,” followed by “I’ve loved you for a while now.”",
      "supports": "Strong T: Franco explicitly avows a present and continuing loving state.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“I needed to make sure I didn’t rush this. But now... I know. I know it’s real.”",
      "supports": "The utterance is presented as a considered conclusion after deliberation, supporting T and weighing against expressive/reflexive E.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "He whispers with a voice described as “steady and sincere,” despite being visibly emotional.",
      "supports": "Supports earnest, controlled delivery; the emotional intensity does not independently indicate reflex-like verbal discharge.",
      "confidence": 0.95
    },
    {
      "evidence_id": "e4",
      "source": "local_text",
      "quotation_or_description": "Franco squeezes Nikki’s hand and addresses her by name during the declaration.",
      "supports": "Supports direct interpersonal and courtship significance, with only weak evidence of an enacted relational undertaking.",
      "confidence": 0.85
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
    "diagnosis": "T naturally captures the central considered avowal, while a low P score registers its limited relational force. E is unnecessary because deliberation and controlled delivery explain the event without positing expressive/reflexive discharge; no important core force remains outside T/P/E.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 7. `cofield-nikkis-touch-fe0a036beb97`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.5)
- **Source offsets:** 344385–344395
- **Relative position:** 0.937250
- **Chapter/section:** Unavailable
- **Supplied context:** 93 characters (2 before; 81 after)

#### Passage

> 	“I love you too, Franco,” she said, her voice thick with emotion. “I’m so glad I found you.”

#### Annotation

- **Selected attempt:** `results\batch_runs\indie_romance_pilot_v1\v0.3.1-5.6\texts\lulu-cofield-nikkis-touch-ebook\annotations\cofield-nikkis-touch-fe0a036beb97\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The speaker directly and reciprocally avows love for Franco. The emotional delivery reinforces the sincerity and intensity of the avowal but does not independently establish either a relational undertaking or reflex-like expressive force.
- **Ontology fit:** natural — T naturally captures the reciprocal avowal. Emotional intensity can remain contextual because nothing important about the utterance’s core force requires P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "cofield-nikkis-touch-fe0a036beb97",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.94,
    "analysis": "The speaker directly and reciprocally avows love for Franco. The emotional delivery reinforces the sincerity and intensity of the avowal but does not independently establish either a relational undertaking or reflex-like expressive force.",
    "ambiguity": "The narrow excerpt cannot establish sincerity with certainty, but sincerity is not required for the strongly truth-conditional force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A character directly addresses Franco with the spoken utterance “I love you too, Franco.”"
  },
  "contextual_interpretation": "“Too” presents the declaration as a reciprocal response to an earlier or understood expression of love. Her emotion-thickened voice and gladness at having found Franco frame it as an affectively intense avowal. Those delivery cues do not by themselves make the words an expressive/reflexive discharge, and the excerpt contains no explicit commitment or undertaking.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I love you too, Franco,”",
      "supports": "The literal first-person declaration, direct address, and reciprocal “too” strongly support truth-conditional avowal.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“she said, her voice thick with emotion”",
      "supports": "This establishes emotionally intense delivery, but supplies no independent evidence that the words are a reflex-like discharge rather than an emotional avowal.",
      "confidence": 0.96
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“I’m so glad I found you.”",
      "supports": "The follow-up conveys positive relational valuation and supports the affectionate context, without explicitly undertaking an obligation or commitment.",
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
    "diagnosis": "T naturally captures the reciprocal avowal. Emotional intensity can remain contextual because nothing important about the utterance’s core force requires P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 8. `cofield-nikkis-touch-8ba019011267`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.5)
- **Source offsets:** 364567–364577
- **Relative position:** 0.992176
- **Chapter/section:** Unavailable
- **Supplied context:** 256 characters (58 before; 188 after)

#### Passage

> 	“Nikki D,” Franco continued, his voice full of emotion, “I love you more than words could ever express. You’ve changed my life in ways I never thought possible. You make me a better man, and I can’t imagine my future without you in it. Will you marry me?”

#### Annotation

- **Selected attempt:** `results\batch_runs\indie_romance_pilot_v1\v0.3.1-5.6\texts\lulu-cofield-nikkis-touch-ebook\annotations\cofield-nikkis-touch-8ba019011267\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** Franco directly avows that he loves Nikki, elaborating on the depth and transformative significance of that state. The surrounding marriage proposal gives the avowal a modest commitment-related role, but the love clause itself primarily presents his feelings as true. Emotional delivery does not independently establish expressive/reflexive force.
- **Ontology fit:** natural — T/P/E adequately represents the core force: it is dominantly an avowal, with slight commitment-related force from its role in a marriage proposal and no independent evidence for expressive/reflexive production.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "cofield-nikkis-touch-8ba019011267",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.95,
    "analysis": "Franco directly avows that he loves Nikki, elaborating on the depth and transformative significance of that state. The surrounding marriage proposal gives the avowal a modest commitment-related role, but the love clause itself primarily presents his feelings as true. Emotional delivery does not independently establish expressive/reflexive force.",
    "ambiguity": "The proposal context creates limited uncertainty about P: the declaration helps frame a relational undertaking, although the explicit commitment-invoking work is principally done by “Will you marry me?” rather than by “I love you.”"
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Franco directly addresses Nikki in dialogue and says, “I love you more than words could ever express.”"
  },
  "contextual_interpretation": "The declaration is presented as a sincere-seeming avowal within an emotionally charged marriage proposal. Franco supports it with claims that Nikki changed his life, makes him better, and is indispensable to his imagined future. His voice being “full of emotion” indicates affective intensity, but there is no evidence that the words are a reflex-like discharge rather than an intentional avowal leading into the proposal.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I love you more than words could ever express.”",
      "supports": "Strong truth-conditional force: Franco explicitly avows an exceptionally deep loving state.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“You’ve changed my life in ways I never thought possible. You make me a better man, and I can’t imagine my future without you in it.”",
      "supports": "Elaborates the asserted significance of his love and situates the avowal within a future-oriented relationship.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“Will you marry me?”",
      "supports": "The adjacent proposal supplies modest performative support by making the love avowal part of a commitment-invoking conversational turn.",
      "confidence": 0.95
    },
    {
      "evidence_id": "e4",
      "source": "local_text",
      "quotation_or_description": "The narration describes Franco’s voice as “full of emotion.”",
      "supports": "Establishes emotional delivery but, without evidence of involuntary or discharge-like production, does not independently support E.",
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
    "diagnosis": "T/P/E adequately represents the core force: it is dominantly an avowal, with slight commitment-related force from its role in a marriage proposal and no independent evidence for expressive/reflexive production.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 9. `cofield-nikkis-touch-fe6c3e255563`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.5)
- **Source offsets:** 365744–365754
- **Relative position:** 0.995379
- **Chapter/section:** Unavailable
- **Supplied context:** 100 characters (2 before; 88 after)

#### Passage

> 	“I love you,” he murmured against her lips, his voice full of promise. “I love you so much, Nikki.”

#### Annotation

- **Selected attempt:** `results\batch_runs\indie_romance_pilot_v1\v0.3.1-5.6\texts\lulu-cofield-nikkis-touch-ebook\annotations\cofield-nikkis-touch-fe6c3e255563\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 3 / 0 / 0
- **Core analysis:** The direct declaration strongly avows the speaker's love. The narration that his voice is “full of promise” gives substantial independent support to a relational undertaking as well as an assertion of feeling. Murmuring against Nikki's lips and immediately repeating the declaration convey intimacy and intensity, but do not show that the words function as a reflex-like expressive discharge.
- **Ontology fit:** natural — T and P naturally capture the avowal and its explicitly promise-laden relational force. Intimate, emotional delivery can remain contextual because the passage supplies no positive evidence of expressive/reflexive production, and no residual core force requires O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "cofield-nikkis-touch-fe6c3e255563",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 3,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.92,
    "analysis": "The direct declaration strongly avows the speaker's love. The narration that his voice is “full of promise” gives substantial independent support to a relational undertaking as well as an assertion of feeling. Murmuring against Nikki's lips and immediately repeating the declaration convey intimacy and intensity, but do not show that the words function as a reflex-like expressive discharge.",
    "ambiguity": "The exact content and strength of the implied promise are unspecified, so performative force is substantial but less certain than truth-conditional force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A male speaker directly tells Nikki “I love you” during an intimate exchange; the highlighted utterance is followed by a repeated and intensified declaration."
  },
  "contextual_interpretation": "The utterance is framed as an intimate avowal delivered against Nikki's lips. Its repetition (“I love you so much, Nikki”) reinforces the declaration and personal reassurance, while “his voice full of promise” presents it as carrying commitment-like relational force. Nothing in the supplied passage indicates deception, irony, quotation, or involuntary blurting.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I love you,” he murmured against her lips",
      "supports": "Direct address and the ordinary declarative form strongly support a truth-conditional avowal in an intimate setting.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“his voice full of promise”",
      "supports": "The narrator explicitly frames the delivery as promise-bearing, supporting performative or undertaking force beyond affection alone.",
      "confidence": 0.9
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“I love you so much, Nikki.”",
      "supports": "The immediate repetition and naming of the addressee reinforce the avowal and reassurance; absent reflex-like framing, they do not independently support E.",
      "confidence": 0.95
    },
    {
      "evidence_id": "e4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is at relative position 0.995379 in Ania Cofield's Nikki's Touch.",
      "supports": "The declaration occurs very near the end of the work, but without wider textual knowledge this supplies only weak contextual support for a culminating relational affirmation.",
      "confidence": 0.72
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
    "diagnosis": "T and P naturally capture the avowal and its explicitly promise-laden relational force. Intimate, emotional delivery can remain contextual because the passage supplies no positive evidence of expressive/reflexive production, and no residual core force requires O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 10. `cofield-nikkis-touch-271daac625fd`

- **Exact match:** `I love you`
- **Pattern:** `en_i_optional_emphatic_do_love_you` (v0.5)
- **Source offsets:** 365815–365825
- **Relative position:** 0.995572
- **Chapter/section:** Unavailable
- **Supplied context:** 100 characters (73 before; 17 after)

#### Passage

> 	“I love you,” he murmured against her lips, his voice full of promise. “I love you so much, Nikki.”

#### Annotation

- **Selected attempt:** `results\batch_runs\indie_romance_pilot_v1\v0.3.1-5.6\texts\lulu-cofield-nikkis-touch-ebook\annotations\cofield-nikkis-touch-271daac625fd\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 3 / 0 / 0
- **Core analysis:** The first “I love you” directly avows the speaker’s loving state, strongly supporting T. The narration that his voice is “full of promise” gives the avowal substantial relational-undertaking force and therefore supports P, although no explicit commitment is articulated. Murmuring during a kiss and immediately repeating the declaration indicate intimacy and intensity but do not independently establish expressive/reflexive discharge, so E is unsupported.
- **Ontology fit:** natural — T naturally captures the avowal, while P captures the promise-laden relational force. Delivery and intensity remain contextual features, with no residual core force requiring E or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "cofield-nikkis-touch-271daac625fd",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 3,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.93,
    "analysis": "The first “I love you” directly avows the speaker’s loving state, strongly supporting T. The narration that his voice is “full of promise” gives the avowal substantial relational-undertaking force and therefore supports P, although no explicit commitment is articulated. Murmuring during a kiss and immediately repeating the declaration indicate intimacy and intensity but do not independently establish expressive/reflexive discharge, so E is unsupported.",
    "ambiguity": "The degree of P is somewhat uncertain because “full of promise” may describe romantic tone and future potential rather than a definite undertaking."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A male character directly says “I love you” to Nikki while kissing her; he then repeats and intensifies the declaration."
  },
  "contextual_interpretation": "The utterance is framed as an intimate, sincere-seeming avowal delivered against Nikki’s lips and reinforced by “I love you so much, Nikki.” The narrator’s description of his voice as “full of promise” presents it not only as a statement of feeling but also as carrying prospective relational commitment. Nothing in the supplied passage indicates irony, deception, coercion, or reflex-like loss of verbal control.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“I love you,” he murmured against her lips",
      "supports": "The direct first-person declaration strongly supports T; the intimate delivery supplies context but does not by itself support E.",
      "confidence": 0.98
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“his voice full of promise”",
      "supports": "The explicit narratorial framing supplies substantial evidence that the declaration invokes a relational or future-oriented undertaking, supporting P.",
      "confidence": 0.88
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“I love you so much, Nikki.”",
      "supports": "The immediate personalized repetition reinforces the interpretation of the highlighted utterance as a strong avowal of loving feeling rather than a semantically empty token.",
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
    "diagnosis": "T naturally captures the avowal, while P captures the promise-laden relational force. Delivery and intensity remain contextual features, with no residual core force requiring E or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The classification applies to the first matched “I love you”; the following repetition is used as immediate contextual evidence."
}
```

</details>
