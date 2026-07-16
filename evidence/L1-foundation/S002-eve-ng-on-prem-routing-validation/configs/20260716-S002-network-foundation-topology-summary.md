# S002 Network Foundation Topology Summary

**Record type:** operator-confirmed implementation summary
**Evidence status:** READY - this summary is supported by the mapped sanitized
device and connectivity outputs; it is not a substitute for those source files.

## Implemented Topology

```text
VMware NAT
    |
    | DHCP uplink and default route
    v
SNSD-R1 (Cisco 3725)
    |
    | 802.1Q trunk / Router-on-a-Stick
    v
SNSD-SW1 (Cisco vIOS L2)
    |-- VLAN 20  DMZ
    |-- VLAN 30  KUBERNETES
    |-- VLAN 40  DATABASE
    |-- VLAN 50  MONITORING
    |-- VLAN 60  BACKUP
    `-- VLAN 70  OPENSTACK_PROVIDER
```

## Operator-Confirmed Implementation State

| Component | Reported state | Repository evidence state |
|---|---|---|
| EVE-NG NAT uplink and host-only management | NAT operational; host-only ping, SSH/22, and HTTP/80 operational | Sanitized host, ping, SSH, and HTTP output exists; HTTPS/443 is accurately recorded unavailable |
| KVM acceleration | Available | Kernel-module output exists |
| `pnet0` through `pnet7` | Operational | Interface and bridge-membership output exists |
| `SNSD-R1` and `SNSD-SW1` | Booted successfully | Live CLI state output proves both nodes operational |
| Configuration register | Corrected to `0x2102`; persistence confirmed after reload | Register and NVRAM-loaded interface output exists; reload transcript is not retained |
| Router-switch link | Duplex mismatch corrected | Connected full-duplex switch status exists |
| VLANs 20, 30, 40, 50, 60, 70 | Configured | Sanitized active VLAN inventory exists |
| Router-on-a-Stick trunk | Configured | Sanitized trunk and six up/up subinterface outputs exist |
| NAT/PAT | `10.10.0.0/16` overload operational | Sanitized translations, statistics, NAT ACL counter, gateway, and public connectivity output exists |
| Directional ACL | Pre-ACL DMZ-to-Kubernetes allow, post-ACL deny, and Kubernetes-to-DMZ reverse permit evidenced | NAT source ACL counter exists; directional ACL counter output is not retained |
| Temporary ACL cleanup | ACL removed and Cloud/LAN links restored | ACL inventory and DMZ subinterface prove no ACL attachment; four replies after one initial timeout prove DMZ-to-Kubernetes restoration |

## Gateway Plan

| VLAN | Zone | Gateway |
|---:|---|---|
| 20 | DMZ | `10.10.20.1/24` |
| 30 | Kubernetes | `10.10.30.1/24` |
| 40 | Database | `10.10.40.1/24` |
| 50 | Monitoring | `10.10.50.1/24` |
| 60 | Backup | `10.10.60.1/24` |
| 70 | OpenStack Provider | `10.10.70.1/24` |

WAN DHCP, VMware gateway, management addresses, MAC addresses, hardware serial
numbers, public test addresses, and proprietary image details are intentionally
absent or represented by approved placeholders.

## Final Boundary

- EVE-NG network foundation: operator-confirmed `IMPLEMENTED`
- VLAN and Router-on-a-Stick behavior: validated by sanitized VLAN, trunk, subinterface, and route output
- NAT/PAT behavior: validated by sanitized translations, statistics, and connectivity output
- Directional ACL behavior: pre-ACL allow, post-ACL deny, and reverse-direction permit evidenced
- Temporary ACL cleanup: validated by sanitized ACL inventory and interface attachment state
- S002 repository judgment: `VALIDATED` / evidence `READY`
- Service VM integration: `NOT_STARTED`
- OpenStack integration: `NOT_STARTED`
