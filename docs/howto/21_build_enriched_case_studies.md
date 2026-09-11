# Build enriched literary case studies

The case-study pipeline keeps frozen annotations separate from deterministic evidence preparation
and separately versioned AI enrichment. Run it from the repository root. Selection accepts repeatable
score/confidence/fit criteria, explicit IDs (`--occurrence-id`), and top-N rules (`--top P:5`).

## Classical-six pilot reproduction

```bash
python scripts/case_studies/select_cases.py --batch-root results/batch_runs/classical_six_v1/v0.3.1-5.6 --review results/reconnaissance/classical_six_v1/reviewed_occurrences.json --criterion 'O>0' --criterion 'E>=2' --criterion 'P>=2' --output results/case_studies/classical_six_v1/selection.json
python scripts/case_studies/prepare_case_context.py --selection results/case_studies/classical_six_v1/selection.json --output-root results/case_studies/classical_six_v1 --rights-policy PUBLIC_DOMAIN_FULL_CONTEXT_OK
OPENAI_API_KEY='your-key' python scripts/case_studies/enrich_case_studies.py --case-root results/case_studies/classical_six_v1 --model 5.6
python scripts/case_studies/render_case_studies.py --case-root results/case_studies/classical_six_v1 --output results/case_studies/classical_six_v1/critical_case_studies.md --title 'Classical Six: Critical Literary Case Studies'
python scripts/case_studies/validate_case_studies.py --selection results/case_studies/classical_six_v1/selection.json --case-root results/case_studies/classical_six_v1 --dossier results/case_studies/classical_six_v1/critical_case_studies.md
```

Valid artifacts with matching source, prompt, and model fingerprints are skipped. Changed inputs archive
the prior artifact before replacement. A narrative `INSUFFICIENT_CONTEXT` result is retained for audit;
widen the deterministic context and retry. The pilot's checked-in enrichments were generated in the
interactive GPT-5.6 Sol session, so their records explicitly report unavailable usage and zero separately
metered API cost rather than inventing token or price data.

## Rights decisions

Choose one explicit policy during preparation: `PUBLIC_DOMAIN_FULL_CONTEXT_OK`,
`PERMISSIONED_CONTEXT_OK`, `LIMITED_QUOTATION_ONLY`, or `NO_PUBLIC_RENDER`. Preparation remains possible
under every policy. The renderer refuses non-publishable policies; a future rights-specific excerpt adapter
must implement limited quotation before public output.

## Checkpoint commands for Manny

These commands inspect precisely this checkpoint and never use `git add .`:

```bash
sed -n '1,240p' results/case_studies/classical_six_v1/critical_case_studies.md
cat results/case_studies/classical_six_v1/cost_coverage_summary.json
python -m unittest discover -s scripts -p 'test_*.py'
python scripts/case_studies/validate_case_studies.py --selection results/case_studies/classical_six_v1/selection.json --case-root results/case_studies/classical_six_v1 --dossier results/case_studies/classical_six_v1/critical_case_studies.md
python scripts/security/scan_credentials.py prompts/case_studies results/case_studies/classical_six_v1
git status --short
git add prompts/case_studies scripts/case_studies docs/howto/21_build_enriched_case_studies.md results/case_studies/classical_six_v1
git diff --cached --check
git diff --cached --stat
git diff --cached -- prompts/case_studies scripts/case_studies docs/howto/21_build_enriched_case_studies.md
git commit -m "Add reusable enriched literary case studies"
git status --short
git show --stat --oneline --decorate HEAD
```
