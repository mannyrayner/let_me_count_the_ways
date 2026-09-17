# Search-pattern changes in v0.11

Version 0.11 starts from v0.10 and makes only two targeted precision changes.

## German: case-sensitive formal `Sie`

The common target alternation in `de_negative_perfect`, `de_perfect`, `de_main`,
and `de_subordinate` now represents the targets as `dich`, `euch`, and
case-sensitive `(?-i:Sie)`. The enclosing patterns remain case-insensitive.
This prevents lowercase third-person `sie` from being treated as formal
second-person `Sie` while retaining orthographic flexibility elsewhere.

The motivating false positives were `ich liebe sie noch` and `ich liebe sie so
wie du` in *Effi Briest*, and `Sie weiß, wie ich sie liebe!` in *Werther*.
Those three candidates are removed; `dich`, `euch`, and uppercase `Sie` remain
supported in main and subordinate word order (and where applicable in the
perfect patterns).

## French: split future and conditional metadata

The v0.10 `fr_future_conditional` pattern is split into constrained `fr_future`
and `fr_conditional` patterns. `aimerai` remains `tense_aspect: future`;
`aimerais` is now `tense_aspect: modal` with `modality: conditional`.
Attested examples such as `je t'aimerai` and `Je vous aimerais` retain candidate
membership; only their pattern identity and, for conditionals, metadata change.
