# Humanities paper: working draft v0.4

Current source: [let_me_count_the_ways.tex](let_me_count_the_ways.tex). References: [references.bib](references.bib). Revision notes: [CHANGELOG.md](CHANGELOG.md).

The existing draft's cases can now be read in the [human-readable collection](../../reader/README.md).
The [context-study protocol](../../notes/context_study_v1.md) records the next empirical questions;
its pending results have not been inserted into this historical draft.

## Build the paper

From this directory, with a TeX distribution containing pdfLaTeX, BibTeX, latexmk, Latin Modern, natbib, microtype, xurl and the usual LaTeX packages:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error let_me_count_the_ways.tex
```

Alternatively:

```bash
pdflatex let_me_count_the_ways.tex
bibtex let_me_count_the_ways
pdflatex let_me_count_the_ways.tex
pdflatex let_me_count_the_ways.tex
```

The default PDF contains the article, references and corpus inventory. For the additional research notes and 21-record source register, change `\includesupplementfalse` to `\includesupplementtrue` and rebuild. Return the switch to false for the normal reading copy.

All generated TeX files are committed, so the sources also compile outside the full corpus repository. PDF and temporary TeX outputs are ignored by Git. The downloadable draft bundle includes a compiled reading copy.

## Reproduce the tables

From the repository root:

```bash
python docs/paper/humanities/build_tables.py --check
```

To regenerate, omit `--check`. Python 3 and Git are the only requirements. The script performs no network requests or model calls.

The script reads Git objects at **ef7ea7933d8aa02b176d8fbddc496e55a41a7144**, rather than whatever happens to be in the current working tree. This snapshot contains:

- Original stage: 225 retained occurrences, 30 public works, extraction v0.11.
- Targeted extension: 27 retained occurrences, five works, extraction v0.12.
- Classification prompt v0.3.1 throughout; original scores and rationales unchanged.

`generated/statistics.json` records score distributions, thresholds 2/3/4, direct-speech subsets, work counts and input hashes. `case_selection.json` identifies the cases discussed; `generated/case_register.json` records their exact inputs and outputs. These close readings are purposively selected, not an independent validation sample.

A source-only download can compile using the generated files. To recompute them, run the script inside a full repository checkout or pass `--repo /path/to/let_me_count_the_ways`.

## Record a new draft

1. Edit the same LaTeX and BibTeX files.
2. Update the working-draft version/date and add a concise entry to `CHANGELOG.md`.
3. If the evidence changes, explicitly update the data snapshot/run definitions and regenerate the tables. Do not silently replace the historical scores.
4. Compile and check the PDF. Run the table check.
5. Commit the paper directory, then push when ready to share.

For example, from the repository root:

```bash
git add docs/paper
git diff --cached --stat
git commit -m "Revise humanities paper to v0.5: clarify commitment and uptake"
git push origin main
```

Use a commit message describing the intellectual change. To find or compare drafts:

```bash
git log --oneline -- docs/paper/humanities
git diff OLD_COMMIT NEW_COMMIT -- docs/paper/humanities
```

Git history preserves v0.3 and v0.4 in the installation patch. To inspect an earlier version without changing the current files, use a separate worktree:

```bash
git worktree add ../lmcw-earlier-draft OLD_COMMIT
```

For a circulated milestone, an optional annotated tag such as `humanities-v0.4` can make the commit easy to find. Tag the actual manuscript commit, and push that tag explicitly. No tag is required for ordinary edits.

## Editorial status

This is a working draft for discussion, not a completed independent validation study. [research_notes.tex](research_notes.tex) records unresolved methodological choices. [SOURCE_CHECKS.md](SOURCE_CHECKS.md) records quotation checks and the distinction between scored records and external illustrations.
