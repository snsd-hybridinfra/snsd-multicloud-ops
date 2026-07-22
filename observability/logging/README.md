# Bounded Persistent Visibility Stack

This directory defines the repository-controlled configuration for the
single-node `ZT-VIS-001` persistent-storage pilot on the dedicated monitoring
VM. It uses pinned Grafana, Loki, and Alloy images.

## Security boundary

- Only sanitized JSON Lines under the VM-local approved input directory are
  collected.
- No host journal, broad filesystem, Docker socket, credential file, private
  key, or raw validator output is mounted.
- Loki, Alloy, and Grafana listen only on VM loopback host ports. Operator UI
  access requires the approved SSH boundary and a loopback tunnel.
- Anonymous Grafana access and self-registration are disabled.
- The Grafana administrator password is read from
  `/opt/snsd-monitoring/secrets/grafana_admin_password`, which is never stored
  in Git or printed in evidence.
- The stack has no external alert receiver and performs no blocking or
  remediation.

## Retention and persistence

Loki uses filesystem TSDB storage with a 14-day retention policy. Grafana,
Loki, and Alloy state lives below `/opt/snsd-monitoring/data/` on the VM.
Container deletion does not authorize deletion of those directories.

## Validation

Configuration validation and image availability do not establish runtime
acceptance. Runtime validation must confirm healthy pinned containers, Loki
readiness, a synthetic sanitized write and query, Grafana health, Alloy
health, persistence paths, retention, and absence of exposed secrets.

## Rollback

Run Compose down for the exact `snsd-zero-trust-visibility` project. Preserve
the VM-local data and secret directories until a separate deletion approval is
recorded. Do not remove Docker, the VM, networking, or operator access as part
of stack rollback.
