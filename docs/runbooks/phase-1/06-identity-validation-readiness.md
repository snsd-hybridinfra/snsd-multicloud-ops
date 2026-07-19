# Identity Validation Readiness

```json runbook-metadata
{
  "runbook_id": "RB-P1-006",
  "title": "Identity Validation Readiness",
  "phase": "PHASE_1",
  "related_packages": ["ZT-ID-001"],
  "owner_domain": "IDENTITY_SECURITY",
  "supported_target_types": ["REPOSITORY_LOCAL_POLICY_VALIDATION"],
  "procedure_status": "PARTIALLY_IMPLEMENTED",
  "validation_status": "VALIDATED_LOCAL",
  "runtime_required": true,
  "live_execution_permitted": false,
  "required_authority": "ZT_ID_001_LOCAL_PACKAGE_AUTHORITY_AND_SEPARATE_RUNTIME_APPROVAL",
  "evidence_authority": "CODEX_EXECUTED_LOCAL",
  "last_reviewed": "2026-07-19",
  "limitations": ["ZT-ID-001 policy, schemas, validator, and synthetic fixtures are locally validated; live identity inspection and enforcement remain not implemented and not validated."]
}
```

## Purpose

Define the minimum gates for validating the implemented repository-local
ZT-ID-001 policy package and for keeping any future runtime identity work under
separate approval, without configuring an identity service.

## Scope

Repository-local synthetic identity inventory, access policy, MFA requirement,
role mapping, lifecycle, decision, evidence, failure, and rollback validation.
Live target selection, inspection, authentication, and enforcement are outside
the current procedure.

## Related Phase

ZT-ID-001 is a Phase 1 package. Package-local implementation does not complete
Phase 1 or satisfy runtime acceptance for identity controls.

## Related Package or Governance Action

ZT-ID-001 package files exist and are `PRESENT`, `IMPLEMENTED`, and
`LOCAL_VALIDATED`. Runtime validation remains `NOT_VALIDATED`, runtime
acceptance is pending, and maturity is `UNASSESSED`.

## Supported Target Types

Repository-local policy, schema, validator, and synthetic-fixture validation
only. No Keycloak, OIDC provider, MFA service, directory, RBAC engine,
application integration, or live identity target is approved.

## Current Procedure Status

`PARTIALLY_IMPLEMENTED`: the local package procedure is executable and
read-only; runtime inspection and enforcement procedures are not implemented.

## Current Validation Status

`VALIDATED_LOCAL` covers ZT-ID-001 schemas, policy semantics, 9 positive
synthetic cases, 34 negative synthetic cases, evidence synchronization, and
repository integrity. Identity runtime remains `NOT_VALIDATED`.

## Evidence Authority

`CODEX_EXECUTED_LOCAL` for synthetic fixture and package validation. Runtime
identity evidence authority remains `NONE`.

## Required Authority

The current local procedure uses ZT-ID-001 package authority. Future runtime
work additionally requires an identified identity owner, target owner,
data/privacy review, change approval, rollback approval, and bounded runtime
authority.

## User-Performed Physical or Approval Steps

Select and approve the identity target, accounts/roles, MFA method, recovery
owners, service window, and any interactive secret entry outside Git.

## Codex or Automation-Managed Steps

Validate the secret-free package, schemas, policy mappings, synthetic fixtures,
sanitization rules, local evidence, and rollback documentation. Do not execute
runtime adapters or resolve external secret references.

## Prerequisites

For local validation: authoritative package ID, explicit synthetic scope,
least-privilege roles, lifecycle, MFA requirement, evidence contract, rollback,
and stop criteria. A non-production target and live owner approvals are
prerequisites only for a separate runtime action.

## Inputs

Identity architecture decision, stable non-sensitive role names, access matrix,
authentication and authorization flows, target profile, acceptance cases, and
operator responsibilities.

## Secret Inputs

