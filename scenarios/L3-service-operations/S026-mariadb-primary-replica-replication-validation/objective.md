# Objective

S026 defines the MariaDB Primary-Replica replication validation model for the On-Prem Internal Server Zone.

The scenario validates that `db-primary-01`, `db-replica-01`, and `db-replica-02` have a documented replication topology, that replication configuration can be reviewed, and that primary write plus replica read consistency can be validated later through sanitized evidence.

This scenario does not implement MariaDB configuration or create replication credentials. It defines how future replication topology, configuration, status, and consistency evidence must be captured and reviewed.

## Operational Capability

- Confirm DB Primary and Replica node roles are planned.
- Confirm replication user placeholder model is documented.
- Confirm binary log and replica source configuration validation is planned.
- Confirm primary write and replica read consistency validation is planned.
- Confirm replication status and error field review is planned.
- Confirm replication topology evidence can be captured without secrets.
