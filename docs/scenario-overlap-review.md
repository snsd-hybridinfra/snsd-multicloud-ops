# Scenario Overlap Review

This review identifies ownership risks only. It does not change scenario files or their locked implementation scope.

| Overlap Group | Related Scenarios | Risk Description | Recommended Boundary | Severity |
|---|---|---|---|---|
| Provider security rules and misconfiguration recovery | S014, S015, S016, S037 | Baseline rule review and failure testing may capture the same rule sets and denial checks. | S014-S016 own provider-specific steady-state least-privilege acceptance. S037 owns controlled misconfiguration detection, impact observation, and manual rollback using baseline evidence by reference. | MEDIUM |
| MariaDB access, replication, and failure handling | S017, S026, S027, S033, S034 | User grants, replication credentials, status output, lag, and outage response share database hosts and command families. | S017 owns users, hosts, grants, and network access. S026 owns replication function, S027 lag measurement, S033 replica outage behavior, and S034 the manual primary-stop runbook. Reuse evidence by reference rather than recapture. | MEDIUM |
| Traffic entry and availability path | S023, S024, S025, S030, S035 | HTTP responses and endpoint health can be interpreted as ingress routing, proxy forwarding, backend health, external probing, or failure recovery. | S023 owns Ingress rules and backend routing; S024 provider reverse-proxy forwarding; S025 backend health and single-backend continuity; S030 independent Blackbox probe results; S035 entrypoint failure and manual recovery. Assign a unique evidence owner for each hop. | HIGH |
| Observability discovery and failure detection | S028, S029, S030, S036 | The same target, query, dashboard, and DOWN state may be collected by several scenarios. | S028 owns scrape discovery and UP state, S029 dashboard rendering, S030 endpoint probe semantics, and S036 deliberate target-DOWN detection. Cross-reference target IDs and timestamps. | MEDIUM |
| Backup, restore, and post-recovery health | S038, S039, S040 | A restore test can accidentally absorb backup creation and service-health acceptance into one scenario. | S038 ends at sanitized backup artifact creation and integrity evidence; S039 owns restore execution and data checks; S040 starts after restore and owns end-to-end service health. Use one recovery correlation ID across all three. | HIGH |
| Drift, policy, cost, and cleanup governance | S041, S042, S043, S044, S045, S046 | Drift, policy violation, cost risk, and cleanup candidacy can describe the same resource and lead to overlapping remediation decisions. | S041 detects Terraform drift; S042 documents approved manual remediation; S043 evaluates general policy; S044 evaluates Kubernetes manifests; S045 identifies cost risk; S046 owns approved cleanup planning. No scenario should silently trigger another. | HIGH |
| ML evidence and final reporting | S047, S048, S049, S050 | Dataset, anomaly result, anomaly report, and final repository report can duplicate conclusions or imply stronger security capability. | S047 owns sanitized metric datasets; S048 owns bounded anomaly judgment; S049 owns a human-reviewable anomaly report; S050 aggregates scenario status and evidence without revalidating or certifying results. | MEDIUM |

## Review Conclusion

Current scenario documents generally state these boundaries explicitly. No immediate scenario-file correction is required. Before implementation, define stable artifact identifiers and cross-scenario reference rules so evidence is referenced rather than duplicated.

