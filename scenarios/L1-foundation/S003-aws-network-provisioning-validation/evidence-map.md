# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Terraform AWS provider initialization plan | `commands.md`; `configs/aws-network-plan-summary.md`; `validation.md` | command plan, plan summary, validation record | yes |
| Terraform validate plan | `commands.md`; `logs/terraform-aws-network-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| AWS VPC creation validation plan | `configs/aws-network-plan-summary.md`; `validation.md`; `screenshots/aws-vpc-resource-view.png` | plan summary, validation record, screenshot reference | yes |
| AWS subnet creation validation plan | `configs/aws-network-plan-summary.md`; `validation.md`; `screenshots/aws-vpc-resource-view.png` | plan summary, validation record, screenshot reference | yes |
| AWS route table validation plan | `commands.md`; `logs/terraform-aws-network-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| AWS security group baseline validation plan | `configs/aws-network-plan-summary.md`; `validation.md` | plan summary, validation record | yes |
| Terraform output capture plan | `commands.md`; `logs/terraform-aws-network-validation.log`; `validation.md` | command plan, output capture log, validation record | yes |
| AWS CLI resource listing plan | `commands.md`; `logs/terraform-aws-network-validation.log`; `validation.md` | command plan, AWS CLI listing log, validation record | yes |
| Missing VPC, subnet, route, or security group failure condition | `validation.md` | failure criteria and status record | yes |
| Rollback plan using terraform destroy checklist | `commands.md`; `validation.md` | rollback checklist and validation record | yes |

## Evidence Notes

No real Terraform or AWS output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
