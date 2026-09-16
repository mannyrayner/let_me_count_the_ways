# Runeberg cross-domain debugging example

This is an internal note for later drafting, not polished publication prose.

Human inspection first identified what appeared to be unusually poor OCR in
*Kristin Lavransdatter*. AI-assisted comparison of the assembled Norwegian text
with retained Runeberg HTML showed that the discontinuities aligned with page
boundaries. Inspection of the Python acquisition code then established that it
always discarded content before the first `<br>` in raw-OCR regions.

Comparison with Hamsun's *Victoria* explained why the original rule had seemed
reasonable: the same structural position often contains a printed Arabic page
number there. In Undset, however, Norwegian linguistic coherence and the raw
page structure showed that it frequently contained genuine literary text. The
diagnosis therefore combined HTML/source-format analysis, Python acquisition
reasoning, page-layout and OCR knowledge, and Norwegian-language competence.
That diagnosis led directly to a narrow deterministic rule—discard digits-only
prefixes and preserve everything else—and a repository-wide audit. It does not
imply that all apparent OCR defects have this cause, nor does it correct source
OCR.

> A single AI collaborator can sometimes integrate competencies that, in a conventional research workflow, might be distributed across several specialists. This can substantially reduce the coordination cost of diagnosing problems that sit at disciplinary or technical boundaries.
