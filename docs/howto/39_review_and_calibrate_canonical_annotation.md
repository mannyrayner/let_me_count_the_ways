# Review v0.11 candidates and calibrate canonical annotation

This step treats `results/extraction/canonical_31_v0_11/` and
`data/development/search_patterns_v0_11.json` as immutable. It reviews every
publicly renderable candidate from scratch, freezes only KEEP records, enriches
canonical offsets, and annotates only the eight explicitly named calibration
cases. Public enrichment includes both public-domain works and works whose
permissions allow public context, such as `PERMISSIONED_CONTEXT_OK`.

```bash
set -e
cd "$LMCW"
python - <<'PY'
import json, pathlib
root=pathlib.Path('results/extraction/canonical_31_v0_11')
rows=[json.loads(line) for p in root.glob('works/*/candidates.jsonl') for line in p.read_text(encoding='utf-8').splitlines() if line]
assert len(rows)==227 and len({r['occurrence_id'] for r in rows})==227
assert json.loads((root/'summary.json').read_text())['total_candidates']==227
print('valid frozen extraction: 227 unique public candidates')
PY
```

Run, validate, render, and freeze the uniform membership review (the first
command resumes by occurrence/model/prompt and requires `OPENAI_API_KEY`):

```bash
set -e
python scripts/review/scholarly_candidate_review.py run --candidates results/extraction/canonical_31_v0_11 --output results/review/canonical_31_v0_11_ai_review_v1 --model 5.6
python scripts/review/scholarly_candidate_review.py validate --candidates results/extraction/canonical_31_v0_11 --review results/review/canonical_31_v0_11_ai_review_v1 --expected-total 227
python scripts/review/scholarly_candidate_review.py render --candidates results/extraction/canonical_31_v0_11 --review results/review/canonical_31_v0_11_ai_review_v1 --output results/review/canonical_31_v0_11_ai_review_v1
python scripts/review/scholarly_candidate_review.py freeze --candidates results/extraction/canonical_31_v0_11 --review results/review/canonical_31_v0_11_ai_review_v1 --output results/review/canonical_31_v0_11_ai_review_v1/kept_candidates
```

Before creating v2 inputs, create the enrichment template below. The file is a
curated, run-specific artifact, so it is intentionally not supplied by the
repository. The command refuses to overwrite an existing file and limits the
template to non-English cases in the fixed calibration manifest.

```bash
set -e
python - <<'PY'
import json
from pathlib import Path
from scripts.annotation.enrich_canonical_candidates import enrich, read_jsonl

reviewed = Path('results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/kept_candidates.jsonl')
manifest = json.loads(Path('data/annotation/calibration_v1.json').read_text(encoding='utf-8'))
output = Path('data/annotation/calibration_v2_enrichment.json')
if output.exists():
    raise SystemExit(f'refusing to overwrite existing enrichment: {output}')
rows = {row.get('candidate', row.get('occurrence', row))['occurrence_id']: row
        for row in read_jsonl(reviewed)}
generated = {}
for case in manifest['cases']:
    occurrence_id = case['occurrence_id']
    if occurrence_id not in rows:
        raise SystemExit(f'calibration case is not in frozen KEEP set: {occurrence_id}')
    enriched = enrich(rows[occurrence_id], Path('corpus'))
    if enriched['work_metadata']['language'] != 'en':
        generated[occurrence_id] = {'translation': enriched['translation']}
output.write_text(json.dumps(generated, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'wrote {len(generated)} translation templates to {output}')
PY
```

The `wrote 4 translation templates` message means only that four blank forms
were created; it is **not** a successful enrichment result. **Stop at this
point. Do not run the next code block until all four translations have been
manually completed.** A newly generated template intentionally contains
`"status": "required"` and `"text": null` for every entry.

Edit each translation in `data/annotation/calibration_v2_enrichment.json`: set
`status` to `provided` and replace the null `text` with an English translation
of the entire wide context. Preserve `source_occurrence_id`,
`source_language_text_sha256`, `scope`, and `notice`, which bind the translation
to its source context. Then validate the curated artifact and create v2 inputs:

