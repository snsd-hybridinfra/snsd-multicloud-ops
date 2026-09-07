# Authoritative Project Architecture

The repository's primary product architecture is the
[Financial Hybrid-Ready IDP target architecture](platform/target-architecture.md),
with a machine-readable boundary in
[architecture-baseline.yaml](platform/architecture-baseline.yaml).

[ZT-ARC-001](zero-trust/target-architecture/README.md) remains the surrounding
Zero Trust security architecture authority. It governs how the platform is
protected and validated, but it is not the product architecture by itself and
does not promote implementation, runtime, acceptance, maturity, or compliance
state.

## Platform Model

The primary product flow is developer experience -> approved composite blueprint
-> policy and approval -> immutable resolved manifest -> automation
-> OpenStack IaaS and k3s PaaS -> financial network underlay. Internal
components and provider-bound execution profiles are not directly user-facing.
Zero Trust, observability, audit, backup/restore, and FinOps are
cross-cutting controls. Public cloud is a deferred provider-adapter extension;
until it is implemented and runtime validated, the accurate designation is
`Hybrid-Ready`.

The flagship PaaS blueprint is `AI_AGENT_SANDBOX` (Project Mini-Ona). Its
durable authority is control-plane job state; k3s execution pods are disposable
and require strong RuntimeClass isolation, brokered egress, task-scoped
credentials, hard budgets, checkpoint/resume approval and sanitized trace
continuity. A service-only state-machine and inert manifest-bundle slice is
locally implemented; it creates no live runtime claim.

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

The protected internal IaaS and k3s PaaS portal under
`applications/internal-iaas-portal/` is a local OpenStack application candidate.
ADR 0012 defines its private Nova/Neutron boundary and its fail-closed k3s
bootstrap gate. It is not part of the authoritative application inventory and
does not change package, capability, maturity, or Phase 1 status.

ADR 0013 removes ZT-SCH-001 from the sequential Phase 1 predecessor chain. The
installed task is disabled and preserved as the final Phase 5 gate immediately
before P5-ACC-001. ADR 0014 records the reviewed `P1-RV-FRESHNESS-001`
exception: Phase 1 is `COMPLETED_WITH_GAPS` and Phase 2 local preparation may
start, while the three historical RV records remain stale and the new manual
refresh window is only 1/3 at EC3, so current EC4 freshness is not
claimed. No EC5 or maturity claim follows from either decision.

## Current Truth Boundary

The architecture pivot is `ACCEPTED / LOCAL_GOVERNANCE_VALIDATED`, while the
integrated IDP runtime remains `NOT_VALIDATED`. The portal remains a local
candidate with deployment `NOT_AUTHORIZED`. Nexus/IOS financial underlay is
`DESIGN_ONLY`, and public-cloud integration is `DEFERRED / NOT_IMPLEMENTED`.
Existing files under `platform/` are reusable candidates and do not inherit
root authority or runtime status merely by existing.

ZT-ARC-001 is `DESIGN_ONLY` / `VALIDATED_LOCAL`. Existing package and scenario
records remain the authorities for implementation and runtime validation. All
52 capability maturity values remain `UNASSESSED`; no overall maturity score
exists. Monitoring work under `.runtime/zero-trust/zt-vis-002/` remains an
untracked non-authority. `ZT-VIS-002` is partially implemented, partially
runtime validated, and partially accepted at bounded EC3 for one private
non-production OpenStack monitoring VM. Alert delivery, elapsed retention, and
full Cinder snapshot restore remain outside that accepted evidence.

The current Phase 1 runtime-package set includes ZT-FND-001, ZT-NET-001,
ZT-VIS-001, ZT-ID-001, ZT-DEV-001, ZT-APP-001, ZT-DATA-001, ZT-SYS-001,
ZT-AUTO-001, ZT-CV-001, and ZT-RV-001. ZT-RV-001 is implemented, runtime
validated, and accepted at bounded EC4 with three eligible independent runs.
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
selects only ZT-4.1.1 through ZTCV-VAL-SYS and has accepted three consecutive
successes separated by at least 24 hours at bounded EC4. Neither package
establishes scheduling, EC5, continuous observation, continuous enforcement,
maturity, or Phase 1 completion at the current state.

## Related Authorities

- [Scope lock](scope-lock.md)
- [Composite service catalog](platform/composite-service-catalog.yaml)
- [AI agent sandbox contract](platform/ai-agent-sandbox.yaml)
- [Lab reference architecture](lab-reference-architecture.md)
- [Zero Trust governance](zero-trust/governance.md)
- [Capability catalog](zero-trust/capability-catalog.yaml)
- [Current baseline](zero-trust/current-baseline-assessment.yaml)
- [Capability backlog](zero-trust/capability-implementation-backlog.yaml)
- [Target phase roadmap](zero-trust/target-architecture/phase-roadmap.md)
- [Runbook framework](runbooks/README.md)
