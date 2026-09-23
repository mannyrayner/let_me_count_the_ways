# Clarifying P: a fixed comparison against completed v2

This experiment follows inspection of the v2 results. Some responses acknowledge
an existing obligation but give P=0 because no new promise is made. Others treat
neighbouring commitment language as categorically separate from the focal
expression. We test whether clarifying these two points changes judgments and
their explanations. This is an exploratory, post-v2 prompt revision, not a
preregistered confirmation or independent validation of the categories.

## Fixed design

Use all eight existing dossier cases (96 calls) and the two whole-play Lear
cases (24 calls). All A/B/C/D evidence, target markers, reference identities,
three repetitions, call ordering, model alias, response schema and planned
8000-token output ceiling are unchanged. Keep the full set so that changes on
suspected cases can be compared with changes on the other cases. No cases are
added or removed based on their v3 scores.

Only the instruction text about P and its relation to surrounding speech is
changed. `classify_v3.md` retains the old heading to avoid even an unnecessary
version cue in the request. The saved protocol and result directory identify
v3 unambiguously. The schema name also remains context_pilot_v2; its contents
are identical. The existing selection_v2.json remains the source selection.

P can involve creating, renewing, affirming or invoking an obligation. A new
promise is not required, and contextual commitment need not be explicitly
spelled out inside the extracted match. Conversely, description of a duty,
affection, a relationship or a neighbouring promise does not automatically
establish that the target itself has undertaking force. The classifier must
explain the connection. There are no named literary examples or desired scores
in the revised prompt. T/E/O definitions, uncertainty rules, identity validation,
quotation checks, sincerity distinctions and treatment of later events are
unchanged.

## Install, prepare and test

Apply `context_pilot_p_clarification_v3.patch` from the repository root:

```bash
git apply --check context_pilot_p_clarification_v3.patch &&
git apply context_pilot_p_clarification_v3.patch
python scripts/context_pilot/run_pilot.py --protocol v3
python scripts/context_pilot/run_pilot.py --protocol v3 --scope full_text --cases C05 C06
python -m unittest scripts.context_pilot.test_target_grounding scripts.context_pilot.test_p_prompt_comparison
python scripts/context_pilot/compare_p_prompts.py
```

These commands make no API calls. Initially the comparison reports v2 complete,
v3 zero, and awaiting_v3. Comparison checks both saved plans and input objects;
accepted results must also match their retained API responses and provenance.

## Run the new variant

```bash
python scripts/context_pilot/run_pilot.py --protocol v3 --run &&
python scripts/context_pilot/run_pilot.py --protocol v3 --scope full_text --cases C05 C06 --run &&
python scripts/context_pilot/compare_p_prompts.py
```

The completed v2 baseline is reused, not called again. The two new runs need
96 and 24 calls. Each resumes its own accepted results if interrupted. Inspect
retained failures before adding --retry-failed. The initial estimates using the
repository's dated pricing snapshot and the full output ceiling are about
USD 18.54 and USD 5.43; these are planning heuristics, not predicted charges.
No model calls have been made while preparing this patch.

Outputs:

- `results/context_pilot/v3_dossier/summary.md` and `summary.json`
- `results/context_pilot/v3_full_text/summary.md` and `summary.json`
- `results/context_pilot/comparison_v2_v3/dossier/summary.md` and `summary.json`
- `results/context_pilot/comparison_v2_v3/full_text/summary.md` and `summary.json`

The comparison Markdown shows every case/condition's P scores and median
change. JSON also includes T/E/O, counts, missingness and original-output paths.
Median differences are withheld unless both groups have three assessable
judgments. Null means insufficient evidence; pending results are never zero.
The model still needs to justify every score with supplied source evidence.

## How to interpret the comparison

Review reasons as well as numbers. In particular:

1. Does a P=0 explanation still treat absence of a new promise as sufficient?
2. Does a nonzero P explanation identify what the speaker affirms or undertakes,
   and how that force belongs to the focal utterance in context?
3. Does the model still separate truth-conditional force from sincerity, and
   correctly retain speaker and addressee throughout its explanations?
4. Does added context change interpretations consistently across repetitions,
   or mainly shift the model's application of the P definition?
5. Are changes selective, or does the clarification raise P broadly without
   stronger evidence? Inspect A and the previously low-P cases too.

A higher P score is not in itself an improvement. Both versions' outputs stay
available; do not replace the baseline or silently pool the protocols. T/E/O
scores may change despite unchanged definitions because classifications are
made jointly in one response; report those changes too.

This is a sequential comparison against an existing baseline, not interleaved
random assignment of prompts. Sampling variation and model-alias/backend drift
remain possible explanations. Repetitions are not additional independent
literary cases. The small purposive sample cannot establish corpus prevalence.

## Check in after review

```bash
git add .gitattributes \
  prompts/context_pilot/classify_v3.md \
  scripts/context_pilot/run_pilot.py \
  scripts/context_pilot/compare_p_prompts.py \
  scripts/context_pilot/test_p_prompt_comparison.py \
  docs/notes/context_pilot_p_clarification_v3.md \
  docs/howto/45_read_cases_and_run_context_pilot.md \
  results/context_pilot/v3_dossier results/context_pilot/v3_full_text \
  results/context_pilot/comparison_v2_v3
git diff --cached --stat
git commit -m "Compare clarified P instructions with context pilot v2"
git push origin main
```

The downloaded patch is not part of the research data and need not be committed.
