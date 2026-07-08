# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Git version check | Run `git --version` | Git returns version information. | `commands.md`, `validation.md` |
| V002 | PowerShell version check | Run `$PSVersionTable.PSVersion` | PowerShell returns version information. | `commands.md`, `validation.md` |
| V003 | Terraform version check | Run `terraform version` | Terraform CLI returns version information. | `commands.md`, `validation.md` |
| V004 | Ansible version check | Run `ansible --version` | Ansible returns version information. | `commands.md`, `validation.md` |
| V005 | Python version check | Run `python --version` | Python returns version information. | `commands.md`, `validation.md` |
| V006 | kubectl version check | Run `kubectl version --client` | kubectl client returns version information. | `commands.md`, `validation.md` |
| V007 | Helm version check | Run `helm version` | Helm returns version information. | `commands.md`, `validation.md` |
| V008 | AWS CLI version check | Run `aws --version` | AWS CLI returns version information without requiring login. | `commands.md`, `validation.md` |
| V009 | Azure CLI version check | Run `az version` | Azure CLI returns version information without requiring login. | `commands.md`, `validation.md` |
| V010 | OpenStack CLI version check | Run `openstack --version` | OpenStack CLI returns version information without requiring login. | `commands.md`, `validation.md` |

## Review Notes

All checks must map to evidence. A missing tool should be recorded as `FAIL` if the command runs and reports absence, or `BLOCKED` if local execution cannot proceed.
