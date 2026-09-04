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
