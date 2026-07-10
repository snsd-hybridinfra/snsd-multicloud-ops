# Rollback Plan

1. Stop load balancer failure validation if real public IPs, DNS records, TLS keys, certificates, credentials, secrets, or account-specific values appear in commands or evidence.
2. If future execution leaves the entrypoint unavailable, pause additional failure injection and restore the expected entrypoint state using approved manual operational procedures.
3. Remove or sanitize unapproved evidence from `commands.md`, `validation.md`, `configs/`, `logs/`, and `screenshots/`.
4. Recheck that only placeholders such as `<load-balancer-endpoint>`, `<reverse-proxy-host>`, `<ingress-host>`, `<backend-service>`, `<web-endpoint>`, `<api-endpoint>`, `<health-endpoint>`, and `<recovery-threshold-seconds>` remain.
5. Mark S035 as `BLOCKED` if safe failure detection, backend isolation, manual decision review, or restoration observation cannot be completed.
6. Preserve a short note in `docs/implementation-log.md` if rollback or sanitization is required.

No load balancer configuration, TLS material, automatic cross-cloud failover logic, or runtime resources are created by this documentation skeleton.
