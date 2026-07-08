# Expected Result

## Success Conditions

- AWS baseline network validation is fully documented.
- Terraform initialization and validate plans are defined without credentials or backend state.
- VPC, subnet, route table, internet gateway, and security group validation methods are mapped to evidence.
- Terraform output capture is planned without exposing tfstate content.
- AWS CLI resource listing is planned with sanitized placeholders only.
- Rollback using a future `terraform destroy` checklist is defined.

## Required Evidence

- `commands.md`
- `validation.md`
- `configs/aws-network-plan-summary.md`
- `logs/terraform-aws-network-validation.log`
- `screenshots/aws-vpc-resource-view.png`

## Completion Criteria

The scenario can move from `PLANNED` to `VALIDATED` only after approved, sanitized evidence confirms the AWS baseline network validation checks. Real AWS execution is not part of this skeleton.
