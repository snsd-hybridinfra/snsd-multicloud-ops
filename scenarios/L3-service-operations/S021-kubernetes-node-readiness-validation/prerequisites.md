# Prerequisites

## Static Mode

- PowerShell capable of running repository validators.
- Readiness policy, command reference, and tracked non-production sample evidence.
- Writable S021 evidence directories.

## Optional LiveKubectl Mode

- The operator explicitly supplies `-LiveKubectl`.
- `kubectl` is available and its external access context is approved outside the repository.
- No kubeconfig path, token, certificate, endpoint, or credential is copied into repository files.

## Safety Preconditions

Live mode remains read-only and may not apply, delete, patch, cordon, drain, taint, or edit resources.
