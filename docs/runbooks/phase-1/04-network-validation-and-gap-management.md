# Network Validation and Gap Management

```json runbook-metadata
{
  "runbook_id": "RB-P1-004",
  "title": "Network Validation and Gap Management",
  "phase": "PHASE_1",
  "related_packages": ["ZT-NET-001"],
  "owner_domain": "NETWORK_SECURITY",
  "supported_target_types": ["REPOSITORY_LOCAL", "BOUNDED_NON_PRODUCTION_EVE_NG_ROUTER"],
  "procedure_status": "PARTIALLY_IMPLEMENTED",
  "validation_status": "PARTIALLY_RUNTIME_VALIDATED",
  "runtime_required": true,
  "live_execution_permitted": true,
  "required_authority": "EXPLICIT_OPERATOR_APPROVAL_AND_EXISTING_RESTRICTED_ENDPOINT",
  "evidence_authority": "CODEX_EXECUTED_LIVE_RUNTIME",
  "last_reviewed": "2026-07-19",
  "limitations": ["Existing bounded router evidence does not prove persistent interface ACL enforcement or complete micro-segmentation."]
}
```

## Purpose

Revalidate the bounded ZT-NET-001 network evidence safely and manage its
permanent ACL enforcement gap without changing router policy.

## Scope

Existing forced-command read-only router validation, static package checks,
evidence review, and gap acceptance planning. Configuration and remediation are
outside this runbook.

## Related Phase

Phase 1; ZT-NET-001 remains implemented as recorded and partially runtime
validated.

## Related Package or Governance Action

ZT-NET-001 package, validation record, rollback record, and current baseline.

## Supported Target Types

Repository-local package records and the already established bounded
non-production EVE-NG router restricted endpoint.

## Current Procedure Status

`PARTIALLY_IMPLEMENTED`: read-only validation exists; persistent ACL
implementation and its acceptance evidence do not.

## Current Validation Status

`PARTIALLY_RUNTIME_VALIDATED` from existing bounded evidence only.

## Evidence Authority

Existing package authority is `CODEX_EXECUTED_LIVE_RUNTIME`. This action does
not create new live authority.

## Required Authority

Repository-local inspection needs no extra approval. Any new live invocation
requires explicit operator approval and the existing fixed restricted endpoint.
Any configuration change requires a separate mutating action and rollback plan.

## User-Performed Physical or Approval Steps

Approve any future live revalidation and separately approve any proposed
persistent ACL change after reviewing blast radius and rollback.

## Codex or Automation-Managed Steps

Validate package records locally, invoke only the approved fixed read-only
command when separately authorized, sanitize output, and preserve the gap.

## Prerequisites

RB-P1-001 ready; ZT-FND-001 restricted endpoint boundary intact; ZT-NET-001
records consistent; fixed alias available; source evidence and sanitization
path approved.

## Inputs

Package metadata, existing validation record, fixed command contract, router
identity classification, expected check set, and gap register.

## Secret Inputs

None in Git or command arguments. Interactive credentials, router
configuration, raw addresses, MAC inventories, and private keys are prohibited.

## Service Impact

The approved validator is read-only. Persistent ACL configuration could affect
connectivity and is not authorized by this runbook.

## Security Impact

The restricted endpoint blocks interactive shell, arbitrary commands,
configuration commands, and arbitrary ping. Weakening that boundary is a stop.

## Preflight Checks

Confirm package state `IMPLEMENTED` / `PARTIALLY_VALIDATED`, current maturity
`UNASSESSED`, fixed alias/command, BatchMode, existing rollback record,
sanitized destination, and the unresolved gap
`PERMANENT_ACL_ENFORCEMENT_EVIDENCE_MISSING`.

## Procedure

1. Validate ZT-NET-001 machine records and references locally.
2. Review the prior bounded results: identity, interfaces, routing, and NAT
   evidence; access control remains partial without interface binding.
3. If a separately approved live revalidation exists, invoke only this command.

```json command-metadata
{
  "command": "ssh -o BatchMode=yes snsd-r1-validator validate-routing",
  "command_status": "LIVE_RUNTIME_REQUIRED",
  "execution_owner": "CODEX_OR_AUTOMATION",
  "approval_required": true,
  "runtime_target": "BOUNDED_NON_PRODUCTION_EVE_NG_ROUTER",
  "expected_effect": "Read fixed router-observable validation data through the restricted dispatcher; no configuration change.",
  "evidence_output": "Ignored raw output and a reviewed sanitized ZT-NET-001 derivative.",
  "rollback_reference": "docs/zero-trust/packages/zt-net-001-rollback.md"
}
```

4. Preserve segmentation classification as
   `SEGMENTATION_CONFIGURATION_ONLY` and access control as
   `PARTIAL_NO_INTERFACE_BINDING` unless new accepted evidence proves otherwise.
5. Keep the permanent ACL gap open. Do not enter configuration mode, bind an
   ACL, change a rule, or test arbitrary targets.
6. Record only sanitized evidence under RB-P1-003.

## Expected Output

Package/reference status, bounded read-only check categories, sanitized
counters when a separately authorized run occurs, unchanged limitations, and
the open permanent ACL gap. No fictional execution result is produced here.

## Validation

Static validation checks package consistency and restricted wrapper semantics.
Runtime validation, when separately approved, must use the exact fixed command
and must confirm the security boundary as well as routing results.

## Pass Criteria

Existing package facts remain consistent; restricted endpoint controls hold;
no configuration change occurs; evidence is sanitized; the ACL gap remains
explicit until its own acceptance criteria are met.

## Stop Conditions

Unapproved live request, non-fixed target or command, interactive shell,
configuration command, arbitrary ping, credential request, router identity
drift, service-impacting change, missing rollback, unsafe evidence, or proposal
to equate bounded macro separation with comprehensive per-workload enforcement.

## Failure Handling

Do not retry by broadening access. Classify transport, wrapper, router check,
sanitization, and evidence failures separately and keep package validation
partial.

## Rollback

Read-only validation needs no network rollback. For repository-only record
errors, correct the bounded derivative through review. ACL changes are not part
of this runbook and require their own approved rollback.

## Evidence

Retain command contract, executor, bounded target class, counters, security
boundary, sanitization result, and limitations. Never commit raw configuration
or dynamic identifiers.

## Escalation

Escalate any ACL implementation proposal, connectivity risk, security-boundary
failure, unknown router state, or request for broader access.

## Known Limitations

Future gap closure requires approved least-privilege ACL design, persistent
interface binding, before/after reachability results for fixed flows, denial
evidence for prohibited flows, configuration persistence evidence, security
boundary revalidation, and tested rollback. Until then the gap remains open.

## Related Architecture

`docs/zero-trust/packages/zt-net-001-router-validation.md` and the Phase 1
dependency map.

## Related Runbooks

RB-P1-003 for evidence and RB-P1-007 for future repeatability requirements.
