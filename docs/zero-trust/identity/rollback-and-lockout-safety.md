# ZT-ID-001 Rollback and Lockout Safety

## Current boundary

P1-ID-001 changes repository-local policy, schemas, synthetic fixtures,
validator code, and sanitized local evidence only. It creates no user, role,
credential, session, authentication factor, identity provider, or enforcement
policy. Current rollback is therefore limited to removing the package-local
tracked files and restoring the reviewed repository records.

## Mandatory future live-enforcement safeguards

Before any future live inspection or enforcement, all of the following are
mandatory:

1. Use an explicitly approved non-production target.
2. Confirm a separately controlled break-glass path.
3. Document and test the recovery path before enforcement.
4. Preserve a known-good administrative session.
5. Bound every role and target scope.
6. Define a session timeout and credential expiry.
7. Identify the rollback owner and accountable approver.
8. Back up the prior policy without copying secrets into Git.
9. Stop immediately on any unexpected denial or administrative-path loss.
10. Prohibit bulk account disablement.
11. Prohibit password, key, token, or factor rotation during initial validation.
12. Exclude production targets.
13. Preserve the default administrative role until recovery is proven.
14. Require separate approval before live enforcement.

The local validator rejects a future runtime plan that lacks a break-glass
identity, rollback procedure, recovery procedure, lockout stop condition, or
accountable approver.

## Failure handling

If a local fixture or policy validation fails, make no runtime change. Record
the reason code, preserve the failing synthetic input, repair only the package
model or validator, and rerun the targeted tests. A schema or validator failure
does not authorize a weaker rule.

If a later live action causes an unexpected denial, stop the action, keep the
known-good administrative session open, use the approved recovery path, restore
the prior policy, and revalidate the original access path before proceeding.

## Break-glass requirements

A break-glass design record requires a non-shared identity, accountable owner,
explicit approval, expiration, external secret reference, logging requirement,
recovery procedure, rollback procedure, and lockout stop condition. P1-ID-001
defines and validates these fields but does not create the credential or test
live emergency access.

## Phase 2 boundary

Keycloak, LDAP, Active Directory, OIDC, MFA enforcement, application RBAC,
centralized identity lifecycle, PAM, and access-decision telemetry are Phase 2
or separately approved runtime work. They are not rollback targets of this
repository-local package.
