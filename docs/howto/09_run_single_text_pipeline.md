# Step 9: run the single-text pipeline

The single-text runner turns an approved local source into a preserved,
metadata-enriched annotation run while retaining visible stage boundaries. It
does not download sources. Begin with a dry run and inspect its inputs before
allowing paid API calls.

## Jane Eyre preparation-only run

From the repository root:

```bash
python scripts/pipeline/run_single_text_pipeline.py \
  provenance/sources/gutenberg-1260.json \
  --patterns data/development/search_patterns_v0_1.json \
  --annotation-version 0.2 \
  --model 5.6 \
  --dry-run
```

The command prints the new run directory. Inspect:

```bash
RUN_DIR='results/pipeline_runs/gutenberg-1260/20260901T100338Z'
python -m json.tool "$RUN_DIR/manifest.json"
python -m json.tool "$RUN_DIR/summary.json"
python -m json.tool "$RUN_DIR/extraction/metadata.json"
python -m json.tool --json-lines "$RUN_DIR/extraction/passages.jsonl" >/dev/null
find "$RUN_DIR/inputs" -maxdepth 1 -type f -name '*.json' -print | sort
```

During execution, the runner prints progress for source resolution, extraction,
input preparation, every annotation attempt, aggregation, and report creation.
The final path printed remains the run directory.

Each prepared input contains occurrence data plus deterministic bibliographic,
source-location, chapter, relative-position, and context-extent metadata. It
does not inject speaker, addressee, relationship, deception, or embedding
interpretations.

## Continue the reviewed run with API calls

Only after the prepared input structure is approved, resume the same directory:

```bash
test -n "${OPENAI_API_KEY:-}" || { echo 'OPENAI_API_KEY is not set'; exit 1; }
python scripts/pipeline/run_single_text_pipeline.py \
  provenance/sources/gutenberg-1260.json \
  --patterns data/development/search_patterns_v0_1.json \
  --annotation-version 0.2 \
  --model 5.6 \
  --run-dir "$RUN_DIR"
```

The annotation version is always explicit. v0.1 remains selectable, and later
versions can be registered without changing the command's conceptual
interface.

## Resume and force behavior

Reusing `--run-dir` checks the source, extraction, annotation version, model,
prompt, and schema fingerprints. Compatible extraction is reused. An
occurrence with a valid result for that exact annotation/model combination is
skipped. Failed, invalid, or unattempted occurrences receive a new numbered
attempt without overwriting earlier artifacts.

Use `--force` only for an intentional new attempt at every occurrence:

```bash
python scripts/pipeline/run_single_text_pipeline.py \
  provenance/sources/gutenberg-1260.json \
  --patterns data/development/search_patterns_v0_1.json \
  --annotation-version 0.2 \
  --model 5.6 \
  --run-dir "$RUN_DIR" \
  --force
```

`--force` does not delete or replace previous attempts.

Every invocation also rebuilds `report.md` from preserved artifacts. Rerunning
the normal command after annotations are complete skips the valid model calls
and refreshes the report idempotently. This is useful after pulling reporting
improvements:

```bash
python scripts/pipeline/run_single_text_pipeline.py \
  provenance/sources/gutenberg-1260.json \
  --patterns data/development/search_patterns_v0_1.json \
  --annotation-version 0.2 \
  --model 5.6 \
  --run-dir "$RUN_DIR"
```

Open `$RUN_DIR/report.md` for one human-readable document containing the run
totals and, for every occurrence, its passage, deterministic metadata,
annotation highlights, and complete structured annotation JSON. Do not add
`--force` when the purpose is only to rebuild the report.

## Artifact layout

```text
<run-dir>/
    source_reference.json
    pricing_snapshot.json
    extraction/
        metadata.json
        passages.jsonl
    inputs/
        <occurrence-id>.json
    annotations/
        <occurrence-id>/
            attempt-001/
                metadata.json
                request.json
                response.json       # after an API response
                output.txt          # raw model output text
                output.json         # after successful JSON parsing
                validation.json     # after structural validation
                cost.json
                failure.json        # on failure
                status.json
    failures/
        <occurrence-and-attempt>.json
    manifest.json
    summary.json
    report.md
```

The source text itself is referenced, not copied. Extraction, prepared inputs,
requests, raw responses, parsed outputs, validation, failures, usage, cost, and
run summaries remain independently inspectable. `summary.json` also points to
the generated human-readable report.

## Failure and context policy

An API, parsing, or validation failure is written to its attempt directory and
the run-level `failures/` directory. The runner continues with independent
occurrences. Restarting the same run retries non-valid occurrences with the
next attempt number.

The initial context-expansion policy is record-only: any v0.2 `context_needs`
remain in the preserved annotation, but the runner does not automatically
expand and silently replace it. A later deterministic expansion stage can add
a new, linked attempt while preserving the original.
