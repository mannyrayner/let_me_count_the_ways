# Annotation comparison: v0.2 → v0.3

> This is a diagnostic comparison. v0.2 is not treated as ground truth; changes may
> reflect improvement, information loss, overclassification, instability, or ambiguity.

- **Batch:** `development_three`
- **Matched occurrences:** 22
- **Unmatched occurrences:** 0
- **Exact T/P/E agreement:** truth_conditional 21/22, performative 11/22, exclamatory_reflexive 12/22
- **All three scores exact:** 7/22
- **O scores:** O=0: 22; O=1: 0; O≥2: 0
- **Ontology fit:** natural: 22, strained: 0, inadequate: 0

## Cases requiring inspection

### `bronte-jane-eyre-14913cd0a6a4`

- **T/P/E:** [4, 1, 0] → [4, 1, 0]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The text gives Rochester's exact revoicing of Jane's earlier words rather than the original speaking event directly; however, both his framing and the quoted sentence strongly support an original truth-conditional avowal.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `bronte-jane-eyre-9267e616f948`

- **T/P/E:** [4, 1, 0] → [4, 1, 0]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The surrounding discussion of a shared future creates weak performative pressure, though that future-oriented context does not turn the core clause into an explicit commitment.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `bronte-jane-eyre-b57472f62694`

- **T/P/E:** [4, 1, 0] → [4, 0, 0]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The avowal affirms an existing bond, but its explicit sisterly qualification and argumentative setting provide little basis for performative undertaking force.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `bronte-jane-eyre-b94304d3eea5`

- **T/P/E:** [4, 1, 0] → [4, 1, 0]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The utterance's reaffirmation of devotion during their reunion gives some support to P, although its grammatical and pragmatic centre remains an avowal of feeling rather than an explicit undertaking.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `bronte-jane-eyre-d0cd60fde247`

- **T/P/E:** [4, 1, 0] → [4, 0, 0]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The intensifiers “most dearly” and “far too dearly” convey strong emotion, but the utterance remains a deliberate propositional avowal rather than an emotionally triggered exclamation.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `bronte-jane-eyre-f221719b1af4`

- **T/P/E:** [4, 1, 0] → [4, 0, 1]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The words are Jane’s interpretation of nonverbal signs rather than St John’s spoken formulation, so the exact intentional force of his expression is inferential.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `alcott-little-women-15ef9596ac4e`

- **T/P/E:** [4, 1, 0] → [4, 0, 0]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The utterance also encourages and reassures Jo, but those interpersonal effects do not by themselves give it performative undertaking force.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `alcott-little-women-44ca305cf65a`

- **T/P/E:** [4, 1, 0] → [4, 1, 0]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The declaration may help enact a courtship appeal, but that contextual relational function provides only weak support for P beyond the dominant T force.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `alcott-little-women-58c41f8731dd`

- **T/P/E:** [4, 1, 0] → [4, 0, 1]
- **O / fit:** 0 / `natural`
- **Ambiguity:** Her clinging and full eyes give the utterance some exclamatory coloring, but its controlled syntax and reassurance function make truth-conditional force dominant.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `alcott-little-women-f1eab387a74e`

- **T/P/E:** [4, 1, 0] → [4, 0, 1]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The emphatic “how much” and the emotional surrounding speech give slight exclamatory force, but not enough to compete substantially with the clear truth-conditional avowal.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-06903c63a2d7`

- **T/P/E:** [4, 0, 3] → [3, 0, 4]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The main overlap is between a sincere truth-conditional avowal and an exclamation whose intensified form foregrounds immediate emotion; both forces are substantially present.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-1e7d6742e45b`

- **T/P/E:** [4, 1, 1] → [4, 2, 2]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The future-tense continuation can be heard either as a prediction of enduring feeling or as a promise-like undertaking, so the precise degree of performative force is uncertain.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-400a3aed5a88`

- **T/P/E:** [4, 1, 2] → [4, 0, 3]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The imperfect reporting frame and highly stylised romantic language suggest a recurrent or rehearsed mode of expression, which slightly complicates how reflex-like the outburst is; nevertheless, its presented exclamatory force is substantial.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-47361213aeaa`

- **T/P/E:** [4, 1, 1] → [4, 0, 1]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The exclamation and urgent surrounding appeals create some E pressure, but the utterance retains strong, explicit propositional force.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-5396f984c871`

- **T/P/E:** [4, 0, 1] → [4, 0, 3]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The very short extract does not establish how spontaneous or strategically persuasive the declaration is, but that uncertainty lies between truth-conditional and exclamatory force rather than outside T/P/E.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-8c91fb38ed76`

- **T/P/E:** [4, 0, 3] → [4, 0, 4]
- **O / fit:** 0 / `natural`
- **Ambiguity:** T and E are simultaneously strong: the utterance is both a genuine avowal and an exclamation, rather than clearly reducible to only one mode.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-8fe83e2776a5`

- **T/P/E:** [4, 0, 1] → [4, 0, 1]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The emphatic form gives limited E support, while the wider relationship raises doubts about sincerity; neither factor displaces the utterance's dominant truth-conditional force.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-97b0baa4e5cf`

