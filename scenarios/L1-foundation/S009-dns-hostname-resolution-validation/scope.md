# Scope

## Included

- Non-production hostname-to-placeholder mappings.
- Required host aliases, domain suffixes, and address tokens.
- Naming convention and zone/domain separation policy.
- Internal-only public-DNS independence boundary.
- Bastion, database, Kubernetes, monitoring, and cloud-node resolution rules.
- Failure and evidence-capture policy statements.
- Local checks for numeric IPs, sensitive content, account identifiers, DNS exports, and active external commands.
- Generated local log and Markdown summary evidence.

## Excluded

- Real DNS queries, resolver changes, records, zones, servers, and hosts-file updates.
- Public or private DNS record validation.
- Host connection, reachability, port, or instance-existence validation.
- Credentials, keys, cloud authentication, and account-specific values.
- Cloud-provider DNS, Kubernetes DNS, OpenStack, or external network queries.
- Multi-cloud inventory validation, which belongs to S007.
- Bastion reachability, which belongs to S008.
- Kubernetes service and ingress routing, which belong to S022-S023.
- Prometheus and Grafana validation, which belong to S028-S029.

## Assumptions

- Names and domains are symbolic placeholders only.
- The model does not assert that a resolver, zone, record, service, or instance exists.
