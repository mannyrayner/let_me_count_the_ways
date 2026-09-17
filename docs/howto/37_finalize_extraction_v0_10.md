# 37. Finalize and freeze extraction v0.10

Run from the repository root (`cd "$LMCW"`). This is a deterministic extraction
stage. Do not call a model, perform KEEP/EXCLUDE review, enrich context, translate,
or begin T/P/E/O annotation.

## Procedure

1. Validate the canonical corpus and the checked-in v0.9 baseline:
   `python scripts/corpus/validate_canonical_corpus.py`, then confirm
   `results/extraction/canonical_31_v0_9/summary.json` reports pattern version
   `0.9`, 31 attempted works, 213 public candidates, and one unavailable work.
2. Run the targeted pattern regressions:
   `python -m unittest scripts.extraction.test_search_patterns_v0_10`.
3. Confirm `data/development/search_patterns_v0_10.json` was generated from v0.9
   and that `git diff --no-index data/development/search_patterns_v0_9.json data/development/search_patterns_v0_10.json`
   contains only the changes documented in `search_patterns_v0_10_changes.md`.
4. Remove only a disposable prior v0.10 run, then run all 31 canonical works:
   `rm -rf results/extraction/canonical_31_v0_10 results/extraction_private/canonical_31_v0_10 && python scripts/extraction/extract_canonical_corpus.py --patterns data/development/search_patterns_v0_10.json --output results/extraction/canonical_31_v0_10 --private-output results/extraction_private/canonical_31_v0_10`.
   An unavailable local McMillan source is acceptable; never copy its text into
   the public output.
5. Inspect `results/extraction/canonical_31_v0_10/delta_from_v0_9.md` candidate by
   candidate. Confirm every changed-work count, pattern ID, and match, and reject
   an unexplained count increase.
6. Explicitly verify the required French perfect and conditional, Swedish
   exclusive modal/perfect, German `euch`, Italian elided imperfect, and English
   emphasized-target cases with `rg -n 'assez aimée|aimerais|kunnat älska|euch liebe|t’amavo|loved _you' results/extraction/canonical_31_v0_10/works`.
7. Inspect `summary.json` and `summary.md`: confirm 230 public candidates, no
   zero-yield works, no unusually high-count works, and McMillan `unavailable`.
8. Confirm the delta report declares `canonical_31_v0_10` the frozen
   deterministic candidate set. Do not revise patterns during annotation absent
   a truly blocking error.
9. Stage only the named v0.10 pattern/report, regression test, extraction tree,
   methodology note, this runbook, and its single index entry. Never use
   `git add .`.
10. Commit with `git commit -m "Finalize multilingual LOVE extraction v0.10"`.
11. Post-commit, run `git status --short`,
    `git show --stat --oneline HEAD`, and the tests from step 2; then stop for
    Manny/ChatGPT review before annotation.

## Review checkpoint

Review the complete 17-candidate delta and the freeze declaration. This runbook
ends deterministic extraction and does not authorize scholarly annotation.
