# Initial pipeline runbooks

These runbooks follow the C-LARA-2 operating convention: use persistent Cygwin
environment variables, keep the checkout under `/home/github`, expose small
top-level commands, and stop for review after each step.

Run one document at a time. Each runbook ends at a review checkpoint; share the
named outputs and agree changes before proceeding.

**This table is the authoritative runbook sequence. Every numbered Markdown
file directly under `docs/howto/` must appear exactly once in this table.
Unlinked numbered runbooks are not permitted, and repository validation enforces
this invariant.**

When adding a runbook, choose the next step number, add the file, and update the
table in the same commit. Run the mechanical inventory from the repository root:

```bash
python scripts/docs/validate_runbook_index.py
```

Obsolete runbooks are removed from the current tree rather than archived
in-place because Git history already preserves them.

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
| 14 | [Build the eight-work corpus report](14_build_canonical_corpus_report.md) | Cached enrichment contract and inspectable Markdown/JSON report for all eight canonical works |
| 15 | [Ingest the one-work indie-romance pilot](15_ingest_indie_romance_pilot.md) | Preserved *Nikki's Touch* EPUB, reproducible Calibre text, exclusions, and reviewed rights/provenance |
| 16 | [Extract and annotate the indie-romance pilot](16_annotate_indie_romance_pilot.md) | Reviewed *Nikki's Touch* extraction and complete audited v0.3.1 pilot batch |
| 17 | [Report and compare the pilot](17_report_and_compare_indie_romance_pilot.md) | One-work pilot inspection report and descriptive canonical-versus-indie comparison |
| 18 | [Triage three local romance candidates](18_triage_local_romance_candidates.md) | Local-only, reproducible conversion, extraction inventory, and retain/drop recommendations |
| 19 | [Acquire and reconnoitre the classical six](19_acquire_and_reconnoitre_classical_six.md) | Six verified original-language sources and reviewed extraction-only occurrence inventories |
| 20 | [Annotate the classical six](20_annotate_classical_six.md) | KEEP-only, resumable v0.3.1 annotations joined to definitive AI-review provenance |
| 21 | [Build enriched case studies](21_build_enriched_case_studies.md) | Validated narrative, ontology, translation, and reader-facing case-study artifacts |
| 22 | [Create the canonical corpus pilot](22_create_canonical_corpus_pilot.md) | Three validated canonical works and the generated corpus index |
| 23 | [Migrate the original development three](23_migrate_development_three_to_canonical_corpus.md) | Six validated canonical works, including the three original development works |
| 24 | [Migrate three multilingual works](24_migrate_multilingual_three_to_canonical_corpus.md) | Nine validated canonical works, including Ibsen, Rostand, and Strindberg |
| 25 | [Migrate the remaining multilingual-five works](25_migrate_remaining_multilingual_five_to_canonical_corpus.md) | Eleven validated canonical works, completing the historical multilingual-five batch |
| 26 | [Migrate Pan and Women in Love](26_migrate_pan_and_women_in_love_to_canonical_corpus.md) | Thirteen validated canonical works, including the next two classical-six works |
| 27 | [Complete the existing canonical corpus](27_complete_existing_canonical_corpus.md) | Sixteen validated research works, including one hash-verified local/private canonical source and its rights-review reminder |
| 28 | [Extract the broadened canonical corpus](28_extract_broadened_canonical_corpus.md) | Public-safe multilingual candidate inventories and counts for human inspection |
| 29 | [Extract the private McMillan text locally](29_extract_private_mcmillan_text.md) | Private context-bearing candidates and a public-safe non-quoting count summary |
| 30 | [Run the provisional AI scholarly review](30_ai_scholarly_review_canonical_candidates.md) | Resumable public/private AI membership decisions pending human review |
| 31 | [Acquire the fifteen-work corpus expansion](31_acquire_expansion_fifteen.md) | Fifteen verified source acquisitions, or an exact blocked inventory |
| 32 | [Repair and audit Runeberg acquisition](32_repair_audit_runeberg_acquisition.md) | Repaired Undset derivations, repository-wide prefix audit, and resolved provenance warnings |
| 33 | [Canonicalize the expansion fifteen locally](33_canonicalize_expansion_fifteen_locally.md) | Fifteen locally generated canonical works, deterministic special derivations, and a 31-work validated corpus |
| 34 | [Complete special canonical provenance](34_complete_special_canonical_provenance.md) | Complete source and transformation provenance links for the two specially derived canonical works |
| 35 | [Extract the fifteen-work expansion](35_extract_expansion_fifteen.md) | Deterministic Danish/Italian-aware candidate inventories and diagnostics for fifteen works |
| 36 | [Audit recall and extract with v0.9](36_audit_recall_and_extract_v0_9.md) | Cross-linguistic recall audit, bounded exclusive-target patterns, and full-corpus deterministic extraction |
| 37 | [Finalize and freeze extraction v0.10](37_finalize_extraction_v0_10.md) | Targeted multilingual recall repairs, inspected v0.9 delta, and frozen deterministic candidates |
| 38 | [Finalize extraction precision and freeze v0.11](38_finalize_extraction_v0_11.md) | German case-sensitive formal address, corrected French metadata, inspected delta, and frozen deterministic candidates |
| 39 | [Review and calibrate canonical annotation](39_review_and_calibrate_canonical_annotation.md) | Uniform v0.11 membership review, frozen KEEP set, canonical enrichment, and an eight-case v0.3.1 calibration |
| 40 | [Annotate the full canonical KEEP set](40_annotate_full_canonical_keep_set.md) | Resumable translations, enrichment, and T/P/E/O annotations for all 225 public KEEP candidates |
| 41 | [Prepare full annotation inputs locally](41_prepare_full_annotation_inputs.md) | Validated full enrichment and a bounded annotation estimate, with no annotation API calls |
| 42 | [Run the full canonical annotation locally](42_run_full_canonical_annotation_locally.md) | Complete resumable 225-case annotations, empty failures, and priority-review inventory |
| 43 | [Complete the private EoU pipeline](43_complete_private_eou_pipeline.md) | Private v0.11 EoU extraction/review/annotation and a local publication-permission request package |
| 44 | [Commitment extension](44_extend_commitment_corpus.md) | Acquire and annotate five additional works |

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
