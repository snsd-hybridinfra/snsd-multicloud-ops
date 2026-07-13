# Scope

## Included

- Static validation of non-production Namespace, Deployment, and ClusterIP Service examples.
- Fixed image, labels/selectors, probes, resources, and manifest safety checks.
- Parsing of sample deployment readiness/availability and Pod readiness/status/restarts.
- Optional explicit `-LiveKubectl` deployment and Pod listings.
- Credential-file, endpoint, address, secret-content, and mutation-command safety checks.

## Excluded

- Applying manifests or deleting, patching, editing, replacing, scaling, rolling out, or otherwise modifying resources.
- Implicit kubectl execution or storing kubeconfig, tokens, certificates, endpoints, raw live rows, or secrets.
- Node readiness (S021), ingress routing (S023), Nginx proxy operation (S024), RBAC (S018), and manifest policy (S044).
