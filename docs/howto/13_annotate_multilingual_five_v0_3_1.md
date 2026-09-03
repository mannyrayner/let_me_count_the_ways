# Step 13: annotate the multilingual five-text batch with v0.3.1

This runbook acquires, extracts, reviews, annotates, and audits the named
`multilingual_five_v1` corpus. It stops after this batch. Do not add these works
to `development_three`, change annotation v0.3.1 during the run, or proceed to a
larger corpus from this runbook.

The membership manifest contains only provenance paths. Annotation version,
model, prompt, patterns, and context radius remain run configuration. The five
current provenance records are deliberately marked `acquisition_blocked`; that
is a safe checkpoint, not approval. Replace that status only after exact files
and rights findings have been reviewed.

## 1. Preflight

```bash
cd "$LMCW"
git pull --ff-only
test -z "$(git status --short)" || {
  echo 'Working tree is not clean; stop and review it.' >&2
  exit 1
}
python -m pytest -q
python -m json.tool data/batches/multilingual_five_v1.json
python -m json.tool data/development/search_patterns_v0_3.json
test -f prompts/annotation/classify_passage_v0_3_1.md
test -f prompts/annotation/classification_schema_v0_3.json
```

The expected IDs are `runeberg-dukkhjem`, `gutenberg-1256`,
`runeberg-frkjulie`, `gutenberg-19794`, and `gutenberg-18797`.

## 2. Acquire and approve the exact editions

Open each catalogue page recorded in `provenance/sources/*.json`, confirm its
identity and original language, and select UTF-8 plain text where offered. For
Runeberg, save the dedicated continuous electronic edition, not facsimile/OCR.
Do not substitute a translation, another Gutenberg number, or raw OCR merely
because it downloads more easily.

Create these local literary texts:

| Source ID | Local path |
| --- | --- |
| `runeberg-dukkhjem` | `data/raw/ibsen-et-dukkehjem/runeberg-dukkhjem.txt` |
| `gutenberg-1256` | `data/raw/rostand-cyrano-de-bergerac/gutenberg-1256.txt` |
| `runeberg-frkjulie` | `data/raw/strindberg-froken-julie/runeberg-frkjulie.txt` |
| `gutenberg-19794` | `data/raw/goethe-die-leiden-des-jungen-werther/gutenberg-19794.txt` |
| `gutenberg-18797` | `data/raw/lafayette-la-princesse-de-cleves/gutenberg-18797.txt` |

Preserve every download unchanged alongside any derived literary text. If a
Runeberg source is HTML, retain it as `source-download.html`, derive `.txt`
deterministically, and record both hashes, the tool/version, and transformations.
Never search HTML markup. For Gutenberg #18797, retain the exact download and
remove only the ordinary Gutenberg header/footer in the derived `.txt`; record
exact boundary lines and both checksums. Do not modernise spelling, punctuation,
apostrophes, or Unicode content.

```bash
find data/raw/ibsen-et-dukkehjem \
     data/raw/rostand-cyrano-de-bergerac \
     data/raw/strindberg-froken-julie \
     data/raw/goethe-die-leiden-des-jungen-werther \
     data/raw/lafayette-la-princesse-de-cleves \
     -type f -print0 | sort -z | xargs -0 sha256sum
```

Update, rather than replace, the existing provenance records. Each approved
record needs `local_path`, direct `source_url`, `retrieved_at`, `sha256`, and an
edition-specific `rights_note`. Preserve Gutenberg ebook/release/update data,
its header statement, separately checked Australian status and guidance URL,
author-death/publication evidence, Runeberg editors/source edition and editorial
transformations, raw/derived hashes, observed encoding, and review date.

For *Et dukkehjem*, retain “Norwegian; modernised electronic edition of Ibsen's
Danish-Norwegian original.” Never claim that Runeberg preserves 1879 orthography
or simply call the 1879 original “Bokmål.” Retain the documented typography
changes for *Fröken Julie*. Only then set `review_status` to
`approved_for_development_processing`.

```bash
python - <<'PY'
import hashlib, json
from pathlib import Path
manifest = json.loads(Path("data/batches/multilingual_five_v1.json").read_text(encoding="utf-8"))
for member in manifest["sources"]:
    provenance_path = Path(member["provenance"])
    record = json.loads(provenance_path.read_text(encoding="utf-8"))
    assert record["review_status"] == "approved_for_development_processing", provenance_path
    required = {"local_path", "source_url", "retrieved_at", "sha256", "rights_note"}
    assert not required.difference(record), (provenance_path, required.difference(record))
    assert "PENDING" not in record["rights_note"].upper(), provenance_path
    source = Path(record["local_path"])
    assert source.is_file(), source
    actual = hashlib.sha256(source.read_bytes()).hexdigest()
    assert actual == record["sha256"], (source, actual, record["sha256"])
    source.read_text(encoding="utf-8")
    print(f"Approved source passed: {record['source_id']} {actual}")
PY
```

Stop if any edition, transformation, rights basis, encoding, or checksum is
uncertain. Commit reviewed sources and provenance before deriving artifacts.

## 3. Inspect source spelling and patterns

Inspect actual bytes, including every eventual zero-hit work:

```bash
rg -n -i -C 2 'jeg|elsker|deg|dig' data/raw/ibsen-et-dukkehjem/runeberg-dukkhjem.txt
rg -n -i -C 2 "je|t[’']|vous|aime" data/raw/rostand-cyrano-de-bergerac/gutenberg-1256.txt
rg -n -i -C 2 'jag|älskar|dig|er' data/raw/strindberg-froken-julie/runeberg-frkjulie.txt
rg -n -i -C 2 'ich|liebe|dich|euch|sie' data/raw/goethe-die-leiden-des-jungen-werther/gutenberg-19794.txt
rg -n -i -C 2 "je|t[’']|vous|aime" data/raw/lafayette-la-princesse-de-cleves/gutenberg-18797.txt
```

