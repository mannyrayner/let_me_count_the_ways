# Initial pipeline runbooks

These runbooks follow the C-LARA-2 operating convention: use persistent Cygwin
environment variables, keep the checkout under `/home/github`, expose small
top-level commands, and stop for review after each step.

Run one document at a time. Each runbook ends at a review checkpoint; share the
named outputs and agree changes before proceeding.

| Step | Runbook | Result to review |
| --- | --- | --- |
| 0 | [Configure Cygwin](00_configure_cygwin.md) | Persistent environment variables |
| 1 | [Check out and verify](01_checkout_and_verify.md) | Checkout and passing checks |
| 2 | [Configure a model and generate targets](02_configure_model_and_generate_targets.md) | Priced model snapshot and raw candidates |
| 3 | [Review and approve targets](03_review_targets.md) | Versioned approved manifest |
| 4 | [Acquire one approved text](04_acquire_one_text.md) | Raw text and provenance draft |
| 5 | [Extract passages](05_extract_passages.md) | Occurrence JSONL |
| 6 | [Classify one passage](06_classify_one_passage.md) | Costed structured AI analysis |

## Conventions

- `LMCW` points to `C:\cygwin64\home\github\LMCW`, the sister checkout to
  C-LARA-2. Every later runbook begins with `cd "$LMCW"`.
- `OPENAI_API_KEY` is the existing global credential shared by OpenAI-based
  projects. Commands check it but never print it or place it on the command line.
- Every API top-level command takes `--model ALIAS`; the alias resolves to an
  exact API identifier and a human-verified pricing snapshot in
  `config/api_models.json`.
- API runs retain token usage, estimated USD cost, the pricing snapshot, exact
  request, raw response, prompt/input/schema hashes, and errors.
- Do not commit downloads or model outputs until provenance, licensing, and the
  research role have been reviewed.
- If a command fails, stop and retain its run directory for diagnosis.
