# Step 14: build the eight-work corpus inspection report

This runbook generates one human-readable report from the accepted v0.3.1
annotations for the development three and multilingual five. The enrichment
stage adds translations and explanations but cannot alter P/T/E/O, confidence,
ontology fit, or utterance status. Complete this review and commit checkpoint
before beginning Step 15.

The report command deliberately exits with status 2 when an offline or failed
run produces an incomplete report. That status means “prepared but incomplete,”
not that model calls occurred.

## 1. Preflight

```bash
cd "$LMCW"
git pull --ff-only
test -z "$(git status --short)" || {
  echo 'Working tree is not clean; stop and review it.' >&2
  exit 1
}
test -n "$OPENAI_API_KEY" || {
  echo 'OPENAI_API_KEY is not set; stop before the eventual online run.' >&2
  exit 1
}
python scripts/reporting/build_corpus_report.py --help
python scripts/reporting/render_corpus_report.py --help
python scripts/reporting/validate_corpus_report.py --help
```

The API key is checked but never printed or placed on the command line.

## 2. Verify the exact source batch runs and counts

Use these paths; do not substitute a glob or a directory selected as “latest.”

```bash
cd "$LMCW"
DEV_RUN='results/batch_runs/development_three/v0.3.1-5.6'
MULTI_RUN='results/batch_runs/multilingual_five_v1/v0.3.1-5.6'
REPORT_NAME='canonical_eight_v0_3_1'
REPORT_ROOT='results/corpus_reports'

for RUN in "$DEV_RUN" "$MULTI_RUN"
do
  test -f "$RUN/summary.json" || {
    echo "Missing $RUN/summary.json; stop." >&2
    exit 1
  }
  python -m json.tool "$RUN/summary.json" >/dev/null
done

python - "$DEV_RUN/summary.json" "$MULTI_RUN/summary.json" <<'PY'
import json, sys
summaries=[json.load(open(path,encoding="utf-8")) for path in sys.argv[1:]]
for item in summaries:
    if item["status"] != "complete" or item["dry_run"]:
        raise SystemExit(f"Not a completed real batch: {item['batch_id']}")
    if item["valid_annotations"] != item["occurrences"] or item["failures"]:
        raise SystemExit(f"Incomplete annotations: {item['batch_id']}")
    print(f"{item['batch_id']}: {item['occurrences']} occurrences")
print(f"Combined: {sum(item['occurrences'] for item in summaries)} occurrences")
PY
```

Expected output is 22 development occurrences, 19 multilingual occurrences,
and 41 combined. The report command independently validates complete text runs,
extraction/input/annotation set equality, exactly one valid annotation per hit,
unique composite occurrence identities, and the same summary totals.

## 3. Run all tests immediately before the dry run

```bash
cd "$LMCW"
python -m pytest -q
```

The reporting tests cover the English/non-English translation contract, cache
invalidation by model/prompt/passage/annotation, cache reuse, failed-attempt
retry, bounded passages, Markdown-sensitive text, deterministic anchors/order,
duplicate-looking IDs from different run contexts, incomplete/missing records,
annotation immutability, and deterministic JSON-only rendering.

## 4. Prepare offline and inspect the call estimate

`--offline` performs all deterministic collection, validation, cache inspection,
request preparation, and incomplete rendering, but makes no model calls. Status
2 is required while any enrichment is absent.

```bash
cd "$LMCW"
set +e
python scripts/reporting/build_corpus_report.py \
  --name "$REPORT_NAME" \
  --batch-run "$DEV_RUN" \
  --batch-run "$MULTI_RUN" \
  --enrichment-model 5.6 \
  --offline \
  | tee "$REPORT_ROOT/$REPORT_NAME.offline.log"
OFFLINE_STATUS=${PIPESTATUS[0]}
set -e
test "$OFFLINE_STATUS" -eq 0 -o "$OFFLINE_STATUS" -eq 2
```

On a fresh cache the command reports exactly 8 works, 41 unique occurrences,
languages `en, fr, no, sv, de`, 0 cache hits, 41 cache misses/calls required,
0 invalid source records, the output paths, and an output-token-only rough
maximum cost. On a complete cache it exits 0 and reports 41 hits and 0 calls.
Review the exact model (`gpt-5.6-sol`), call count, and rough estimate before
continuing. The estimate is deliberately conservative and excludes input cost;
the completed summary records actual API usage cost.

## 5. Inspect one prepared request in every language

Offline preparation writes easy-to-find request records here:

```text
results/corpus_reports/canonical_eight_v0_3_1/work/requests/
```

List all requests, then print the first in report order available for each
language:

