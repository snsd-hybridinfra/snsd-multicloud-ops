# Expected Result

## Success Conditions

- AWS, AzureRM, and OpenStack provider validation roles are clearly separated.
- Terraform fmt, init, and validate plans are defined without credentials.
- Provider version pinning strategy is documented.
- Provider separation by environment is documented.
- Hardcoded credential checks are planned.
- tfstate exclusion policy is mapped to evidence.
- Failure conditions cover missing providers, invalid provider versions, and credential exposure.

## Required Evidence

- `commands.md`
- `validation.md`
- `configs/terraform-provider-structure-summary.md`
- `logs/terraform-provider-validation.log`
- `configs/gitignore-tfstate-check.md`

## Completion Criteria

The scenario can move from `PLANNED` to `VALIDATED` only after approved, sanitized evidence confirms the Terraform provider structure checks. Real provider credentials and tfstate are not part of this scenario.
