# Implementation Log

This log records confirmed implementation events only. Repository/document
editing and linting are not runtime scenario implementation.

| Date | Scope | Result | Evidence |
|---|---|---|---|
| 2026-07-15 | Repository truth-state reset | All S001-S050 scenarios reset to NOT_STARTED; all evidence reset to NOT_READY/NOT_RUN; only an empty EVE-NG appliance is confirmed to exist | Previous non-executed and provenance-uncertain artifacts quarantined under `quarantine/non-authoritative-evidence/2026-07-15-truth-state-reset/` |
| 2026-07-15 | Lab Phase 0 host-capacity planning | Documented observed host capacity, planned VM allocations, mutually exclusive execution profiles, storage roles, snapshot limits, nested virtualization, and one-small-Nova-instance ceiling | Planning completion only; no infrastructure or scenario status changed and no runtime evidence created |
| 2026-07-15 | EVE-NG host uplink bootstrap | Documented sanitized interface, bridge, masked-address, and default-route evidence; `pnet0` is the NAT bootstrap bridge and `pnet1` is reserved for host-only management | S002 set to IN_PROGRESS/PARTIAL; gateway/public probe evidence and all internal routing/ACL implementation remain pending |
| 2026-07-16 | EVE-NG network-foundation validation completed | Sanitized E001-E014 evidence covers host/KVM, live devices, VLAN/routing, NAT/PAT, persistence, directional traffic, cleanup, host-only ping, SSH/22, and HTTP/80; topology PNG reviewed but not copied | S002 set to VALIDATED and evidence READY; HTTPS/443 remains an accurately recorded unavailable optional path |

No service VM, OpenStack, Kubernetes, MariaDB, monitoring, backup, AWS, or Azure
integration is recorded. The temporary validation ACL was operator-confirmed
removed after testing; no persistent firewall implementation is claimed.
