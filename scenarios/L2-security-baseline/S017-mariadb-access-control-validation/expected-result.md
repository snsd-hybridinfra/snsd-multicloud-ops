# Expected Result

S017 is successful when the MariaDB access control validation plan is complete and ready for future approved execution.

## Success Conditions

- MariaDB bind-address or equivalent listener behavior is planned for the intended access boundary.
- MariaDB user and host mappings use approved placeholders only.
- `<app-db-user>` is scoped to required application privileges.
- `<replication-user>` is separate from application and backup users.
- `<backup-user>` is separate from application and replication users.
- Root remote access is denied.
- DB port `3306` is not exposed to public sources.
- Cloud App/API node DB access is explicitly scoped to `<app-node-cidr>`.
- Direct Web node DB access is denied.
- Administrative access is limited to Bastion or management boundaries.
- All validation checks map to required evidence files.

## Evidence Conditions

- `commands.md` lists planned command or review actions with TODO output placeholders.
- `validation.md` lists each check with `NOT_RUN` status until execution.
- Future supporting evidence is expected in `configs/mariadb-access-control-summary.md`, `configs/mariadb-grant-policy.md`, `logs/mariadb-access-control-validation.log`, and `screenshots/mariadb-access-control-test.png`.
