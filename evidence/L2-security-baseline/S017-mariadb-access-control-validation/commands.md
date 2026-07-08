# Commands

Scenario: S017-mariadb-access-control-validation
Level: L2-security-baseline
Capability: MariaDB Access Control Validation
Target: `<db-primary-host>`
Execution timestamp: TODO

Record sanitized output only. Do not include database passwords, credentials, real public IPs, private keys, tfstate, kubeconfig content, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | MariaDB bind-address validation plan | Review MariaDB bind-address or equivalent listener configuration on `<db-primary-host>`. | Confirm listener scope is aligned to the intended access boundary. | TODO: record sanitized output after approved execution. |
| V002 | MariaDB user and host mapping validation plan | Review planned MariaDB user and host mappings using placeholder users and hosts. | Confirm users are mapped to approved sources only. | TODO: record sanitized output after approved execution. |
| V003 | Application DB user least privilege validation plan | Review planned grants for `<app-db-user>`. | Confirm application privileges are least privilege. | TODO: record sanitized output after approved execution. |
| V004 | Replication DB user separation validation plan | Review planned grants and host mapping for `<replication-user>`. | Confirm replication access is separated from application and backup access. | TODO: record sanitized output after approved execution. |
| V005 | Backup DB user separation validation plan | Review planned grants and host mapping for `<backup-user>`. | Confirm backup access is separated from application and replication access. | TODO: record sanitized output after approved execution. |
| V006 | Root remote access denial validation plan | Review root user host mappings for remote access. | Confirm remote root login is denied. | TODO: record sanitized output after approved execution. |
| V007 | DB port 3306 public exposure denial validation plan | Review network exposure for port `3306`. | Confirm DB port is not publicly reachable. | TODO: record sanitized output after approved execution. |
| V008 | Cloud App/API node to DB access rule validation plan | Review placeholder access from `<app-node-cidr>`. | Confirm cloud App/API access is explicitly scoped. | TODO: record sanitized output after approved execution. |
| V009 | Web node direct DB access denial validation plan | Review direct Web node access attempt or rule model. | Confirm direct Web node DB access is denied. | TODO: record sanitized output after approved execution. |
| V010 | Bastion or management admin access validation plan | Review administrative access placeholder through Bastion or management boundary. | Confirm admin access is management-only. | TODO: record sanitized output after approved execution. |
| V011 | Failure condition for public DB exposure, root remote access, overly broad grants, missing app user, missing replication user, or direct unauthorized DB access | Review validation findings against failure criteria. | Confirm unsafe access patterns result in `FAIL` or `BLOCKED`. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/mariadb-access-control-summary.md`
- `configs/mariadb-grant-policy.md`
- `logs/mariadb-access-control-validation.log`
- `screenshots/mariadb-access-control-test.png`
