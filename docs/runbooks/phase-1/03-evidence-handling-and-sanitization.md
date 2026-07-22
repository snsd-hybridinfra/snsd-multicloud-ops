# Evidence Handling and Sanitization

```json runbook-metadata
{
  "runbook_id": "RB-P1-003",
  "title": "Evidence Handling and Sanitization",
  "phase": "PHASE_1",
  "related_packages": ["ZT-FND-001", "ZT-NET-001", "ZT-VIS-001", "ZT-DEV-001", "ZT-APP-001", "ZT-DATA-001", "ZT-SYS-001", "ZT-AUTO-001"],
  "owner_domain": "EVIDENCE_GOVERNANCE",
  "supported_target_types": ["REPOSITORY_LOCAL", "NON_PRODUCTION_LAB_EVIDENCE"],
  "procedure_status": "PARTIALLY_IMPLEMENTED",
  "validation_status": "VALIDATED_LOCAL",
  "runtime_required": false,
  "live_execution_permitted": false,
  "required_authority": "REVIEWED_SANITIZATION_AND_PACKAGE_EVIDENCE_AUTHORITY",
  "evidence_authority": "CODEX_EXECUTED_LOCAL",
  "last_reviewed": "2026-07-19",
  "limitations": ["The handling contract is locally validated; this action captured no new runtime evidence."]
}
```

## Purpose

Keep raw runtime material outside Git and retain only minimal, sanitized,
source-traceable evidence with an accurate execution authority.

## Scope

Evidence classification, raw-versus-sanitized storage, review gates, rejection
criteria, and references for the current bounded Phase 1 packages.

## Related Phase

Phase 1 evidence governance; it does not establish Phase 1 completion.

## Related Package or Governance Action

ZT-FND-001, ZT-NET-001, ZT-VIS-001, ZT-DEV-001, ZT-APP-001,
ZT-DATA-001, ZT-SYS-001, ZT-AUTO-001, ADR-0002, and Zero Trust governance.

## Supported Target Types

Repository-local validation records and sanitized evidence derived from a
separately authorized disposable non-production lab execution.

## Current Procedure Status

`PARTIALLY_IMPLEMENTED`: repository policies and examples exist, but evidence
review remains a human/automation gate for every new capture.

## Current Validation Status

`VALIDATED_LOCAL` for this handling contract only; no runtime was executed.

## Evidence Authority

Only `NONE`, `CODEX_EXECUTED_LOCAL`, `CODEX_EXECUTED_LIVE_RUNTIME`, and
`USER_EXECUTED_LIVE_RUNTIME` are allowed. Authority records who executed the
supporting action and is independent of evidence level and package status.

## Required Authority

The applicable package or scenario must already authorize the execution.
Tracking a sanitized derivative requires review of source, scope, executor,
target, checks, limitations, and sensitive-data removal.

## User-Performed Physical or Approval Steps

The user performs physical access, interactive secret entry, and explicitly
approved live or service-affecting actions. The user reviews ambiguous
redaction or evidence-authority decisions.

## Codex or Automation-Managed Steps

Keep raw capture in ignored runtime storage, normalize only necessary fields,
scan for sensitive values, bind evidence to existing authority, and validate
references before tracking.

## Prerequisites

Existing S001-S050 scenario or approved package record, declared executor and
environment, approved evidence path, known sanitization rules, and raw runtime
ignore protection.

## Inputs

Execution authority, source action, timestamp, bounded target description,
validator/version, counters, limitations, and the minimum output needed for the
acceptance decision.

## Secret Inputs

Secrets never enter evidence handling. Prohibited material includes passwords,
tokens, keys, certificates with private material, `clouds.yaml`,
`passwords.yml`, kubeconfig, `.env`, tfstate, account values, unnecessary UUID
or MAC collections, real host addresses, and raw terminal history.

## Service Impact

None in this runbook. It handles already-authorized output and does not contact
or modify a runtime target.

## Security Impact

Incorrect retention can expose credentials, infrastructure identity, network
topology, or personal data. Minimal disclosure and rejection on ambiguity are
mandatory.

## Preflight Checks

Confirm source authority exists; raw path is under ignored
`.runtime/zero-trust/`; destination is an approved evidence or recovery path;
no raw configuration is copied; executor and limitations are known; and no
scenario beyond S050 is referenced.

## Procedure

1. Write or retain raw output only under ignored `.runtime/zero-trust/` during
   the separately authorized execution.
2. Select only fields required by the existing acceptance criteria.
3. Replace environment-specific values with stable, non-reversible labels when
   they are not necessary; remove secrets rather than masking them into Git.
4. Assign one allowed evidence authority based on the actual executor.
5. Validate content, links, counts, limitations, and package/scenario mapping.
6. Reject the derivative if any sensitive or unsupported content remains.
7. Track only the reviewed text derivative under its approved authority.

No exact executable command is defined by this runbook; sanitization tooling is
selected by the authorized source workflow.

## Expected Output

A text-only sanitized record containing source, execution authority, bounded
target class, date, checks/counters, evidence paths, limitations, sanitization
result, and explicit non-claims. Raw output remains ignored.

## Validation

Parse machine-readable records, resolve references, scan sensitive patterns,
confirm runtime is untracked, and compare the claimed authority to the source
execution record.

## Pass Criteria

No prohibited value or raw configuration; authority and source resolve;
minimum required facts are present; limitations remain; tracked runtime count
is zero.

## Stop Conditions

Unknown executor, missing source authority, sensitive content, raw output in a
tracked path, unapproved destination, invented result, unsupported maturity or
completion claim, or inability to sanitize without losing audit meaning.

## Failure Handling

Leave raw content ignored, do not create a tracked derivative, record the
rejection reason without echoing the sensitive value, and request a safer
recollection or human review.

## Rollback

Before tracking, discard only the unsafe derivative from the bounded work area.
After review, correct or remove an unsafe evidence record only through an
explicitly authorized change that preserves the incident trail.

## Evidence

The evidence-handling record must state whether raw runtime was committed
(`false`), whether runtime is ignored, who executed the source action, who
reviewed sanitization, and which limitations remain.

## Escalation

Escalate suspected secret exposure, ambiguous identity or infrastructure data,
authority mismatch, or a request to retain raw configuration.

## Known Limitations

Pattern scanning cannot prove absence of all sensitive context. Human review is
required for novel data shapes and environment-specific identifiers.

## Related Architecture

`docs/zero-trust/target-architecture/operator-interface-contract.md` and
`docs/adr/0002-non-production-runtime-evidence-boundary.md`.

## Related Runbooks

RB-P1-002, RB-P1-004, and RB-P1-005.
