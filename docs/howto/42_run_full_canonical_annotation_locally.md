# Run the full canonical annotation locally

This step is **local-only**. Manny runs the paid 225-case annotation in an
interactive terminal so that progress remains visible. Do not run the batch in
an automated coding-agent environment, and do not add a partially generated
result tree to a patch. The runner is resumable: let each pass finish, preserve
valid results, and retry only unresolved timeouts.

The fixed input and output paths are:

```text
results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_full_v1.jsonl
results/annotation/canonical_31_v0_11_v0_3_1/
```

Do not use `set -e` for the annotation passes. An isolated request failure must
not stop the runner from completing the remaining cases.

## 1. Final preflight

Run this in the local checkout:

```bash
python - <<'PY'
import json
from pathlib import Path

enriched = Path(
    'results/review/canonical_31_v0_11_ai_review_v1/'
    'kept_candidates/enriched_full_v1.jsonl'
)
rows = [
    json.loads(line)
    for line in enriched.read_text(encoding='utf-8').splitlines()
    if line.strip()
]

assert len(rows) == 225
assert len({r['occurrence']['occurrence_id'] for r in rows}) == 225
assert all(r['review']['decision'] == 'KEEP' for r in rows)

english = [r for r in rows if r['work_metadata']['language'] == 'en']
non_english = [r for r in rows if r['work_metadata']['language'] != 'en']
assert len(english) == 54
assert len(non_english) == 171
assert all(r['translation'] is None for r in english)
assert all(
    r['translation']
    and r['translation']['status'] == 'provided'
    and r['translation']['text']
    for r in non_english
)

estimate = json.load(open(
    'results/annotation/canonical_31_v0_11_v0_3_1/estimate.json',
    encoding='utf-8',
))
assert estimate['total_candidates'] == 225
assert estimate['api_calls_needed'] == 225
assert estimate['estimated_total_usd'] <= 25

print('preflight valid:')
print('  225 KEEP records')
print('  54 English')
print('  171 translated non-English')
print(f"  estimated annotation cost: USD {estimate['estimated_total_usd']:.2f}")
PY
```

Stop without launching annotation if any assertion fails. The expected estimate
is approximately USD 11.99.

## 2. Complete the annotation passes

Start the first pass with the default 300-second timeout:

```bash
python scripts/annotation/annotate_canonical_candidates.py \
  --enriched results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_full_v1.jsonl \
  --all \
  --output results/annotation/canonical_31_v0_11_v0_3_1 \
  --model 5.6
```

The startup line should report 225 candidates, zero existing valid results, and
225 API calls needed. Let the entire pass finish even if individual calls fail.
Then inspect all three run summaries:

```bash
cat results/annotation/canonical_31_v0_11_v0_3_1/summary.json
cat results/annotation/canonical_31_v0_11_v0_3_1/failures.json
cat results/annotation/canonical_31_v0_11_v0_3_1/usage.json
```

Classify every failure before retrying. Stop for diagnosis if any failure is a
schema or validation failure, JSON parse failure, missing translation,
source/provenance failure, rights failure, or unexpected API error. Never hide
a substantive failure by increasing the timeout.

If and only if every unresolved failure is a transport/request timeout, rerun
the same input and output directory at 600 seconds:

```bash
python scripts/annotation/annotate_canonical_candidates.py \
  --enriched results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_full_v1.jsonl \
  --all \
  --output results/annotation/canonical_31_v0_11_v0_3_1 \
  --model 5.6 \
  --timeout 600
```

Confirm from the startup line that existing valid results are resumed and only
unresolved cases make API calls. If this pass still leaves timeout-only
failures, make one final selective retry at 1200 seconds:

```bash
python scripts/annotation/annotate_canonical_candidates.py \
  --enriched results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_full_v1.jsonl \
  --all \
  --output results/annotation/canonical_31_v0_11_v0_3_1 \
  --model 5.6 \
  --timeout 1200
```

## 3. Verify the completed result mechanically

```bash
python - <<'PY'
import json

root = 'results/annotation/canonical_31_v0_11_v0_3_1'
summary = json.load(open(f'{root}/summary.json', encoding='utf-8'))
failures = json.load(open(f'{root}/failures.json', encoding='utf-8'))
assert summary['status'] == 'complete'
assert summary['requested'] == 225
assert summary['valid'] == 225
assert summary['failed'] == 0
assert failures == []
print('full annotation complete: 225/225 valid, 0 failures')
print(json.dumps(summary['distributions'], indent=2))

cases = json.load(open(f'{root}/review_cases.json', encoding='utf-8'))
print('priority review cases:', len(cases))
PY
```

Printing the distributions and priority-review count is a mechanical check
only. Do not interpret or adjudicate the results in this step.

## 4. Test and commit only the completed result tree

```bash
python -m pytest
python scripts/docs/validate_runbook_index.py
git diff --check
git status --short
```

Stop before committing if any check fails. Inspect the status and do not stage
unrelated files, including `data/annotation/calibration_v2_enrichment.json` if
it exists locally. Stage and commit only the full annotation output:

```bash
git add results/annotation/canonical_31_v0_11_v0_3_1
git commit -m "Annotate full canonical LOVE candidate set"
```

Synchronize without guessing at conflict resolution:

```bash
git fetch origin
git rebase origin/main
git push origin main
git status --short
git show --stat --oneline HEAD
```

If the rebase conflicts, stop. Report any remaining untracked files separately.

## 5. Review checkpoint

Report requested, valid, and failed counts; the number resumed and called on the
final pass; the outcome of each timeout tier; the priority-review count; test
status; and repository push/cleanliness status. The main outputs for the next
phase are:

```text
results/annotation/canonical_31_v0_11_v0_3_1/summary.json
results/annotation/canonical_31_v0_11_v0_3_1/review_cases.json
```

Stop after 225/225 valid annotations, zero unresolved failures, passing tests,
and committed/pushed results. Do not begin aggregate literary interpretation,
language or work comparison, ontology revision, paper drafting, or human
adjudication.
