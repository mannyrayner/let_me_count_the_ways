# Single-text pipeline report: Fröken Julie

## Run summary

- **Run ID:** `runeberg-frkjulie`
- **Work:** *Fröken Julie* by August Strindberg
- **Source:** `runeberg-frkjulie`
- **Annotation:** v0.3.1 with `gpt-5.6-sol`
- **Status:** `complete`
- **Extracted occurrences:** 2
- **Valid occurrences:** 2
- **Unresolved failed occurrences:** 0
- **Historical failed/invalid attempts:** 0
- **Estimated total cost:** USD 0.079768

This report is generated from the preserved extraction, inputs, and annotation attempts. Rerunning the pipeline rebuilds it without repeating valid annotations unless `--force` is used.

## Occurrences

### 1. `strindberg-froken-julie-10aa8aab447d`

- **Exact match:** `Jag älskar er`
- **Pattern:** `sv_jag_alskar_dig_er` (v0.4)
- **Source offsets:** 28428–28441
- **Relative position:** 0.417684
- **Chapter/section:** Unavailable
- **Supplied context:** 102 characters (52 before; 37 after)

#### Passage

> Jag vill - men jag törs inte! Inte här i huset mer! Jag älskar er
> - utan tvivel - kan ni tveka på det?

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\runeberg-frkjulie\annotations\strindberg-froken-julie-10aa8aab447d\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The utterance primarily avows a loving emotional state and presents that state as unquestionably true. The immediate appeal asking whether the addressee can doubt it reinforces its truth-conditional force. It contains no clear relational undertaking, and neither its emphatic delivery nor its placement amid hesitation independently establishes expressive/reflexive force.
- **Ontology fit:** natural — T naturally captures the core avowal. Persuasive intent, possible reassurance, sincerity, and dramatic intensity are contextual features and create no residual pressure requiring P, E, or O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "strindberg-froken-julie-10aa8aab447d",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.93,
    "analysis": "The utterance primarily avows a loving emotional state and presents that state as unquestionably true. The immediate appeal asking whether the addressee can doubt it reinforces its truth-conditional force. It contains no clear relational undertaking, and neither its emphatic delivery nor its placement amid hesitation independently establishes expressive/reflexive force.",
    "ambiguity": "The utterance may also serve a persuasive or reassuring purpose, and its sincerity cannot be determined from the excerpt alone; neither issue changes its dominant truth-conditional mode."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "direct",
    "description": "A character directly addresses another character in represented dramatic dialogue: “Jag älskar er” (“I love you”)."
  },
  "contextual_interpretation": "The speaker follows hesitation about acting in the house with an emphatic avowal, “Jag älskar er,” then treats that love as something the addressee should not doubt. This makes the line an insistent assertion or reassurance, potentially serving persuasion in the immediate interaction. The passage does not itself show the words being involuntarily blurted or functioning as an affective discharge, nor does it formulate a promise or commitment.",
  "evidence": [
    {
      "evidence_id": "e1",
      "source": "local_text",
      "quotation_or_description": "“Jag älskar er” (“I love you”).",
      "supports": "The declarative wording directly presents the speaker's loving state as true, strongly supporting T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "e2",
      "source": "local_text",
      "quotation_or_description": "“utan tvivel - kan ni tveka på det?” (“without doubt—can you doubt it?”).",
      "supports": "The speaker explicitly frames the love claim in terms of certainty and the addressee's belief, reinforcing truth-conditional avowal rather than expressive discharge.",
      "confidence": 0.97
    },
    {
      "evidence_id": "e3",
      "source": "local_text",
      "quotation_or_description": "“Jag vill - men jag törs inte! Inte här i huset mer!” (“I want to—but I dare not! Not here in the house anymore!”).",
      "supports": "The surrounding hesitation supplies emotional and situational intensity, but it does not state an undertaking and provides no positive evidence that the love words themselves are reflex-like.",
      "confidence": 0.88
    },
    {
      "evidence_id": "e4",
      "source": "supplied_metadata",
      "quotation_or_description": "The occurrence is from August Strindberg's Swedish play “Fröken Julie.”",
      "supports": "The dramatic-work metadata supports reading the line as represented direct speech between characters rather than as narration or a merely written love message.",
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
    "diagnosis": "T naturally captures the core avowal. Persuasive intent, possible reassurance, sincerity, and dramatic intensity are contextual features and create no residual pressure requiring P, E, or O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The classification relies on the supplied excerpt and metadata only; no wider-plot claims about the speaker's motives or sincerity are assumed."
}
```

</details>

### 2. `strindberg-froken-julie-184b60844c92`

- **Exact match:** `jag älskar dig`
- **Pattern:** `sv_jag_alskar_dig_er` (v0.4)
- **Source offsets:** 55020–55034
- **Relative position:** 0.808392
- **Chapter/section:** Unavailable
- **Supplied context:** 1394 characters (380 before; 1000 after)

#### Passage

> Tror ni inte att jag kan se blod! Tror ni att jag är så svag ---
> åh - jag skulle vilja se ditt blod, din hjärna på en träkubbe - jag
> skulle vilja se hela ditt kön simma i en sjö som den där --- jag tror
> jag skulle kunna dricka ur din huvudskål, jag skulle vilja bada mina
> fötter i din bröstkorg och jag skulle kunna äta ditt hjärta helstekt!
> -Du tror att jag är svag; du tror att jag älskar dig, därför att min
> livsfrukt åtrådde ditt frö; du tror att jag vill bära din avföda under
> mitt hjärta och nära den med mitt blod - föda ditt barn och ta ditt
> namn -hör du, vad heter du? -jag har aldrig hört ditt tillnamn - du
> har väl inget kan jag tro. Jag skulle bli fru "grindstugan" - eller
> madam Bobacken - du hund som bär mitt halsband, du dräng som bär mitt
> bomärke i dina knappar - jag dela med min köksa, rivalisera med min
> piga - åh! åh! åh! - Du tror att jag är feg och vill fly! Nej, nu
> stannar jag - och så må åskan gå! Min far kommer hem - finner sin
> chiffonjé uppbruten - sina pengar borta - så ringer han - på den där
> klockan - två tag efter betjänten - och så skickar han efter länsman -
> och så talar jag om allt! Allt! åh det skall bli skönt att få ett slut
> - bara det ville bli slut - och så får han slag och dör! - så bli vi
> slut allihop - och så blir det lugn - ro - evig vila - och så krossas
> vapnet mot likkistan - grevesläkten är slocknad och betjäntätten
> fortsätter på ett barnh

#### Annotation

- **Selected attempt:** `results\batch_runs\multilingual_five_v1\v0.3.1-5.6\texts\runeberg-frkjulie\annotations\strindberg-froken-julie-184b60844c92\attempt-001`
- **State:** `valid`
- **Core T/P/E/O support:** 4 / 0 / 0 / 0
- **Core analysis:** The embedded clause “jag älskar dig” represents the proposition that Julie has a loving emotional state toward Jean. Its force is therefore truth-conditional, though Julie embeds it under “du tror” (“you think”) and contextually repudiates rather than endorses it. It neither undertakes a relationship nor functions as a reflex-like discharge.
- **Ontology fit:** natural — T naturally captures the embedded representation of a loving state. Matrix-level belief attribution, repudiation, and dramatic hostility are adequately handled as contextual framing; no residual core force requires O.

<details>
<summary>Complete structured annotation</summary>

```json
{
  "occurrence_id": "strindberg-froken-julie-184b60844c92",
  "core_classification": {
    "label_support": {
      "truth_conditional": 4,
      "performative": 0,
      "exclamatory_reflexive": 0,
      "other": 0
    },
    "confidence": 0.96,
    "analysis": "The embedded clause “jag älskar dig” represents the proposition that Julie has a loving emotional state toward Jean. Its force is therefore truth-conditional, though Julie embeds it under “du tror” (“you think”) and contextually repudiates rather than endorses it. It neither undertakes a relationship nor functions as a reflex-like discharge.",
    "ambiguity": "The matrix clause attributes the belief to Jean rather than asserting the love proposition in Julie’s own voice, but this affects commitment to its truth, not the represented core’s truth-conditional mode."
  },
  "other_diagnosis": {
    "tpe_failure": null,
    "core_not_context": null
  },
  "utterance_status": {
    "status": "reported",
    "description": "An embedded love proposition presented as the content of the addressee’s alleged belief: Julie says, in effect, “you think that I love you,” without reporting a prior literal utterance."
  },
  "contextual_interpretation": "Julie attributes to Jean the belief that she loves him and then scornfully attacks that interpretation. Her violent denunciation, rejection of marriage and maternity, and insistence that she will remain rather than flee frame the embedded proposition as something Jean supposedly believes, not as Julie’s sincere avowal. The emotional intensity belongs to the surrounding tirade and does not independently give the embedded words expressive/reflexive force.",
  "evidence": [
    {
      "evidence_id": "local-1",
      "source": "local_text",
      "quotation_or_description": "“du tror att jag älskar dig” (“you think that I love you”)",
      "supports": "The matrix phrase “du tror att” embeds the love proposition as Jean’s alleged belief, while “jag älskar dig” itself denotes a loving state and therefore supports T.",
      "confidence": 0.99
    },
    {
      "evidence_id": "local-2",
      "source": "local_text",
      "quotation_or_description": "Julie continues by deriding the supposed consequences: bearing his child, taking his name, and becoming the wife of a servant.",
      "supports": "These relational possibilities are objects of scorn and repudiation, not commitments undertaken by the love clause; this supports P=0.",
      "confidence": 0.97
    },
    {
      "evidence_id": "local-3",
      "source": "local_text",
      "quotation_or_description": "The surrounding speech contains violent fantasies and repeated interjections such as “åh! åh! åh!”",
      "supports": "The scene is intensely affective, but the highlighted embedded clause is a deliberate characterization of Jean’s belief rather than a reflex-like discharge; intensity alone does not support E.",
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
    "diagnosis": "T naturally captures the embedded representation of a loving state. Matrix-level belief attribution, repudiation, and dramatic hostility are adequately handled as contextual framing; no residual core force requires O.",
    "candidate_recurrent_dimension": null
  },
  "notes": "The classification concerns the embedded clause “jag älskar dig,” not the full matrix assertion “du tror att jag älskar dig.”"
}
```

</details>
