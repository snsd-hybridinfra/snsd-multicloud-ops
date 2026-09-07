# AGENTS.md

This file defines working rules for Codex and repository automation.

## Operating model

- The primary product is the Financial Hybrid-Ready Internal Developer Platform. Use the platform hierarchy user experience -> approved composite blueprint -> policy and approval -> immutable resolved manifest -> automation -> OpenStack/k3s service plane -> financial network underlay.
- Use the catalog hierarchy internal component -> approved composite blueprint -> limited user input -> immutable resolved manifest. Do not expose internal components, raw execution profiles, free-form graphs, provider identifiers, or user-supplied HCL as products.
- Zero Trust is the cross-cutting security and validation plane. Within it, use the hierarchy Zero Trust architecture -> package -> capability -> control -> validator -> sanitized evidence -> status decision.
- Keep platform delivery status independent from Zero Trust package, capability, evidence, acceptance, maturity, and compliance status.
- The numbered scenario framework has been retired from the active tree. Do not create a successor scenario series.
- Treat package metadata, capability authorities, validators, and evidence records as independent authorities.
- Keep changes bounded, reviewable, deterministic, and evidence-based.

## Required workflow

1. Read `docs/scope-lock.md`, `docs/excluded-scope.md`, relevant package metadata, and applicable governance before editing.
2. Use an existing package ID or obtain explicit approval for a new package. Do not invent an unrelated numbering system.
3. Run positive, negative, bypass, persistence, and rollback checks when appropriate to the package.
4. Store only sanitized evidence under reviewed package evidence authorities.
5. Use `docs/adr/` for architecture or scope decisions.
6. Read `docs/platform/architecture-baseline.yaml` and `docs/platform/implementation-roadmap.md` before changing the platform boundary.
7. Until a public-cloud adapter is implemented and runtime validated, use `Hybrid-Ready`; do not claim active hybrid-cloud operation.

## Phase 1 authority

`ZT-ARC-001` surrounds, but is not a sequential member of, this flow:

`ZT-FND-001 -> ZT-NET-001 -> ZT-VIS-001 -> ZT-ID-001 -> ZT-CV-001 -> ZT-RV-001 -> P1-ACC-001`

`ZT-SCH-001` is retained as the disabled, deferred final project gate immediately
before `P5-ACC-001`; it is not a Phase 1 predecessor. Re-enabling it requires
separate explicit approval.

Package removal or status promotion requires matching implementation and evidence authority. Phase 1 is `PARTIAL / PARTIALLY_VALIDATED / COMPLETED_WITH_GAPS` under `P1-RV-FRESHNESS-001`; the stale RV finding remains open and must close before final scheduling or P5-ACC-001. Phase 2 is limited to bounded local preparation until live work is separately authorized.

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
