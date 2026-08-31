# Step 8: complete the Jane Eyre v0.1 diagnostic set

This runbook implements Phase A1 of the
[next-development-phase handover](../next_development_phase_handoff.md). It uses
the unchanged v0.1 prompt and schema on the two remaining extracted occurrences
so that all six *Jane Eyre* results are directly comparable.

Run **one substep at a time**. After each API call, stop and share the requested
artifacts for review. Do not edit the prompt, schema, input helper, or validator
during this step, and do not use a previous run directory as the output root.

| Substep | Case | Occurrence ID |
| --- | --- | --- |
| 8A | Future-life avowal | `bronte-jane-eyre-9267e616f948` |
| 8B | Comparative-care avowal | `bronte-jane-eyre-b94304d3eea5` |

## Preflight: confirm the six-occurrence inventory

```bash
cd "$LMCW"
SOURCE_ID='gutenberg-1260'
PASSAGES_FILE="data/development/passages/$SOURCE_ID.jsonl"

test -f "$PASSAGES_FILE"
python -m json.tool --json-lines "$PASSAGES_FILE" >/dev/null
python - "$PASSAGES_FILE" <<'PY'
import json
import sys

expected = {
    "bronte-jane-eyre-d0cd60fde247",
    "bronte-jane-eyre-9267e616f948",
    "bronte-jane-eyre-14913cd0a6a4",
    "bronte-jane-eyre-f221719b1af4",
    "bronte-jane-eyre-b57472f62694",
    "bronte-jane-eyre-b94304d3eea5",
}
with open(sys.argv[1], encoding="utf-8") as stream:
    records = [json.loads(line) for line in stream]
actual = [record["occurrence_id"] for record in records]
assert len(actual) == 6, f"expected 6 records, found {len(actual)}"
assert len(set(actual)) == 6, "duplicate occurrence IDs found"
assert set(actual) == expected, f"unexpected occurrence IDs: {actual}"
print("Jane Eyre inventory passed: 6 expected occurrences.")
PY
```

If this check fails, stop. Do not regenerate the extraction or proceed with an
API call until the discrepancy has been reviewed.

## Substep 8A: future-life avowal

Prepare exactly one classification input:

```bash
cd "$LMCW"
SOURCE_ID='gutenberg-1260'
CASE_NAME='future_life_avowal'
OCCURRENCE_ID='bronte-jane-eyre-9267e616f948'
PASSAGES_FILE="data/development/passages/$SOURCE_ID.jsonl"
CLASSIFICATION_INPUT="results/development_runs/classification_inputs/$OCCURRENCE_ID.json"
RUN_ROOT="results/development_runs/classification_diagnostics/$CASE_NAME"

test ! -e "$CLASSIFICATION_INPUT" || {
  echo "Refusing to overwrite existing input: $CLASSIFICATION_INPUT"
  exit 1
}
test ! -e "$RUN_ROOT" || {
  echo "Refusing to reuse existing run root: $RUN_ROOT"
  exit 1
}

python scripts/annotation/prepare_classification_input.py \
  "$PASSAGES_FILE" "$CLASSIFICATION_INPUT" \
  --occurrence-id "$OCCURRENCE_ID"
python -m json.tool "$CLASSIFICATION_INPUT"
```

Make one API call with the unchanged v0.1 artifacts:

```bash
test -n "${OPENAI_API_KEY:-}" || { echo 'OPENAI_API_KEY is not set'; exit 1; }
python scripts/api/call_responses.py \
  --model '5.6' \
  --prompt prompts/annotation/classify_passage_v0_1.md \
  --input "$CLASSIFICATION_INPUT" \
  --schema prompts/annotation/classification_schema_v0_1.json \
  --output-root "$RUN_ROOT"
```

Inspect and validate the newly created run:

```bash
RUN_DIR="$(find "$RUN_ROOT" -mindepth 1 -maxdepth 1 -type d | sort | tail -1)"
test -n "$RUN_DIR" || { echo 'No run directory found'; exit 1; }
printf 'Run directory: %s\n' "$RUN_DIR"
python -m json.tool "$RUN_DIR/metadata.json"
python -m json.tool "$RUN_DIR/pricing_snapshot.json"
python -m json.tool "$RUN_DIR/cost.json"
python -m json.tool "$RUN_DIR/response.json" >/dev/null
python -m json.tool "$RUN_DIR/output.txt" >/dev/null
python scripts/annotation/validate_classification.py "$RUN_DIR/output.txt" \
  --expected-occurrence-id "$OCCURRENCE_ID"
sed -n '1,300p' "$RUN_DIR/output.txt"
```

