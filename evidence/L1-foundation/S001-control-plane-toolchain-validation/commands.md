# Commands

Scenario: S001-control-plane-toolchain-validation
Level: L1-foundation
Capability: Control Plane Toolchain Validation
Target: `<target-node>`
Execution timestamp: TODO

Record sanitized output only. Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

| Check ID | Tool | Command | Purpose | Output |
|---|---|---|---|---|
| V001 | Git | `git --version` | Confirm Git CLI is installed and reports version information. | TODO: paste sanitized output after execution. |
| V002 | PowerShell | `$PSVersionTable.PSVersion` | Confirm PowerShell reports version information. | TODO: paste sanitized output after execution. |
| V003 | Terraform CLI | `terraform version` | Confirm Terraform CLI is installed and reports version information. | TODO: paste sanitized output after execution. |
| V004 | Ansible | `ansible --version` | Confirm Ansible is installed and reports version information. | TODO: paste sanitized output after execution. |
| V005 | Python | `python --version` | Confirm Python is installed and reports version information. | TODO: paste sanitized output after execution. |
| V006 | kubectl | `kubectl version --client` | Confirm kubectl client is installed and reports version information. | TODO: paste sanitized output after execution. |
| V007 | Helm | `helm version` | Confirm Helm is installed and reports version information. | TODO: paste sanitized output after execution. |
| V008 | AWS CLI | `aws --version` | Confirm AWS CLI is installed and reports version information without login. | TODO: paste sanitized output after execution. |
| V009 | Azure CLI | `az version` | Confirm Azure CLI is installed and reports version information without login. | TODO: paste sanitized output after execution. |
| V010 | OpenStack CLI | `openstack --version` | Confirm OpenStack CLI is installed and reports version information without login. | TODO: paste sanitized output after execution. |
