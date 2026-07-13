# Prerequisites

## Static

- PowerShell and `tools/validate-web-pod-failure-recovery.ps1`.
- Three runbook artifacts and five sanitized samples.
- No kubectl, cluster, kubeconfig, credential, network, or fault injection.

## Optional LiveKubectl

- Explicit approval, kubectl, Namespace, and DeploymentName.
- Read-only access to a safe lab.

Destructive evidence collection is separate, manual, and restricted to a disposable non-production namespace. The validator never performs deletion.
