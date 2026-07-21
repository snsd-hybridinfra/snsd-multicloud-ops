# Identity Validation Readiness

```json runbook-metadata
{
  "runbook_id": "RB-P1-006",
  "title": "Identity Validation Readiness",
  "phase": "PHASE_1",
  "related_packages": ["ZT-ID-001"],
  "owner_domain": "IDENTITY_SECURITY",
  "supported_target_types": ["REPOSITORY_LOCAL_POLICY_VALIDATION", "BOUNDED_NON_PRODUCTION_EVE_NG_VALIDATOR"],
  "procedure_status": "IMPLEMENTED",
  "validation_status": "VALIDATED_RUNTIME",
  "runtime_required": true,
  "live_execution_permitted": true,
  "required_authority": "EXPLICIT_USER_APPROVAL_FOR_BOUNDED_NON_PRODUCTION_ENFORCEMENT",
  "evidence_authority": "CODEX_EXECUTED_LIVE_RUNTIME",
  "last_reviewed": "2026-07-19",
  "limitations": ["Runtime acceptance covers one dedicated validator identity on one non-production EVE-NG endpoint; centralized identity, MFA, OIDC, application RBAC, production validation, and maturity remain absent or unassessed."]
}
```

## Purpose

Define the gates for validating the repository-local ZT-ID-001 policy package
and applying its dedicated validator boundary to one explicitly approved
non-production target without configuring a centralized identity service.

## Scope

Repository-local synthetic policy validation plus one bounded validator account
and group, forced command, SSH restrictions, exact sudo allowlist, positive and
negative authorization tests, backup, rollback, recovery, and sanitized runtime
evidence. Centralized identity and application integration remain excluded.

## Related Phase

ZT-ID-001 is a Phase 1 package. Its bounded runtime acceptance does not complete
Phase 1 and does not satisfy Phase 2 centralized-identity gates.

## Related Package or Governance Action

ZT-ID-001 is `PRESENT`, `IMPLEMENTED`, and `RUNTIME_VALIDATED`. Runtime
validation is `VALIDATED`, runtime acceptance is `ACCEPTED`, scope is
`BOUNDED_NON_PRODUCTION_TARGET`, and maturity is `UNASSESSED`.

## Supported Target Types

Repository-local policy, schema, validator, synthetic fixtures, and one bounded
non-production EVE-NG restricted-validator endpoint. No Keycloak, OIDC
provider, MFA service, directory, application RBAC engine, or production target
is approved.

## Current Procedure Status

`IMPLEMENTED`: local policy validation and the bounded non-production validator
enforcement procedure are executable and evidence-backed.

## Current Validation Status

`VALIDATED_RUNTIME` covers the local 9 positive and 34 negative synthetic cases
plus 20 target positive checks and 42 harmless deterministic target denials.
Unexpected allowances, residual jobs, secret findings, and privacy findings are
zero.

## Evidence Authority

`CODEX_EXECUTED_LOCAL` applies to synthetic fixtures. The accepted runtime
record uses `USER_APPROVED_CODEX_EXECUTION`; the runbook classifies its evidence
as `CODEX_EXECUTED_LIVE_RUNTIME`.

## Required Authority

Runtime execution requires explicit user approval, a verified non-production
target, operator and recovery-console access, package ownership classification,
backup and automatic rollback, sanitized evidence, and bounded remediation.

## User-Performed Physical or Approval Steps

Select and approve the target and bounded control scope; preserve the
independent VMware recovery path. No MFA method or interactive secret entry is
part of this package.

## Codex or Automation-Managed Steps

Validate the secret-free package, schemas, mappings, fixtures, sanitization and
local evidence; inventory the approved target; arm rollback; apply only
package-owned controls; run positive and negative tests; preserve operator and
console access; generate sanitized evidence; and cancel rollback after success.

## Prerequisites

Authoritative package ID, local policy validation, explicit non-production
target, two operator sessions, independent recovery console, valid SSH and
sudoers configuration, package ownership boundaries, target-local backup,
automatic rollback, disk and service health, and stop criteria.

## Inputs

Identity architecture decision, stable non-sensitive role names, access matrix,
authentication and authorization flows, target profile, acceptance cases, and
operator responsibilities.

