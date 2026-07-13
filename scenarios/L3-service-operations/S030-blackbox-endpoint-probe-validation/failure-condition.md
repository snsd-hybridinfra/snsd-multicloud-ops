# Failure Condition

S030 fails if required artifacts/modules/scrape fields/metrics/samples are missing; healthy evidence fails; warning/failure fixtures are misclassified; query metrics are absent/unhealthy; auth/TLS/credentials/tokens/cookies/authorization, real URLs/domains/addresses, IDs, or secrets are detected; Static mode invokes a client/reload/network; or LiveBlackbox fails validation.

The warning fixture and live 401/403 produce WARN. The negative failure fixture must contain failure indicators and be rejected operationally for its validator check to pass.
