# Failure Condition

## Failure Conditions

- Git, PowerShell, SSH, or Python is not discoverable.
- A core version command exits non-zero or returns no version output.
- The log or summary cannot be generated.
- A check attempts cloud authentication, cluster access, registry access, credential reads, kubeconfig reads, tfstate access, or infrastructure changes.
- Generated evidence exposes sensitive or account-specific data.

Later-stage tool warnings do not fail S001 core readiness.

## Evidence of Failure

The console, log, summary, and `validation.md` identify the failed core check without including unsafe local details.

## Follow-Up Requirement

Install or repair the failed core tool, rerun S001, and replace the generated evidence before dependent implementation proceeds.
