# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Hostname naming convention validation plan | `commands.md`; `configs/hostname-resolution-plan.md`; `validation.md` | command plan, hostname plan, validation record | yes |
| Hostname-to-inventory consistency validation plan | `configs/hostname-inventory-mapping.md`; `validation.md` | inventory mapping, validation record | yes |
| Control Plane hostname resolution plan | `commands.md`; `logs/hostname-resolution-validation.log`; `validation.md` | command plan, lookup log, validation record | yes |
| Bastion hostname resolution plan | `commands.md`; `logs/hostname-resolution-validation.log`; `validation.md` | command plan, lookup log, validation record | yes |
| On-Prem DB hostname resolution plan | `commands.md`; `configs/hostname-inventory-mapping.md`; `validation.md` | command plan, inventory mapping, validation record | yes |
| On-Prem Monitoring hostname resolution plan | `commands.md`; `configs/hostname-inventory-mapping.md`; `validation.md` | command plan, inventory mapping, validation record | yes |
| AWS service node hostname resolution plan | `commands.md`; `logs/hostname-resolution-validation.log`; `validation.md` | command plan, lookup log, validation record | yes |
| Azure service node hostname resolution plan | `commands.md`; `logs/hostname-resolution-validation.log`; `validation.md` | command plan, lookup log, validation record | yes |
| OpenStack service node hostname resolution plan | `commands.md`; `logs/hostname-resolution-validation.log`; `validation.md` | command plan, lookup log, validation record | yes |
| Prometheus target hostname consistency plan | `configs/hostname-resolution-plan.md`; `screenshots/hostname-resolution-test.png`; `validation.md` | hostname plan, screenshot reference, validation record | yes |
| Evidence target hostname consistency plan | `configs/hostname-inventory-mapping.md`; `validation.md` | inventory mapping, validation record | yes |
| Unresolved hostname, duplicate hostname, inconsistent inventory mapping, or real public IP exposure failure condition | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real hostname resolution output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
