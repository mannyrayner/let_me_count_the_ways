# Annotate the full canonical KEEP set

This runbook starts only after the corrected calibration has passed. It never
changes extraction or membership decisions, and both API stages are resumable.
Stop if a count differs, validation fails, or either estimate exceeds USD 25.

## 1–2. Verify KEEP inventory and corrected calibration

```bash
set -e
python - <<'PY'
import json, pathlib
kept=pathlib.Path('results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/kept_candidates.jsonl')
rows=[json.loads(x) for x in kept.read_text(encoding='utf-8').splitlines() if x]
assert len(rows)==225 and len({r['candidate']['occurrence_id'] for r in rows})==225
assert all(r['review']['decision']=='KEEP' for r in rows)
summary=json.load(open('results/annotation/calibration_v2_v0_3_1/summary.json',encoding='utf-8'))
assert summary['requested']==summary['valid']==8 and summary['failed']==0
print('225 KEEP records; corrected calibration 8/8 valid')
PY
```

## 3–5. Estimate, run/resume, and validate translations

```bash
set -e
python scripts/annotation/generate_context_translations.py --reviewed results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/kept_candidates.jsonl --all-reviewed --output results/annotation/canonical_31_v0_11_translations_v1 --model 5.6 --estimate-only
python - <<'PY'
import json
x=json.load(open('results/annotation/canonical_31_v0_11_translations_v1/estimate.json'))
assert x['keep_cases']==225 and x['estimated_total_usd'] <= 25
PY
python scripts/annotation/generate_context_translations.py --reviewed results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/kept_candidates.jsonl --all-reviewed --output results/annotation/canonical_31_v0_11_translations_v1 --model 5.6
python - <<'PY'
import json
x=json.load(open('results/annotation/canonical_31_v0_11_translations_v1/summary.json'))
assert x['status']=='complete' and x['failed']==0
PY
```

If otherwise-valid translation calls fail only because of the default
300-second request timeout, rerun the same output directory with `--timeout
600`. Compatible successful artifacts resume automatically, so only unresolved
translations are retried. The ordinary full run should continue to use the
default timeout.

## 6–7. Build and validate all enriched records

```bash
set -e
python scripts/annotation/enrich_canonical_candidates.py --reviewed results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/kept_candidates.jsonl --generated results/annotation/canonical_31_v0_11_translations_v1/generated_enrichment.json --output results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_full_v1.jsonl
python - <<'PY'
import json
p='results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_full_v1.jsonl'
rows=[json.loads(x) for x in open(p,encoding='utf-8') if x.strip()]
assert len(rows)==225 and len({r['occurrence']['occurrence_id'] for r in rows})==225
assert all(r['review']['decision']=='KEEP' for r in rows)
assert all((r['translation'] is None) if r['work_metadata']['language']=='en' else (r['translation']['status']=='provided' and r['translation']['text']) for r in rows)
print('225 unique enriched KEEP records; translations complete')
PY
```

## 8–10. Estimate, run/resume, and inspect annotations

```bash
set -e
python scripts/annotation/annotate_canonical_candidates.py --enriched results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_full_v1.jsonl --all --output results/annotation/canonical_31_v0_11_v0_3_1 --estimate-only
python - <<'PY'
import json
x=json.load(open('results/annotation/canonical_31_v0_11_v0_3_1/estimate.json'))
assert x['total_candidates']==225 and x['estimated_total_usd'] <= 25
PY
python scripts/annotation/annotate_canonical_candidates.py --enriched results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_full_v1.jsonl --all --output results/annotation/canonical_31_v0_11_v0_3_1
python - <<'PY'
import json
x=json.load(open('results/annotation/canonical_31_v0_11_v0_3_1/summary.json'))
assert x['requested']==x['valid']==225 and x['failed']==0 and x['status']=='complete'
print(json.dumps(x['distributions'],indent=2))
print('review cases:',len(json.load(open('results/annotation/canonical_31_v0_11_v0_3_1/review_cases.json'))))
PY
```

If otherwise-valid annotation calls fail only because of the default
300-second request timeout, rerun the same enriched input and output directory
with `--timeout 600`. Compatible successful annotation artifacts resume
automatically, so only unresolved cases are retried. If exceptional cases still
time out, `--timeout 1200` may be used after confirming that the failures are
timeout-only.

## 11. Run tests

```bash
set -e
python -m pytest
python scripts/docs/validate_runbook_index.py
git diff --check
```

## 12–14. Explicit staging, commits, and final checks

Never use `git add .`. Stage only the named implementation files, commit them,
then explicitly stage only the four intended generated-result paths for the
second commit.

```bash
set -e
git add scripts/annotation/generate_context_translations.py scripts/annotation/annotate_canonical_candidates.py scripts/annotation/test_generate_context_translations.py scripts/annotation/test_canonical_annotation.py docs/howto/39_review_and_calibrate_canonical_annotation.md docs/howto/40_annotate_full_canonical_keep_set.md docs/howto/README.md
git commit -m "Generalize canonical translation and annotation runs"
git add results/annotation/calibration_v2_v0_3_1 results/annotation/canonical_31_v0_11_translations_v1 results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_full_v1.jsonl results/annotation/canonical_31_v0_11_v0_3_1
git commit -m "Annotate full canonical LOVE candidate set"
git status --short
git show --stat --oneline HEAD
git diff HEAD^ --check
```

Stop here for Manny/ChatGPT review; do not begin aggregate literary analysis.
