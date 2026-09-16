# Extract the fifteen-work expansion

This step deterministically extracts broadened lexical `LOVE(I,YOU)` candidates
from only the fifteen expansion works. It creates no AI review or annotation.
Stop after committing the extraction inventory so that its counts and contexts
can be inspected.

## 1. Validate patterns and inheritance

```bash
cd "$LMCW"
python -m pytest -q scripts/extraction
python -m pytest -q scripts/extraction/test_extract_canonical_corpus.py \
  -k inherited_language_definitions_are_exactly_equal
python scripts/corpus/validate_canonical_corpus.py corpus/works
```

The corpus validator must report `Canonical corpus valid: 31 work(s).` (A warning
about the unavailable local/private McMillan file is expected on machines that
do not hold it.)

## 2. Run the filtered extraction

```bash
rm -rf results/extraction/expansion_15_v0_8
python scripts/extraction/extract_canonical_corpus.py \
  --patterns data/development/search_patterns_v0_8.json \
  --work-manifest data/canonicalization/expansion_15_v1/manifest.json \
  --output results/extraction/expansion_15_v0_8
```

## 3. Validate outputs and counts

```bash
python - <<'PY'
import json
from pathlib import Path
p = Path("results/extraction/expansion_15_v0_8")
m = json.loads((p / "manifest.json").read_text(encoding="utf-8"))
assert m["run_id"] == "expansion_15_v0_8"
assert m["pattern_version"] == "0.8"
assert (m["works_requested"], m["works_attempted"], m["works_extracted"]) == (15, 15, 15)
assert len(list((p / "works").glob("*/summary.json"))) == 15
assert len(list((p / "works").glob("*/candidates.jsonl"))) == 15
print(json.dumps(m, indent=2))
PY

python - <<'PY'
import json
from pathlib import Path
for path in sorted(Path("results/extraction/expansion_15_v0_8/works").glob("*/summary.json")):
    row = json.loads(path.read_text(encoding="utf-8"))
    print(f"{row['work_id']}\t{row['language']}\t{row['candidate_count']}")
PY
```

## 4. Inspect Danish and Italian candidates

```bash
python - <<'PY'
import json
from pathlib import Path
root = Path("results/extraction/expansion_15_v0_8/works")
for work_id in ("bang-ved-vejen", "nansen-maria"):
    print("\n#", work_id)
    for line in (root / work_id / "candidates.jsonl").read_text(encoding="utf-8").splitlines():
        row = json.loads(line); print(row["pattern_id"], repr(row["match"]))
PY

python - <<'PY'
import json
from pathlib import Path
root = Path("results/extraction/expansion_15_v0_8/works")
for work_id in ("zuccoli-lamore-di-loredana", "verona-colei-che-non-si-deve-amare"):
    print("\n#", work_id)
    for line in (root / work_id / "candidates.jsonl").read_text(encoding="utf-8").splitlines():
        row = json.loads(line); print(row["pattern_id"], repr(row["match"]))
PY
```

## 5. Inspect diagnostics

Zero yield is a review flag, not an extraction failure. High-count flags likewise
require inspection rather than automatic suppression.

```bash
python - <<'PY'
import json
p = "results/extraction/expansion_15_v0_8/summary.json"
d = json.load(open(p, encoding="utf-8"))
print(json.dumps(d["diagnostics"], indent=2))
PY
sed -n '1,80p' results/extraction/expansion_15_v0_8/summary.md
```

## 6. Verify and commit explicitly

```bash
python scripts/docs/validate_runbook_index.py
git diff --check
git status --short
git diff -- data/development/search_patterns_v0_8.json scripts/extraction \
  docs/howto/35_extract_expansion_fifteen.md docs/howto/README.md \
  results/extraction/expansion_15_v0_8

git add data/development/search_patterns_v0_8.json
git add scripts/extraction/extract_canonical_corpus.py \
  scripts/extraction/test_extract_canonical_corpus.py
git add results/extraction/expansion_15_v0_8
git add docs/howto/35_extract_expansion_fifteen.md docs/howto/README.md
git commit -m "Extract LOVE candidates from fifteen expansion works"
```

## 7. Post-commit verification and stop

```bash
git status --short
git show --stat --oneline HEAD
python -m pytest -q scripts/extraction
```

Stop here. Do not run model calls, assign KEEP/EXCLUDE decisions, retrieve wider
context, translate passages, or begin T/P/E/O annotation.
