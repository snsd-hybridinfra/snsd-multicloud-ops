# Failure Condition

S014 fails if the AWS Security Group model allows unsafe or undocumented access patterns.

## Failure Conditions

- AWS Security Group target cannot be identified by placeholder name or ID.
- SSH ingress allows `0.0.0.0/0` or another unrestricted source.
- DB port `3306` is exposed to the public internet.
- Bastion-to-AWS SSH rule is missing when SSH administration is required.
- Required HTTP or HTTPS service rule is missing or undocumented.
- App-to-On-Prem DB access is missing, overly broad, or not mapped to `<onprem-db-cidr>`.
- Monitoring scrape access is missing, overly broad, or not mapped to `<monitoring-cidr>`.
- Any all-protocol or all-ports ingress rule is accepted without an explicit failure.
- Rule evidence cannot be captured or reviewed.
- Evidence contains AWS credentials, account IDs, access keys, private keys, tfstate, real public IPs, or account-specific values.

## Blocked Conditions

- Validation cannot proceed because no approved placeholder rule model exists.
- Future read-only AWS CLI or Terraform plan output is unavailable.
- Required evidence files are missing.
