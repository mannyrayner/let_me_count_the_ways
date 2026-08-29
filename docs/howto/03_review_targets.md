# Step 3: stage, review, and approve targets

The Step 2 output is structurally valid and contains 40 candidates. It is still a
proposal, not an acquisition manifest: every edition, URL, rights claim, language
label, and likely phrase occurrence requires human review.

## Stage an editable review copy

Copy the model output—not `response.json`, which is the API envelope—into a
versioned working file. These commands preserve the original run and confirm that
the initial working copy is byte-for-byte identical:

```bash
cd "$LMCW"
RUN_DIR="$(find results/development_runs/target_discovery -mindepth 1 \
  -maxdepth 1 -type d | sort | tail -1)"
REVIEW_JSON='data/development/target_candidates_review_v0_1.json'
python -m json.tool "$RUN_DIR/output.txt" >/dev/null
cp "$RUN_DIR/output.txt" "$REVIEW_JSON"
cmp "$RUN_DIR/output.txt" "$REVIEW_JSON"
sha256sum "$RUN_DIR/output.txt" "$REVIEW_JSON"
python scripts/ontology_development/summarize_target_candidates.py \
  "$REVIEW_JSON"
git status --short "$REVIEW_JSON"
```

The silent `cmp` and matching hashes show that no accidental transformation took
place. The review copy may now be edited without altering the raw run artifacts.

## Review checklist

Review all 40 records, paying particular attention to:

- whether each `likely_phrase_forms` item is a direct first-person declaration,
  rather than a question, third-person statement, or broader expression;
- whether at least one likely form can be found by the current search patterns;
- historical spelling and address forms that require a pattern revision;
- edition-specific language labels, especially older Danish and Norwegian texts;
- normalized genre labels for later stratification;
- balance across language, genre, period, relationship, and pragmatic situation;
- whether repository and rights claims remain explicitly provisional;
- duplicate or near-duplicate works, adaptations, and translations.

Do not delete a potentially useful candidate merely because its exact phrase or
source has not yet been verified. Correct clear factual or structural problems
and retain uncertainty as a concrete `verification_needed` task.

## Promote the reviewed candidate list

Run this block only after we have reviewed the working file together and agreed
that its corrections are appropriate:

```bash
cd "$LMCW"
REVIEW_JSON='data/development/target_candidates_review_v0_1.json'
APPROVED_JSON='data/development/target_candidates_v0_1.json'
python -m json.tool "$REVIEW_JSON" >/dev/null
python scripts/ontology_development/summarize_target_candidates.py \
  "$REVIEW_JSON"
cp "$REVIEW_JSON" "$APPROVED_JSON"
sha256sum "$APPROVED_JSON"
git diff --no-index /dev/null "$APPROVED_JSON" || true
```

“Approved” here means approved for source verification, not cleared for download,
corpus inclusion, or quotation.

## Review checkpoint

For the first half of this step, stop after staging the review copy and share its
path, checksum output, summary, and the file itself. We will review and correct
that complete file together before running the promotion block or selecting one
specific edition for the Step 4 acquisition trial.
