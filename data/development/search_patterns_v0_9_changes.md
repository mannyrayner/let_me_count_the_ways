# Search-pattern changes in v0.9

Version 0.9 starts from v0.8. It adds only the English exclusive-target class
that has direct corpus evidence. The cross-linguistic audit found no exclusive
target occurrence to justify promoting a French, German, Norwegian, Swedish,
Danish, or Italian audit template into production.

| Language | Pattern ID | Change type | Motivating occurrence/work | Grammatical class | Precision note |
| --- | --- | --- | --- | --- | --- |
| English | `en_exclusive_only`, `en_exclusive_only_past`, `en_exclusive_only_perfect` | Added bounded templates | Synthetic forms tightly related to the *Persuasion* miss | exclusive particle + second-person target | Requires the complete adjacent complement `only you`; tense-specific patterns preserve metadata. |
| English | `en_exclusive_none_but`, `en_exclusive_none_but_past`, `en_exclusive_none_but_perfect` | Added bounded templates | `I have loved none but you`, `austen-persuasion`, offset 435667 | negative indefinite + exception target | Requires the complete adjacent complement `none but you`; does not accept `none of you`. |
| English | `en_exclusive_no_one_but`, `en_exclusive_no_one_but_past`, `en_exclusive_no_one_but_perfect` | Added bounded templates | Synthetic forms tightly related to the *Persuasion* miss | negative indefinite + exception target | Enumerates `no one`/`nobody` and requires adjacent `but you`; punctuation breaks the template. |

All patterns use `form_family: exclusive_target` and semantic
`polarity: affirmative`. No generic LOVE-to-YOU window was added.
