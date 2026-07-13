# Expected Result

## Success Conditions

- Both baseline files, all placeholder groups, and required policy statements exist.
- The AWS Terraform module contains a safe Security Group placeholder.
- No dangerous public inbound row exists.
- Only public web HTTP/HTTPS rows use public inbound exposure.
- Egress is justified and marked for review.
- No state, real variables, backend, credential, account value, secret, or real public IP exists.
- The validator exits zero and generates evidence.

## Required Evidence

- `logs/aws-security-group-least-privilege-validation.log`
- `configs/aws-security-group-least-privilege-summary.md`
- `commands.md`
- `validation.md`

The result proves repository policy and placeholder safety only; it does not prove live AWS Security Group state.
