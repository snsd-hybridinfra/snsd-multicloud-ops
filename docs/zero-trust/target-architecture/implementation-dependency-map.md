
# Implementation Dependency Map

The dependency model is phase-gated, profile-driven, and package-specific. Phase exit criteria are prerequisites for the next phase; architecture documentation never satisfies a runtime gate.

`ZT-ID-001` is an implemented and locally validated Phase 1 identity-policy package. Its synthetic inventory, role, assurance, lifecycle, decision, schema, validator, and evidence contracts are repository-local; runtime identity validation remains not validated and requires separate approval. `ZT-ID-002` remains a separate later Phase 2 candidate. `ZT-VIS-002` is protected Phase 2 enabling preparation limited to Docker or Compose traces; it is not deployed, runtime validated, or usable to close `ZT-VIS-001`. Identity-based Grafana access remains a Phase 2 design use case. IaC, Configuration as Code, and Policy as Code convergence waits for cross-domain signal and enforcement validation.

`implementation-dependency-map.yaml` is the machine-readable authority. It records Phase 1 as `PARTIAL` / `PARTIALLY_VALIDATED` / `NOT_COMPLETE`, preserves `ZT-SCH-001` as a design-only boundary, and records future packages only as design, not-started, unassessed, or roadmap-only work.
