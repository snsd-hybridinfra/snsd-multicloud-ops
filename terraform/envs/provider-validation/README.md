# Terraform Provider Validation Environment

This directory declares the AWS, AzureRM, and OpenStack provider baselines for static repository review in S006.

## Safety Boundary

- Credentials must be supplied through secure local environment configuration outside the repository when real implementation begins.
- Provider authentication validation is not performed in S006.
- Remote backend validation is out of scope for S006.
- Real `terraform init`, `validate`, `plan`, and `apply` execution is out of scope for S006.
- No account identifiers, authentication URLs, usernames, passwords, tokens, state, real tfvars, or `.terraform` content belongs here.

The version ranges are compatibility baselines, not claims that the newest provider release has been selected.
