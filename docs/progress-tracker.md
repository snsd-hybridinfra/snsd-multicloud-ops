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
| ZT-RV-001 | IMPLEMENTED | LOCAL_VALIDATED | VALIDATED | ACCEPTED | UNASSESSED | Bounded EC4 for the selected three-run campaign; no schedule or EC5 |
| ZT-SCH-001 | IMPLEMENTED | LOCAL_VALIDATED | NOT_VALIDATED | PENDING | UNASSESSED | Bounded catch-up installed; 0/3 successful correlated scheduled dates |

## Phase 1

- Implementation: PARTIAL
- Validation: PARTIALLY_VALIDATED
- Completion: NOT_COMPLETE
- Scope boundary: ZT-SCH-001

Progress is not calculated from a scenario count or a repository-wide percentage.

The 2026-07-28 remediated CV execution completed 8 PASS / 2 WARN / 0 FAIL with
zero blocked or review-required gates. Three RV campaign executions are now
accepted at bounded EC4 with stable fingerprints, 24-hour separation, and no
blocking failure. ZT-SCH-001 retained six failed sanitized candidates from
2026-08-03 through 2026-08-08 and has zero accepted scheduled dates; bounded
09:00-11:00 catch-up was installed on 2026-08-11. The bounded ZT-ID-001 evidence was revalidated on 2026-07-30
with 20/20 positive and 42/42 denied checks. Seven other current evidence
streams are now stale review findings; no acceptance, maturity, or Phase 1
completion is inferred from the RV result. ZT-SCH-001 remains the boundary.
