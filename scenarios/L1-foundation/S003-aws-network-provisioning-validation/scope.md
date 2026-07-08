# Scope

## Included

- Terraform AWS provider initialization plan.
- Terraform validate plan.
- AWS VPC creation validation plan.
- AWS public and private subnet creation validation plan.
- AWS route table validation plan.
- AWS internet gateway validation plan.
- AWS security group baseline validation plan.
- Optional bastion entry point placeholder validation.
- Terraform output capture plan.
- AWS CLI resource listing plan.
- Failure condition for missing VPC, subnet, route, or security group.
- Rollback plan using a `terraform destroy` checklist.

## Excluded

- Real AWS Terraform resource implementation.
- Terraform provider credentials or backend configuration.
- AWS credentials, access keys, account IDs, private keys, tfstate files, or account-specific files.
- Real AWS resource creation, modification, or deletion.
- Terraform plan, apply, or destroy execution against a real account.
- Ansible, Kubernetes, monitoring, ML, backup, or other unrelated logic.

## Assumptions

- AWS identifiers are represented only with placeholders such as `<aws-vpc-id>` and `<aws-public-subnet-id>`.
- Any future AWS CLI output must be sanitized before commit.
- This scenario remains in planning status until an approved lab execution path exists.
