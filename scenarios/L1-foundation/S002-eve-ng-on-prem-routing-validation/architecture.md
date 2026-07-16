# Architecture

```text
VMware NAT / Host-only Management
              |
          EVE-NG Host
              |
          SNSD-R1
              |
        802.1Q trunk
              |
          SNSD-SW1
   +-----+-----+-----+-----+-----+-----+
 VLAN20 VLAN30 VLAN40 VLAN50 VLAN60 VLAN70
  DMZ    K8S     DB    MON   BACKUP  OSP-PROVIDER
```

`SNSD-R1` provides six `/24` gateways, a VMware NAT-side DHCP uplink, a
default route through `<vmware-nat-gateway-masked>`, and PAT for
`10.10.0.0/16`. A temporary ACL was used only to prove directional behavior
and was removed after validation.

No service VM or OpenStack component is part of the implemented topology yet.
