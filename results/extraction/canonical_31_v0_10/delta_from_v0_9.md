# v0.9 → v0.10 extraction delta

The final targeted repair increases the public inventory from **213** to **230** candidates (**+17**). All 17 additions were inspected and are plausible explicit LOVE(I,YOU) candidates; no zero-yield or unusually high-count work was introduced. The unavailable private McMillan work remains non-quoting and contributes no public candidate text.

| Work ID | Old count | New count | Delta | New pattern ID | New match |
| --- | ---: | ---: | ---: | --- | --- |
| balzac-illusions-perdues | 7 | 11 | +4 | `fr_perfect` | `je vous ai aimée depuis le premier jour` |
| balzac-illusions-perdues | 7 | 11 | +4 | `fr_future_conditional` | `Je t'aimerais` |
| balzac-illusions-perdues | 7 | 11 | +4 | `fr_future_conditional` | `Je t'aimerai` |
| balzac-illusions-perdues | 7 | 11 | +4 | `fr_future_conditional` | `Je vous aimerais` |
| bronte-jane-eyre | 8 | 9 | +1 | `en_emphasized_target` | `I loved _you;_` |
| bronte-tenant-of-wildfell-hall | 9 | 10 | +1 | `en_emphasized_target` | `I loved _you_` |
| dumas-fils-la-dame-aux-camelias | 19 | 20 | +1 | `fr_future_conditional` | `je vous aimerai` |
| flaubert-madame-bovary | 12 | 15 | +3 | `fr_future_conditional` | `je t’aimerai` |
| flaubert-madame-bovary | 12 | 15 | +3 | `fr_future_conditional` | `je t’aimerai` |
| flaubert-madame-bovary | 12 | 15 | +3 | `fr_future_conditional` | `je t’aimerai` |
| fontane-effi-briest | 3 | 4 | +1 | `de_subordinate` | `ich euch liebe` |
| lagerlof-gosta-berlings-saga | 6 | 7 | +1 | `sv_exclusive_modal_perfect` | `jag har aldrig kunnat älska någon annan än dig` |
| rostand-cyrano-de-bergerac | 19 | 20 | +1 | `fr_future_conditional` | `Je t'aimerais` |
| sand-la-mare-au-diable | 5 | 6 | +1 | `fr_future_conditional` | `je t’aimerai` |
| stendhal-le-rouge-et-le-noir | 9 | 11 | +2 | `fr_perfect` | `je vous ai assez aimée` |
| stendhal-le-rouge-et-le-noir | 9 | 11 | +2 | `fr_perfect` | `je t'ai toujours aimée` |
| verona-colei-che-non-si-deve-amare | 15 | 16 | +1 | `it_imperfect` | `t’amavo` |

## Freeze declaration

`canonical_31_v0_10` is the frozen deterministic candidate extraction set for downstream review and annotation. Extraction patterns are not to change during annotation unless a truly blocking error is discovered.