```bash
cd "$LMCW"
REQUEST_DIR="$REPORT_ROOT/$REPORT_NAME/work/requests"
find "$REQUEST_DIR" -maxdepth 1 -type f -name '*.json' -print | sort
for LANG in en fr no sv de
do
  REQUEST=$(find "$REQUEST_DIR" -maxdepth 1 -type f \
    -name "$LANG--*.json" -print | sort | head -n 1)
  test -n "$REQUEST" || { echo "No $LANG request; stop." >&2; exit 1; }
  echo "===== $LANG: $REQUEST ====="
  python -m json.tool "$REQUEST"
done
```

Confirm each bounded source passage includes its target; metadata, location,
existing annotation analysis/evidence, and background-knowledge metadata are
present; English requests require `translation_en: null`; and no output field
can revise annotation data. Check especially that negation, embedding, and
quotation are preserved in the requested translation. Requests contain a
maximum 1,600-character deterministic passage and never clip inside the target.

## 6. Generate missing enrichments and the complete report

After approving the requests, model, maximum call count, and cost estimate, run:

```bash
cd "$LMCW"
python scripts/reporting/build_corpus_report.py \
  --name "$REPORT_NAME" \
  --batch-run "$DEV_RUN" \
  --batch-run "$MULTI_RUN" \
  --enrichment-model 5.6 \
  | tee "$REPORT_ROOT/$REPORT_NAME.generation.log"
```

The command calls only missing/stale cache identities. A cache identity includes
the composite run occurrence key, occurrence ID, exact API model, prompt
version/hash, schema version/hash, source-input hash, and immutable annotation
input hash. Calls preserve numbered attempts with request, raw response, parsed
output, validation, status, usage/cost, metadata, and any error beneath:

```text
results/corpus_reports/cache/<report-occurrence-key>/<cache-key>/attempt-NNN/
```

A failure does not erase other results: it is retained, the report is visibly
`INCOMPLETE`, and the command exits 2. After inspecting the saved `error.txt`,
retry with the identical generation command above; only missing records are
called. Use `--force-enrichment` only after an explicit decision to regenerate
all valid cached enrichments—it is not needed to rerender a report.

A successful run writes:

```text
results/corpus_reports/canonical_eight_v0_3_1.json
results/corpus_reports/canonical_eight_v0_3_1.md
results/corpus_reports/canonical_eight_v0_3_1.summary.json
```

## 7. Validate completeness and annotation immutability

```bash
cd "$LMCW"
REPORT_JSON="$REPORT_ROOT/$REPORT_NAME.json"
REPORT_MD="$REPORT_ROOT/$REPORT_NAME.md"
REPORT_SUMMARY="$REPORT_ROOT/$REPORT_NAME.summary.json"

python -m json.tool "$REPORT_JSON" >/dev/null
python -m json.tool "$REPORT_SUMMARY" >/dev/null
test -s "$REPORT_MD"
python scripts/reporting/validate_corpus_report.py \
  --report "$REPORT_JSON" \
  --batch-run "$DEV_RUN" \
  --batch-run "$MULTI_RUN"
python - "$REPORT_SUMMARY" <<'PY'
import json, sys
value=json.load(open(sys.argv[1],encoding="utf-8"))
assert value["works"] == 8, value
assert value["occurrences"] == 41, value
assert value["failures"] == 0, value
assert value["completeness_status"] == "complete", value
print(json.dumps(value,indent=2,ensure_ascii=False))
PY
```

The purpose-built validator recollects the explicit batch runs and compares the
report with the original annotations. It rejects missing/extra occurrences,
duplicate anchors, unresolved provenance, incorrect language/translation
pairings, absent context/commentary, any changed P/T/E/O score, confidence,
ontology fit or utterance status, and an incorrect completeness flag.

## 8. Rerun and prove that no model call occurs

Run the identical ordinary command. Do not use `--offline` or
`--force-enrichment` for this acceptance test.

```bash
cd "$LMCW"
python scripts/reporting/build_corpus_report.py \
  --name "$REPORT_NAME" \
  --batch-run "$DEV_RUN" \
  --batch-run "$MULTI_RUN" \
  --enrichment-model 5.6 \
  | tee "$REPORT_ROOT/$REPORT_NAME.rerun.log"
grep -Fx 'Cache misses: 0' "$REPORT_ROOT/$REPORT_NAME.rerun.log"
grep -Fx 'Model calls required: 0' "$REPORT_ROOT/$REPORT_NAME.rerun.log"
grep -Fx 'Enrichments reused: 41; newly generated: 0; failures: 0' \
  "$REPORT_ROOT/$REPORT_NAME.rerun.log"
```

If any grep fails, stop: identical reruns are not yet acceptably cached.

## 9. Rerender Markdown using JSON only

This command has no model/API pathway:

```bash
cd "$LMCW"
python scripts/reporting/render_corpus_report.py \
  "$REPORT_JSON" \
  --markdown "$REPORT_ROOT/$REPORT_NAME.rerendered.md"
cmp "$REPORT_MD" "$REPORT_ROOT/$REPORT_NAME.rerendered.md"
rm "$REPORT_ROOT/$REPORT_NAME.rerendered.md"
```

