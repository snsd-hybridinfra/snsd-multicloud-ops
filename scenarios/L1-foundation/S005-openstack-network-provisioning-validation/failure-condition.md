# Failure Condition

## Failure Conditions

- OpenStack CLI authentication validation cannot be planned safely.
- Provider Network and Tenant Network roles are not clearly distinguished.
- Network, subnet, router, router interface, or security group validation criteria are missing.
- Terraform or OpenStack CLI output capture would require committing tfstate, `openrc`, `clouds.yaml`, credentials, or sensitive values.
- OpenStack CLI resource listing would expose real project IDs, credentials, real public IPs, private keys, or other sensitive values.
- Rollback through Terraform destroy or OpenStack CLI cleanup is not documented for future approved execution.
- Real OpenStack resources, credentials, `openrc` files, `clouds.yaml`, tfstate, private keys, or account-specific files are added.

## Evidence of Failure

Record failed or blocked checks in `validation.md`, with supporting TODO references to `commands.md`, `configs/openstack-network-plan-summary.md`, or `logs/openstack-network-validation.log`.

## Follow-Up Requirement

Create a follow-up task to clarify the OpenStack network plan, distinguish provider and tenant responsibilities, sanitize evidence expectations, or define a safe future lab execution path before implementation proceeds.
