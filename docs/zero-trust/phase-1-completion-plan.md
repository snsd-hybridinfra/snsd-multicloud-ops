# Phase 1 Completion Plan

## Authority

The package flow in `docs/zero-trust/package-flow.yaml` is authoritative. ZT-ARC-001 surrounds, but is not a sequential member of, the flow.

```text
ZT-FND-001 -> ZT-NET-001 -> ZT-VIS-001 -> ZT-ID-001
           -> ZT-CV-001 -> ZT-RV-001 -> P1-ACC-001
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

ZT-SCH-001 remains `IMPLEMENTED / NOT_VALIDATED / PENDING`, but is installed,
disabled, and deferred to the final Phase 5 gate before P5-ACC-001.

## Completion gates

1. Preserve truthful FND, NET, VIS, and ID boundaries.
2. Preserve the accepted bounded CV decision and its explicit open gaps.
3. Preserve the accepted bounded RV decision and its three stable, separated execution records.
4. Accept Phase 1 only after every required predecessor through ZT-RV-001 is accepted and evidence remains sanitized and current.
5. Preserve the disabled SCH installation for separate final-gate validation; do not assign EC5 to Phase 1.

## Current decision

- Implementation: PARTIAL
- Validation: PARTIALLY_VALIDATED
- Completion: COMPLETED_WITH_GAPS
- Boundary: ZT-RV-001
- Acceptance decision: ACCEPTED_WITH_GAPS (`P1-RV-FRESHNESS-001`)
- Deferred final risk: STALE_RV_EVIDENCE

ZT-NET-001 acceptance is limited to one bounded directional inter-zone ACL, ZT-VIS-001 acceptance is limited to four sanitized summary sources and one single-node local telemetry stack, and ZT-ID-001 acceptance is limited to one bounded non-production validator endpoint. ZT-CV-001 is partially accepted at EC3, while ZT-RV-001 retains its historical bounded EC4 three-run decision. The 2026-08-20 P1-ACC-001 preflight found all three historical RV records older than P7D and accepted zero current records. The reviewed `P1-RV-FRESHNESS-001` exception permits Phase 2 local preparation but does not reclassify those records. A later separately approved manual read-only execution established refresh progress of 1/3 at EC3; two more PT24H-separated executions remain mandatory before final scheduling or P5-ACC-001. ZT-SCH-001 has an installed disabled task, eleven retained candidates, and zero accepted correlated dates; it is deferred to the final Phase 5 gate. Seven non-RV evidence streams also require freshness review. Persistent NTP synchronization, central visibility, broader segmentation, centralized identity, MFA, OIDC, application RBAC, production enforcement, scheduled-runtime acceptance, and maturity remain open. Retiring the scenario framework does not satisfy a package gate, create runtime evidence, assign maturity, or authorize a live target.
