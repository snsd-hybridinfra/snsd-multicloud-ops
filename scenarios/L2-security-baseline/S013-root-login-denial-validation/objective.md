# Objective

Validate a safe SSH root-login denial baseline containing `PermitRootLogin no`, public-key-only access, approved non-root administration, controlled sudo escalation, root-password storage prohibition, placeholders, and evidence rules.

Success means all local baseline and repository safety checks pass without a root-login attempt, privilege escalation, host connection, or SSH configuration change.

SSH key authentication is handled in S011, password-login denial in S012, bastion reachability in S008, and cloud access controls in S014-S016.
