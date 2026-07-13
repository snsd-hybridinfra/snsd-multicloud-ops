# Execution Plan

## Preparation

1. Confirm no real tfvars, tfstate, backend, credentials, or Azure identity assignments are present.
2. Confirm the validation paths are inside the repository.

## Execution Steps

1. Run `tools/validate-azure-network-provisioning.ps1` from the repository root.
2. Review V001-V009 as required repository checks.
3. Review V010-V011 as informational Terraform readiness checks.
4. Inspect the generated log and summary.
5. Run repository structure and scenario quality validation.

## Safety Boundary

The execution reads local files and may run `terraform fmt -check` only. It does not run Azure CLI, authenticate, read environment credentials or kubeconfig, initialize providers, or execute Terraform validation, planning, apply, or destroy operations.
