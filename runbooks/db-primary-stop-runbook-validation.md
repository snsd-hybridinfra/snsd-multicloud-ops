# DB Primary Stop Runbook Validation

S034 validates a controlled MariaDB Primary-stop response using local sanitized evidence only.

1. Record active Primary role, symbolic master status, replica threads, and lag.
2. A separately authorized operator may run `systemctl stop <primary-service-name-placeholder>` as **MANUAL FAULT INJECTION ONLY** in a disposable lab.
3. Record Primary inactive/connection-refused/exporter-down placeholders and application write impact.
4. Confirm `<db-replica-host-placeholder>` is **not promoted**, remains read-only, and reports source unavailable/NULL lag.
5. Record `systemctl start <primary-service-name-placeholder>` as **MANUAL RECOVERY ACTION ONLY**.
6. Validate restored Primary role, symbolic `<binlog-file-placeholder>`/`<binlog-position-placeholder>`, healthy replica threads, lag within `<replication-lag-threshold-seconds>`, and evidence under `<evidence-path>`.

The validator performs no database connection, SQL, stop/start, promotion, failover, replication change, Ansible execution, monitoring query, or network action. Automatic promotion, automatic failover, production-grade HA, and cross-cloud DR are excluded.
