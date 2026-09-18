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

Before creating v2 inputs, estimate and then generate translations for the
non-English cases in the fixed calibration manifest. The runner deterministically
derives each wide context from the canonical corpus and makes no API request for
English cases. It requires `OPENAI_API_KEY` for generation (but not estimation).
Do not write or edit translations by hand.

```bash
set -e
python scripts/annotation/generate_context_translations.py \
  --reviewed results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/kept_candidates.jsonl \
  --calibration data/annotation/calibration_v1.json \
  --output results/annotation/calibration_v2_translations \
  --model 5.6 \
  --estimate-only
python scripts/annotation/generate_context_translations.py \
  --reviewed results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/kept_candidates.jsonl \
  --calibration data/annotation/calibration_v1.json \
  --output results/annotation/calibration_v2_translations \
  --model 5.6
```

Each successful API response is validated and stored in its own key-addressed
artifact beneath `translations/`. The resumption key contains occurrence ID,
wide-context source hash, resolved model, and prompt version. Compatible valid
artifacts skip the API; changed source, model, or prompt values cannot be
silently reused. `usage.json` records calls, token usage, and estimated cost,
and `generated_enrichment.json` is assembled for the enrichment stage. Create
the v2 inputs directly from that generated mapping:

```bash
set -e
python scripts/annotation/enrich_canonical_candidates.py --reviewed results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/kept_candidates.jsonl --generated results/annotation/calibration_v2_translations/generated_enrichment.json --output results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_v2.jsonl
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

**Stop after building and inspecting `enriched_v2.jsonl`. Do not launch the
T/P/E/O commands below until Manny/ChatGPT have inspected the generated
translation artifacts.** When that approval is given, estimate first, then run
only the fixed calibration manifest and render its summary (rendering occurs at
the end of the run). The old `enriched.jsonl` and
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
git add prompts/annotation/translate_context_v1.md prompts/annotation/translation_schema_v1.json scripts/annotation/generate_context_translations.py scripts/annotation/enrich_canonical_candidates.py scripts/annotation/test_canonical_annotation.py scripts/annotation/test_generate_context_translations.py docs/howto/39_review_and_calibrate_canonical_annotation.md results/annotation/calibration_v2_translations results/review/canonical_31_v0_11_ai_review_v1/kept_candidates/enriched_v2.jsonl
git commit -m "Restore API-generated canonical context translations"
git status --short
git show --stat --oneline HEAD
```

Stop here. Do not annotate the full KEEP set until humans inspect all outputs.
