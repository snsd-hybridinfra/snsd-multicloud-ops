# Scope

## Included

- EVE-NG NAT and host-only management readiness.
- KVM capability and `pnet0` through `pnet7` bridge readiness.
- `SNSD-R1` and `SNSD-SW1` boot and configuration persistence.
- VLANs 20, 30, 40, 50, 60, and 70.
- 802.1Q trunk and six Router-on-a-Stick subinterfaces.
- Connected routes, router default route, and PAT for `10.10.0.0/16`.
- Pre-ACL zone routing, directional deny, preserved allowed traffic, and
  reverse-direction permit.
- Temporary ACL removal and restoration of lab Cloud/LAN connections.
- Sanitized evidence and topology summary.

## Excluded

- Service VM deployment or service-zone application validation.
- OpenStack, Kubernetes, database, monitoring, backup, AWS, or Azure integration.
- Production firewall enforcement or persistent production ACLs.
- Cisco image files, filenames, checksums, binaries, serial numbers, or image
  acquisition details.
- Raw console output, credentials, secrets, runtime WAN/management addresses,
  MAC addresses, or hardware identifiers.

## Current Boundary

The implementation and required E001-E014 evidence chain are represented in
sanitized form. S002 is `VALIDATED`; service VM and cloud integrations remain
outside this scenario and are `NOT_STARTED`.
