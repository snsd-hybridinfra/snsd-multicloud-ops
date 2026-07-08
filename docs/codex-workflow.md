# Codex Workflow

Codex should work as a scoped repository collaborator, not as an autonomous deployment agent.

## Before Changing Files

1. Read `AGENTS.md`.
2. Read the relevant scope and scenario documents.
3. Confirm the change does not introduce excluded scope.
4. Prefer concise documentation and skeletal structure for foundation work.

## During Changes

- Keep changes scenario-based.
- Update naming, evidence, or scope docs when conventions change.
- Add ADRs for meaningful architecture or scope decisions.
- Avoid generated binaries and local machine artifacts.
- Do not create credentials, secrets, tfstate, kubeconfig files, or provider configuration.

## Validation

After changes, verify:

- required directories exist
- required docs are populated
- `.gitignore` blocks sensitive and local artifacts
- scenario IDs follow naming rules
- evidence paths match the evidence model

## Handoff

Summaries should include changed files, validation performed, and any remaining risks or deferred work.
