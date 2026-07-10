# Execution Plan

1. Confirm that manifest policy validation is static review only.
2. Identify `<namespace>`, `<manifest-file>`, `<deployment-name>`, `<service-name>`, `<ingress-name>`, `<container-image>`, and `<policy-result>`.
3. Review whether namespace is explicitly defined.
4. Review whether image tag is not `latest`.
5. Review whether resource requests are defined.
6. Review whether resource limits are defined.
7. Review whether privileged container mode is prohibited.
8. Review whether `hostNetwork`, `hostPID`, and `hostIPC` are restricted or justified.
9. Review whether HostPath volume usage is absent or justified.
10. Review whether secret values are not embedded directly in manifests.
11. Review whether ConfigMap and Secret references are documented as placeholders.
12. Review whether Ingress host and path mapping is documented.
13. Reference RBAC dependency without revalidating RBAC controls.
14. Classify each result as `MANIFEST_PASS`, `MANIFEST_FAIL`, `MANIFEST_WARNING`, `MANIFEST_NOT_APPLICABLE`, or `MANIFEST_INCONCLUSIVE`.
15. Capture TODO evidence references in `commands.md`, `validation.md`, `configs/`, `logs/`, and `screenshots/`.

No manifest deployment, kubeconfig access, or admission controller enforcement occurs in this skeleton.
