# Initial pipeline runbooks

These runbooks are designed for a Cygwin Bash terminal on Windows. Run them in
order, one document at a time. Each runbook ends at a review checkpoint: stop,
share the named outputs, and agree any changes before proceeding.

| Step | Runbook | Result to review |
| --- | --- | --- |
| 0 | [Set up and verify](00_setup_and_verify.md) | Environment and passing checks |
| 1 | [Generate target candidates](01_generate_targets.md) | Raw AI candidate response |
| 2 | [Review and approve targets](02_review_targets.md) | Versioned approved manifest |
| 3 | [Acquire one approved text](03_acquire_one_text.md) | Raw text and provenance draft |
| 4 | [Extract passages](04_extract_passages.md) | Occurrence JSONL |
| 5 | [Classify one passage](05_classify_one_passage.md) | Raw structured AI analysis |

## Conventions

- Replace `C:/path/to/let_me_count_the_ways` with the actual Windows checkout
  path in the first command of each terminal session. `cygpath` converts it to a
  Cygwin path safely.
- Commands assume they are run from the repository root.
- Never paste an API key into a file or command-line argument. The runbooks read
  it silently into an environment variable for the current shell.
- Do not commit downloaded texts or model outputs until their provenance,
  licensing, and research role have been reviewed.
- If a command fails, stop. Keep any generated run directory: the scripts retain
  request metadata and error details for diagnosis.
