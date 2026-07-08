# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| OpenStack CLI authentication validation plan | `commands.md`; `configs/openstack-network-plan-summary.md`; `validation.md` | command plan, plan summary, validation record | yes |
| OpenStack network list validation plan | `commands.md`; `logs/openstack-network-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Provider network existence validation plan | `configs/openstack-network-plan-summary.md`; `validation.md`; `screenshots/openstack-network-resource-view.png` | plan summary, validation record, screenshot reference | yes |
| Tenant network creation validation plan | `configs/openstack-network-plan-summary.md`; `validation.md`; `screenshots/openstack-network-resource-view.png` | plan summary, validation record, screenshot reference | yes |
| Tenant subnet creation validation plan | `configs/openstack-network-plan-summary.md`; `validation.md` | plan summary, validation record | yes |
| Router creation validation plan | `commands.md`; `logs/openstack-network-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Router interface validation plan | `commands.md`; `logs/openstack-network-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Security group baseline validation plan | `configs/openstack-network-plan-summary.md`; `validation.md` | plan summary, validation record | yes |
| Floating IP availability validation plan | `commands.md`; `logs/openstack-network-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Terraform or OpenStack CLI output capture plan | `commands.md`; `logs/openstack-network-validation.log`; `validation.md` | command plan, output capture log, validation record | yes |
| Missing network, subnet, router, interface, or security group failure condition | `validation.md` | failure criteria and status record | yes |
| Rollback using Terraform destroy or OpenStack CLI cleanup checklist | `commands.md`; `validation.md` | rollback checklist and validation record | yes |

## Evidence Notes

No real Terraform or OpenStack output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
