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
| ZT-CV-001 | IMPLEMENTED | PARTIALLY_VALIDATED | PARTIALLY_ACCEPTED |
| ZT-RV-001 | IMPLEMENTED | VALIDATED | ACCEPTED_AT_BOUNDED_EC4 |
| ZT-SCH-001 | IMPLEMENTED | NOT_VALIDATED | PENDING_0_OF_3 |

## Completion gates

1. Preserve truthful FND, NET, VIS, and ID boundaries.
2. Preserve the accepted bounded CV decision and its explicit open gaps.
3. Preserve the accepted bounded RV decision and its three stable, separated execution records.
4. Retain the explicitly approved SCH installation and accept it only after scheduled-runtime, failure, freshness, persistence, rollback, and evidence-integrity gates pass.
5. Accept Phase 1 only after every required predecessor is accepted and evidence remains sanitized and current.

## Current decision

- Implementation: PARTIAL
- Validation: PARTIALLY_VALIDATED
- Completion: NOT_COMPLETE
- Boundary: ZT-SCH-001

ZT-NET-001 acceptance is limited to one bounded directional inter-zone ACL, ZT-VIS-001 acceptance is limited to four sanitized summary sources and one single-node local telemetry stack, and ZT-ID-001 acceptance is limited to one bounded non-production validator endpoint. ZT-CV-001 is partially accepted at EC3, while ZT-RV-001 is accepted at bounded EC4 for the selected three-run campaign. ZT-SCH-001 has an installed locally validated task, six retained failed candidates, bounded catch-up, and zero successful correlated dates. Seven non-RV evidence streams currently require freshness review. Persistent NTP synchronization, central visibility, broader segmentation, centralized identity, MFA, OIDC, application RBAC, production enforcement, scheduled-runtime acceptance, and maturity remain open. Retiring the scenario framework does not satisfy a package gate, create runtime evidence, assign maturity, or authorize a live target.
