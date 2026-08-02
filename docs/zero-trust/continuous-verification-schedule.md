# Continuous Verification Frequency and Schedule Boundary

Frequency values ending in `_REFERENCE` are governance recommendations. They
are not installed jobs and do not prove scheduled or continuous operation.
`ZT-CV-WF-001` is currently manual, `scheduled_trigger=false`, and contributes
only `EC3_ONE_TIME_RUNTIME`.

The next campaign, `ZT-RV-001`, must execute the unchanged candidate workflow
three independent times with at least 24 hours between accepted runs. The
earliest campaign shape is therefore run 1 at T0, run 2 no earlier than T0+24h,
and run 3 no earlier than T0+48h. Actual dates are recorded only after each run
occurs.

`ZT-SCH-001` preparation began after EC4 acceptance. Following explicit
approval, the bounded Windows Task Scheduler job was installed on 2026-08-02
with its first run due at 2026-08-03 09:00 KST. The local runner, lock, timeout,
missed-run assessment, and disable/removal controls are configuration-validated;
no scheduled runtime has occurred. EC5 requires at least three valid correlated
scheduled-trigger executions on distinct scheduled dates. A daily job is
neither EC6 continuous observation nor EC7 continuous enforcement.
