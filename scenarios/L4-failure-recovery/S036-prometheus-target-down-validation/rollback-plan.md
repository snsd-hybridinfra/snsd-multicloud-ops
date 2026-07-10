# Rollback Plan

1. Stop target DOWN validation if real credentials, secrets, public IPs, private keys, or account-specific values appear in commands or evidence.
2. If future execution leaves a monitored target unavailable, pause additional failure injection and restore the expected exporter or endpoint state using approved manual operational procedures.
3. Remove or sanitize unapproved evidence from `commands.md`, `validation.md`, `configs/`, `logs/`, and `screenshots/`.
4. Recheck that only placeholders such as `<prometheus-endpoint>`, `<target-job>`, `<target-instance>`, `<node-exporter-target>`, `<db-exporter-target>`, `<blackbox-exporter-target>`, and `<recovery-threshold-seconds>` remain.
5. Mark S036 as `BLOCKED` if safe DOWN detection, query evidence, restoration, or UP recovery observation cannot be completed.
6. Preserve a short note in `docs/implementation-log.md` if rollback or sanitization is required.

No Prometheus configuration, Alertmanager integration, notification workflow, or SOAR-style response is created by this documentation skeleton.
