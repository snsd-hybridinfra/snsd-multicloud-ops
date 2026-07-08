# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Azure NSG existence validation plan | `commands.md`; `configs/azure-nsg-rule-summary.md`; `validation.md` | command plan, rule summary, validation record | yes |
| SSH inbound restricted to Bastion CIDR validation plan | `commands.md`; `configs/azure-nsg-least-privilege-policy.md`; `validation.md` | command plan, policy summary, validation record | yes |
| HTTP/HTTPS inbound exposure validation plan | `commands.md`; `configs/azure-nsg-rule-summary.md`; `validation.md` | command plan, rule summary, validation record | yes |
| DB port 3306 not exposed to public internet validation plan | `commands.md`; `configs/azure-nsg-least-privilege-policy.md`; `validation.md` | command plan, policy summary, validation record | yes |
| Azure App-to-On-Prem DB access rule validation plan | `commands.md`; `configs/azure-nsg-rule-summary.md`; `validation.md` | command plan, rule summary, validation record | yes |
| Monitoring scrape access rule validation plan | `commands.md`; `configs/azure-nsg-rule-summary.md`; `validation.md` | command plan, rule summary, validation record | yes |
| No Any/Internet SSH rule validation plan | `commands.md`; `logs/azure-nsg-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| No unrestricted all-ports inbound rule validation plan | `commands.md`; `logs/azure-nsg-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Outbound rule review plan | `commands.md`; `configs/azure-nsg-least-privilege-policy.md`; `validation.md` | command plan, policy summary, validation record | yes |
| Terraform plan or Azure CLI NSG rule capture plan | `commands.md`; `logs/azure-nsg-validation.log`; `screenshots/azure-nsg-rules.png`; `validation.md` | command plan, log, screenshot reference, validation record | yes |
| Failure condition for unrestricted SSH, unrestricted DB, missing Bastion rule, missing service rule, or unexpected wide-open inbound rule | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real Azure NSG output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
