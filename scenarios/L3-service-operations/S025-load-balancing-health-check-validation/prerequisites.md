# Prerequisites

## Required Previous Scenarios

- S021-kubernetes-node-readiness-validation: defines node readiness assumptions.
- S022-kubernetes-workload-deployment-validation: defines workload and Service assumptions.
- S023-ingress-routing-validation: defines routing assumptions.
- S024-nginx-reverse-proxy-validation: defines reverse proxy forwarding assumptions.

## Required Tools or References

- `kubectl` command planning capability, when future execution is approved.
- HTTP response capture capability, when future execution is approved.
- Nginx log review capability, when future execution is approved.
- Evidence model from `docs/evidence-model.md`.
- Placeholder naming rules from `docs/naming-rules.md`.

## Safety Preconditions

- Do not add TLS private keys, certificates, credentials, secrets, private keys, tfstate, kubeconfig content, cloud account values, subscription IDs, tenant IDs, or account-specific values.
- Do not record real public IPs.
- Do not implement load balancer, Kubernetes, Nginx, Blackbox Exporter, or cloud configuration as part of this scenario skeleton.
