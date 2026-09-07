# Zero Trust Governance

Zero Trust is the cross-cutting security and validation plane of the Financial Hybrid-Ready Internal Developer Platform. Platform delivery status and Zero Trust package status are independent; neither may promote the other without matching implementation and evidence authority.

## Source hierarchy

1. Local **제로트러스트 가이드라인 2.0** PDF
2. `capability-catalog.yaml`
3. `current-baseline-assessment.yaml`
4. `capability-implementation-backlog.yaml`
5. `package-flow.yaml` and package metadata
6. Sanitized package evidence
7. Reviewed Markdown views

A future authenticated KISA 2026 mapping is a secondary technical inspection and hardening reference. It cannot override Zero Trust capability or maturity semantics and cannot establish implementation or compliance.

## Capability and maturity

- Keep the canonical 52 capabilities and source IDs unchanged without source review.
- Assess maturity per capability and only from matching evidence and source maturity criteria.
- Keep implementation, local validation, runtime validation, evidence, acceptance, and maturity separate.
- Design, backlog, package order, or mapping cannot promote status.

## Package governance

- ZT-ARC-001 surrounds the Phase 1 flow and is not a sequential package.
- `package-flow.yaml` owns sequence and Phase 1 boundary.
- Package YAML owns package state; evidence must resolve and support the claim.
- CV and RV enforce the Phase 1 integration and repeatability gates. SCH remains
  a separate installed, disabled scheduling package deferred to the final Phase
  5 gate.
- The historical P1-ACC-001 default-deny record remains authoritative for the
  stale assessment. ADR 0014 and `P1-RV-FRESHNESS-001` supersede only the entry
  decision: Phase 1 is `COMPLETED_WITH_GAPS` and Phase 2 local preparation may
  proceed. Current EC4 freshness is not claimed, and fresh manual RV evidence
  remains mandatory before final scheduling or P5-ACC-001.
- Package validators must be deterministic, read-only by default, and mutation-detecting where relevant.

## Evidence

Track only sanitized text evidence under approved package authorities. Never track raw runtime, credentials, keys, tokens, state, kubeconfigs, account values, or personal data.

## Retired model

The numbered scenario framework, dedicated evidence tree, matrices, and aggregate tools are removed. Git history is the recovery authority. No active numbered scenario identifier is permitted outside the retirement record.

## Prohibited claims

Do not claim full compliance, certification, complete Zero Trust implementation, production readiness, enterprise-wide validation, continuous operation, or repository-wide Advanced or Optimal maturity.

## Exceptions

Exceptions require a documented owner role, rationale, evidence, residual risk, expiry or review date, and compensating control. Never use an exception to authorize secrets, personal data, unsupported status, or unapproved live mutation.
