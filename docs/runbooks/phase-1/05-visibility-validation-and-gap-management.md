# Visibility Validation and Gap Management

```json runbook-metadata
{
  "runbook_id": "RB-P1-005",
  "title": "Visibility Validation and Gap Management",
  "phase": "PHASE_1",
  "related_packages": ["ZT-VIS-001", "ZT-VIS-002"],
  "owner_domain": "VISIBILITY_AND_ANALYTICS",
  "supported_target_types": ["REPOSITORY_LOCAL", "BOUNDED_NON_PRODUCTION_TELEMETRY_SOURCES", "BOUNDED_NON_PRODUCTION_MONITORING_VM"],
  "procedure_status": "IMPLEMENTED",
  "validation_status": "PARTIALLY_RUNTIME_VALIDATED",
  "runtime_required": true,
  "live_execution_permitted": true,
  "required_authority": "EXPLICIT_OPERATOR_APPROVAL_FOR_COLLECTION",
  "evidence_authority": "CODEX_EXECUTED_LIVE_RUNTIME",
  "last_reviewed": "2026-07-22",
  "limitations": ["ZT-VIS-001 persistent storage accepts only approved sanitized JSONL; host journals, full service logs, external alerting, high availability, behavior analytics, and automated response remain absent. ZT-VIS-002 remains protected Phase 2 preparation only."]
}
```

## Purpose

Validate the existing bounded telemetry pipeline and accepted persistent
monitoring service without changing its approved scope.

## Scope

Static source/schema/rule validation, separately authorized bounded collection,
evidence sanitization, persistent-stack health and retention validation, and
ZT-VIS-002 protection.

## Related Phase

Phase 1 for ZT-VIS-001. ZT-VIS-002 remains Phase 2 enabling preparation.

## Related Package or Governance Action

ZT-VIS-001 package and evidence records; P1-REC-002 protection for ZT-VIS-002.

## Supported Target Types

Repository-local telemetry assets, the four existing bounded validator sources,
and the dedicated non-production monitoring VM.

## Current Procedure Status

`IMPLEMENTED`: local normalization, deterministic correlation, and bounded
persistent Grafana/Loki/Alloy storage exist.

## Current Validation Status

`PARTIALLY_RUNTIME_VALIDATED` for the bounded ZT-VIS-001 scope.

## Evidence Authority

Existing ZT-VIS-001 authority is `CODEX_EXECUTED_LIVE_RUNTIME`. Protected
ZT-VIS-002 preparation has no package or evidence authority.

## Required Authority

Static telemetry validation is repository-local and read-only. New collection
requires explicit operator approval. Deployment, ports, volumes, persistence,
identity integration, or service changes require a separate package action.

## User-Performed Physical or Approval Steps

Approve future bounded collection, restart-based persistence tests, and any
change to monitoring sources, service, storage, retention, network, or identity
design before implementation.

## Codex or Automation-Managed Steps

Validate inventory, schemas, rules, controlled fixtures, sanitized records,
service health, retention, and query behavior; collect only through the
existing bounded workflow when separately approved.

## Prerequisites

RB-P1-001 ready; ZT-VIS-001 sources and schemas consistent; raw runtime ignored;
collection scope approved; ZT-VIS-002 protected files untouched.

## Inputs

Telemetry inventory, schemas, deterministic rules, existing execution record,
source availability expectations, sanitization rules, and gap register.

## Secret Inputs

None. Do not collect credentials, tokens, private keys, raw cloud
configuration, full host journals, environment files, account values, or
unnecessary identifiers.

## Service Impact

Static validation has none. Bounded collection reads current source outputs and
writes ignored raw files; no monitoring service or target configuration may
change.

## Security Impact

Telemetry may expose sensitive topology or identity context. Source scope,
least privilege, raw-data isolation, and sanitization are mandatory.

## Preflight Checks

Confirm ZT-VIS-001 remains `IMPLEMENTED` / `VALIDATED`; the bounded central log
source is healthy and persistent-storage evidence remains accepted; ZT-VIS-002 is
`PREPARATION_TRACES_ONLY`, Phase 2, not deployed, `NOT_VALIDATED`, and not
evidence authority.

## Procedure

1. Run the repository-local validator to inspect inventory, schemas, rules, and
   bounded event files without changing services.

