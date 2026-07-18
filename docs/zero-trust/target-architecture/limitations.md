
# Limitations

- ZT-ARC-001 is architecture and local validation only.
- Capability implementation, validation, evidence authority, and maturity remain separate.
- The current baseline stays `UNASSESSED` for all 52 capabilities.
- The monitoring VM base and Docker work under `.runtime` do not establish a validated Grafana/Loki/Alloy stack.
- Keycloak, OIDC, MFA, role mapping, and protected Grafana access are not implemented by this task.
- Existing VM and physical-server adapters do not provision compute or hardware.
- AWS, Azure, Kubernetes, and additional OpenStack adapters remain roadmap-only.
- No automatic remediation is enabled.
- Device posture, behavior risk, continuous adaptive authorization, and dynamic risk are unavailable or future signals.
- Runbooks are design specifications until clean-operator and runtime tests exist.
- No overall maturity score is produced.
