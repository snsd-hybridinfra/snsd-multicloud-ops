# Failure Condition

## Failure Conditions

- Terraform AWS provider initialization validation cannot be planned safely.
- Terraform validate evidence cannot be defined.
- VPC, subnet, route table, internet gateway, or security group validation criteria are missing.
- Terraform output capture would require committing tfstate or sensitive values.
- AWS CLI resource listing would expose account IDs, credentials, real public IPs, or other sensitive values.
- Rollback through `terraform destroy` is not documented for future approved execution.
- Real AWS resources, credentials, access keys, account IDs, tfstate, private keys, or account-specific files are added.

## Evidence of Failure

Record failed or blocked checks in `validation.md`, with supporting TODO references to `commands.md`, `configs/aws-network-plan-summary.md`, or `logs/terraform-aws-network-validation.log`.

## Follow-Up Requirement

Create a follow-up task to clarify the AWS network plan, sanitize evidence expectations, or define a safe future lab execution path before implementation proceeds.
