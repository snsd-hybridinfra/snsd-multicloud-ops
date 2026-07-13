# Execution Plan

1. Run `powershell -ExecutionPolicy Bypass -File tools/validate-web-pod-failure-recovery.ps1`.
2. Verify three baselines and five samples.
3. Validate workflow placeholders, ten criteria phases, read-only commands, and manual deletion warning.
4. Parse pre-failure Ready Pods, fault marker, original inactivity, replacement Ready Pod, rollout, and endpoint.
5. Warn when elapsed recovery time is not measured.
6. Reject unhealthy post-state, empty endpoints, kube credentials/TLS files, real endpoints/domains/IPs, secrets, and destructive validator logic.
7. Review generated log and summary.
8. Optionally run read-only LiveKubectl after approval.

LiveKubectl and real fault injection are `NOT_RUN` in committed Static evidence.
