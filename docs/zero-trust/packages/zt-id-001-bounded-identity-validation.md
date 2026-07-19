# ZT-ID-001 Bounded Identity Inventory, Role, Authentication, and Access Validation

## Package Identity

- Action: `P1-ID-001`
- Package: `ZT-ID-001`
- Type: `IDENTITY_VALIDATION`
- Phase: `PHASE_1`
- Policy version: `1.0.0`
- Authority: `AUTHORITATIVE`
- Package implementation: `IMPLEMENTED`
- Package validation: `LOCAL_VALIDATED`
- Runtime validation: `NOT_VALIDATED`
- Maturity: `UNASSESSED`

## Purpose

Implement a bounded, repository-level identity-control model that validates
synthetic subject inventory, roles, authentication requirements, lifecycle
rules, deterministic authorization decisions, external secret references,
privacy controls, evidence, and recovery safeguards.

## Scope

The package contains JSON-compatible policy documents, JSON Schemas, a
read-only validator, synthetic fixtures, unit tests, sanitized local evidence,
and action records. Local implementation means these artifacts exist and pass
deterministic fixture validation. It does not mean a live identity control is
deployed.

## Explicit Exclusions

The package does not deploy or inspect Keycloak, LDAP, Active Directory,
MariaDB, Nginx, an OIDC provider, an MFA provider, PAM, an identity VM, or a
monitoring VM. It does not enumerate users, query OpenStack, run SSH, change
sudo or SSH policy, create accounts, rotate credentials, test authentication,
or modify Grafana, Loki, Alloy, Docker Compose, or ZT-VIS-002 preparation.

It is not evidence that MFA, OIDC, runtime RBAC, federation, continuous
authentication, ICAM, biometric recognition, or a centralized identity service
is operational. It makes no Phase 1 completion or official maturity claim.

## Guideline Capability Mapping

| Capability | Canonical name | Bounded package relationship | Runtime state |
|---|---|---|---|
| `ZT-1.1.1` | 사용자 인벤토리 | Direct synthetic inventory contract and local validation | `NOT_VALIDATED` |
| `ZT-1.1.2` | ID 연계 및 사용자 자격 증명 | Federation and credential-lifecycle requirement only | `NOT_VALIDATED` |
| `ZT-1.2.1` | 다중인증 (MFA) | Privileged-interactive MFA requirement only | `NOT_VALIDATED` |
| `ZT-1.4.1` | 조건부 사용자 접근 | Local deterministic decision policy only | `NOT_VALIDATED` |
| `ZT-1.4.2` | 최소 권한 접근 | Local role, approval, and separation policy only | `NOT_VALIDATED` |

`ZT-1.2.2`, `ZT-1.3.1`, and `ZT-1.3.2` remain excluded. `ZT-4.1.1`,
`ZT-4.2.1`, and `ZT-4.2.2` are related system-control references and are not
promoted by this package.

## Current Authority

The package YAML is authoritative for ZT-ID-001 package state. The capability
catalog remains authoritative for capability IDs and canonical Korean names.
Capability current assessment and maturity remain separate. The package does
not promote any capability to runtime validation or assign maturity.

Existing ZT-FND-001 evidence records dedicated forced-command validator
accounts and operator/validator key separation. That evidence is reused only as
a boundary reference; no account name, key, credential, or live inventory is
copied into ZT-ID-001.

## Identity Subject Model

The subject contract defines `HUMAN_OPERATOR`, `SERVICE_IDENTITY`,
`AUTOMATION_IDENTITY`, `VALIDATOR_IDENTITY`, and `BREAK_GLASS_IDENTITY`.
Every synthetic record includes identity ID and type, non-sensitive label,
owner role, accountable owner, target and environment scope, authentication
category, privilege, roles, lifecycle and approval state, creation authority,
review and expiration, revocation, sharing and interaction boundaries, MFA and
recovery requirements, evidence reference, and limitations.

## Role and Privilege Model

The bounded roles are `IDENTITY_READER`, `VALIDATION_OPERATOR`,
`EVIDENCE_REVIEWER`, `PACKAGE_APPROVER`, `MUTATING_OPERATOR`, and
`BREAK_GLASS_OPERATOR`. Each role defines allowed and prohibited actions,
approval requirements, interactive and mutating boundaries, evidence, runtime,
and secret access, and separation-of-duties conflicts.

Anonymous, unregistered, shared privileged, ownerless, unrestricted
administrator, unapproved privilege, read-only mutation, conflicting
validation/approval, and uncontrolled break-glass records are rejected.

## Authentication Assurance Model

The policy categories are `SSH_KEY`, `LOCAL_CREDENTIAL`, `FEDERATED_OIDC`,
`SERVICE_TOKEN`, `CERTIFICATE`, `MFA_PROTECTED_INTERACTIVE`, and
`BREAK_GLASS_CREDENTIAL`. Categories specify policy requirements only.

Privileged interactive and emergency identities require MFA in the target
model and record `REQUIRED_NOT_IMPLEMENTED`. Automation, service, and validator
identities are non-interactive and use external secret references. No category
is treated as deployed by this package.

## Lifecycle Model

The lifecycle states are `PROPOSED`, `APPROVED`, `ACTIVE`, `SUSPENDED`,
`REVOKED`, `EXPIRED`, and `REVIEW_REQUIRED`. Active records require an owner and
approval. Revoked records cannot retain roles; expired and suspended records
cannot receive positive authorization. Review-due behavior is privilege-aware,
and emergency identities require explicit expiration.

## Decision Model

