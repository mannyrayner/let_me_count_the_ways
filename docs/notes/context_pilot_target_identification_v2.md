# Context pilot v2: correcting target identification

The first dossier pilot contains five judgments filed as Goneril (C05) whose
explanations instead analyse Cordelia. They are C05 C repeats 1 and 3, and C05 D
repeats 1, 2 and 3. The source scene contains both speakers; an unmarked TARGET
string did not reliably identify the intended occurrence. Quotation validation
alone could not detect this because Cordelia's words really occur in that scene.

The retained audit is `results/context_pilot/audits/v1_target_attribution.json`.
It records paths, content hashes, original scores and verbatim diagnostic
explanations. These five judgments must not support a context-effect claim for
Goneril. They must not be relabelled as Cordelia judgments either. All original
requests, attempts, outputs and summaries remain unchanged. The audit is an AI
close reading available for human review, not independent human adjudication.

## What changes

`selection_v2.json` preserves all eight cases, source hashes, target and context
spans, three repetitions and the shuffle seed. It adds reviewed speaker and
addressee labels with the textual basis for each attribution. B/C/D receive:

- Markers around the exact extracted target, inserted by character offsets.
- Reviewed speaker and addressee labels, with an exact source anchor excerpt.
- An instruction to keep that utterance as the subject of every score and explanation.

The anchor is not necessarily a whole speech turn and does not change the
expression being classified. It is already present in the supplied scene.
Condition A receives only the original extracted expression, empty source
blocks and a null reference. No character names, work title, source offsets or
reference anchor are added to A. Its response must leave speaker and addressee
null; recognition can still be reported separately.

The response schema puts target identification before scores. Validation checks
its speaker, addressee and anchor against the supplied reference. Evidence
quotes must match actual source text, ignoring only whitespace and removing
editorial markers from the input before comparison. Incorrect attribution
stops the run and retains the failed attempt for inspection. A correct identity
field is not proof that every sentence of an explanation is correctly grounded;
the explanations still need review, especially the two Lear cases.

The definitions of T/P/E/O and the instruction about neighbouring promises are
unchanged. This repair does not test a broader definition of P. Supplying verified
identities is a methodological change, not simply a formatting correction; v1
and v2 must remain distinct. No conclusions about a context effect follow from
v2 until its new judgments have been collected and reviewed.

All 120 calls are fresh, including A, to keep the revised instruction/schema
uniform. v1 results cannot resume as v2. The default v2 output ceiling is 8000;
retries retain their original responses. No automatic paid retry is introduced.
The source and publication decision for the rose case are read from the existing
public export, so an ignored local copy is not required for v2.

## Prepare and inspect (no API calls)

```bash
python -m unittest scripts.context_pilot.test_target_grounding
python scripts/context_pilot/run_pilot.py --protocol v2
python scripts/context_pilot/run_pilot.py --protocol v2 --scope full_text --cases C05 C06
```

Expect 96 dossier calls and 24 whole-play Lear calls, initially zero resumable.
Open these files in a browser to inspect the exact model evidence and reference:

- `results/context_pilot/v2_dossier/inputs/C05/B.html` — Goneril's first I love you.
- `results/context_pilot/v2_dossier/inputs/C06/B.html` — Cordelia's I love your majesty.
- `results/context_pilot/v2_dossier/README.md` — links to all eight cases.

A page's human-facing heading names its case; that heading is not sent to the
model. The adjacent JSON file is the model's evidence object. The instruction
prompt is `prompts/context_pilot/classify_v2.md`.

## Collect fresh judgments

```bash
python scripts/context_pilot/run_pilot.py --protocol v2 --run
python scripts/context_pilot/run_pilot.py --protocol v2 --scope full_text --cases C05 C06 --run
```

Run sequentially. Each command is resumable: repeat it after an interruption.
If an attempt failed validation, inspect its retained response before explicitly
adding `--retry-failed`. Use `--max-calls 4` for a first small batch if desired.
With the checked-in model configuration, the initial conservative estimates are
about USD 18.38 and USD 5.39 respectively, using the entire 8000-token output
ceiling for every call. These are planning heuristics, not predicted bills or
verified current prices; the preflight prints the pricing snapshot date.

Summaries are at:

- `results/context_pilot/v2_dossier/summary.md` and `summary.json`
- `results/context_pilot/v2_full_text/summary.md` and `summary.json`

The JSON includes each accepted response's target identification and a link to
its complete output. The Markdown table reports P as before. Inspect the full
T/P/E/O values and explanations before interpreting score changes.

Full-text scope still includes the canonical work's front matter; this repair
does not strip it. Dossier versus full-text comparisons therefore differ in
which text is supplied as well as its amount. The cases are purposively selected;
repetitions are model judgments, not additional independent literary occurrences.

## Check in

After reviewing the completed runs:

```bash
git add .gitattributes \
  data/context_pilot/selection_v2.json \
  prompts/context_pilot/classify_v2.md prompts/context_pilot/schema_v2.json \
  scripts/context_pilot/run_pilot.py scripts/context_pilot/target_grounding.py \
  scripts/context_pilot/test_target_grounding.py \
  docs/howto/45_read_cases_and_run_context_pilot.md \
  docs/notes/context_pilot_target_identification_v2.md \
  results/context_pilot/audits/v1_target_attribution.json \
  results/context_pilot/v2_dossier results/context_pilot/v2_full_text
git diff --cached --stat
git commit -m "Correct context-pilot target identification and record v2 judgments"
git push origin main
```

Do not add the downloaded installation patch or force-add private directories.
The same file list can be committed before collecting responses, with a commit
message describing prepared inputs rather than completed judgments.
