# Commands

Scenario: S003-aws-network-provisioning-validation
Level: L1-foundation
Capability: AWS Network Provisioning Validation
Target: `<target-node>`
Execution timestamp: TODO

Record sanitized output only. Do not include AWS credentials, access keys, account IDs, tokens, tfstate, private keys, real public IPs, private IPs, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Terraform AWS provider initialization plan | `terraform init` in the future approved AWS network module path | Confirm initialization plan without committing credentials or backend state. | TODO: record sanitized output after approved execution. |
| V002 | Terraform validate plan | `terraform validate` in the future approved AWS network module path | Confirm Terraform configuration syntax and internal consistency. | TODO: record sanitized output after approved execution. |
| V003 | AWS VPC creation validation plan | `aws ec2 describe-vpcs --filters Name=tag:Name,Values=<aws-vpc-name>` | Confirm planned VPC listing method using placeholders. | TODO: record sanitized output after approved execution. |
| V004 | AWS subnet creation validation plan | `aws ec2 describe-subnets --filters Name=vpc-id,Values=<aws-vpc-id>` | Confirm planned public and private subnet listing method. | TODO: record sanitized output after approved execution. |
| V005 | AWS route table validation plan | `aws ec2 describe-route-tables --filters Name=vpc-id,Values=<aws-vpc-id>` | Confirm planned route table listing method. | TODO: record sanitized output after approved execution. |
| V006 | AWS security group baseline validation plan | `aws ec2 describe-security-groups --filters Name=vpc-id,Values=<aws-vpc-id>` | Confirm planned security group baseline listing method. | TODO: record sanitized output after approved execution. |
| V007 | Terraform output capture plan | `terraform output` | Capture sanitized output names and placeholder values only. | TODO: record sanitized output after approved execution. |
| V008 | AWS CLI resource listing plan | AWS CLI describe commands for VPC, subnets, route tables, and security groups | Cross-check Terraform output against AWS resource listing. | TODO: record sanitized output after approved execution. |
| V009 | Missing VPC, subnet, route, or security group failure condition | Review missing-resource validation results. | Confirm missing required resources are marked `FAIL` or `BLOCKED`. | TODO: record decision after execution. |
| V010 | Rollback plan using terraform destroy checklist | `terraform destroy` only after future explicit approval | Confirm rollback checklist exists for approved lab execution. | TODO: record checklist result after approved execution. |

## Planned Supporting Evidence

- `configs/aws-network-plan-summary.md`
- `logs/terraform-aws-network-validation.log`
- `screenshots/aws-vpc-resource-view.png`
