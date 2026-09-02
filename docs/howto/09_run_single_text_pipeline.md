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

## Review and check in the completed run

The complete run directory is a research record and should be checked in as a
unit after review. Do not commit only `report.md`: the source reference,
fingerprints, extraction, enriched inputs, exact requests, raw responses,
parsed outputs, validation decisions, attempt statuses, failures, token usage,
costs, machine-readable summaries, and human-readable report are all needed to
audit or reproduce the result.

The source text, provenance record, prompt, schema, model catalogue, validator,
and runner are referenced by path and hash. They should already be tracked and
should not be copied into the run directory. Python caches, temporary files,
environment files, and credentials are not research artifacts and must not be
added.

For the current *Jane Eyre* run, first rebuild the report without `--force` so
it incorporates the latest reporting code while reusing all valid annotations:

```bash
RUN_DIR='results/pipeline_runs/gutenberg-1260/20260901T100338Z'

python scripts/pipeline/run_single_text_pipeline.py \
  provenance/sources/gutenberg-1260.json \
  --patterns data/development/search_patterns_v0_1.json \
  --annotation-version 0.2 \
  --model 5.6 \
  --run-dir "$RUN_DIR"
```

Run structural and completeness checks over the preserved results:

```bash
python - "$RUN_DIR" <<'PY'
import json
import sys
from pathlib import Path

from scripts.annotation.validate_classification import validate_v0_2

run_dir = Path(sys.argv[1])
manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
summary = json.loads((run_dir / "summary.json").read_text(encoding="utf-8"))
passages = [
    json.loads(line)
    for line in (run_dir / "extraction/passages.jsonl").read_text(encoding="utf-8").splitlines()
    if line
]

assert manifest["status"] == "complete", manifest["status"]
assert manifest["annotation_version"] == "0.2"
assert manifest["extracted_occurrences"] == 6
assert manifest["valid_occurrences"] == 6
assert summary["valid_occurrences"] == 6
assert len(passages) == 6
assert (run_dir / "report.md").is_file()

for passage in passages:
    occurrence_id = passage["occurrence_id"]
    input_path = run_dir / "inputs" / f"{occurrence_id}.json"
    assert input_path.is_file(), input_path
    attempts = sorted((run_dir / "annotations" / occurrence_id).glob("attempt-*"))
    valid_attempts = []
    for attempt in attempts:
        status_path = attempt / "status.json"
        if not status_path.is_file():
            continue
        status = json.loads(status_path.read_text(encoding="utf-8"))
        if status.get("state") == "valid":
            valid_attempts.append(attempt)
    assert valid_attempts, f"no valid attempt for {occurrence_id}"
    selected = valid_attempts[-1]
    for name in [
        "metadata.json", "request.json", "response.json", "output.txt",
        "output.json", "validation.json", "cost.json", "status.json",
    ]:
        assert (selected / name).is_file(), selected / name
    output = json.loads((selected / "output.json").read_text(encoding="utf-8"))
    validate_v0_2(output, occurrence_id)

print("Jane Eyre v0.2 run passed: six extracted and six valid annotations.")
PY
```

Although the runner does not store the API authorization header, scan the run
directory before staging it. The following command should print the success
message and no matching file content:

```bash
python scripts/security/scan_credentials.py "$RUN_DIR"
```

The scanner exits nonzero if a likely credential is found, if a requested path
does not exist, or if scanning cannot be completed. It reports only file and
line locations, not the possible secret itself.

Inspect the human-readable report and the set of files before committing:

```bash
sed -n '1,240p' "$RUN_DIR/report.md"
find "$RUN_DIR" -type f -print | sort
git status --short "$RUN_DIR"
```

Then stage the whole run directory, verify the staged patch, commit, and push
the current branch:

```bash
git add "$RUN_DIR"
git diff --cached --check
git diff --cached --stat
git status --short
git commit -m 'Record Jane Eyre v0.2 pipeline run'
git push origin HEAD
git status --short
```

If any validation or credential check fails, stop before `git add`. Preserve
the local directory for diagnosis rather than deleting or selectively hiding a
failed attempt: failures and retries are part of the scientific record once
they have been reviewed as safe to publish.

## Failure and context policy

An API, parsing, or validation failure is written to its attempt directory and
the run-level `failures/` directory. The runner continues with independent
occurrences. Restarting the same run retries non-valid occurrences with the
next attempt number.

The initial context-expansion policy is record-only: any v0.2 `context_needs`
remain in the preserved annotation, but the runner does not automatically
expand and silently replace it. A later deterministic expansion stage can add
a new, linked attempt while preserving the original.