- **T/P/E:** [4, 0, 1] → [4, 0, 4]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The exclamatory delivery does not erase the clear avowal: T and E are both strongly supported. The wider sincerity or strategic purpose of the declaration cannot be determined from the short extract.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-acc8280ba5f0`

- **T/P/E:** [4, 1, 3] → [4, 0, 2]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The highly emotional delivery creates some overlap between truth-conditional avowal and exclamatory expression, but there is little evidence of performative undertaking force.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-b0502164917d`

- **T/P/E:** [4, 0, 3] → [4, 0, 3]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The exclamatory form is prominent, but it does not displace the utterance's clear propositional avowal; the precise balance between T and E is therefore somewhat gradient.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-d0ec3752ec68`

- **T/P/E:** [4, 1, 1] → [4, 0, 1]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The exclamation and embrace provide limited support for E, but the brief context does not show that the utterance is predominantly reflex-like rather than an intelligible avowal.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

### `flaubert-madame-bovary-fc563b7babfd`

- **T/P/E:** [4, 0, 1] → [4, 0, 1]
- **O / fit:** 0 / `natural`
- **Ambiguity:** The exclamation marks and crisis-like exchange give the avowal some emotionally triggered force, but not enough to weaken its clear propositional content.
- **O diagnosis:** {'tpe_failure': None, 'core_not_context': None}

## Qualitative preservation review

The paired summaries below support human/AI review; lexical similarity is not treated as proof of preservation.

### `bronte-jane-eyre-14913cd0a6a4`

- **v0.2:** At the level of Jane's original avowal, “because I love you” straightforwardly presents her love for Edward as a true emotional state and as the reason she values the hope of living with him. The reference to living together gives the avowal prospective relational significance, but it is an expression of hope rather than a promise or substantial undertaking; performative force is therefore weak. The complete sentence is reflective and syntactically reasoned (“I think ... because”), not substantially reflexive or exclamatory. Rochester currently speaks the highlighted words within the fictional world, but he speaks them as part of an attributed revoicing of Jane's earlier utterance. His surrounding references to “those words,” their articulation on her lips, and his having heard them also make the wording an object of metalinguistic attention. Both the current quotation and the original avowal are represented as spoken, although the schema's single actuality field cannot distinguish those two speech events. Rochester quotes Jane's earlier avowal as evidence that she loves him, emphasizes that she “cannot deny it,” and commands her to repeat it. In the immediate exchange this helps redirect attention from Jane's disturbing dreams toward the relationship's promised happiness. The quotation consequently combines affectionate reassurance with an insistent elicitation of reaffirmation. Calling her a “Little nervous subject,” dismissing her apprehensions as “visionary woe,” and insisting on repetition add pressure and a manipulative element, especially given Rochester's concealed marital impediment. The revoicing preserves Jane's explicit propositional avowal rather than challenging or retracting it. Rochester strengthens its salience by describing it as solemn and musical, treating it as undeniable evidence, and demanding repetition. At the same time, he redirects it from Jane's original explanation of hopeful shared life into a means of controlling the present conversation and displacing her ominous anxieties. Knowledge of Rochester's concealed existing marriage makes that redirection more troubling and dramatically ironic, without making Jane's avowal itself insincere. Supported assessments: deception_misrepresentation, manipulation_pressure.
- **v0.3:** Rochester treats Jane's earlier words as a definite, audible declaration and insistently asks her to repeat them. His possessive reassurance-seeking and their prospective shared life add relational pressure, but they do not transform the core clause into a clear undertaking. The nearby references to Jane's troubling dreams contrast her anxiety with Rochester's appeal to their supposedly “real happiness.”

### `bronte-jane-eyre-9267e616f948`

- **v0.2:** Jane explicitly presents her love for Rochester as a true emotional state and as the reason she welcomes the prospect of living with him. The causal construction, “because I love you,” gives the avowal unusually clear propositional and explanatory force. Although spoken within an engagement and capable of reaffirming intimacy, the clause does not itself substantially undertake or renew the marriage commitment. Jane's request to be allowed to continue talking undisturbed also weighs against treating it as a reflexive exclamation. The words are represented as being spoken directly by Jane to Rochester in the current fictional scene. They are not a quotation of an earlier avowal, an imagined utterance, or narrator-supplied wording for nonverbal conduct. Jane directly avows love while explaining why she considers the prospect of living with Rochester “a glorious thing.” In the surrounding exchange she also counters Rochester's apparent belief that she is troubled by fears, so the avowal contributes to reassurance that her anticipated life with him is genuinely desired. Its explanatory and reassuring effects do not make the core proposition strongly performative. The immediate context preserves and strengthens the avowal through Jane's sustained descriptions of happiness, thoughts of Rochester, and imaginative investment in their future. Background knowledge of Rochester's existing marriage does not undermine Jane's sincerity, but redirects the implications of her stated hope: the apparently uncomplicated shared future is already threatened by a fact concealed from her, producing dramatic irony.
- **v0.3:** Jane is reassuring Rochester that she is happy rather than fearful about their anticipated life together. Her request to be allowed to speak undisturbed and her extended account of the previous day frame the avowal as considered and explanatory, not as an impulsive outburst. Their engagement and impending wedding lend the words some relational reaffirmation, but the immediate force remains a sincere-seeming declaration of emotional state.

### `bronte-jane-eyre-b57472f62694`