```json command-metadata
{
  "command": "python tools/telemetry/validate_telemetry_sources.py",
  "command_status": "AVAILABLE_READ_ONLY",
  "execution_owner": "CODEX_OR_AUTOMATION",
  "approval_required": false,
  "runtime_target": "REPOSITORY_LOCAL",
  "expected_effect": "Validate ZT-VIS-001 static sources, schemas, rules, events, and findings.",
  "evidence_output": "Console validation findings only.",
  "rollback_reference": "No rollback; validator is read-only."
}
```

2. If and only if separately approved, perform bounded live collection through
   the existing workflow.

```json command-metadata
{
  "command": "powershell -ExecutionPolicy Bypass -File tools/live-validation/collect-telemetry-live.ps1",
  "command_status": "AVAILABLE_MUTATING_APPROVAL_REQUIRED",
  "execution_owner": "CODEX_OR_AUTOMATION",
  "approval_required": true,
  "runtime_target": "BOUNDED_NON_PRODUCTION_TELEMETRY_SOURCES",
  "expected_effect": "Read the approved fixed sources and write ephemeral raw output only under ignored runtime storage.",
  "evidence_output": "Ignored raw JSONL and a separately reviewed sanitized summary.",
  "rollback_reference": "docs/zero-trust/packages/zt-vis-001-rollback.md"
}
```

3. Validate the accepted stack without changing its scope.

```json command-metadata
{
  "command": "powershell -ExecutionPolicy Bypass -File tools/live-validation/manage-persistent-telemetry.ps1 -Mode Validate",
  "command_status": "AVAILABLE_MUTATING_APPROVAL_REQUIRED",
  "execution_owner": "CODEX_OR_AUTOMATION",
  "approval_required": true,
  "runtime_target": "BOUNDED_NON_PRODUCTION_MONITORING_VM",
  "expected_effect": "Validate pinned healthy services, loopback endpoints, retention, and one synthetic sanitized event ingestion/query.",
  "evidence_output": "Ignored runtime output and a separately reviewed sanitized derivative.",
  "rollback_reference": "docs/zero-trust/packages/zt-vis-001-rollback.md"
}
```

4. Use `-Mode Persistence` only under explicit restart approval; it restarts
   the exact Compose project and proves pre/post-restart retrieval.
5. Use controlled fixture findings only to validate rule behavior; never
   present them as live findings.
6. Do not read, hash, copy, modify, deploy, or accept ZT-VIS-002 preparation
   traces in this action.

## Expected Output

Static validation findings and, only after separate approval, bounded source
counters with sanitization and limitations. The output must distinguish live
findings from controlled fixtures and bounded persistent storage from a
complete SIEM.

## Validation

Validate inventory, event/finding schemas, deterministic rules, source counts,
raw ignore state, sanitized references, pinned services, loopback endpoints,
retention, restart retrieval, and package claims.

## Pass Criteria

Static validator succeeds; approved sources remain bounded; raw output stays
ignored; controlled fixture is labeled; health, retention, ingestion, query,
and restart persistence pass; no unapproved monitoring or identity change
occurs.

## Stop Conditions

Unapproved collection, new source, service deployment, port/volume or retention
change, identity integration, raw runtime tracking, credentials, protected
ZT-VIS-002 access, behavior-analytics claim, complete-SIEM claim, or central
storage claim without accepted evidence.

## Failure Handling

Separate source, schema, rule, fixture, sanitization, and availability failures.
Do not bypass a failed source or convert it to success; retain partial status.

## Rollback

Static validation needs none. A separately approved collection may remove only
its bounded ignored temporary output. No service rollback applies because this
runbook does not deploy services.

## Evidence

Record executor, approved scope, source classifications, counters, fixture
label, raw-ignore result, sanitization, limitations, and open gaps. Never treat
ZT-VIS-002 traces as evidence.

## Escalation

Escalate any central monitoring/persistence design, new source, identity
dependency, protected-file access, or request to promote package status.

## Known Limitations

Future expansion needs separately approved least-privilege source onboarding,
availability design, external alerting, broader dashboards, data minimization,
and rollback. Current acceptance remains single-node and sanitized-input only.

## Related Architecture

`docs/zero-trust/packages/zt-vis-001-centralized-telemetry-foundation.md` and
the Phase 1 dependency map.

## Related Runbooks

RB-P1-003 for sanitization and RB-P1-007 for future repeatability.
