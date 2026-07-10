# Architecture

This scenario models a controlled security rule misconfiguration and manual rollback workflow across provider and on-prem access control layers.

## Relevant Components

- AWS Security Group placeholder: `<security-group-id>`.
- Azure NSG placeholder: `<nsg-name>`.
- OpenStack Security Group placeholder: `<openstack-security-group>`.
- On-Prem firewall rule placeholder: `<firewall-rule>`.
- Allowed CIDR placeholder: `<allowed-cidr>`.
- Unauthorized CIDR placeholder: `<unauthorized-cidr>`.
- Service port placeholder: `<service-port>`.
- Evidence store: `evidence/L4-failure-recovery/S037-security-rule-misconfiguration-validation/`.

## Detection and Recovery Flow

1. Capture the pre-change security rule baseline.
2. Plan a controlled placeholder misconfiguration.
3. Validate exposure detection for public SSH, public DB, or broad inbound CIDR patterns.
4. Validate required service access breakage if a required rule is removed or narrowed incorrectly.
5. Validate unauthorized and authorized source behavior.
6. Record manual rollback decision points.
7. Validate post-rollback rule state.
8. Validate post-rollback service reachability.
9. Measure detection and recovery timing against provisional thresholds.

This scenario does not implement real rule changes or automated security response.