- **v0.2:** The speaker directly presents her love as a genuine existing state, coordinated with admiration and confidence: “I admire, confide in, and, as a sister, I love you.” The carefully inserted qualification “as a sister” specifies the kind of love rather than retracting it. There is at most weak performative force in affirming an existing sibling-like bond; the utterance does not substantially undertake a new commitment, and the surrounding conditional concerns what she would have ventured, not a present promise. Its measured syntax and argumentative setting weigh strongly against an exclamatory or reflexive reading. The words are represented as spoken directly by Jane within the fictional scene. “As a sister” qualifies and limits the otherwise potentially romantic declaration, functioning as a relational hedge or specification rather than indicating uncertainty about whether she loves the addressee. Jane avows affection while explaining why she would have been willing to venture much with this particular person. At the same time, “as a sister” establishes distance from a romantic or marital construal and reinterprets their intimacy as sibling-like. In the broader refusal beginning “I am not under the slightest obligation,” this qualification contributes to rejecting the marital or otherwise binding basis on which St John wants her to accompany him; it does not reject affection itself. The context preserves the literal avowal of love but redirects its expected romantic force toward sisterly affection. The parenthetical qualification distances Jane from marital implications, while the conditional “With you I would have ventured much” makes the love relevant as an explanation of trust and willingness rather than as a present undertaking to travel or marry.
- **v0.3:** The declaration is carefully qualified as sisterly love and embedded in Jane’s reasoned refusal to accept that she is obliged to go to India. It distinguishes genuine admiration, confidence, and familial affection from the marital or vocational commitment St. John seeks. Thus it is principally an avowal of an existing feeling, not an acceptance of his proposed relational undertaking.

### `bronte-jane-eyre-b94304d3eea5`

- **v0.2:** Jane explicitly presents her love for Rochester as a genuine continuing state and asserts that it is now stronger. The comparative construction and its reasoned explanation give the utterance strong propositional force. Saying it directly also enacts intimacy and offers limited relational affirmation, but it does not itself substantially create or renew an obligation or undertaking, so its performative support remains weak. Its controlled comparative syntax is not substantially exclamatory or reflex-like. The highlighted words are represented as words Jane currently speaks to Rochester in the fictional scene. They are neither a quotation of an earlier avowal nor wording narratively supplied for nonverbal conduct. Jane directly avows love, reassures Rochester that his altered circumstances do not diminish her attachment, and explains why she loves him 'better now.' She also reinterprets his dependence: rather than treating the loss of his former independence as a relational defect, she values being able to contribute and implicitly challenges his former insistence on being only giver and protector. The surrounding comparison preserves the literal avowal while strengthening it through 'better now.' It redirects attention from love as attraction to a proud, independent protector toward love compatible with care, reciprocity, and Jane's usefulness. The final clause challenges Rochester's former hierarchical conception of himself as exclusively giver and protector.
- **v0.3:** Jane answers Rochester's apparent concern about his diminished condition by saying that his losses are no defects to her and that she loves him more now that she can be useful to him. The comparison rejects a merely dependency-based or status-based objection and presents her present love as sincere, reflective, and compatible with a more reciprocal caregiving relationship. In the wider Chapter XXXVII reunion, the statement also reassures Rochester of her freely renewed attachment, but its core force is chiefly an avowal rather than a promise or spontaneous outburst.

### `bronte-jane-eyre-d0cd60fde247`

- **v0.2:** Jane explicitly presents her love for Rochester as true and intensifies it with “most dearly” and “far too dearly.” The clause is a sincere avowal embedded in an argument that genuine love requires honesty rather than flattery. Its direct interpersonal delivery gives it slight commitment-enacting force, but it does not substantially undertake or renew an obligation, and it is not primarily a reflexive exclamation. The highlighted words are represented as being spoken by Jane directly to Mr. Rochester in the current fictional scene. They are neither a quotation of an earlier avowal nor wording narratively supplied for nonverbal conduct. Jane avows love while explaining why she refuses to flatter Rochester: loving him deeply is offered as a reason for speaking candidly. The avowal also reassures him that her refusal to call him handsome is not emotional rejection. Within the larger exchange, she uses the love-content to support an admonition that neither partner should disguise or idealise the other. The concessive “though” preserves the avowal despite Jane's refusal to praise Rochester's appearance. “Most dearly” and “far too dearly” strengthen the represented feeling. The surrounding argument redirects the avowal toward a defence of candour and challenges any assumption that romantic love should entail flattery, ornamental display, or loss of authentic identity.
- **v0.3:** Jane rejects Rochester’s proposed ornamental transformation of her and refuses reciprocal flattery. Her declaration reassures him that her adverse judgment of his looks is compatible with profound love, but its immediate pragmatic role is to ground uncompromising honesty: she loves him too dearly to flatter him. The surrounding engagement context heightens its relational significance without turning this particular clause into a commitment-making act.

### `bronte-jane-eyre-f221719b1af4`

