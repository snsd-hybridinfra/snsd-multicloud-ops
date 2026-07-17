# Failure Condition

## Failure Conditions

- Kolla deployment or post-deploy authentication fails.
- A required core service, Nova service, hypervisor, or Neutron agent is unavailable.
- A provider/tenant network, router, image, instance, or Floating IP is not active.
- Required router/DHCP namespaces or OVS provider mappings are absent.
- EVE-NG cannot reach the external router/Floating IP after convergence.
- The instance cannot reach its gateway or the public IPv4 network.
- Cloud-init completion is not observed.
- Evidence is incomplete, provenance is unclear, or sensitive values remain.

`LOCAL(br-ex)` DOWN alone is not a failure when the provider NIC, OVS mapping,
and end-to-end functional path all pass.

## Evidence of Failure

Record failed or inconclusive checks in `validation.md` without copying tokens,
authentication files, IDs, or raw terminal output.

## Follow-Up Requirement

Keep the scenario `IN_PROGRESS`, `PARTIAL`, or `BLOCKED` until the failed check
is rerun and sanitized evidence closes the gap.
