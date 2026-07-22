# ZT-SYS-001 System Change Control

Every change records scope, owner, classification, approval, pre-change state,
configuration backup, syntax check, implementation authority, maintenance
boundary, runtime checks, rollback trigger, post-change evidence, incident
handling, tracking updates, and any capability-specific maturity proposal.

| Classification | Authority |
|---|---|
| DOCUMENTATION_ONLY | Repository review |
| LOCAL_TOOLING | Repository review plus tests |
| READ_ONLY_VALIDATOR | Fixed-command and privacy review |
| LOW_RISK_CONFIGURATION | Explicit target owner and rollback review |
| SERVICE_AFFECTING | Explicit user approval and maintenance/recovery plan |
| NETWORK_AFFECTING | Explicit user approval, path tests, and network rollback |
| ACCESS_AFFECTING | Explicit user approval and independent recovery access |
| DESTRUCTIVE | Explicit user approval, exact target, backup, and isolated recovery |

Detection never authorizes remediation. Drift, stopped service, update, audit,
exposure, or recovery findings create a recommendation and approval request;
they do not trigger restart, installation, overwrite, credential rotation,
firewall change, or automatic authoritative-document mutation.
