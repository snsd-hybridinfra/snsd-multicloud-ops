# Validation

Scenario: S002-eve-ng-on-prem-routing-validation

Level: L1-foundation

Overall status: `PASS`

| Check ID | Validation Item | Expected Condition | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| B001 | Interface inventory | `eth0`-`eth7` and `pnet0`-`pnet7` are present; unattached placeholders are distinguished. | Observed; `pnet8` and `pnet9` are no-carrier placeholders. | PASS | `logs/20260715-S002-eve-uplink-bootstrap.sanitized.txt` |
| B002 | Bridge membership | Each active `pnet` bridge maps to the corresponding physical interface. | `pnet0`-`pnet7` map to `eth0`-`eth7`. | PASS | `logs/20260715-S002-eve-uplink-bootstrap.sanitized.txt` |
| B003 | NAT-side address | `pnet0` has a sanitized IPv4 address consistent with the operator-confirmed DHCP bootstrap. | Masked address presence and the NAT uplink role are represented. | PASS | `logs/20260715-S002-eve-uplink-bootstrap.sanitized.txt`, `logs/20260716-S002-router-switch-network-state.sanitized.txt` |
| B004 | Default route ownership | Only `pnet0` owns the default route. | One default route via `pnet0` was observed. | PASS | `logs/20260715-S002-eve-uplink-bootstrap.sanitized.txt` |
| B005 | NAT gateway reachability | A read-only probe reaches the VMware NAT gateway. | Masked gateway probe succeeded. | PASS | `logs/20260716-S002-router-switch-network-state.sanitized.txt` |
| B006 | Public IPv4 reachability | A read-only probe reaches a public test endpoint. | Masked public-connectivity probe succeeded. | PASS | `logs/20260716-S002-router-switch-network-state.sanitized.txt` |
| B007 | Host-only management readiness | `pnet1` is up without a default route; host reachability is separately checked. | Interface posture, ping, SSH/22, and HTTP/80 succeeded; HTTPS/443 was unavailable. | PASS | `logs/20260715-S002-eve-uplink-bootstrap.sanitized.txt`, `logs/20260716-S002-management-reachability.sanitized.txt` |
| B008 | Evidence integrity | Runtime addresses, networks, gateway, MACs, and bridge IDs are masked; raw output is absent. | Sanitization review passed. | PASS | `logs/20260715-S002-eve-uplink-bootstrap.sanitized.txt` |
| B009 | S002 routing boundary | Internal routing and ACL behavior are supported by sanitized execution output. | Pre-ACL allow, directional deny, reverse permit, and post-removal restoration are represented. | PASS | `logs/20260716-S002-routing-acl-connectivity.sanitized.txt`, `logs/20260716-S002-post-acl-cleanup.sanitized.txt` |

## Network Foundation Evidence Chain

| Check ID | Required category | Operator-confirmed result | Repository evidence result | Status | Evidence |
|---|---|---|---|---|---|
| E001 | EVE-NG host network readiness | NAT and host-only paths operational; SSH/HTTP confirmed | NAT, host-only ping, SSH/22, and HTTP/80 evidenced; HTTPS/443 is unavailable | PASS | `logs/20260715-S002-eve-uplink-bootstrap.sanitized.txt`, `logs/20260716-S002-router-switch-network-state.sanitized.txt`, `logs/20260716-S002-management-reachability.sanitized.txt` |
| E002 | KVM availability | Available | AMD KVM and core KVM modules loaded | PASS | `logs/20260716-S002-kvm-availability.sanitized.txt` |
| E003 | Router and switch boot | Both nodes booted | Both nodes accepted and returned populated live CLI state | PASS | `logs/20260716-S002-router-switch-network-state.sanitized.txt` |
| E004 | VLAN inventory | VLANs 20/30/40/50/60/70 configured | All six VLANs active | PASS | `logs/20260716-S002-router-switch-network-state.sanitized.txt` |
| E005 | Trunk validation | 802.1Q trunk operational | Trunking with all six VLANs active and forwarding | PASS | `logs/20260716-S002-router-switch-network-state.sanitized.txt` |
| E006 | Router subinterfaces | Six gateways configured | All six required subinterfaces up/up | PASS | `logs/20260716-S002-router-switch-network-state.sanitized.txt` |
| E007 | Routing table | Connected VLAN routing reported operational | Six connected VLAN routes present | PASS | `logs/20260716-S002-router-switch-network-state.sanitized.txt` |
| E008 | Default route | Router default route through VMware NAT reported | Masked default route present | PASS | `logs/20260716-S002-router-switch-network-state.sanitized.txt` |
| E009 | PAT/NAT translations | Overload and counter increases reported | Five dynamic translations, nine hits, and five NAT ACL matches | PASS | `logs/20260716-S002-router-switch-network-state.sanitized.txt` |
| E010 | Zone-to-zone routing | VLAN 20 and VLAN 30 communicated before ACL | Five successful pre-ACL replies observed | PASS | `logs/20260716-S002-routing-acl-connectivity.sanitized.txt` |
| E011 | Directional ACL deny | DMZ-to-Kubernetes ICMP echo denied | Five administrative-prohibition responses observed | PASS | `logs/20260716-S002-routing-acl-connectivity.sanitized.txt` |
| E012 | Reverse-direction permit | Kubernetes-to-DMZ succeeded | Five successful reverse-direction replies observed | PASS | `logs/20260716-S002-routing-acl-connectivity.sanitized.txt` |
| E013 | Configuration persistence | Config register corrected and reload persistence confirmed | Register is `0x2102`; intended interfaces are loaded from NVRAM in operator-confirmed post-reload output | PASS | `logs/20260716-S002-router-switch-network-state.sanitized.txt` |
| E014 | Final topology and cleanup | Network foundation and post-test cleanup are documented | NAT ACL remains; temporary directional ACL is absent; post-cleanup DMZ-to-Kubernetes returned four replies after one initial timeout | PASS | `configs/20260716-S002-network-foundation-topology-summary.md`, `logs/20260716-S002-post-acl-cleanup.sanitized.txt` |

The evidence chain now contains both pre-ACL allowed and post-ACL denied
DMZ-to-Kubernetes traffic, plus preserved DMZ-gateway and public reachability.
All E001-E014 categories are represented by sanitized execution evidence or a
sanitized summary grounded in that evidence. S002 is `VALIDATED` and its
evidence readiness is `READY`. Service VM and OpenStack integration remain
`NOT_STARTED`.
