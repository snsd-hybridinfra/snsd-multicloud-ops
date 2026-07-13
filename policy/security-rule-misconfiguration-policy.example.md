# Security Rule Misconfiguration Policy Example

**NON-PRODUCTION POLICY EXAMPLE**

- Admin ports must not be open to unrestricted source.
- Database ports must not be open to unrestricted source.
- Internal service ports must not be publicly exposed.
- Temporary exceptions require an `<owner-placeholder>`, `<reason-placeholder>`, `<expiry-placeholder>`, `<approval-placeholder>`, and `<rollback-evidence-placeholder>`.
- Rollback evidence is mandatory after correcting a misconfiguration.
- Every exception requires owner, reason, expiry, approval, change reference, and rollback evidence placeholders.
- Real cloud changes are out of scope for this repository scenario.

No account, project, network, rule, or resource value is represented here.
