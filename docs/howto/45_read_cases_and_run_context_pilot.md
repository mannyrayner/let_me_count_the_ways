# 45. Read the evidence and run the context pilot

Run commands from the repository root. Python 3 and Git suffice for preparation;
API stages use the existing OPENAI_API_KEY and model alias 5.6. The patch includes
completed reader pages, public source texts and the initial candidate inventory.
It includes no new model judgments.

## 1. Read the existing evidence

Open docs/reader/index.html in a browser. On Cygwin:

```bash
cygstart docs/reader/index.html
```

Search/filter locally without a server or internet connection. On GitHub, use
[the Markdown index](../reader/README.md), whose individual records render directly.
GitHub's ordinary file view does not execute HTML; the HTML is for a local browser
or static hosting. The collection has 252 annotations across 35 searched works.

Rebuild and check without API calls:

```bash
python scripts/reader/build_reader.py
python scripts/reader/build_reader.py --check
python scripts/docs/validate_runbook_index.py
```

## 2. Reproduce the three new sources and candidates

```bash
python scripts/corpus_acquisition/prepare_context_extension.py
python scripts/corpus/validate_canonical_corpus.py --write-index corpus/index.md
python scripts/extraction/extract_canonical_corpus.py \
  --patterns data/development/search_patterns_v0_13.json \
  --work-manifest data/acquisition/context_extension_3_v1/selection.json \
  --output results/extraction/context_extension_3_v0_13 \
  --private-output results/extraction_private/context_extension_3_v0_13
python scripts/extraction/audit_context_extension.py
```

The public downloads are cached in the repository. Le Petit Prince downloads
locally and is stored under existing ignored source/derived directories. Its
public manifest intentionally has no repository canonical.txt. The downloader
refuses to overwrite divergent bytes; a changed upstream edition needs an explicit
new source revision, not deletion of the hash check.

Expected inventory: War and Peace 37 candidates; King Lear 4; Le Petit Prince 1.
These are regex candidates, not approved occurrences. Read the
[source and research notes](../notes/context_study_v1.md) before interpreting counts.
An unavailable private McMillan source is an expected warning on a checkout that
does not contain that separately permissioned text.

## 3. Inspect the pilot inputs and estimate

```bash
python scripts/context_pilot/run_pilot.py
```

This prepares inputs and reports an estimate without making API calls. Expected:
8 cases, 4 conditions, 3 repetitions = 96 calls. The initial estimate is USD 7.43
using the recorded prices; actual use can differ.

Read results/context_pilot/v1_dossier/README.md for links to the exact context
inputs. Open its HTML inputs in a browser. The rose's inputs are local under
results/context_pilot_private/v1_dossier/inputs/C08/. Inspect the A/B/C/D boundaries
before running. The selection, prompt and schema are versioned. If the protocol
needs substantive changes, create a new version rather than overwriting prepared
v1 inputs or mixing incompatible results.

A means the extracted expression alone. Dossier D adds later excerpts; it does
not claim to supply the whole book. No historical score or prior model response
is supplied to any condition. Null/insufficient judgments remain distinct from zero.

## 4. Run the dossier pilot

For an initial small execution checkpoint, process four calls:

```bash
python scripts/context_pilot/run_pilot.py --run --max-calls 4
```

Calls are in the recorded shuffled order, so these are not necessarily one
case's four conditions. Then complete the same plan:

```bash
python scripts/context_pilot/run_pilot.py --run
```

Successful compatible calls resume automatically. Each call retains its request,
raw response, costs and validated output. If a call fails, inspect the retained
attempt before retrying:

```bash
python scripts/context_pilot/run_pilot.py --run --retry-failed
```

A retry is a new retained attempt and may incur another charge. The estimate
limit defaults to USD 25 for all remaining planned calls, not a hard billing cap.
The size guard defaults to 250,000 input characters, not a claim about the
model's token capacity. No input is silently truncated.

Reports are results/context_pilot/v1_dossier/summary.md and summary.json. They
remain explicitly not_run or partial until all selected judgments validate.
The JSON contains all T/P/E/O judgments and each condition's P distribution.
Private-source explanations and quotations remain in the local-only directory;
the public report contains scores and a local-only marker for that case.

## 5. Optional whole-play comparison

The shorter Lear text makes a practical first full-text comparison:

```bash
python scripts/context_pilot/run_pilot.py --scope full_text --cases C05 C06
python scripts/context_pilot/run_pilot.py --scope full_text --cases C05 C06 --run
```

This is a separate 24-call plan, initially estimated at USD 2.65. Its outputs go
to v1_full_text. D supplies the entire canonical play, C all text before the
specified exchange plus that exchange. Do not combine dossier and full-text
results as though they were the same condition. With --cases, the summary covers
the selected plan; retained call artifacts for other plans are not deleted.

Full-text mode also exists for the other works. Inspect its preflight and verify
the selected API model's capacity before raising --max-input-chars. In particular,
War and Peace has about 2.9 million characters; the default guard prevents that
large request. There is no automatic summarization or truncation fallback.

## 6. Annotate all three new works using the established method

This is separate from the context experiment and can run before or after it:

```bash
python scripts/annotation/run_context_extension.py
python scripts/annotation/run_context_extension.py --run
```

The first command is preflight only. The second runs membership review, freezes
KEEP cases, generates translations and uses unchanged classification v0.3.1.
UNCERTAIN cases are not promoted. Estimate guards apply to each translation and
classification stage; membership review is separately metered, as in runbook 44.

Public outputs:

- results/review/context_extension_3_v0_13_ai_review_v1/
- results/annotation/context_extension_3_v0_13_translations_v1/
- results/annotation/context_extension_3_v0_13_v0_3_1/

Le Petit Prince uses the corresponding results/review_private/ and
results/annotation_private/ directories. Do not force-add those directories.
The current 252-record reader stays frozen until completed annotations and the
next corpus snapshot are explicitly added to its configuration.

## 7. Review and check in completed public results

Inspect summaries and failures, then stage only the relevant public run directories:

```bash
git status --short
git add results/context_pilot/v1_dossier
# Add v1_full_text too if that experiment was run.
git diff --cached --stat
git commit -m "Record context pilot v1 judgments"
git push origin main
```

For the established-method extension, stage its public review, translation and
annotation directories listed above after reviewing them. Keep the two methods
identifiable; do not overwrite historical runs or revise old scores silently.

## Checks for implementation changes

The focused standard-library tests require no API:

```bash
python -m unittest scripts.reader.test_reader \
  scripts.context_pilot.test_pilot \
  scripts.corpus_acquisition.test_prepare_context_extension \
  scripts.docs.test_howto_inventory
```

The JavaScript filter check runs when Node is installed. Source tests needing
the local Petit Prince source skip if it has not been acquired. Existing
annotation regression tests use pytest; all API responses in those tests are
synthetic fixtures held in temporary directories, never research results.
