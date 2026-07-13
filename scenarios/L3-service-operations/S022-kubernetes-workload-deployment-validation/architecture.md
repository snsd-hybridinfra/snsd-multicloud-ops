# Architecture

## Validation Flow

```text
Static default
  -> baseline + commands + Namespace/Deployment/Service
  -> deployment and pod sample parsers

Explicit -LiveKubectl
  -> kubectl get deployments -n snsd-example
  -> kubectl get pods -n snsd-example
  -> aggregate readiness/status/restart counts

Both modes -> manifest and secret safety -> sanitized evidence
```

## Workload Model

Two replicas use matching `app` labels, readiness/liveness probes, resource requests/limits, and a ClusterIP Service. Unsafe host and secret patterns are denied.

## Trust Boundary

Static mode is repository-local. Live mode is opt-in and read-only; raw workload names, endpoints, kubeconfig details, and credentials are not written to evidence.
