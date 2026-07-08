# Execution Plan

## Preparation

1. Review S002 for zone routing assumptions.
2. Review S007 for inventory group and placeholder assumptions.
3. Confirm this scenario is documentation and evidence planning only.
4. Confirm no real IPs, credentials, SSH private keys, provider account values, tfstate, or kubeconfig files are present or required.
5. Confirm SSH hardening is excluded and deferred to L2 scenarios.

## Execution Steps

1. Define the bastion inventory entry validation plan.
2. Define Management Zone to Bastion ping or TCP reachability plan.
3. Define Bastion SSH reachability plan using placeholder commands.
4. Define Bastion to On-Prem DB node reachability plan.
5. Define Bastion to Monitoring node reachability plan.
6. Define Bastion to AWS service node reachability plan.
7. Define Bastion to Azure service node reachability plan.
8. Define Bastion to OpenStack service node reachability plan.
9. Define SSH ProxyJump command pattern validation plan.
10. Define evidence collection through Bastion path validation plan.
11. Define failure condition for unreachable Bastion, missing route, blocked SSH, or invalid inventory entry.

## Evidence Capture

1. Record planned reachability commands and placeholders in `commands.md`.
2. Record validation checks and TODO results in `validation.md`.
3. Map reachability path evidence to `configs/bastion-reachability-path-summary.md`.
4. Map SSH jump pattern evidence to `configs/ssh-jump-pattern-summary.md`.
5. Map future reachability logs to `logs/bastion-reachability-validation.log`.
6. Map future path diagram evidence to `screenshots/bastion-path-diagram.png` only after binary evidence is approved and sanitized.
