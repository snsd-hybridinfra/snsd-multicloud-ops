# Architecture

## Repository Components

- `ssh-password-login-denial-baseline.md`: password denial, storage, break-glass, placeholder, and evidence rules.
- `sshd_config.password-denial.example`: non-production denial directives.
- `validate-ssh-password-login-denial-baseline.ps1`: local directive, password-value, key-safety, secret, and execution-boundary checks.
- S012 evidence directory: generated log and summary.

## Baseline Model

Administrative login remains public-key only. Password, challenge-response, and keyboard-interactive methods are disabled. No password value is stored, and emergency access remains external to the repository.

## Validation Flow

The validator reads the two baseline files, verifies directives and policy statements, scans for enabled password authentication and password values, checks repository key safety, and prevents active SSH-related commands. It does not inspect or change a running SSH service.
