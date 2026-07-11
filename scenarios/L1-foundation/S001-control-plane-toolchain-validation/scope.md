# Scope

## Included

- Discover Git, PowerShell, SSH, Python, Terraform, Ansible, kubectl, and Docker with `Get-Command`.
- Run local version-only commands.
- Classify core results as `PASS` or `FAIL`.
- Classify unavailable later-stage tools as `WARN`.
- Generate a sanitized text log and Markdown summary under the S001 evidence directory.

## Excluded

- Cloud resource provisioning or modification.
- Authentication to AWS, Azure, OpenStack, Kubernetes, or Docker registries.
- Provider credential validation; Terraform provider validation belongs to S006.
- Terraform initialization, planning, or application.
- Ansible inventory access or playbook execution.
- Kubernetes cluster access or kubeconfig reads; node readiness belongs to S021.
- Docker daemon, registry, or image operations.
- Prometheus or Grafana validation, which occurs in later scenarios.
- Reading credentials, environment variables, private keys, tfstate, kubeconfig, or account-specific data.

## Assumptions

- The script runs from a local PowerShell process with repository write access for evidence generation.
- Version output is safe to retain after reducing multi-line results to the first non-empty line.
- Missing later-stage tools will be installed only when their dependent scenario requires them.
