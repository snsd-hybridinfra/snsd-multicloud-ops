# Architecture

## Relevant Components

- `db-primary-01`: planned MariaDB Primary node.
- `db-replica-01`: planned MariaDB Replica node.
- `db-replica-02`: planned MariaDB Replica node.
- `<replication-user>`: placeholder replication account identity.
- Binary log configuration: planned primary-side replication prerequisite.
- Replica source configuration: planned replica-side source definition.
- Replication status output: future evidence source for replication health.

## Replication Model

- `db-primary-01` is the planned write source for replication validation.
- `db-replica-01` and `db-replica-02` are planned read replicas.
- Primary write test uses placeholders such as `<test-database>` and `<test-table>`.
- Replica read consistency checks confirm the placeholder test data is visible on replicas.
- Replication status checks review running state and error fields.
- Replication lag timing is outside this scenario and handled in S027.

## Boundary Notes

This scenario validates primary-replica replication only. Access control, lag, backup, restore, failover, Galera, ProxySQL, and split-brain automation are separate or excluded responsibilities.
