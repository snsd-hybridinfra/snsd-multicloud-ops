# EDR and XDR adoption decision

Decision: `DEFERRED`.

The current Phase 1 endpoint package has one 2-vCPU/4-GB monitoring VM pilot,
two infrastructure hosts protected by existing restricted validators, a
legacy virtual router, and no agent-management plane. Installing an endpoint
agent now would add CPU, memory, kernel-compatibility, privacy, lifecycle, and
false-positive operations without an approved central management or tested
uninstall path. Existing telemetry validates sanitized state summaries but is
not EDR, and independent validators are not XDR.

Reconsideration requires a separately approved non-critical pilot, measured
resource headroom, kernel compatibility, a pre-installation recovery point,
an uninstall test, privacy review, telemetry health verification, and explicit
approval. Automated isolation and remediation remain prohibited. Capability
`ZT-2.4.1` therefore remains reference-only and not validated.
