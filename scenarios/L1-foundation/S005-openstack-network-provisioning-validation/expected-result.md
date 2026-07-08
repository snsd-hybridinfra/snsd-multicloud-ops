# Expected Result

## Success Conditions

- OpenStack baseline network validation is fully documented.
- Provider Network role is clearly distinguished as external, shared, or dependency-owned.
- Tenant Network role is clearly distinguished as project-owned workload networking.
- Tenant Network, Tenant Subnet, Router, Router Interface, Security Group baseline, Floating IP placeholder, and Keypair placeholder validation methods are mapped to evidence.
- Terraform or OpenStack CLI output capture is planned without exposing tfstate, `openrc`, `clouds.yaml`, credentials, or private keys.
- Rollback using future Terraform destroy or OpenStack CLI cleanup checklist is defined.

## Required Evidence

- `commands.md`
- `validation.md`
- `configs/openstack-network-plan-summary.md`
- `logs/openstack-network-validation.log`
- `screenshots/openstack-network-resource-view.png`

## Completion Criteria

The scenario can move from `PLANNED` to `VALIDATED` only after approved, sanitized evidence confirms the OpenStack baseline network validation checks. Real OpenStack execution is not part of this skeleton.
