# Expected Result

- Pre-change security rule baseline is documented.
- Controlled placeholder misconfiguration injection is planned.
- Public SSH, public DB, and overly broad CIDR detection checks are planned.
- Required service access breakage detection is planned.
- Unauthorized and authorized source access behavior is documented.
- Manual rollback decision points are explicit.
- Post-rollback security rule and service reachability validation are planned.
- Detection and rollback timing are recorded with TODO placeholders until execution is approved.
- Real-time blocking, WAF, IDS/IPS, EDR, SOAR, and CSPM claims are explicitly excluded.
- All validation checks map to `commands.md`, `validation.md`, or required future artifacts under `configs/`, `logs/`, and `screenshots/`.
- No credentials, secrets, public IPs, private keys, tfstate, kubeconfig, cloud account values, subscription IDs, tenant IDs, or account-specific values are added.
