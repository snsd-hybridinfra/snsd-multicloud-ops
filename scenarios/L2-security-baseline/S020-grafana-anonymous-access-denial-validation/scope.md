# Scope

## Included

- Grafana anonymous-access denial policy, access-control matrix, and INI example validation.
- Anonymous section, disabled value, true-value/environment override, and Viewer-effect checks.
- Admin password placeholder, API token, datasource credential, URL, address, identifier, private material, and secret safety checks.
- Safe local evidence generation.

## Excluded

- Running Grafana, starting containers, curling endpoints, connecting to hosts, or reading environment secrets.
- Live login, dashboard authorization, sharing, datasource access, or production configuration validation.
- Prometheus target discovery (S028), Grafana dashboard behavior (S029), Nginx headers (S019), and public exposure controls (S014-S016).
