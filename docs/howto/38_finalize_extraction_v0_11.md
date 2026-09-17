# 38. Finalize extraction precision and freeze v0.11

Run from the repository root (`cd "$LMCW"`). This is a deterministic extraction
stage. Do not call a model, perform KEEP/EXCLUDE review, enrich context,
translate, or begin T/P/E/O annotation.

## Procedure

1. Validate the corpus with `python scripts/corpus/validate_canonical_corpus.py`.
   Confirm `results/extraction/canonical_31_v0_10/summary.json` reports version
   `0.10`, 31 attempted works, 230 public candidates, and one unavailable work.
2. Run the blocking German positive and negative regressions with
   `python -m unittest scripts.extraction.test_search_patterns_v0_11`. Confirm
   main and subordinate `dich`, `euch`, and uppercase `Sie` match, while all
   three lowercase-`sie` examples do not.
3. In that same test run, confirm `aimerai` matches only `fr_future` and carries
   future metadata, while `aimerais` matches only `fr_conditional` and carries
   modal/conditional metadata.
4. Generate v0.11 by copying v0.10, changing its schema version, applying the
   shared German target substitution `(?:dich|euch|(?-i:Sie))` to all four
   German families, and splitting only the French future/conditional pattern.
   Review `git diff --no-index data/development/search_patterns_v0_10.json data/development/search_patterns_v0_11.json`.
5. Remove only a disposable v0.11 run and extract all canonical works:
   `rm -rf results/extraction/canonical_31_v0_11 results/extraction_private/canonical_31_v0_11`, then
   `python scripts/extraction/extract_canonical_corpus.py --patterns data/development/search_patterns_v0_11.json --output results/extraction/canonical_31_v0_11 --private-output results/extraction_private/canonical_31_v0_11`.
   McMillan may remain unavailable; never move private candidate text into the
   public output.
6. Inspect every row of `results/extraction/canonical_31_v0_11/delta_from_v0_10.md`.
   Confirm all membership changes are explained German removals, with no
   additions or non-German changes.
7. Search the v0.11 candidate files for `ich liebe sie noch`, `ich liebe sie so
   wie du`, and `ich sie liebe`; explicitly confirm the three known lowercase
   third-person false positives are absent.
8. Inspect extracted `fr_future` and `fr_conditional` records. Confirm at least
   one `je t'aimerai` record has `tense_aspect: future`, and one `Je vous
   aimerais` record has `tense_aspect: modal` plus `modality: conditional`.
9. Confirm `summary.json` reports 227 public candidates, no zero-yield works,
   no unusually high-count works, and one unavailable work. Then confirm the
   delta report declares `canonical_31_v0_11` frozen. Do not change extraction
   during annotation unless a truly blocking defect is found.
10. Stage only the named v0.11 pattern and change report, focused regression
    test, v0.11 public extraction tree, methodology note, this runbook, and its
    one index entry. Never use `git add .` and never stage private output.
11. Commit with `git commit -m "Finalize LOVE extraction precision v0.11"`.
12. Post-commit, run `git status --short`, `git show --stat --oneline HEAD`, and
    `python -m unittest scripts.extraction.test_search_patterns_v0_11`; then stop
    for Manny/ChatGPT review before annotation.

## Review checkpoint

The freeze requires an explained three-candidate German delta and unchanged
French membership with corrected metadata. This runbook does not authorize
scholarly annotation.
