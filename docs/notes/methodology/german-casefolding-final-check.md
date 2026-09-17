# German case-folding in the final precision check

The v0.10 recall additions had been inspected and looked plausible. A final
inspection of the complete candidate set was nevertheless performed before the
extraction freeze. It exposed an older German precision bug: the inventory
intended formal second-person `Sie`, but the patterns' case-insensitive matching
also admitted lowercase third-person `sie` (“her”). This produced real false
positives in *Effi Briest* and *The Sorrows of Young Werther*.

The defect survived earlier extraction stages because the German `Sie`
alternative predated the latest recall changes and therefore was not visible in
the v0.9→v0.10 delta. The v0.11 correction is narrow and language-specific: only
`Sie` is case-sensitive inside the otherwise case-insensitive German patterns.

This case complements, rather than duplicates, the earlier methodology notes:

- the Runeberg case records a technical/source-processing bug;
- the *Persuasion* case records literary knowledge revealing a recall failure;
- the multilingual spot-check records multiple residual recall gaps across
  languages; and
- the German `Sie`/`sie` case records a precision bug caused by the interaction
  of a linguistic case distinction with regular-expression flags.

The final inspection illustrates that reviewing only newly added candidates is
insufficient when inherited extraction logic may contain older systematic
errors. A language-aware examination of the frozen candidate set exposed a
German case distinction that the generic regular-expression configuration had
erased.
