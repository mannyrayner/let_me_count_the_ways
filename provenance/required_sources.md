# Required source inventory and acquisition plan

## Purpose

This living inventory records works that the project needs for its theoretical
framework, motivating examples, ontology development, or validation. It is an
acquisition plan, not a corpus manifest: inclusion here does not mean that the
work may be copied into the repository or used as corpus data.

For each source, record:

- the exact edition, language, and relevant passage;
- why the source is needed and its priority;
- a lawful access route;
- copyright and licence information for that particular edition or translation;
- whether the project may retain the full text, a derived extract, or notes only;
- acquisition date, stable catalogue or seller identifier, and receipt or loan
  record where appropriate;
- any transcription, OCR, translation, or normalization performed by the
  project.

Availability and licensing must be verified before acquisition. A work not found
in a general web search should not be assumed to be unavailable, and a readable
online copy should not be assumed to be lawful or reusable.

## Acquisition statuses

| Status | Meaning |
| --- | --- |
| `needed` | Required, but no access route has yet been selected. |
| `locating` | Catalogues, libraries, publishers, or sellers are being checked. |
| `requested` | A loan, scan, purchase, or permission request is in progress. |
| `accessible` | A collaborator has lawful access; reuse conditions still apply. |
| `cleared` | The intended research use and retention plan have been documented. |

## Priority sources

### Roland Barthes, *Fragments d’un discours amoureux* — `needed`

- **Required material:** the original French text, especially the entry
  “Je-t’aime”.
- **Provisional bibliography:** Roland Barthes, *Fragments d’un discours
  amoureux* (Paris: Éditions du Seuil, 1977). The edition and pagination used in
  the study must be recorded from the acquired copy.
- **Why required:** this is the principal theoretical account that the empirical
  study will describe and test. A translation is useful for comparison, but it
  cannot replace the French source.
- **Suggested access sequence:**
  1. Search a local public or university library catalogue by author, title,
     publisher, and ISBN; also search national and union catalogues.
  2. Request the book through interlibrary loan or ask a research librarian to
     locate the relevant French edition.
  3. Check the publisher and established booksellers for a current new edition,
     then reputable second-hand sellers for the 1977 or another identifiable
     French edition.
  4. If the whole book cannot be borrowed, ask a library whether it can lawfully
     supply the relevant entry for private research under the rules applicable
     in its jurisdiction.
  5. Purchase a copy if library access is impractical; retain the bibliographic
     page and purchase record as provenance, not a scan of the book.
- **Repository treatment:** store bibliographic metadata, analytical notes, and
  only short quotations needed for scholarship. Do not commit an unauthorized
  scan, ebook, or full transcription.
- **Open questions:** identify the exact entry boundaries and pagination;
  determine whether later French editions change the text or pagination; locate
  the edition used by any cited English translation.

### Ludwig Wittgenstein, *Philosophical Investigations* §593 — `needed`

- **Required material:** §593 in a citable German edition and, if the paper quotes
  English, the exact published English translation used.
- **Why required:** the “one-sided diet” warning motivates the project’s move
  from selected examples to a larger empirical sample.
- **Suggested access:** borrow or purchase a scholarly edition; use library
  catalogues to identify edition and translator. Treat the German original and
  each translation as separate copyright objects.
- **Repository treatment:** record edition, translator, section number, and a
  short quotation where justified; do not infer that a recent translation is
  reusable because the underlying work is older.

### Cora Sandel, *Alberte* trilogy, final volume — `locating`

- **Required material:** the scene in the final volume in which Sivert recalls
  Alberte saying “Jeg elsker dig,” including enough surrounding context to
  analyse both characters’ construals.
- **Provisional identification:** the final volume is commonly identified as
  *Bare Alberte*. Exact title, language variety, edition, pagination, and wording
  must be verified against a physical or licensed digital copy.
- **Why required:** this is the strongest motivating counterexample to a single
  privileged interpretation.
- **Suggested access:** search Norwegian and other Nordic national/union library
  catalogues as well as local library catalogues; request the relevant edition
  through interlibrary loan; ask a Scandinavian-studies librarian for help; or
  purchase an identifiable new or second-hand edition. Obtain a published
  translation separately if one will be cited.
- **Repository treatment:** retain a location note, short necessary quotations,
  and analysis. Do not store a full chapter or unlicensed digital copy.
- **Open questions:** establish which edition produced the quoted orthography and
  verify that the two remembered lines and their context have been transcribed
  accurately.

### *Postcards from the Edge* — `needed`

