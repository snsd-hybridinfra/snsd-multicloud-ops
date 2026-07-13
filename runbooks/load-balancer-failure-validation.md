# Load Balancer Failure Validation

S035 validates load-balancer failure isolation with sanitized local evidence.

1. Record healthy `<load-balancer-url-placeholder>`, `<backend-a-url-placeholder>`, and `<backend-b-url-placeholder>`.
2. A separately authorized operator may run `systemctl stop <load-balancer-service-placeholder>` as **MANUAL FAULT INJECTION ONLY** in a disposable lab.
3. Record LB inactive/503/timeout/connection-refused and client impact while direct backends remain healthy.
4. Record `systemctl start <load-balancer-service-placeholder>` as **MANUAL RECOVERY ACTION ONLY**.
5. Confirm restored LB and client health, document `<manual-bypass-placeholder>` and `<rollback-to-normal-path-placeholder>`, and compare elapsed time with `<recovery-time-threshold-seconds>` under `<evidence-path>`.

Static mode uses samples only. Explicit LiveHttp sends unauthenticated HEAD requests and stores only sanitized status judgments. The validator never stops/starts services, changes Nginx, DNS, routing, Ingress, or cloud load balancers. S025 owns normal load balancing, S030 probing, and S040 final health.
