# S002 EVE-NG Uplink Bootstrap Summary

> Historical bootstrap snapshot: this record was `PARTIAL` when captured on
> 2026-07-15. The later 2026-07-16 evidence chain resolves its connectivity and
> management gaps; current S002 status is `VALIDATED` with `READY` evidence.

| Field | Result |
|---|---|
| Evidence source | Real lab terminal output supplied by the operator |
| Validation mode | Sanitized host-interface and bridge observation |
| EVE-NG interface inventory | PASS - physical interfaces `eth0` through `eth7` and bridges `pnet0` through `pnet7` are up; `pnet8` and `pnet9` are no-carrier placeholders |
| `pnet0` to VMware VMnet8 mapping | PARTIAL - operator context identifies VMnet8 NAT; evidence directly confirms `pnet0` contains `eth0` |
| DHCP assignment | PARTIAL - a masked IPv4 address is present on `pnet0`; the supplied abbreviated output does not independently show DHCP lease metadata |
| Default route | PASS - the only observed default route uses `pnet0` and a masked VMware NAT gateway |
| VMware NAT gateway connectivity | NOT_EVIDENCED - no gateway ping output was supplied |
| Public IPv4 connectivity | NOT_EVIDENCED - no public connectivity output was supplied |
| DNS or HTTPS | NOT_EVIDENCED - no DNS or HTTPS output was supplied |
| `pnet1` management-network readiness | PARTIAL - `pnet1` is up, contains `eth1`, has a masked host-only address, and owns no default route; host-to-EVE reachability was not supplied |
| `pnet2` through `pnet7` bridge readiness | PASS - each bridge is up and has the corresponding `eth2` through `eth7` physical member; no Layer-3 service is claimed |
| Sensitive-data sanitization | PASS - runtime IPv4/IPv6 values, networks, gateway, MAC addresses, and bridge identifiers are masked; raw output is not committed |
| Final judgment | **PARTIAL** |

## Judgment Basis

The EVE-NG host bridge inventory, NAT-side address presence, host-only
management address presence, and `pnet0` default-route selection are evidenced.
The supplied output does not contain connectivity probes for the VMware NAT
gateway, public IPv4, DNS, or HTTPS. Later operator-confirmed router, VLAN,
NAT/PAT, and ACL implementation is tracked separately in the 2026-07-16
topology and evidence-gap summaries; it is not validated by this bootstrap
output alone.
