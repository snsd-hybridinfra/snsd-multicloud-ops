
# Implementation Dependency Map

The dependency model is phase-gated, profile-driven, and package-specific. Phase exit criteria are prerequisites for the next phase; architecture documentation never satisfies a runtime gate.

`ZT-ID-001` is an implemented and runtime-validated Phase 1 identity package for one bounded non-production validator endpoint. Its synthetic policy suite remains locally validated, while the accepted runtime scope covers a dedicated validator account/group, forced command, SSH restrictions, exact sudo allowlist, recovery, and deterministic allow/deny evidence. It does not establish centralized identity, MFA, OIDC, application RBAC, production validation, or maturity. `ZT-ID-002` remains a separate later Phase 2 candidate. `ZT-VIS-002` is protected Phase 2 enabling preparation limited to Docker or Compose traces; it is not deployed, runtime validated, or usable to close `ZT-VIS-001`. Identity-based Grafana access remains a Phase 2 design use case. IaC, Configuration as Code, and Policy as Code convergence waits for cross-domain signal and enforcement validation.

`implementation-dependency-map.yaml` is the machine-readable authority. It records Phase 1 as `PARTIAL` / `PARTIALLY_VALIDATED` / `NOT_COMPLETE`, preserves `ZT-SCH-001` as a design-only boundary, and records future packages only as design, not-started, unassessed, or roadmap-only work.
