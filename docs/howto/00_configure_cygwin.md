# Step 0: configure the Cygwin environment

This repository follows the C-LARA-2 convention: `LMCW` is a persistent global
variable naming a checkout under `/home/github`, and `OPENAI_API_KEY` is the
shared API credential already configured for OpenAI-based projects.

Run this once in Cygwin. It adds `LMCW` only if `.bash_profile` does not already
define it:

```bash
mkdir -p /home/github
grep -q '^export LMCW=' "$HOME/.bash_profile" 2>/dev/null || \
  printf '%s\n' "export LMCW='C:\\cygwin64\\home\\github\\let_me_count_the_ways'" >> "$HOME/.bash_profile"
source "$HOME/.bash_profile"
printf 'LMCW=%s\n' "$LMCW"
test -n "${OPENAI_API_KEY:-}" && echo 'OPENAI_API_KEY is set' || \
  echo 'OPENAI_API_KEY is NOT set'
```

Expected output includes the Windows path to the sister checkout and confirms
that the API key is set. The command deliberately never prints the key.

If `OPENAI_API_KEY` is not set, configure it using the same private, persistent
mechanism used by C-LARA-2. Do not put the key in this repository or a runbook.

## Review checkpoint

Stop and share the two status lines, with any credential value redacted. Do not
proceed until `LMCW` and `OPENAI_API_KEY` are both available in a fresh Cygwin
terminal.
