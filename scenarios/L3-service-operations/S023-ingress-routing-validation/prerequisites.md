# Prerequisites

## Static Mode

- PowerShell and the routing baseline, command reference, Ingress/Service examples, and three sample evidence files.
- Writable S023 evidence directories.

## Optional LiveKubectl Mode

- Explicit `-LiveKubectl`, approved external context, and existing resources in `snsd-example`.
- No kubeconfig path, token, certificate, TLS key, endpoint, address, or credential copied to the repository.

## Safety Preconditions

Live mode is read-only and never runs curl or modifies resources.
