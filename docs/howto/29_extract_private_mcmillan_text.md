# 29. Extract the private McMillan text locally

This checkpoint completes the deterministic v0.7 candidate extraction for
Stella McMillan's *Error of Understanding* on an authorized machine. The full
text and all context-bearing candidates remain local and Git-ignored. Only
non-quoting counts and status are written to the public extraction summary.

Do not use a model, change the pattern set, or make scholarly KEEP/EXCLUDE or
T/P/E/O judgments during this procedure.

## 1. Verify the private source and canonical hash

Enter the checkout, require the configured private source, and stop unless its
bytes match the canonical manifest:

```bash
cd "$LMCW"
PRIVATE_TEXT=data/local_candidate_derived/mcmillan-error-of-understanding/text.txt
EXPECTED_SHA256=b941746d22087c6cfc9e9634880d0f950db8017de786077c37fdfc643f880839
test -f "$PRIVATE_TEXT" || {
  printf 'Missing private canonical source: %s\n' "$PRIVATE_TEXT" >&2
  exit 1
}
ACTUAL_SHA256=$(sha256sum "$PRIVATE_TEXT" | awk '{print $1}')
printf '%s  %s\n' "$ACTUAL_SHA256" "$PRIVATE_TEXT"
test "$ACTUAL_SHA256" = "$EXPECTED_SHA256" || {
  printf 'Canonical hash mismatch; stop without extracting.\n' >&2
  exit 1
}
```

The canonical rights state remains `REVIEW_REQUIRED`, with
`AUTHOR_APPROVAL_FOR_PUBLICATION_EXCERPTS`. Extraction does not change it.

## 2. Verify the private output is ignored

Use the extractor's existing private-results convention and confirm Git ignores
both the source and destination before writing candidates:

```bash
PRIVATE_WORK=results/extraction_private/canonical_16_v0_7/works/mcmillan-error-of-understanding
PRIVATE_CANDIDATES="$PRIVATE_WORK/candidates.jsonl"
git check-ignore -v "$PRIVATE_TEXT"
git check-ignore -v "$PRIVATE_CANDIDATES"
test ! -e results/extraction/canonical_16_v0_7/works/mcmillan-error-of-understanding/candidates.jsonl
```

Stop if either `git check-ignore` command fails. Do not add an exception that
re-includes either private path.

## 3. Run the canonical v0.7 extractor

The canonical runner currently processes all manifests. Its deterministic
public files may be rewritten with identical content, while the McMillan
context-bearing artifact is routed only to `results/extraction_private/`:

```bash
python scripts/extraction/extract_canonical_corpus.py \
  --patterns data/development/search_patterns_v0_7.json \
  --output results/extraction/canonical_16_v0_7 \
  --private-output results/extraction_private/canonical_16_v0_7
test -f "$PRIVATE_CANDIDATES"
test ! -e results/extraction/canonical_16_v0_7/works/mcmillan-error-of-understanding/candidates.jsonl
```

The runner automatically updates the public per-work and aggregate summaries
with candidate, pattern, and form-family counts; it does not put matched strings
or contexts in those summaries. Preserve a private copy of the non-quoting
per-work summary beside the candidates for convenient local provenance:

```bash
cp results/extraction/canonical_16_v0_7/works/mcmillan-error-of-understanding/summary.json \
  "$PRIVATE_WORK/summary.json"
```

## 4. Inspect counts without printing private text

Print only the requested inventory counts, not matches or contexts:

```bash
python - <<'PY'
import json
from collections import Counter
from pathlib import Path

path = Path("results/extraction_private/canonical_16_v0_7/works/mcmillan-error-of-understanding/candidates.jsonl")
records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
assert all(record["work_id"] == "mcmillan-error-of-understanding" for record in records)
print("work_id:", "mcmillan-error-of-understanding")
print("candidate_count:", len(records))
print("counts_by_form_family:", dict(sorted(Counter(record.get("form_family", "unspecified") for record in records).items())))
print("counts_by_pattern_id:", dict(sorted(Counter(record["pattern_id"] for record in records).items())))
PY
```

