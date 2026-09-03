# Annotation comparison: v0.3 → v0.3.1

> This is a diagnostic comparison. v0.3 is not treated as ground truth; changes may
> reflect improvement, information loss, overclassification, instability, or ambiguity.

- **Batch:** `development_three`
- **Matched occurrences:** 22
- **Unmatched occurrences:** 0
- **Exact T/P/E agreement:** truth_conditional 21/22, performative 16/22, exclamatory_reflexive 7/22
- **All three scores exact:** 5/22
- **O scores:** O=0: 22; O=1: 0; O≥2: 0
- **E changes / magnitude ≥2:** 15 / 8
- **O / ontology-fit changes:** 0 / 0
- **Confidence changes ≥0.20:** 0
- **Ontology fit:** natural: 22, strained: 0, inadequate: 0

## Cases requiring inspection

### `bronte-jane-eyre-14913cd0a6a4`

- **T/P/E:** [4, 1, 0] → [4, 0, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.95 → 0.97
- **Ambiguity:** The surrounding reference to living together gives the statement relational significance, but it does not make the highlighted causal avowal itself a commitment.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `bronte-jane-eyre-9267e616f948`

- **T/P/E:** [4, 1, 0] → [4, 1, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.96 → 0.96
- **Ambiguity:** A weak performative reading is possible because the avowal occurs within an anticipated marriage, but the core clause is principally explanatory and truth-conditional.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `bronte-jane-eyre-b57472f62694`

- **T/P/E:** [4, 0, 0] → [4, 0, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.97 → 0.98
- **Ambiguity:** The love is explicitly familial rather than romantic; this affects its object-level meaning but not its predominantly truth-conditional force.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `bronte-jane-eyre-b94304d3eea5`

- **T/P/E:** [4, 1, 0] → [4, 1, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.96 → 0.94
- **Ambiguity:** The surrounding emphasis on Jane's ability to be useful to Rochester gives the utterance some commitment-like pragmatic force, but that force may belong chiefly to the context rather than to the core love statement.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `bronte-jane-eyre-f221719b1af4`

- **T/P/E:** [4, 0, 1] → [4, 0, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.95 → 0.97
- **Ambiguity:** The words are a narrator-supplied interpretation of nonverbal behaviour rather than an actually spoken sentence, but this affects utterance status rather than the T/P/E classification.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `alcott-little-women-15ef9596ac4e`

- **T/P/E:** [4, 0, 0] → [4, 0, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.98 → 0.97
- **Ambiguity:** The excerpt’s dialogue segmentation is slightly awkward, but the exchange and Jo’s “Thank you, Mother” make the speaker and addressee sufficiently clear.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `alcott-little-women-44ca305cf65a`

- **T/P/E:** [4, 1, 0] → [4, 0, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.94 → 0.95
- **Ambiguity:** The courtship setting gives the avowal relational significance, but that contextual function is insufficient to establish performative undertaking force in the core utterance.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `alcott-little-women-58c41f8731dd`

- **T/P/E:** [4, 0, 1] → [4, 0, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.95 → 0.98
- **Ambiguity:** The surrounding promises of continued visits and family closeness have commitment-like force, but that force belongs to adjacent utterances rather than to the classified love clause.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `alcott-little-women-f1eab387a74e`

- **T/P/E:** [4, 0, 1] → [4, 1, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.97 → 0.96
- **Ambiguity:** There is slight T/P overlap because the avowal supports Amy’s affirmation of marriage irrespective of wealth, but the commitment force principally belongs to the surrounding statement rather than to “I love you” itself.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-06903c63a2d7`

- **T/P/E:** [3, 0, 4] → [4, 0, 2]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.96 → 0.90
- **Ambiguity:** The exclamative syntax, repetition, and impetuous embrace support E, but they could also be interpreted simply as the intense delivery of a T-dominant avowal; hence E is moderate rather than maximal.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-1e7d6742e45b`

- **T/P/E:** [4, 2, 2] → [4, 2, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.89 → 0.91
- **Ambiguity:** The degree of performative force is uncertain: “je t’aimerai toujours” may be either a pledge of constancy or an emphatic prediction/reassurance about continued feeling.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-400a3aed5a88`

- **T/P/E:** [4, 0, 3] → [4, 1, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.93 → 0.93
- **Ambiguity:** The surrounding claims “Je suis ta servante et ta concubine” give limited support to a performative reading, though they more naturally characterize the avowed love than make “je t’aime” itself a commitment.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-47361213aeaa`

- **T/P/E:** [4, 0, 1] → [4, 0, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.95 → 0.94
- **Ambiguity:** The emphatic punctuation and urgent requests convey emotional intensity and interpersonal pressure, but they do not independently establish expressive/reflexive or undertaking force.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-5396f984c871`

- **T/P/E:** [4, 0, 3] → [4, 1, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.91 → 0.90
- **Ambiguity:** The narrow excerpt does not establish whether the avowal is sincere or strategically intended to prevent departure, but either reading remains principally truth-conditional in mode.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-8c91fb38ed76`

- **T/P/E:** [4, 0, 4] → [4, 0, 2]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.97 → 0.88
- **Ambiguity:** The exclamative syntax and affective action support E, but the narration does not explicitly present the words as involuntary or pre-reflective; they could also be understood primarily as an intensely delivered avowal.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-8fe83e2776a5`

- **T/P/E:** [4, 0, 1] → [4, 0, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.91 → 0.96
- **Ambiguity:** The narrow excerpt does not establish whether the avowal is sincere, habitual, impatient, or reassuring, but those possibilities do not alter its strongly truth-conditional mode.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-97b0baa4e5cf`

- **T/P/E:** [4, 0, 4] → [4, 0, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.96 → 0.96
- **Ambiguity:** The fragment does not identify the speaker or broader conversational motive, but that uncertainty does not materially affect the dominant truth-conditional force.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-acc8280ba5f0`

- **T/P/E:** [4, 0, 2] → [4, 1, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.92 → 0.93
- **Ambiguity:** There is minor uncertainty between P=0 and P=1: the broader speech invokes an asymmetrical lover relationship, but the highlighted declaration itself contains no explicit undertaking.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-b0502164917d`

- **T/P/E:** [4, 0, 3] → [4, 0, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.94 → 0.93
- **Ambiguity:** The narrow excerpt does not establish the speaker’s sincerity or immediate conversational motive, but either uncertainty is compatible with a predominantly truth-conditional classification.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-d0ec3752ec68`

- **T/P/E:** [4, 0, 1] → [4, 0, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.94 → 0.92
- **Ambiguity:** The very short extract does not establish the avowal’s sincerity or broader interpersonal purpose, but those uncertainties do not alter its strongly truth-conditional force.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-fc563b7babfd`

- **T/P/E:** [4, 0, 1] → [4, 0, 0]
- **O / fit:** 0 / `natural`
- **Confidence:** 0.93 → 0.95
- **Ambiguity:** The utterance may have strategic or soothing interpersonal purposes, but these do not alter its predominantly truth-conditional core force.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

## All E changes

- `bronte-jane-eyre-f221719b1af4`: 1 → 0
- `alcott-little-women-58c41f8731dd`: 1 → 0
- `alcott-little-women-f1eab387a74e`: 1 → 0
- `flaubert-madame-bovary-06903c63a2d7`: 4 → 2 **(magnitude ≥2)**
- `flaubert-madame-bovary-1e7d6742e45b`: 2 → 0 **(magnitude ≥2)**
- `flaubert-madame-bovary-400a3aed5a88`: 3 → 0 **(magnitude ≥2)**
- `flaubert-madame-bovary-47361213aeaa`: 1 → 0
- `flaubert-madame-bovary-5396f984c871`: 3 → 0 **(magnitude ≥2)**
- `flaubert-madame-bovary-8c91fb38ed76`: 4 → 2 **(magnitude ≥2)**
- `flaubert-madame-bovary-8fe83e2776a5`: 1 → 0
- `flaubert-madame-bovary-97b0baa4e5cf`: 4 → 0 **(magnitude ≥2)**
- `flaubert-madame-bovary-acc8280ba5f0`: 2 → 0 **(magnitude ≥2)**
- `flaubert-madame-bovary-b0502164917d`: 3 → 0 **(magnitude ≥2)**
- `flaubert-madame-bovary-d0ec3752ec68`: 1 → 0
- `flaubert-madame-bovary-fc563b7babfd`: 1 → 0

## Qualitative preservation review

The paired summaries below support human/AI review; lexical similarity is not treated as proof of preservation.

### `bronte-jane-eyre-14913cd0a6a4`

- **v0.3:** Rochester treats Jane's earlier words as a definite, audible declaration and insistently asks her to repeat them. His possessive reassurance-seeking and their prospective shared life add relational pressure, but they do not transform the core clause into a clear undertaking. The nearby references to Jane's troubling dreams contrast her anxiety with Rochester's appeal to their supposedly “real happiness.”
- **v0.3.1:** Rochester treats Jane’s prior words as a clear and consequential confession, recalls them with pleasure, and presses her to repeat the avowal. His insistence heightens the interpersonal stakes, but Jane’s quoted core utterance remains principally truth-conditional rather than performative or reflex-like.

### `bronte-jane-eyre-9267e616f948`

- **v0.3:** Jane is reassuring Rochester that she is happy rather than fearful about their anticipated life together. Her request to be allowed to speak undisturbed and her extended account of the previous day frame the avowal as considered and explanatory, not as an impulsive outburst. Their engagement and impending wedding lend the words some relational reaffirmation, but the immediate force remains a sincere-seeming declaration of emotional state.
- **v0.3.1:** Jane describes herself as happy and untroubled by the prospect of a new shared life, explicitly grounding that happiness in her love for Rochester. The surrounding reflection on Providence, his journey, their future, and her wedding dress situates the avowal within their engagement. Nevertheless, her request to be allowed to speak undisturbed and the explanatory construction “because I love you” make this a deliberate statement of feeling, not a reflexive outburst or a standalone promise.

### `bronte-jane-eyre-b57472f62694`

- **v0.3:** The declaration is carefully qualified as sisterly love and embedded in Jane’s reasoned refusal to accept that she is obliged to go to India. It distinguishes genuine admiration, confidence, and familial affection from the marital or vocational commitment St. John seeks. Thus it is principally an avowal of an existing feeling, not an acceptance of his proposed relational undertaking.
- **v0.3.1:** The avowal occurs in Jane's reasoned refusal to accept that she is obliged to go to India. She cites admiration, confidence, and sisterly love to explain how much she might have ventured with St John, while sharply limiting the kind of love she professes. In the wider episode, this qualification distinguishes familial affection from the marital love and commitment implicated by St John's proposal; it therefore supports T strongly without converting the utterance into a commitment-performing P event.

### `bronte-jane-eyre-b94304d3eea5`

- **v0.3:** Jane answers Rochester's apparent concern about his diminished condition by saying that his losses are no defects to her and that she loves him more now that she can be useful to him. The comparison rejects a merely dependency-based or status-based objection and presents her present love as sincere, reflective, and compatible with a more reciprocal caregiving relationship. In the wider Chapter XXXVII reunion, the statement also reassures Rochester of her freely renewed attachment, but its core force is chiefly an avowal rather than a promise or spontaneous outburst.
- **v0.3.1:** Jane contrasts Rochester's former position as a proud, independent giver and protector with his present dependence, insisting that his losses do not diminish her attachment. Her declaration both reports intensified love and reassures him that being able to help him is compatible with—and deepens—her freely chosen relationship to him. The wording is reflective and reason-giving rather than reflexive or uncontrolled.

### `bronte-jane-eyre-d0cd60fde247`

- **v0.3:** Jane rejects Rochester’s proposed ornamental transformation of her and refuses reciprocal flattery. Her declaration reassures him that her adverse judgment of his looks is compatible with profound love, but its immediate pragmatic role is to ground uncompromising honesty: she loves him too dearly to flatter him. The surrounding engagement context heightens its relational significance without turning this particular clause into a commitment-making act.
- **v0.3.1:** The love avowal supports Jane’s insistence on honesty and equality: she can love Rochester deeply while refusing to flatter him or accept his attempt to dress her in an alien, ornamental identity. Its placement after “though” makes it a sincere concession within an argument, not a new promise. The intensification “most dearly” and “far too dearly” indicates emotional strength but does not make the utterance independently expressive/reflexive.

### `bronte-jane-eyre-f221719b1af4`

- **v0.3:** Jane interprets St John’s trembling hand, burning eye, and look as disclosing love for Rosamond and confidence that she would accept him. The disclosure is framed by renunciation: he remains verbally silent because he considers his heart already consecrated to a sacred vocation. Thus the imagined address avows love while explicitly withholding any offer or relational undertaking.
- **v0.3.1:** The passage presents affection that is visible despite attempted restraint: his trembling hand and burning eye disclose what he keeps verbally unexpressed. The imagined continuation distinguishes love from commitment. He believes the woman would accept him, but regards his heart as already consecrated elsewhere, so the declaration reports suppressed love while withholding any relational offer.

### `alcott-little-women-15ef9596ac4e`

- **v0.3:** Mrs. March combines affectionate praise with encouragement: she identifies Jo’s effort to overcome a fault and offers love as the “cheery word” that can give her a lift. Jo’s grateful thanks and kiss confirm that the statement is received as sincere maternal affirmation. This supportive function remains contextual to a core truth-conditional avowal rather than constituting a new commitment.
- **v0.3.1:** The avowal is embedded in maternal praise and encouragement: Mrs. March commends Jo for trying to fight her shyness. The qualifying phrase “for it” links the declaration to Jo’s effort, while the surrounding affectionate response—a grateful kiss—supports a sincere reading. Its reassuring interpersonal effect does not itself create performative undertaking force.

### `alcott-little-women-44ca305cf65a`

- **v0.3:** The declaration follows Mr. Brooke's request to know whether Meg cares for him even a little, so it functions as a sincere-seeming confession intended to invite reciprocation. “So much” intensifies the avowal, while “tenderly” presents the delivery as controlled affection rather than a reflexive outburst. The surrounding courtship appeal adds limited performative pressure but does not by itself turn the declaration into a clear undertaking.
- **v0.3.1:** The avowal follows Mr. Brooke’s request to know whether Meg cares for him “a little,” so it functions as a sincere-seeming declaration offered while soliciting reciprocal feeling. The narration marks his manner as tender. These features reinforce the emotional avowal but do not independently turn it into either a commitment or a reflexive discharge.

### `alcott-little-women-58c41f8731dd`

- **v0.3:** On her wedding day, Meg reassures her mother that loving and marrying John does not separate her emotionally from her family or reduce her love for Marmee. Her physical clinging and momentarily full eyes mark strong feeling. Her subsequent plans to visit and retain her place in the family's hearts reinforce the reassurance, but those future-oriented statements should not be transferred into performative force for the core love avowal itself.
- **v0.3.1:** On her wedding day, the speaker reassures Marmee that loving John and marrying him do not separate her emotionally from her family. The negative-comparative wording—“I love you any the less”—occurs within “Don’t feel ... that” and pragmatically affirms that her love remains undiminished. Her clinging and full eyes indicate emotional intensity, while the following promises concern continued family participation; neither feature changes the core clause from a primarily truth-conditional avowal.

### `alcott-little-women-f1eab387a74e`

- **v0.3:** Amy is rebutting the implication that wealth motivated her acceptance. Her claims that she forgot he was rich and would have married him penniless frame the love avowal as sincere reassurance about her emotional state and marital motives. The narrator's statement that she gave “convincing proofs” explicitly endorses the truth of her words. This validating and affectionate context strengthens T but does not turn the embedded avowal itself into a distinct commitment-performing act.
- **v0.3.1:** Amy reassures the addressee that accepting his proposal was not motivated by wealth: she says she forgot he was rich when she said yes and would have married him penniless. The love avowal therefore functions chiefly as a sincere assertion offered to rebut suspicion about her motives. The narrator’s statement that she gave “convincing proofs of the truth of her words” explicitly validates the avowal, while her affectionate response remains contextual confirmation rather than evidence of independent expressive/reflexive force.

### `flaubert-madame-bovary-06903c63a2d7`

- **v0.3:** The mother calls for her daughter, rushes to embrace her, addresses her compassionately as « ma pauvre enfant », and repeats the declaration with exclamation marks. The embrace, repetition, and « comme » construction strongly frame the utterance as an immediate surge of maternal affection, while its ordinary assertion of love remains intact. The passage supplies no distinct undertaking or promise.
- **v0.3.1:** The mother calls for her child, rushes to embrace her, addresses her compassionately as “ma pauvre enfant,” and twice exclaims how much she loves her. This frames the utterance as an affectionate, consoling maternal avowal with a partially expressive outpouring, not as a promise or undertaking.

### `flaubert-madame-bovary-1e7d6742e45b`

- **v0.3:** The speaker asks forgiveness, calls himself foolish and cruel, asserts that the addressee is the only woman who pleases him, and then declares present and lasting love. This makes the declaration strongly avowal-like while also using it to repair a strained interaction. The local passage does not establish whether the profession is sincere, calculated, or durable; those questions do not alter its principally truth-conditional and secondarily commitment-invoking force.
- **v0.3.1:** The speaker seeks forgiveness, admits having been foolish and cruel, asserts the addressee’s uniqueness, avows present love, and promises continued love. This framing makes the utterance both an assertion of feeling and, to a lesser extent, an attempt to repair or reaffirm the relationship. The excerpt alone does not establish whether the avowal is sincere, strategic, or self-deceived, but those possibilities do not alter its presented T/P force.

### `flaubert-madame-bovary-400a3aed5a88`

- **v0.3:** Emma intensifies the avowal through repetition, jealousy, longing, idealisation, and declarations of submission: she cannot do without him, imagines rival women, and calls herself his servant and concubine. This makes the utterance an emotionally charged profession of love rather than a distinct promise. In the wider novel, Emma's expression draws on romantic absolutism while her relationship with Rodolphe is markedly asymmetrical; that narrative irony bears on sincerity, self-understanding, and reception, but it does not prevent the utterance itself from combining truth-conditional avowal with exclamatory force.
- **v0.3.1:** The declaration belongs to an extended, highly emotional profession of dependence, jealousy, devotion, and idealization. Repetition, exclamations, and hyperbole intensify the avowal, while “reprenait-elle” presents it as continued discourse rather than an involuntary blurt. Whatever the sincerity or durability of these feelings, the utterance presents love as true and is adequately represented mainly by T.

### `flaubert-madame-bovary-47361213aeaa`

- **v0.3:** The speaker emphatically rejects or corrects something with “Non,” reduces the explanation to love alone (“voilà tout”), insists that the addressee must not doubt it, and urgently requests verbal confirmation. This makes the avowal emotionally intense and responsive, but the request for “un mot” belongs to the surrounding exchange rather than turning the core declaration into an undertaking.
- **v0.3.1:** The declaration is emphatic and insistent. The speaker not only avows love but presses the addressee to acknowledge believing the avowal: “Vous n’en doutez pas! Dites-le-moi.” This may have persuasive or courtship force in the interaction, but the core love utterance remains adequately represented as truth-conditional rather than as a commitment or reflexive discharge.

### `flaubert-madame-bovary-5396f984c871`

- **v0.3:** “De grâce, restez!” frames “je vous aime!” as an urgent appeal against departure: the speaker invokes an asserted emotional state to persuade the addressee to remain. The exclamation marks and compressed sequence support emotional intensity, while the available passage does not justify a firm conclusion about sincerity, calculation, or the broader relationship.
- **v0.3.1:** The love avowal follows and reinforces an urgent request that the addressee stay. It may therefore function persuasively or as reassurance, but the local text does not show a distinct promise, relational undertaking, or reflex-like loss of verbal control. Sincerity and broader motives remain unresolved by the supplied excerpt.

### `flaubert-madame-bovary-8c91fb38ed76`

- **v0.3:** The declaration occurs amid an urgent request to have the child brought to her and a movement to embrace her. “Comme” and the exclamation mark present the love as emotionally overflowing, while “ma pauvre enfant” adds tenderness and concern. The local passage supplies no evidence of deception, irony, or an undertaking with commitment force.
- **v0.3.1:** The maternal speaker rushes to embrace the addressee and twice exclaims how much she loves her, calling her “ma pauvre enfant.” The scene presents tender, pity-inflected maternal affection. The embrace and repetition intensify and partly externalize that affection, but do not establish any undertaking in the performative sense.

### `flaubert-madame-bovary-8fe83e2776a5`

- **v0.3:** The reply functions as reassurance when Emma seeks confirmation of Rodolphe's love. “Mais oui” can sound mildly impatient or formulaic as well as emphatic, and the wider novel casts doubt on the depth and durability of Rodolphe's declarations. Possible insincerity, habituation, or manipulation concerns the reliability and context of the avowal, not its core T/P/E force.
- **v0.3.1:** The prefatory “Mais oui” and the reporting clause “répondait-il” frame the utterance as an affirmative response, likely to a question or doubt about love. Its possible interpersonal role as reassurance does not by itself make it performative, and its emphatic punctuation does not establish expressive/reflexive force.

### `flaubert-madame-bovary-97b0baa4e5cf`

- **v0.3:** The French construction “Si je t’aime!” functions here as an emphatic response akin to “Do I love you!” rather than as an unresolved condition. Immediate repetition and the stronger continuation “mais je t’adore, mon amour!” intensify the declaration. The excerpt supplies no secure evidence about sincerity, deception, manipulation, or any concrete relational undertaking, and those issues are not needed to represent the core force as combined T and E.
- **v0.3.1:** The French exclamative construction “Si je t’aime!” strongly affirms love, and its immediate repetition followed by “mais je t’adore, mon amour” heightens and amplifies the declaration. Nothing in the supplied fragment establishes that the words undertake a relational commitment, and intensity alone does not warrant expressive/reflexive classification.

### `flaubert-madame-bovary-acc8280ba5f0`

- **v0.3:** The speaker presents her love as overwhelming dependence, jealousy, and idealisation: she cannot do without the addressee, imagines him approaching other women, and calls herself his servant and concubine while calling him her king and idol. This extravagant rhetoric may be theatrical and is situated within the novel’s unequal, ultimately disenchanted adulterous relationship, but it still functions locally as an intelligible avowal rather than as a semantically empty token. The surrounding declarations of submission intensify the relationship rhetoric without turning the core “je t’aime” into a clear commitment-making act.
- **v0.3.1:** The speaker elaborates the declaration through dependence, jealous imaginings, requests for reassurance, self-abasement, and idealizing praise. This makes the avowal rhetorically intense and potentially reassurance-seeking, but those contextual functions do not displace its core presentation of love as true or independently establish expressive/reflexive force.

### `flaubert-madame-bovary-b0502164917d`

- **v0.3:** The idiomatic « Si je t’aime! » is an emphatic confirmation, plausibly answering or resisting doubt about the speaker's love. Repetition, exclamation marks, direct second-person address, and the escalation from loving to adoring make the delivery highly affective. The narrow extract does not identify the participants or establish whether the declaration is sincere, deceptive, or strategically reassuring, but those possibilities do not alter its presented T/E force.
- **v0.3.1:** The construction “Si je t’aime!” reads as an emphatic response or confirmation, approximately “Do I love you!/Indeed I love you,” followed by repetition and the stronger “je t’adore.” This supports forceful reassurance or avowal. Repetition, exclamation marks, and the endearment intensify the delivery but do not independently establish expressive/reflexive force or a commitment.

### `flaubert-madame-bovary-d0ec3752ec68`

- **v0.3:** The utterance is an emphatic response accompanied by putting her arms around the addressee’s neck. This bodily gesture reinforces affectionate engagement and emotional intensity. Nothing in the supplied passage establishes irony, deception, coercion, or an undertaking extending beyond the present avowal.
- **v0.3.1:** The speech tag “répondit-elle” frames the utterance as an answer, while her embrace reinforces its affectionate and emotionally emphatic delivery. The extract provides no independent evidence of promising, undertaking an obligation, or involuntarily blurting out the words. Any possible sincerity, manipulation, or narrative irony remains unresolved by the supplied context.

### `flaubert-madame-bovary-fc563b7babfd`

- **v0.3:** The speaker is astonished by the addressee’s distress and repeatedly urges them to calm down. The love avowal functions as immediate reassurance and as an appeal to something the addressee is said already to know; the following “viens!” reinforces the urgency. Nothing in the supplied excerpt establishes a distinct promise or relational undertaking, regardless of the speaker’s possible sincerity outside this context.
- **v0.3.1:** The speaker is responding to the addressee’s apparent distress or agitation: he repeatedly asks what is wrong, urges her to calm herself, reassures her that she knows he loves her, and then calls her to come. The reassurance is situationally instrumental, but the local text neither establishes deception nor supplies commitment-making or reflexive expressive force.

