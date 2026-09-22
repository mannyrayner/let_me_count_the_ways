# Context pilot: whitespace-only evidence matching

On 2026-09-22, the first run stopped at C02/C/repeat 2 because the model replaced
a line break with a space in two otherwise verbatim quotations. All other quotes
matched exactly. The validator was stricter than necessary for source layout.

The validator now collapses whitespace on both sides when checking whether a
quotation occurs in its named source block. Case, spelling, punctuation, word
order and block identity remain significant. It performs no fuzzy matching,
translation, paraphrase acceptance or text correction.

The protocol's prompt, inputs, request fingerprints and returned scores are
unchanged. New accepted calls record the validation policy
`literal_quote_whitespace_normalized_v1` in provenance. Previously accepted
calls remain unchanged. The original literal-substring requirement in the prompt
is also unchanged; this is a documented validation tolerance for layout, not a
new instruction to the annotator.

To recover an already saved, otherwise valid response without another API call:

```bash
python scripts/context_pilot/run_pilot.py --recover-saved
```

This checks the saved request against the current plan, validates the original
response and writes output/provenance if it passes. It retains the original
request, response, costs and failure record unchanged. Recovery is idempotent;
it does not overwrite accepted judgments. It selects the earliest valid retained
attempt deterministically. Responses that still fail are not promoted.

After the reported C02 failure, expect one recovered response and two resumable
calls. Complete the original four-call checkpoint with:

```bash
python scripts/context_pilot/run_pilot.py --run --max-calls 2
```

Then complete the pilot:

```bash
python scripts/context_pilot/run_pilot.py --run
```

No retry flag is needed for the recovered C02 call. Other failed responses still
require inspection and, if necessary, an explicit paid retry. The validation
change was checked against the actual uploaded response and seven pilot tests,
including rejection of changed punctuation, spelling case, order and block
identity, and preservation of original failed attempts during recovery.
