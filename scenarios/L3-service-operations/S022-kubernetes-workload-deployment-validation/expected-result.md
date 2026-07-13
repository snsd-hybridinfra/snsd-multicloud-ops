# Expected Result

## Static Pass Criteria

- V001 through V016 return PASS with zero warnings for current samples.
- One Deployment reports 2/2 ready and two available replicas.
- Two Pods report 1/1 Running with zero restarts.
- Manifests contain required controls and no unsafe pattern.
- kubectl is not invoked.

## Optional Live Criteria

At least one Deployment and Pod row must parse; all desired replicas must be ready/available and all Pods Running/ready. Restarts above zero produce WARN.

## Evidence Criteria

Evidence records mode, required files, manifest safety, deployment/Pod parsing, restarts, secret safety, and final judgment without raw live workload rows.
