# Terraform Drift Remediation Commands — Examples Only

> SAMPLE / NON-PRODUCTION. The validator never runs these commands.

## Local Review Examples

```text
terraform fmt -check
terraform validate
git diff -- terraform/
git status --short
```

## MANUAL LAB EXECUTION ONLY

```text
terraform plan -detailed-exitcode
terraform plan -refresh-only -detailed-exitcode
terraform show -json <plan-file-placeholder>
```

`git checkout -- <terraform-file-placeholder>` is a MANUAL LOCAL ROLLBACK EXAMPLE ONLY.

## OUT OF SCOPE

The following are documentation references only and are never a normal executable S042 workflow:

```text
terraform apply <plan-file-placeholder>
terraform destroy
terraform import <resource-address-placeholder> <resource-id-placeholder>
terraform state rm <resource-address-placeholder>
terraform state mv <source-resource-address-placeholder> <destination-resource-address-placeholder>
terraform force-unlock <lock-id-placeholder>
```

The validator must not run Terraform. Production execution, real tfstate, tfvars, plan binaries, backend configuration, credentials, and cloud identifiers are OUT OF SCOPE and must not be committed.
