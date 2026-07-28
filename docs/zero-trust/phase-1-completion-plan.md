# Phase 1 Completion Plan

## Authority

The package flow in `docs/zero-trust/package-flow.yaml` is authoritative. ZT-ARC-001 surrounds, but is not a sequential member of, the flow.

```text
ZT-FND-001 -> ZT-NET-001 -> ZT-VIS-001 -> ZT-ID-001
           -> ZT-CV-001 -> ZT-RV-001 -> ZT-SCH-001
           -> P1-ACC-001
```

## Current state

| Package | Implementation | Runtime validation | Acceptance |
|---|---|---|---|
| ZT-FND-001 | IMPLEMENTED | VALIDATED | BOUNDED_ACCEPTED |
| ZT-NET-001 | IMPLEMENTED | VALIDATED | ACCEPTED |
| ZT-VIS-001 | IMPLEMENTED | VALIDATED | ACCEPTED |
| ZT-ID-001 | IMPLEMENTED | VALIDATED | ACCEPTED |
| ZT-CV-001 | IMPLEMENTED | PARTIALLY_VALIDATED | BLOCKED |
| ZT-RV-001 | NOT_IMPLEMENTED | NOT_VALIDATED | PENDING |
| ZT-SCH-001 | NOT_IMPLEMENTED | NOT_VALIDATED | PENDING |

## Completion gates

1. Preserve truthful FND, NET, VIS, and ID boundaries.
2. Keep CV blocked until its four predecessor states and evidence pass their current gates together; the 2026-07-27 run exposed an FND warning-budget blocker.
3. Implement RV only after CV acceptance and prove deterministic repeated execution.
4. Implement SCH only after RV acceptance and separate scheduler approval.
5. Accept Phase 1 only after every required predecessor is accepted and evidence remains sanitized and current.

## Current decision

- Implementation: PARTIAL
- Validation: PARTIALLY_VALIDATED
- Completion: NOT_COMPLETE
- Boundary: ZT-SCH-001

ZT-NET-001 acceptance is limited to one bounded directional inter-zone ACL, ZT-VIS-001 acceptance is limited to four sanitized summary sources and one single-node local telemetry stack, and ZT-ID-001 acceptance is limited to one bounded non-production validator endpoint. ZT-CV-001 has implemented read-only tooling and partial runtime evidence, but its current FND gate is `REVIEW_REQUIRED` because one warning exceeds the configured budget of zero. Persistent NTP synchronization, central visibility, broader segmentation, centralized identity, MFA, OIDC, application RBAC, production enforcement, and maturity remain open. Retiring the scenario framework does not satisfy a package gate, create runtime evidence, assign maturity, or authorize a live target.
