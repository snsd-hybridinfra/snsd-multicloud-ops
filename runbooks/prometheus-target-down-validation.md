# Prometheus Target Down Validation

S036 validates target-down detection and recovery using sanitized local Prometheus evidence.

1. Confirm `<scrape-job-name>` and `<target-instance-placeholder>` are discovered and UP before failure.
2. A separately authorized operator may run `systemctl stop <exporter-name-placeholder>` using `<failure-method-placeholder>` as **MANUAL FAULT INJECTION ONLY** in a disposable lab.
3. Confirm target health DOWN, `up == 0`, scrape-error placeholder, and alert firing after `<target-down-duration-threshold>`.
4. Record `systemctl start <exporter-name-placeholder>` as **MANUAL RECOVERY ACTION ONLY**.
5. Confirm target UP, `up == 1`, alert resolved, and recovery within `<recovery-time-threshold-seconds>`; store under `<evidence-path>`.

Static mode parses samples and does not access `<prometheus-server>`. Explicit LivePrometheus is read-only and stores sanitized job/instance/health/up/timestamp judgments only. The validator never starts/stops exporters or Prometheus, reloads Prometheus, or changes rules. S028 owns normal discovery, S030 probing, and S040 final health.
