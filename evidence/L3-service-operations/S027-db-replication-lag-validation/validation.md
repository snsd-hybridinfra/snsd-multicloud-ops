# Validation

Scenario: S027-db-replication-lag-validation
Level: L3-service-operations
Mode: StaticEvidence
Date: 2026-07-13
Overall status: PASS

| Check ID | Check Description | Expected Condition | Actual Result | Status | Evidence File |
|---|---|---|---|---|---|
| V001 | Required baseline and sample files | Seven artifacts exist. | All exist. | PASS | summary |
| V002 | Replication lag threshold model | Ranges/threads/errors/matrix complete. | Complete. | PASS | runbook/matrix; summary |
| V003 | Prometheus metric placeholders | Four names and boundaries exist. | Complete. | PASS | metric reference; summary |
| V004 | Normal lag evidence | Healthy and 0-5. | NORMAL at 0. | PASS | normal sample; summary |
| V005 | Warning lag evidence | Healthy and 6-30. | WARNING at 12. | WARN | warning sample; summary |
| V006 | Critical lag negative fixture | Detect above 30. | CRITICAL at 45 detected. | PASS | critical sample; summary |
| V007 | NULL lag negative fixture | Detect NULL/thread/error failure. | Expected failure detected. | PASS | NULL sample; summary |
| V008 | Thread health parsing | Distinguish healthy/stopped. | Correct. | PASS | samples; summary |
| V009 | Replication error parsing | Empty positives, placeholder negative. | Correct. | PASS | samples; summary |
| V010 | Replication terminology | Modern or legacy. | Modern. | PASS | samples; summary |
| V011 | Database credential and connection safety | None. | None detected. | PASS | log; summary |
| V012 | Database dump file safety | None. | None detected. | PASS | log; summary |
| V013 | Observability credential safety | None. | None detected. | PASS | log; summary |
| V014 | Address and account-specific safety | None. | None detected. | PASS | log; summary |
| V015 | Static execution boundary | No external query/destructive path. | Confirmed. | PASS | script; summary |
| V016 | Validation mode | Four marked fixtures. | StaticEvidence complete. | PASS | samples; summary |

## Generated Result

- Critical failures: 0
- Warnings: 1 (expected warning-range fixture)
- Critical fixture: EXPECTED_CRITICAL_DETECTED
- NULL fixture: EXPECTED_NULL_FAILURE_DETECTED
- Final judgment: PASS
- No MariaDB, Prometheus, or Grafana access; SQL/API query; credential read; replication change; dump; or network action occurred.
