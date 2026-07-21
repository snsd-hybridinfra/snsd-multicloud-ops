
# ZT-ARC-001 Target Architecture

- Status: `DESIGN_ONLY` / `LOCAL_VALIDATED`
- Runtime validation: `NOT_VALIDATED`
- Authority status: `AUTHORITATIVE`
- Current maturity: `UNASSESSED`
- Target boundary: `ADVANCED_TARGET`
- Architecture designation: `OPTIMAL_READY` (repository-local, not an official maturity level)

This directory is the authoritative post-Phase-1 target architecture for the SNSD laboratory. It positions the project as an **IaC, Configuration as Code, and Policy as Code-driven Advanced Zero Trust Secure Operations Platform with an Optimal-Ready Extension Architecture**. The conservative public title is **Hybrid and Multicloud-Ready Secure Operations Platform** because AWS and Azure adapters are not implemented.

## Terms

- IaC = Infrastructure as Code: infrastructure desired state and provider adapters.
- CaC = Configuration as Code: versioned operating-system and service configuration. Here, CaC never means Compliance as Code.
- PaC = Policy as Code: deterministic design-time, deployment-time, and runtime policy evaluation.
- `ADVANCED_TARGET`: the selected capability is intended to satisfy official Advanced-stage conditions.
- `ADVANCED_VALIDATED`: capability-specific implementation and fresh runtime evidence support an Advanced-stage assessment.
- `OPTIMAL_READY`: stable local interfaces exist for future Optimal-stage functions. It is not `OPTIMAL`, and readiness does not establish maturity.

## Authority and Boundaries

The external authority is the local **제로트러스트 가이드라인 2.0** PDF whose recorded SHA-256 is in `../authoritative-source.md`. The repository taxonomy authority remains `../capability-catalog.yaml`; current truth remains `../current-baseline-assessment.yaml`; planning remains `../capability-implementation-backlog.yaml`.

The architecture represents all 52 canonical capabilities: 21 Advanced primary, 15 Advanced supporting, 4 Initial, 5 design-only, and 7 future Optimal-roadmap. No capability status or current maturity is promoted by this package.

Active monitoring work under `.runtime/zero-trust/zt-vis-002/` is protected. This package neither edits that work nor claims the monitoring stack is runtime validated.

Phase 1 remains bounded by `ZT-SCH-001` with implementation `PARTIAL`, validation `PARTIALLY_VALIDATED`, and completion `NOT_COMPLETE`. `ZT-ID-001` is runtime accepted only for one bounded non-production validator endpoint; centralized identity, MFA, OIDC, application RBAC, production validation, and maturity remain open. `ZT-VIS-002` is protected Phase 2 enabling work and does not replace identity or close visibility gaps.

## Navigation

- Scope and selection: `advanced-maturity-scope.md`, `capability-selection-method.md`, `capability-traceability-matrix.md`
- Platform architecture: `iac-cac-pac-reference-architecture.md`, `target-portability-architecture.md`
- Contracts: `host-onboarding-contract.md`, `operator-interface-contract.md`
- Assessment: `advanced-maturity-acceptance-model.md`, `handoff-acceptance-model.md`
- Roadmaps: `phase-roadmap.md`, `optimal-expansion-roadmap.md`
- Execution model: `golden-path.md`, `implementation-dependency-map.md`
- Authoritative operational runbooks: `../../runbooks/RUNBOOK_INDEX.md`
