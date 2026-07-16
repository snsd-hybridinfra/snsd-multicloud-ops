# External Address Exposure Policy

**Status: PLANNED — no external address or public service is configured.**

## Purpose

An external address is optional. When approved, it supports only temporary
HTTP/HTTPS ingress, external availability checks, and Blackbox validation.
The actual value is always committed as `<external-address-masked>`.

## Allowed Exposure

| Protocol | Port | Purpose | Conditions |
|---|---:|---|---|
| HTTP | 80 | Redirect, bounded lab routing, or availability validation | Approved window, minimal source scope where practical, no sensitive content |
| HTTPS | 443 | Encrypted ingress and availability validation | Approved certificate handling outside repository, bounded window |

## Prohibited Public Exposure

- SSH and Bastion administration;
- MariaDB and replication ports;
- Kubernetes API;
- OpenStack API and management endpoints;
- Prometheus, Grafana, exporter management, or datasource endpoints;
- EVE-NG management;
- backup repositories;
- cloud credentials, dashboards, or administrative interfaces.

## Validation Window

1. Confirm owner, purpose, TTL, and rollback.
2. Apply only the minimum HTTP/HTTPS rule.
3. Run the owning availability/Blackbox scenario.
4. Collect sanitized evidence without the real address, DNS name, certificate,
   token, cookie, or Authorization header.
5. Remove the rule and public/Floating IP where applicable.
6. Verify exposure and resource cleanup.

## No Implied Availability Claim

Optional exposure does not establish production availability, global load
balancing, DDoS protection, WAF, automatic failover, or public-cloud runtime.

## Non-Production Disclaimer

The policy applies only to disposable lab validation and is not authorization
to expose any organizational or production system.
