# Scope

## Included

- Pre-change security rule baseline validation plan.
- Intentional misconfiguration injection plan using placeholders.
- Public SSH exposure detection validation plan.
- Public DB exposure detection validation plan.
- Overly broad inbound CIDR detection validation plan.
- Required service access breakage detection validation plan.
- Unauthorized source access test validation plan.
- Authorized source access test validation plan.
- Manual rollback decision point validation plan.
- Post-rollback security rule validation plan.
- Post-rollback service reachability validation plan.
- Evidence collection for before, misconfigured, and after states.

## Target Security Control Areas

- AWS Security Group placeholder.
- Azure NSG placeholder.
- OpenStack Security Group placeholder.
- On-Prem firewall rule placeholder.
- Bastion access rule placeholder.
- Web/API service access rule placeholder.
- DB access rule placeholder.
- Monitoring access rule placeholder.

## Misconfiguration Examples

- Public SSH exposure placeholder.
- Public DB port exposure placeholder.
- Overly broad inbound CIDR placeholder.
- Missing HTTP/HTTPS service rule placeholder.
- Incorrect Bastion-only access rule placeholder.
- Incorrect monitoring access boundary placeholder.
- Incorrect inter-zone service rule placeholder.

## Important Boundary

- Do not claim real-time automated blocking.
- Do not claim WAF, IDS/IPS, EDR, or SOAR response.
- Do not claim production-grade cloud security posture management.
- This scenario validates misconfiguration through controlled detection, manual rollback, and evidence capture only.

## Detection and Recovery Threshold Model

- DETECTED: misconfiguration identified within `< 60 seconds`.
- WARNING: rollback completed within `60-300 seconds`.
- CRITICAL: unauthorized exposure remains or rollback exceeds `300 seconds`.

These are provisional validation thresholds and must be replaced only when an approved operational threshold is documented.

## Excluded

- Real cloud firewall, AWS Security Group, Azure NSG, OpenStack Security Group, or On-Prem firewall rule changes.
- Real-time automated blocking, WAF, IDS/IPS, EDR, SOAR, or CSPM capability.
- Real public IPs, real cloud account IDs, credentials, secrets, private keys, tfstate, kubeconfig, subscription IDs, tenant IDs, or account-specific values.
- AWS Security Group least privilege validation, which is handled in S014.
- Azure NSG least privilege validation, which is handled in S015.
- OpenStack Security Group validation, which is handled in S016.
- MariaDB access control validation, which is handled in S017.
- Terraform drift detection, which is handled in S041.
- Policy as Code validation, which is handled in S043.
- Changes outside this scenario directory, its matching evidence directory, and the required tracking documents.
