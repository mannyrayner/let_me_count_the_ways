# Acquire and annotate the five-work commitment extension

This targeted extension contains *Pengar*, *Constance Ring*, *The Odd Women*,
*Vera*, and *Lucie*. See [selection and literary context](../notes/commitment_extension_5_v1.md).
Its selection is exploratory; classification outcomes remain to be measured.
The original extraction/review/annotation directories and 225-case baseline
are historical outputs and must not be overwritten.

Run from the repository root. Commands work with the existing Cygwin `python`
and `OPENAI_API_KEY` setup. The key is read only from the environment.

## 1. Verify the acquired texts

The change includes sources, canonical texts, and extraction outputs. To verify
deterministic reproduction, run:

```bash
cd "$LMCW"
python scripts/corpus_acquisition/prepare_commitment_extension.py
python scripts/corpus/validate_canonical_corpus.py corpus/works --write-index corpus/index.md
```

On this baseline, expect 36 canonical works: 35 public and the existing private
McMillan work. The usual unavailable-private-source warning is acceptable.
The acquisition script downloads missing public sources, reuses preserved
downloads, and refuses divergent existing derived or canonical files. National
Library OCR is indexed by printed page and retains links to page images.

## 2. Reproduce the five-work extraction and preflight

```bash
python scripts/extraction/extract_canonical_corpus.py --patterns data/development/search_patterns_v0_11.json --work-manifest data/acquisition/commitment_extension_5_v1/selection.json --output results/extraction/commitment_extension_5_v0_11
python scripts/extraction/extract_canonical_corpus.py --patterns data/development/search_patterns_v0_12.json --work-manifest data/acquisition/commitment_extension_5_v1/selection.json --output results/extraction/commitment_extension_5_v0_12
python scripts/extraction/compare_commitment_patterns.py
python scripts/annotation/run_commitment_extension.py
```

The default wrapper makes no API calls. It verifies the selected work set,
canonical hashes, candidate uniqueness, matched strings, and context offsets.
It reports the model alias, pricing date, and whether an API key is configured,
without printing the key. Inspect the extraction summary and the recorded
passage leads, including the original page images for doubtful OCR.

V0.12 adds two Norwegian constructions: intervening `også/ogsaa` and historical
past-tense `elskede`. The comparison covers all available public corpus texts
and is recorded under `results/extraction_audit/commitment_extension_5_v0_12/`.
The previous extraction and annotation outputs remain untouched.

## 3. Run the existing annotation pipeline

With the normal `OPENAI_API_KEY` available locally:

```bash
python scripts/annotation/run_commitment_extension.py --run
```

This command runs the established membership review, validates and freezes
the KEEP subset, generates context translations, enriches the retained records,
and classifies all KEEP cases using v0.3.1. It uses the existing priced model
alias `5.6` for comparability and retains the standard API usage/provenance
artifacts. The selection notes are not injected into the classifier.

Translations and classifications are estimated before their respective API
stages. Each defaults to a USD 25 estimate limit, matching the earlier full-run
convention; this is not a total-spend cap. Membership review is separately
metered by the existing reviewer. All stages use extension-specific paths and
compatible successful API artifacts are resumable.

If a stage fails, inspect its retained failure artifacts. For timeout-only
translation/classification failures, the same run can be resumed with
`--timeout 600`. The existing membership reviewer retains its own timeout.

## 4. Inspect results and verify

The final annotation summary is
`results/annotation/commitment_extension_5_v0_12_v0_3_1/summary.json`.
Its neighbouring `review_cases.md` identifies high-P, mixed, and other flagged
cases. Candidate, KEEP, and high-P counts must be reported separately.

```bash
python -m unittest discover -s scripts/corpus_acquisition -p 'test_*.py' -q
python -m unittest discover -s scripts/corpus -p 'test_*.py' -q
python scripts/docs/validate_runbook_index.py
git diff --check
git status --short
```

Review and explicitly stage only this extension's generated API directories
when ready to commit. No API output exists merely because an acquisition or
extraction command succeeded.