```bash
set -e
python - <<'PY'
import json
from pathlib import Path
from scripts.annotation.enrich_canonical_candidates import enrich, read_jsonl

p = Path('data/annotation/calibration_v2_enrichment.json')
generated = json.loads(p.read_text(encoding='utf-8'))
manifest = json.loads(Path('data/annotation/calibration_v1.json').read_text(encoding='utf-8'))
reviewed = Path('results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/kept_candidates.jsonl')
rows = {row.get('candidate', row.get('occurrence', row))['occurrence_id']: row
        for row in read_jsonl(reviewed)}
expected = {case['occurrence_id'] for case in manifest['cases']
            if enrich(rows[case['occurrence_id']], Path('corpus'))['work_metadata']['language'] != 'en'}
if set(generated) != expected:
    raise SystemExit(f'enrichment IDs differ: expected {sorted(expected)}, got {sorted(generated)}')
incomplete = [occurrence_id for occurrence_id, item in generated.items()
              if item.get('translation', {}).get('status') != 'provided'
              or not item.get('translation', {}).get('text')]
if incomplete:
    raise SystemExit('incomplete translations: ' + ', '.join(incomplete))
print(f'valid curated enrichment: {len(generated)} completed translations')
PY
python scripts/annotation/enrich_canonical_candidates.py --reviewed results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/kept_candidates.jsonl --generated data/annotation/calibration_v2_enrichment.json --output results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_v2.jsonl
python - <<'PY'
import json
p='results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_v2.jsonl'
rows=[json.loads(x) for x in open(p,encoding='utf-8')]
for language in ('en','no'): print(next(r for r in rows if r['work_metadata']['language']==language))
PY
```

Translations are mandatory for non-English calibration records: annotation
stops if an enrichment still has `translation.status == "required"` and null
`translation.text`. The enrichment CLI also refuses a supplied generated file
containing an incomplete translation, so disabling the shell's `set -e` cannot
silently produce an unusable `enriched_v2.jsonl`. Narrative-context summaries
are optional calibration aids; their absence is represented explicitly as
null.

Estimate first, then run only the fixed calibration manifest and render its
summary (rendering occurs at the end of the run). The old `enriched.jsonl` and
`results/annotation/calibration_v1_v0_3_1` remain historical pre-full-enrichment
artifacts; do not overwrite or delete them. The corrected run uses the new v2
paths:

```bash
set -e
python scripts/annotation/annotate_canonical_candidates.py --enriched results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_v2.jsonl --calibration data/annotation/calibration_v1.json --output results/annotation/calibration_v2_v0_3_1 --estimate-only
python scripts/annotation/annotate_canonical_candidates.py --enriched results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_v2.jsonl --calibration data/annotation/calibration_v1.json --output results/annotation/calibration_v2_v0_3_1
cat results/annotation/calibration_v2_v0_3_1/summary.md
```

Run checks, explicitly stage only intended paths, commit, and check the commit:

```bash
set -e
python -m pytest
python scripts/docs/validate_runbook_index.py
git diff --check
git status --short
git add scripts/review/scholarly_candidate_review.py scripts/review/test_scholarly_candidate_review.py scripts/annotation/contracts.py scripts/annotation/enrich_canonical_candidates.py scripts/annotation/annotate_canonical_candidates.py scripts/annotation/test_canonical_annotation.py scripts/docs/test_howto_inventory.py data/annotation/calibration_v1.json data/annotation/calibration_v2_enrichment.json docs/howto/39_review_and_calibrate_canonical_annotation.md docs/howto/README.md results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_v2.jsonl results/annotation/calibration_v2_v0_3_1
git commit -m "Review canonical candidates and calibrate annotation"
git status --short
git show --stat --oneline HEAD
```

Stop here. Do not annotate the full KEEP set until humans inspect all outputs.
