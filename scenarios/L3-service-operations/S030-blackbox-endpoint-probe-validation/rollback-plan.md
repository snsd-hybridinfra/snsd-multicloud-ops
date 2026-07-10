# Rollback Plan

1. Stop endpoint probe validation if real endpoint values, credentials, TLS material, or account-specific data appear in commands or evidence.
2. Remove or sanitize any unapproved probe evidence from `commands.md`, `validation.md`, `configs/`, `logs/`, and `screenshots/`.
3. Revert S030 status to `BLOCKED` if endpoint categories cannot be mapped safely.
4. Recheck that only placeholder values such as `<blackbox-exporter-endpoint>`, `<probe-target>`, `<web-endpoint>`, `<api-endpoint>`, `<ingress-host>`, `<reverse-proxy-host>`, and `<health-endpoint>` remain.
5. Preserve a short note in `docs/implementation-log.md` if rollback or sanitization is required.

No infrastructure, Blackbox Exporter configuration, Prometheus configuration, TLS material, or endpoint implementation is changed by this documentation skeleton.
