# Expected Result

## Technical Result

- The EVE-NG host has separate operational NAT and host-only paths plus KVM.
- `SNSD-R1` and `SNSD-SW1` boot and retain configuration after reload.
- Six VLANs and gateway subinterfaces operate across an 802.1Q trunk.
- The router has a default route and PAT provides external connectivity.
- Baseline inter-VLAN routing works.
- The temporary directional ACL denies the intended DMZ-originated flow while
  retaining approved gateway, internet, and reverse-direction traffic.
- The temporary ACL is removed after capture.

## Completion Criteria

All E001-E014 categories, including allowed, denied, reverse-direction,
cleanup, SSH, and HTTP evidence, are represented. S002 is `VALIDATED` with
evidence readiness `READY`.
