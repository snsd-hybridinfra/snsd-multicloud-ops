# Architecture

## Relevant Components

- `<target-node>`: local workstation or approved control-plane host.
- Repository workspace: local clone of `snsd-multicloud-ops`.
- CLI toolchain: Git, PowerShell, Terraform CLI, Ansible, Python, kubectl, Helm, AWS CLI, Azure CLI, and OpenStack CLI.
- Evidence directory: `evidence/L1-foundation/S001-control-plane-toolchain-validation/`.

## Logical Flow

1. The operator opens a shell on `<target-node>`.
2. The operator changes to the repository root.
3. Each required tool is invoked with a version-only command.
4. Command intent and TODO output placeholders are recorded in evidence.
5. Validation status is determined from whether every tool can be checked.

## Out-of-Scope Components

Cloud accounts, Kubernetes clusters, Terraform backends, Ansible inventories, monitoring services, and ML pipelines are not accessed by this scenario.
