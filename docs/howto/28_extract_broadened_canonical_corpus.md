# 28. Extract the broadened canonical corpus

This deterministic checkpoint searches all canonical work manifests for explicit
lexical `LOVE(I,YOU)` candidates. It neither calls a model nor makes scholarly
KEEP/EXCLUDE judgments. Character offsets address the decoded canonical text
without Unicode normalization. Candidate IDs hash the work ID, canonical hash,
span, matched surface, and pattern version.

## 1. Enter the checkout and run focused tests

```bash
cd "$LMCW"
python -m unittest scripts.extraction.test_extract_canonical_corpus -v
python scripts/docs/validate_runbook_index.py
```

## 2. Run all 16 manifests

```bash
python scripts/extraction/extract_canonical_corpus.py
```

A missing local/private source produces a clear warning and an `unavailable`
summary rather than making an ordinary public clone fail. On the authorized
research machine, the hash-verified private source produces its context-bearing
inventory only below ignored `results/extraction_private/`.

## 3. Validate and inspect public outputs

```bash
python -m json.tool results/extraction/canonical_16_v0_7/manifest.json >/dev/null
python -m json.tool results/extraction/canonical_16_v0_7/summary.json >/dev/null
cat results/extraction/canonical_16_v0_7/summary.md
python - <<'PY'
import json
from pathlib import Path
root = Path("results/extraction/canonical_16_v0_7")
summary = json.loads((root / "summary.json").read_text(encoding="utf-8"))
assert summary["works_attempted"] == 16
assert all(summary["known_case_assertions"].values())
for work in summary["works"]:
    print(work["work_id"], work["candidate_count"], work["candidate_artifact"])
PY
```

The mechanical assertions cover Nora's negative cessation, Rank's formal
perfect, and Lawrence's surface `I love you` formula. Inspect examples without
assigning scholarly status:

```bash
rg -n 'Jeg elsker deg|jeg har elsket Dem' \
  results/extraction/canonical_16_v0_7/works/ibsen-et-dukkehjem/candidates.jsonl
rg -n 'I love you' \
  results/extraction/canonical_16_v0_7/works/lawrence-women-in-love/candidates.jsonl
```

## 4. Verify private/public separation

The public McMillan summary contains counts and status only—never matches or
contexts. If the private source is available, inspect its inventory locally:

```bash
python -m json.tool \
  results/extraction/canonical_16_v0_7/works/mcmillan-error-of-understanding/summary.json
test ! -e results/extraction/canonical_16_v0_7/works/mcmillan-error-of-understanding/candidates.jsonl
git check-ignore results/extraction_private/canonical_16_v0_7/works/mcmillan-error-of-understanding/candidates.jsonl
git status --short --ignored | rg 'extraction_private|mcmillan' || true
```

## 5. Stage public-safe files explicitly

Never use `git add .`. Review status, then name only the intended public paths:

```bash
git status --short
git add .gitignore \
  data/development/search_patterns_v0_7.json \
  scripts/extraction/extract_canonical_corpus.py \
  scripts/extraction/test_extract_canonical_corpus.py \
  docs/howto/28_extract_broadened_canonical_corpus.md \
  docs/howto/README.md \
  results/extraction/canonical_16_v0_7
git diff --cached --name-only
test -z "$(git diff --cached --name-only | rg 'results/extraction_private|mcmillan.*/candidates' || true)"
git diff --cached --check
git commit -m "Extract broadened LOVE candidates from canonical corpus"
```

Stop here. Manny and ChatGPT should inspect recall, obvious false positives,
language gaps, and pattern-family distributions before scholarly review.
