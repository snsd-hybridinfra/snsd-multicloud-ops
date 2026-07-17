# Zero Trust Reference Laboratory Architecture

This reference architecture distinguishes observed components from planned and reference-only boundaries. A diagram node labelled PLANNED or REFERENCE_ONLY is not implementation evidence.

## Status legend

- **CURRENT:** supported by accepted repository or sanitized runtime evidence.
- **PLANNED:** included in the approved backlog but not yet accepted as implemented.
- **REFERENCE_ONLY:** describes an enterprise dependency the laboratory cannot honestly reproduce.

## 1. Physical and virtual lab boundaries

```mermaid
flowchart TB
  OP["Operator workstation\nCURRENT: repository validators"]
  EVE["EVE-NG network\nCURRENT: VLAN, routing, NAT/PAT, ACL"]
  OS["OpenStack AIO\nCURRENT: provider/tenant/FIP path"]
  PUB["Public-cloud boundary\nPLANNED: temporary AWS/Azure validation"]
  WL["Workload/container boundary\nPLANNED"]
  ID["Identity boundary\nPLANNED"]
  DATA["Data-protection boundary\nPLANNED"]
  ENT["Enterprise UEM, DLP, SIEM, ICAM\nREFERENCE_ONLY"]
  OP --> EVE --> OS
  OP -. approved temporary path .-> PUB
  OS -. future workload .-> WL
  ID -. future identity context .-> WL
  WL -. classified test data .-> DATA
  ENT -. architecture reference only .-> ID
```

The operator workstation is the current governance/validation plane. It must not store cloud credentials, state, kubeconfig, raw traffic, or VM disks in the synchronized repository.

## 2. Policy and telemetry flow

```mermaid
flowchart LR
  SRC["Identity, device, workload, network and data sources\nPLANNED"] --> PIP["PIP context normalization\nPLANNED"]
  PIP --> PE["PE policy evaluation\nPLANNED"]
  PE --> PA["PA approved change coordination\nPLANNED"]
  PA --> PEP["PEP enforcement\nCURRENT only for bounded network controls"]
  PEP --> TEL["Telemetry boundary\nPLANNED centralized collection"]
  TEL --> PIP
  TEL --> EV["Evidence boundary\nCURRENT repository conventions"]
```

This is a **CONCEPTUAL ALIGNMENT**. Current network enforcement is not a complete PDP/PA/PEP implementation.

## 3. Validation and evidence flow

```mermaid
flowchart LR
  PLAN["Approved backlog and verification plan"] --> PRE["Preconditions and sanitizer"]
  PRE --> TEST["Positive, negative, bypass, failure and recovery tests"]
  TEST --> RAW["Raw local-only output\nNever commit"]
  RAW --> SAN["Sanitized evidence"]
  SAN --> ACCEPT["Evidence authority review"]
  ACCEPT --> STATUS["Catalog, baseline and gap reassessment"]
  ACCEPT --> REJECT["Reject or mark inconclusive"]
  REJECT --> PLAN
```

The evidence boundary stores sanitized text and approved configuration extracts only. Secrets, unique identifiers, state, keys, certificates with private material, raw packet captures, and unsanitized output are prohibited.

## 4. Implementation-wave overlay

```mermaid
flowchart LR
  W0["W0 Governance and evidence"] --> W1["W1 Infrastructure and trust"]
  W1 --> W2["W2 Identity, endpoint and workload"]
  W2 --> W3["W3 Application, software and data"]
  W3 --> W4["W4 Visibility, correlation and response"]
  W4 --> W5["W5 Continuous verification"]
  G0["Gate ZT-0"] --> W0
  W0 --> G1["Gate ZT-1"]
  W1 --> G2["Gate ZT-2"]
  W2 --> G3["Gate ZT-3"]
  W3 --> G4["Gate ZT-4"]
  W4 --> G5["Gate ZT-5"]
```

Wave progression is dependency- and evidence-gated, not calendar-driven. A later wave may be designed while an earlier wave is incomplete, but it must not be accepted or represented as operating.

## Boundary responsibilities

| Boundary | Intended responsibility | Status |
|---|---|---|
| Operator workstation | Governance, local validation, sanitized evidence acceptance | CURRENT, bounded |
| EVE-NG | Network zones and controlled flow enforcement | CURRENT, bounded |
| OpenStack | Private-cloud network/workload substrate | CURRENT network path; workload controls PLANNED |
| Public cloud | Temporary provider validation | PLANNED |
| Workload/container | Application identity, admission, authorization, runtime state | PLANNED |
| Identity | Inventory, authentication, MFA, roles, session context | PLANNED |
| Policy | Context normalization, decision, approved administration | PLANNED |
| Telemetry | Normalized events, health, correlation | PLANNED |
| Evidence | Sanitization, acceptance, traceability, reassessment | CURRENT conventions; continuous evidence PLANNED |
| Automation | Approval-gated change and rollback | PLANNED |
| Data protection | Synthetic data inventory, labels, access, encryption, recovery | PLANNED |
| Enterprise services | ICAM, UEM/MDM, EDR/XDR, DLP, SIEM, threat intelligence | REFERENCE_ONLY |
