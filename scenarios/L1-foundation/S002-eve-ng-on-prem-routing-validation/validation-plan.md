# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| E001 | EVE-NG host network readiness | NAT, host-only, SSH/HTTP, and bridges are operational. | Sanitized host and management output |
| E002 | KVM availability | Hardware acceleration is available. | Sanitized KVM output |
| E003 | Router and switch boot | Both named nodes boot successfully. | Sanitized version/uptime output |
| E004 | VLAN inventory | VLANs 20/30/40/50/60/70 exist with intended names. | Sanitized VLAN output |
| E005 | Trunk validation | Router-switch 802.1Q trunk is operational. | Sanitized trunk output |
| E006 | Router subinterface inventory | Six gateway subinterfaces are up. | Sanitized interface output |
| E007 | Routing table | Six connected service routes exist. | Sanitized route output |
| E008 | Default route | Router default route uses the masked VMware NAT gateway. | Sanitized route output |
| E009 | PAT/NAT translations | PAT translations and counters increase. | Sanitized NAT/ACL counter output |
| E010 | Zone-to-zone routing | VLAN 20 and VLAN 30 communicate before ACL application. | Sanitized allowed traffic output |
| E011 | Directional ACL deny | DMZ-originated ICMP toward Kubernetes is denied. | Sanitized denied traffic and counter output |
| E012 | Reverse-direction permit | Kubernetes-to-DMZ validation succeeds. | Sanitized permitted traffic output |
| E013 | Configuration persistence | Register and intended configuration persist after reload. | Sanitized reload/startup output |
| E014 | Final topology summary | Topology, cleanup, and integration boundaries are documented. | Sanitized summary and gap matrix |

Every category must have actual sanitized execution output before S002 can be
`VALIDATED`.
