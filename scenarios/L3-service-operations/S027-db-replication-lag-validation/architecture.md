# Architecture

## Relevant Components

- `db-primary-01`: planned source for timestamp write validation.
- `db-replica-01`: planned replica lag validation target.
- `db-replica-02`: planned replica lag validation target.
- Replication status output: planned source for lag fields.
- `<test-database>` and `<test-table>`: placeholders for timestamp validation.
- DB exporter metric mapping: placeholder for future observability integration.
- Prometheus metric integration: placeholder for future S028 work.

## Lag Measurement Model

- Replica status fields provide direct lag indicators through `Seconds_Behind_Source` or `Seconds_Behind_Master`.
- Primary timestamp write uses a placeholder row or event in `<test-database>.<test-table>`.
- Replica read delay compares the primary timestamp with the time observed on replicas.
- Lag values are compared against provisional NORMAL, WARNING, and CRITICAL thresholds.
- Metric mapping is documented only; exporter installation and Prometheus discovery are outside this scenario.

## Boundary Notes

This scenario validates replication lag only. Replication setup, access control, backup, restore, replica failure, primary stop runbooks, automatic failover, and split-brain automation are separate or excluded responsibilities.
