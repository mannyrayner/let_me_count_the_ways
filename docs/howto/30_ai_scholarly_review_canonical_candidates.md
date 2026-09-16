# 30. Run the provisional AI scholarly review

This checkpoint creates a resumable **AI first pass, pending human review** of
the frozen v0.7 candidates. It decides only whether each candidate explicitly
realizes LOVE(first-person singular experiencer, second-person target). It does
not accept decisions, make a final KEEP set, retrieve wider context, translate,
or perform T/P/E/O annotation.

## 1. Tests and inputs

```bash
cd "$LMCW"
python -m pytest -q scripts/review/test_scholarly_candidate_review.py scripts/api/test_call_responses.py
python scripts/docs/validate_runbook_index.py
test "$(find results/extraction/canonical_16_v0_7/works -name candidates.jsonl -print0 | xargs -0 cat | wc -l)" -eq 118
test -f results/extraction_private/canonical_16_v0_7/works/mcmillan-error-of-understanding/candidates.jsonl
git diff --exit-code -- results/extraction/canonical_16_v0_7
```

The last path is local-only. If it is absent, stop: the authorized machine must
run Runbook 29 first. Never substitute invented records or review quotations
from an unauthorized copy.

## 2. Public review run (and resumption)

```bash
test -n "$OPENAI_API_KEY"
PUBLIC_INPUT=results/extraction/canonical_16_v0_7
PUBLIC_REVIEW=results/review/canonical_16_v0_7_ai_review_v1
python scripts/review/scholarly_candidate_review.py run \
  --candidates "$PUBLIC_INPUT" --output "$PUBLIC_REVIEW" --model 5.6
```

Run the identical command to resume after interruption. A record keyed by
occurrence ID, exact model, and prompt version is skipped; an incompatible
existing record causes a stop rather than a silent overwrite. Temperature is
not sent because `gpt-5.6-sol` does not support the `temperature` request
parameter; the manifest and usage report record that omission explicitly.
Per-run usage and estimated cost use `config/api_models.json`.

## 3. Private McMillan review (and resumption)

```bash
PRIVATE_INPUT=results/extraction_private/canonical_16_v0_7
PRIVATE_REVIEW=results/review_private/canonical_16_v0_7_ai_review_v1
git check-ignore -v "$PRIVATE_INPUT" "$PRIVATE_REVIEW"
python scripts/review/scholarly_candidate_review.py run \
  --candidates "$PRIVATE_INPUT" --output "$PRIVATE_REVIEW" --model 5.6
```

The private records contain decisions and identifiers but no copied context;
the private inspection sheet below does contain context and must remain ignored.
The rights state remains `LIMITED_QUOTATION_ONLY`, `REVIEW_REQUIRED`, and
`AUTHOR_APPROVAL_FOR_PUBLICATION_EXCERPTS`. KEEP never grants publication
permission.

## 4. Validate exactly 125 records

```bash
python scripts/review/scholarly_candidate_review.py validate \
  --candidates "$PUBLIC_INPUT" --candidates "$PRIVATE_INPUT" \
  --review "$PUBLIC_REVIEW" --review "$PRIVATE_REVIEW" --expected-total 125
```

Validation requires exact one-to-one coverage, rejects unknown and duplicate
IDs, checks work IDs, allowed decisions/reasons, decision/reason compatibility,
confidence range, and prompt version.

## 5. Summaries and human inspection files

Create the public sheet (which always suppresses private candidate text) and a
separate ignored private sheet:

```bash
python scripts/review/scholarly_candidate_review.py render \
  --candidates "$PUBLIC_INPUT" --candidates "$PRIVATE_INPUT" \
  --review "$PUBLIC_REVIEW" --review "$PRIVATE_REVIEW" --output "$PUBLIC_REVIEW"
python scripts/review/scholarly_candidate_review.py render \
  --candidates "$PRIVATE_INPUT" --review "$PRIVATE_REVIEW" \
  --output "$PRIVATE_REVIEW" --include-private-in-sheet
```

`summary.json` and `summary.md` report raw/KEEP/EXCLUDE/UNCERTAIN counts per
work and exclusion reasons. `human_inspection.tsv` sorts UNCERTAIN, EXCLUDE,
low-confidence KEEP, then high-confidence KEEP. Inspect all UNCERTAIN and
EXCLUDE rows and low-confidence KEEP rows. Specifically confirm Nora's
negative, Rank's perfect, and Lawrence's metalinguistic formula are KEEP, and
that any Dumas *aimer mieux* “prefer” match is
`EXCLUDE_NOT_LOVE_SENSE`.

Report cost without exposing text:

```bash
cat "$PUBLIC_REVIEW/usage.json"
cat "$PRIVATE_REVIEW/usage.json"
```

Combine the two usage files when recording the public manifest totals: public
and private candidate counts, total candidates, input/output tokens, total
estimated USD cost, model, prompt version, and relevant generation settings.
The public
McMillan entry may contain counts and provenance only—not match, context, note,
request, response, or other quotation-bearing data.

## 6. Public/private safety and explicit staging

```bash
git status --short
git diff --cached --name-only
git check-ignore -v "$PRIVATE_REVIEW" "$PRIVATE_INPUT"
test -z "$(git status --short --untracked-files=all | rg 'review_private|extraction_private|local_candidate' || true)"
git diff --check
git add \
  .gitignore \
  prompts/review/scholarly_candidate_review_v1.md \
  prompts/review/scholarly_candidate_review_schema_v1.json \
  scripts/review/scholarly_candidate_review.py \
  scripts/review/test_scholarly_candidate_review.py \
  results/review/canonical_16_v0_7_ai_review_v1 \
  docs/howto/30_ai_scholarly_review_canonical_candidates.md \
  docs/howto/README.md
git diff --cached --name-only
test -z "$(git diff --cached --name-only | rg 'review_private|extraction_private|local_candidate|mcmillan.*/review|\.epub$' || true)"
git diff --cached --check
git commit -m "Add provisional AI scholarly review of extracted candidates"
```

Never use `git add .`. After the commit, stop for Manny's inspection. Do not
apply human decisions or begin contextual annotation.
