# Expected Result

## Success Conditions

- All required provider files and blocks exist.
- Terraform and all provider version constraints are explicit.
- AWS, AzureRM, and OpenStack provider sources match the baseline.
- No state, real tfvars, `.terraform`, backend, credential-like content, or account assignment is present.
- Safety boundaries are documented.
- The validator exits zero when all required checks pass.
- Optional formatting or runtime provider-validation limitations are recorded as warnings.

## Required Evidence

- `logs/terraform-provider-validation.log`
- `configs/terraform-provider-baseline-summary.md`
- `commands.md`
- `validation.md`

The result proves declaration safety only; it does not prove provider authentication or cloud connectivity.
