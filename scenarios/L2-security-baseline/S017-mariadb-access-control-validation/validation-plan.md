# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | MariaDB bind-address validation plan | Document planned review of bind-address or equivalent listener configuration. | MariaDB listener is scoped to the intended On-Prem DB access boundary. | `commands.md`, `configs/mariadb-access-control-summary.md`, `validation.md` |
| V002 | MariaDB user and host mapping validation plan | Document planned review of user and host mappings. | Users are mapped only to approved placeholder hosts or CIDRs. | `commands.md`, `configs/mariadb-access-control-summary.md`, `validation.md` |
| V003 | Application DB user least privilege validation plan | Review planned grants for `<app-db-user>`. | Application user has only required application privileges. | `commands.md`, `configs/mariadb-grant-policy.md`, `validation.md` |
| V004 | Replication DB user separation validation plan | Review planned grants and host mapping for `<replication-user>`. | Replication user is separate and limited to replication purpose. | `commands.md`, `configs/mariadb-grant-policy.md`, `validation.md` |
| V005 | Backup DB user separation validation plan | Review planned grants and host mapping for `<backup-user>`. | Backup user is separate and limited to backup purpose. | `commands.md`, `configs/mariadb-grant-policy.md`, `validation.md` |
| V006 | Root remote access denial validation plan | Review planned root user host mappings. | Root is not allowed remote database login. | `commands.md`, `logs/mariadb-access-control-validation.log`, `validation.md` |
| V007 | DB port 3306 public exposure denial validation plan | Review planned network exposure for port `3306`. | DB port is not exposed to public sources. | `commands.md`, `logs/mariadb-access-control-validation.log`, `validation.md` |
| V008 | Cloud App/API node to DB access rule validation plan | Review placeholder App/API source access using `<app-node-cidr>`. | Cloud App/API DB access is explicitly scoped. | `commands.md`, `configs/mariadb-access-control-summary.md`, `validation.md` |
| V009 | Web node direct DB access denial validation plan | Review planned Web node access denial. | Direct Web node DB access is denied. | `commands.md`, `logs/mariadb-access-control-validation.log`, `validation.md` |
| V010 | Bastion or management admin access validation plan | Review administrative access placeholder path. | Administrative DB access is limited to Bastion or management boundary. | `commands.md`, `configs/mariadb-access-control-summary.md`, `screenshots/mariadb-access-control-test.png`, `validation.md` |
| V011 | Failure condition for public DB exposure, root remote access, overly broad grants, missing app user, missing replication user, or direct unauthorized DB access | Evaluate findings against explicit failure conditions. | Unsafe access patterns produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates MariaDB access control design only; replication, replication lag, backup, and restore behavior are handled in later scenarios.
