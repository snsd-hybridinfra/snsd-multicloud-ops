# Commands

Scenario: S021-kubernetes-node-readiness-validation

Level: L3-service-operations

## Run Static Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-kubernetes-node-readiness.ps1
```

## Run Optional Explicit Live Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-kubernetes-node-readiness.ps1 -LiveKubectl
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L3-service-operations\S021-kubernetes-node-readiness-validation\logs\kubernetes-node-readiness-validation.log
Get-Content evidence\L3-service-operations\S021-kubernetes-node-readiness-validation\configs\kubernetes-node-readiness-summary.md
```

## Safety Notes

Default mode does not invoke kubectl. Live mode is planned only when explicitly requested, runs one read-only node listing, and stores no raw node rows, kubeconfig details, tokens, certificates, endpoints, or addresses.

## Real-Lab Evidence Command Categories

The pasted terminal evidence for S021 should be collected with these command categories. Repository documentation uses placeholders only:

```text
ssh <ssh-user-placeholder>@<k3s-node-ip-placeholder>
sudo systemctl is-active k3s
sudo kubectl get nodes -o wide
sudo kubectl get pods -A
sudo kubectl version --client
```

Before commit:

- replace the SSH user with `<user-masked>`;
- replace the Bastion address with `<bastion-ip-masked>`;
- replace the k3s node address with `<k3s-node-ip-masked>`;
- replace every other address with `<lab-ip-masked>`;
- replace the k3s hostname with `<hostname-masked>`;
- remove kubeconfig content, tokens, certificates, private keys, passwords, secrets, Authorization headers, cookies, and credential-like values.

Raw terminal output must not be committed. The current sanitized intake is stored at `logs/20260714-S021-k3s-node-readiness.sanitized.txt`; its validation summary is `configs/20260714-S021-k3s-node-readiness-validation-summary.md`.
