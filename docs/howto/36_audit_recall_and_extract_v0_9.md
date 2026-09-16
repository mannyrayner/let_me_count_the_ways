# 36. Audit recall and extract the canonical corpus with v0.9

Run from the repository root (`cd "$LMCW"`). This is a deterministic extraction
stage: do not call a model or begin scholarly KEEP/EXCLUDE review.

## Procedure

1. Validate all canonical manifests, files, and hashes:
   `python scripts/corpus/validate_canonical_corpus.py`.
2. Run the broad diagnostic audit:
   `python scripts/extraction/audit_love_recall.py`.
3. Inspect `results/extraction_audit/canonical_31_pre_v0_9/summary.md` and the
   per-work `unmatched_cues.jsonl` files. These cues are not occurrences.
4. Review the evidence and bounded production changes in
   `data/development/search_patterns_v0_9_changes.md`; confirm v0.7 and v0.8
   remain unchanged.
5. Run focused regressions:
   `python -m unittest scripts.extraction.test_audit_love_recall scripts.extraction.test_extract_canonical_corpus`.
6. Extract all 31 requested works, keeping private output outside the public tree:
   `python scripts/extraction/extract_canonical_corpus.py --patterns data/development/search_patterns_v0_9.json --output results/extraction/canonical_31_v0_9 --private-output results/extraction_private/canonical_31_v0_9`.
   An unavailable local McMillan source is non-blocking.
7. Verify *Persuasion*:
   `rg -n 'I have loved none but you' results/extraction/canonical_31_v0_9/works/austen-persuasion/candidates.jsonl`.
8. Build the exclusive-target and historical diagnostics:
   `python scripts/extraction/compare_v09_extraction.py`.
9. Inspect `exclusive_target_candidates.md`, `historical_comparison.md`, and
   `low_yield_inspection.md` under the v0.9 extraction directory.
10. Confirm the required low-yield works are discussed without imposing a quota.
11. Stage only named files and directories with explicit `git add` arguments;
    never use `git add .`.
12. Commit with
    `git commit -m "Audit LOVE recall and extract canonical corpus v0.9"`.
13. Post-commit, run `git status --short`, inspect the commit with
    `git show --stat --oneline HEAD`, and stop for Manny/ChatGPT review.

## Review checkpoint

Review the deterministic candidates and diagnostics. Do not retrieve wider
contexts, translate, annotate T/P/E/O, or launch AI scholarly review.
