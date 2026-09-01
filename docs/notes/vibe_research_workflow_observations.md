# Vibe-research workflow observations

## Status and purpose

These are provisional, repository-native observations for possible later use in
the methodology or discussion sections. They are not paper prose, a general
theory of humanities research, or an evaluation establishing that any AI
interpretation is ground truth. The empirical research result remains primary.

The note should be revised against preserved handoffs, commits, run artifacts,
model outputs, and human decisions rather than polished from retrospective
memory alone.

## The effective research unit

The practical research unit in this project is not adequately described as one
human using one coding assistant. It currently includes:

- Manny, contributing literary knowledge, theoretical motivations, examples,
  selection and valuation of questions, plausibility checks, and approval of
  consequential decisions;
- interactive ChatGPT-5.6 Sol, acting as a conversational research interlocutor
  and steering layer;
- Codex, acting as a research-engineering and methodological agent within the
  versioned repository;
- high-end structured annotation-model calls, producing inspectable candidate
  analyses rather than ground-truth labels; and
- persistent repository artifacts, which provide memory, provenance,
  reproducibility, testable contracts, and a medium for handoffs.

These elements form a human–AI–agent–repository system. Its capability appears
to arise from their interaction, not merely from the quality of one model.

## Interactive ChatGPT as interlocutor and steering layer

In the work so far, interactive ChatGPT has:

- interpreted experimental outputs and compared cases;
- identified conceptual problems in the original T/P/E implementation;
- proposed distinctions such as core force versus present discourse act;
- connected empirical cases back to Barthes, Sandel, and the motivating theory;
- proposed methodological revisions and experimental priorities;
- generated explicit conceptual handoffs that Codex could operationalise;
- independently reviewed Codex analyses and synthesised multiple reviews; and
- helped select *Little Women* and *Madame Bovary* as the next pressure tests.

The human collaborator reports that this interpretive and redesign cycle occurs
faster than he could sustain manually. One consequence is that results can be
followed almost immediately by conceptual diagnosis and a concrete next
experiment. That report is itself evidence to preserve, not a measured
productivity result.

## Codex as research-engineering and methodological agent

“Coding assistant” is too narrow a description of the role Codex has played in
this project. Its work has included:

- translating conceptual requirements into executable and reviewable stages;
- designing repository structure and provenance machinery;
- implementing extraction, annotation-input preparation, and validation;
- creating and revising prompts and schemas;
- designing diagnostic experiments and methodological safeguards;
- implementing resumability, failure preservation, costing, and reporting;
- conducting independent diagnostic review; and
- maintaining the persistent research environment through code, tests,
  runbooks, and versioned artifacts.

Code-writing is the enabling capability through which Codex can alter and
maintain that environment; it is not the whole research role.

## A fluid division of labour

The observed process is not a one-way sequence in which the human supplies all
ideas and an AI merely implements them. Conceptual contributions have come from
several places:

- human literary examples, priorities, and theoretical intuitions;
- ChatGPT-generated distinctions and syntheses;
- Codex-generated operational structures, caveats, and reproducibility checks;
- annotation-model diagnoses of ontology inadequacy; and
- textual cases that resist the categories proposed by every participant.

Roles overlap. A human selects between directions proposed by AIs; ChatGPT
turns results into a design brief; Codex makes conceptual choices while turning
that brief into an operational contract; annotation calls can identify missing
dimensions; all outputs return to joint review. The resemblance is therefore
closer to a small research group with differentiated strengths than to a fixed
tool/user pair. This is a working description, not a claim of equivalent agency
or responsibility.

## The working loop

```text
research question
    ↓
human–ChatGPT conceptual discussion
    ↓
explicit research handoff
    ↓
Codex operationalisation
    ↓
executable experiment
    ↓
model-generated data
    ↓
ChatGPT / Codex / human review
    ↓
conceptual revision
    ↓
new experiment
```

The loop can occur rapidly because different systems handle different parts of
the epistemic and operational workflow. Its speed should eventually be
documented using concrete sequences of dated artifacts rather than asserted in
the abstract.

## AI-to-AI handoffs

A notable mechanism is the detailed AI-to-AI handoff, mediated and approved by
the human collaborator. Interactive ChatGPT can transform an interpretation of
results into requirements covering concepts, schema behavior, implementation
constraints, tests, and review checkpoints. Codex can then operationalise the
handoff inside the repository.

The human therefore need not personally translate every insight into technical
requirements. This does not remove human steering: the handoff is selected,
transmitted, reviewed, and approved by the collaborator. The repository makes
the exchange persistent and inspectable rather than an invisible model-to-model
conversation.

## Increasing AI autonomy and continuing human responsibility

AI collaborators are performing an increasing share of conceptual analysis,
experiment design, implementation, annotation, diagnosis, documentation, and
methodological review. The workflow may permit them to perform much of the
operational and intellectual labor in a sharply scoped project.

The human collaborator remains consequential in choosing and valuing research
questions, supplying domain judgment, introducing examples, adjudicating among
directions, checking plausibility, controlling credentials and expenditure,
and approving sources, ontology changes, and publication claims. Responsibility
for legal, ethical, and scholarly decisions is not transferred merely because
an AI performed much of the work.

The changing allocation of labor should be documented empirically rather than
celebrated or deplored in advance.

## Why the case may matter

Literary theory and Continental philosophy are not normally presented as
natural domains for coding agents. Yet the systems here participate in close
reading, conceptual analysis, theory criticism, ontology construction, corpus
design, quantitative methodology, and literary interpretation, alongside the
more expected engineering work.

The eventual paper should show this through the actual research history rather
than preach about AI capability. Readers can then judge what the workflow did
and did not contribute.

## Limits and non-claims

This one project does not establish that:

- AI can generally do literary theory;
- human scholars are obsolete;
- the workflow transfers automatically to other humanities questions;
- model judgments are ground truth;
- rapid iteration guarantees correct concepts; or
- canonical-work background knowledge is always reliable.

A defensible provisional observation is narrower: this workflow has worked
unexpectedly well for a sharply defined project, suggesting that related
approaches may be worth exploring elsewhere. Like the annotation ontology, the
workflow account should not be generalised from too few cases.

## Candidate observation for later discussion

> The relevant unit of AI-assisted research may not be the individual model,
> but the whole human–AI–agent–repository system.

The apparent productivity of this system combines human literary judgment,
conversational high-end reasoning, agentic repository manipulation, executable
code, structured model calls, and persistent versioned artifacts. This is more
capable than simply asking one language model a research question. For now this
is a hypothesis about the observed workflow, not a final theoretical claim.

## Evidence to preserve

Where practical, retain:

- human-authored and AI-generated research handoffs;
- independent reviews and later syntheses;
- schema-change rationales and implementation notes;
- prompts, schemas, validators, tests, and code hashes;
- exact requests, raw responses, parsed outputs, failures, retries, and costs;
- source and edition provenance;
- dry-run and complete experiment reports;
- commits and review checkpoints; and
- human steering and approval decisions, including decisions not to proceed.

This evidence can support a concrete reconstruction of how the research
developed and expose mistakes or revisions that a retrospective success story
might erase.
