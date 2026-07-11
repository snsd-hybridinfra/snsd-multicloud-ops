# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Git core readiness | `Get-Command git`; `git --version` | Command exists and returns version output. | `logs/control-plane-toolchain-validation.log`, `configs/control-plane-toolchain-summary.md` |
| V002 | PowerShell core readiness | `Get-Command powershell`; local version command | Command exists and returns version output. | `logs/control-plane-toolchain-validation.log`, `configs/control-plane-toolchain-summary.md` |
| V003 | SSH core readiness | `Get-Command ssh`; `ssh -V` | Command exists and returns version output. | `logs/control-plane-toolchain-validation.log`, `configs/control-plane-toolchain-summary.md` |
| V004 | Python core readiness | `Get-Command python`; `python --version` | Command exists and returns version output. | `logs/control-plane-toolchain-validation.log`, `configs/control-plane-toolchain-summary.md` |
| V005 | Terraform later-stage readiness | `Get-Command terraform`; `terraform version` | Availability and version are recorded; absence is a warning. | `logs/control-plane-toolchain-validation.log`, `configs/control-plane-toolchain-summary.md` |
| V006 | Ansible later-stage readiness | `Get-Command ansible`; `ansible --version` | Availability and version are recorded; absence is a warning. | `logs/control-plane-toolchain-validation.log`, `configs/control-plane-toolchain-summary.md` |
| V007 | kubectl later-stage readiness | `Get-Command kubectl`; `kubectl version --client` | Client availability and version are recorded without cluster access; absence is a warning. | `logs/control-plane-toolchain-validation.log`, `configs/control-plane-toolchain-summary.md` |
| V008 | Docker later-stage readiness | `Get-Command docker`; `docker --version` | CLI availability and version are recorded without daemon or registry access; absence is a warning. | `logs/control-plane-toolchain-validation.log`, `configs/control-plane-toolchain-summary.md` |

## Review Notes

- V001-V004 are core checks and determine the script exit code.
- V005-V008 are later-stage readiness checks and may produce warnings.
- Every validation item maps to generated evidence by check ID.
