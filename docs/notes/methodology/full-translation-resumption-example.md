# Full translation resumption example

The full canonical translation stage required 171 non-English wide-context
translations. Its initial run, with a 300-second request timeout, preserved 164
successful artifacts and left seven timeout failures. A retry with a 600-second
timeout recovered some of those failures; the remaining four completed on a
further retry with a 1,200-second timeout.

The final run resumed 167 already-valid artifacts, made four new calls, and
finished with 171 of 171 translations valid and no unresolved failures. Because
the timeout is a transport setting rather than part of the semantic resumption
key, increasing it did not invalidate completed translation artifacts or repeat
their calls.

This run is one concrete example of fault-tolerant research infrastructure:
successful work survived transport-level failures, while some long literary
wide-context calls in this run required substantially more than 300 seconds.
It does not establish a general model-latency claim.
