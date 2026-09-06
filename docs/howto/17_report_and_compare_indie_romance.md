# Step 17: report and compare the indie-romance pilot

This runbook uses the accepted Step 14 report machinery and accepted Step 16
v0.3.1 annotations. It produces an indie inspection report and a descriptive
genre comparison. It does not perform significance testing, add texts, revise
annotations, or encode claims about literary quality.

## 1. Preflight

```bash
cd "$LMCW"
git pull --ff-only
test -z "$(git status --short)" || {
  echo 'Working tree is not clean; stop and review it.' >&2
  exit 1
}
python -m pytest -q
test -f results/corpus_reports/canonical_eight_v0_3_1.json
python -m json.tool results/corpus_reports/canonical_eight_v0_3_1.json >/dev/null
```

Select the exact accepted `indie_romance_three_v1` batch run. Confirm its three
works, occurrence total, annotation version `0.3.1`, and complete audit. Do not
use a mutable “latest” selection.

## 2. Generate the indie report

Run the corpus-report command offline first. Because all three works are
English, translation must be `null` and no translation call is needed. Review
cache identities, missing enrichment count, prompt payloads, model/pricing, and
estimated cost. Then enrich only missing/stale items and render:

```text
results/corpus_reports/indie_romance_three_v1_v0_3_1.md
results/corpus_reports/indie_romance_three_v1_v0_3_1.json
```

Rerun without force and confirm no repeated valid model calls. Read every
occurrence and verify source passage, context, immutable scores, confidence,
commentary, utterance status, and provenance. Explicit or sexual contexts must
remain present when the extraction found them.

## 3. Implement a deterministic descriptive comparison

The comparison command must consume saved structured report/run data and make
no model calls. Define the two groups explicitly:

- canonical literary fiction/drama: the eight works in `development_three` and
  `multilingual_five_v1`;
- contemporary indie romance: the three works in
  `indie_romance_three_v1`.

For each group and, where useful, each work, report:

- works and occurrences;
- complete distributions for P, T, E, and O scores;
- P >= 2 and E >= 2 counts and proportions (state the denominator);
- mixed P/T/E count and proportion, with “mixed” defined in output metadata;
- ontology-fit distribution;
- direct-affirmative versus embedded/reported, negated, quoted/revoiced,
  hypothetical/other-marked counts and proportions.

Categories may overlap, so label them as non-exclusive where applicable. Do not
force unknown status into “direct.” Surface missing/unknown fields and ensure
every occurrence contributes to each applicable denominator exactly once.
Include input paths/hashes, generation time, definitions, and code version.

Write both:

```text
results/corpus_reports/canonical_vs_indie_romance_three_v1.md
results/corpus_reports/canonical_vs_indie_romance_three_v1.json
```

Do not run inferential significance tests in this pilot. Describe observed
differences with raw counts and proportions, not causal or population-level
claims.

## 4. Test and review the hypotheses symmetrically

Add fixture tests for zero denominators, unknown/overlapping statuses, score
boundaries, mixed-case definition, deterministic ordering, and reconciliation
of totals. Verify recomputation from identical inputs is byte-stable apart from
an explicitly isolated generation timestamp.

Interpret all live outcomes without preference: more P, more E, continuing T
dominance, more mixed cases, or credible O cases. Reinspect surprising cases
before proposing ontology changes. Use only the neutral corpus labels above;
do not frame the result as good/bad literature or use taste-coded metadata.

```bash
cd "$LMCW"
python -m json.tool results/corpus_reports/indie_romance_three_v1_v0_3_1.json >/dev/null
python -m json.tool results/corpus_reports/canonical_vs_indie_romance_three_v1.json >/dev/null
python -m pytest -q
python scripts/security/scan_credentials.py
git status --short
```

Stop and share both indie report files, both comparison files, tests, cache and
cost summary, missing-data inventory, and a compact list of unexpected P, E, O,
mixed, non-natural-fit, and low-confidence cases. The next decision is whether
the exploratory contrast justifies a larger genre-controlled corpus; do not
acquire further titles in this run.
