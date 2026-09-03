# Initial pipeline runbooks

These runbooks follow the C-LARA-2 operating convention: use persistent Cygwin
environment variables, keep the checkout under `/home/github`, expose small
top-level commands, and stop for review after each step.

Run one document at a time. Each runbook ends at a review checkpoint; share the
named outputs and agree changes before proceeding.

The table below is authoritative. Some checkouts may temporarily retain older,
unlinked runbooks from the first draft; they can be ignored while repository
history is cleaned up and do not block the current sequence.

| Step | Runbook | Result to review |
| --- | --- | --- |
| 0 | [Configure Cygwin](00_configure_cygwin.md) | Persistent environment variables |
| 1 | [Check out and verify](01_checkout_and_verify.md) | Checkout and passing checks |
| 2 | [Configure a model and generate targets](02_configure_model_and_generate_targets.md) | Priced model snapshot and raw candidates |
| 3 | [Review and approve targets](03_review_targets.md) | Versioned approved manifest |
| 4 | [Acquire one approved text](04_acquire_one_text.md) | Raw text and provenance draft |
| 5 | [Extract passages](05_extract_passages.md) | Occurrence JSONL |
| 6 | [Classify one passage](06_classify_one_passage.md) | Costed structured AI analysis |
| 7 | [Classify diagnostic passages](07_classify_diagnostic_passages.md) | Quoted, imagined, and sisterly pilot analyses |
| 8 | [Complete Jane Eyre v0.1](08_complete_jane_eyre_v0_1.md) | All six comparable v0.1 analyses |
| 9 | [Run the single-text pipeline](09_run_single_text_pipeline.md) | Dry-run inputs, then a resumable text-level annotation run |
| 10 | [Acquire and dry-run the next texts](10_acquire_and_dry_run_next_texts.md) | Verified *Little Women* and *Madame Bovary* sources and inspected dry runs |
| 11 | [Annotate the next texts with v0.2](11_annotate_next_texts_v0_2.md) | Complete, audited *Little Women* and *Madame Bovary* v0.2 runs |
| 12 | [Run manifest-defined annotation batches](12_run_annotation_batches.md) | Reusable, resumable multi-text annotation and version comparison |
| 13 | [Annotate the multilingual five-text batch](13_annotate_multilingual_five_v0_3_1.md) | Acquired sources, reviewed extraction inventories, and a complete audited v0.3.1 batch |

## Conventions

- `LMCW` points to `C:\cygwin64\home\github\let_me_count_the_ways`, the sister
  checkout to C-LARA-2. Every later runbook begins with `cd "$LMCW"`.
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
