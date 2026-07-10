# S026-mariadb-primary-replica-replication-validation

| Field | Value |
|---|---|
| Scenario ID | S026 |
| Scenario Name | MariaDB Primary-Replica Replication Validation |
| Level | L3 Service Operations Validation |
| Category | Service Operations |
| Primary Domain | Database replication |
| Related Components | db-primary-01, db-replica-01, db-replica-02, replication user placeholder, binary logs, replica status |
| Validation Type | Service Operation Validation |
| Evidence Directory | evidence/L3-service-operations/S026-mariadb-primary-replica-replication-validation/ |
| Status | PLANNED |

## Objective Summary

Define and validate MariaDB Primary-Replica replication for the On-Prem Internal Server Zone in the SNSD Multi-Cloud Ops project.

## Scope Summary

This scenario validates MariaDB Primary-Replica replication only. It covers primary and replica role validation, replication user placeholders, binary log configuration, replica source configuration, primary write and replica read checks, replication status, replication error detection, and replication topology evidence collection.

## Validation Summary

Validation checks confirm that primary and replica roles are documented, replication configuration can be reviewed, write/read consistency is planned, `SHOW REPLICA STATUS` or `SHOW SLAVE STATUS` output is captured later, and failures such as stopped replication, errors, inconsistent data, missing binary logs, or missing replication user are explicitly captured.

## Evidence Output Summary

Evidence must be recorded under `evidence/L3-service-operations/S026-mariadb-primary-replica-replication-validation/`, with command plans in `commands.md`, validation results in `validation.md`, and future sanitized supporting artifacts under `configs/`, `logs/`, and `screenshots/`.
