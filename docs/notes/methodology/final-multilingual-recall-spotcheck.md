# Final multilingual recall spot-check

## Background

After v0.9 repaired the *Persuasion* false negative and produced a numerically stable 31-work extraction, the human supervisor requested one final spot-check before the candidate set was frozen.

## What happened

During the final pre-annotation inspection, the AI researcher was asked to spot-check the extraction results. It independently examined unmatched audit contexts in several languages and identified multiple residual false negatives, each arising from a different linguistic or representational phenomenon. These findings motivated the final v0.10 extraction repair.

The concrete gaps were French `je vous ai assez aimée` and `Je vous aimerais à la folie`; Swedish `jag har aldrig kunnat älska någon annan än dig`; German `daß ich euch liebe`; Italian `t’amavo`; and English `I loved _you_`. The human supervisor did not propose these cases or direct the language-by-language inspection.

## Nature and significance of the gaps

The causes were distinct: adverbial flexibility in a compound tense, future/conditional morphology, exclusive-target syntax under a modal/perfect construction, second-person plural pronoun coverage, clitic elision, and source-format markup around the target pronoun.

This episode documents a rapid multilingual qualitative audit in which individual anomalies were connected to different linguistic or implementation causes. It is not intended as a general claim about AI research capability. It also occurred after the automated recall audit, illustrating that deterministic diagnostics and higher-level linguistic inspection were complementary rather than interchangeable.

The episode differs from the [Runeberg example](runeberg-cross-domain-debugging-example.md), which records cross-domain technical diagnosis, and the [*Persuasion* example](persuasion-recall-gap-example.md), in which literary knowledge exposed a particular extraction gap. Here the activity was an autonomous qualitative audit across several languages.
