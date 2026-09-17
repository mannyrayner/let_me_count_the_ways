# v0.10 → v0.11 extraction delta

The precision correction reduces the public inventory from **230** to **227**
candidates (**−3**). Every membership change is a German removal caused by the
new case-sensitive treatment of formal `Sie`; there are no additions and no
non-German membership changes. The unavailable private McMillan work remains
non-quoting and contributes no public candidate text.

| Work ID | v0.10 count | v0.11 count | Delta | Removed/added surface | Reason |
| --- | ---: | ---: | ---: | --- | --- |
| fontane-effi-briest | 4 | 2 | −2 | removed `ich liebe sie` (context: `ich liebe sie so wie du`) | Lowercase `sie` is third-person “her,” not formal second-person `Sie`. |
| fontane-effi-briest | 4 | 2 | −2 | removed `ich liebe sie` (context: `ich liebe sie noch`) | Lowercase `sie` refers to “meine Frau,” not formal second-person `Sie`. |
| goethe-die-leiden-des-jungen-werther | 2 | 1 | −1 | removed `ich sie liebe` (context: `Sie weiß, wie ich sie liebe!`) | Lowercase `sie` is third-person “her,” not formal second-person `Sie`. |

French future and conditional candidate membership is unchanged. Existing
`aimerai` candidates now use `fr_future` with `tense_aspect: future`; existing
`aimerais` candidates now use `fr_conditional` with `tense_aspect: modal` and
`modality: conditional`.

## Freeze declaration

Validation succeeded. `canonical_31_v0_11` is the frozen deterministic candidate
extraction set for downstream scholarly review and annotation. Patterns are not
to change during annotation unless a truly blocking defect is found.
