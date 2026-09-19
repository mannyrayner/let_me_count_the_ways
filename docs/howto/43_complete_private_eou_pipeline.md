# Complete the private EoU pipeline

This runbook is for Manny to execute on the authorized local machine. It takes
Stella McMillan's *Error of Understanding* through v0.11 extraction, scholarly
membership review, frozen KEEP selection, wide-context enrichment, and v0.3.1
T/P/E/O annotation, then prepares a passage-specific publication-permission
request. **Do not run any part of this workflow in a coding-agent environment.**

Everything produced here is private: source text, candidates, review decisions,
contexts, annotations and explanations, distributions, interpretive notes,
proposed quotations, and permission documents. Do not paste them into issues,
pull requests, public logs, public runbooks, or publication-oriented chats. Do
not commit them. Existing permission covers private academic analysis only;
publication of specific excerpts requires explicit written author approval.

The commands below intentionally place every generated file under
`results/private_eou_v0_11/`. Run sections in order and stop at every stated
failure condition.

## 1. Verify private paths before writing anything

Start from a cleanly understood checkout, but do not discard unrelated work:

```bash
cd "$LMCW"
git status --short

PRIVATE_ROOT=results/private_eou_v0_11
PRIVATE_TEXT=data/local_candidate_derived/mcmillan-error-of-understanding/text.txt
WORK_ID=mcmillan-error-of-understanding
EXPECTED_SHA256=b941746d22087c6cfc9e9634880d0f950db8017de786077c37fdfc643f880839

git check-ignore -v "$PRIVATE_TEXT" "$PRIVATE_ROOT"
test "$(git check-ignore "$PRIVATE_TEXT" "$PRIVATE_ROOT" | wc -l)" -eq 2 || {
  printf 'STOP: the private source and output root must both be Git-ignored.\n' >&2
  exit 1
}
```

If either path is not ignored, **STOP**. Do not add a public exception. Only
after both checks succeed, create the private layout:

```bash
mkdir -p \
  "$PRIVATE_ROOT"/{extraction,review,frozen,enrichment,annotation,publication_permission}
```

## 2. Verify the canonical source

Do not inspect or extract an unverified file:

```bash
test -f "$PRIVATE_TEXT" || {
  printf 'STOP: missing private canonical source: %s\n' "$PRIVATE_TEXT" >&2
  exit 1
}
ACTUAL_SHA256=$(sha256sum "$PRIVATE_TEXT" | awk '{print $1}')
printf '%s  %s\n' "$ACTUAL_SHA256" "$PRIVATE_TEXT"
test "$ACTUAL_SHA256" = "$EXPECTED_SHA256" || {
  printf 'STOP: canonical hash mismatch.\n' >&2
  exit 1
}
```

## 3. Extract one work under v0.11

The seven v0.7 candidates are a historical baseline, not an inventory to
migrate. Make a private one-work selector and invoke the canonical extractor;
do not alter `search_patterns_v0_11.json` and do not implement another
extractor. New occurrence IDs must arise naturally from v0.11 and the current
offsets.

```bash
cat > "$PRIVATE_ROOT/extraction/work_selector.json" <<'JSON'
{"works":["mcmillan-error-of-understanding"]}
JSON

python scripts/extraction/extract_canonical_corpus.py \
  --patterns data/development/search_patterns_v0_11.json \
  --work-manifest "$PRIVATE_ROOT/extraction/work_selector.json" \
  --output "$PRIVATE_ROOT/extraction/metadata" \
  --private-output "$PRIVATE_ROOT/extraction"

PRIVATE_CANDIDATES="$PRIVATE_ROOT/extraction/works/$WORK_ID/candidates.jsonl"
test -f "$PRIVATE_CANDIDATES"
```

Print only non-quoting counts. Do not print matches or contexts:

```bash
python - "$PRIVATE_CANDIDATES" <<'PY'
import json, sys
from collections import Counter
from pathlib import Path

rows = [json.loads(line) for line in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines() if line]
assert all(row["work_id"] == "mcmillan-error-of-understanding" for row in rows)
assert all(str(row["pattern_version"]) == "0.11" for row in rows)
assert len({row["occurrence_id"] for row in rows}) == len(rows)
print("v0.7 historical candidate count: 7")
print("v0.11 current candidate count:", len(rows))
print("counts by pattern_id:", dict(sorted(Counter(r["pattern_id"] for r in rows).items())))
print("counts by form_family:", dict(sorted(Counter(r.get("form_family", "unspecified") for r in rows).items())))
PY
```

