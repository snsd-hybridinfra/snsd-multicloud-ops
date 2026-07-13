# Root Login Denial Summary

- Scenario: S013-root-login-denial-validation
- Generated: 2026-07-13T10:16:38+09:00
- Overall result: **PASS**
- Scope: local root-denial baseline, secret-safety, and execution-boundary checks

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | Root denial baseline | PASS | ssh-root-login-denial-baseline.md exists. |
| V002 | SSHD root-denial example | PASS | sshd_config.root-login-denial.example exists. |
| V003 | Non-production marker | PASS | The SSHD example is marked as non-production. |
| V004 | PermitRootLogin setting | PASS | PermitRootLogin no is present. |
| V005 | PubkeyAuthentication setting | PASS | PubkeyAuthentication yes is present. |
| V006 | PasswordAuthentication setting | PASS | PasswordAuthentication no is present. |
| V007 | ChallengeResponseAuthentication setting | PASS | ChallengeResponseAuthentication no is present. |
| V008 | KbdInteractiveAuthentication setting | PASS | KbdInteractiveAuthentication no is present. |
| V009 | AuthenticationMethods setting | PASS | AuthenticationMethods publickey is present. |
| V010 | Root denial policy statements | PASS | All required denial, non-root, sudo, password-storage, placeholder, and evidence statements exist. |
| V011 | Root password safety | PASS | No enabled root login, root password assignment, root credential, or sshpass value was detected. |
| V012 | Private key safety | PASS | No private-key filename or private-key material exists in the repository. |
| V013 | Authorized keys safety | PASS | No authorized_keys file exists in the repository. |
| V014 | Secret and account content | PASS | No password value, key material, credential assignment, numeric IP, account ID, UUID, or token value was detected. |
| V015 | Execution safety boundary | PASS | The validator contains no SSH modification, restart, root attempt, privilege escalation, connection, network, Ansible, cloud, or Kubernetes command. |

## Safety Boundary

The validator inspected repository files only. It did not modify sshd configuration, restart SSH, attempt root login or privilege escalation, connect to hosts, read keys or credentials, or require live network access.
