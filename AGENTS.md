# AGENTS.md

This file defines working rules for Codex and other automation agents in this repository.

## Operating Principles

- Treat scenario-based validation as the main repository method.
- Keep changes small, reviewable, and aligned with the locked scope.
- Prefer documentation and skeletal structure until a scenario explicitly requires implementation.
- Do not introduce real cloud resources, credentials, secrets, keys, tfstate, kubeconfig files, or account-specific files.
- Do not add technologies outside the locked scope without updating the scope documents through an ADR.
- Do not generate binary files.

## Required Workflow

1. Read `docs/scope-lock.md`, `docs/excluded-scope.md`, and the relevant scenario before changing files.
2. Keep scenario definitions under `scenarios/<level>/`.
3. Keep validation outputs under `evidence/<level>/<scenario-id>/`.
4. Update documentation when conventions, naming, or evidence requirements change.
5. Use `docs/adr/` for meaningful architecture or scope decisions.

## Tracking File Update Rule

When modifying or implementing a scenario, update:

- `docs/progress-tracker.md`
- `docs/scenario-status-matrix.md`
- `docs/evidence-status-matrix.md`
- `docs/implementation-log.md`

If scenario work is blocked or introduces a risk, update `docs/risk-register.md`.

## File Safety

- Never commit secrets, credentials, private keys, generated state, kubeconfigs, or local environment files.
- Keep placeholders text-only.
- Use `.gitkeep` only to preserve intentionally empty directories.
- Do not overwrite user work unless the task explicitly requires it.

## Scenario Expectations

Each scenario should include an ID, title, objective, scope, prerequisites, validation steps, evidence requirements, and pass criteria.
