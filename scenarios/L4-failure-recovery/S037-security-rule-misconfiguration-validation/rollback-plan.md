# Rollback Plan

1. Stop validation if real public IPs, cloud account IDs, credentials, secrets, private keys, or account-specific values appear in commands or evidence.
2. If future execution leaves a rule in an unsafe state, pause additional misconfiguration testing and restore the approved baseline using documented manual procedures.
3. Remove or sanitize unapproved evidence from `commands.md`, `validation.md`, `configs/`, `logs/`, and `screenshots/`.
4. Recheck that only placeholders such as `<security-group-id>`, `<nsg-name>`, `<openstack-security-group>`, `<firewall-rule>`, `<allowed-cidr>`, `<unauthorized-cidr>`, and `<service-port>` remain.
5. Mark S037 as `BLOCKED` if safe detection, manual rollback, or post-rollback validation cannot be completed.
6. Preserve a short note in `docs/implementation-log.md` if rollback or sanitization is required.

No real cloud firewall, security group, NSG, OpenStack security group, WAF, IDS/IPS, EDR, SOAR, or CSPM capability is created by this documentation skeleton.
