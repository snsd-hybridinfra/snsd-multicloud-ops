# P1-REC-001 Adoption Plan

This plan is deterministic but unexecuted. Every future operation requires a fresh hash check against `recovery-snapshot.yaml` and explicit approval.

## Group 0 — Mandatory blockers

Files: none currently classified as changed, unreadable, missing, secret-bearing, or in a Git operation state.

- Proposed operation: stop the future adoption action if any candidate hash, HEAD, origin relation, tracked-runtime count, secret result, or protected-owner state changes.
- Prerequisite: approvals P1REC-D001 through P1REC-D004.
- Validation: repeat the baseline and secret gates.
- Rollback: no operation begins.
- Approval requirement: recovery owner.
- Implementation-claim impact: none.
- Package-status impact: none.

## Group 1 — Recovery governance artifacts

Files:

- `docs/zero-trust/phase-1-recovery-audit.md`
- `docs/zero-trust/phase-1-recovery-audit.yaml`
- `docs/zero-trust/recovery/P1-REC-001/README.md`
- `docs/zero-trust/recovery/P1-REC-001/recovery-snapshot.yaml`
- `docs/zero-trust/recovery/P1-REC-001/file-disposition.yaml`
- `docs/zero-trust/recovery/P1-REC-001/adoption-plan.md`
- `docs/zero-trust/recovery/P1-REC-001/protected-files.yaml`
- `docs/zero-trust/recovery/P1-REC-001/validation-report.md`

- Proposed operation: adopt unchanged as recovery provenance after hash review.
- Prerequisite: P1-0/P1-REC-001 consistency review.
- Validation: parse YAML/Markdown, verify links, recompute hashes.
- Rollback: revert only the future reviewed adoption patch.
- Approval requirement: recovery owner.
- Implementation-claim impact: none.
- Package-status impact: none.

## Group 2 — Existing Phase 1 package recovery

Files:

- `docs/implementation-log.md`
- `docs/progress-tracker.md`
- `docs/risk-register.md`
- `docs/zero-trust/capability-implementation-backlog.yaml`
- `docs/zero-trust/current-baseline-assessment.md`
- `docs/zero-trust/current-baseline-assessment.yaml`
- `docs/zero-trust/gap-register.md`
- `docs/zero-trust/implementation-roadmap.md`
- `docs/zero-trust/prioritized-implementation-queue.md`
- `docs/zero-trust/README.md`
- `README.md`

- Proposed operation: merge approved hunks into the same tracked paths; do not replace the HEAD files wholesale.
- Prerequisite: P1REC-D001 and per-hunk claim review.
- Validation: Zero Trust validator 34/34, sync 5/5, report check, repository structure, full tests, diff review.
- Rollback: revert only the future merge patch while preserving this snapshot.
- Approval requirement: governance and package owners.
- Implementation-claim impact: no promotion beyond existing bounded/partial states.
- Package-status impact: ZT-FND-001, ZT-NET-001, and ZT-VIS-001 statuses remain unchanged unless separately evidenced and approved.

## Group 3 — Phase 1 gap-remediation candidates

Files: none in this recovered set qualify as implementation or runtime evidence.

- Proposed operation: no adoption.
- Prerequisite: a separate approved gap-remediation action.
- Validation: package-specific, scenario-locked evidence.
- Rollback: not applicable.
- Approval requirement: separate package owner approval.
- Implementation-claim impact: none.
- Package-status impact: none.

## Group 4 — Active monitoring work

Files:

- `.runtime/zero-trust/zt-vis-002/docker-runtime-install.raw.txt`
- `.runtime/zero-trust/zt-vis-002/inspect-docker-install.ps1`
- `.runtime/zero-trust/zt-vis-002/install-docker-runtime.ps1`
- `.runtime/zero-trust/zt-vis-002/monitoring-base-validation.raw.txt`

- Proposed operation: keep ignored and protected; do not merge into tracked paths during recovery.
- Prerequisite: P1REC-D004 plus a separate monitoring-package and sanitization approval.
- Validation: metadata-only during recovery; later runtime validation must be separately authorized.
- Rollback: not applicable because no operation is authorized here.
- Approval requirement: monitoring/runtime owner.
- Implementation-claim impact: Docker readiness only; no deployment, ingestion, or persistence claim.
- Package-status impact: ZT-VIS-002 remains without tracked package authority and NOT_VALIDATED.

