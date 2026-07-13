# Objective

## Objective Statement

Validate that every evaluated Kubernetes node reports `Ready` and no node reports `NotReady`, while preserving cluster credential and endpoint safety.

## Success Measures

- Readiness policy and five safe command references are documented.
- Three non-production placeholder nodes are present and report Ready.
- NotReady fails validation; SchedulingDisabled produces a visible warning.
- Static mode never invokes kubectl.
- Optional live mode invokes only `get nodes --no-headers` and stores no raw cluster details.
- No kubeconfig, token, certificate, private key, endpoint, numeric address, or secret is present.
