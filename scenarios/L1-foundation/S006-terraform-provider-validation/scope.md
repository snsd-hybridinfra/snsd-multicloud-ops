# Scope

## Included

- Terraform `required_version` constraint.
- AWS, AzureRM, and OpenStack entries in `required_providers`.
- Explicit source and version constraints for all three providers.
- Empty or non-authenticating provider blocks.
- Local checks for required files, unsafe Terraform artifacts, backend blocks, credential-like content, account assignments, and boundary documentation.
- Optional `terraform fmt -check` when Terraform is locally available.
- Generated local log and Markdown summary evidence.

## Excluded

- Authentication to AWS, Azure, OpenStack, or any external system.
- Real provider credential validation.
- Access keys, client credentials, tenant or subscription IDs, authentication URLs, usernames, passwords, project IDs, tokens, `clouds.yaml`, and openrc.
- Backend creation or remote backend validation.
- `terraform init`, `validate`, `plan`, `apply`, or `destroy` execution.
- Provider download, lock-file creation, `.terraform`, state, real tfvars, or account-specific values.
- AWS network validation, which belongs to S003.
- Azure network validation, which belongs to S004.
- OpenStack network validation, which belongs to S005.
- Terraform drift detection and remediation, which belong to S041 and S042.

## Assumptions

- Version ranges are compatibility baselines rather than a latest-version claim.
- Future authentication must use approved secure local configuration outside the repository.
