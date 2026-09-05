# Step 14: build the eight-work corpus inspection report

This runbook defines the next implementation increment: a human-readable report
over `development_three` and `multilingual_five_v1`. Complete and review this
machinery before ingesting the indie-romance sources. The report stage explains
existing annotations; it must never change P/T/E/O scores or discard negated,
embedded, reported, quoted, revoiced, hypothetical, or otherwise marked hits.

## 1. Preflight and freeze the inputs

```bash
cd "$LMCW"
git pull --ff-only
test -z "$(git status --short)" || {
  echo 'Working tree is not clean; stop and review it.' >&2
  exit 1
}
python -m pytest -q
python -m json.tool data/batches/development_three.json >/dev/null
python -m json.tool data/batches/multilingual_five_v1.json >/dev/null
test -f prompts/annotation/classify_passage_v0_3_1.md
test -f prompts/annotation/classification_schema_v0_3.json
```

Record the exact completed v0.3.1 batch-run directories selected for the
report. Do not silently select “latest” if more than one completed run exists.
The intended current inputs are the three development works and five
multilingual works named by those manifests.

## 2. Implement a separate, versioned enrichment contract

Add a corpus-report enrichment prompt and JSON schema under a distinct prompt
namespace (for example `prompts/corpus_report/`). The structured response must
contain only presentational fields:

- an idiomatic English translation for non-English passages, with the target
  visibly marked and genuine ambiguity retained;
- an AI-generated larger-context summary, including uncertainty rather than
  speculative plot claims;
- one synthetic interpretive paragraph that explains the scores without merely
  copying the annotation analysis.

English occurrences should use `null` for translation, not incur a translation
call. The contract must explicitly prohibit revised scores, labels, confidence,
ontology fit, and utterance status. Validate the schema and prompt version in
tests.

## 3. Implement deterministic assembly and a persistent cache

Create a report command that accepts explicit batch-run paths and a report
name. It should:

1. read preserved source, extraction, annotation, run, prompt, model, and
   provenance records;
2. retain every extracted and annotated occurrence;
3. reuse annotation fields wherever possible;
4. cache each enrichment under an identity containing occurrence ID, exact
   model ID, enrichment prompt version/hash, schema version/hash, and the hashes
   of the relevant source/annotation inputs;
5. reuse a valid cached result by default and regenerate only missing, invalid,
   stale, or explicitly forced entries;
6. assemble Markdown and JSON without a model call once the cache is complete;
7. write atomically beneath `results/corpus_reports/`.

Do not key only on occurrence ID: that would incorrectly reuse an enrichment
after its prompt, model, passage, or annotation changed. Preserve requests,
responses, usage/cost, validation, and errors consistently with pipeline runs.
A failed enrichment must remain diagnosable and must not yield a falsely
complete report.

The JSON is the durable presentation model. Markdown must be rendered from that
JSON-equivalent structure, so another format can later be generated without
new AI calls. HTML is optional for this increment.

## 4. Required report contents

The report header must identify its input batches/runs, generation time,
enrichment version/model, annotation version(s), and completeness counts. Add
linked indices, without duplicating occurrence bodies, for:

- work and language;
- P >= 2, E >= 2, and O > 0;
- ontology fit other than `natural`;
- negated;
- embedded/reported;
- quoted/revoiced;
- low confidence.

Use stable, collision-resistant anchors derived from occurrence IDs.

Each occurrence must show ID, title, author, language, source ID, approximate
position, utterance status, a bounded original passage, translation when
needed, clearly labelled AI-generated context and commentary, P/T/E/O scores,
confidence, ontology fit, ambiguity note, and compact provenance pointers.
Escape Markdown metacharacters where source content could break structure.

Status groupings should use preserved structured annotation/extraction fields.
If a requested distinction is not represented structurally, display it as
`unknown` and report the data gap; do not infer it with a brittle substring
test or omit the occurrence.

## 5. Test before spending API credit

Add fixtures covering English/non-English records, every index category,
duplicate-looking IDs from different runs, Markdown-sensitive text, missing
optional fields, invalid cache entries, and a failed enrichment. Tests must
prove that:

- assembly does not mutate annotations;
- no occurrence disappears;
- cache hits cause no API call;
- prompt/model/input changes invalidate the cache;
- rerendering from saved JSON causes no API call;
- output ordering and anchors are deterministic.

```bash
cd "$LMCW"
python -m pytest -q
python scripts/security/scan_credentials.py
```

## 6. Dry-run, estimate, and generate

Expose `--help`, an offline/dry-run mode, and an explicit force-enrichment
option. Use the implemented command's actual flags rather than copying a
hypothetical invocation from this design document.

First run offline assembly. It should report the selected runs, occurrence
count, cache hits/misses, calls required, and incomplete inputs without making
API calls. Review the complete prompt payload for representative English,
French, German, Norwegian, and Swedish cases. Confirm the annotation block is
input-only and absent from the enrichment output schema.

After approving the exact model and cost estimate, fill the missing cache and
generate:

```text
results/corpus_reports/canonical_eight_v0_3_1.md
results/corpus_reports/canonical_eight_v0_3_1.json
```

Validate the JSON, rerun without force, and confirm zero additional model calls.

## 7. Human review checkpoint

Read every occurrence in Markdown. Check translations against originals,
context summaries against the supplied passage and known plot, commentary
against immutable scores, all links/anchors, all unusual-case indices, and
provenance pointers. Reconcile the report occurrence total with the two source
batch runs.

Stop here and share the Markdown report, JSON report, cache-hit/miss summary,
cost summary, test output, and any data gaps. Do not begin purchased-source
ingestion until this checkpoint is accepted.
