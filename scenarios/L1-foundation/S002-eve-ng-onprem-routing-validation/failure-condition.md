# Failure Condition

## Failure Conditions

- EVE-NG topology evidence cannot be located or summarized.
- Router configuration snapshots are missing or not sanitized.
- Management, Bastion, Internal Server, or Monitoring Zone gateway reachability cannot be validated.
- Transit Zone routes are missing where expected.
- Default route existence cannot be confirmed where applicable.
- Inter-zone ping test paths are undefined or fail without a documented boundary reason.
- Firewall implementation is attempted in this scenario.
- Evidence includes real credentials, private keys, tfstate, kubeconfig content, account-specific values, or unsanitized network identifiers.

## Evidence of Failure

Record failed or blocked checks in `validation.md`, with supporting TODO references to `logs/routing-validation.log`, `configs/router-config-snapshot.md`, or `configs/topology-summary.md`.

## Follow-Up Requirement

Create a follow-up task for topology correction, route correction, gateway clarification, or firewall-policy analysis. Do not remediate firewall rules in S002.