No secrets may be committed. Passwords, client secrets, tokens, signing keys,
MFA seeds, recovery codes, directory binds, private certificates, and real user
identifiers remain external and interactively supplied only when authorized.

## Service Impact

None in the current phase action. A future identity change may block access and
must have a service-impact review and break-glass recovery.

## Security Impact

Identity misconfiguration can create privilege escalation, lockout, weak MFA,
or unauthorized federation. Default-deny, least privilege, separation of duty,
and recovery controls are future acceptance requirements, not current facts.

## Preflight Checks

Confirm ZT-ID-001 is promoted only to local package implementation; runtime is
still not validated; no Keycloak/OIDC/MFA/RBAC deployment or enforcement claim
is present; ZT-VIS-002 does not replace runtime identity work; S001-S050 remains
locked.

### Recorded sudoers preflight remediation

`P1-ID-ENF-PREFLIGHT-REMEDIATION` repaired one pre-existing `eve-ng`
package-owned sudoers file mode on the approved non-production target. The
repair changed metadata only, preserved rule content and the existing validator
boundary, and passed exact/global sudoers validation, independent-console,
rollback, and operator-access checks. It did not execute identity enforcement
or promote ZT-ID-001 runtime validation; a fresh approved P1-ID-ENF-001 retry is
still required.

## Procedure

1. Confirm the package metadata preserves local/runtime/maturity truth.
2. Parse the JSON-compatible policy models and JSON Schemas.
3. Run `python tools/validate_zt_id_001.py --verbose --strict --format text`.
4. Run `python -m unittest tests.test_zt_id_001 -v`.
5. Confirm no repository mutation, tracked runtime, secret, or scenario drift.
6. Stop before any live identity inspection, authentication, or enforcement.

## Expected Output

For the current action: deterministic local decisions, package validation,
sanitized local evidence, and explicit limitations. This runbook does not
produce identity runtime evidence.

## Validation

Current validation covers local schema, policy, fixture, decision, privacy,
secret-reference, evidence, and repository-integrity checks. Separately
authorized runtime positive/negative tests remain required for runtime
acceptance.

## Pass Criteria

The local validator and tests pass, all identities remain synthetic, no secret
is stored, the package claim is limited to local implementation, runtime
authority remains separate, and rollback and negative tests are reviewable.

## Stop Conditions

No approved package/owner, production target, secret in Git, real user data,
unbounded federation, missing rollback, unreviewed privilege mapping,
unavailable break-glass, service-impact ambiguity, or request to claim
implementation or validation from documentation.

## Failure Handling

Mark the readiness gate blocked with the missing decision. Do not deploy a
placeholder service, weaken authentication, skip negative tests, or reuse
ZT-VIS-002 preparation as identity evidence.

## Rollback

Current rollback removes only repository-local ZT-ID-001 artifacts and restores
reviewed tracking records. A future runtime action must define tested config,
session/token, role, federation, and service-access rollback before execution.

## Evidence

Current evidence authority is `CODEX_EXECUTED_LOCAL` at
`docs/evidence/zero-trust/zt-id-001-local-validation.yaml`. It contains only
synthetic case outcomes and sanitized counts. Future runtime evidence must be a
separate record and must omit real identities and secrets.

## Escalation

Escalate target/vendor selection, privacy, privilege model, MFA/recovery,
service lockout risk, secret handling, and any production or enterprise scope.

## Known Limitations

The document does not choose or configure Keycloak, OIDC, MFA, runtime RBAC, a
user store, an application, or a policy engine. It establishes a local policy
package only; it establishes no runtime identity control, runtime capability
validation, maturity, or compliance.

## Related Architecture

`docs/zero-trust/target-architecture/implementation-dependency-map.md` and
`docs/zero-trust/target-architecture/operator-interface-contract.md`.

## Related Runbooks

RB-P1-001, RB-P1-003, and RB-P1-007.
