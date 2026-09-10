# Single-text pipeline report: Victoria

## Run summary

- **Run ID:** `runeberg-hamsun-victoria`
- **Work:** *Victoria* by Knut Hamsun
- **Source:** `runeberg-hamsun-victoria`
- **Annotation:** v0.3.1 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 8
- **Valid occurrences:** 8
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.378284

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `hamsun-victoria-2c42c4d8b538`

- **Exact match:** `Jeg elsker Dem`
- **Pattern:** `no_jeg_elsker_dem_formal` (v0.6)
- **Source offsets:** 41854–41868
- **Relative position:** 0.265406
- **Chapter/section:** Unavailable
- **Supplied context:** 139 characters (16 before; 109 after)

#### Passage

> høre Deres .... Jeg elsker Dem og sier det nu. Det vil da av-
> hænge av Deres svar om jeg .... De råder så aldeles over mig.
> Hvad svarer De?

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\runeberg-hamsun-victoria\annotations\hamsun-victoria-2c42c4d8b538\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 2 / 0 / 0
- **Core analysis:** “Jeg elsker Dem” is principally an explicit avowal of the speaker’s loving state. In conjunction with the demand for an answer and the claim that what follows depends on that answer, it also functions as a consequential courtship or relational bid, giving moderate support to P. The deliberate formulation “and I say it now” provides no positive evidence that the words are a reflex-like affective discharge.
- **Ontology fit:** natural — T captures the explicit avowal, while moderate P captures its role as a consequential relational bid. Intensity and vulnerability belong to context and do not require E or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "hamsun-victoria-2c42c4d8b538",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 2,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.89,
    "analysis": "“Jeg elsker Dem” is principally an explicit avowal of the speaker’s loving state. In conjunction with the demand for an answer and the claim that what follows depends on that answer, it also functions as a consequential courtship or relational bid, giving moderate support to P. The deliberate formulation “and I say it now” provides no positive evidence that the words are a reflex-like affective discharge.",
    "ambiguity": "The fragment does not disclose the omitted consequences of the addressee’s answer, so the extent to which the declaration itself undertakes a commitment rather than merely soliciting a response remains uncertain."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A speaker directly tells the formally addressed addressee, “Jeg elsker Dem” (“I love you”), then asks for an answer."
  },
  "contextual_interpretation": "The confession is presented as deliberate and consequential: the speaker explicitly says it “now,” makes an unspecified outcome depend on the addressee’s answer, declares the addressee’s power over them, and asks for a response. This frames the avowal as a serious courtship bid, but the supplied fragment does not establish a specific promise or obligation.",
  "evidence": [
    {
      "evidence_id": "ev1",
      "source": "local_text",
      "quotation_or_description": "“Jeg elsker Dem og sier det nu.”",
      "supports": "The explicit first-person declaration strongly supports T; “sier det nu” presents the disclosure as consciously timed rather than reflexively blurted.",
      "confidence": 0.98
    },
    {
      "evidence_id": "ev2",
      "source": "local_text",
      "quotation_or_description": "“Det vil da avhænge av Deres svar om jeg .... De råder så aldeles over mig. Hvad svarer De?”",
      "supports": "Making an outcome depend on the addressee’s answer and directly requesting that answer supports a relational or courtship-bid component, hence moderate P.",
      "confidence": 0.9
    },
    {
      "evidence_id": "ev3",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is from Knut Hamsun’s Norwegian novel Victoria and matches the formal-address construction “Jeg elsker Dem.”",
      "supports": "Confirms the work, language, and formal second-person form; it does not independently determine the utterance’s force.",
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
    "diagnosis": "T captures the explicit avowal, while moderate P captures its role as a consequential relational bid. Intensity and vulnerability belong to context and do not require E or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The English gloss of “Jeg elsker Dem” is “I love you,” with formal or polite second-person address."
}
```

</details>

### 2. `hamsun-victoria-03bc3c21f598`

- **Exact match:** `Jeg elsker Dem`
- **Pattern:** `no_jeg_elsker_dem_formal` (v0.6)
- **Source offsets:** 43020–43034
- **Relative position:** 0.272800
- **Chapter/section:** Unavailable
- **Supplied context:** 62 characters (0 before; 48 after)

#### Passage

> Jeg elsker Dem, sa hun. Forstår De det? Det er Dem jeg
> elsker.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\runeberg-hamsun-victoria\annotations\hamsun-victoria-03bc3c21f598\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The utterance is a direct, explicit avowal that the speaker loves the addressee. Her immediate request for comprehension and focused repetition reinforce its truth-conditional force. Nothing in the supplied text independently indicates a commitment or relational undertaking, and there is no evidence that the words are a reflex-like expressive discharge rather than an emphatic avowal.
- **Ontology fit:** natural — T naturally captures the core force as an explicit and emphatically clarified avowal. Delivery and repetition are adequately handled as contextual emphasis, with no residual need for P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "hamsun-victoria-03bc3c21f598",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "The utterance is a direct, explicit avowal that the speaker loves the addressee. Her immediate request for comprehension and focused repetition reinforce its truth-conditional force. Nothing in the supplied text independently indicates a commitment or relational undertaking, and there is no evidence that the words are a reflex-like expressive discharge rather than an emphatic avowal.",
    "ambiguity": "The declaration may have consequential relational effects, but the excerpt does not make those effects part of its core undertaking force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Victoria's spoken declaration is represented as direct fictional dialogue: “Jeg elsker Dem,” followed by a confirming reformulation."
  },
  "contextual_interpretation": "The formal pronoun “Dem” coexists with an intimate declaration. “Forstår De det?” and “Det er Dem jeg elsker” press the addressee to understand and remove doubt about whom she loves, making the event an insistent avowal rather than evidence of a separate promise or reflexive outburst.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“Jeg elsker Dem, sa hun.” (“I love you, she said.”)",
      "supports": "Directly presents the speaker's loving emotional state as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "“Forstår De det? Det er Dem jeg elsker.” (“Do you understand? It is you I love.”)",
      "supports": "The demand for comprehension and focused repetition reinforce assertion and clarify the love object's identity; they do not independently establish P or E.",
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
    "diagnosis": "T naturally captures the core force as an explicit and emphatically clarified avowal. Delivery and repetition are adequately handled as contextual emphasis, with no residual need for P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 3. `hamsun-victoria-2e7f05327ab0`

- **Exact match:** `Jeg elsker Dem`
- **Pattern:** `no_jeg_elsker_dem_formal` (v0.6)
- **Source offsets:** 51695–51709
- **Relative position:** 0.327810
- **Chapter/section:** Unavailable
- **Supplied context:** 530 characters (103 before; 413 after)

#### Passage

> Lat os ikke snakke mere om det. Jeg har sagt nok, jeg har
> sagt meget formeget og jeg gjør dem ondt nu. Jeg elsker Dem,
> Jeg løi ikke iforgårs og lyver ikke nu; men det er så meget
> som skiller os. Jeg holder meget av Dem, taler gjærne med
> Dem, heller med Dem end nogen anden, men.... Ja jeg tør
> ikke stå her længer, de kan se os fra vinduerne. Johannes, det
> er så mange grunde som De ikke kjender, så De skal ikke be
> mig mere om å si hvad jeg mener. Jeg har tænkt på det nat og
> dag; jeg mener hvad jeg har sagt. Men det blir umulig.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\runeberg-hamsun-victoria\annotations\hamsun-victoria-2e7f05327ab0\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** “Jeg elsker Dem” is a direct and explicitly defended avowal of the speaker’s loving state. Her insistence that she did not lie and means what she has said strongly supports truth-conditional force. The surrounding refusal and declaration that a relationship is impossible provide no substantial undertaking force, while her prolonged reflection provides no positive evidence that the words are a reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the core force as a considered avowal. The frustrated relationship and social constraints belong to contextual interpretation; they do not require P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "hamsun-victoria-2e7f05327ab0",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.98,
    "analysis": "“Jeg elsker Dem” is a direct and explicitly defended avowal of the speaker’s loving state. Her insistence that she did not lie and means what she has said strongly supports truth-conditional force. The surrounding refusal and declaration that a relationship is impossible provide no substantial undertaking force, while her prolonged reflection provides no positive evidence that the words are a reflex-like expressive discharge.",
    "ambiguity": null
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "The speaker directly addresses Johannes with the formal singular/plural pronoun “Dem” and says, “Jeg elsker Dem” (“I love you”)."
  },
  "contextual_interpretation": "The confession is sincere as presented but does not constitute a promise or relational commitment. The speaker distinguishes love from practical possibility: social or other barriers separate them, she fears being observed, asks Johannes not to press her further, and concludes that union will be impossible. The passage frames the utterance as a considered disclosure made despite her intention to end the discussion, not as an unpremeditated emotional reflex.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“Jeg elsker Dem, Jeg løi ikke iforgårs og lyver ikke nu” (“I love you; I did not lie the day before yesterday and am not lying now”).",
      "supports": "The explicit assertion of present truth strongly supports truth-conditional avowal.",
      "confidence": 0.99
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "“Jeg holder meget av Dem, taler gjærne med Dem, heller med Dem end nogen anden” (“I care greatly for you and prefer talking with you to anyone else”).",
      "supports": "The elaboration independently corroborates the loving emotional state presented by the core utterance.",
      "confidence": 0.97
    },
    {
      "evidence_id": "local-3",
      "source": "local_text",
      "quotation_or_description": "“Jeg har tænkt på det nat og dag; jeg mener hvad jeg har sagt” (“I have thought about it night and day; I mean what I have said”).",
      "supports": "This presents the confession as considered and semantically endorsed, supporting T and weighing against expressive/reflexive E.",
      "confidence": 0.99
    },
    {
      "evidence_id": "local-4",
      "source": "local_text",
      "quotation_or_description": "“det er så meget som skiller os” and “Men det blir umulig” (“there is so much that separates us”; “But it will be impossible”).",
      "supports": "The speaker expressly separates her avowed love from any undertaking to form or continue a relationship, weighing against P.",
      "confidence": 0.98
    },
    {
      "evidence_id": "metadata-1",
      "source": "supplied_metadata",
      "quotation_or_description": "The supplied metadata identifies the passage as occurring in Knut Hamsun’s Norwegian novel Victoria at relative position 0.32781.",
      "supports": "Establishes the bibliographic and textual location of the classified occurrence without adding unsupported plot claims.",
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
    "diagnosis": "T naturally captures the core force as a considered avowal. The frustrated relationship and social constraints belong to contextual interpretation; they do not require P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The formal “Dem” is contextually addressed to Johannes and is equivalent here to singular English “you.”"
}
```

</details>

### 4. `hamsun-victoria-9b199e4962fa`

- **Exact match:** `Jeg elsker Dem`
- **Pattern:** `no_jeg_elsker_dem_formal` (v0.6)
- **Source offsets:** 67029–67043
- **Relative position:** 0.425047
- **Chapter/section:** Unavailable
- **Supplied context:** 1168 characters (1000 before; 154 after)

#### Passage

>  en majestæt. Herren reiser sig brat, hans
> mørke sjæl blir som beskinnet av en lystre-ild i samme nu. De
> er så god mot alle, sier han bitter, De kommer også til mig. Hun
> svarer ikke, hun står bare og ser på ham og hendes ansigt blir
> dunkelt rødt. Hvad vil De? spør han like så bittert som før: er
> De kommet for å minde mig om det forbigangne? for så er det
> siste gang, nådige frue, nu reiser jeg for altid. Og fremdeles
> svarer ikke den unge slotsfrue, men hendes mund bæver. Han
> sier: Er det Dem ikke nok at jeg har erkjendt min dårskap én
> gang, så hør, jeg gjør det igjen: min hu stod til Dem, jeg var
> Dem ikke værdig, — er De nu tilfreds? Han fortsætter med sti-
> gende hæftighet: De svarte mig nei, De tok en anden; jeg var
> en bonde, en bjørn, en barbar som i min ungdom var tumlet
> ind på en kongelig vildtbane! Men da kaster herren sig på
> en stol og hulker og ber: Å, gål tilgiv mig, gå Deres veil Nu er
> al rødme veket fra slotsfruens ansigt. Så sier hun og hun uttaler
> ordene så langsomt og vel: Jeg elsker Dem; misforstå mig ikke
> mere, det er Dem jeg elsker; farvel! Og det var sig den unge slots-
> frue, hun la hænderne for ansigtet og gik hurtig ut av døren ....

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\runeberg-hamsun-victoria\annotations\hamsun-victoria-9b199e4962fa\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The woman directly and deliberately avows that she loves the man, then restates the object of her love to prevent further misunderstanding. The utterance presents her emotional state as true. It neither promises a future relationship nor undertakes an obligation, and its slow, careful articulation weighs against construing it as reflex-like expressive discharge.
- **Ontology fit:** natural — T/P/E adequately represents the core force as a deliberate truth-conditional avowal. Emotional intensity and narrative consequences are contextual features rather than residual dimensions of the utterance itself.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "hamsun-victoria-9b199e4962fa",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.97,
    "analysis": "The woman directly and deliberately avows that she loves the man, then restates the object of her love to prevent further misunderstanding. The utterance presents her emotional state as true. It neither promises a future relationship nor undertakes an obligation, and its slow, careful articulation weighs against construing it as reflex-like expressive discharge.",
    "ambiguity": "The disclosure has major relational consequences, but its force here is clarification and avowal rather than commitment: she immediately says farewell and leaves."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Direct speech by the young lady of the manor within the narrated scene: she tells the man, “Jeg elsker Dem,” and immediately clarifies the declaration."
  },
  "contextual_interpretation": "The declaration answers the man's bitter belief that she rejected him and chose another. Her earlier silence, blushing, trembling mouth, and covered face indicate emotional difficulty, but she pronounces the words “så langsomt og vel” and explicitly asks not to be misunderstood. This controlled clarification strongly supports truth-conditional avowal rather than expressive/reflexive discharge. Her “farvel” and rapid departure make the speech a painful revelation, not an evident relational undertaking.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“Jeg elsker Dem; misforstå mig ikke mere, det er Dem jeg elsker” (“I love you; misunderstand me no longer, it is you I love”).",
      "supports": "The direct declaration and its clarifying repetition strongly support maximal truth-conditional force.",
      "confidence": 0.99
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "“hun uttaler ordene så langsomt og vel” (“she pronounces the words so slowly and clearly/well”).",
      "supports": "The controlled, deliberate delivery weighs against treating the words as a reflex-like expressive discharge.",
      "confidence": 0.97
    },
    {
      "evidence_id": "local-3",
      "source": "local_text",
      "quotation_or_description": "She ends with “farvel,” covers her face, and quickly leaves through the door.",
      "supports": "The immediate farewell supplies no clear promise, obligation, or relational undertaking, while showing the emotional cost of the avowal.",
      "confidence": 0.96
    },
    {
      "evidence_id": "local-4",
      "source": "local_text",
      "quotation_or_description": "Before speaking, she remains silent, blushes, and her mouth trembles while the man recounts her rejection of him and his unworthiness.",
      "supports": "The declaration is emotionally intense and corrective, but these surrounding signs of affect do not independently establish expressive/reflexive core force.",
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
    "diagnosis": "T/P/E adequately represents the core force as a deliberate truth-conditional avowal. Emotional intensity and narrative consequences are contextual features rather than residual dimensions of the utterance itself.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The formal pronoun “Dem” marks respectful or socially distanced address but does not alter the basic classification."
}
```

</details>

### 5. `hamsun-victoria-be00bbdbf853`

- **Exact match:** `jeg / elsker Dem`
- **Pattern:** `no_jeg_elsker_dem_formal` (v0.6)
- **Source offsets:** 81513–81527
- **Relative position:** 0.516893
- **Chapter/section:** Unavailable
- **Supplied context:** 218 characters (181 before; 23 after)

#### Passage

> De gik hver sin vei. Han stanset og vendte sig. Der gik hun
> nu. Han strakte hænderne ut og hvisket, sa ømme ord for sig
> selv: Jeg bærer ikke nag til Dem, nei nei det gjør jeg ikke; jeg
> elsker Dem endnu, elsker Dem ....

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\runeberg-hamsun-victoria\annotations\hamsun-victoria-be00bbdbf853\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 3 / 0
- **Core analysis:** The utterance strongly avows an enduring emotional state: he still loves her. It also has substantial expressive/reflexive force because he whispers the repeated words to himself after she has departed; they function as a solitary discharge of feeling rather than solely as communication to her. Nothing indicates a commitment or relational undertaking.
- **Ontology fit:** natural — T and E naturally capture the continuing-state avowal and its independently supported private expressive discharge; P is unnecessary, and no residual core force requires O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "hamsun-victoria-be00bbdbf853",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 3,
      "other": 0
    },
    "confidence": 0.9,
    "analysis": "The utterance strongly avows an enduring emotional state: he still loves her. It also has substantial expressive/reflexive force because he whispers the repeated words to himself after she has departed; they function as a solitary discharge of feeling rather than solely as communication to her. Nothing indicates a commitment or relational undertaking.",
    "ambiguity": "The self-directed apostrophe could be read as an intensely delivered private avowal rather than a distinct expressive discharge, but the narration's framing and repetition provide positive independent support for E."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "An actually spoken, whispered utterance addressed apostrophically to the absent woman but explicitly said to himself."
  },
  "contextual_interpretation": "After they separate, he turns to watch her leave, reaches out his hands, and privately insists that he bears her no grudge and still loves her. Her absence means the utterance does not directly alter their relationship; it combines a sincere-seeming self-avowal with affective self-expression. The repetition and trailing ellipsis reinforce that expressive reading, though intensity alone is not decisive.",
  "evidence": [
    {
      "evidence_id": "ev1",
      "source": "local_text",
      "quotation_or_description": "“jeg elsker Dem endnu” (“I still love you”)",
      "supports": "The verb of love and temporal adverb “endnu” directly present his continuing loving state as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev2",
      "source": "local_text",
      "quotation_or_description": "“han ... hvisket, sa ømme ord for sig selv” (“he ... whispered, said tender words to himself”)",
      "supports": "The words are privately voiced to himself rather than communicated to their grammatical addressee, supplying independent evidence that their production functions as affective expression and supporting E.",
      "confidence": 0.94
    },
    {
      "evidence_id": "ev3",
      "source": "local_text",
      "quotation_or_description": "“Han strakte hænderne ut ... elsker Dem endnu, elsker Dem ....” (“He stretched out his hands ... still love you, love you ...”)",
      "supports": "The gesture, immediate repetition, and trailing-off reinforce the interpretation of a solitary emotional discharge, while supplying no specific evidence of an undertaking required for P.",
      "confidence": 0.9
    },
    {
      "evidence_id": "ev4",
      "source": "local_text",
      "quotation_or_description": "“De gik hver sin vei. Han stanset og vendte sig. Der gik hun nu.” (“They went their separate ways. He stopped and turned. There she went.”)",
      "supports": "Establishes that she is departing and apparently not the recipient of the whisper, making a performative relational undertaking unlikely in this event.",
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
    "diagnosis": "T and E naturally capture the continuing-state avowal and its independently supported private expressive discharge; P is unnecessary, and no residual core force requires O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "English glosses are provided only as translations of the supplied Norwegian text."
}
```

