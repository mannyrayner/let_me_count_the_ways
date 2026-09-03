# Step 12: run manifest-defined annotation batches

The batch runner is a thin orchestration layer over the existing single-text
pipeline. It does not duplicate extraction, annotation, validation, retry, or
reporting logic. A corpus manifest says **which sources belong**; CLI arguments
say **how to run them**.

## Development-three dry run

From the repository root:

```bash
python scripts/pipeline/run_batch.py \
  --manifest data/batches/development_three.json \
  --annotation-version 0.3 \
  --model 5.6 \
  --dry-run \
  --compare-with 0.2
```

This locates each source's latest compatible, completed extraction and copies
that immutable inventory into the new batch result. Different sources may have
used different search-pattern versions; the runner matches each preserved
fingerprint to the supplied candidate pattern files. It refuses to extract
implicitly if no compatible inventory exists.

The dry run prepares all per-text inputs and reports the exact number of calls
still required. It makes no API call.

## Execute or resume

Set `OPENAI_API_KEY`, then rerun without `--dry-run`:

```bash
python scripts/pipeline/run_batch.py \
  --manifest data/batches/development_three.json \
  --annotation-version 0.3 \
  --model 5.6 \
  --compare-with 0.2
```

The predictable result directory is
`results/batch_runs/development_three/v0.3-5.6/`. Repeating the command uses
the same directory: valid occurrence outputs are skipped, while incomplete or
failed cases receive new preserved attempts. `--force` intentionally creates a
new attempt even where a valid output exists; it does not overwrite old
attempts.

On resume, the pipeline first tries to recover prior parse failures that consist
of one valid JSON object surrounded only by a Markdown JSON fence. Successful
recovery is recorded in `recovery.json` and costs no additional model call.
Arbitrary trailing prose or multiple JSON objects are not silently discarded.
New v0.3 calls request strict JSON-schema Structured Outputs from the Responses
API, while the local v0.3 validator continues to enforce cross-field rules.

One source failure does not abort other sources. Raw responses, malformed
outputs, validation errors, retry state, requests, parameters, token usage, and
cost remain in each single-text result exactly as before. The batch summary
adds corpus-level totals and per-text result links.

## Reports

Each batch directory contains:

- `summary.json` and `report.md`: machine- and human-readable aggregate state;
- `comparison.json` and `comparison.md` when `--compare-with` is supplied; and
- `texts/<source-id>/`: the complete single-text run artifacts.

The comparison reports T/P/E agreement and differences, O usage and diagnoses,
ontology fit, explicit ambiguity, conspicuous changes, and paired old/new
context summaries for qualitative-preservation review. It is explicitly
diagnostic: the older annotation is not treated as ground truth.

## Add another corpus or annotation version

To add a corpus, create another `data/batches/*.json` file containing canonical
provenance paths. Do not put prompt, model, extraction, or context settings in
that membership manifest. To rerun the same corpus under v0.4, retain the
manifest and select `--annotation-version 0.4` after that contract has been
registered in the single-text pipeline.

Additional historic pattern candidates can be supplied by repeating
`--patterns PATH`. This affects only validation of a reused extraction's
fingerprint; it does not change corpus membership or trigger re-extraction.

## Run the calibrated-E prompt experiment

Prompt v0.3.1 reuses the v0.3 schema but has a distinct prompt hash and result
directory. Run it against the same extractions and compare it with v0.3:

```bash
python scripts/pipeline/run_batch.py \
  --manifest data/batches/development_three.json \
  --annotation-version 0.3.1 \
  --model 5.6 \
  --compare-with 0.3
```

The result is stored alongside, rather than over, v0.3 at
`results/batch_runs/development_three/v0.3.1-5.6/`. Its comparison reports every
E change, marks E changes of magnitude at least two, and also exposes changes in
O, ontology fit, and confidence. The comparison is diagnostic: neither prompt
version is treated as ground truth and lower E is not automatically preferred.

## Audit and check in a completed batch

Set the batch directory after a successful or resumed run:

```bash
BATCH_DIR=results/batch_runs/development_three/v0.3-5.6
```

First require a complete aggregate with no unresolved failures, all 22
annotations valid, and a complete v0.2 comparison. Historical failed attempts
are expected to remain in the scientific record and do not make the completed
batch unsuccessful:

```bash
python - <<'PY'
import json
from pathlib import Path

root = Path("results/batch_runs/development_three/v0.3-5.6")
summary = json.loads((root / "summary.json").read_text(encoding="utf-8"))
comparison = json.loads((root / "comparison.json").read_text(encoding="utf-8"))
assert summary["status"] == "complete", summary
assert summary["texts_completed"] == summary["texts_requested"] == 3, summary
assert summary["valid_annotations"] == summary["occurrences"] == 22, summary
assert summary["failures"] == 0, summary
assert summary["model_calls_needed"] == 0, summary
assert comparison["matched_occurrences"] == 22, comparison
assert not comparison["unmatched"], comparison["unmatched"]
print("Complete batch and comparison: 3 texts, 22/22 valid, 0 unresolved failures.")
PY
```

Audit each underlying single-text run using the existing audit command:

```bash
python scripts/pipeline/audit_pipeline_run.py "$BATCH_DIR/texts/gutenberg-1260" \
  --expected-occurrences 6
python scripts/pipeline/audit_pipeline_run.py "$BATCH_DIR/texts/gutenberg-514" \
  --expected-occurrences 4
python scripts/pipeline/audit_pipeline_run.py "$BATCH_DIR/texts/gutenberg-14155" \
  --expected-occurrences 12
```

Inspect the aggregate and comparison reports, inventory the artifacts, and run
the credential scanner before staging anything:

```bash
sed -n '1,220p' "$BATCH_DIR/report.md"
sed -n '1,260p' "$BATCH_DIR/comparison.md"
find "$BATCH_DIR" -type f -print | sort
python scripts/security/scan_credentials.py "$BATCH_DIR"
git status --short "$BATCH_DIR"
```

Finally ensure that the index is initially empty, stage the complete batch as a
unit, inspect the staged change, commit, and push:

```bash
test -z "$(git diff --cached --name-only)" || {
  echo 'The index already contains staged files; review or unstage them first.' >&2
  exit 1
}
git add "$BATCH_DIR"
git diff --cached --check
git diff --cached --stat
git status --short
git commit -m 'Record development-three v0.3 batch run'
git push origin HEAD
git status --short
```

Stop before `git add` if the batch is partial, an audit fails, the comparison
has unmatched occurrences, or credential scanning reports a finding. Do not
delete failed attempts from an otherwise successful run: the aggregate now
distinguishes zero **unresolved failed occurrences** from the retained count of
**historical failed/invalid attempts**.
