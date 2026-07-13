# Terraform Drift Detection Commands — Examples Only

> SAMPLE / NON-PRODUCTION. No command below is executed by the S041 validator.

## Local Syntax Checks

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

These commands require a disposable lab review. The validation script must not run Terraform against a real cloud environment. Production execution is OUT OF SCOPE.

## OUT OF SCOPE

`terraform apply`, `terraform destroy`, `terraform import`, `terraform state rm`, `terraform state mv`, and `terraform force-unlock` are OUT OF SCOPE and must never be presented as the S041 workflow.

Real tfstate, tfvars, backend configuration, plan binaries, provider credentials, cloud identifiers, and production resource names must not be committed.
