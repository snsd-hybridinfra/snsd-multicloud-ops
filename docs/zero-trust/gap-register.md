# Zero Trust Gap Register

Implementation sequencing and capability-specific blockers are maintained in the [machine-readable backlog](capability-implementation-backlog.yaml). A planned target or queue position does not close a gap; only accepted capability evidence can change these current-state entries.

| Gap ID | Category | Gap | Current evidence | Status | Next action |
|---|---|---|---|---|---|
| ZG-001 | identity | No MFA, continuous authentication, ICAM, conditional access, or identity-risk implementation | None | GAP_IDENTIFIED | Define bounded identity lab and evidence plan |
| ZG-002 | endpoint | No endpoint inventory, posture, UEM/MDM, EDR/XDR, or patch automation | None | GAP_IDENTIFIED | Select non-production endpoint scope before tooling |
| ZG-003 | network | Macro VLAN separation, routing, NAT, and the fixed provider path are evidenced; no persistent interface ACL binding exists, and micro-segmentation, traffic encryption, SDN policy, and resilience are not implemented | S002/S005 runtime plus ZT-NET-001 38 PASS/1 WARN/0 FAIL | PARTIAL | Require a separately approved least-privilege ACL change and live allow/deny evidence before stronger segmentation claims |
| ZG-004 | system | One restricted validator demonstrates a narrow access boundary; PAM and broad credential/policy management are absent | S005 restricted endpoint | PARTIAL | Define system-account and policy-control evidence |
| ZG-005 | application-workload | Kubernetes, ingress, application authorization, secure deployment, inventory, and software security are not implemented | Design only | GAP_IDENTIFIED | Implement existing S018-S025/S044 before assessment |
| ZG-006 | data | Database, data catalog, governance, classification, encryption, monitoring, and DLP are absent | Design only | GAP_IDENTIFIED | Establish data scope and ownership before implementation |
| ZG-007 | visibility-analytics | Four bounded live sources normalize into a deterministic local correlation pipeline, but persistent central log storage, host journals, dashboards, continuous analytics, and behavior analytics are absent | ZT-VIS-001 164 events; seven rules; controlled finding | PARTIAL | User installs the approved Monitoring VM with Docker/Compose, Grafana, Loki, and Alloy before persistent-storage validation |
| ZG-008 | automation-integration | Repository validators and one forced read-only validator exist; policy integration and automated response do not | Local tools and S005 endpoint | PARTIAL | Separate read-only validation from mutation/response authority |
| ZG-009 | governance | No capability maturity assessment has been completed | This framework only | UNASSESSED | Assess one bounded capability against its source table |
| ZG-010 | evidence | Most scenarios have design-only or no evidence | Tracking matrices | GAP_IDENTIFIED | Collect sanitized execution evidence under existing scenarios |
| ZG-011 | source terminology | Korean source names may drift if unofficial translations become canonical | Source catalog | OPEN | Keep Korean display names authoritative and slugs stable |
| ZG-012 | enterprise scope | A disposable lab could be misrepresented as enterprise Zero Trust | Limited lab evidence | OPEN | Keep environment and authority labels on every assessment |
