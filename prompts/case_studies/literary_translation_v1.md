# Literary translation prompt — version 1

Translate the supplied original-language literary context into English. Preserve paragraphing,
speaker turns, ambiguity, tone, and repetitions. Be literary but do not embellish, normalize,
summarize, or silently repair OCR. Return JSON with `status` (`complete` or
`INSUFFICIENT_CONTEXT`), `translation`, and `translator_notes`. The original remains the primary
evidence; this is an AI-generated working translation for this study.
