# Let Me Count the Ways

A quantitative, AI-assisted investigation of the semantics and pragmatic uses of
the phrase “I love you” across legally reusable text corpora.

## Status

This project is in its initial design phase. The repository currently provides a
scaffold for corpus acquisition, ontology development, annotation, analysis, and
research reporting.

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

See `docs/research_plan.md` for the initial plan and
`docs/research_handoff.md` for the current project state.

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
