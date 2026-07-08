# Execution Plan

1. Confirm the scenario evidence directory exists for S017.
2. Identify placeholder database targets as `<db-primary-host>` and `<db-replica-host>`.
3. Record the planned MariaDB bind-address review method.
4. Record the planned MariaDB user and host mapping review method.
5. Review planned grants for `<app-db-user>` and confirm least privilege intent.
6. Review planned grants for `<replication-user>` and confirm role separation.
7. Review planned grants for `<backup-user>` and confirm role separation.
8. Review root remote access denial criteria.
9. Review network-level DB port `3306` exposure criteria.
10. Review cloud App/API node to DB access placeholders using `<app-node-cidr>`.
11. Review direct Web node DB access denial criteria.
12. Review Bastion or management-only administrative access placeholders.
13. Record TODO placeholders in evidence files until approved execution produces sanitized output.

## Execution Boundaries

This plan does not modify MariaDB configuration, create database users, grant privileges, or change network controls. It only defines the review flow and evidence requirements for later approved validation.
