# Execution Plan

## Preparation

1. Review S001 for Terraform CLI and OpenStack CLI readiness.
2. Confirm this scenario is documentation and evidence planning only.
3. Confirm no OpenStack credentials, `openrc` files, `clouds.yaml`, tfstate, private keys, or account-specific files are present or required.
4. Confirm the S005 evidence directory exists.
5. Confirm the provider network role and tenant network role are documented separately.

## Execution Steps

1. Define the OpenStack CLI authentication validation plan.
2. Define the OpenStack network list validation plan.
3. Define the Provider Network existence validation plan.
4. Define the Tenant Network validation plan.
5. Define the Tenant Subnet validation plan.
6. Define the Router validation plan.
7. Define the Router Interface validation plan.
8. Define the Security Group baseline validation plan.
9. Define the Floating IP availability validation plan.
10. Define the Terraform or OpenStack CLI output capture plan.
11. Define failure conditions for missing network, subnet, router, interface, or security group.
12. Define rollback using Terraform destroy or OpenStack CLI cleanup checklist for future approved execution.

## Evidence Capture

1. Record planned commands and placeholders in `commands.md`.
2. Record validation checks and TODO results in `validation.md`.
3. Map future plan evidence to `configs/openstack-network-plan-summary.md`.
4. Map future Terraform or OpenStack CLI logs to `logs/openstack-network-validation.log`.
5. Map future console evidence to `screenshots/openstack-network-resource-view.png` only after binary evidence is approved and sanitized.