- **v0.2:** The attributed words present as true a settled romantic state: the man loves the woman and believes she would accept him. They have only weak performative force because he does not actually utter them, and the continuation explicitly distinguishes loving her from offering his heart or undertaking a relationship. His heart's dedication to a 'sacred altar' frames the love as something he intends to sacrifice rather than enact. The formulation is reflective and controlled, not a reflexive exclamation. The narrator supplies articulate words for what the man's 'sad and resolute look' appears to communicate. The construction 'He seemed to say' hedges the attribution, while 'if he did not say it with his lips' explicitly establishes that the represented words were not spoken. The quotation marks therefore mark constructed or imagined discourse, not direct represented speech or quotation of an earlier utterance. The narrator interprets trembling, a burning eye, and a resolute look as evidence of love, then dramatizes the inferred meaning as an unspoken monologue. The current act explains both his attraction and why he remains silent: he expects success but considers himself already committed to a religious sacrifice. It is not a current direct avowal by the man. The embedding preserves the basic proposition that he loves her, but 'seemed to say' and the narrator's mediation weaken its status as directly asserted speech and distance the reader from his literal words. Conversely, the involuntary bodily signs and the claim that he cannot conceal his feeling strengthen the inference that the emotion is genuine. The continuation redirects the apparent avowal away from courtship or commitment and toward an account of self-denial: he believes she would accept him, yet refuses to offer his heart because of a prior sacred dedication.
- **v0.3:** Jane interprets St John’s trembling hand, burning eye, and look as disclosing love for Rosamond and confidence that she would accept him. The disclosure is framed by renunciation: he remains verbally silent because he considers his heart already consecrated to a sacred vocation. Thus the imagined address avows love while explicitly withholding any offer or relational undertaking.

### `alcott-little-women-15ef9596ac4e`

- **v0.2:** “I love you for it” directly presents Jo's love for the addressee as true and identifies the addressee's effort against shyness as a reason or occasion for the avowal. Its primary force is truth-conditional. Uttering it also weakly enacts affectionate affirmation, but it does not substantially undertake or renew an obligation or commitment, and it is not framed as a reflexive exclamation. The highlighted words occur within a represented spoken turn. The continuation “Thank you, Mother,” followed by Jo's action attributes the encompassing turn to Jo. The words are neither a quotation of an earlier avowal nor wording narratively supplied for nonverbal conduct. Jo currently avows love while praising and encouraging the addressee for trying to overcome shyness. “For it” explains the immediate basis of the praise-inflected avowal. The affectionate recognition also has a reassuring effect, but that effect does not turn the core proposition into a strong performative commitment. The context preserves the avowal's ordinary literal force. “That's my good girl” and the recognition that the addressee does try strengthen its affectionate and encouraging character. “For it” redirects attention from an unqualified declaration of love to love expressed through approval of a particular moral effort; this is better read as praise than as a claim that love is strictly conditional on success.
- **v0.3:** Mrs. March combines affectionate praise with encouragement: she identifies Jo’s effort to overcome a fault and offers love as the “cheery word” that can give her a lift. Jo’s grateful thanks and kiss confirm that the statement is received as sincere maternal affirmation. This supportive function remains contextual to a core truth-conditional avowal rather than constituting a new commitment.

### `alcott-little-women-44ca305cf65a`

- **v0.2:** Mr. Brooke explicitly presents his intense romantic love for Meg as true. The first-person present-tense wording, intensified by “so much,” strongly supports a truth-conditional avowal. In this courtship setting the declaration has relational consequences, but it does not itself clearly undertake or renew an obligation, so its core performative support remains weak. Its complete proposition and the narrator’s attribution make a substantially reflexive or merely exclamatory reading unsupported. The words are represented as being spoken by Mr. Brooke to Meg in the current fictional scene. The attribution “added Mr. Brooke tenderly” confirms direct represented speech rather than quotation of an earlier or hypothetical utterance. Mr. Brooke directly avows love and assures Meg of its intensity. In conjunction with his request to know whether she cares for him, the avowal also functions as a courtship appeal inviting a reciprocal answer. This is not precisely “elicitation_of_reaffirmation,” because the passage does not establish that Meg has previously affirmed love. Nothing in the embedding negates, quotes, distances, or challenges the avowal. “So much,” the address “dear,” and the narrator’s description “tenderly” strengthen its emotional intensity and apparent sincerity. The preceding request to know whether Meg cares places the avowal within an appeal for reciprocity without changing its basic assertion of love.
- **v0.3:** The declaration follows Mr. Brooke's request to know whether Meg cares for him even a little, so it functions as a sincere-seeming confession intended to invite reciprocation. “So much” intensifies the avowal, while “tenderly” presents the delivery as controlled affection rather than a reflexive outburst. The surrounding courtship appeal adds limited performative pressure but does not by itself turn the declaration into a clear undertaking.

### `alcott-little-women-58c41f8731dd`

- **v0.2:** Although the words occur inside the negative directive “Don’t feel ... that I love you any the less,” the speaker is not denying love; she strongly avows that her love for her mother has not diminished. The principal content is therefore truth-conditional. The surrounding promises of continued visits and family belonging give slight commitment-like resonance, but the love-content itself does not substantially undertake a new obligation or relationship. The narrator explicitly attributes the quoted words to the speaker with “she said,” so this is current spoken dialogue in the fictional world. Negation operates at the level of the directive and comparative proposition: the mother is told not to believe that the speaker loves her less. Thus the embedding reverses a possible diminished-love inference rather than negating the existence of love. The speaker avows continuing love while reassuring her mother that marriage and intense love for John do not separate her emotionally from her family. “For loving John so much” explains the circumstance that might otherwise prompt fear of diminished filial attachment. The subsequent statements about daily visits and retaining her old place in the family's hearts reinforce this reassurance. The negative-comparative frame preserves the affirmative love-content by rejecting diminution: she loves her mother no less than before. “Marmee dear,” physical clinging, tearful eyes, and plans for continued contact strengthen the sincerity and emotional salience of the avowal. The context redirects a generic declaration into a specific reassurance that marital love will not displace filial love or family membership.
- **v0.3:** On her wedding day, Meg reassures her mother that loving and marrying John does not separate her emotionally from her family or reduce her love for Marmee. Her physical clinging and momentarily full eyes mark strong feeling. Her subsequent plans to visit and retain her place in the family's hearts reinforce the reassurance, but those future-oriented statements should not be transferred into performative force for the core love avowal itself.

