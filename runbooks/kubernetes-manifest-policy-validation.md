# Kubernetes Manifest Policy Validation

> SAMPLE / NON-PRODUCTION — static manifest evidence only.

S044 validates workload security context, image, requests/limits, probes, service exposure, namespace/labels/annotations, secret handling, violations, exceptions, and final judgments for `<namespace-placeholder>`, `<deployment-name-placeholder>`, `<container-name-placeholder>`, and `<image-placeholder>`. Exceptions use `<policy-id-placeholder>`, `<violation-id-placeholder>`, `<exception-id-placeholder>`, `<approval-id-placeholder>`, and `<evidence-path>`.

Containers should be non-root, non-privileged, deny privilege escalation, use a read-only root filesystem where applicable, declare resources and probes, avoid `latest`, and avoid host namespaces/hostPath. Services require approval for NodePort/LoadBalancer. Secrets must not be embedded. RBAC detail belongs to S018 and general policy governance to S043.

Static evidence validation is not live admission control. Live apply, cluster admission, Gatekeeper/Kyverno, Pod Security Admission, service mesh/Istio, Argo CD/GitOps enforcement, production enforcement, and automatic remediation are OUT OF SCOPE.
