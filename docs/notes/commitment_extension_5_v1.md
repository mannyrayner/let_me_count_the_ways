# Targeted extension: commitment, duty, and declarations of love

Selected 20 September 2026, following Manny and Cathy's suggestion to examine
fiction about women's economic dependence and declarations made from duty.
This is an exploratory addition to the frozen 30-public-work, 225-KEEP baseline.
The five novels were selected for relevant situations and passages, before
obtaining new T/P/E/O classifications. Their selection does not establish a
high-P or low-T result or a difference in frequency between literary genres.

## Selected works and first inspection leads

| Work | Language | Why included | Passage lead |
| --- | --- | --- | --- |
| Victoria Benedictsson, *Pengar* (1885) | Swedish | Financially advantageous marriage and the difference between vows and felt affection | Chapters 5–6: Selma recalls her marriage formula while denying that she otherwise told her husband she loved him. |
| Amalie Skram, *Constance Ring* (1885) | Norwegian, historical Dano-Norwegian | A requested declaration accompanied by recoil and deliberate self-persuasion | Chapter XXIV, pp. 369–370: Constance and her second husband Lorck. |
| George Gissing, *The Odd Women* (1893) | English | Economic vulnerability, courtship undertakings, and marital control | Chapter XVI: Widdowson demands that Monica say she loves him; she evades the formula. Inspect all other declarations as well. |
| Elizabeth von Arnim, *Vera* (1921) | English | Love, dependence, and resolutions about future marital conduct | Chapter XVII: Lucy repeats ILY while making private vows about her future behaviour. |
| Amalie Skram, *Lucie* (1888) | Norwegian, historical Dano-Norwegian | Courtship acceptance and the sexual double standard | Henny and Knut, pp. 175–177, chapter XVII in corrected numbering (XVI in the first edition). |

