# S033-db-replica-failure-validation

| Field | Value |
|---|---|
| Scenario ID | S033 |
| Scenario Name | DB Replica Failure Validation |
| Level | L4 Failure Recovery Validation |
| Category | Failure Recovery |
| Related Components | MariaDB Primary, Replica, replication threads, lag, catch-up |
| Validation Type | StaticEvidence only |
| Evidence Directory | evidence/L4-failure-recovery/S033-db-replica-failure-validation/ |
| Status | VALIDATED |

## Objective Summary

Validate a controlled MariaDB replica outage workflow, Primary availability, and sanitized recovery/catch-up evidence without accessing a database.

## Scope Summary

The validator reads local documentation and samples only. It performs no SQL, database connection, service action, Ansible execution, monitoring query, failover, or replication change.

## Validation Summary

Fifteen checks cover artifacts, boundaries, criteria, safe examples, pre/failure/Primary/post/catch-up evidence, timing, sensitive data, and execution safety.

## Evidence Output Summary

Committed samples are non-production. Generated evidence contains local parsing judgments only.
