# Expansion 15 acquisition status

**Status: 0/15 acquired; source access blocked.**

On 2026-09-16, HTTPS requests to both source providers were rejected by the
execution environment's network proxy before source identity and rights review.
The failed requests did not create partial downloads. No mirror, translation,
or substitute edition was used. Because the source catalogues could not be
inspected, no source provenance, raw text, derived text, hash, or Runeberg page
range is claimed.

| Work | Source | Language | Status | Characters | Warning |
| --- | --- | --- | --- | ---: | --- |
| Le Rouge et le Noir | Gutenberg 798 | fr | blocked | — | Source unreachable |
| Illusions perdues | Gutenberg 54723 | fr | blocked | — | Containing volume not inspected |
| Le blé en herbe | Gutenberg 59926 | fr | blocked | — | Source unreachable |
| La Mare au Diable | Gutenberg 23582 | fr | blocked | — | Source unreachable |
| Corinne; ou, l'Italie | Gutenberg 60810 | fr | blocked | — | Source unreachable |
| Effi Briest | Gutenberg 5323 | de | blocked | — | Source unreachable |
| L'amore di Loredana | Gutenberg 34346 | it | blocked | — | Source unreachable |
| Colei che non si deve amare | Gutenberg 69294 | it | blocked | — | Publication title not inspected |
| Ved Vejen | Gutenberg 13175 | da | blocked | — | Source unreachable |
| Maria: En Bog om Kærlighed | Gutenberg 41786 | da | blocked | — | Source unreachable |
| The Tenant of Wildfell Hall | Gutenberg 969 | en | blocked | — | Source unreachable |
| Persuasion | Gutenberg 105 | en | blocked | — | Source unreachable |
| Middlemarch | Gutenberg 145 | en | blocked | — | Source unreachable |
| Gösta Berlings saga | Runeberg `/berling/` | sv | blocked | — | Page range not guessed |
| Kristin Lavransdatter | Runeberg `/kristin/1/`, `/2/`, `/3/` | no | blocked | — | All three page ranges undiscovered |

Resume only in an environment that can reach both provider catalogues. Follow
Runbook 31 and do not change a blocked entry to acquired until its raw and
derived artifacts, provenance, hashes, and source-specific validation exist.
