# Objective

S017 defines the MariaDB access control validation model for the On-Prem Internal Server Zone.

The scenario validates that database access is planned around explicit database users, host mappings, grants, and network exposure boundaries. It prevents public DB exposure, remote root access, overly broad grants, and direct unauthorized DB access from being accepted as a baseline security state.

This scenario does not implement MariaDB configuration. It defines how future MariaDB user, host, grant, and network exposure evidence must be reviewed and validated.

## Operational Capability

- Confirm MariaDB bind-address behavior is planned for the intended DB access boundary.
- Confirm application, replication, and backup users are separated by purpose.
- Confirm root remote access is denied.
- Confirm DB port `3306` is not publicly exposed.
- Confirm cloud App/API access is placeholder-scoped.
- Confirm direct Web node DB access is denied unless explicitly approved in a later scenario.
