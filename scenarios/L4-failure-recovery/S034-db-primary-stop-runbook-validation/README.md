# S034-db-primary-stop-runbook-validation

| Field | Value |
|---|---|
| Scenario ID | S034 |
| Scenario Name | DB Primary Stop Runbook Validation |
| Level | L4 Failure and Recovery Validation |
| Category | Failure Recovery |
| Primary Domain | MariaDB Primary outage manual runbook response |
| Related Components | MariaDB Primary, MariaDB Replicas, replication state, application DB dependency placeholder, manual decision points, recovery threshold model |
| Validation Type | Failure Recovery Validation |
| Evidence Directory | evidence/L4-failure-recovery/S034-db-primary-stop-runbook-validation/ |
| Status | PLANNED |

## Objective Summary

Define and validate the manual runbook response model for MariaDB Primary stop events in the On-Prem Internal Server Zone database layer.

## Scope Summary

This scenario validates manual DB Primary stop runbook behavior only. It covers pre-failure Primary, Replica, and replication state; placeholder Primary stop injection; Primary write failure detection; application impact placeholder; Replica state verification; manual decision points; Primary restoration; post-recovery replication state; and runbook evidence collection.

## Validation Summary

Validation checks confirm that a Primary outage is detectable, application impact is documented, Replica state is reviewed, manual decision points are explicit, restoration is planned, replication state is reviewed after recovery, and failures such as unclear decision points, accidental automatic failover claims, Primary restoration failure, replication not resumed, application dependency unavailability, or missing evidence are captured.

## Evidence Output Summary

Evidence must be recorded under `evidence/L4-failure-recovery/S034-db-primary-stop-runbook-validation/`, with command plans in `commands.md`, validation results in `validation.md`, and future sanitized supporting artifacts under `configs/`, `logs/`, and `screenshots/`.
