# Recovering substantial quotations with accent transcription differences

The v3 C07 B repeat 2 E quotation and C07 B repeat 1 O quotation both changed
чтò to чтó in the same long sentence. Retrying the first failure produced a
new annotation with P=3 instead of the original P=2. A transcription rejection
therefore changes the sample as well as costing another call. This motivates
separating auditable passage alignment from a claim of verbatim accuracy.

The updated matcher applies to both v2 and v3. It first checks verbatim matching,
then whitespace-only matching. If those fail, an accent-only alignment is allowed
when all of the following hold:

- The whitespace-normalized quotation is at least 40 characters and six words.
- Folding combining marks on Latin, Cyrillic or Greek letters yields exactly one
  matching occurrence in the named source block.
- NFC-normalized submitted and source passages have the same length and differ
  at no more than two character positions, at most 5% of the alphabetic characters.
- All other characters, including case and punctuation, match.

These thresholds are conservative engineering choices, not empirically calibrated
error rates. Uniqueness is checked within the named block. A distinctive accented
word can still affect meaning inside a long sentence: the alignment establishes
which source passage is being cited, not semantic equivalence of every word.
The source version must be used when reproducing the quotation in scholarship.
Short quotations, target identity and anchor checks remain strict. No global
source normalization, word substitutions or fuzzy edit-distance matching is used.
Original requests, model responses, output quotations and scores are unchanged.
The v1 runner retains its existing whitespace-only acceptance rule.

New or recovered calls receive quotation_audit.json with the matching class,
submitted quotation, exact source substring, offsets into the unmarked source
block and accent differences. The current matching policy is recorded in new
provenance. Historical frozen protocols and provenance are not rewritten.

Existing accepted outputs are preserved. Recovery selects the first valid retained
attempt only for calls that do not already have an accepted output. Superseded
responses, including the first C07 B repeat 2 attempt, are audited but never
silently substituted for accepted retries. Use these records for sensitivity
analysis of retry effects, reporting any alternative selection explicitly.

Apply the patch on top of the v3 clarification patch, then:

```bash
python -m unittest scripts.context_pilot.test_quotation_matching
python scripts/context_pilot/run_pilot.py --protocol v2 --audit-saved-quotes
python scripts/context_pilot/run_pilot.py --protocol v2 --scope full_text --cases C05 C06 --audit-saved-quotes
python scripts/context_pilot/run_pilot.py --protocol v3 --recover-saved --audit-saved-quotes
python scripts/context_pilot/run_pilot.py --protocol v3 --scope full_text --cases C05 C06 --audit-saved-quotes
```

No API calls occur in these commands. With the reported local state, v3 dossier
should recover C07 B repeat 1 and show 13 resumable calls, leaving 83. The already
accepted C07 B repeat 2 retry remains selected. The audit of all retained attempts
is quotation_attempt_audit.json in each run directory. It includes valid superseded
responses, selected status, scores and any still-invalid attempts with errors.

Then resume:

```bash
python scripts/context_pilot/run_pilot.py --protocol v3 --run &&
python scripts/context_pilot/run_pilot.py --protocol v3 --scope full_text --cases C05 C06 --run &&
python scripts/context_pilot/compare_p_prompts.py
```

After completion, repeat the four no-API audit commands above to refresh the full
attempt inventories. The comparison script uses the same updated validator.
If another genuinely invalid attempt occurs, inspect it before using --retry-failed.

In addition to the v3 check-in list, stage:

```bash
git add scripts/context_pilot/quotation_matching.py \
  scripts/context_pilot/test_quotation_matching.py \
  scripts/context_pilot/run_pilot.py \
  docs/notes/context_pilot_accent_alignment.md \
  results/context_pilot/v2_dossier/quotation_attempt_audit.json \
  results/context_pilot/v2_full_text/quotation_attempt_audit.json
```

The existing recursive v3 result-directory additions include new call audits and
attempt inventories. No downloaded patch or uploaded attachment needs committing.
