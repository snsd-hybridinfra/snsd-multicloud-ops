# Failure Condition

## Failure Conditions

- SSH private key permission expectations are undefined.
- SSH public key placement validation is undefined.
- Control Plane to Bastion key authentication path is undefined.
- Bastion to on-prem or cloud target key authentication path is undefined.
- ProxyJump command pattern includes real users, hosts, private keys, credentials, or public IPs.
- A real private key, credential, tfstate file, kubeconfig file, cloud account value, subscription ID, tenant ID, or account-specific value is added.
- Password login denial or root login denial is implemented in this scenario.

## Evidence of Failure

Record failed or blocked checks in `validation.md`, with supporting TODO references to `configs/ssh-key-authentication-plan.md`, `configs/ssh-proxyjump-pattern-summary.md`, or `logs/ssh-key-authentication-validation.log`.

## Follow-Up Requirement

Create a follow-up task to correct SSH key path planning, public key placement documentation, ProxyJump syntax, or target reachability assumptions before future execution proceeds.