The historical detail is six `present` and one `negative_present`. A different
v0.11 total is not itself an error; inspect the delta locally. Inspect the
private JSONL with `less "$PRIVATE_CANDIDATES"` for recall/precision sanity,
valid offsets, and parser damage. Never copy its output publicly. If extraction
is defective, **STOP** before review or annotation.

## 4. Review every v0.11 candidate from scratch

Use model alias `5.6` and the unchanged public-corpus prompt and schema. The
question is exactly whether the candidate genuinely instantiates explicit
lexical LOVE(first-person singular experiencer, second-person
target/addressee). Decisions are `KEEP`, `EXCLUDE`, or `UNCERTAIN`, using the
existing reason-code ontology. Do not classify T/P/E/O at this stage and do not
migrate v0.7 decisions.

```bash
python scripts/review/scholarly_candidate_review.py run \
  --candidates "$PRIVATE_ROOT/extraction" \
  --output "$PRIVATE_ROOT/review" \
  --prompt prompts/review/scholarly_candidate_review_v1.md \
  --schema prompts/review/scholarly_candidate_review_schema_v1.json \
  --model 5.6

CANDIDATE_COUNT=$(python - "$PRIVATE_CANDIDATES" <<'PY'
import sys
print(sum(bool(line.strip()) for line in open(sys.argv[1], encoding="utf-8")))
PY
)
python scripts/review/scholarly_candidate_review.py validate \
  --candidates "$PRIVATE_ROOT/extraction" \
  --review "$PRIVATE_ROOT/review" \
  --expected-total "$CANDIDATE_COUNT"
python scripts/review/scholarly_candidate_review.py render \
  --candidates "$PRIVATE_ROOT/extraction" \
  --review "$PRIVATE_ROOT/review" \
  --output "$PRIVATE_ROOT/review" \
  --include-private-in-sheet
python scripts/review/scholarly_candidate_review.py freeze \
  --candidates "$PRIVATE_ROOT/extraction" \
  --review "$PRIVATE_ROOT/review" \
  --output "$PRIVATE_ROOT/frozen"
```

Validation requires exactly one valid review per extracted candidate. Confirm
the frozen manifest accounts for all decisions, including exclusions retained
in the review tree, and stop on any uncertainty:

```bash
python - "$PRIVATE_ROOT/review/summary.json" "$PRIVATE_ROOT/frozen/manifest.json" <<'PY'
import json, sys
review, frozen = (json.load(open(path, encoding="utf-8")) for path in sys.argv[1:])
assert review["candidate_count"] == review["KEEP"] + review["EXCLUDE"] + review["UNCERTAIN"]
assert frozen["candidate_count"] == frozen["review_count"] == review["candidate_count"]
assert frozen["KEEP"] == review["KEEP"] and frozen["UNCERTAIN"] == review["UNCERTAIN"]
print({key: review[key] for key in ("candidate_count", "KEEP", "EXCLUDE", "UNCERTAIN")})
if review["UNCERTAIN"]:
    raise SystemExit("STOP: Manny/ChatGPT must inspect UNCERTAIN cases; never promote them silently")
PY
```

## 5. Enrich and validate the private KEEP set

The canonical enrichment uses approximately ±3000 characters expanded outward
to paragraph boundaries. Its private-output switch preserves rights checks
rather than weakening them globally. EoU is English, so every translation must
be null and no translation API stage is needed.