### Review checkpoint for 8A

Stop and share complete `metadata.json`, `cost.json`, and `output.txt`. Review
whether the result distinguishes the core avowal from its role as Jane's reason
for anticipating life with Rochester, avoids treating that anticipated future
as an undertaking made by the phrase itself, and requests more context only for
claims that the supplied passage cannot settle.

After the result has been reviewed and approved for preservation:

```bash
git add "$CLASSIFICATION_INPUT" "$RUN_ROOT"
git diff --cached --check
git status --short
git commit -m 'Record future-life avowal diagnostic classification'
git push origin main
git status --short
```

Do not begin 8B until 8A has been reviewed.

## Substep 8B: comparative-care avowal

After 8A review is complete, prepare the final v0.1 input:

```bash
cd "$LMCW"
SOURCE_ID='gutenberg-1260'
CASE_NAME='comparative_care_avowal'
OCCURRENCE_ID='bronte-jane-eyre-b94304d3eea5'
PASSAGES_FILE="data/development/passages/$SOURCE_ID.jsonl"
CLASSIFICATION_INPUT="results/development_runs/classification_inputs/$OCCURRENCE_ID.json"
RUN_ROOT="results/development_runs/classification_diagnostics/$CASE_NAME"

test ! -e "$CLASSIFICATION_INPUT" || {
  echo "Refusing to overwrite existing input: $CLASSIFICATION_INPUT"
  exit 1
}
test ! -e "$RUN_ROOT" || {
  echo "Refusing to reuse existing run root: $RUN_ROOT"
  exit 1
}

python scripts/annotation/prepare_classification_input.py \
  "$PASSAGES_FILE" "$CLASSIFICATION_INPUT" \
  --occurrence-id "$OCCURRENCE_ID"
python -m json.tool "$CLASSIFICATION_INPUT"
```

Make one API call with the same unchanged artifacts:

```bash
test -n "${OPENAI_API_KEY:-}" || { echo 'OPENAI_API_KEY is not set'; exit 1; }
python scripts/api/call_responses.py \
  --model '5.6' \
  --prompt prompts/annotation/classify_passage_v0_1.md \
  --input "$CLASSIFICATION_INPUT" \
  --schema prompts/annotation/classification_schema_v0_1.json \
  --output-root "$RUN_ROOT"
```

Inspect and validate the result:

```bash
RUN_DIR="$(find "$RUN_ROOT" -mindepth 1 -maxdepth 1 -type d | sort | tail -1)"
test -n "$RUN_DIR" || { echo 'No run directory found'; exit 1; }
printf 'Run directory: %s\n' "$RUN_DIR"
python -m json.tool "$RUN_DIR/metadata.json"
python -m json.tool "$RUN_DIR/pricing_snapshot.json"
python -m json.tool "$RUN_DIR/cost.json"
python -m json.tool "$RUN_DIR/response.json" >/dev/null
python -m json.tool "$RUN_DIR/output.txt" >/dev/null
python scripts/annotation/validate_classification.py "$RUN_DIR/output.txt" \
  --expected-occurrence-id "$OCCURRENCE_ID"
sed -n '1,300p' "$RUN_DIR/output.txt"
```

### Review checkpoint for 8B

Stop and share complete `metadata.json`, `cost.json`, and `output.txt`. Review
whether the result treats “better now” as a comparison across circumstances,
distinguishes the asserted love from Jane's ability to be useful and care for
Rochester, and avoids inferring that caregiving either constitutes or exhausts
the core love-content.

After the result has been reviewed and approved for preservation:

```bash
git add "$CLASSIFICATION_INPUT" "$RUN_ROOT"
git diff --cached --check
git status --short
git commit -m 'Record comparative-care avowal diagnostic classification'
git push origin main
git status --short
```

Once 8B is preserved, stop. The next task is the six-case review in Phase B;
do not revise the v0.1 prompt or schema as part of this runbook.
