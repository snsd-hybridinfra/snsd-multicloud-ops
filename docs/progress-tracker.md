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
| ZT-SCH-001 | IMPLEMENTED | LOCAL_VALIDATED | NOT_VALIDATED | PENDING | UNASSESSED | Installed and disabled; deferred final Phase 5 gate; 0 accepted scheduled dates |
| ZT-VIS-002 | PARTIALLY_IMPLEMENTED | LOCAL_VALIDATED | PARTIALLY_VALIDATED | PARTIALLY_ACCEPTED | UNASSESSED | One private OpenStack target accepted at bounded EC3; alert delivery passed one-time runtime validation but status review, clock synchronization, elapsed retention, and full Cinder snapshot restore remain open |

## Phase 1

- Implementation: PARTIAL
- Validation: PARTIALLY_VALIDATED
- Completion: COMPLETED_WITH_GAPS
- Scope boundary: ZT-RV-001
- Acceptance decision: ACCEPTED_WITH_GAPS (`P1-RV-FRESHNESS-001`)
- Deferred final risk: STALE_RV_EVIDENCE
- RV freshness refresh: 1/3 eligible manual executions accepted
- Next RV execution not before: 2026-08-21T11:59:07.686986Z

## Phase 2

- Status: IN_PROGRESS
- Current action: P2-VIS-001
- Current package: ZT-VIS-002 partial bounded runtime
- Local artifacts: OpenStack Terraform and fail-closed Ansible static validation PASS
- Native tool validation: Terraform 1.15.9 `fmt/init(-backend=false)/validate` PASS; OpenStack provider 3.4.0 checksum lock tracked
- Ansible control node: dedicated Ubuntu 24.04 VMware Workstation VM with 2 vCPU, 4 GiB RAM, 30 GiB thin disk, NAT plus host-only networking, and ansible-core 2.16.3; key-only SSH, firewall, local ping, deploy/rollback syntax, negative access, and clean restart persistence checks PASS; WSL is stopped and is not an active authority
- Live-gate discovery: compute, network, image, flavor, security-group and recovery-key candidates were confirmed and used only within the explicitly authorized bounded deployment path
- Storage prerequisite: dedicated 100 GiB thin AIO disk, `cinder-volumes` LVM backend, block-storage service and volume-v3 endpoints are active; positive, unauthenticated-deny, invalid-token-deny, reboot-persistence and temporary-volume rollback checks PASS
- Deployment readiness: five Linux AMD64 manifests are digest fixed; private mTLS plus Grafana login, separated viewer/administrator/recovery roles, PT336H Cinder retention, volume reattachment and snapshot rollback are locally validated design decisions; signature, vulnerability, retention and restore runtime claims remain open
- External inputs: explicitly authorized administrator cloud profile, exact existing-private-resource Terraform values, mTLS CA/server/client material and Grafana administrator secret are present only on the dedicated control VM; hash, chain, server-name and `0600` checks PASS; no values are committed
- Terraform preflight: control-node Terraform 1.15.8 signature/archive verification, OpenStack provider authentication, backend-disabled init/validate/plan and sanitized plan review PASS; zero prior resources, four create actions, zero destructive actions and no state; raw plan and logs remain outside Git at `0600`
- Live deployment: bounded private OpenStack deployment and the separately authorized one-time validator PASS; positive, negative, bypass, restart persistence, package-only rollback, preserved-data recovery and evidence-integrity checks PASS; temporary restricted access removed and protected state, PKI, OCI archives and external raw log preserved
- Status decision: ZT-VIS-002 is conservatively promoted to `PARTIALLY_IMPLEMENTED / LOCAL_VALIDATED / PARTIALLY_VALIDATED / PARTIALLY_ACCEPTED` for one private non-production OpenStack monitoring VM at EC3
- Alert validation execution: Grafana 13.1.0 rule CRUD, missing/invalid-auth denial, exact-path bypass denial, and one-time webhook `v1` delivery PASS; all temporary rules, folders, listener, validator and recovery access were removed, five permanent components remain, and no permanent Contact Point or public listener was added
- Alert status boundary: the new sanitized evidence is `ALERT_VALIDATION_EXECUTED_STATUS_REVIEW_PENDING`; the alert gap is not automatically closed, and a target clock skew finding remains open because the time service has no upstream packets and no clock correction was authorized
- Completion boundary: P2-VIS-001 remains `IN_PROGRESS`; alert status review, target clock synchronization, elapsed-retention behavior, and full Cinder snapshot rebuild/reattachment restore remain open

Progress is not calculated from a scenario count or a repository-wide percentage.

The 2026-07-28 remediated CV execution completed 8 PASS / 2 WARN / 0 FAIL with
zero blocked or review-required gates. Three RV campaign executions are now
accepted at bounded EC4 with stable fingerprints, 24-hour separation, and no
blocking failure at their original assessment time. The 2026-08-20 acceptance
preflight found all three records older than P7D and accepted zero current
records. ADR 0014 preserves that stale result as a final-gate residual risk and
accepts Phase 1 with gaps for Phase 2 local preparation. A separately approved
manual read-only refresh on 2026-08-20 added one fresh eligible execution with
4 PASS / 6 WARN / 0 FAIL and no target change; the refresh window is 1/3 and
remains `STALE / EC3 / IN_PROGRESS` until two more PT24H-separated runs pass.
ZT-SCH-001 retained six failed sanitized candidates from
2026-08-03 through 2026-08-08 and has zero accepted scheduled dates; bounded
09:00-11:00 catch-up was installed on 2026-08-11. The bounded ZT-ID-001 evidence was revalidated on 2026-07-30
with 20/20 positive and 42/42 denied checks. Seven other current evidence
streams are now stale review findings; no freshness, maturity, or runtime
promotion is inferred from the exception. ZT-SCH-001 is installed and disabled
as the deferred final Phase 5 gate; it is not a Phase 1 predecessor.
