# Validation

Scenario: S017-mariadb-access-control-validation
Level: L2-security-baseline
Capability: MariaDB Access Control Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real MariaDB access control output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | MariaDB bind-address validation plan | MariaDB listener is scoped to the intended On-Prem DB access boundary. | TODO | NOT_RUN | `commands.md`; `configs/mariadb-access-control-summary.md` |
| V002 | MariaDB user and host mapping validation plan | Users are mapped only to approved placeholder hosts or CIDRs. | TODO | NOT_RUN | `commands.md`; `configs/mariadb-access-control-summary.md` |
| V003 | Application DB user least privilege validation plan | Application user has only required application privileges. | TODO | NOT_RUN | `commands.md`; `configs/mariadb-grant-policy.md` |
| V004 | Replication DB user separation validation plan | Replication user is separate and limited to replication purpose. | TODO | NOT_RUN | `commands.md`; `configs/mariadb-grant-policy.md` |
| V005 | Backup DB user separation validation plan | Backup user is separate and limited to backup purpose. | TODO | NOT_RUN | `commands.md`; `configs/mariadb-grant-policy.md` |
| V006 | Root remote access denial validation plan | Root is not allowed remote database login. | TODO | NOT_RUN | `commands.md`; `logs/mariadb-access-control-validation.log` |
| V007 | DB port 3306 public exposure denial validation plan | DB port is not exposed to public sources. | TODO | NOT_RUN | `commands.md`; `logs/mariadb-access-control-validation.log` |
| V008 | Cloud App/API node to DB access rule validation plan | Cloud App/API DB access is explicitly scoped. | TODO | NOT_RUN | `commands.md`; `configs/mariadb-access-control-summary.md` |
| V009 | Web node direct DB access denial validation plan | Direct Web node DB access is denied. | TODO | NOT_RUN | `commands.md`; `logs/mariadb-access-control-validation.log` |
| V010 | Bastion or management admin access validation plan | Administrative DB access is limited to Bastion or management boundary. | TODO | NOT_RUN | `commands.md`; `configs/mariadb-access-control-summary.md`; `screenshots/mariadb-access-control-test.png` |
| V011 | Failure condition for public DB exposure, root remote access, overly broad grants, missing app user, missing replication user, or direct unauthorized DB access | Unsafe access patterns produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- MariaDB access control summary is captured: NOT_READY
- MariaDB grant policy is captured: NOT_READY
- MariaDB access control validation log is captured: NOT_READY
- MariaDB access control screenshot is captured: NOT_READY

## Notes

This scenario validates MariaDB access control design only. MariaDB replication validation is handled in S026, replication lag in S027, backup creation in S038, and restore execution in S039.
