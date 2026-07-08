# S001-control-plane-toolchain-validation

| Field | Value |
|---|---|
| Scenario ID | S001 |
| Scenario Name | Control Plane Toolchain Validation |
| Level | L1 Foundation Validation |
| Category | Foundation |
| Primary Domain | Local control plane readiness |
| Related Components | Git, PowerShell, Terraform CLI, Ansible, Python, kubectl, Helm, AWS CLI, Azure CLI, OpenStack CLI |
| Validation Type | Infrastructure Validation |
| Evidence Directory | evidence/L1-foundation/S001-control-plane-toolchain-validation/ |
| Status | PLANNED |

## Objective Summary

Validate that the local control plane has the required command-line toolchain available for later scenario work.

## Scope Summary

This scenario checks tool availability and version reporting only. It does not authenticate to cloud platforms, read credentials, create resources, or execute infrastructure changes.

## Related Components

- Local operator workstation or approved control-plane host
- Repository workspace
- Required CLI tools listed in this scenario

## Validation Summary

Each required tool must respond to a version check command and produce reviewable output that can be recorded in evidence.

## Evidence Output Summary

Evidence must be recorded in:

- `evidence/L1-foundation/S001-control-plane-toolchain-validation/commands.md`
- `evidence/L1-foundation/S001-control-plane-toolchain-validation/validation.md`
