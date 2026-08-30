# Target discovery prompt v0.1

You are proposing candidate works for a small, exploratory corpus about uses of
the expression “I love you”. This is discovery, not source verification.

## Languages

English, Swedish, French, Norwegian, Danish, German, and Italian. Prefer original
language texts over translations. A multilingual work may be included if its
edition and language are explicit.

## Selection goals

Propose 30–50 literary or dramatic works that:

- are plausibly in the public domain or available under a documented open licence
  in at least one machine-readable edition;
- are likely to contain one or more direct equivalents of “I love you”;
- are sufficiently well known that a model may have useful contextual knowledge;
- collectively vary in period, genre, relationship, speaker gender, tone, and
  pragmatic situation;
- are not all selected from a single national canon or repository.

Do not claim that a work is available from a particular site unless you are
confident, and do not invent URLs, identifiers, quotations, licences, or
occurrence counts. Mark every availability and phrase-presence claim as needing
human verification. Model familiarity is not evidence about the text.

## Output

Return one JSON object with `prompt_version` set to `0.1` and a `candidates`
array. Each candidate must contain:

- `candidate_id`: stable ASCII slug;
- `author`;
- `title`;
- `original_language`: ISO 639-1 code;
- `original_publication_year`: integer or null;
- `genre`;
- `why_contextually_useful`;
- `likely_phrase_forms`: array of strings;
- `possible_repositories`: array of names only, or an empty array;
- `rights_notes`: cautious provisional note;
- `familiarity`: `high`, `medium`, or `low`;
- `selection_dimensions`: array of short tags;
- `verification_needed`: array of concrete checks.

Rank candidates by usefulness for the first development run. Return JSON only.
