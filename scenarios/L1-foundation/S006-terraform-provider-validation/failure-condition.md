# Failure Condition

## Failure Conditions

- AWS, AzureRM, and OpenStack provider roles are not clearly separated.
- Provider version constraints are missing, invalid, or inconsistent with the repository strategy.
- Terraform fmt, init, or validate checks cannot be planned safely.
- Provider blocks include hardcoded credentials, keys, tokens, account IDs, subscription IDs, tenant IDs, passwords, or endpoints tied to a real account.
- Terraform state files, `.terraform/` directories, backend state files, or account-specific files are created or committed.
- Evidence requires real credentials, private keys, tfstate, or account-specific values.

## Evidence of Failure

Record failed or blocked checks in `validation.md`, with supporting TODO references to `commands.md`, `configs/terraform-provider-structure-summary.md`, `logs/terraform-provider-validation.log`, or `configs/gitignore-tfstate-check.md`.

## Follow-Up Requirement

Create a follow-up task to correct provider separation, version pinning, credential handling, or tfstate policy before Terraform implementation proceeds.
