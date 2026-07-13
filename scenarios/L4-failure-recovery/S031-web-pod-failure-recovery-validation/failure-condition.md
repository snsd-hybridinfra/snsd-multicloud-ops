# Failure Condition

S031 fails for missing artifacts/criteria/commands; unhealthy pre/post Pods; missing manual marker, original termination, replacement, successful rollout, or endpoint; CrashLoop/ImagePull/Failed/Pending/Unknown/0-ready/none states; destructive validator commands; kubeconfig/token/certificate/key/secret; real cluster URLs/domains/IPs; or unhealthy LiveKubectl results.

Missing numeric elapsed time is WARN. Pod deletion may appear only in clearly marked manual disposable-lab documentation/evidence and is never executed by the validator.