```bash
python scripts/annotation/enrich_canonical_candidates.py \
  --reviewed "$PRIVATE_ROOT/frozen/kept_candidates.jsonl" \
  --output "$PRIVATE_ROOT/enrichment/enriched.jsonl" \
  --private-output

python - "$PRIVATE_ROOT/enrichment/enriched.jsonl" "$EXPECTED_SHA256" <<'PY'
import hashlib, json, sys
from pathlib import Path

rows = [json.loads(line) for line in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines() if line]
expected = sys.argv[2]
for row in rows:
    occurrence = row["occurrence"]
    assert occurrence["canonical_sha256"] == expected
    assert row["review"]["decision"] == "KEEP"
    assert row["work_metadata"]["language"] == "en"
    assert row["translation"] is None
    assert occurrence["match"] == row["context"]["local"]["text"][
        occurrence["start"] - row["context"]["local"]["context_start"]:
        occurrence["end"] - row["context"]["local"]["context_start"]
    ]
    wide = row["context"]["wide"]
    assert wide["policy"] == "radius_3000_expanded_outward_to_paragraph_boundaries"
    hashlib.sha256(wide["text"].encode("utf-8")).hexdigest()
assert len({r["occurrence"]["occurrence_id"] for r in rows}) == len(rows)
print("validated private enriched KEEP records:", len(rows))
PY

# Prove a second deterministic enrichment has identical wide-context hashes.
python scripts/annotation/enrich_canonical_candidates.py \
  --reviewed "$PRIVATE_ROOT/frozen/kept_candidates.jsonl" \
  --output "$PRIVATE_ROOT/enrichment/enriched.recheck.jsonl" \
  --private-output
python - "$PRIVATE_ROOT/enrichment/enriched.jsonl" "$PRIVATE_ROOT/enrichment/enriched.recheck.jsonl" <<'PY'
import hashlib, json, sys

def hashes(path):
    rows = [json.loads(line) for line in open(path, encoding="utf-8") if line.strip()]
    return {
        row["occurrence"]["occurrence_id"]:
        hashlib.sha256(row["context"]["wide"]["text"].encode("utf-8")).hexdigest()
        for row in rows
    }

assert hashes(sys.argv[1]) == hashes(sys.argv[2])
print("wide-context hashes stable")
PY
rm "$PRIVATE_ROOT/enrichment/enriched.recheck.jsonl"
```

The enrichment command itself verifies the manifest/canonical hash, reproduces
the match and local context from offsets, and derives deterministic wide
contexts. Re-run the validation after any regeneration; unchanged input must
produce stable wide context and hashes.

## 6. Estimate, run, and complete v0.3.1 annotation

Use the unchanged `classify_passage_v0_3_1.md`,
`classification_schema_v0_3.json`, and `validate_v0_3` contract selected by the
canonical runner. Estimate first and inspect `estimate.json`. If the total or
cost is unexpectedly high for this small work, **STOP** rather than calling the
API blindly.

```bash
python scripts/annotation/annotate_canonical_candidates.py \
  --enriched "$PRIVATE_ROOT/enrichment/enriched.jsonl" \
  --all --output "$PRIVATE_ROOT/annotation" --model 5.6 \
  --estimate-only
cat "$PRIVATE_ROOT/annotation/estimate.json"
```

After accepting the estimate, run the first pass at the default 300-second
timeout. Progress is printed per occurrence and successful fingerprinted
artifacts are resumable:

```bash
python scripts/annotation/annotate_canonical_candidates.py \
  --enriched "$PRIVATE_ROOT/enrichment/enriched.jsonl" \
  --all --output "$PRIVATE_ROOT/annotation" --model 5.6
```

Inspect `failures.json`. If and only if every remaining failure is a
request/transport timeout, rerun the same command and output directory with
`--timeout 600`, then if necessary `--timeout 1200`. Never delete successful
artifacts. Do not use a longer timeout to mask schema, parsing, or validation
failures; **STOP** on those.

Require a complete run before preparing any permission request:

```bash
python - "$PRIVATE_ROOT/frozen/manifest.json" "$PRIVATE_ROOT/annotation/usage.json" "$PRIVATE_ROOT/annotation/summary.json" <<'PY'
import json, sys
frozen, usage, summary = (json.load(open(path, encoding="utf-8")) for path in sys.argv[1:])
keep = frozen["KEEP"]
assert usage["requested"] == keep
assert usage["valid"] == keep
assert usage["failed"] == 0
assert usage["status"] == "complete"
assert summary["requested"] == keep and len(summary["cases"]) == keep
print("complete private annotations:", keep)
PY
```

## 7. Create and inspect the private research summary

Create a local-only summary from the extraction, review, and annotation JSON.
It must include the v0.11 raw, KEEP, EXCLUDE, and UNCERTAIN counts; T, P, E, and
O distributions; utterance-status and ontology-fit distributions; and
priority-review count. The annotation `summary.json` already contains these
distributions and `review_cases.json` contains cases flagged for `O > 0`,
`E >= 2`, `P >= 2`, confidence below 0.75, non-natural ontology fit, or at
least two T/P/E dimensions at 2 or above. Store the combined human-readable
record under the private root; do not publish even its aggregates.