The decisions are `ALLOW`, `DENY`, `REVIEW_REQUIRED`, and `NOT_APPLICABLE`.
Every decision contains a stable decision ID, identity, action, target, role,
policy version, reason codes, approval requirement, evidence authority, fixture
time, and limitations. The default policy is
`DENY_BY_DEFAULT_FOR_UNREGISTERED_IDENTITY`.

An `ALLOW` result applies only to a synthetic policy evaluation and never
grants live access.

## Positive Acceptance Cases

Nine positive cases cover a read-only human, validation operator, evidence
reviewer, scoped automation identity, non-interactive validator, controlled
break-glass design, approved mutating fixture, future OIDC requirement marked
not implemented, and non-interactive service identity.

## Negative Acceptance Cases

Thirty-four negative cases cover missing or duplicate IDs, unknown types,
missing owners, shared privilege, missing MFA requirement, expiry, revocation,
suspension, unregistered access, read-only mutation, interactive automation,
invalid service scope, incomplete break-glass controls, synthetic secret-field
injection, separation conflicts, invalid role/lifecycle/authentication values,
fictional deployment and maturity claims, S051 and runtime tracking, production
data markers, missing approval, and unrestricted emergency scope.

Controlled secret-field names and synthetic sentinel values exist only in the
negative fixture set to prove rejection. They are not credentials.

## Evidence Contract

The accepted record is
`docs/evidence/zero-trust/zt-id-001-local-validation.yaml`. It uses
`CODEX_EXECUTED_LOCAL`, `SYNTHETIC_FIXTURE_VALIDATION`, and
`LOCAL_REPOSITORY_FIXTURES`, with `runtime_executed` and
`live_identity_changed` both false. Counts, policy and validator versions,
reason codes, limitations, and synchronization are validated.

## Privacy and Data-Minimization Boundary

The package enforces purpose limitation, minimum fields, synthetic fixtures,
non-sensitive target labels, and sanitized evidence. It prohibits personal
email, full names, production account exports, password hashes, authentication
factors, and complete login histories. The retention policy keeps only reviewed
synthetic artifacts and sanitized counts.

## Secret Boundary

Only `env://`, `file-ref://`, `vault-ref://`, and `external-secret://` logical
references are accepted. The validator never dereferences them. Passwords,
tokens, client secrets, private keys, MFA seeds, recovery codes, `clouds.yaml`,
`passwords.yml`, and real environment contents are prohibited.

## Lockout Prevention

Future live work requires a non-production target, confirmed break-glass path,
tested recovery, known-good administrative session, bounded roles, session
timeout, rollback owner, prior-policy backup, and an immediate stop on
unexpected denial. Bulk disablement, initial factor rotation, production use,
and removal of the default administrative role are prohibited.

## Break-Glass Requirements

The emergency design record must be non-shared, owner-bound, approved,
time-limited, externally referenced, logged, recoverable, rollback-capable, and
scope-bounded. These requirements are validated locally; no emergency
credential or access path is created or exercised.

## Failure Handling

Local failures retain the synthetic failing input and reason code. They do not
authorize a weaker rule or runtime workaround. Any future unexpected live
denial requires an immediate stop, preservation of the known-good session,
approved recovery, policy restoration, and revalidation.

## Rollback

Current rollback removes only ZT-ID-001 package-local repository artifacts and
restores reviewed tracking records. It cannot remove or alter accounts because
none are created. Future runtime rollback is defined in
`docs/zero-trust/identity/rollback-and-lockout-safety.md` and requires separate
approval.

## Runtime Validation Boundary

Future adapters may inspect restricted SSH identity boundaries, Linux accounts
and sudo policy, OpenStack identity, Keycloak identities and roles, Grafana OIDC
roles, or certificate identities. Every adapter remains `NOT_IMPLEMENTED`.
P1-ID-001 performs no network access or live inspection.

## Phase 2 Dependency Boundary

Centralized identity, Keycloak, federation, MFA enforcement, OIDC, runtime RBAC,
application integration, access-decision telemetry, and ZT-ID-002 remain Phase
2 or separately approved work. ZT-VIS-002 is protected and is neither identity
evidence nor a prerequisite modified by this action.

## Known Limitations

- The identity inventory contains synthetic fixtures, not real accounts.
- Decisions are not consumed by a runtime policy enforcement point.
- MFA and OIDC are requirements, not operating controls.
- No runtime authentication, denial, recovery, or lockout behavior is tested.
- Capability maturity remains `UNASSESSED`.
- Phase 1 remains `PARTIAL`, `PARTIALLY_VALIDATED`, and `NOT_COMPLETE`.

## Package Acceptance

Package acceptance requires all schemas to parse, all models to satisfy schema
and semantic rules, nine positive cases to match expected decisions,
thirty-four negative cases to be rejected for the expected reason, evidence to
synchronize, the validator and unit tests to pass, S001-S050 to remain locked,
S051 to remain absent, and no secret or runtime file to be tracked.

Acceptance sets ZT-ID-001 to `PRESENT`, `IMPLEMENTED`, and `LOCAL_VALIDATED`.
Runtime validation stays `NOT_VALIDATED`, runtime acceptance stays `PENDING`,
and maturity stays `UNASSESSED`.

## Related Runbooks

- `docs/runbooks/phase-1/06-identity-validation-readiness.md`
- `docs/runbooks/phase-1/03-evidence-handling-and-sanitization.md`
- `docs/runbooks/phase-1/07-repeatable-and-scheduled-validation.md`

## Related Architecture

- `docs/zero-trust/target-architecture/implementation-dependency-map.md`
- `docs/zero-trust/target-architecture/operator-interface-contract.md`
- `docs/zero-trust/target-architecture/security-boundaries.md`
