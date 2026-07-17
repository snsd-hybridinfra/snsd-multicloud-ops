# ZT-VIS-001 Rollback

Normal validation does not execute rollback. A reviewed repository change may
remove the local telemetry tools, schemas, event/rule catalogs, wrapper, tests,
and generated package evidence. Ignored files below
.runtime/zero-trust/telemetry/ may be removed locally after confirming they are
not required for review.

No central logging service, collector account, dashboard, firewall exception,
or persistent volume was deployed, so there is no remote-service rollback in
this increment. Preserve OpenStack, EVE-NG, router configuration, all existing
validators, operator access, unrelated Docker volumes, and S001-S050.
