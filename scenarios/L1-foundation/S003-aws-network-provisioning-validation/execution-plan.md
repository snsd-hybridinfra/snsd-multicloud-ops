# Execution Plan

## Preparation

1. Review S001 for Terraform CLI and AWS CLI readiness.
2. Confirm this scenario is documentation and evidence planning only.
3. Confirm no AWS credentials, account IDs, access keys, tfstate, private keys, or account-specific files are present or required.
4. Confirm the S003 evidence directory exists.

## Execution Steps

1. Define the Terraform AWS provider initialization validation plan.
2. Define the Terraform validate command plan.
3. Define the AWS VPC creation validation plan.
4. Define the AWS public and private subnet validation plan.
5. Define the AWS route table validation plan.
6. Define the AWS security group baseline validation plan.
7. Define the Terraform output capture plan.
8. Define the AWS CLI resource listing plan.
9. Define failure conditions for missing VPC, subnet, route, or security group.
10. Define the rollback checklist using `terraform destroy` for future approved execution.

## Evidence Capture

1. Record planned commands and placeholders in `commands.md`.
2. Record validation checks and TODO results in `validation.md`.
3. Map future plan evidence to `configs/aws-network-plan-summary.md`.
4. Map future Terraform and AWS CLI logs to `logs/terraform-aws-network-validation.log`.
5. Map future console evidence to `screenshots/aws-vpc-resource-view.png` only after binary evidence is approved and sanitized.
