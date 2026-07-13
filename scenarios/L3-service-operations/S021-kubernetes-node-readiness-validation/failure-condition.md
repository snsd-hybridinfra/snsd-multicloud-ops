# Failure Condition

S021 fails if a required file, command reference, readiness term, sample node, or parseable row is missing; a node reports NotReady or lacks Ready; a forbidden credential or sensitive value is detected; or requested live validation cannot safely return ready node statuses.

## Warning Condition

SchedulingDisabled produces WARN and requires an expected-maintenance review, but does not itself imply NotReady.

## Safety Failure

Any kubeconfig, token, certificate, key, endpoint, numeric address, raw sensitive live output, or mutation command violates the scenario boundary.