A nonzero `cmp` means Markdown is not reproducibly derived from the durable
presentation JSON; stop and diagnose it.

## 10. Human review and occurrence-ID reconciliation

Read the report sequentially and inspect its useful-case index:

```bash
cd "$LMCW"
less "$REPORT_MD"
grep -nE '\*\*[PEO]:\*\* [234]' "$REPORT_MD"
grep -n '\*\*Ontology fit:\*\*' "$REPORT_MD"
grep -n '\*\*Utterance status:\*\*' "$REPORT_MD"
```

The opening indices group all eight works and five languages, then P >= 2,
E >= 2, O > 0, non-natural fit, low confidence, embedded/reported, and
quoted/revoiced cases. Negation is printed as
`unknown / not structurally represented`: the command intentionally does not
apply unreliable multilingual substring heuristics.

Compare the report's composite occurrence keys and source-run occurrence IDs:

```bash
cd "$LMCW"
python - "$REPORT_JSON" "$DEV_RUN" "$MULTI_RUN" <<'PY'
import json, pathlib, sys
report=json.load(open(sys.argv[1],encoding="utf-8"))["occurrences"]
reported={(r["batch_run"],r["source_id"],r["occurrence_id"]) for r in report}
source=set()
for run_name in sys.argv[2:]:
    run=pathlib.Path(run_name)
    summary=json.load(open(run/"summary.json",encoding="utf-8"))
    for text in summary["texts"]:
        passages=run/"texts"/text["source_id"]/"extraction"/"passages.jsonl"
        for line in passages.read_text(encoding="utf-8").splitlines():
            if line.strip():
                source.add((run_name,text["source_id"],json.loads(line)["occurrence_id"]))
assert reported == source, (len(reported-source),len(source-reported))
print(f"Matched {len(reported)} report/source occurrence identities")
for item in report:
    print(item["anchor"], item["occurrence_id"])
PY
```

Review every translation against its original, especially negated/embedded
cases; verify larger context is useful but visibly AI-generated and uncertain
where needed; ensure commentary explains rather than restates scores; and check
all provenance links. Do not accept a report with boilerplate, fabricated plot
claims, missing cases, or passages that are too large or clipped through a
target.

## 11. Security scan and staging review

Raw requests/responses are normal audit artifacts in this repository, but they
must be scanned. Logs and prepared request files are reproducible operational
artifacts and are not staged below. Cache attempts are staged because they are
the persistent model-call audit trail; inspect their contents first.

```bash
cd "$LMCW"
find scripts/reporting -type d -name __pycache__ -prune -exec rm -rf {} +
python scripts/security/scan_credentials.py \
  prompts/corpus_report \
  scripts/reporting \
  "$REPORT_ROOT"
rm -f \
  "$REPORT_ROOT/$REPORT_NAME.offline.log" \
  "$REPORT_ROOT/$REPORT_NAME.generation.log" \
  "$REPORT_ROOT/$REPORT_NAME.rerun.log"
rm -rf "$REPORT_ROOT/$REPORT_NAME/work"
git status --short
```

## 12. Commit and push the accepted report

Stage named implementation, report, summary, and cache artifacts only. Do not
blindly stage the entire results tree.

```bash
cd "$LMCW"
git add \
  prompts/corpus_report/enrich_occurrence_v0_1.md \
  prompts/corpus_report/enrichment_schema_v0_1.json \
  scripts/reporting/__init__.py \
  scripts/reporting/build_corpus_report.py \
  scripts/reporting/render_corpus_report.py \
  scripts/reporting/validate_corpus_report.py \
  scripts/reporting/test_corpus_report.py \
  docs/howto/14_build_canonical_corpus_report.md \
  "$REPORT_JSON" \
  "$REPORT_MD" \
  "$REPORT_SUMMARY" \
  "$REPORT_ROOT/cache"
git diff --cached --check
git diff --cached --stat
python scripts/security/scan_credentials.py \
  prompts/corpus_report \
  scripts/reporting \
  "$REPORT_JSON" \
  "$REPORT_MD" \
  "$REPORT_SUMMARY" \
  "$REPORT_ROOT/cache"
python -m pytest -q
git commit -m 'Add canonical eight-work corpus inspection report'
git push origin HEAD
git status --short
```

If a cache directory contains an artifact not suitable for the public
repository, unstage it, document why, and retain it securely outside Git rather
than losing the audit record.

## 13. Stop before Step 15

Share the complete Markdown and JSON reports, summary JSON, validation output,
zero-call rerun evidence, rerender comparison, test output, total recorded cost,
and any uncertain translations/context. Stop for review. Do not ingest the
purchased indie-romance files until this report is accepted.
