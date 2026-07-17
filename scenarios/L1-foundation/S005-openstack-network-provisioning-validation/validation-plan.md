# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Kolla deployment workflow | Review normalized operator result | Bootstrap, prechecks, pull, deploy, and post-deploy succeed | `validation.md`, sanitized log |
| V002 | Keystone authentication | Review token-issuance result with value omitted | Authentication succeeds | `validation.md`, sanitized log |
| V003 | Core services and endpoints | Review service/endpoint summary | Keystone, Nova, Placement, Glance, and Neutron are registered | `validation.md`, sanitized log |
| V004 | Nova services | Review compute-service summary | Scheduler, conductor, and compute are enabled/up | `validation.md`, sanitized log |
| V005 | Hypervisor | Review hypervisor summary | AIO hypervisor is up and QEMU-based | `validation.md`, sanitized log |
| V006 | Neutron agents | Review network-agent summary | OVS, L3, DHCP, and metadata agents are alive/up | `validation.md`, sanitized log |
| V007 | Provider network | Review sanitized resource attributes | ACTIVE, flat, `physnet1`, external=true | `validation.md`, sanitized log |
| V008 | Tenant network and DHCP | Review network/subnet result | Tenant network is ACTIVE and DHCP address is assigned | `validation.md`, sanitized log |
| V009 | Router | Review router result | Router is ACTIVE with an external provider port | `validation.md`, sanitized log |
| V010 | Image | Review image result | Image is active | `validation.md`, sanitized log |
| V011 | Instance | Review server result | One instance is ACTIVE with a fixed address | `validation.md`, sanitized log |
| V012 | Floating IP | Review Floating IP result | Address is associated and ACTIVE | `validation.md`, sanitized log |
| V013 | Neutron namespaces | Review namespace result | Router and DHCP namespaces exist | `validation.md`, sanitized log |
| V014 | OVS provider mapping | Review bridge/port/OpenFlow result | Required bridges and patch path exist; provider NIC maps to `br-ex` with valid state/ofport | `validation.md`, sanitized log |
| V015 | EVE external-router reachability | Review probe result | Reachability succeeds after normal ARP convergence | `validation.md`, sanitized log |
| V016 | EVE Floating IP reachability | Review probe result | All recorded Floating IP probes succeed | `validation.md`, sanitized log |
| V017 | Instance gateway reachability | Review cloud-init result | Tenant gateway probe succeeds | `validation.md`, sanitized log |
| V018 | Instance Internet reachability | Review cloud-init result | Public IPv4 probe succeeds | `validation.md`, sanitized log |
| V019 | Cloud-init completion | Review markers | Start, end, and completion markers are present | `validation.md`, sanitized log |
| V020 | False-negative analysis | Correlate `LOCAL(br-ex)` with functional results | Local-port DOWN is not treated as forwarding failure | `validation.md`, summary |
| V021 | Evidence sanitization | Scan committed evidence | No raw secret, ID, MAC, dynamic address, or auth file is retained | `validation.md`, summary |

## Review Notes

An initial lost probe attributable to ARP convergence is retained as context;
the subsequent successful sequence supports the result. A mistyped external
address is excluded because it did not target the validated path.
