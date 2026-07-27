# AGENTS.md

This file defines working rules for Codex and repository automation.

## Operating model

- Use the hierarchy Zero Trust architecture -> package -> capability -> control -> validator -> sanitized evidence -> status decision.
- The numbered scenario framework has been retired from the active tree. Do not create a successor scenario series.
- Treat package metadata, capability authorities, validators, and evidence records as independent authorities.
- Keep changes bounded, reviewable, deterministic, and evidence-based.

## Required workflow

1. Read `docs/scope-lock.md`, `docs/excluded-scope.md`, relevant package metadata, and applicable governance before editing.
2. Use an existing package ID or obtain explicit approval for a new package. Do not invent an unrelated numbering system.
3. Run positive, negative, bypass, persistence, and rollback checks when appropriate to the package.
4. Store only sanitized evidence under reviewed package evidence authorities.
5. Use `docs/adr/` for architecture or scope decisions.

## Phase 1 authority

`ZT-ARC-001` surrounds, but is not a sequential member of, this flow:

`ZT-FND-001 -> ZT-NET-001 -> ZT-VIS-001 -> ZT-ID-001 -> ZT-CV-001 -> ZT-RV-001 -> ZT-SCH-001 -> P1-ACC-001`

Package removal or status promotion requires matching implementation and evidence authority. Phase 1 remains PARTIAL / PARTIALLY_VALIDATED / NOT_COMPLETE until all accepted prerequisites pass.

## Source governance

- The local **제로트러스트 가이드라인 2.0** PDF is the primary authority for canonical terminology, capability numbering, architecture, and maturity characteristics.
- The authenticated 2026 KISA critical-infrastructure technical vulnerability guide is a secondary technical inspection and hardening reference. `ZT-GOV-MAP-001` owns the accepted source-verified mapping framework.
- Mapping is not implementation, runtime validation, maturity, compliance, or certification.

## File safety

- Never commit credentials, keys, secrets, state, kubeconfigs, local runtime files, account values, personal data, or raw live output.
- Do not execute a live validator without separate explicit authorization.
- Do not weaken validators, change the capability fingerprint, add dependencies, or add CI automation without review.
- Preserve package evidence and Git history. The removed scenario framework is recoverable only from Git history.

## Validation

After governance changes, run the read-only package-flow, retirement, Zero Trust, synchronization, report-check, architecture, runbook, repository-structure, and unit-test validators. Confirm no tracked `.runtime/**`, secret, personal data, active numbered scenario path, or scenario aggregate executable exists.
