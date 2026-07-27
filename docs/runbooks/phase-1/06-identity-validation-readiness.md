# Identity Validation Readiness

```json runbook-metadata
{"runbook_id":"RB-P1-006","phase":"PHASE_1","related_packages":["ZT-ID-001"],"procedure_status":"IMPLEMENTED","validation_status":"LOCAL_VALIDATED","live_execution_permitted":true}
```

## Purpose

Validate the repository-local ZT-ID-001 policy, schemas, fixtures, and authorization model while keeping runtime enforcement separately approval-gated.

## Current boundary

- Implementation: IMPLEMENTED
- Local validation: LOCAL_VALIDATED
- Runtime validation: NOT_VALIDATED
- Runtime acceptance: PENDING
- Maturity: UNASSESSED

Centralized identity, federation, MFA, PAM, and application RBAC are not established.

## Procedure

1. Validate package metadata, policy, schema, fixture, and evidence references locally.
2. Confirm positive and negative authorization cases and secret/privacy boundaries.
3. Require an explicit non-production target, independent recovery path, backup, automatic rollback, service-impact review, and separate user approval before any live enforcement retry.
4. Run `python tools/validate_zt_id_001.py --verbose --strict --format text`.
5. Do not execute P1-ID-ENF-001-RETRY as part of repository governance.

## Pass criteria

Local policy validation passes, runtime remains unclaimed, recovery requirements remain explicit, and no real identity, credential, key, or authentication log is tracked.
