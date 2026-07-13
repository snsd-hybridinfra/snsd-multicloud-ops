# Execution Plan

1. Run the validator without parameters for static validation.
2. Confirm documentation, manifests, command examples, and samples.
3. Validate object kinds, namespace, labels/selectors, probes, resources, and image tag.
4. Reject unsafe manifest patterns and sensitive content.
5. Parse deployment and Pod samples; evaluate availability, readiness, running state, failures, and restarts.
6. Confirm only two guarded read-only live argument sets exist.
7. Review generated evidence; use `-LiveKubectl` only when explicitly approved.

## Execution Boundary

Default mode never invokes kubectl. Live mode lists deployments and Pods only; dry-run and rollout examples are documentation references, not validator actions.
