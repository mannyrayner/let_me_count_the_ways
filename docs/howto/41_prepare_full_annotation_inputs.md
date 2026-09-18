# Prepare full annotation inputs locally

This runbook prepares and estimates the full canonical annotation batch after
translation has completed. It is local-only: **do not make annotation API
calls**. If any assertion or command fails, stop and report the failure; do not
silently repair an artifact or continue to annotation.

## 1–2. Verify the completed translation stage

From the repository root, run this exact local check. It verifies both the
translation summary and all 171 generated non-English translations.

```bash
python - <<'PY'
import json

summary = json.load(open(
    'results/annotation/canonical_31_v0_11_translations_v1/summary.json',
    encoding='utf-8'
))

assert summary['status'] == 'complete'
assert summary['selected_cases'] == 225
assert summary['translations'] == 171
assert summary['failed'] == 0
assert summary['unresolved_occurrences'] == []

generated = json.load(open(
    'results/annotation/canonical_31_v0_11_translations_v1/generated_enrichment.json',
    encoding='utf-8'
))

assert len(generated) == 171

for oid, item in generated.items():
    tr = item['translation']
    assert tr['status'] == 'provided'
    assert tr['text']
    assert tr['source_occurrence_id'] == oid
    assert tr['scope'] == 'wide_context'
    assert tr['source_language_text_sha256']
    assert tr['prompt_version'] == 'translate_context_v1'

print('translation stage valid: 171/171 complete')
PY
```

## 3. Build the full enriched dataset

```bash
python scripts/annotation/enrich_canonical_candidates.py \
  --reviewed results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/kept_candidates.jsonl \
  --generated results/annotation/canonical_31_v0_11_translations_v1/generated_enrichment.json \
  --output results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_full_v1.jsonl
```

Expected output:

```text
enriched 225 reviewed canonical candidates
```

## 4. Validate all enriched records

This check rejects count, identity, review, language, translation, and source
hash discrepancies. It does not alter the dataset.

```bash
python - <<'PY'
import hashlib
import json

path = 'results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_full_v1.jsonl'
with open(path, encoding='utf-8') as stream:
    rows = [json.loads(line) for line in stream if line.strip()]

assert len(rows) == 225
occurrence_ids = [row['occurrence']['occurrence_id'] for row in rows]
assert len(set(occurrence_ids)) == 225
assert all(row['review']['decision'] == 'KEEP' for row in rows)

english = [row for row in rows if row['work_metadata']['language'] == 'en']
non_english = [row for row in rows if row['work_metadata']['language'] != 'en']
assert len(english) == 54
assert len(non_english) == 171

for row in english:
    assert row['translation'] is None

for row in non_english:
    occurrence_id = row['occurrence']['occurrence_id']
    translation = row['translation']
    assert translation['status'] == 'provided'
    assert translation['text']
    assert translation['scope'] == 'wide_context'
    assert translation['source_occurrence_id'] == occurrence_id
    source_hash = hashlib.sha256(
        row['context']['wide']['text'].encode('utf-8')
    ).hexdigest()
    assert source_hash == translation['source_language_text_sha256']

print('225 unique enriched KEEP records validated:')
print('54 English, 171 translated non-English, 0 failures')
PY
```

If any assertion fails, **STOP** and report it.

## 5. Inspect a multilingual sample

This inspection prints existing content only; it does not generate anything.
It selects the first record in each requested language.

```bash
python - <<'PY'
import json

path = 'results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_full_v1.jsonl'
with open(path, encoding='utf-8') as stream:
    rows = [json.loads(line) for line in stream if line.strip()]

for language in ('en', 'fr', 'de', 'it', 'no'):
    row = next(row for row in rows if row['work_metadata']['language'] == language)
    occurrence = row['occurrence']
    translation = row['translation']
    print('\n' + '=' * 72)
    print('occurrence_id:', occurrence['occurrence_id'])
    print('work_id:', occurrence['work_id'])
    print('language:', language)
    print('exact match:', occurrence['match'])
    print('wide source context:', row['context']['wide']['text'][:500])
    print('translation status:', None if translation is None else translation['status'])
    print('translation text:', None if translation is None else translation['text'][:500])
PY
```

Inspect all five examples before continuing.

## 6–7. Estimate annotation cost and validate the estimate

Run the estimator only:

```bash
python scripts/annotation/annotate_canonical_candidates.py \
  --enriched results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_full_v1.jsonl \
  --all \
  --output results/annotation/canonical_31_v0_11_v0_3_1 \
  --model 5.6 \
  --estimate-only
```

**This command must not call the API.** Validate its output locally:

```bash
python - <<'PY'
import json

x = json.load(open(
    'results/annotation/canonical_31_v0_11_v0_3_1/estimate.json',
    encoding='utf-8'
))

assert x['total_candidates'] == 225
assert x['estimated_total_usd'] <= 25

print(json.dumps(x, indent=2))
PY
```

If `total_candidates != 225` or `estimated_total_usd > 25`, **STOP**. Do not
run annotation.

## 8. Run local checks after preparation

Run these interactively without `set -e`, so every result remains visible:

```bash
python -m pytest
python scripts/docs/validate_runbook_index.py
git diff --check
```

## 9. Optional local checkpoint

This checkpoint is optional. First inspect the worktree:

```bash
git status --short
```

Stage only the deterministic enriched dataset and estimate:

```bash
git add \
  results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_full_v1.jsonl \
  results/annotation/canonical_31_v0_11_v0_3_1/estimate.json
```

Do **not** stage `data/annotation/calibration_v2_enrichment.json`. Then create
and publish the checkpoint:

```bash
git commit -m "Prepare full canonical annotation inputs"
git fetch origin
git rebase origin/main
git push origin main
```

If the rebase conflicts, **STOP**.

## 10. Stop condition

Stop after all of the following are true:

- translation stage validated;
- `enriched_full_v1.jsonl` created locally;
- 225 enriched records validated;
- annotation estimate generated;
- estimate validated; and
- tests pass.

**STOP.** Do not run annotation. The full annotation command belongs in the
subsequent handoff, after Manny and ChatGPT inspect the estimate.
