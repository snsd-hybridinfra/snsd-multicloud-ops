# Package Progress Tracker

Machine-readable authority: `docs/zero-trust/package-flow.yaml` and the corresponding package metadata and evidence records.

| Package | Implementation | Local validation | Runtime validation | Acceptance | Maturity | Blocking boundary |
|---|---|---|---|---|---|---|
| ZT-ARC-001 | DESIGN_ONLY | LOCAL_VALIDATED | NOT_VALIDATED | DESIGN_ONLY | UNASSESSED | Architecture is not runtime implementation |
| ZT-FND-001 | IMPLEMENTED | LOCAL_VALIDATED | VALIDATED | BOUNDED_ACCEPTED | UNASSESSED | Bounded non-production scope |
| ZT-NET-001 | IMPLEMENTED_AS_RECORDED | LOCAL_VALIDATED | PARTIALLY_VALIDATED | PARTIALLY_ACCEPTED | UNASSESSED | Control coverage remains partial |
| ZT-VIS-001 | IMPLEMENTED | LOCAL_VALIDATED | PARTIALLY_VALIDATED | PARTIALLY_ACCEPTED | UNASSESSED | Visibility coverage remains partial |
| ZT-ID-001 | IMPLEMENTED | LOCAL_VALIDATED | VALIDATED | ACCEPTED | UNASSESSED | One bounded non-production endpoint; centralized identity remains open |
| ZT-CV-001 | NOT_IMPLEMENTED | NOT_VALIDATED | NOT_VALIDATED | PENDING | UNASSESSED | Predecessor acceptance required |
| ZT-RV-001 | NOT_IMPLEMENTED | NOT_VALIDATED | NOT_VALIDATED | PENDING | UNASSESSED | CV acceptance required |
| ZT-SCH-001 | NOT_IMPLEMENTED | NOT_VALIDATED | NOT_VALIDATED | PENDING | UNASSESSED | RV repeatability acceptance required |

## Phase 1

- Implementation: PARTIAL
- Validation: PARTIALLY_VALIDATED
- Completion: NOT_COMPLETE
- Scope boundary: ZT-SCH-001

Progress is not calculated from a scenario count or a repository-wide percentage.