### `alcott-little-women-f1eab387a74e`

- **v0.2:** Amy presents her love for the addressee as an existing and substantial emotional state. The degree construction “how much I love you” presupposes or asserts love while emphasizing its magnitude. Although saying this also reassures and relationally reaffirms the addressee, it does not substantially create or undertake a new commitment, so its performative support is weak. The utterance is emotionally emphatic but remains propositionally controlled rather than reflex-like. The matched words occur within Amy’s presently represented spoken dialogue. The imagined poverty concerns circumstances in which she could demonstrate her love; it does not make the love itself hypothetical. The printed quotation around “Yes” revoices an earlier acceptance, but the matched love-content is not that quotation. Amy directly avows love while reassuring the addressee that his wealth did not motivate her acceptance. Her willingness to have married him penniless and her wish for an opportunity to prove her love explain and support that reassurance. The wish construction redirects hypothetical force toward an imagined opportunity to demonstrate love, while preserving the love as a present reality. Amy’s claim that she would have married him without money strengthens the avowal by excluding mercenary motivation. The narrator further strengthens it by describing her subsequent affectionate behavior as “convincing proofs of the truth of her words.”
- **v0.3:** Amy is rebutting the implication that wealth motivated her acceptance. Her claims that she forgot he was rich and would have married him penniless frame the love avowal as sincere reassurance about her emotional state and marital motives. The narrator's statement that she gave “convincing proofs” explicitly endorses the truth of her words. This validating and affectionate context strengthens T but does not turn the embedded avowal itself into a distinct commitment-performing act.

### `flaubert-madame-bovary-06903c63a2d7`

- **v0.2:** “Comme je t’aime!” presents the mother's love as true with maximal directness. Its exclamative syntax and repetition make it substantially expressive or reflex-like, but do not erase its clear propositional content. It does not undertake a new commitment or obligation. The narrator's speech tag, “dit sa mère,” represents the mother as currently speaking the quoted words in the fictional world. This is neither a citation of an earlier utterance nor narration that merely supplies words for nonverbal behavior. The mother directly avows her love to the child. The exclamation, repetition, affectionate vocative, and accompanying attempt to kiss her intensify the avowal; the limited context does not firmly establish a separate act such as reassurance. Direct represented speech preserves the love-content without quotation, negation, or distancing. Repetition and the congruent action of rushing to kiss the child strengthen its emotional intensity and apparent sincerity.
- **v0.3:** The mother calls for her daughter, rushes to embrace her, addresses her compassionately as « ma pauvre enfant », and repeats the declaration with exclamation marks. The embrace, repetition, and « comme » construction strongly frame the utterance as an immediate surge of maternal affection, while its ordinary assertion of love remains intact. The passage supplies no distinct undertaking or promise.

### `flaubert-madame-bovary-1e7d6742e45b`

- **v0.2:** “Je t’aime” directly presents the speaker’s present love as true. Its unhedged first-person present tense gives it very strong truth-conditional force. The adjacent “je t’aimerai toujours” adds a promise-like assertion of future constancy, but the highlighted present-tense avowal does not by itself substantially undertake a new relational obligation. The exclamation marks and urgent apologetic setting add emotion without reducing the utterance to a reflex-like exclamation. The passage represents a character currently addressing another character in direct speech. Nothing indicates quotation of an earlier utterance, writing, imagination, negation, or narrative verbalisation of nonverbal conduct. The speaker directly avows love while asking to be forgiven. “Tu es la seule qui me plaise,” the admission of having been foolish and cruel, and “je t’aimerai toujours” make the declaration a reassurance of exclusivity and constancy intended to repair an apparent relational disturbance. The final question, “Qu’as-tu? dis-le donc!”, also solicits an explanation of the addressee’s distress. Direct speech preserves the avowal’s ordinary assertive force. Locally, the claims that the addressee is the only person who pleases the speaker and that the love will last forever strengthen it through exclusivity and projected permanence. At the same time, remembered wider context from the deteriorating Emma–Léon affair and the novel’s subsequent events weakens confidence in the literal durability of “toujours,” giving the reassurance an ironic or unstable retrospective aspect without proving that the present-tense feeling is consciously false.
- **v0.3:** The speaker asks forgiveness, calls himself foolish and cruel, asserts that the addressee is the only woman who pleases him, and then declares present and lasting love. This makes the declaration strongly avowal-like while also using it to repair a strained interaction. The local passage does not establish whether the profession is sincere, calculated, or durable; those questions do not alter its principally truth-conditional and secondarily commitment-invoking force.

### `flaubert-madame-bovary-400a3aed5a88`

