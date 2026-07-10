# S024-nginx-reverse-proxy-validation

| Field | Value |
|---|---|
| Scenario ID | S024 |
| Scenario Name | Nginx Reverse Proxy Validation |
| Level | L3 Service Operations Validation |
| Category | Service Operations |
| Primary Domain | Provider-level service entry |
| Related Components | AWS reverse proxy, Azure reverse proxy, OpenStack reverse proxy, Kubernetes Ingress endpoint, upstream service, Nginx logs |
| Validation Type | Service Operation Validation |
| Evidence Directory | evidence/L3-service-operations/S024-nginx-reverse-proxy-validation/ |
| Status | PLANNED |

## Objective Summary

Define and validate the Nginx Reverse Proxy model used as the provider-level service entry point for AWS, Azure, and OpenStack service zones.

## Scope Summary

This scenario validates Nginx reverse proxy forwarding only. It covers provider-level reverse proxy endpoints, forwarding to Kubernetes Ingress, upstream mapping, HTTP response validation, health check placeholders, Nginx syntax validation, and access/error log evidence collection.

## Validation Summary

Validation checks confirm that Nginx service status and syntax can be reviewed, AWS/Azure/OpenStack reverse proxy endpoints are planned, upstream mappings point to the intended Ingress endpoint, successful HTTP responses are defined, and failures such as Nginx down, invalid config, wrong upstream, route timeout, HTTP 5xx, or missing logs are explicitly captured.

## Evidence Output Summary

Evidence must be recorded under `evidence/L3-service-operations/S024-nginx-reverse-proxy-validation/`, with command plans in `commands.md`, validation results in `validation.md`, and future sanitized supporting artifacts under `configs/`, `logs/`, and `screenshots/`.
