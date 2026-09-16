# Scholarly candidate membership review v1

Return **JSON only**, conforming to the supplied schema.

## Question

Does the candidate genuinely instantiate an explicit lexical realization of
`LOVE(first-person singular experiencer, second-person target/addressee)`?

The deterministic extraction deliberately favours recall, so a surface match
may be a false positive. Decide membership only: `KEEP`, `EXCLUDE`, or, when
the supplied local evidence genuinely cannot support a confident binary
decision, `UNCERTAIN`.

Use the work metadata, language, matched text, local context, form metadata,
and pattern metadata together. Be conservative about excluding a plausible
target case. Do not retrieve or assume wider narrative context. If wider
context is essential, use `UNCERTAIN_NEEDS_WIDER_CONTEXT`.

`KEEP` includes affirmative, negative, past, perfect, future, cessative,
remembered, interrogative, and embedded realizations. Reported speech,
self-quotation, quoted formulae, and metalinguistic uses also belong when their
lexical material instantiates LOVE(I,YOU). An unusual discourse function is
not grounds for exclusion. Assertion, sincerity, truth, performative force,
expressivity, quotation status, and speaker/hearer construal are later-stage
questions and must not determine this membership decision.

Exclude a match only when syntax or lexical sense fails the target—for
example, `I'd love you to come` (second person is not the loved target) or
French `aimer mieux X que Y` meaning “prefer.” Do not exclude merely because a
passage is difficult.

Choose exactly one compatible reason code:

- `VALID_EXPLICIT_LOVE_I_YOU`
- `EXCLUDE_NOT_LOVE_SENSE`
- `EXCLUDE_SECOND_PERSON_NOT_TARGET`
- `EXCLUDE_FIRST_PERSON_NOT_EXPERIENCER`
- `EXCLUDE_SYNTACTIC_FALSE_POSITIVE`
- `EXCLUDE_TEXT_CORRUPTION`
- `EXCLUDE_OTHER`
- `UNCERTAIN_NEEDS_WIDER_CONTEXT`
- `UNCERTAIN_OTHER`

Give a confidence from 0 through 1 and one concise, evidence-based note. Do
not perform T/P/E/O or any contextual annotation.
