# SSH Key Authentication Summary

- Scenario: S011-ssh-key-authentication-validation
- Generated: 2026-07-13T09:58:24+09:00
- Overall result: **PASS**
- Scope: local SSH baseline, key-safety, and execution-boundary checks

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | SSH baseline document | PASS | ssh-key-authentication-baseline.md exists. |
| V002 | SSHD example config | PASS | sshd_config.key-auth.example exists. |
| V003 | Non-production marker | PASS | The SSHD example is marked as non-production. |
| V004 | PubkeyAuthentication setting | PASS | PubkeyAuthentication yes is present. |
| V005 | PasswordAuthentication setting | PASS | PasswordAuthentication no is present. |
| V006 | PermitRootLogin setting | PASS | PermitRootLogin no is present. |
| V007 | ChallengeResponseAuthentication setting | PASS | ChallengeResponseAuthentication no is present. |
| V008 | KbdInteractiveAuthentication setting | PASS | KbdInteractiveAuthentication no is present. |
| V009 | AuthorizedKeysFile setting | PASS | AuthorizedKeysFile .ssh/authorized_keys is present. |
| V010 | Baseline policy statements | PASS | All required access, storage, rotation, user, placeholder, and evidence statements exist. |
| V011 | Private key safety | PASS | No private-key filename or private-key material exists in the repository. |
| V012 | Authorized keys safety | PASS | No authorized_keys file exists in the repository. |
| V013 | Secret and account content | PASS | No password value, key material, credential assignment, numeric IP, account ID, UUID, or token value was detected. |
| V014 | Execution safety boundary | PASS | The validator contains no SSH modification, restart, connection, network, Ansible, cloud, or Kubernetes command. |

## Safety Boundary

The validator inspected repository files only. It did not modify sshd configuration, restart SSH, connect to hosts, read keys or credentials, or require live network access.
