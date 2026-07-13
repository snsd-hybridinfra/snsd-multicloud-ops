# Scope

## Included

- Static runbook, command reference, criteria, and nine sanitized samples.
- API Pod, Service endpoint, HTTP, failure signal, recovery, rollout, and timing review.
- Optional explicit read-only LiveKubectl and unauthenticated LiveHttp checks.
- Safety checks for kubeconfig, tokens, certificates, keys, cookies, authorization values, endpoints, addresses, and destructive automation.

## Excluded

- Automated Pod deletion, scale-to-zero, apply, patch, edit, restart, cordon, drain, taint, or any resource mutation.
- Production tests, credentials, kubeconfig, real endpoints/IPs/domains, payloads, response bodies, or secrets.
- S030, S031, S035, and S040 responsibilities.
