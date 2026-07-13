# Failure Condition

S022 fails if required documentation, manifests, controls, or sample evidence is missing; labels/selectors disagree; probes/resources are absent; an unsafe manifest pattern is present; deployment replicas are unavailable; Pods are non-running/non-ready; or credentials, endpoints, addresses, secrets, or mutation commands are detected.

## Warning Condition

Any Pod restart above zero produces WARN unless separately documented as expected.

## Safety Failure

Any kubeconfig, token, certificate, key, endpoint, public address, raw sensitive live output, Secret, image-pull secret, or cluster mutation violates the scenario boundary.
