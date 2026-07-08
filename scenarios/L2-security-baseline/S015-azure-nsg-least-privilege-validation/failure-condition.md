# Failure Condition

S015 fails if the Azure NSG model allows unsafe or undocumented access patterns.

## Failure Conditions

- Azure NSG target cannot be identified by placeholder name or ID.
- SSH inbound allows `Any`, `Internet`, `0.0.0.0/0`, or another unrestricted source.
- DB port `3306` is exposed to the public internet.
- Bastion-to-Azure SSH rule is missing when SSH administration is required.
- Required HTTP or HTTPS service rule is missing or undocumented.
- Azure App-to-On-Prem DB access is missing, overly broad, or not mapped to `<onprem-db-cidr>`.
- Monitoring scrape access is missing, overly broad, or not mapped to `<monitoring-cidr>`.
- Any all-protocol or all-ports inbound rule is accepted without an explicit failure.
- Rule evidence cannot be captured or reviewed.
- Evidence contains Azure credentials, subscription IDs, tenant IDs, private keys, tfstate, real public IPs, or account-specific values.

## Blocked Conditions

- Validation cannot proceed because no approved placeholder rule model exists.
- Future read-only Azure CLI or Terraform plan output is unavailable.
- Required evidence files are missing.
