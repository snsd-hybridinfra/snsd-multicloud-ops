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

## Zero Trust Governance

- Treat the local **제로트러스트 가이드라인 2.0** PDF as the authority for
  canonical Korean terminology, capability numbering, architecture, and
  maturity characteristics.
- Use capability IDs exactly as `ZT-<source-number>`, such as `ZT-3.1.1`.
- Keep canonical Korean display names separate from stable English slugs.
- Do not assign maturity without capability-specific evidence and a reference
  to the corresponding source maturity table.
- Keep alignment, implementation, validation, evidence level, and maturity as
  separate fields. Documentation or mapping alone is not implementation.
- Do not claim full compliance, certification, complete implementation,
  enterprise-wide validation, or repository-wide Optimal maturity.
- Do not create or renumber scenarios outside locked S001-S050 without scope
  approval and the required architecture decision.

### Zero Trust Validation Workflow

- Treat `docs/zero-trust/capability-catalog.yaml` as the repository taxonomy authority, `docs/zero-trust/current-baseline-assessment.yaml` as the current-assessment authority, and `docs/zero-trust/capability-implementation-backlog.yaml` as the planning authority. Markdown matrices are presentation views.
- Never use backlog applicability, target maturity, wave, queue position, or planned tasks to promote current implementation, validation, evidence, or maturity state.
- Backlog records use capability IDs and control-pattern IDs only. Do not assign a future scenario identifier until scenario creation is explicitly approved.
- Before changing Zero Trust governance data, read `docs/zero-trust/governance.md` and `docs/zero-trust/maintenance-workflow.md`.
- Run `python tools/validate_zero_trust.py --verbose`, `python tools/check_zero_trust_sync.py`, and `python tools/generate_zero_trust_reports.py --check`.
- Run the combined read-only entry point with `powershell -ExecutionPolicy Bypass -File tools/validate-zero-trust.ps1`.
- The report generator may write only when `--write` is explicitly requested and only inside reviewed generated markers.
- Do not weaken validation, add dependencies, change the canonical taxonomy fingerprint, or add CI automation without review.