## Group 5 — Target architecture

Files:

- `docs/adr/0003-advanced-maturity-implementation-target.md`
- `docs/adr/0004-iac-cac-pac-responsibility-boundaries.md`
- `docs/adr/0005-portable-vm-physical-onboarding.md`
- `docs/adr/0006-policy-gated-operations.md`
- `docs/adr/0007-optimal-ready-extension-interfaces.md`
- `docs/adr/0008-runbook-backed-operator-handoff.md`
- `docs/zero-trust/packages/zt-arc-001-advanced-target-architecture.md`
- `docs/zero-trust/packages/zt-arc-001-package.yaml`
- `docs/zero-trust/packages/zt-arc-001-rollback.md`
- `docs/zero-trust/target-architecture/advanced-maturity-acceptance-model.md`
- `docs/zero-trust/target-architecture/advanced-maturity-acceptance-model.yaml`
- `docs/zero-trust/target-architecture/advanced-maturity-scope.md`
- `docs/zero-trust/target-architecture/advanced-maturity-scope.yaml`
- `docs/zero-trust/target-architecture/capability-selection.yaml`
- `docs/zero-trust/target-architecture/capability-selection-method.md`
- `docs/zero-trust/target-architecture/capability-traceability-matrix.md`
- `docs/zero-trust/target-architecture/capability-traceability-matrix.yaml`
- `docs/zero-trust/target-architecture/golden-path.md`
- `docs/zero-trust/target-architecture/handoff-acceptance-model.md`
- `docs/zero-trust/target-architecture/handoff-acceptance-model.yaml`
- `docs/zero-trust/target-architecture/host-onboarding-contract.md`
- `docs/zero-trust/target-architecture/host-onboarding-contract.yaml`
- `docs/zero-trust/target-architecture/iac-cac-pac-reference-architecture.md`
- `docs/zero-trust/target-architecture/implementation-dependency-map.md`
- `docs/zero-trust/target-architecture/implementation-dependency-map.yaml`
- `docs/zero-trust/target-architecture/limitations.md`
- `docs/zero-trust/target-architecture/operator-interface-contract.md`
- `docs/zero-trust/target-architecture/portfolio-positioning.md`
- `docs/zero-trust/target-architecture/project-objective.md`
- `docs/zero-trust/target-architecture/README.md`
- `docs/zero-trust/target-architecture/target-portability-architecture.md`
- `profiles/templates/existing-vm/profile.yaml`
- `profiles/templates/openstack-vm/profile.yaml`
- `profiles/templates/physical-server/profile.yaml`
- `schemas/zero-trust-advanced-acceptance.schema.json`
- `schemas/zero-trust-advanced-maturity-scope.schema.json`
- `schemas/zero-trust-capability-selection.schema.json`
- `schemas/zero-trust-capability-traceability.schema.json`
- `schemas/zero-trust-handoff-acceptance.schema.json`
- `schemas/zero-trust-host-onboarding-contract.schema.json`
- `schemas/zero-trust-implementation-dependency-map.schema.json`
- `schemas/zero-trust-optimal-roadmap.schema.json`
- `schemas/zero-trust-target-profile.schema.json`
- `tests/test_advanced_target_architecture.py`
- `tools/validate_advanced_target_architecture.py`

- Proposed operation: normalize design-only wording, future-ID boundaries, path authority, links, and schema ownership; then adopt only approved files.
- Prerequisite: P1REC-D002, architecture review, unchanged hashes, and no overlap overwrite.
- Validation: recovered validator 28/28, 61-test suite, JSON/Markdown/Python parsing, Zero Trust validation, scenario lock.
- Rollback: revert only the future architecture adoption patch; preserve this recovery snapshot.
- Approval requirement: architecture and Zero Trust governance owners.
- Implementation-claim impact: remains design-only; local validation is not runtime validation.
- Package-status impact: ZT-ARC-001 may become an approved governance package only after review; it cannot alter actual package states.

## Group 6 — Future phase designs

Files:

