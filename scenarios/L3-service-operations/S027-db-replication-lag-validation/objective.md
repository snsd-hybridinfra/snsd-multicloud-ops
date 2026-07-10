# Objective

S027 defines the MariaDB replication lag measurement validation model for the On-Prem Internal Server Zone Primary-Replica database layer.

The scenario validates that replication lag can be measured from MariaDB replica status fields and from a placeholder primary timestamp write plus replica read delay model. It also defines provisional threshold bands for operational review and placeholders for future DB exporter and Prometheus metric mapping.

This scenario does not configure MariaDB replication, install exporters, or configure Prometheus. It defines how future lag evidence must be captured and reviewed.

## Operational Capability

- Confirm replica lag status fields are reviewable.
- Confirm `Seconds_Behind_Source` or `Seconds_Behind_Master` can be interpreted.
- Confirm primary timestamp write and replica read delay checks are planned.
- Confirm `db-replica-01` and `db-replica-02` lag checks are planned.
- Confirm provisional NORMAL, WARNING, and CRITICAL thresholds are documented.
- Confirm future metric mapping is defined as a placeholder only.
