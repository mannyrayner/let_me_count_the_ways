# Step 11: annotate *Little Women* and *Madame Bovary* with v0.2

The reviewed dry runs contain four *Little Women* occurrences and twelve
*Madame Bovary* occurrences. Inspection found no obvious false positive:

- the English cases are first-person declarations directed to “you,” including
  parental/filial and romantic contexts;
- the French cases are direct `je t’aime` or `je vous aime` constructions;
- repeated declarations in one passage have distinct source spans and should
  remain distinct occurrences; and
- line-broken matches preserve the source while satisfying the intended
  whitespace-tolerant patterns.

This step resumes the exact dry-run directories. It does not re-extract or
create a new experiment. Do not use `--force`, and do not change annotation
v0.2 in response to an interesting result.

## Set and verify the run directories

```bash
cd "$LMCW"
LITTLE_WOMEN_RUN='results/pipeline_runs/gutenberg-514/20260902T043336Z'
MADAME_BOVARY_RUN='results/pipeline_runs/gutenberg-14155/20260902T043409Z'

python - "$LITTLE_WOMEN_RUN" 4 "$MADAME_BOVARY_RUN" 12 <<'PY'
import json
import sys
from pathlib import Path

for index in range(1, len(sys.argv), 2):
    run_dir = Path(sys.argv[index])
    expected = int(sys.argv[index + 1])
    manifest = json.loads((run_dir / "manifest.json").read_text(encoding="utf-8"))
    summary = json.loads((run_dir / "summary.json").read_text(encoding="utf-8"))
    assert manifest["status"] == "prepared", (run_dir, manifest["status"])
    assert manifest["dry_run"] is True, run_dir
    assert manifest["annotation_version"] == "0.2", run_dir
    assert manifest["search_pattern_version"] == "0.2", run_dir
    assert manifest["extracted_occurrences"] == expected, run_dir
    assert manifest["valid_occurrences"] == 0, run_dir
    assert summary["model_calls_needed"] == expected, run_dir
    print(f"Prepared run passed: {run_dir} ({expected} calls pending)")
PY

test -n "${OPENAI_API_KEY:-}" || {
  echo 'OPENAI_API_KEY is not set; stop before annotation.' >&2
  exit 1
}
```

## Annotate *Little Women*

Resume the four-occurrence run:

```bash
python scripts/pipeline/run_single_text_pipeline.py \
  provenance/sources/gutenberg-514.json \
  --patterns data/development/search_patterns_v0_2.json \
  --annotation-version 0.2 \
  --model 5.6 \
  --run-dir "$LITTLE_WOMEN_RUN"
```

The trace should show four annotation attempts followed by `Pipeline complete`.
Audit every preserved valid output against v0.2, scan the full run for possible
credentials, and inspect the summary and report:

```bash
python scripts/pipeline/audit_pipeline_run.py \
  "$LITTLE_WOMEN_RUN" --expected-occurrences 4
python scripts/security/scan_credentials.py "$LITTLE_WOMEN_RUN"
python -m json.tool "$LITTLE_WOMEN_RUN/manifest.json"
python -m json.tool "$LITTLE_WOMEN_RUN/summary.json"
sed -n '1,320p' "$LITTLE_WOMEN_RUN/report.md"
```

If the audit fails or the manifest status is `partial`, stop and inspect
`$LITTLE_WOMEN_RUN/failures` and the relevant numbered attempt directories. Do
not use `--force`. A later normal resume retries only occurrences without a
compatible valid result and preserves the earlier attempts.

When the audit and credential scan pass, check in the whole run:

```bash
test -z "$(git diff --cached --name-only)" || {
  echo 'The index already contains staged files; review or unstage them first.' >&2
  exit 1
}
git add "$LITTLE_WOMEN_RUN"
git diff --cached --check
git diff --cached --stat
git status --short
git commit -m 'Record Little Women v0.2 pipeline run'
git push origin HEAD
git status --short
```

## Annotate *Madame Bovary*

Only after the *Little Women* run has been audited and preserved, resume the
twelve-occurrence French run:

```bash
python scripts/pipeline/run_single_text_pipeline.py \
  provenance/sources/gutenberg-14155.json \
  --patterns data/development/search_patterns_v0_2.json \
  --annotation-version 0.2 \
  --model 5.6 \
  --run-dir "$MADAME_BOVARY_RUN"
```

Audit, scan, and inspect it:

```bash
python scripts/pipeline/audit_pipeline_run.py \
  "$MADAME_BOVARY_RUN" --expected-occurrences 12
python scripts/security/scan_credentials.py "$MADAME_BOVARY_RUN"
python -m json.tool "$MADAME_BOVARY_RUN/manifest.json"
python -m json.tool "$MADAME_BOVARY_RUN/summary.json"
sed -n '1,480p' "$MADAME_BOVARY_RUN/report.md"
```

As above, stop on `partial`, failed audit, or a credential finding. Otherwise
preserve the complete run:

```bash
test -z "$(git diff --cached --name-only)" || {
  echo 'The index already contains staged files; review or unstage them first.' >&2
  exit 1
}
git add "$MADAME_BOVARY_RUN"
git diff --cached --check
git diff --cached --stat
git status --short
git commit -m 'Record Madame Bovary v0.2 pipeline run'
git push origin HEAD
git status --short
```

## Review checkpoint

After both complete runs are pushed, create two working review documents from
the common template:

```bash
cp docs/notes/next_text_diagnostic_review_template.md \
  docs/notes/little_women_v0_2_diagnostic_review.md
cp docs/notes/next_text_diagnostic_review_template.md \
  docs/notes/madame_bovary_v0_2_diagnostic_review.md
```

Do not fill the reviews by counting only the Markdown highlights. Review the
complete structured outputs and relevant passages. Accumulate ontology pressure
across both works before proposing any v0.2 revision. The next development task
is to complete these two diagnostic reviews and then make the provisional
three-text comparison with *Jane Eyre*.
