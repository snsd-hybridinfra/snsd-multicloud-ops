# Prerequisites

## Static Mode

- PowerShell and the repository baseline, command reference, manifests, and sample evidence.
- Writable S022 evidence directories.

## Optional LiveKubectl Mode

- Explicit `-LiveKubectl` invocation.
- Approved external kubectl context and an existing workload in `snsd-example`.
- No kubeconfig path, token, certificate, endpoint, or credential copied into repository files.

## Safety Preconditions

Live mode performs two read-only `get` operations only and may not mutate resources.
