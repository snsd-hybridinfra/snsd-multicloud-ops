# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Hostname naming convention validation plan | Review `*.snsd.local` names and approved prefixes. | Hostnames follow the documented naming convention. | `commands.md`, `configs/hostname-resolution-plan.md`, `validation.md` |
| V002 | Hostname-to-inventory consistency validation plan | Compare hostname plan with inventory placeholder groups. | Hostnames map consistently to inventory placeholders. | `configs/hostname-inventory-mapping.md`, `validation.md` |
| V003 | Control Plane hostname resolution plan | Document lookup plan for `control.snsd.local`. | Control Plane hostname maps to `<control-plane-ip>`. | `commands.md`, `logs/hostname-resolution-validation.log`, `validation.md` |
| V004 | Bastion hostname resolution plan | Document lookup plan for `bastion.snsd.local`. | Bastion hostname maps to `<bastion-ip>`. | `commands.md`, `logs/hostname-resolution-validation.log`, `validation.md` |
| V005 | On-Prem DB hostname resolution plan | Document lookup plan for DB primary and replicas. | DB hostnames map to DB placeholders. | `commands.md`, `configs/hostname-inventory-mapping.md`, `validation.md` |
| V006 | On-Prem Monitoring hostname resolution plan | Document lookup plan for Prometheus and Grafana hostnames. | Monitoring hostnames map to monitoring placeholders. | `commands.md`, `configs/hostname-inventory-mapping.md`, `validation.md` |
| V007 | AWS service node hostname resolution plan | Document lookup plan for `aws-app-01.snsd.local`. | AWS service hostname maps to `<aws-app-node-ip>`. | `commands.md`, `logs/hostname-resolution-validation.log`, `validation.md` |
| V008 | Azure service node hostname resolution plan | Document lookup plan for `azure-app-01.snsd.local`. | Azure service hostname maps to `<azure-app-node-ip>`. | `commands.md`, `logs/hostname-resolution-validation.log`, `validation.md` |
| V009 | OpenStack service node hostname resolution plan | Document lookup plan for `openstack-app-01.snsd.local`. | OpenStack service hostname maps to `<openstack-app-node-ip>`. | `commands.md`, `logs/hostname-resolution-validation.log`, `validation.md` |
| V010 | Prometheus target hostname consistency plan | Review Prometheus target naming model. | Prometheus targets use consistent hostname placeholders. | `configs/hostname-resolution-plan.md`, `screenshots/hostname-resolution-test.png`, `validation.md` |
| V011 | Evidence target hostname consistency plan | Review evidence target hostnames and inventory mapping. | Evidence target hostnames are consistent and sanitized. | `configs/hostname-inventory-mapping.md`, `validation.md` |
| V012 | Unresolved hostname, duplicate hostname, inconsistent inventory mapping, or real public IP exposure failure condition | Define explicit failure criteria. | Unsafe or inconsistent hostname data produces `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. Real DNS implementation is explicitly excluded from S009.
