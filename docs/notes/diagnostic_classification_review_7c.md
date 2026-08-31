# Diagnostic classification review 7C: sisterly love

## Run record

- Case: `sisterly_love`
- Occurrence: `bronte-jane-eyre-b57472f62694`
- Run directory: `results/development_runs/classification_diagnostics/sisterly_love/20260830T133959Z`
- Model alias: `5.6`
- API model: `gpt-5.6-sol`
- Prompt: `prompts/annotation/classify_passage_v0_1.md`
- Schema: `prompts/annotation/classification_schema_v0_1.json`
- Input SHA-256: `45888eadd43ef52fa7364a92be3c26ed7ce8225940ec3edba983ee0cdc77ef1c`
- Prompt SHA-256: `bc28060585a36658bffdcc1d71e8a6e4f6f8bfe65a0972e5bace60c728448587`
- Schema SHA-256: `f2c3f81b241e4b2b8ed7738f428f1ba503db942f2a88ff0a28e48f86a9a58789`
- Estimated cost: USD 0.026084 (1,191 input tokens and 1,066 output tokens)
- Validation: passed for the expected occurrence ID

These values transcribe the reviewed local run. The exact input and API run
artifacts should be committed from the machine on which the call was made.

## Result

The result assigns support 4/1/0 to truth-conditional, performative, and
exclamatory/reflexive readings, with confidence 0.94. This is a convincing
analysis of the core construction. The phrase reports an existing attitude;
its limited interpersonal reassurance does not make it an undertaking, and
the deliberative syntax gives no support to an exclamatory reading.

The model also correctly treats “as a sister” as a constraint on the kind of
love avowed rather than as a competing T/P/E category. It connects the avowal
with admiration, confidence, and willingness to venture much, while keeping
that affection distinct from a commitment to travel to India.

## Caveats

The `quoted` feature is formally permitted by v0.1 but is not analytically
helpful here. The supplied passage is represented as direct speech, yet unlike
7A and 7B it does not contain quotation, revoicing, or imagined verbalization
inside the highlighted speech. A future embedding annotation should distinguish
ordinary presented dialogue from an occurrence embedded in quoted, reported,
imagined, or metalinguistically reused language.

The request for more context is appropriately limited. The excerpt settles the
core T/P/E classification and the explicitly sisterly construal. Preceding and
following dialogue could clarify whether the avowal is received as reassurance,
relational preservation, or rejection of a romantic interpretation, but that
uncertainty should not lower confidence in the core analysis.

## Comparison with 7A and 7B

Together the three diagnostics support the provisional layered design:

1. retain T/P/E for the semantic-pragmatic force of the core construction;
2. annotate production and embedding context independently;
3. annotate how that context constrains, redirects, or otherwise affects the
   interpretation of the core construction; and
4. distinguish uncertainty about the core phrase from uncertainty about the
   wider discourse and relationship.

The set also shows that relationship type is orthogonal to both T/P/E and
embedding. In 7C, “sisterly” constrains the love relation without changing the
predominantly truth-conditional force or introducing a special embedding type.

## Decision

The comparable v0.1 diagnostic set is complete. Preserve the 7C artifacts and
invite review of 7A–7C before changing the prompt, schema, validator, or input
format. A later v0.2 design can use the three cases as regression examples for
core T/P/E force, embedding context, contextual effect, relationship type,
evidence provenance, and separately scoped uncertainty.
