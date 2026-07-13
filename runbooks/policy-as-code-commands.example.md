# Policy as Code Commands — Examples Only

```text
powershell -ExecutionPolicy Bypass -File tools/validate-policy-as-code.ps1
git diff -- policy/
git diff -- terraform/
git diff -- security-baseline/
```

`terraform show -json <plan-file-placeholder>` is MANUAL LAB EVIDENCE CONVERSION ONLY.

The following are OPTIONAL EXAMPLES ONLY; OPA and Conftest are not required by this repository validator:

```text
conftest test <input-file-placeholder> --policy <policy-dir-placeholder>
opa eval --data <policy-file-placeholder> --input <input-file-placeholder> <query-placeholder>
```

Live cloud checks and enforcement are OUT OF SCOPE. Real state, tfvars, plan binaries, backend configuration, credentials, identifiers, and production resource names must not be committed.
