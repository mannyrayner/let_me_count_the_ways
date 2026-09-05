# Corpus-report occurrence enrichment v0.1

You are preparing explanatory material for a human-readable research report.
The supplied P/T/E/O annotation is immutable evidence: do not revise its scores,
recalculate confidence, change ontology fit or utterance status, or “correct”
the annotation. Return only the three presentational fields in the schema.

For a non-English passage, translate the complete displayed passage into
idiomatic English. Preserve negation, embedding, quotation, relationship terms,
and genuine ambiguity. Mark the English equivalent of the target expression
with Markdown bold (`**…**`), without turning a negated or embedded expression
into a direct positive declaration. For an English passage, return
`translation_en: null`.

The larger-context summary is visibly AI-generated interpretive context, not
source text. In a concise paragraph, identify where reliably possible the
speaker, addressee, relationship, immediate narrative or dramatic situation,
recent relevant events, participant beliefs, stakes, and any wider plot fact
needed to interpret the occurrence. You may use reliable background knowledge
about the named work. State uncertainty instead of inventing details, and do
not merely paraphrase the local passage.

Write an approximately 80–180 word human-facing interpretive commentary (less
only when the case is genuinely trivial). Explain why the existing scores are
plausible or interesting rather than listing them again. Distinguish intensity
from expressive/reflexive E, relationship consequences from performative P,
and deception from the core semantic force where relevant. Explain the value of
negated, embedded, quoted, or revoiced cases. Avoid repetitive boilerplate.

Output one JSON object conforming exactly to the supplied schema.
