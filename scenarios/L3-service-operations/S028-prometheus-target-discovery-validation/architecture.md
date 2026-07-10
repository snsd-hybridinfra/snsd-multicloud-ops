# Architecture

## Relevant Components

- Prometheus: target discovery and scrape status source.
- Node Exporter targets: placeholder host metrics targets.
- kube-state-metrics target: placeholder Kubernetes state target.
- DB Exporter target: placeholder MariaDB metrics target.
- Blackbox Exporter target: placeholder probe target mapping source.
- AWS, Azure, and OpenStack service zone targets: placeholder cloud service targets.
- On-Prem Internal Server Zone targets: placeholder database and internal service targets.

## Discovery Model

- Prometheus service status must be reviewable before target discovery checks.
- Prometheus configuration syntax must be validated before `/targets` evidence is accepted.
- `/targets` page evidence must show placeholder target states and labels.
- Target categories must be mapped to expected job names and labels.
- Target labels must be unique enough to avoid duplicate or ambiguous evidence.
- Exporter installation and probe execution are outside this scenario unless covered by later scenarios.

## Boundary Notes

This scenario validates Prometheus target discovery only. Grafana dashboards, blackbox endpoint probe behavior, replication lag measurement, alerting, and Alertmanager integration are separate or excluded responsibilities.
