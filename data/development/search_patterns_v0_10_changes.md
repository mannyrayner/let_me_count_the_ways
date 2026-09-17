# Search-pattern changes in v0.10

Version 0.10 is a targeted extension of v0.9. It changes only the five languages below; Danish and every other language are byte-for-structure identical to their v0.9 language entries. No generic LOVE–target proximity rule was added.

| Language | Pattern ID | Motivating corpus occurrence | Class | Precision constraint |
| --- | --- | --- | --- | --- |
| French | `fr_perfect` | `je vous ai assez aimée`; `je vous ai aimée depuis le premier jour` | Compound perfect with bounded adverbial/postverbal material and feminine participle | Requires `je`, an immediately governed `te`/`t’`/`vous` clitic, `ai`, at most one enumerated adverb, and optionally the exact attested *depuis le premier jour* phrase. |
| French | `fr_future_conditional` | `Je vous aimerais à la folie` | First-person singular future/conditional | Requires `je` plus an immediately governed second-person clitic and only `aimerai` or `aimerais`. |
| Swedish | `sv_exclusive_modal_perfect` | `jag har aldrig kunnat älska någon annan än dig` | Exclusive target under perfect/modal syntax | Requires the complete sequence `jag har aldrig kunnat älska`, `någon/ingen annan än`, and an established second-person target form. |
| German | `de_negative_perfect`, `de_perfect`, `de_main`, `de_subordinate` | `daß ich euch liebe` | Second-person plural target | Adds only `euch` to each existing `dich`/`Sie` target alternation; word order and verbal constraints are unchanged. |
| Italian | `it_future`, `it_conditional`, `it_imperfect`, `it_remote_past` | `io, che t’amavo con tanta pena` | Elided second-person clitic in already-supported simple tenses | Adds straight/curly `t'` immediately fused to the same finite forms already covered with `ti`; no tense family is added. Existing `it_present_elided` already covers `t'amo`/`t’amo`. |
| English | `en_emphasized_target` | `I should say I loved _you;_` | Gutenberg underscore emphasis around the target | Requires an existing first-person `love`/`loved` frame followed immediately by `_you_`, allowing only a small punctuation set before the closing underscore. |

The resulting 17-candidate increase was inspected in full and is recorded in `results/extraction/canonical_31_v0_10/delta_from_v0_9.md`.
