# Policy as Code Validation

> SAMPLE / NON-PRODUCTION — repository-native static evidence only.

S043 validates a governance rule model, schema, evaluation input, violation, exception, and final judgment. A rule uses `<policy-id-placeholder>`, `<policy-rule-placeholder>`, `<policy-domain-placeholder>`, `<resource-type-placeholder>`, `<resource-address-placeholder>`, `<expected-value-placeholder>`, and `<observed-value-placeholder>`. Violations and exceptions use `<violation-id-placeholder>`, `<exception-id-placeholder>`, `<approval-id-placeholder>`, and `<evidence-path>`.

The schema defines conditions, severity, evidence, exception fields, scenario mappings, and judgment values. Exceptions require owner, reason, expiry, approval, rollback condition, and evidence. S041/S042 own Terraform drift, security baselines own provider controls, and S044 owns Kubernetes manifest policy details.

Static validation reads sanitized repository artifacts. It does not execute an external policy engine.

## Out of Scope

Live cloud enforcement/checks, Terraform execution, Kubernetes admission control, OPA Gatekeeper/Kyverno deployment, required Conftest runtime, cloud API calls, automatic blocking, SOAR, production attestation, and automated production exception approval are OUT OF SCOPE.