</details>

### 6. `hamsun-victoria-ac5e0080c204`

- **Exact match:** `Jeg / elsker Dem`
- **Pattern:** `no_jeg_elsker_dem_formal` (v0.6)
- **Source offsets:** 103172–103186
- **Relative position:** 0.654238
- **Chapter/section:** Unavailable
- **Supplied context:** 1272 characters (1000 before; 258 after)

#### Passage

> e grepet sit glas og drukket. Skål,
> se på mig hvor pent jeg drikker .... Se forøvrig på en kvinde
> fra siden når hun drikker. Lat hende drikke av en kop, av et
> glas, av hvadsomhelst, men se på hende fra siden. Hun skaper
> sig så det er en gru. Hun spidser munden og dypper den
> ytterste rand av den ned i drikken og hun er fortvilet hvis
> man herunder lægger mærke til hendes hånd. Se i det hele tat
> ikke en kvinde på hånden. Hun utstår det ikke, hun kapitulerer.
> Hun begynder straks å rykke sin hånd til sig, å lægge den i
> en skjønnere og skjønnere stilling, altsammen for å skjule en
> rynke, en krokethet i fingrene eller en mindre velformet negl.
> Tilsist holder hun det ikke længer ut, men spør ute av sig selv:
> hvad ser De på? .... Hun hadde engang kysset ham, engang,
> en sommer. Det var så længe siden, Gud vet om det endog var
> sandt. Hvordan var det, sat de ikke på en bænk? De talte længe
> sammen og da de gik kom han hende så aldeles nær at han
> berørte hendes arm. Utenfor en entré kysset hun ham. Jeg
> elsker Dem! sa hun. .... Nu gik de forbi, de sat kanske endnu
> i lysthuset. Løitnanten vilde gi ham et slag på øret, sa han.
> Han hørte det så godt, han sov ikke, men han reiste sig heller
> ikke og trådte frem. En officers hånd, sa han. Javel, det var
> ham likegyldig ....

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\runeberg-hamsun-victoria\annotations\hamsun-victoria-ac5e0080c204\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** Victoria's represented utterance is principally a direct avowal that she loves the addressee. The kiss and exclamation mark indicate romantic and emotional intensity, but there is no independent evidence that the words undertake a commitment or emerge as a reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the represented confession. The passage's uncertainty concerns the recollected event, while its emotional punctuation and romantic setting can be handled contextually without adding E, P, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "hamsun-victoria-ac5e0080c204",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.91,
    "analysis": "Victoria's represented utterance is principally a direct avowal that she loves the addressee. The kiss and exclamation mark indicate romantic and emotional intensity, but there is no independent evidence that the words undertake a commitment or emerge as a reflex-like expressive discharge.",
    "ambiguity": "The narration questions whether the remembered episode actually occurred, and the declaration may carry some implicit relational significance; neither uncertainty establishes a different core force."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "quoted_or_revoiced",
    "description": "The narrator reproduces her earlier words as direct speech within a retrospective recollection whose factual reliability is explicitly questioned."
  },
  "contextual_interpretation": "The declaration follows her kissing him and is remembered as an intimate confession from a past summer. The narrator's thought that God knows whether it was even true casts doubt on the memory or imagined reconstruction of the episode, rather than changing the represented utterance's truth-conditional avowal force. The exclamation mark supplies intensity but not independent E evidence.",
  "evidence": [
    {
      "evidence_id": "ev1",
      "source": "local_text",
      "quotation_or_description": "“Jeg elsker Dem! sa hun.”",
      "supports": "The explicit first-person love declaration, followed by a speech tag, strongly supports T and identifies an originally spoken event reproduced in quotation.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev2",
      "source": "local_text",
      "quotation_or_description": "“Utenfor en entré kysset hun ham. Jeg elsker Dem!”",
      "supports": "The preceding kiss establishes an intimate romantic setting for the avowal, while not by itself establishing commitment or reflexive discharge.",
      "confidence": 0.96
    },
    {
      "evidence_id": "ev3",
      "source": "local_text",
      "quotation_or_description": "“Hun hadde engang kysset ham ... Det var så længe siden, Gud vet om det endog var sandt.”",
      "supports": "The utterance is embedded in a distant, possibly unreliable recollection; this creates contextual uncertainty about occurrence without creating ontology failure.",
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
    "diagnosis": "T naturally captures the represented confession. The passage's uncertainty concerns the recollected event, while its emotional punctuation and romantic setting can be handled contextually without adding E, P, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": null
}
```

</details>

### 7. `hamsun-victoria-728a88f42cf3`

- **Exact match:** `jeg elsker dig`
- **Pattern:** `no_jeg_elsker_deg_dig_dere` (v0.6)
- **Source offsets:** 142059–142073
- **Relative position:** 0.900829
- **Chapter/section:** Unavailable
- **Supplied context:** 407 characters (5 before; 388 after)

#### Passage

> Jeg, jeg elsker dig mere, mere end mit liv, du kjære, elsker
> dig som den første dag, den første stund da du gav mig rosen.
> Husker du det? Du rakte mig rosen og så på mig med dine
> skjønne øine; rosen duftet som du, du rødmet som den og jeg
> blev beruset i alle mine sanser. Men endnu mere elsker jeg dig
> nu, du er skjønnere end i din ungdom og mit hjærte takker og
> velsigner dig for hver dag du har været min.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\runeberg-hamsun-victoria\annotations\hamsun-victoria-728a88f42cf3\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** The utterance strongly presents the speaker's enduring and increasing love as true, elaborating it through comparison with life itself, first love, and continued devotion. The imagined shared lifetime gives weak support to relational reaffirmation, but the words do not clearly undertake a new commitment. Repetition and emotional intensity do not independently establish expressive/reflexive force.
- **Ontology fit:** natural — T naturally captures the sustained avowal, while a low P score registers limited relational-reaffirmation pressure. Emotional intensity and imagined written framing are contextual features rather than missing core-force categories; E and O are unnecessary.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "hamsun-victoria-728a88f42cf3",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.82,
    "analysis": "The utterance strongly presents the speaker's enduring and increasing love as true, elaborating it through comparison with life itself, first love, and continued devotion. The imagined shared lifetime gives weak support to relational reaffirmation, but the words do not clearly undertake a new commitment. Repetition and emotional intensity do not independently establish expressive/reflexive force.",
    "ambiguity": "The supplied excerpt omits the framing immediately before the speech. Wider-work context indicates that it is embedded in Victoria's letter and voices an imagined declaration within an unrealized shared future, but the exact nesting and imagined speaker are not visible locally."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "imagined",
    "description": "An imagined direct declaration, apparently scripted within Victoria's written farewell letter; it therefore combines imagined speech with written and revoiced framing."
  },
  "contextual_interpretation": "The declaration envisions love persisting into old age and retrospectively blesses every day of a shared life. Against the novel's unrealized relationship, this is a counterfactual image of lifelong union rather than evidence that such a union actually occurred. Its repetitions and luxuriant recollection convey high emotional intensity, but T plus contextual delivery adequately captures the core force without assigning E.",
  "evidence": [
    {
      "evidence_id": "ev1",
      "source": "local_text",
      "quotation_or_description": "“jeg elsker dig mere, mere end mit liv” (“I love you more, more than my life”).",
      "supports": "Strong truth-conditional avowal of an exceptionally intense loving state.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev2",
      "source": "local_text",
      "quotation_or_description": "“Men endnu mere elsker jeg dig nu” (“But I love you still more now”).",
      "supports": "Presents the love as enduring and increasing over time, reinforcing T.",
      "confidence": 0.98
    },
    {
      "evidence_id": "ev3",
      "source": "local_text",
      "quotation_or_description": "“mit hjærte takker og velsigner dig for hver dag du har været min” (“my heart thanks and blesses you for every day you have been mine”).",
      "supports": "Invokes an established lifelong bond, giving slight support to relational reaffirmation, though not a clear new undertaking.",
      "confidence": 0.92
    },
    {
      "evidence_id": "ev4",
      "source": "local_text",
      "quotation_or_description": "The broken repetitions “Jeg, jeg” and “mere, mere” accompany an extended, coherent account of why and how long the speaker has loved the addressee.",
      "supports": "Shows emotionally heightened delivery but supplies no independent evidence that the words are a reflex-like discharge rather than an intense avowal.",
      "confidence": 0.9
    },
    {
      "evidence_id": "ev5",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is at relative position 0.900829 in Hamsun's Victoria.",
      "supports": "Places the passage near the end of the work, consistent with the late farewell-letter context, though position alone does not determine utterance status.",
      "confidence": 0.88
    },
    {
      "evidence_id": "ev6",
      "source": "background_knowledge",
      "quotation_or_description": "The closing portion of Victoria includes Victoria's farewell letter and counterfactual imaginings of the life she and Johannes did not share; this passage appears within that layered written imagining.",
      "supports": "Supports classifying the event primarily as imagined, with written and revoiced complications, and explains the poignant counterfactual shared-life language.",
      "confidence": 0.78
    }
  ],
  "background_knowledge": {
    "used": true,
    "familiarity": "moderate",
    "confidence": 0.78,
    "contribution": "Used to identify the likely farewell-letter and counterfactual-future framing that is absent from the narrowly supplied excerpt."
  },
  "ontology_assessment": {
    "fit": "natural",
    "diagnosis": "T naturally captures the sustained avowal, while a low P score registers limited relational-reaffirmation pressure. Emotional intensity and imagined written framing are contextual features rather than missing core-force categories; E and O are unnecessary.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The imagined speaker's precise identity is not asserted because the excerpt omits the preceding framing."
}
```

</details>

### 8. `hamsun-victoria-738c9e32224b`

- **Exact match:** `jeg elsker dig`
- **Pattern:** `no_jeg_elsker_deg_dig_dere` (v0.6)
- **Source offsets:** 142846–142860
- **Relative position:** 0.905820
- **Chapter/section:** Unavailable
- **Supplied context:** 201 characters (176 before; 11 after)

#### Passage

> O, du min brudgom, min elskede! stammer den gamle kvinde
> og kysser hans hænder. Du er skjønnere end nogen mand på
> jorden, din røst gjør mig endnu den dag idag het i hjærtet
> og jeg elsker dig til døden.

#### Annotation

- **Selected attempt:** `results\batch_runs\classical_six_v1\v0.3.1-5.6\texts\runeberg-hamsun-victoria\annotations\hamsun-victoria-738c9e32224b\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 1 / 0 / 0
- **Core analysis:** The old woman directly avows an enduring and intense loving state: “jeg elsker dig til døden” (“I love you unto death”). Addressing him as her bridegroom and beloved gives slight support to relational invocation, but the utterance does not clearly undertake a new obligation or commitment. Her stammering and physical emotion intensify the avowal without independently showing that the words themselves are a reflex-like expressive discharge.
- **Ontology fit:** natural — T naturally captures the avowal, with slight P support for its bridegroom framing. Emotional intensity and stammered delivery can remain contextual features, so neither E nor O is required.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "hamsun-victoria-738c9e32224b",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 1,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.9,
    "analysis": "The old woman directly avows an enduring and intense loving state: “jeg elsker dig til døden” (“I love you unto death”). Addressing him as her bridegroom and beloved gives slight support to relational invocation, but the utterance does not clearly undertake a new obligation or commitment. Her stammering and physical emotion intensify the avowal without independently showing that the words themselves are a reflex-like expressive discharge.",
    "ambiguity": "“Til døden” and “min brudgom” could weakly suggest lifelong relational commitment, but they function more naturally here as descriptions of love and relationship than as an undertaking."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "Direct speech by the old woman to the man whose hands she kisses, embedded in third-person narration."
  },
  "contextual_interpretation": "The avowal forms the culmination of an intensely affectionate address: the woman calls the addressee her bridegroom and beloved, praises his beauty, says his voice still heats her heart, stammers, and kisses his hands. These details strongly frame the statement as an emotionally charged profession of enduring love. They do not by themselves convert its core force into an expressive/reflexive discharge.",
  "evidence": [
    {
      "evidence_id": "ev1",
      "source": "local_text",
      "quotation_or_description": "“jeg elsker dig til døden” (“I love you unto death”)",
      "supports": "Strong truth-conditional support: the speaker presents her enduring love as true.",
      "confidence": 0.99
    },
    {
      "evidence_id": "ev2",
      "source": "local_text",
      "quotation_or_description": "“O, du min brudgom, min elskede!” (“O, you my bridegroom, my beloved!”)",
      "supports": "Establishes intimate relational framing and provides limited support for performative invocation of the bond.",
      "confidence": 0.9
    },
    {
      "evidence_id": "ev3",
      "source": "local_text",
      "quotation_or_description": "The old woman “stammer” and kisses his hands; she says his voice still makes her heart hot.",
      "supports": "Shows intense affective delivery, while not independently establishing reflex-like expressive core force.",
      "confidence": 0.94
    },
    {
      "evidence_id": "ev4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is in Knut Hamsun’s Norwegian-language novel Victoria, at relative source position 0.90582.",
      "supports": "Identifies the literary source and late-work location without altering the local force classification.",
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
    "diagnosis": "T naturally captures the avowal, with slight P support for its bridegroom framing. Emotional intensity and stammered delivery can remain contextual features, so neither E nor O is required.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The archaic spelling “dig” and phrase “til døden” are interpreted as an avowal of love enduring unto death."
}
```

</details>