- **v0.2:** The highlighted « je t’aime » directly presents the speaker's love as true. The continuation—her inability to do without the addressee, painful jealousy, and extravagant praise—intensifies that avowal and makes it partly exclamatory. « Je suis ta servante et ta concubine » invokes an existing lover relationship and submissive posture, but neither the highlighted formula nor its immediate elaboration substantially creates or renews a commitment. The narrator represents a woman directly addressing her lover, with « reprenait-elle » functioning as a speech attribution. The words are presented as spoken in the fictional world, not as a quotation of an earlier or hypothetical utterance. She directly avows love and explains its intensity through dependence and jealous suffering. Her questions—especially « aucune ne te plaît? »—seek reassurance that no other woman attracts him. The combination of declared inability to live without him, jealousy, and solicitations for confirmation places emotional pressure on the addressee, although the passage does not establish calculated manipulation. The surrounding speech preserves the literal avowal and strongly intensifies it through repetition, dependency, jealousy, superlative self-comparison, and idolizing praise. It also redirects the avowal toward possessiveness and a request for exclusivity. Knowledge of the wider novel creates some ironic distance between Emma's romantic absolutism and the unstable, unequal affair in which she voices it; that distance qualifies the relational implications without negating the sincerity of her present emotion. Supported assessments: manipulation_pressure.
- **v0.3:** Emma intensifies the avowal through repetition, jealousy, longing, idealisation, and declarations of submission: she cannot do without him, imagines rival women, and calls herself his servant and concubine. This makes the utterance an emotionally charged profession of love rather than a distinct promise. In the wider novel, Emma's expression draws on romantic absolutism while her relationship with Rodolphe is markedly asymmetrical; that narrative irony bears on sincerity, self-understanding, and reception, but it does not prevent the utterance itself from combining truth-conditional avowal with exclamatory force.

### `flaubert-madame-bovary-47361213aeaa`

- **v0.2:** The declarative “je vous aime” straightforwardly presents the speaker's love as true, reinforced by “voilà tout,” which frames love as the simple and sufficient explanation. It does not itself clearly undertake a durable obligation or relational commitment. The exclamation and urgent continuation add emotional intensity, but the utterance retains strong propositional force rather than functioning principally as a reflexive cry. The dash introduces words currently uttered by a character in the fictional scene. Nothing in the supplied text indicates quotation of an earlier utterance, writing, imagination, negation, or metalinguistic mention. The speaker directly avows love and insists that the addressee should not doubt it. “Dites-le-moi; un mot! un seul mot!” urgently solicits verbal confirmation that she believes or accepts the avowal, rather than clearly asking her to avow her own love. The repeated imperatives and narrowing demand for even one word exert pressure. Knowledge of Rodolphe's calculated seduction of Emma supports interpreting this pressure as manipulative, although that does not turn the core proposition into a performative commitment. Locally, “voilà tout,” the denial of possible doubt, the exclamation marks, and the demand for an answer rhetorically strengthen the avowal's urgency and apparent certainty. In the wider novel, Rodolphe's calculated pursuit and eventual abandonment of Emma weaken the credibility of the claim as an avowal of deep or durable love. The immediate demand for confirmation also uses the love-content to press Emma toward emotional acquiescence. Supported assessments: deception_misrepresentation, manipulation_pressure.
- **v0.3:** The speaker emphatically rejects or corrects something with “Non,” reduces the explanation to love alone (“voilà tout”), insists that the addressee must not doubt it, and urgently requests verbal confirmation. This makes the avowal emotionally intense and responsive, but the request for “un mot” belongs to the surrounding exchange rather than turning the core declaration into an undertaking.

### `flaubert-madame-bovary-5396f984c871`

- **v0.2:** The explicit declarative “je vous aime” presents the speaker's love as true. Its exclamation mark and placement within an urgent plea give it emotional intensity, but its propositional force remains clear, so the exclamatory/reflexive reading is secondary rather than independently substantial. It does not itself undertake or renew a commitment. The dialogue dash, imperative addressed to another person, and exclamation marks represent a character currently speaking in the fictional world. Nothing in the supplied text indicates quotation, report, imagination, writing, negation, or hedging. The speaker directly avows love while pleading “De grâce, restez!” The avowal functions pragmatically as an emotionally forceful reason for the requested action. The short extract supports pleading and persuasion, but not by itself coercion or manipulation. The context preserves the ordinary avowal of love, while the urgent request and repeated exclamatory punctuation intensify its emotional presentation. Its discourse function is also redirected toward supporting the immediate plea that the addressee stay.
- **v0.3:** “De grâce, restez!” frames “je vous aime!” as an urgent appeal against departure: the speaker invokes an asserted emotional state to persuade the addressee to remain. The exclamation marks and compressed sequence support emotional intensity, while the available passage does not justify a firm conclusion about sincerity, calculation, or the broader relationship.

### `flaubert-madame-bovary-8c91fb38ed76`

