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
directory. The `development_three` manifest is the reproducible definition of
the three-corpus experiment:

| Corpus | Source ID | Expected passages |
| --- | --- | ---: |
| *Jane Eyre* | `gutenberg-1260` | 6 |
| *Little Women* | `gutenberg-514` | 4 |
| *Madame Bovary* | `gutenberg-14155` | 12 |

Do not run three ad hoc single-text commands. The one batch command below runs
all three manifest members, keeps their outputs together, and produces a
22-passage comparison with v0.3. Before starting, update the checkout, confirm
that the prompt and baseline exist, and make sure the working tree is clean:

```bash
cd "$LMCW"
git pull --ff-only
test -f prompts/annotation/classify_passage_v0_3_1.md
test -f results/batch_runs/development_three/v0.3-5.6/summary.json
git status --short
```

The reference must be a complete v0.3 run made with the same model alias. If
the baseline path above is absent, complete the v0.3 procedure earlier in this
runbook first. Do not silently compare different model aliases: that would
confound the prompt change with a model change.

### Prepare and review the 22 calls

First use a dry run with the same comparison arguments as the real run:

```bash
python scripts/pipeline/run_batch.py \
  --manifest data/batches/development_three.json \
  --annotation-version 0.3.1 \
  --model 5.6 \
  --dry-run \
  --compare-with 0.3
```

Inspect `results/batch_runs/development_three/v0.3.1-5.6/report.md`. It should
list all three source IDs and 22 calls needed (6 + 4 + 12). A dry run makes no
API calls, but it does create prepared inputs and summary files. These are
temporary working artifacts, not research results to commit. Stop if a corpus
is missing, an extraction cannot be reused, or the counts differ.

### Execute or resume all three corpora

Confirm that the API key is set without printing it, then rerun without
`--dry-run`:

```bash
test -n "${OPENAI_API_KEY:-}" || {
  echo 'OPENAI_API_KEY is not set' >&2
  exit 1
}
python scripts/pipeline/run_batch.py \
  --manifest data/batches/development_three.json \
  --annotation-version 0.3.1 \
  --model 5.6 \
  --compare-with 0.3
```

The result is stored alongside, rather than over, v0.3 at
`results/batch_runs/development_three/v0.3.1-5.6/`. The command is resumable:
rerun the identical command after a failure, without deleting the directory or
adding `--force`. Valid annotations will be skipped and failed or incomplete
ones will receive preserved new attempts. Use `--force` only for an explicitly
approved fresh sample, since it deliberately calls the model again for valid
passages.

### Verify completeness and the v0.3 comparison

After the run, verify the aggregate, every corpus, and the pairing with v0.3:

```bash
python - <<'PY'
import json
from pathlib import Path

root = Path("results/batch_runs/development_three/v0.3.1-5.6")
summary = json.loads((root / "summary.json").read_text(encoding="utf-8"))
comparison = json.loads((root / "comparison.json").read_text(encoding="utf-8"))
expected = {"gutenberg-1260": 6, "gutenberg-514": 4, "gutenberg-14155": 12}

assert summary["annotation_version"] == "0.3.1", summary
assert summary["model_alias"] == "5.6", summary
assert summary["status"] == "complete", summary
assert summary["texts_completed"] == summary["texts_requested"] == 3, summary
assert summary["valid_annotations"] == summary["occurrences"] == 22, summary
assert summary["failures"] == summary["model_calls_needed"] == 0, summary
actual = {item["source_id"]: item["valid_occurrences"] for item in summary["texts"]}
assert actual == expected, actual

assert comparison["old_annotation_version"] == "0.3", comparison
assert comparison["new_annotation_version"] == "0.3.1", comparison
assert comparison["matched_occurrences"] == 22, comparison
assert not comparison["unmatched"], comparison["unmatched"]
compared = {}
for record in comparison["records"]:
    compared[record["source_id"]] = compared.get(record["source_id"], 0) + 1
assert compared == expected, compared
print("Complete v0.3.1 run: 3 corpora, 22/22 valid and paired with v0.3.")
PY
```

Audit each corpus independently so an aggregate total cannot hide a misplaced
or incomplete text:

```bash
BATCH_DIR=results/batch_runs/development_three/v0.3.1-5.6
python scripts/pipeline/audit_pipeline_run.py "$BATCH_DIR/texts/gutenberg-1260" \
  --expected-occurrences 6
python scripts/pipeline/audit_pipeline_run.py "$BATCH_DIR/texts/gutenberg-514" \
  --expected-occurrences 4
python scripts/pipeline/audit_pipeline_run.py "$BATCH_DIR/texts/gutenberg-14155" \
  --expected-occurrences 12
```

Produce a compact per-corpus quantitative view before reading the individual
cases. This prevents the 12 *Madame Bovary* passages from obscuring behavior in
the two smaller corpora:

```bash
python - <<'PY'
import json
from collections import defaultdict
from pathlib import Path

path = Path("results/batch_runs/development_three/v0.3.1-5.6/comparison.json")
records = json.loads(path.read_text(encoding="utf-8"))["records"]
by_source = defaultdict(list)
for record in records:
    by_source[record["source_id"]].append(record)
for source_id in ("gutenberg-1260", "gutenberg-514", "gutenberg-14155"):
    rows = by_source[source_id]
    exact = sum(row["exact_tpe_agreement"] for row in rows)
    e_changed = sum(row["e_changed"] for row in rows)
    large_e = sum(row["conspicuous_e_change"] for row in rows)
    other = sum(row["other_changed"] for row in rows)
    fit = sum(row["ontology_fit_changed"] for row in rows)
    confidence = sum(abs(row["confidence_difference"]) >= 0.2 for row in rows)
    print(f"{source_id}: n={len(rows)}, exact T/P/E={exact}, "
          f"E changes={e_changed} (>=2: {large_e}), O changes={other}, "
          f"fit changes={fit}, confidence changes >=0.20={confidence}")
PY
```

Finally read `comparison.md`, not just its headline counts. Review every item
under **All E changes**, every magnitude-two-or-greater T/P/E change, each O or
ontology-fit change, confidence changes of at least 0.20, explicit ambiguity,
and the paired contextual summaries. Break the review down by the three
`source_id` values as well as considering the aggregate. The empirical question
is whether v0.3.1 distinguishes reflexive expressive force more consistently
without losing context or moving errors into T, P, or O; a lower E score is not
automatically an improvement, and v0.3 is a comparator rather than ground
truth.

Record qualitative judgments separately from the generated comparison. If a
pair is missing, do not compare corpus percentages or check in the run; repair
or resume it until all 22 occurrence IDs are paired. Then follow **Audit and
check in a completed batch** below. The completeness checks and audits above
replace that section's v0.3/v0.2-specific versions; continue with its report
inspection, credential scan, and staging safeguards using the already-set
`BATCH_DIR`. Commit with an appropriate message such as
`Record development-three v0.3.1 batch run`.

## Audit and check in a completed batch

Keep implementation changes and generated research results separate. A prompt,
schema, validator, or runner pull request must not include dry-run placeholders,
credential-failure summaries, or regenerated copies of an already authoritative
batch. Merge the implementation first; then run, audit, and check in only the
completed new result directory in a dedicated results commit or pull request.
This prevents generated files on an implementation branch from conflicting with
authoritative results produced meanwhile on the target branch.

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
