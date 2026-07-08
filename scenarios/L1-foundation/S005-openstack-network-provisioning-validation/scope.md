# Scope

## Included

- OpenStack CLI authentication validation plan.
- OpenStack network list validation plan.
- Provider Network existence validation plan.
- Tenant Network creation validation plan.
- Tenant Subnet creation validation plan.
- Router creation validation plan.
- Router Interface validation plan.
- Security Group baseline validation plan.
- Floating IP availability validation plan.
- Keypair placeholder validation plan.
- Terraform or OpenStack CLI output capture plan.
- Failure condition for missing network, subnet, router, interface, or security group.
- Rollback plan using Terraform destroy or OpenStack CLI cleanup checklist.

## Excluded

- Real OpenStack Terraform resource implementation.
- OpenStack credentials, `openrc` files, `clouds.yaml`, private keys, tfstate files, or account-specific files.
- Real OpenStack resource creation, modification, or deletion.
- Terraform plan, apply, or destroy execution against a real OpenStack environment.
- OpenStack CLI execution against a real environment.
- Ansible, Kubernetes, monitoring, ML, backup, or other unrelated logic.

## Assumptions

- OpenStack identifiers are represented only with placeholders such as `<openstack-provider-network-name>` and `<openstack-tenant-network-name>`.
- Provider Network means a pre-existing external or shared network boundary and is not owned by this scenario.
- Tenant Network means the project-owned workload network planned for future validation.
- Any future OpenStack CLI output must be sanitized before commit.
