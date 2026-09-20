# Project papers

The humanities-facing manuscript is in [humanities](humanities/).

Keep stable source filenames. Use Git commits to preserve successive drafts.
This first manuscript commit imports the supplied working draft v0.3, dated
19 September 2026, and its existing optional research notes. The LaTeX and
BibTeX files are byte-for-byte copies of the supplied attachments.

Compile in `docs/paper/humanities` with `pdflatex`, `bibtex`, then two further
`pdflatex` passes on `let_me_count_the_ways`. The research notes are optional;
set the manuscript's `includesupplement` switch to true to append them.
