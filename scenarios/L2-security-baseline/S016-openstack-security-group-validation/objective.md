# Objective

## Objective Statement

Validate that SNSD Multi-Cloud Ops defines OpenStack Security Group rules using least-privilege principles through safe local inspection.

## Success Measures

- Required policy and matrix files exist.
- Five logical Security Group placeholders and all required policy statements are present.
- Existing Terraform Security Group and management-scoped rule placeholders are recognized without deployment.
- Public ingress is limited to HTTP/HTTPS on the public web tier.
- Administrative, database, and monitoring ports are not public.
- No credentials, OpenStack configuration files, identity values, state, real variables, secrets, or real public addresses are present.
