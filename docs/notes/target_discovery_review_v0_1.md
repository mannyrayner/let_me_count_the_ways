# Target discovery review v0.1

## Run reviewed

- Run directory: `results/development_runs/target_discovery/20260829T102542Z`
- Model alias: `5.6`
- API model: `gpt-5.6-sol`
- Prompt version: `0.1`
- Prompt SHA-256:
  `293726bb48b62ab690d10976a04c675721d8fa02fa9b387c7c3bf170a9341464`
- Output SHA-256:
  `b52352f736c7cab2037bee061601b931fff20f229d0b90406c541ed2c15cb786`
- Candidate count: 40
- Estimated API cost: USD 0.231644

This note records review of the candidate proposal supplied by the model. It does
not verify any edition, repository, phrase occurrence, rights claim, or copyright
status.

## Distribution

- Languages: Danish 2, German 6, English 11, French 7, Italian 5, Norwegian 4,
  Swedish 5.
- Broad forms represented: 31 prose works and 9 plays, if verse drama is grouped
  with plays and prose subgenres are grouped together.
- Familiarity: 29 high, 11 medium, according to the model’s own estimates.

The pool covers all requested languages and includes useful variation in genre,
period, relationship, speaker perspective, social constraint, sincerity,
manipulation, and romantic versus nonromantic affection. English is the largest
language group and Danish the smallest; this imbalance should be addressed at
sampling time rather than by treating candidate counts as corpus weights.

## Phrase-form audit

The `likely_phrase_forms` field is useful discovery metadata but is not an
approved search-pattern list. It mixes several types:

1. Direct first-person forms close to the target, such as “I love you”, “je vous
   aime”, “jag älskar dig”, “ich liebe dich”, and “ti amo”.
2. Direct variants that the initial patterns do not yet cover, including tense,
   emphasis, historical address, and elision: “I do love you”, “I love thee”,
   “jeg elsker Dem”, “ich habe dich geliebt”, and “io t’amo”.
3. Questions or hearer-oriented forms, including “do you love me”, “du liebst
   mich”, “tu m’aimes”, and “voi mi amate”.
4. Third-person forms, including “je l’aime”, “ich liebe sie”, “jag älskar
   henne”, and “I love him”.
5. Adjacent but non-equivalent expressions, including “my love”, “I am in love
   with you”, and Italian “ti voglio bene”.

Only the first two groups are plausible candidates for an expanded direct-
declaration search. The remaining groups may be useful comparisons but must not
silently enter the extraction pattern set.

## Language and metadata cautions

- Historical Norwegian works may use Danish or Dano-Norwegian orthography. The
  work-level language code does not determine the correct edition-level search
  patterns; this is especially relevant to *Et dukkehjem*, *Amtmandens Døtre*,
  and *Skipper Worse*.
- Genre values mix broad and narrow labels (`novel`, `Gothic novel`, `diary
  novel`, `children’s novel`, and `epistolary novel`). Preserve the descriptive
  value, but derive a separate normalized genre family before stratified
  sampling.
- Model familiarity, repository names, and publication dates are candidate
  metadata, not verified provenance.
- The pool is heavily canonical and concentrated in European and North American
  works from the eighteenth through early twentieth centuries. This is useful
  for a first technically tractable run but limits any later generalization.

## Review decision

Retain all 40 records in `target_candidates_v0_1.json` as candidates for source
verification. Do not rewrite uncertain claims as facts, and do not treat
`likely_phrase_forms` as executable patterns. No candidate is yet approved for
download, corpus inclusion, quotation, or quantitative sampling.

The next action is to select one candidate for an acquisition trial based on a
specific, lawfully reusable, machine-readable edition. That decision must record
the edition, direct URL or catalogue identifier, language/orthography, rights
basis, and confirmed presence of at least one relevant form.
