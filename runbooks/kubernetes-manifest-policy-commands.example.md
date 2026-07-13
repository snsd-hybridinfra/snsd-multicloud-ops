# Kubernetes Manifest Policy Commands — Examples Only

Run the repository validator with `powershell -ExecutionPolicy Bypass -File tools/validate-kubernetes-manifest-policy.ps1`.

`kubectl apply --dry-run=client -f <manifest-file-placeholder>`, `kubectl diff -f <manifest-file-placeholder>`, `kubectl get deployment <deployment-name-placeholder> -n <namespace-placeholder>`, and `kubectl describe deployment <deployment-name-placeholder> -n <namespace-placeholder>` are OPTIONAL MANUAL LAB CHECK EXAMPLES ONLY.

`conftest test <manifest-file-placeholder> --policy <policy-dir-placeholder>`, `opa eval --data <policy-file-placeholder> --input <manifest-input-placeholder> <query-placeholder>`, and `kyverno apply <policy-file-placeholder> --resource <manifest-file-placeholder>` are OPTIONAL EXAMPLES ONLY.

The validator does not require kubectl, OPA, Conftest, Gatekeeper, or Kyverno and never connects to a cluster. Production execution, real kubeconfig/endpoints/namespaces/private registries are OUT OF SCOPE.
