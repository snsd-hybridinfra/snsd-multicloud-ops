# Failure Condition

S016 fails if the OpenStack Security Group model allows unsafe or undocumented access patterns.

## Failure Conditions

- OpenStack Security Group target cannot be identified by placeholder name or ID.
- SSH ingress allows `0.0.0.0/0` or another unrestricted source.
- DB port `3306` is exposed to public internet, provider network, or unrestricted sources.
- Bastion-to-OpenStack SSH rule is missing when SSH administration is required.
- Required HTTP or HTTPS service rule is missing or undocumented.
- OpenStack App-to-On-Prem DB access is missing, overly broad, or not mapped to `<onprem-db-cidr>`.
- Monitoring scrape access is missing, overly broad, or not mapped to `<monitoring-cidr>`.
- Any all-protocol or all-ports ingress rule is accepted without an explicit failure.
- Rule evidence cannot be captured or reviewed.
- Evidence contains OpenStack credentials, openrc content, clouds.yaml content, private keys, tfstate, real public IPs, or account-specific values.

## Blocked Conditions

- Validation cannot proceed because no approved placeholder rule model exists.
- Future read-only OpenStack CLI or Terraform plan output is unavailable.
- Required evidence files are missing.
