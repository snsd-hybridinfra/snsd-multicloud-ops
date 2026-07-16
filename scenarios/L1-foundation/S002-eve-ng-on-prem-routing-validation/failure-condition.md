# Failure Condition

- A required E001-E014 output is missing or cannot be sanitized.
- KVM, a required node, VLAN, trunk, subinterface, connected route, or default
  route is unavailable.
- PAT does not create translations or counters do not increase.
- Baseline allowed traffic fails before ACL application.
- The ACL fails to deny the intended direction or blocks approved reverse,
  gateway, or internet traffic.
- Configuration does not persist after reload.
- The temporary ACL or disconnected Cloud/LAN link is not restored.
- Raw identifiers, credentials, secrets, image details, binaries, MACs, serials,
  or unsanitized runtime addresses enter evidence.

Missing evidence is an incomplete result, not permission to infer `PASS`.
