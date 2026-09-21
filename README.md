# Let Me Count the Ways

A quantitative, AI-assisted investigation of the semantics and pragmatic uses of
the phrase “I love you” across legally reusable text corpora.

## Status

The current completed public annotation set contains 252 occurrences from 35
complete works searched in seven languages. Read the [human-readable case
collection](docs/reader/README.md), including source context, translations,
scores and saved explanations. The corpus has grown through successive revisions.

A [controlled context pilot and three further source texts](docs/notes/context_study_v1.md)
are prepared; their new annotations are pending. See [runbook 45](docs/howto/45_read_cases_and_run_context_pilot.md)
for the offline reader and reproducible API workflows. [LaTeX/BibTeX paper drafts](docs/paper/humanities/README.md)
are versioned in the repository.

## Repository layout

- `docs/`: research plans, handoff notes, annotation guidance, and paper drafts
- `data/`: development, raw, and processed corpus data
- `prompts/`: versioned prompts for ontology development and annotation
- `scripts/`: reproducible acquisition, extraction, annotation, and analysis code
- `results/`: development outputs and formal experiment results
- `provenance/`: source, licensing, retrieval, and processing records

## Research principles

- Use only texts whose acquisition and research use can be documented legally.
- Preserve source and licensing provenance throughout the data pipeline.
- Separate exploratory development from preregistered or final experiments.
- Version prompts, models, parameters, annotation schemes, and derived datasets.
- Avoid committing secrets, API keys, or restricted source texts.

See `docs/research_plan.md` for the initial plan,
`docs/research_handoff.md` for the initial project handoff, and
[`docs/next_development_phase_handoff.md`](docs/next_development_phase_handoff.md)
for the current development-phase handover.

## Background reading

- [“On saying ‘I love you’”](docs/notes/on_saying_i_love_you.md): an earlier
  essay motivating the project’s central semantic question

## Source acquisition

- [`provenance/required_sources.md`](provenance/required_sources.md) tracks
  required works, lawful access options, verification questions, and intended
  repository treatment.

## Initial development pipeline

See [`docs/initial_pipeline.md`](docs/initial_pipeline.md) for the staged target
selection, acquisition, extraction, and diagnostic annotation plan. Versioned
search patterns and prompts live under `data/development/` and `prompts/`.

Cygwin-compatible, checkpointed commands for running the pipeline one step at a
time are in [`docs/howto/`](docs/howto/README.md).
