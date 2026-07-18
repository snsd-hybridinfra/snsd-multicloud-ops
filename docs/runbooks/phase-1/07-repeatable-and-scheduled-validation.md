# Repeatable and Scheduled Validation

```json runbook-metadata
{
  "runbook_id": "RB-P1-007",
  "title": "Repeatable and Scheduled Validation",
  "phase": "PHASE_1",
  "related_packages": ["ZT-CV-001", "ZT-RV-001", "ZT-SCH-001"],
  "owner_domain": "VALIDATION_OPERATIONS",
  "supported_target_types": ["REPOSITORY_LOCAL_DESIGN_REVIEW"],
  "procedure_status": "DESIGN_SPECIFICATION",
  "validation_status": "VALIDATED_LOCAL",
  "runtime_required": true,
  "live_execution_permitted": false,
  "required_authority": "FUTURE_PACKAGE_AND_SCHEDULER_APPROVAL",
  "evidence_authority": "NONE",
  "last_reviewed": "2026-07-19",
  "limitations": ["No continuous-validation, repeatable-validation, or scheduler package, job, service, or runtime evidence exists."]
}
```

## Purpose

Define how bounded validations could become deterministic, repeatable, and
eventually scheduled without creating a scheduler or claiming continuous
operation.

## Scope

Design requirements for sequencing, input pinning, isolation, concurrency,
timeouts, retries, evidence retention, alerting, approval gates, and scheduler
failure/rollback.

## Related Phase

Phase 1 boundary design only. Phase 1 remains incomplete and no scheduled
operation is accepted.

## Related Package or Governance Action

ZT-CV-001 and ZT-RV-001 are `ABSENT`, non-authoritative, `NOT_IMPLEMENTED`, and
`NOT_VALIDATED`. ZT-SCH-001 is `DESIGN_ONLY`, `NOT_IMPLEMENTED`, and
`NOT_VALIDATED`; no scheduler, scheduled job, or operational schedule exists.

## Supported Target Types

Repository-local design review. No cron, Windows Task Scheduler, CI workflow,
systemd timer, orchestrator, monitoring job, or runtime target is approved.

## Current Procedure Status

`DESIGN_SPECIFICATION`.

## Current Validation Status

`VALIDATED_LOCAL` means the design and non-claim boundaries were checked only.
The three referenced package concepts remain `NOT_VALIDATED`.

## Evidence Authority

`NONE` for repeatable, continuous, or scheduled operation.

## Required Authority

Approved package ownership, scheduler technology decision, security review,
secret-free execution identity, target approvals, retention policy, failure
owner, service-impact review, and tested disable/rollback.

## User-Performed Physical or Approval Steps

Approve future scheduler technology, maintenance windows, target list,
notification destinations, service account boundary, retention, and emergency
disable owner.

## Codex or Automation-Managed Steps

After approval, implement deterministic manifests, read-only default execution,
locking, timeout/retry controls, structured results, sanitization, tests, and a
disabled-by-default schedule definition.

## Prerequisites

Stable package validators; RB-P1-002 repository-safe entry; package-specific
runbooks; deterministic inputs; version pinning; bounded target profiles;
authority per target; concurrency and timeout policy; retention and escalation;
tested disable and rollback.

## Inputs

Validator catalog, dependency graph, package status, target class, approved
window, timeout, retry budget, concurrency key, result schema, evidence policy,
and notification/escalation route.

## Secret Inputs

No scheduler secret may reside in Git, arguments, logs, environment files, or
evidence. A future external secret mechanism and least-privilege execution
identity require separate approval and validation.

## Service Impact

None today. Future scheduled validation may consume target capacity or create
read load and must remain read-only unless a separate mutating runbook and
approval explicitly authorize otherwise.

## Security Impact

Automation can amplify scope, credential, denial-of-service, evidence leakage,
and repeated-failure risks. Default-deny targets, single-run locks, bounded
timeouts, redaction, and emergency disable are required.

## Preflight Checks

Confirm all three concepts remain non-operational; dependencies have current
authority; no live or mutating validator is silently included; default
repository-safe mode is used; scenarios remain bounded to S001-S050; and
CI/scheduler artifacts are absent.

## Procedure

1. Define a catalog that records command status, target, authority, expected
   duration, timeout, retry policy, evidence, and rollback for every validator.
2. Sequence repository-local static validation before separately authorized
   runtime validation; stop dependent runs after a prerequisite defect.
3. Require immutable input versions, deterministic output schemas, idempotent
   read-only behavior, unique run IDs, and source-repository immutability.
4. Define one concurrency key per repository/target and reject overlapping runs.
5. Define hard timeouts, no automatic retry for policy/security/authorization
   failures, and a small reviewed retry budget for transient transport only.
6. Route raw output to ignored runtime storage and retain sanitized summaries
   under RB-P1-003 with bounded retention.
7. Define schedule enable/disable, missed-run, clock/time-zone, notification,
   audit, health, and rollback acceptance criteria.
8. Keep every schedule disabled and unimplemented until a separate action is
   approved and runtime validated.

No exact scheduler command or job definition exists. Presenting one as
executable is prohibited in the current phase.

## Expected Output

For a future approved action: machine-readable validator catalog, dependency
order, concurrency/timeout/retry policy, disabled schedule definition, result
schema, sanitization/retention policy, health checks, and disable/rollback plan.

## Validation

Current validation checks document structure and absence of operational claims.
Future validation must cover deterministic repeated runs, overlap rejection,
timeout, retry classification, missed run, disabled state, target isolation,
evidence sanitation, notification, and scheduler recovery.

## Pass Criteria

For design readiness: every validator is classified; runtime actions remain
approval-gated; sequencing and failure propagation are deterministic; scheduler
enablement is disabled; evidence and rollback contracts are complete.

## Stop Conditions

Unapproved scheduler/job creation, CI automation, live target, credential,
silent retry, unbounded concurrency, missing timeout, mutating validator in a
read-only group, raw evidence retention, unsupported package claim, or missing
disable owner.

## Failure Handling

Stop dependent work, classify content failure separately from orchestrator
failure, preserve sanitized diagnostics, avoid automatic remediation, and
require human review before re-enable.

## Rollback

Future rollback must disable new triggers first, stop queued work, preserve the
last accepted catalog, revoke only the scheduler execution identity through its
owner, verify no job remains active, and revalidate repository state.

## Evidence

No operational evidence exists. Future records require run ID, schedule/version,
executor, target class, start/end, exit semantics, per-validator status,
timeouts/retries, overlap decision, sanitized references, limitations, and
explicit schedule-enabled state.

## Escalation

Escalate scheduler technology, execution identity, live target scope,
notification/retention, repeated failures, missed runs, service impact, and
enable/disable authority.

## Known Limitations

This runbook creates no ZT-CV-001, ZT-RV-001, or ZT-SCH-001 package; no job,
timer, CI workflow, service account, notification integration, or runtime
validation is present. Repeatability and scheduling remain future work.

## Related Architecture

`docs/zero-trust/target-architecture/implementation-dependency-map.md` and
`docs/zero-trust/target-architecture/phase-roadmap.md`.

## Related Runbooks

RB-P1-002 for repository-safe execution, RB-P1-003 for evidence, and RB-P1-004
through RB-P1-006 for package-specific boundaries.
