# Execution Plan

## Preparation

1. Open PowerShell on `<target-node>`.
2. Change to the repository root.
3. Confirm the S001 evidence directory exists.
4. Confirm no credential files, kubeconfig files, private keys, or tfstate files are required.

## Execution Steps

1. Run the Git version check.
2. Run the PowerShell version check.
3. Run the Terraform CLI version check.
4. Run the Ansible version check.
5. Run the Python version check.
6. Run the kubectl version check.
7. Run the Helm version check.
8. Run the AWS CLI version check.
9. Run the Azure CLI version check.
10. Run the OpenStack CLI version check.

## Evidence Capture

1. Record each command and its purpose in `commands.md`.
2. Paste sanitized command output into the matching TODO section after execution.
3. Record pass, fail, partial, blocked, or not-run status in `validation.md`.
4. Do not capture secrets, credentials, account identifiers, kubeconfig content, tfstate, or private keys.
