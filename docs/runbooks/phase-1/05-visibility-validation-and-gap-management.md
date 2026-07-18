# Visibility Validation and Gap Management

```json runbook-metadata
{
  "runbook_id": "RB-P1-005",
  "title": "Visibility Validation and Gap Management",
  "phase": "PHASE_1",
  "related_packages": ["ZT-VIS-001", "ZT-VIS-002"],
  "owner_domain": "VISIBILITY_AND_ANALYTICS",
  "supported_target_types": ["REPOSITORY_LOCAL", "BOUNDED_NON_PRODUCTION_TELEMETRY_SOURCES"],
  "procedure_status": "PARTIALLY_IMPLEMENTED",
  "validation_status": "PARTIALLY_RUNTIME_VALIDATED",
  "runtime_required": true,
  "live_execution_permitted": true,
  "required_authority": "EXPLICIT_OPERATOR_APPROVAL_FOR_COLLECTION",
  "evidence_authority": "CODEX_EXECUTED_LIVE_RUNTIME",
  "last_reviewed": "2026-07-19",
  "limitations": ["ZT-VIS-001 has no accepted central monitoring service or persistent storage; ZT-VIS-002 is protected Phase 2 preparation only."]
}
```

## Purpose

Validate the existing bounded telemetry pipeline and manage visibility gaps
without deploying or changing monitoring services.

## Scope

Static source/schema/rule validation, separately authorized bounded collection,
evidence sanitization, ZT-VIS-001 gap preservation, and ZT-VIS-002 protection.

## Related Phase

Phase 1 for ZT-VIS-001. ZT-VIS-002 remains Phase 2 enabling preparation.

## Related Package or Governance Action

ZT-VIS-001 package and evidence records; P1-REC-002 protection for ZT-VIS-002.

## Supported Target Types

Repository-local telemetry assets and the four existing bounded validator
sources. No central log service is an available target.

## Current Procedure Status

`PARTIALLY_IMPLEMENTED`: local normalization and deterministic correlation
exist; centralized service and persistent retention do not.

## Current Validation Status

`PARTIALLY_RUNTIME_VALIDATED` from the existing bounded ZT-VIS-001 run only.

## Evidence Authority

Existing ZT-VIS-001 authority is `CODEX_EXECUTED_LIVE_RUNTIME`. Protected
ZT-VIS-002 preparation has no package or evidence authority.

## Required Authority

Static telemetry validation is repository-local and read-only. New collection
requires explicit operator approval. Deployment, ports, volumes, persistence,
identity integration, or service changes require a separate package action.

## User-Performed Physical or Approval Steps

Approve future bounded collection and separately approve any monitoring VM,
service, storage, retention, network, or identity design before implementation.

## Codex or Automation-Managed Steps

Validate inventory, schemas, rules, controlled fixtures, and sanitized records;
collect only through the existing bounded workflow when separately approved.

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

Confirm ZT-VIS-001 remains `IMPLEMENTED` / `PARTIALLY_VALIDATED`; central log
source is absent; gaps `CENTRAL_MONITORING_SERVICE_ABSENT` and
`PERSISTENT_STORAGE_EVIDENCE_MISSING` remain open; ZT-VIS-002 is
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

3. Preserve unavailable central-log-service state and the two named gaps.
4. Use controlled fixture findings only to validate rule behavior; never
   present them as live findings.
5. Do not read, hash, copy, modify, deploy, or accept ZT-VIS-002 preparation
   traces in this action.

## Expected Output

Static validation findings and, only after separate approval, bounded source
counters with sanitization and limitations. The output must distinguish live
findings from controlled fixtures and retain absent central storage.

## Validation

Validate inventory, event/finding schemas, deterministic rules, source counts,
raw ignore state, sanitized references, and package claims. No dashboard or
persistent retention is inferred.

## Pass Criteria

Static validator succeeds; approved sources remain bounded; raw output stays
ignored; controlled fixture is labeled; gaps remain explicit; no monitoring or
identity service changes occur.

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

Future closure needs an approved central service design, least-privilege source
onboarding, persistent storage and retention evidence, availability/recovery
testing, protected access, query/dashboards acceptance, data minimization, and
rollback. None is implemented here.

## Related Architecture

`docs/zero-trust/packages/zt-vis-001-centralized-telemetry-foundation.md` and
the Phase 1 dependency map.

## Related Runbooks

RB-P1-003 for sanitization and RB-P1-007 for future repeatability.
