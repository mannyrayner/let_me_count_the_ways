# Context pilot output-budget amendment, 2026-09-22

C02/D/repeat 2 returned status=incomplete and reason=max_output_tokens at the
2400-token ceiling. API usage reports 1692 reasoning tokens within those 2400
output tokens. The JSON stops in its final limitations string and cannot be
recovered as a complete judgment. Sixteen earlier judgments were accepted.

The runner now exposes --max-output-tokens for new attempts. Its default remains
2400 for compatibility. The operational recommendation for the remaining pilot
calls is 8000. The original failed attempt is retained; retrying makes a new call.

Install the patch after context_pilot_whitespace_fix.patch, then run:

```bash
python scripts/context_pilot/run_pilot.py --max-output-tokens 8000
python scripts/context_pilot/run_pilot.py --run --retry-failed --max-output-tokens 8000
```

The estimate uses the selected ceiling for every remaining call; it is a
conservative output allowance rather than a prediction of actual usage. The
existing estimate guard still applies. API charges follow actual usage.

Original plan files, call directories and plan fingerprints remain unchanged,
so successful judgments resume without any API call or alteration. Each new
attempt saves its actual request (including its ceiling). Its accepted provenance
adds max_output_tokens and actual_request_sha256, separately from the original
plan fingerprint. This is an explicit attempt-level execution amendment, not a
claim that the modified request is byte-identical to the original plan.

The prompt, evidence, model and schema are unchanged. The budget changed partway
through execution; report this in the methods and retain budget metadata when
examining results. Increasing the ceiling does not guarantee identical model
behavior or unlimited completion. A fully uniform-budget replication would be a
separate run, not an overwrite of the current pilot.

Incomplete API responses are now detected before JSON parsing and receive an
explicit diagnostic. --recover-saved never accepts an incomplete response. For
complete saved responses, recovery permits only an increased output ceiling as
a difference from the original planned request; changes to the prompt, evidence,
model or any other request field are rejected.

Nine pilot tests pass, including mixed-budget resumption without repeated API
calls, recovery preservation, and rejection of incompatible requests. The
truncation diagnostic was also verified against the actual supplied response.