## Secret Inputs

No secrets may be committed. Passwords, client secrets, tokens, signing keys,
MFA seeds, recovery codes, directory binds, private certificates, and real user
identifiers remain external and interactively supplied only when authorized.

## Service Impact

The bounded action reloaded SSH after successful syntax validation. Operator
access and EVE-NG health remained available; no reboot or unrelated service
change occurred.

## Security Impact

Identity misconfiguration can create privilege escalation or lockout. The
accepted endpoint uses public-key-only access, a forced command, no forwarding
or PTY, exact sudo commands, default denial, deterministic audit reason codes,
operator-session preservation, and independent recovery.

## Preflight Checks

Confirm ZT-ID-001 is runtime accepted only for the bounded endpoint; no
Keycloak/OIDC/MFA/application-RBAC or production claim is present; ZT-VIS-002
does not replace identity evidence; Phase 1 stays partial; S001-S050 remains
locked.

### Recorded sudoers preflight remediation

`P1-ID-ENF-PREFLIGHT-REMEDIATION` repaired one pre-existing `eve-ng`
package-owned sudoers file mode on the approved non-production target. The
repair changed metadata only, preserved rule content and the existing validator
boundary, and passed exact/global sudoers validation, independent-console,
rollback, and operator-access checks. It did not itself execute identity
enforcement. The separately approved P1-ID-ENF-001-RETRY action subsequently
completed bounded enforcement and runtime acceptance.

## Procedure

1. Confirm package ownership, target, operator access, and recovery-console gates.
2. Back up package-owned state and arm the target-local automatic rollback.
3. Validate candidate wrapper, SSH, authorized-key, and sudoers controls.
4. Apply atomically, validate SSH and sudoers, and reload SSH without reboot.
5. Run at least 20 positive checks and all 42 deterministic denial checks.
6. Generate sanitized runtime evidence and cancel rollback only after acceptance.
7. Run `python tools/validate_zt_id_001.py --verbose --strict --format text`.
8. Run `python -m unittest tests.test_zt_id_001 -v` and repository safety checks.

## Expected Output

Deterministic local decisions, package validation, 20/20 positive and 42/42
negative target outcomes, zero unexpected allowances, preserved recovery paths,
and sanitized local and runtime evidence.

## Validation

Validation covers local schema, policy, fixture, privacy, secret-reference and
repository checks plus target SSH, sudoers, service, identity boundary,
positive/negative behavior, backup, rollback, recovery, and third-party
integrity checks.

## Pass Criteria

Local and runtime evidence pass schema and synchronization tests; all 20
positive checks pass; all 42 negative checks deny with nonzero outcomes; no
unexpected allowance or protected mutation exists; operator and console access
pass; rollback is cancelled with no residual job; no secret is tracked.

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

The target-local idempotent rollback restores existing package-owned files,
removes newly created package-owned files, restores account/group and key
restrictions, validates SSH and sudoers, reloads SSH only after validation, and
preserves unrelated policy. The accepted action cancelled its timer after all
checks and retained the restrictive backup under target policy.

## Evidence

Local evidence remains at
`docs/evidence/zero-trust/zt-id-001-local-validation.yaml`. Accepted runtime
evidence is `docs/evidence/zero-trust/zt-id-001-runtime-validation.yaml`; it
contains aliases, counts, statuses, limitations, and no real identities,
addresses, keys, credentials, raw sudoers, or full authentication logs.

## Escalation

Escalate target/vendor selection, privacy, privilege model, MFA/recovery,
service lockout risk, secret handling, and any production or enterprise scope.

## Known Limitations

The procedure does not choose or configure Keycloak, OIDC, MFA, application
RBAC, a centralized user store, or an adaptive policy engine. Runtime acceptance
is bounded to one non-production endpoint and establishes no production scope,
capability maturity, certification, or Phase 1 completion.

## Related Architecture

`docs/zero-trust/target-architecture/implementation-dependency-map.md` and
`docs/zero-trust/target-architecture/operator-interface-contract.md`.

## Related Runbooks

RB-P1-001, RB-P1-003, and RB-P1-007.
