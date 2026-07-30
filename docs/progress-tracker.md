# Package Progress Tracker

Machine-readable authority: `docs/zero-trust/package-flow.yaml` and the corresponding package metadata and evidence records.

| Package | Implementation | Local validation | Runtime validation | Acceptance | Maturity | Blocking boundary |
|---|---|---|---|---|---|---|
| ZT-ARC-001 | DESIGN_ONLY | LOCAL_VALIDATED | NOT_VALIDATED | DESIGN_ONLY | UNASSESSED | Architecture is not runtime implementation |
| ZT-FND-001 | IMPLEMENTED | LOCAL_VALIDATED | VALIDATED | BOUNDED_ACCEPTED | UNASSESSED | Bounded non-production scope |
| ZT-NET-001 | IMPLEMENTED | LOCAL_VALIDATED | VALIDATED | ACCEPTED | UNASSESSED | One bounded directional ACL; broader network controls remain open |
| ZT-VIS-001 | IMPLEMENTED | LOCAL_VALIDATED | VALIDATED | ACCEPTED | UNASSESSED | Four sanitized summary sources and one single-node local stack; central visibility remains open |
| ZT-ID-001 | IMPLEMENTED | LOCAL_VALIDATED | VALIDATED | ACCEPTED | UNASSESSED | One bounded non-production endpoint; centralized identity remains open |
| ZT-CV-001 | IMPLEMENTED | LOCAL_VALIDATED | PARTIALLY_VALIDATED | PARTIALLY_ACCEPTED | UNASSESSED | Bounded EC3 only; explicit package gaps remain |
| ZT-RV-001 | IMPLEMENTED | LOCAL_VALIDATED | PARTIALLY_VALIDATED | REPEATABILITY_PROVISIONAL | UNASSESSED | Two of three eligible executions accepted; final run requires PT24H separation |
| ZT-SCH-001 | NOT_IMPLEMENTED | NOT_VALIDATED | NOT_VALIDATED | PENDING | UNASSESSED | RV repeatability acceptance required |

## Phase 1

- Implementation: PARTIAL
- Validation: PARTIALLY_VALIDATED
- Completion: NOT_COMPLETE
- Scope boundary: ZT-SCH-001

Progress is not calculated from a scenario count or a repository-wide percentage.

The 2026-07-28 remediated CV execution completed 8 PASS / 2 WARN / 0 FAIL with
zero blocked or review-required gates. Two RV campaign executions are accepted
at EC3 with a provisional repeatability result; one additional eligible
consecutive success after at least 24 hours is still required for EC4. The
bounded ZT-ID-001 evidence was revalidated on 2026-07-30 with 20/20 positive,
42/42 denied, and zero current freshness regressions without changing its scope.
