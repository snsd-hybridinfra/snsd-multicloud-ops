# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | SSH private key permission validation plan | Document planned permission check for `<ssh-private-key-path>`. | Private key permission expectations are defined without storing the key. | `commands.md`, `configs/ssh-key-authentication-plan.md`, `validation.md` |
| V002 | SSH public key placement validation plan | Document planned `authorized_keys` placement check. | Public key placement validation method is defined without real key content. | `configs/ssh-key-authentication-plan.md`, `validation.md` |
| V003 | Control Plane to Bastion key authentication plan | Document placeholder SSH command from Control Plane to `<bastion-host>`. | Control Plane-to-Bastion key authentication method is defined. | `commands.md`, `logs/ssh-key-authentication-validation.log`, `validation.md` |
| V004 | Bastion to On-Prem DB node key authentication plan | Document placeholder SSH command from Bastion to `<db-primary-node>`. | Bastion-to-DB key authentication method is defined. | `commands.md`, `logs/ssh-key-authentication-validation.log`, `validation.md` |
| V005 | Bastion to Monitoring node key authentication plan | Document placeholder SSH command from Bastion to `<monitoring-node>`. | Bastion-to-monitoring key authentication method is defined. | `commands.md`, `logs/ssh-key-authentication-validation.log`, `validation.md` |
| V006 | Bastion to AWS service node key authentication plan | Document placeholder SSH command from Bastion to `<aws-service-node>`. | Bastion-to-AWS key authentication method is defined. | `commands.md`, `logs/ssh-key-authentication-validation.log`, `validation.md` |
| V007 | Bastion to Azure service node key authentication plan | Document placeholder SSH command from Bastion to `<azure-service-node>`. | Bastion-to-Azure key authentication method is defined. | `commands.md`, `logs/ssh-key-authentication-validation.log`, `validation.md` |
| V008 | Bastion to OpenStack service node key authentication plan | Document placeholder SSH command from Bastion to `<openstack-service-node>`. | Bastion-to-OpenStack key authentication method is defined. | `commands.md`, `logs/ssh-key-authentication-validation.log`, `validation.md` |
| V009 | SSH ProxyJump command pattern validation plan | Review placeholder ProxyJump command pattern. | ProxyJump pattern is documented without real users, hosts, or keys. | `commands.md`, `configs/ssh-proxyjump-pattern-summary.md`, `validation.md` |
| V010 | Missing key, wrong key permission, missing authorized_keys entry, or unreachable target failure condition | Define explicit failure criteria. | Key-authentication failures produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. Password login denial is handled in S012, and root login denial is handled in S013.
