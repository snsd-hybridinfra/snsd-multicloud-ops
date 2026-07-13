# Commands

Run `powershell -ExecutionPolicy Bypass -File tools/validate-kubernetes-manifest-policy.ps1`; inspect `logs/kubernetes-manifest-policy-validation.log` and `configs/kubernetes-manifest-policy-validation-summary.md`.

Manual disposable-lab evidence must be sanitized. The validator does not run kubectl, OPA, Conftest, Kyverno, cloud CLIs, or live checks. Optional examples are not runtime requirements. Do not commit kubeconfig, tokens, certificates, private registry values, real endpoints, or secrets. Live execution: `NOT_RUN`.