- **v0.2:** “Comme je t’aime” explicitly presents the speaker’s love as true. Its repetition and exclamative syntax make it an intense outpouring rather than a neutral report. Nothing in the passage indicates that the words undertake or renew a distinct commitment or obligation. The words occur as the mother’s present fictional-world speech, continuous with the dialogue introduced by “dit sa mère.” They are neither a quotation of an earlier avowal nor wording narratively supplied for nonverbal conduct. The mother directly avows her love. Her rush to embrace the addressee and the compassionate address “ma pauvre enfant” also make the utterance consoling or reassuring, although the limited excerpt does not identify the precise distress being answered. The immediate context preserves the literal avowal and intensifies it through repetition, exclamation, the degree construction “Comme,” the affectionate-pitying address “ma pauvre enfant,” and the congruent act of rushing forward to embrace the addressee.
- **v0.3:** The declaration occurs amid an urgent request to have the child brought to her and a movement to embrace her. “Comme” and the exclamation mark present the love as emotionally overflowing, while “ma pauvre enfant” adds tenderness and concern. The local passage supplies no evidence of deception, irony, or an undertaking with commitment force.

### `flaubert-madame-bovary-8fe83e2776a5`

- **v0.2:** The unqualified first-person present statement “je t’aime” explicitly presents the male speaker's love for the addressee as true. Its exclamation mark and the emphatic response “Mais oui” add emotional or impatient emphasis, but the utterance remains a clear proposition rather than a predominantly reflexive cry. It reassures the addressee but does not itself undertake a sufficiently definite commitment to warrant performative support. Possible insincerity affects the credibility of the assertion, not its core truth-conditional form. The words are presented as dialogue spoken by a male character, explicitly attributed by “répondait-il.” They are not merely mentioned, imagined, negated, or quoted from an earlier utterance. The speaker directly avows love while answering an explicit or implicit doubt. “Mais oui” makes the reply strongly reassuring, though its briskness may also suggest impatience or formulaic placation. The supplied fragment does not independently establish that the present act is coercive or manipulative. Direct representation and the speech tag preserve the literal avowal as something the character says. At the same time, the responsive “Mais oui” can make it sound routine or impatient rather than spontaneous. Background knowledge of Flaubert's broader portrayal of Rodolphe as increasingly cynical and emotionally disengaged from Emma further weakens the avowal's credibility and creates narratorial or readerly distance from its face value. Supported assessments: deception_misrepresentation.
- **v0.3:** The reply functions as reassurance when Emma seeks confirmation of Rodolphe's love. “Mais oui” can sound mildly impatient or formulaic as well as emphatic, and the wider novel casts doubt on the depth and durability of Rodolphe's declarations. Possible insincerity, habituation, or manipulation concerns the reliability and context of the avowal, not its core T/P/E force.

### `flaubert-madame-bovary-97b0baa4e5cf`

- **v0.2:** The idiomatic elliptical construction “Si je t’aime!” emphatically affirms that the speaker loves the addressee; the continuation “mais je t’adore, mon amour” makes its propositional avowal especially clear. Repetition and exclamation give the utterance expressive intensity, but it is not merely reflex-like and retains strong truth-conditional force. It does not itself undertake or renew a defined commitment. The dialogue dash and first-person address present the words as currently spoken by a character in the fictional world. Nothing in the supplied text marks them as a citation of an earlier or hypothetical utterance. The speaker directly avows love and intensifies the answer from loving to adoring. The responsive idiom “Si je t’aime!” strongly suggests an emphatic answer to an expressed or implied doubt or question, so reassurance is also likely, although the eliciting turn is not supplied. Locally, repetition, exclamation, “je t’adore,” and the endearment “mon amour” preserve and strengthen the avowal. Background knowledge of Rodolphe’s calculated seduction of Emma and his eventual abandonment of her introduces likely dramatic or narratorial distance between the declaration’s extravagant surface and its reliability. Because the excerpt does not identify the speaker or include surrounding narration, that distancing interpretation is less certain than the local intensification. Supported assessments: deception_misrepresentation.
- **v0.3:** The French construction “Si je t’aime!” functions here as an emphatic response akin to “Do I love you!” rather than as an unresolved condition. Immediate repetition and the stronger continuation “mais je t’adore, mon amour!” intensify the declaration. The excerpt supplies no secure evidence about sincerity, deception, manipulation, or any concrete relational undertaking, and those issues are not needed to represent the core force as combined T and E.

### `flaubert-madame-bovary-acc8280ba5f0`

- **v0.2:** “Je t’aime” directly presents the speaker's love as true, and “je t’aime à ne pouvoir me passer de toi” specifies it as an overwhelming need. “Oh!”, immediate repetition, and the ensuing emotional crescendo support a strong exclamatory dimension. The surrounding claims that she is his servant and concubine have weak pledge-like implications, but the love-content itself does not clearly create or renew an obligation. A female character currently speaks the words in the fictional scene. The reporting clause “reprenait-elle” explicitly attributes the direct speech to her; this is neither a quotation of an earlier utterance nor imagined speech. The speaker directly avows love and uses “c’est que” to present that love as an explanation. Her subsequent jealous questions—whether he speaks to other women and whether any pleases him—seek reassurance or reaffirmation of exclusivity. Claims of being unable to live without him, together with extreme self-subordination and praise, place emotional pressure on the addressee, although the passage does not establish calculated manipulation. Repetition and the claim that she cannot do without him strengthen the avowal. Jealous imaginings, the servant/concubine language, and the sequence “roi,” “idole,” and idealizing compliments redirect love toward possessiveness, dependency, submission, and romantic idolization. Background knowledge of Rodolphe's jaded reception of Emma's conventional romantic language introduces distance between her experienced intensity and the wider novel's treatment of its rhetoric; that distance does not by itself make the avowal insincere. Supported assessments: manipulation_pressure.
- **v0.3:** The speaker presents her love as overwhelming dependence, jealousy, and idealisation: she cannot do without the addressee, imagines him approaching other women, and calls herself his servant and concubine while calling him her king and idol. This extravagant rhetoric may be theatrical and is situated within the novel’s unequal, ultimately disenchanted adulterous relationship, but it still functions locally as an intelligible avowal rather than as a semantically empty token. The surrounding declarations of submission intensify the relationship rhetoric without turning the core “je t’aime” into a clear commitment-making act.

