# Authoritative Project Architecture

The authoritative post-Phase-1 design is
[ZT-ARC-001](zero-trust/target-architecture/README.md).

## Platform Model

- Infrastructure as Code (IaC) owns provider-backed desired infrastructure and
  generated inventory.
- Configuration as Code (CaC) owns versioned operating-system and service
  configuration. In this repository, CaC means Configuration as Code, not
  Compliance as Code.
- Policy as Code (PaC) owns design-time, deployment-time, and runtime policy
  evaluation with `DENY_BY_DEFAULT_FOR_UNREGISTERED_CHANGE`.

The target supports OpenStack-provisioned VMs, registration of existing VMs,
and registration of user-prepared physical servers through a shared host
contract. Existing VMs and physical hardware are never represented as created
by IaC. AWS, Azure, Kubernetes, and additional OpenStack adapters are future
interfaces only.

## Current Truth Boundary

ZT-ARC-001 is `DESIGN_ONLY` / `VALIDATED_LOCAL`. Existing package and scenario
records remain the authorities for implementation and runtime validation. All
52 capability maturity values remain `UNASSESSED`; no overall maturity score
exists. Active monitoring work under `.runtime/zero-trust/zt-vis-002/` is an
untracked dependency and is not accepted as runtime evidence by this document.

The current Phase 1 runtime-package set includes ZT-FND-001, ZT-NET-001,
ZT-VIS-001, ZT-ID-001, ZT-DEV-001, ZT-APP-001, ZT-DATA-001, ZT-SYS-001,
ZT-AUTO-001, and ZT-CV-001. ZT-RV-001 is implemented as a locally validated
campaign configuration but has no accepted campaign execution yet.
ZT-SYS-001 is bounded to seven laboratory records, existing fixed read-only
validators, five safe configuration hashes, and an explicit OpenStack
`CURRENT_DEGRADED` state. It does not establish complete PAM, continuous FIM,
system recovery, maturity, or Phase 1 completion.
ZT-AUTO-001 is bounded to one workstation, fixed R0-R3 handlers, ignored raw
runtime, sanitized evidence, and one partial cross-domain read-only execution.
It does not establish arbitrary execution, mutation authority, external
notification, autonomous response, SOAR, repeatability, scheduling, maturity,
or Phase 1 completion.
ZT-CV-001 is bounded to one manual fixed-handler cycle at 8 PASS/2 WARN/0
FAIL, EC3, and proposal-only acceptance and maturity reassessment. ZT-RV-001
selects only ZT-4.1.1 through ZTCV-VAL-SYS and enforces three consecutive
successes separated by 24 hours. Neither package establishes EC4, scheduling,
continuous observation, continuous enforcement, maturity, or Phase 1
completion at the current state.

## Related Authorities

- [Scope lock](scope-lock.md)
- [Lab reference architecture](lab-reference-architecture.md)
- [Zero Trust governance](zero-trust/governance.md)
- [Capability catalog](zero-trust/capability-catalog.yaml)
- [Current baseline](zero-trust/current-baseline-assessment.yaml)
- [Capability backlog](zero-trust/capability-implementation-backlog.yaml)
- [Target phase roadmap](zero-trust/target-architecture/phase-roadmap.md)
- [Runbook framework](runbooks/README.md)