```bash
python - "$PRIVATE_ROOT/review/summary.json" "$PRIVATE_ROOT/annotation/summary.json" "$PRIVATE_ROOT/annotation/review_cases.json" "$PRIVATE_ROOT/private_summary.json" <<'PY'
import json, sys

review, annotation, priority = (
    json.load(open(path, encoding="utf-8")) for path in sys.argv[1:4]
)
summary = {
    "v0.11_raw_candidate_count": review["candidate_count"],
    "KEEP": review["KEEP"],
    "EXCLUDE": review["EXCLUDE"],
    "UNCERTAIN": review["UNCERTAIN"],
    "T_distribution": annotation["distributions"]["T"],
    "P_distribution": annotation["distributions"]["P"],
    "E_distribution": annotation["distributions"]["E"],
    "O_distribution": annotation["distributions"]["O"],
    "utterance_status_distribution": annotation["distributions"]["utterance_status"],
    "ontology_fit_distribution": annotation["distributions"]["ontology_fit"],
    "priority_review_count": len(priority),
}
with open(sys.argv[4], "w", encoding="utf-8") as stream:
    json.dump(summary, stream, indent=2, ensure_ascii=False)
    stream.write("\n")
print("wrote private summary; inspect it locally and do not publish its values")
PY
```

Locally inspect every priority case and a sample of ordinary unflagged cases.
Use the private enriched records and per-attempt annotation outputs where the
source context or explanation is needed. Do not paste inspection output into a
public transcript.

## 8. Select only publication-worthy passages

Do not request every occurrence. Select the smallest useful set whose members
materially support a prospective paper point: a clear T/P/E contrast, strong
performative case, expressive/reflexive case, ontology-stressing example,
illuminating canonical-literature contrast, or meaningful contemporary-romance
pattern. For each selection record its occurrence ID, chapter/section if
available, source start/end offsets, exact minimally necessary quotation, word
count, surrounding identifying description, analytical rationale, and why
direct quotation is necessary. Do not default to the full wide context.

## 9. Build the private permission package

Create
`publication_permission/request_manifest.json` with the work ID, author
publication name `Stella McMillan`, contact name `Beverly Bree`, research
permission `GRANTED`, overall publication permission `PENDING`, null request
and response dates, and the selected passages. Each passage entry must contain
the fields listed above and begin with per-passage permission `PENDING`.

Create `publication_permission/request_passages.md` as an independent readable
record. For every passage include passage ID, location, exact quotation, word
count, analytical rationale, and why direct quotation matters.

Finally create `publication_permission/draft_email.md` for Manny's review. Use
the subject “Permission to quote passages from Error of Understanding in our
research paper” and a friendly, concise, non-pressuring message to Beverly. It
must:

- thank her again for permitting private academic analysis;
- say that the study is now considering an eventual paper;
- request explicit permission for the exact, individually listed quotations;
- briefly explain the research point for each passage;
- invite approval of all, some, or none, and offer to shorten or omit any;
- promise not to reproduce other substantial text without asking again; and
- state that without permission, all EoU-specific material stays private and
  EoU will be omitted from the published analysis.

Sign as Manny Rayner, adding only author/research details that are already
settled. Do not fabricate an affiliation or venue. **Do not send the email.**

## 10. Permission-state rules

Silence is not approval. Keep overall and per-passage status `PENDING` until an
explicit written response arrives. Then record the response date, overall
status, notes/conditions, and each passage as `APPROVED`,
`APPROVED_WITH_MODIFICATION`, `DECLINED`, or `PENDING`. For a required
shortening, record the approved shortened wording exactly. Publish only
individually approved passages; never infer permission for related text.

If permission is declined, retain the analysis as a legitimate private
methodological case study and omit all EoU-specific results from publication.
Even if permission is granted, a later handoff—not this runbook—must decide
which approved quotations or aggregate results to promote and create any
public-safe provenance.

## 11. Final privacy audit and stop

Verify the source and every private artifact remain ignored, compare status to
the initial status, and ensure no private path is staged:

```bash
git check-ignore -v "$PRIVATE_TEXT" "$PRIVATE_ROOT"
test "$(git check-ignore "$PRIVATE_TEXT" "$PRIVATE_ROOT" | wc -l)" -eq 2
git status --short
git diff --cached --name-only
test -z "$(git diff --cached --name-only | rg 'private_eou|local_candidate_derived|mcmillan-error-of-understanding' || true)"
```

Stop when extraction, review, freezing, enrichment, complete annotation,
private summary, passage selection, manifest, readable passage appendix, and
draft email are complete and ignored. **STOP for Manny/ChatGPT inspection of
the private results and permission draft before Manny sends anything.** No
EoU-specific result, quotation, aggregate, paper text, figure, or public status
marker is produced by this runbook.
