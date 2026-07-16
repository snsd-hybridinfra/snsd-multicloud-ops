# Evidence Map

| Check ID | Evidence Location | Current State |
|---|---|---|
| E001 | `logs/20260715-S002-eve-uplink-bootstrap.sanitized.txt`; `logs/20260716-S002-router-switch-network-state.sanitized.txt`; `logs/20260716-S002-management-reachability.sanitized.txt` | EVIDENCED |
| E002 | `logs/20260716-S002-kvm-availability.sanitized.txt` | EVIDENCED |
| E003 | `logs/20260716-S002-router-switch-network-state.sanitized.txt` | EVIDENCED |
| E004 | `logs/20260716-S002-router-switch-network-state.sanitized.txt` | EVIDENCED |
| E005 | `logs/20260716-S002-router-switch-network-state.sanitized.txt` | EVIDENCED |
| E006 | `logs/20260716-S002-router-switch-network-state.sanitized.txt` | EVIDENCED |
| E007 | `logs/20260716-S002-router-switch-network-state.sanitized.txt` | EVIDENCED |
| E008 | `logs/20260716-S002-router-switch-network-state.sanitized.txt` | EVIDENCED |
| E009 | `logs/20260716-S002-router-switch-network-state.sanitized.txt` | EVIDENCED |
| E010 | `logs/20260716-S002-routing-acl-connectivity.sanitized.txt` | EVIDENCED |
| E011 | `logs/20260716-S002-routing-acl-connectivity.sanitized.txt` | EVIDENCED |
| E012 | `logs/20260716-S002-routing-acl-connectivity.sanitized.txt` | EVIDENCED |
| E013 | `logs/20260716-S002-router-switch-network-state.sanitized.txt` | EVIDENCED |
| E014 | `configs/20260716-S002-network-foundation-topology-summary.md`; `logs/20260716-S002-post-acl-cleanup.sanitized.txt` | EVIDENCED |
| All checks | `commands.md`, `validation.md` | READY |

## Evidence Safety Boundary

Sanitized host-only ping, SSH/22, and HTTP/80 management output are represented.
KVM, node boot,
VLANs, trunk, subinterfaces, routes, PAT, baseline allowed traffic,
directional deny, reverse-direction permit, persistence, and cleanup are now
represented. Raw
outputs, device serials, MACs, runtime addresses, proprietary image details,
credentials, secrets, and binaries are prohibited.
