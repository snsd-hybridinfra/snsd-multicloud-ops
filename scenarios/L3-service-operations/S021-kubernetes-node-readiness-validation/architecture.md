# Architecture

## Validation Flow

```text
Static default
  -> readiness policy + command reference + sample rows
  -> parser -> Ready/NotReady/SchedulingDisabled counts

Explicit -LiveKubectl
  -> kubectl get nodes --no-headers
  -> parser -> status counts only

Both modes -> safety checks -> sanitized log and summary
```

## Judgment Model

- PASS: all parsed nodes include Ready and none include NotReady.
- WARN: SchedulingDisabled is present and maintenance must be confirmed.
- FAIL: required evidence is absent, parsing is empty, or any node is non-ready.

## Trust Boundary

Static mode is repository-local. Live mode is opt-in and read-only; kubeconfig details, endpoints, raw node rows, and credentials are never written to evidence.
