# ZT-RV-001 Future Schedule Proposal

The selected campaign is `ZT-RV-001`, with a manual reference frequency no
faster than once per 24 hours and an expected execution duration below ten
minutes. Windows Task Scheduler, GitHub Actions, cron, and systemd timers all
remain `NOT_IMPLEMENTED`.

The bounded workstation mechanism may be evaluated by `ZT-SCH-001` only after
three independent consecutive successes establish EC4. A future mechanism
must use the fixed campaign, preserve the lock, timeout, sanitized evidence,
manual history-review boundary, and missed-run reporting. It must not perform
an automatic catch-up, remediation, maturity update, commit, or push.
