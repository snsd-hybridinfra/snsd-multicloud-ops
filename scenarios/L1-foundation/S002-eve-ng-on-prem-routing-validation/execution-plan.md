# Execution Plan

1. Confirm EVE-NG host NAT, host-only management, KVM, and bridge readiness.
2. Boot `SNSD-R1` and `SNSD-SW1`; collect sanitized version and uptime output.
3. Confirm configuration register `0x2102` and persistence after reload.
4. Confirm VLAN inventory, trunk state, and duplex state.
5. Confirm router subinterfaces, connected routes, DHCP WAN, and default route.
6. Confirm DMZ gateway, VMware NAT gateway, and public IPv4 reachability.
7. Confirm PAT translations, statistics, and match counters.
8. Confirm VLAN 20-to-30 routing before ACL application.
9. Apply the temporary directional lab ACL and capture the intended deny.
10. Confirm gateway/internet traffic and reverse-direction traffic remain allowed.
11. Remove the temporary ACL and restore Cloud/LAN-segment connections.
12. Sanitize all output and update the evidence gap matrix.

No raw output or proprietary image detail may be committed.
