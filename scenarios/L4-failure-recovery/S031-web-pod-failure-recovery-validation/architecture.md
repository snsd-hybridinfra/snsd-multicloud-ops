# Architecture

This scenario models Web Pod recovery within the Kubernetes/k3s workload control loop.

## Relevant Components

- Namespace placeholder: `<namespace>`.
- Web Deployment placeholder: `<web-deployment>`.
- Web Pod placeholder: `<web-pod>`.
- Web Service placeholder: `<web-service>`.
- Ingress host placeholder: `<ingress-host>`.
- Health endpoint placeholder: `<health-endpoint>`.
- Recovery threshold placeholder: `<recovery-threshold-seconds>`.
- Evidence store: `evidence/L4-failure-recovery/S031-web-pod-failure-recovery-validation/`.

## Recovery Flow

1. Capture pre-failure Web Deployment, Pod, Service endpoint, and HTTP health state.
2. Inject a single Web Pod failure by planning `kubectl delete pod <web-pod> -n <namespace>`.
3. Observe Deployment/ReplicaSet replacement behavior.
4. Confirm replacement Pod reaches Ready state.
5. Confirm the Web Service endpoint and HTTP health endpoint recover.
6. Record recovery time and compare it against provisional thresholds.

This scenario does not define or change Kubernetes manifests. It validates the recovery behavior expected after workload deployment is already handled by S022.