For authorized local inspection of complete records, use:

```bash
less "$PRIVATE_CANDIDATES"
```

Do not paste its output into an issue, pull request, terminal transcript, or
other public artifact.

## 5. Verify the public summary and separation

Confirm the public summary reports an extracted private artifact, contains the
canonical hash, and agrees with the private inventory count:

```bash
python - <<'PY'
import json
from pathlib import Path

public = Path("results/extraction/canonical_16_v0_7")
private = Path("results/extraction_private/canonical_16_v0_7/works/mcmillan-error-of-understanding/candidates.jsonl")
summary = json.loads((public / "summary.json").read_text(encoding="utf-8"))
work = next(item for item in summary["works"] if item["work_id"] == "mcmillan-error-of-understanding")
private_count = sum(1 for line in private.open(encoding="utf-8") if line.strip())
assert work["status"] == "extracted"
assert work["candidate_artifact"] == "private_local"
assert work["private_output_available"] is True
assert work["candidate_count"] == private_count
assert work["canonical_sha256"] == "b941746d22087c6cfc9e9634880d0f950db8017de786077c37fdfc643f880839"
assert work["public_render_policy"] == "LIMITED_QUOTATION_ONLY"
assert work["analysis_allowed"] is True
print({key: work[key] for key in (
    "work_id", "language", "candidate_count", "counts_by_form_family",
    "counts_by_pattern", "canonical_sha256", "candidate_artifact",
)})
PY
test ! -e results/extraction/canonical_16_v0_7/works/mcmillan-error-of-understanding/candidates.jsonl
git check-ignore -v "$PRIVATE_CANDIDATES" "$PRIVATE_WORK/summary.json" "$PRIVATE_TEXT"
git status --short
git diff --cached --name-only
test -z "$(git diff --cached --name-only | rg 'local_candidate|extraction_private|mcmillan.*/candidates|\.epub$' || true)"
```

Review public diffs without printing the private candidate file:

```bash
git diff -- \
  results/extraction/canonical_16_v0_7/summary.json \
  results/extraction/canonical_16_v0_7/summary.md \
  results/extraction/canonical_16_v0_7/works/mcmillan-error-of-understanding/summary.json
```

## 6. Run tests

No command in this checkpoint makes a model call:

```bash
python -m pytest -q scripts/extraction
python -m pytest -q scripts/corpus/test_canonical_corpus.py
python scripts/docs/validate_runbook_index.py
git diff --check
```

Stop and diagnose any failure before staging.

## 7. Stage public-safe files explicitly

Never use `git add .`. Stage only the public non-quoting summaries and runbook
documentation:

```bash
git status --short
git add \
  results/extraction/canonical_16_v0_7/summary.json \
  results/extraction/canonical_16_v0_7/summary.md \
  results/extraction/canonical_16_v0_7/works/mcmillan-error-of-understanding/summary.json \
  docs/howto/29_extract_private_mcmillan_text.md \
  docs/howto/README.md
git diff --cached --name-only
test -z "$(git diff --cached --name-only | rg 'local_candidate|extraction_private|mcmillan.*/candidates|\.epub$' || true)"
git diff --cached --check
```

The staged list must contain no purchased EPUB, private full text, candidate
JSONL, matched string, or context-bearing artifact.

## 8. Commit

```bash
git commit -m "Record private McMillan extraction summary"
```

## 9. Verify after the commit

```bash
git status --short
git show --stat --oneline --decorate HEAD
git show --format= --name-only HEAD
test -z "$(git show --format= --name-only HEAD | rg 'local_candidate|extraction_private|mcmillan.*/candidates|\.epub$' || true)"
test -f "$PRIVATE_CANDIDATES"
git check-ignore -v "$PRIVATE_CANDIDATES" "$PRIVATE_WORK/summary.json" "$PRIVATE_TEXT"
python scripts/docs/validate_runbook_index.py
```

Stop here. Manny and ChatGPT should inspect the complete 16-work candidate
inventory before deciding whether v0.7 is ready to freeze for scholarly review.
