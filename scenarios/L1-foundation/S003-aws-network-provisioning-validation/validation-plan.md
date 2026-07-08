# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Terraform AWS provider initialization plan | Document planned `terraform init` validation without credentials. | Initialization approach is defined without provider credentials or backend state. | `commands.md`, `configs/aws-network-plan-summary.md`, `validation.md` |
| V002 | Terraform validate plan | Document planned `terraform validate` check. | Configuration validation approach is defined for future AWS network code. | `commands.md`, `logs/terraform-aws-network-validation.log`, `validation.md` |
| V003 | AWS VPC creation validation plan | Define how `<aws-vpc-id>` would be confirmed after approved execution. | VPC validation method is documented. | `configs/aws-network-plan-summary.md`, `validation.md`, `screenshots/aws-vpc-resource-view.png` |
| V004 | AWS subnet creation validation plan | Define public and private subnet validation checks. | Public and private subnet validation method is documented. | `configs/aws-network-plan-summary.md`, `validation.md`, `screenshots/aws-vpc-resource-view.png` |
| V005 | AWS route table validation plan | Define route table and association validation checks. | Route table validation method is documented. | `commands.md`, `logs/terraform-aws-network-validation.log`, `validation.md` |
| V006 | AWS security group baseline validation plan | Define baseline security group validation checks. | Security group baseline validation method is documented without rule implementation. | `configs/aws-network-plan-summary.md`, `validation.md` |
| V007 | Terraform output capture plan | Define expected sanitized Terraform outputs. | Output capture method is documented without tfstate content. | `commands.md`, `logs/terraform-aws-network-validation.log`, `validation.md` |
| V008 | AWS CLI resource listing plan | Define planned AWS CLI list or describe commands. | AWS CLI evidence capture method is documented with placeholders only. | `commands.md`, `logs/terraform-aws-network-validation.log`, `validation.md` |
| V009 | Missing VPC, subnet, route, or security group failure condition | Define explicit missing-resource failure criteria. | Missing required AWS network resources produce `FAIL` or `BLOCKED` status. | `validation.md` |
| V010 | Rollback plan using terraform destroy checklist | Define future approved teardown checklist. | Rollback steps are documented without executing destroy. | `commands.md`, `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario does not create real AWS resources or execute Terraform against a real AWS account.
