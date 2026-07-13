# Execution Plan

## Preparation

1. Confirm no real tfvars, tfstate, `.terraform`, backend, credentials, or cloud account assignments are present.
2. Confirm the validation path is inside the repository.

## Execution Steps

1. Run `tools/validate-terraform-provider-baseline.ps1` from the repository root.
2. Review V001-V013 as required repository checks.
3. Review V014-V015 as informational Terraform readiness checks.
4. Inspect the generated log and summary.
5. Run repository structure and scenario quality validation.

## Safety Boundary

The execution reads local files and may run `terraform fmt -check` only. It does not authenticate, read credential sources or kubeconfig, initialize or download providers, or execute Terraform validation, planning, apply, or destroy operations.
