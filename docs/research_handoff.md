# Let Me Count the Ways

## Research handoff

### Working title

**Let Me Count the Ways: A Quantitative AI-Based Investigation of “I Love You”**

### Project idea

This project asks whether recent high-end AI systems make it possible to carry out a serious large-scale empirical study of the semantics and pragmatics of the expression **“I love you”**.

The immediate intellectual starting point is Roland Barthes’s discussion of *je-t’aime* in *Fragments d’un discours amoureux*. Barthes gives an elegant and influential account of the expression as a special kind of utterance, strongly associated with performative and holophrastic properties.

We think the account is insightful but may be substantially too simple.

A useful methodological warning comes from Wittgenstein, *Philosophical Investigations* §593:

> “A main cause of philosophical disease—a one-sided diet: one nourishes one’s thinking with only one kind of example.”

The central question is therefore empirical:

**When “I love you” occurs in naturally situated discourse, how often does it behave in the way Barthes suggests, and what other recurrent kinds of use are found?**

Until very recently, answering this on a useful scale would have required an intolerable amount of expert human annotation. Current high-end AI systems may change this. An AI can potentially acquire suitable textual material, extract large numbers of contextualised occurrences, analyse them individually, give motivated classifications, quantify patterns, and identify difficult or ambiguous cases.

The purpose of this project is to find out whether that actually works.

---

## Historical starting point

An earlier informal essay, [“On saying ‘I love you’”](notes/on_saying_i_love_you.md), proposed three broad kinds of analysis:

1. **Truth-conditional**
   The speaker reports a mental or emotional state: roughly, “I have feelings of love toward you.”

2. **Performative**
   The speaker makes an undertaking or commitment: roughly, “I undertake to value, cherish or remain committed to you.”

3. **Expletive / reflexive**
   The expression is produced more like an emotionally triggered exclamation, without a clear propositional or performative intention.

The essay also noted that combinations are possible.

These categories are useful starting hypotheses, but **they are not to be treated as a final annotation ontology**.

One of the most important goals of the project is to give the AI considerable freedom to discover that this initial scheme is inadequate.

---

## Key counterexamples and motivating cases

### Cora Sandel, *Alberte* trilogy

Near the end of the final volume, Alberte’s cruel and dishonest partner Sivert reminds her that she once said:

> “Jeg elsker dig.”

Alberte barely remembers saying it and reconstructs it as something that may simply have escaped her during an intimate moment.

Sivert, however, insists that saying it was significant:

> “Du sa det. Og det er en feil. Det er mannen som først skal si denslags.”

The case is important because the two characters construe the same utterance differently.

For Alberte, the original utterance seems largely non-performative, perhaps reflexive or truth-conditional.

Sivert retrospectively imposes a performative interpretation.

The scene also appears integrally related to the novel’s feminist structure. Sivert has already announced that he intends to exploit the legal resources available to him in order to impose his will on Alberte. Here, he arguably does something parallel with language: he claims authority to decide what her earlier words must have meant and uses that interpretation against her.

This is a particularly natural counterexample to any theory that assumes a single privileged interpretation of “I love you”.

### *Postcards from the Edge*

A male character says:

> “I think I love you.”

The female character immediately replies:

> “When will you know for sure?”

In the larger context, the man appears predatory and duplicitous. He seems to want the pragmatic benefits of making a commitment while choosing a formulation that lets him retreat from it later.

This suggests that annotation must distinguish not only broad semantic/pragmatic type, but also strategic ambiguity, degree of commitment, and hearer uptake.

### Tolstoy, *War and Peace*

Pierre says *Je vous aime!* after effectively finding himself socially committed to marrying Hélène.

The utterance simultaneously has several properties:

- it is something convention requires him to say;
- it helps bind him socially;
- it is connected with attraction;
- he himself experiences the words as inadequate and artificial.

This is a good example of why ambiguity or mixed interpretation should not be treated as annotation failure.

---

## A central methodological principle

**Ambiguity is part of the phenomenon.**

The goal is not simply to assign every occurrence to a single clean category.

An occurrence may support several interpretations. Different participants may construe it differently. A literary text may deliberately exploit uncertainty about what the utterance means or does.

Potential levels of construal include:

- speaker construal;
- hearer construal;
- textual or authorial framing;
- reader construal.

These should not automatically be collapsed.

Nor should “author construal” be treated as directly observable. In literary texts, authorial stance is inferred through framing, irony, narrative structure, free indirect discourse, genre, and wider context.

