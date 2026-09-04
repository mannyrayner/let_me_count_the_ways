# German word order and multilingual target search

The first German search for the multilingual-five corpus translated the target
lexically but assumed an English-like subject–verb–object surface order:
`ich liebe dich`. Inspection of *Die Leiden des jungen Werther* exposed the
missed verb-final subordinate-clause order in `daß ich dich liebe`.

The manual pre-extraction review caught this blind spot before annotation. The
German production patterns now represent main-clause and subordinate-clause
orders separately, keep the distance between the target elements deliberately
small, and treat formal second-person `Sie` case-sensitively rather than
silently including third-person `sie`.

This incident is methodological evidence that multilingual literary-corpus
extraction requires language-specific syntactic awareness. Replacing “I love
you” with one literal translated string per language is not sufficient, even
when the translated vocabulary itself is correct.

It also exposed the opposite risk. Compensating for underacceptance with a
broad character-proximity search over `lieb*` admits inflections, derivatives,
third-person constructions, and unrelated clauses. A controlled check allowing
at most three intervening word tokens in the checked-in *Werther* found no
additional first-person-to-second-person declarations beyond the adjacent `ich
dich liebe` construction. The broad probe therefore belongs in troubleshooting,
not routine extraction.

The useful middle ground is **linguistically informed but conservative
structural matching, validated against the actual corpus**. Production coverage
should expand in response to observed corpus variation, not hypothetical
grammatical possibility alone.
