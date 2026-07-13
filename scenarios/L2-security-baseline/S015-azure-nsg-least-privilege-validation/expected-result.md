# Expected Result

## Pass Criteria

- V001 through V013 return `PASS`.
- Public inbound matrix rows are limited to ports 80 and 443 on `azure-public-web-nsg`.
- Administrative, database, monitoring, and management ports use non-public placeholders.
- Terraform retains only safe local structural placeholders; no deployment is executed.
- Generated summary records overall `PASS` and the log records the same checks.

## Evidence Criteria

The ignored log and tracked summary contain no credentials, tenant or subscription values, secrets, state, real variables, public addresses, or account-specific data.