- **Required material:** the scene containing “I think I love you” / “When will
  you know for sure?”, with enough audiovisual and narrative context to assess
  strategic ambiguity and hearer uptake.
- **Version control:** distinguish Carrie Fisher’s novel, screenplay, released
  film, subtitles, and any published script. The handoff currently concerns the
  film; wording and speaker identification must be checked against it.
- **Suggested access:** borrow or purchase an authorized DVD/Blu-ray, or use a
  licensed streaming service available to a collaborator; check library film
  holdings and published-screenplay catalogues. Make a time-coded research note
  from the authorized copy rather than relying on an unattributed transcript.
- **Repository treatment:** record edition or release, distributor/platform,
  access date, timecode, and a short quotation. Do not commit video, audio,
  screenshots, subtitles, or an unauthorized screenplay.

### Leo Tolstoy, *War and Peace* — `needed`

- **Required material:** Pierre’s “Je vous aime!” scene and its later echoes.
- **Version control:** record the source language, edition, translator, volume or
  part, chapter, and pagination. Different English translations have distinct
  wording and may have different copyright status.
- **Suggested access:** prefer a library or purchased scholarly edition for the
  version actually cited. A demonstrably public-domain edition from a reputable
  digital library may support exploratory work, but its translation, source
  files, and reuse terms must be checked and recorded.
- **Repository treatment:** a verified public-domain text may be eligible for the
  corpus only after a provenance record is completed. Otherwise retain location
  metadata, short quotations, and analysis only.

## Secondary and comparison sources

Add complete records as the design develops for:

- a reliable English translation of Barthes, used alongside rather than instead
  of the French original;
- scholarship interpreting Barthes’s “Je-t’aime” entry;
- published criticism or editions needed to support the Sandel reading;
- authoritative editions of comparison expressions in naturally situated
  discourse;
- methodological literature on speech acts, performatives, pragmatics,
  ambiguity, literary annotation, and model-assisted qualitative coding.

These should be promoted to **Priority sources** when they become necessary for
an argument, annotation decision, or validation procedure.

## Development-corpus candidates

### Louisa May Alcott, *Little Women* — `locating`

- **Research role:** next English v0.2 pressure test, selected to broaden the
  relationship space beyond the predominantly romantic *Jane Eyre* cases.
- **Candidate source:** Project Gutenberg ebook 514, English original,
  catalogue page `https://www.gutenberg.org/ebooks/514`, with candidate UTF-8
  text URL `https://www.gutenberg.org/cache/epub/514/pg514.txt`.
- **Verification status:** the identifiers and URLs are acquisition candidates,
  not yet an approved edition. The current execution environment returned an
  HTTP 403 before the landing page or file could be inspected. A collaborator
  must verify the live page, downloaded header/footer, edition identity, rights
  statement, format, and checksum before approval.
- **Repository treatment:** after edition-level review, retain the verified raw
  public-domain source, provenance JSON, extraction, pipeline artifacts, and
  diagnostic review. Do not create an approved record from this candidate note.

### Gustave Flaubert, *Madame Bovary* — `locating`

- **Research role:** first French v0.2 pressure test, including the transfer from
  English “I love you” to Barthes's `je t’aime` object.
- **Candidate source:** Project Gutenberg ebook 14155, candidate French
  original, catalogue page `https://www.gutenberg.org/ebooks/14155`, with
  candidate UTF-8 text URL
  `https://www.gutenberg.org/cache/epub/14155/pg14155.txt`.
- **Verification status:** the work, language, edition presentation, URLs,
  rights statement, encoding, header/footer, and checksum remain to be checked
  against the live source. The current execution environment returned HTTP 403,
  so this note deliberately does not mark the source cleared or approved.
- **Repository treatment:** preserve the verified original-language source only
  after provenance review. Treat a translation as a separate source and do not
  substitute one for this experiment.

## Practical next actions

1. Ask a research librarian to locate Barthes’s 1977 French edition and the
   relevant Sandel edition in union catalogues.
2. Record candidate catalogue identifiers and access options here without
   copying restricted text.
3. Choose the Barthes edition that will serve as the citation copy and acquire it
   by loan or purchase.
4. Create one provenance record per acquired edition or audiovisual release.
5. Verify every quotation already present in the essay and handoff against the
   selected source before using it in a paper, prompt, or annotation guideline.
6. Decide separately whether each source is for close reading, quotation,
   development examples, validation, or inclusion in a machine-processable
   corpus; those uses can have different legal and methodological requirements.
