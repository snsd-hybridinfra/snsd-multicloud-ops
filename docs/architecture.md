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

## Related Authorities

- [Scope lock](scope-lock.md)
- [Lab reference architecture](lab-reference-architecture.md)
- [Zero Trust governance](zero-trust/governance.md)
- [Capability catalog](zero-trust/capability-catalog.yaml)
- [Current baseline](zero-trust/current-baseline-assessment.yaml)
- [Capability backlog](zero-trust/capability-implementation-backlog.yaml)
- [Target phase roadmap](zero-trust/target-architecture/phase-roadmap.md)
- [Runbook framework](runbooks/README.md)
