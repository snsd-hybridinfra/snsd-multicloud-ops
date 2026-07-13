# Execution Plan

## Preparation

1. Confirm the baseline and matrix are marked or described as non-production.
2. Confirm the Terraform placeholder contains no traffic rule or account value.

## Execution Steps

1. Run `tools/validate-aws-security-group-least-privilege.ps1` from the repository root.
2. Review V001-V013 in the generated summary.
3. Inspect dangerous-inbound, public-web, egress, Terraform, and safety results.
4. Run repository structure and scenario quality validation.

## Safety Boundary

Execution reads repository files only. It does not authenticate to AWS, run AWS CLI, query Security Groups, initialize Terraform, create a plan, apply changes, or contact external systems.
