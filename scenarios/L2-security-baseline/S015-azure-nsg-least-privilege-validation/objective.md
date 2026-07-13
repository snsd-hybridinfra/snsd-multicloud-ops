# Objective

## Objective Statement

Validate that SNSD Multi-Cloud Ops defines Azure Network Security Group rules using least-privilege principles through safe local inspection.

## Success Measures

- Required policy and matrix files exist.
- Five logical NSG placeholders and all required policy statements are present.
- Existing Terraform NSG and association placeholders are recognized without deploying rules.
- Public inbound exposure is limited to HTTP/HTTPS on the public web tier.
- Dangerous administrative, database, and monitoring ports are not public.
- No credentials, identity values, state, real variables, secrets, or real public addresses are present.
