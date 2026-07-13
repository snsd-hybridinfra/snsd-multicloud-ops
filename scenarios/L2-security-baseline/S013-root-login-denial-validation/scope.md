# Scope

## Included

- SSH root-login denial policy documentation.
- Non-production sshd root-denial example.
- Root denial, public-key authentication, password and interactive denial, and public-key-only method directives.
- Non-root administrator and controlled sudo process placeholders.
- Root-password storage prohibition and evidence model.
- Local root-password, private-key, `authorized_keys`, sensitive-content, and execution-command checks.
- Generated log and summary evidence.

## Excluded

- Modification of local or remote sshd configuration.
- SSH service restart or reload.
- Live root-login, SSH, sudo, or privilege-escalation attempts.
- Real users, root/SSH passwords, public/private keys, `authorized_keys`, hosts, sudo policy, and credentials.
- SSH key-authentication validation, which belongs to S011.
- Password-login denial validation, which belongs to S012.
- Bastion reachability, which belongs to S008.
- Cloud security-group access control, which belongs to S014-S016.

## Assumptions

- The example represents a repository baseline and is not directly deployable.
- Privilege escalation is governed by an approved process outside this repository.
