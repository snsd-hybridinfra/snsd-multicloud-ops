# Scope

## Included

- SSH password-login denial policy documentation.
- Non-production sshd password-denial example.
- Password, challenge-response, and keyboard-interactive denial directives.
- Public-key authentication and `AuthenticationMethods publickey` requirements.
- Password-storage prohibition and external break-glass policy.
- Local password-value, private-key, `authorized_keys`, sensitive-content, and execution-command checks.
- Generated log and summary evidence.

## Excluded

- Modification of local or remote sshd configuration.
- SSH service restart or reload.
- Live SSH or password-authentication attempts.
- Real users, passwords, public/private keys, `authorized_keys`, hosts, and credentials.
- SSH key-authentication validation, which belongs to S011.
- Root-login denial validation, which belongs to S013.
- Bastion reachability, which belongs to S008.
- Cloud security-group access control, which belongs to S014-S016.

## Assumptions

- The example represents a repository baseline and is not directly deployable.
- Emergency access is governed by an approved process outside this repository.