In *Vera*, Lucy is newly married to the widower Wemyss. She is distressed by
the place where his previous wife died, then treats his apparent ease as an
example she should follow. In [chapter XVII](https://www.gutenberg.org/cache/epub/34366/pg34366-images.html),
she murmurs "Oh, I love you, love you----" while making "secret vows" about
her conduct. Her declaration accompanies private resolutions
about herself. Affection is also present. Whether the ILY itself undertakes an
interpersonal commitment, rather than accompanying a private resolve, remains
an annotation question.

In *Lucie*, Henny tests Knut's willingness to marry her by claiming a sexual
past. He affirms his willingness; she responds by declaring love and accepting
him: "jeg elsker også Dig. Jeg tror på Dig og jeg er din. Siden Du vil ha mig."
My translation: "I love you too. I believe in you and I am yours, since you
want me." See the [original printed page 176](https://www.nb.no/services/image/resolver/URN:NBN:no-nb_digibok_2012022824024_0182/full/full/0/native.jpg).
She then reveals the supposed history was invented. Her acceptance offers a
plausible P context, with evident affection too. It is not a demonstrated case
of a loveless promise.

In *Constance Ring*, the second marriage's preceding happiness matters. The
passage must not be paraphrased as an unambiguously loveless declaration.
In *Pengar* and *The Odd Women*, the motivating passages need not themselves
meet the project's explicit LOVE(I,YOU) membership rule. They remain valuable
contextual controls even if the extractor returns no corresponding candidate.

## Sources and rights

- *Pengar*: [Project Runeberg](https://runeberg.org/pengar/), ten explicitly
  ordered chapter pages. Its introductory catalogue note appears to confuse
  the novel with *Från Skåne*; the acquired chapter texts identify the novel.
- *The Odd Women*: [Project Gutenberg 4313](https://www.gutenberg.org/ebooks/4313).
- *Vera*: [Project Gutenberg 34366](https://www.gutenberg.org/ebooks/34366),
  reproducing the 1921 Macmillan edition.
- *Constance Ring*: [National Library of Norway, 1885 edition](https://urn.nb.no/URN:NBN:no-nb_digibok_2013082608001),
  printed narrative pages 5–507.
- *Lucie*: [National Library of Norway, 1888 edition](https://urn.nb.no/URN:NBN:no-nb_digibok_2012022824024),
  printed narrative pages 1–229.

The two National Library catalogue records explicitly state public-domain
status and unrestricted worldwide viewing. Their IIIF manifests link to the
[public-domain licence](https://www.nb.no/lisens/#public-domain). Original
catalogue responses, IIIF manifests, ALTO OCR, and page maps are preserved.
The authors of all five works died more than 70 years ago. These are historical original-
language texts, not modern translations; see the
[Australian copyright-duration guidance](https://www.ag.gov.au/rights-and-protections/copyright/copyright-basics).

Bokselskap's editions were useful for locating the Skram passages, but its
[reuse terms](https://www.bokselskap.no/hjelp_om/om_bokselskap) distinguish the
underlying public-domain work from a potentially protected digital edition.
The repository therefore uses independently acquired National Library sources;
it does not reproduce Bokselskap's digital edition or editorial apparatus.

## Protocol

1. Acquire each complete narrative text with source hashes and explicit
   derivation rules. National Library OCR receives only scan-verified corrections
   recorded in `data/acquisition/commitment_extension_5_v1/ocr_corrections.json`.
   Original OCR is preserved; page images remain the authority for doubtful readings.
2. Extract with both frozen v0.11 and additive v0.12 patterns. The new version
   adds Norwegian `jeg elsker også/ogsaa Dig` and historical `jeg elskede dig`.
   Compare matches across every available public work, using canonical hashes,
   offsets, and wording rather than version-dependent occurrence IDs. Retain
   zero-yield works. Do not count vows or refusals as positive ILY occurrences.
3. Apply the existing scholarly membership review to every candidate, retaining
   its KEEP/EXCLUDE/UNCERTAIN decisions and provenance.
4. Generate context translations and classify all KEEP records with the
   established model alias `5.6` and classification prompt v0.3.1.
5. Inspect high-P cases and OCR-sensitive cases with their narrative context.
   Report the extension separately before considering pooled analyses.

An absent feeling, an avowal of a feeling, and an undertaking are separate
questions. The existing T scale concerns avowal/reporting, not whether the
feeling is actually present. This extension does not change that definition.
Additional qualitative notes may record evidence about affection and pressure,
but they must not be presented as outputs of the existing classifier.

### Acquisition and recall audit

The three logged corrections in *Constance Ring* restore quotation marks
misrecognised as letters before `Jeg` on pp. 368, 370, and 429. The latter two
pages affect v0.11 extraction; p. 368 also requires the historical past-tense
pattern. They were checked directly against the original scans. This limited
audit is not full-book proofreading and does not establish exhaustive recall.

The motivating *Lucie* declaration on p. 176 is correctly present in the OCR,
but v0.11 misses the intervening `også`. This is a lexical coverage gap, not a
membership exclusion or a finding about P. V0.12 adds that grammatical variant
and the attested historical past tense without changing the membership prompt,
classification prompt, or previous patterns. The version comparison records
their effects on both the baseline texts and this extension. Other constructions
can remain outside the regex inventory; for example, *Constance Ring* p. 136
has the cleft `det er jo Dem, jeg elsker`. Candidate counts are therefore
extractor yields, not a claim to enumerate every semantically eligible utterance.

## Execution status

All five complete narrative texts have been acquired and validated. The local
canonical inventory now has 36 entries: 35 public works and the pre-existing
private McMillan entry. V0.12 yields 27 candidates in this extension:

| Work | v0.11 candidates | v0.12 candidates |
| --- | ---: | ---: |
| Pengar | 0 | 0 |
| Constance Ring | 8 | 11 |
| The Odd Women | 12 | 12 |
| Vera | 2 | 2 |
| Lucie | 1 | 2 |
| Total | 23 | 27 |

Both columns use the same final canonical texts, including the logged OCR
corrections. The three additional *Constance Ring* matches use historical
`elskede`; the additional *Lucie* match uses intervening `også`.
Across the earlier 30 public works, both versions yield the same 227 candidate
spans. The frozen 225-KEEP baseline and its annotations are unchanged.

Acquisition reproduced identically from cached raw sources with network access
disabled. Source hashes, all candidate/context offsets, and the version
comparison passed. The acquisition, canonical-corpus, and extraction suites
passed 114 tests in total; the runbook index also validates.

Membership review, translations, and classifications have **not** run: this
environment has no configured model API key. Candidate counts are not
retained-case counts or P counts. The annotation wrapper performs a read-only
preflight by default and uses the established API workflow with `--run`.
The local changes also require application to the user's checkout or publication
through an authenticated GitHub connection; they have not been pushed remotely.
