# Execution Plan

1. Confirm the scenario evidence directory exists for S022.
2. Identify placeholder namespace as `<namespace>`.
3. Identify placeholder Deployments as `<web-deployment>` and `<api-deployment>`.
4. Identify placeholder Services as `<web-service>` and `<api-service>`.
5. Record the planned namespace existence check.
6. Record planned Deployment existence checks for web and API workloads.
7. Record planned rollout status, replica availability, pod Running, and pod Ready checks.
8. Record planned Service object checks.
9. Record planned ConfigMap reference and Secret template reference checks.
10. Record planned resource requests and limits checks.
11. Record planned image tag review to confirm `<container-image>` does not use `latest`.
12. Record TODO placeholders in evidence files until approved execution produces sanitized output.

## Execution Boundaries

This plan does not create Kubernetes manifests, write kubeconfig files, create Secrets, pull private images, deploy workloads, or alter cluster state. It only defines the review flow and evidence requirements for later approved validation.