### `flaubert-madame-bovary-b0502164917d`

- **v0.2:** “Si je t’aime!” is an emphatic echo-like response meaning approximately “Do I love you!/Of course I love you,” not a genuine conditional. Repetition and the escalation “mais je t’adore, mon amour” strongly avow and intensify the claimed emotional state. The line has no clear commitment-making force beyond its immediate relational reassurance. The dash and first-person address represent a character currently speaking these words in the fictional world. Nothing in the supplied extract indicates quotation of an earlier utterance, imagined speech, or narratorial verbalisation. The speaker directly avows love and, through the echoing “Si je t’aime!” and intensified “je t’adore,” answers or pre-empts doubt with extravagant reassurance. Background knowledge identifying the speaker as probably Rodolphe, whose courtship of Emma is calculated and whose devotion proves unreliable, supports a further manipulative use: the declaration helps maintain Emma's emotional investment. That manipulation is less certain than the avowal and reassurance because the immediate prompting exchange is not supplied. The context preserves the literal avowal and strengthens it through repetition, exclamation, the scalar rise from “love” to “adore,” and the endearment “mon amour.” In the wider relationship, Rodolphe's calculated seduction and eventual abandonment cast retrospective suspicion on the declaration and support reading its emphatic reassurance as emotionally manipulative, although they do not conclusively prove that he felt no affection at this exact moment. Supported assessments: deception_misrepresentation, manipulation_pressure.
- **v0.3:** The idiomatic « Si je t’aime! » is an emphatic confirmation, plausibly answering or resisting doubt about the speaker's love. Repetition, exclamation marks, direct second-person address, and the escalation from loving to adoring make the delivery highly affective. The narrow extract does not identify the participants or establish whether the declaration is sincere, deceptive, or strategically reassuring, but those possibilities do not alter its presented T/E force.

### `flaubert-madame-bovary-d0ec3752ec68`

- **v0.2:** The unqualified present-tense declaration “Je t’aime” directly presents the speaker's love as true. The exclamation mark and simultaneous embrace add emotional intensity, but the clearly articulated proposition is not merely reflexive. The avowal may affirm the existing relationship, yet it does not itself clearly undertake a new obligation or commitment, so performative support remains weak. The dash introduces dialogue, and “répondit-elle” explicitly attributes the words to a female character as her current spoken reply. This is neither a quotation of an earlier utterance nor wording supplied for nonverbal conduct. The speaker currently avows love to the person denoted by “t’.” The reporting verb identifies it as a reply, but the omitted preceding turn does not establish whether it is also reassurance, an answer to elicitation, or part of some other conversational strategy. Nothing in the supplied sentence hedges, negates, quotes, or distances the declaration. The exclamation and the speaker's act of putting her arms around the addressee's neck reinforce its immediate emotional and intimate force. The wider novel's treatment of romantic self-dramatization may complicate judgments about durability, but it does not cancel the locally presented avowal.
- **v0.3:** The utterance is an emphatic response accompanied by putting her arms around the addressee’s neck. This bodily gesture reinforces affectionate engagement and emotional intensity. Nothing in the supplied passage establishes irony, deception, coercion, or an undertaking extending beyond the present avowal.

### `flaubert-madame-bovary-fc563b7babfd`

- **v0.2:** The embedded clause “je t’aime” clearly presents the speaker's love as true. “Tu sais bien que” frames that proposition as something the addressee already knows, strengthening its assertive and reassuring presentation. The exclamation mark and surrounding agitation add emotional intensity, but the grammatically explicit proposition remains primary. Nothing here substantially undertakes or renews a relational commitment. The love-content occurs within ongoing character dialogue introduced by a speech dash and accompanied by “répétait-il.” It is represented as presently spoken in the fictional world, not as a quotation of an earlier or hypothetical avowal. The speaker directly affirms that he loves the addressee, while “Tu sais bien” makes the affirmation a reminder or reassurance rather than entirely new information. In the sequence “Calme-toi! reprends-toi!... Tu sais bien que je t’aime! ... viens!”, the avowal also supports directives asking the distressed addressee to regain control and come with him. This creates some immediate interpersonal pressure, although it does not by itself establish manipulation. The context preserves the ordinary propositional content of loving someone. “Tu sais bien” strengthens its presentation by presupposing that the love is already known, while the surrounding calming commands and final “viens!” redirect the avowal toward reassurance and securing an immediate behavioral response. Supported assessments: manipulation_pressure.
- **v0.3:** The speaker is astonished by the addressee’s distress and repeatedly urges them to calm down. The love avowal functions as immediate reassurance and as an appeal to something the addressee is said already to know; the following “viens!” reinforces the urgency. Nothing in the supplied excerpt establishes a distinct promise or relational undertaking, regardless of the speaker’s possible sincerity outside this context.

