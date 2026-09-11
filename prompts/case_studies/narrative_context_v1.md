# Source-grounded narrative context prompt — version 1

Using only the supplied primary-text evidence, explain the immediate narrative situation, the
broader relationship/plot context established by that evidence, and why the utterance occurs here.
Identify speaker or focal consciousness and addressee where supported. Distinguish textual fact
from interpretation and state ambiguity. Do not use unverified model memory. If the evidence is
not adequate, return `INSUFFICIENT_CONTEXT` so the caller can escalate from expanded local context,
to a larger scene/chapter, to a broader/whole-source read. Return JSON with `status`,
`immediate_situation`, `broader_context`, `why_here`, and `ambiguities`.