If this demonstrates a missing historical/typographic variant, revise the
shared versioned pattern file and tests before extraction. Do not broaden it to
general affection, third-person love, or book-specific heuristics.

## 4. Make and inspect extraction-only dry runs

```bash
for PROVENANCE in \
  provenance/sources/runeberg-dukkhjem.json \
  provenance/sources/gutenberg-1256.json \
  provenance/sources/runeberg-frkjulie.json \
  provenance/sources/gutenberg-19794.json \
  provenance/sources/gutenberg-18797.json
do
  python scripts/pipeline/run_single_text_pipeline.py "$PROVENANCE" \
    --patterns data/development/search_patterns_v0_3.json \
    --annotation-version 0.3.1 --model 5.6 --dry-run || exit 1
done
```

For each printed run, inspect `extraction/passages.jsonl`, metadata/fingerprint,
manifest, prepared inputs, and report. Manually confirm every hit is a direct
first-person/second-person target in adequate context. For zero hits, recheck
orthography, apostrophes, spacing, inflection, encoding, and conventional forms.
Do not annotate until all five inventories are accepted. Preserve and commit the
reviewed extraction runs, not disposable batch summaries.

## 5. Prepare, execute, and resume the one-command batch

The batch runner reuses compatible reviewed extractions and refuses implicit
re-extraction. First make a call-free batch dry run:

```bash
python scripts/pipeline/run_batch.py \
  --manifest data/batches/multilingual_five_v1.json \
  --patterns data/development/search_patterns_v0_3.json \
  --annotation-version 0.3.1 --model 5.6 --dry-run
BATCH_DIR='results/batch_runs/multilingual_five_v1/v0.3.1-5.6'
python -m json.tool "$BATCH_DIR/summary.json"
sed -n '1,360p' "$BATCH_DIR/report.md"
```

Require five requested/prepared texts, the manually approved total occurrence
count, zero attempted calls, and no source error. Then execute identically:

```bash
test -n "${OPENAI_API_KEY:-}" || {
  echo 'OPENAI_API_KEY is not set; stop before annotation.' >&2
  exit 1
}
python scripts/pipeline/run_batch.py \
  --manifest data/batches/multilingual_five_v1.json \
  --patterns data/development/search_patterns_v0_3.json \
  --annotation-version 0.3.1 --model 5.6
```

Do not use `--force`, modify v0.3.1, or redesign P/T/E/O. A normal rerun resumes,
skips compatible valid outputs, preserves failures, and lets other texts finish.

## 6. Audit completeness, costs, and unusual cases

```bash
python - "$BATCH_DIR" <<'PY'
import json, sys
from pathlib import Path
root = Path(sys.argv[1])
summary = json.loads((root / "summary.json").read_text(encoding="utf-8"))
assert summary["batch_id"] == "multilingual_five_v1", summary
assert summary["annotation_version"] == "0.3.1" and summary["model_alias"] == "5.6", summary
assert summary["status"] == "complete", summary
assert summary["texts_completed"] == summary["texts_requested"] == 5, summary
assert summary["valid_annotations"] == summary["occurrences"], summary
assert summary["failures"] == summary["model_calls_needed"] == 0, summary
assert sum(summary["ontology_statistics"]["score_distributions"]["T"].values()) == summary["valid_annotations"]
print(f"Complete: 5 texts, {summary['valid_annotations']} valid, USD {summary['estimated_total_cost_usd']:.6f}")
PY

for SOURCE_ID in runeberg-dukkhjem gutenberg-1256 runeberg-frkjulie gutenberg-19794 gutenberg-18797
do
  RUN="$BATCH_DIR/texts/$SOURCE_ID"
  EXPECTED="$(python -c 'import json,sys; print(json.load(open(sys.argv[1], encoding="utf-8"))["extracted_occurrences"])' "$RUN/manifest.json")"
  python scripts/pipeline/audit_pipeline_run.py "$RUN" --expected-occurrences "$EXPECTED" || exit 1
done
python scripts/security/scan_credentials.py "$BATCH_DIR"
python -m json.tool "$BATCH_DIR/unusual_cases.json"
sed -n '1,520p' "$BATCH_DIR/report.md"
```

The report covers requested/completed texts, valid outputs, unresolved and
historical failures, total/per-text cost, cost per valid annotation, locations,
P/T/E/O distributions, ontology fit, and thresholds. Review every unusual case
in full context; flags are informative, not errors. Closely inspect distributed
authorship in *Cyrano*, duty in *Et dukkehjem*, manipulation without false E in
*Fröken Julie*, intense but potentially T introspection in *Werther*, and
restrained confession in *La Princesse de Clèves*. Keep qualitative complexity
in `contextual_interpretation`, do not force O, and audit any background
knowledge declaration.

## 7. Preserve results and stop

```bash
test -z "$(git diff --cached --name-only)" || {
  echo 'The index already contains staged files; review it first.' >&2
  exit 1
}
git add "$BATCH_DIR"
git diff --cached --check
git diff --cached --stat
python scripts/security/scan_credentials.py "$BATCH_DIR"
git commit -m 'Record multilingual-five v0.3.1 batch run'
git push origin HEAD
git status --short
```

Then create a separate descriptive eight-text report combining this completed
batch with `development_three` v0.3.1: languages, occurrences, P/T/E/O
distributions, ontology fit, O cases, high-E cases, and high-P cases. Do not
modify either membership manifest or infer language effects. Answer the eight
handoff questions and stop for review; do not begin the next corpus expansion.