A useful annotation system may therefore need to represent:

- multiple simultaneous interpretations;
- uncertainty;
- disagreement among participants;
- strategic ambiguity;
- deceptive or manipulative use;
- differences between utterance function and attributed function;
- degree of confidence in any interpretation;
- textual evidence supporting the interpretation.

The eventual quantitative study should attempt to **measure ambiguity rather than eliminate it**.

---

## Development methodology

Do not begin by freezing the T/P/E taxonomy.

Instead:

1. Construct a deliberately varied development set of perhaps 100–200 contextualised occurrences of “I love you”.
2. Include literary, dramatic, conversational and other suitable sources where legally and practically possible.
3. Give a high-end model freedom to analyse the examples in detail.
4. Start from the T/P/E distinction but explicitly permit the model to:
   - modify it;
   - add dimensions;
   - split categories;
   - merge categories;
   - reject categories;
   - identify phenomena not anticipated in advance.
5. Ask the model to propose annotation scheme v1.
6. Apply v1 to a fresh development sample.
7. Inspect cases where the scheme gives unnatural, forced or unstable analyses.
8. Revise the scheme.
9. Repeat until genuinely new phenomena become relatively infrequent.
10. Freeze the scheme only then.
11. Run the large-scale annotation.
12. Validate the AI annotation against a carefully selected human-annotated sample.

Every version of the annotation guidelines, prompts, outputs and revisions should be retained.

The evolution of the annotation scheme is itself research evidence.

---

## Possible quantitative outputs

The final study may include:

- frequency of major semantic/pragmatic patterns;
- frequency of mixed cases;
- distribution of interpretive uncertainty;
- model confidence;
- human/model agreement;
- model/model agreement;
- speaker/hearer disagreement;
- strategic ambiguity;
- cases where more context changes the interpretation;
- examples with very high agreement;
- examples with principled disagreement;
- recurring subtypes discovered during ontology development.

Exact metrics should emerge from the development process rather than being fixed prematurely.

---

## Controls and comparisons

Possible comparison expressions include:

- “I hate you”
- “I admire you”
- “I need you”
- “I trust you”
- “I forgive you”
- “I miss you”

These may help test whether “I love you” is unusually semantically or pragmatically unstable.

They are optional and should not distract from the core study.

---

## Scope discipline

There are many interesting adjacent questions:

- prosody;
- cross-linguistic comparison;
- Swedish *Jag ääääälskar dig*;
- English emphatic forms such as “I luuurve you”;
- Hungarian *szeretlek*;
- phonological compression;
- cultural variation;
- gender differences;
- historical change.

These should mostly be treated as footnotes or future work unless they become directly necessary.

The present paper should remain sharply focused.

---

## Desired argumentative structure of the paper

A likely structure is:

1. State the problem.
2. Present Barthes’s account carefully and sympathetically.
3. Introduce one or more compelling natural counterexamples, especially Sandel.
4. Invoke the Wittgensteinian methodological worry: perhaps the theory rests on too narrow a diet of examples.
5. Ask whether counterexamples are rare curiosities or common phenomena.
6. Explain why this was previously difficult to investigate quantitatively.
7. Introduce the AI-based methodology.
8. Explain the iterative development of the annotation scheme.
9. Present the large-scale findings.
10. Discuss what they imply for Barthes’s account.
11. Conclude cautiously that this particular AI-assisted method worked well enough to be interesting, while making no broad claim that it will generalise automatically to literary theory or Continental philosophy as a whole.

A possible final methodological observation is:

**One case cannot establish a general research methodology. But if AI-assisted large-scale interpretation works here, there may be other areas of philosophy and literary studies where claims based on a small number of carefully chosen examples can now be revisited using much larger bodies of evidence.**

---

## Vibe research principle

This project should itself be developed using the vibe research methodology.

The AI should not merely execute a research design already fully specified by humans.

It should be given substantial freedom to:

- propose data sources;
- write acquisition and analysis software;
- inspect development examples;
- identify weaknesses in the current conceptual scheme;
- propose and revise annotation structures;
- design experiments;
- identify anomalies;
- suggest statistical analyses;
- interpret results;
- draft and revise the eventual paper.

The human collaborators should steer, criticise, test and make consequential decisions, but should avoid unnecessarily reducing the AI to a mechanical implementation role.

The aim is not to prove in advance that AI can perform research in this domain.

The immediate aim is simply to conduct the best possible study of “I love you”.
