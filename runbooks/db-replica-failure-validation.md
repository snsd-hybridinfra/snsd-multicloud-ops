# DB Replica Failure Validation

S033 validates a controlled MariaDB replica failure workflow using sanitized local evidence only.

## Workflow

1. Record replica service state, IO/SQL thread health, and lag for `<db-replica-host-placeholder>`.
2. A separately authorized operator may perform `systemctl stop <replica-service-name-placeholder>` as **MANUAL FAULT INJECTION ONLY** in a disposable lab.
3. Record service/thread failure, `Seconds_Behind_Master: NULL`, and `<replica-io-error-placeholder>` or `<replica-sql-error-placeholder>`.
4. Confirm the Primary remains reachable and read/write role remains available at `<db-primary-host-placeholder>`.
5. Record **MANUAL RECOVERY ACTION ONLY**, healthy replica threads, lag within `<replication-lag-threshold-seconds>`, and catch-up evidence under `<evidence-path>`.

The validator performs no database connection, SQL, service action, replication reset, promotion, failover, or Prometheus/Grafana query. Automatic failover and production-grade HA are out of scope.