- `docs/zero-trust/target-architecture/optimal-expansion-roadmap.md`
- `docs/zero-trust/target-architecture/optimal-expansion-roadmap.yaml`
- `docs/zero-trust/target-architecture/optimal-readiness-architecture.md`
- `docs/zero-trust/target-architecture/phase-roadmap.md`

- Proposed operation: adopt only as clearly labeled roadmap/design material after phase and package-ID review.
- Prerequisite: P1REC-D002 and explicit confirmation that future IDs are nonauthoritative.
- Validation: schema, link, duplicate-ID, scenario-lock, and prohibited-claim checks.
- Rollback: revert only the future roadmap adoption patch.
- Approval requirement: architecture and scope owners.
- Implementation-claim impact: none; future-phase design is not Phase 1 evidence.
- Package-status impact: no package becomes implemented, validated, or operational.

## Group 7 — Rejected, superseded, or nonauthoritative files

No file is currently proposed for deletion, rejection, or supersession. The following remain nonauthoritative references:

- `docs/architecture.md`
- `docs/runbooks/00-platform-overview.md`
- `docs/runbooks/01-prerequisites.md`
- `docs/runbooks/02-target-selection.md`
- `docs/runbooks/03-openstack-vm-onboarding.md`
- `docs/runbooks/04-existing-vm-onboarding.md`
- `docs/runbooks/05-physical-server-onboarding.md`
- `docs/runbooks/06-environment-profile.md`
- `docs/runbooks/07-secret-preparation.md`
- `docs/runbooks/08-preflight-validation.md`
- `docs/runbooks/09-iac-plan.md`
- `docs/runbooks/10-policy-evaluation.md`
- `docs/runbooks/11-deployment-approval.md`
- `docs/runbooks/12-platform-deployment.md`
- `docs/runbooks/13-runtime-validation.md`
- `docs/runbooks/14-platform-status.md`
- `docs/runbooks/15-drift-detection.md`
- `docs/runbooks/16-reconciliation.md`
- `docs/runbooks/17-backup.md`
- `docs/runbooks/18-restore.md`
- `docs/runbooks/19-rollback.md`
- `docs/runbooks/20-upgrade.md`
- `docs/runbooks/21-secret-rotation.md`
- `docs/runbooks/22-certificate-rotation.md`
- `docs/runbooks/23-incident-response.md`
- `docs/runbooks/24-target-replacement.md`
- `docs/runbooks/25-decommission.md`
- `docs/runbooks/26-evidence-handling.md`
- `docs/runbooks/27-operator-handoff.md`
- `docs/runbooks/28-troubleshooting.md`
- `docs/runbooks/README.md`
- `docs/runbooks/RUNBOOK_INDEX.md`
- `docs/runbooks/RUNBOOK_TEMPLATE.md`

- Proposed operation: retain unchanged; optionally merge unique approved content into canonical tracked paths in a later action.
- Prerequisite: P1REC-D003 and an exact source-to-target map.
- Validation: duplicate-content, link, claim, and operator-authority review.
- Rollback: retain the snapshot and revert only any later approved merge.
- Approval requirement: documentation/runbook owners.
- Implementation-claim impact: none.
- Package-status impact: none.

## Exactly one next action

```yaml
action_id: P1-REC-002
objective: Apply the approved non-destructive recovery adoption plan.
rationale: The files are stable and classified, but four authority and ordering decisions still require explicit human approval.
prerequisites:
  - Approve P1REC-D001 through P1REC-D004.
  - Revalidate every candidate SHA-256 and the Git baseline.
  - Keep ignored runtime and existing package evidence protected.
authorized_files:
  - Only candidate and recovery-governance files explicitly approved in the four decisions.
protected_files:
  - All paths in protected-files.yaml.
expected_outputs:
  - One reviewable non-destructive adoption patch.
  - Updated hash and validation record.
validation:
  - Zero Trust 34/34 and sync 5/5.
  - Recovered architecture 28/28 and full tests.
  - Repository structure, scenario lock, secret scan, and diff checks.
stop_conditions:
  - Any candidate hash changes.
  - A concurrent writer or Git operation state appears.
  - A likely real tracked secret or tracked runtime file appears.
  - Approval scope is incomplete or conflicts with monitoring ownership.
```

P1-REC-002 is selected but not executed.
