#!/usr/bin/env python3
"""Validate P2-VIS-001 bounded deployment, live evidence, and partial promotion."""

from __future__ import annotations

import json
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from validate_zero_trust import validate_schema_instance  # noqa: E402

PACKAGE = Path("docs/zero-trust/packages/zt-vis-002-package.yaml")
PACKAGE_SCHEMA = Path("schemas/zt-vis-002-package.schema.json")
CONTRACT = Path("docs/zero-trust/phase-2-visibility-deployment-contract.yaml")
CONTRACT_SCHEMA = Path("schemas/phase-2-visibility-deployment-contract.schema.json")
READINESS = Path("docs/zero-trust/phase-2-visibility-readiness-contract.yaml")
READINESS_SCHEMA = Path("schemas/phase-2-visibility-readiness-contract.schema.json")
NATIVE_VALIDATION = Path("docs/zero-trust/phase-2-visibility-native-validation.yaml")
NATIVE_VALIDATION_SCHEMA = Path("schemas/phase-2-visibility-native-validation.schema.json")
CONTROL_NODE_ADR = Path("docs/adr/0015-use-vmware-ansible-control-node.md")
CONTROL_NODE_EVIDENCE = Path("docs/evidence/zero-trust/zt-vis-002-control-node.sanitized.json")
CONTROL_NODE_PROVISIONER = Path("tools/local-vm/New-AnsibleControlVm.ps1")
LIVE_GATE_DISCOVERY = Path("docs/evidence/zero-trust/zt-vis-002-live-gate-discovery.sanitized.json")
LIVE_GATE_DISCOVERY_SCHEMA = Path("schemas/phase-2-visibility-live-gate-discovery.schema.json")
CINDER_ADR = Path("docs/adr/0016-enable-dedicated-cinder-lvm-prerequisite.md")
CINDER_EVIDENCE = Path("docs/evidence/zero-trust/zt-vis-002-cinder-prerequisite-activation.sanitized.json")
CINDER_EVIDENCE_SCHEMA = Path("schemas/phase-2-visibility-cinder-prerequisite.schema.json")
CINDER_DISK_PROVISIONER = Path("tools/local-vm/Add-CinderDiskToOpenStackAio.ps1")
EXTERNAL_INPUT_INITIALIZER = Path("tools/local-vm/Initialize-ZtVis002ExternalInputs.sh")
EXTERNAL_INPUT_EVIDENCE = Path("docs/evidence/zero-trust/zt-vis-002-external-input-readiness.sanitized.json")
EXTERNAL_INPUT_EVIDENCE_SCHEMA = Path("schemas/phase-2-visibility-external-input-readiness.schema.json")
TERRAFORM_PREFLIGHT_EVIDENCE = Path("docs/evidence/zero-trust/zt-vis-002-terraform-preflight.sanitized.json")
TERRAFORM_PREFLIGHT_EVIDENCE_SCHEMA = Path("schemas/phase-2-visibility-terraform-preflight.schema.json")
BOUNDED_DEPLOYMENT_EVIDENCE = Path("docs/evidence/zero-trust/zt-vis-002-bounded-deployment.sanitized.json")
BOUNDED_DEPLOYMENT_EVIDENCE_SCHEMA = Path("schemas/phase-2-visibility-bounded-deployment-evidence.schema.json")
LIVE_VALIDATION_EVIDENCE = Path("docs/evidence/zero-trust/zt-vis-002-live-validation.sanitized.json")
LIVE_VALIDATION_EVIDENCE_SCHEMA = Path("schemas/phase-2-visibility-live-validation.schema.json")
PARTIAL_PROMOTION_DECISION = Path("docs/evidence/zero-trust/zt-vis-002-partial-promotion-decision.sanitized.json")
PARTIAL_PROMOTION_DECISION_SCHEMA = Path("schemas/phase-2-visibility-partial-promotion-decision.schema.json")
ALERT_VALIDATION_PLAN = Path("docs/zero-trust/phase-2-visibility-alert-validation-plan.yaml")
ALERT_VALIDATION_PLAN_SCHEMA = Path("schemas/phase-2-visibility-alert-validation-plan.schema.json")
ALERT_VALIDATION_EVIDENCE = Path("docs/evidence/zero-trust/zt-vis-002-alert-validation.sanitized.json")
ALERT_VALIDATION_EVIDENCE_SCHEMA = Path("schemas/phase-2-visibility-alert-validation-evidence.schema.json")
LIVE_VALIDATOR = Path("tools/live-validation/remote/validate-zt-vis-002-runtime.sh.example")
MTLS_VALIDATOR = Path("tools/live-validation/validate_zt_vis_002_mtls.py")
LIVE_VALIDATION_PLAYBOOK = Path("ansible/playbooks/zt-vis-002-live-validation.yml")
ALERT_VALIDATOR = Path("tools/live-validation/remote/validate-zt-vis-002-alert-delivery.py.example")
ALERT_VALIDATION_PLAYBOOK = Path("ansible/playbooks/zt-vis-002-alert-validation.yml")
TF_MODULE = Path("terraform/modules/zt-vis-002-openstack")
TF_ENV = Path("terraform/envs/zt-vis-002-openstack")
ANSIBLE_ROLE = Path("ansible/roles/zt_vis_002")
ANSIBLE_HOST_ROLE = Path("ansible/roles/zt_vis_002_host")

REQUIRED_PATHS = (
    PACKAGE,
    PACKAGE_SCHEMA,
    CONTRACT,
    CONTRACT_SCHEMA,
    READINESS,
    READINESS_SCHEMA,
    NATIVE_VALIDATION,
    NATIVE_VALIDATION_SCHEMA,
    CONTROL_NODE_ADR,
    CONTROL_NODE_EVIDENCE,
    CONTROL_NODE_PROVISIONER,
    LIVE_GATE_DISCOVERY,
    LIVE_GATE_DISCOVERY_SCHEMA,
    CINDER_ADR,
    CINDER_EVIDENCE,
    CINDER_EVIDENCE_SCHEMA,
    CINDER_DISK_PROVISIONER,
    EXTERNAL_INPUT_INITIALIZER,
    EXTERNAL_INPUT_EVIDENCE,
    EXTERNAL_INPUT_EVIDENCE_SCHEMA,
    TERRAFORM_PREFLIGHT_EVIDENCE,
    TERRAFORM_PREFLIGHT_EVIDENCE_SCHEMA,
    BOUNDED_DEPLOYMENT_EVIDENCE,
    BOUNDED_DEPLOYMENT_EVIDENCE_SCHEMA,
    LIVE_VALIDATION_EVIDENCE,
    LIVE_VALIDATION_EVIDENCE_SCHEMA,
    PARTIAL_PROMOTION_DECISION,
    PARTIAL_PROMOTION_DECISION_SCHEMA,
    ALERT_VALIDATION_PLAN,
    ALERT_VALIDATION_PLAN_SCHEMA,
    ALERT_VALIDATION_EVIDENCE,
    ALERT_VALIDATION_EVIDENCE_SCHEMA,
    LIVE_VALIDATOR,
    MTLS_VALIDATOR,
    LIVE_VALIDATION_PLAYBOOK,
    ALERT_VALIDATOR,
    ALERT_VALIDATION_PLAYBOOK,
    TF_MODULE / "versions.tf",
    TF_MODULE / "variables.tf",
    TF_MODULE / "main.tf",
    TF_MODULE / "outputs.tf",
    TF_MODULE / "README.md",
    TF_ENV / "versions.tf",
    TF_ENV / ".terraform.lock.hcl",
    TF_ENV / "providers.tf",
    TF_ENV / "main.tf",
    TF_ENV / "variables.tf",
    TF_ENV / "outputs.tf",
    TF_ENV / "terraform.tfvars.example",
    TF_ENV / "README.md",
    ANSIBLE_ROLE / "defaults/main.yml",
    ANSIBLE_ROLE / "tasks/main.yml",
    ANSIBLE_ROLE / "handlers/main.yml",
    ANSIBLE_ROLE / "templates/compose.yaml.j2",
    ANSIBLE_ROLE / "templates/loki-config.yaml.j2",
    ANSIBLE_ROLE / "templates/alloy-config.alloy.j2",
    ANSIBLE_ROLE / "templates/prometheus.yaml.j2",
    ANSIBLE_ROLE / "templates/blackbox.yaml.j2",
    ANSIBLE_ROLE / "templates/grafana-datasources.yaml.j2",
    ANSIBLE_ROLE / "README.md",
    ANSIBLE_HOST_ROLE / "defaults/main.yml",
    ANSIBLE_HOST_ROLE / "tasks/main.yml",
    ANSIBLE_HOST_ROLE / "handlers/main.yml",
    ANSIBLE_HOST_ROLE / "templates/nginx-zt-vis-002.conf.j2",
    ANSIBLE_HOST_ROLE / "README.md",
    Path("ansible/playbooks/zt-vis-002-bootstrap.yml"),
    Path("ansible/playbooks/zt-vis-002-deploy.yml"),
    Path("ansible/playbooks/zt-vis-002-rollback.yml"),
    Path("tools/oci/export_digest_to_oci.py"),
)


def text(root: Path, relative: Path) -> str:
    return (root / relative).read_text(encoding="utf-8")


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    missing = [str(path) for path in REQUIRED_PATHS if not (root / path).is_file()]
    if missing:
        return [f"required P2-VIS-001 artifact is missing: {path}" for path in missing]

    package = json.loads(text(root, PACKAGE))
    package_schema = json.loads(text(root, PACKAGE_SCHEMA))
    contract = json.loads(text(root, CONTRACT))
    contract_schema = json.loads(text(root, CONTRACT_SCHEMA))
    readiness = json.loads(text(root, READINESS))
    readiness_schema = json.loads(text(root, READINESS_SCHEMA))
    native_validation = json.loads(text(root, NATIVE_VALIDATION))
    native_validation_schema = json.loads(text(root, NATIVE_VALIDATION_SCHEMA))
    control_node_evidence_text = text(root, CONTROL_NODE_EVIDENCE)
    control_node_evidence = json.loads(control_node_evidence_text)
    control_node_provisioner = text(root, CONTROL_NODE_PROVISIONER)
    live_gate_discovery_text = text(root, LIVE_GATE_DISCOVERY)
    live_gate_discovery = json.loads(live_gate_discovery_text)
    live_gate_discovery_schema = json.loads(text(root, LIVE_GATE_DISCOVERY_SCHEMA))
    cinder_evidence_text = text(root, CINDER_EVIDENCE)
    cinder_evidence = json.loads(cinder_evidence_text)
    cinder_evidence_schema = json.loads(text(root, CINDER_EVIDENCE_SCHEMA))
    cinder_disk_provisioner = text(root, CINDER_DISK_PROVISIONER)
    external_input_initializer = text(root, EXTERNAL_INPUT_INITIALIZER)
    external_input_evidence_text = text(root, EXTERNAL_INPUT_EVIDENCE)
    external_input_evidence = json.loads(external_input_evidence_text)
    external_input_evidence_schema = json.loads(text(root, EXTERNAL_INPUT_EVIDENCE_SCHEMA))
    terraform_preflight_evidence_text = text(root, TERRAFORM_PREFLIGHT_EVIDENCE)
    terraform_preflight_evidence = json.loads(terraform_preflight_evidence_text)
    terraform_preflight_evidence_schema = json.loads(text(root, TERRAFORM_PREFLIGHT_EVIDENCE_SCHEMA))
    bounded_deployment_evidence_text = text(root, BOUNDED_DEPLOYMENT_EVIDENCE)
    bounded_deployment_evidence = json.loads(bounded_deployment_evidence_text)
    bounded_deployment_evidence_schema = json.loads(text(root, BOUNDED_DEPLOYMENT_EVIDENCE_SCHEMA))
    live_validation_evidence_text = text(root, LIVE_VALIDATION_EVIDENCE)
    live_validation_evidence = json.loads(live_validation_evidence_text)
    live_validation_evidence_schema = json.loads(text(root, LIVE_VALIDATION_EVIDENCE_SCHEMA))
    partial_promotion_decision_text = text(root, PARTIAL_PROMOTION_DECISION)
    partial_promotion_decision = json.loads(partial_promotion_decision_text)
    partial_promotion_decision_schema = json.loads(text(root, PARTIAL_PROMOTION_DECISION_SCHEMA))
    alert_validation_plan = json.loads(text(root, ALERT_VALIDATION_PLAN))
    alert_validation_plan_schema = json.loads(text(root, ALERT_VALIDATION_PLAN_SCHEMA))
    alert_validation_evidence_text = text(root, ALERT_VALIDATION_EVIDENCE)
    alert_validation_evidence = json.loads(alert_validation_evidence_text)
    alert_validation_evidence_schema = json.loads(text(root, ALERT_VALIDATION_EVIDENCE_SCHEMA))
    errors.extend(
        f"package schema: {item}"
        for item in validate_schema_instance(package, package_schema)
    )
    errors.extend(
        f"deployment contract schema: {item}"
        for item in validate_schema_instance(contract, contract_schema)
    )
    errors.extend(
        f"readiness contract schema: {item}"
        for item in validate_schema_instance(readiness, readiness_schema)
    )
    errors.extend(
        f"native validation schema: {item}"
        for item in validate_schema_instance(native_validation, native_validation_schema)
    )
    errors.extend(
        f"live-gate discovery schema: {item}"
        for item in validate_schema_instance(live_gate_discovery, live_gate_discovery_schema)
    )
    errors.extend(
        f"Cinder prerequisite schema: {item}"
        for item in validate_schema_instance(cinder_evidence, cinder_evidence_schema)
    )
    errors.extend(
        f"external-input readiness schema: {item}"
        for item in validate_schema_instance(external_input_evidence, external_input_evidence_schema)
    )
    errors.extend(
        f"Terraform preflight schema: {item}"
        for item in validate_schema_instance(terraform_preflight_evidence, terraform_preflight_evidence_schema)
    )
    errors.extend(
        f"bounded deployment evidence schema: {item}"
        for item in validate_schema_instance(bounded_deployment_evidence, bounded_deployment_evidence_schema)
    )
    errors.extend(
        f"live validation evidence schema: {item}"
        for item in validate_schema_instance(live_validation_evidence, live_validation_evidence_schema)
    )
    errors.extend(
        f"partial promotion decision schema: {item}"
        for item in validate_schema_instance(partial_promotion_decision, partial_promotion_decision_schema)
    )
    errors.extend(
        f"alert validation plan schema: {item}"
        for item in validate_schema_instance(alert_validation_plan, alert_validation_plan_schema)
    )
    errors.extend(
        f"alert validation evidence schema: {item}"
        for item in validate_schema_instance(alert_validation_evidence, alert_validation_evidence_schema)
    )
    module_main = text(root, TF_MODULE / "main.tf")
    module_versions = text(root, TF_MODULE / "versions.tf")
    environment = "\n".join(text(root, path) for path in (
        TF_ENV / "versions.tf", TF_ENV / "providers.tf", TF_ENV / "main.tf",
        TF_ENV / "variables.tf", TF_ENV / "outputs.tf", TF_ENV / "terraform.tfvars.example",
    ))
    provider_lock = text(root, TF_ENV / ".terraform.lock.hcl")
    defaults = text(root, ANSIBLE_ROLE / "defaults/main.yml")
    tasks = text(root, ANSIBLE_ROLE / "tasks/main.yml")
    handlers = text(root, ANSIBLE_ROLE / "handlers/main.yml")
    compose = text(root, ANSIBLE_ROLE / "templates/compose.yaml.j2")
    host_defaults = text(root, ANSIBLE_HOST_ROLE / "defaults/main.yml")
    host_tasks = text(root, ANSIBLE_HOST_ROLE / "tasks/main.yml")
    host_proxy = text(root, ANSIBLE_HOST_ROLE / "templates/nginx-zt-vis-002.conf.j2")
    oci_exporter = text(root, Path("tools/oci/export_digest_to_oci.py"))
    live_validator = text(root, LIVE_VALIDATOR)
    mtls_validator = text(root, MTLS_VALIDATOR)
    live_validation_playbook = text(root, LIVE_VALIDATION_PLAYBOOK)
    alert_validator = text(root, ALERT_VALIDATOR)
    alert_validation_playbook = text(root, ALERT_VALIDATION_PLAYBOOK)
    deploy = text(root, Path("ansible/playbooks/zt-vis-002-deploy.yml"))
    rollback = text(root, Path("ansible/playbooks/zt-vis-002-rollback.yml"))

    expected_resources = {
        "openstack_networking_port_v2",
        "openstack_compute_instance_v2",
        "openstack_blockstorage_volume_v3",
        "openstack_compute_volume_attach_v2",
    }
    resources = re.findall(r'resource\s+"([^"]+)"', module_main)
    if set(resources) != expected_resources or len(resources) != len(expected_resources):
        errors.append(f"Terraform module must contain exactly the four approved resource types, got {resources}")
    forbidden_terraform = (
        "openstack_networking_floatingip", "openstack_networking_network_v2",
        "openstack_networking_subnet_v2", "openstack_networking_router_v2",
        "openstack_networking_secgroup_v2", "openstack_identity_", "aws_", "azurerm_",
    )
    if any(token in module_main.lower() for token in forbidden_terraform):
        errors.append("Terraform module contains a forbidden public, network-creation, identity, or public-cloud resource")
    for token in ("port_security_enabled = true", "network_id            = var.network_id", 'Exposure         = "PRIVATE_ONLY"'):
        if token not in module_main:
            errors.append(f"Terraform private-network boundary is missing: {token}")
    if 'version = "~> 3.4.0"' not in module_versions or 'source  = "terraform-provider-openstack/openstack"' not in module_versions:
        errors.append("Terraform OpenStack provider source and reviewed version constraint must be fixed")
    if (
        'provider "registry.terraform.io/terraform-provider-openstack/openstack"' not in provider_lock
        or 'version     = "3.4.0"' not in provider_lock
        or provider_lock.count('"h1:') < 2
        or provider_lock.count('"zh:') < 10
    ):
        errors.append("Terraform provider lock must pin OpenStack v3.4.0 with Linux, Windows, and registry checksums")
    if "cloud  = var.openstack_cloud" not in environment or "terraform.tfstate" in environment:
        errors.append("Terraform environment must use external clouds.yaml resolution and must not declare tracked state")
    if any(token in environment.lower() for token in ("password =", "token =", "auth_url =", "application_credential_secret")):
        errors.append("Terraform example must not contain credential fields or account endpoints")

    for token in (
        "zt_vis_002_deployment_authorized: false",
        "zt_vis_002_authenticated_proxy_ready: false",
        "zt_vis_002_proxy_trust_material_ready: false",
        "zt_vis_002_data_mount_ready: false",
        "zt_vis_002_restore_checkpoint_ready: false",
    ):
        if token not in defaults:
            errors.append(f"Ansible fail-closed default is missing: {token}")
    if (
        "repository@sha256" not in tasks
        or "Stage reviewed OCI image archives" not in tasks
        or "Load reviewed OCI image archives without registry access" not in tasks
        or "Verify every reviewed image digest in local storage" not in tasks
        or tasks.count("no_log: true") < 2
    ):
        errors.append("Ansible role must enforce digest-pinned images and suppress secret-bearing task output")
    if (
        "Enable root Podman restart-policy restoration" not in tasks
        or "name: podman-restart.service" not in tasks
        or "enabled: true" not in tasks
        or "Ensure the reviewed package-owned Compose project is running" not in tasks
    ):
        errors.append("Ansible role must enable Podman reboot restoration and enforce the reviewed running state")
    if (
        "zt_vis_002_host_bootstrap_authorized: false" not in host_defaults
        or "zt_vis_002_data_device_expected_size_gib: 0" not in host_defaults
        or "zt_vis_002_mountpoint.rc not in [0, 32]" not in host_tasks
        or "zt_vis_002_mountpoint.rc == 32" not in host_tasks
        or '"FSTYPE,OPTIONS"' not in host_tasks
        or "difference([zt_vis_002_root])" not in host_tasks
    ):
        errors.append("Host bootstrap must default-deny and preserve exact, idempotent dedicated-volume checks")
    if (
        "ssl_verify_client on;" not in host_proxy
        or "listen {{ zt_vis_002_proxy_bind_address }}:443 ssl;" not in host_proxy
        or "proxy_pass http://127.0.0.1:3000;" not in host_proxy
    ):
        errors.append("Host proxy must require mTLS, use the approved private listener, and forward only to loopback Grafana")
    if 'mode: "0644"' not in tasks or tasks.count('mode: "0755"') < 3 or compose.count(':U"') < 4:
        errors.append("Non-secret container configuration must be readable while writable data mounts retain Podman ownership mapping")
    if "docker-content-digest" not in oci_exporter or "linux" not in oci_exporter or "amd64" not in oci_exporter:
        errors.append("OCI exporter must verify registry digests and preserve the reviewed Linux AMD64 platform boundary")
    required_live_tokens = (
        "ZT_VIS_002_LIVE_VALIDATION_AUTHORIZED",
        "positive=PASS",
        "bypass=PASS",
        "evidence_integrity=PASS",
        "rollback=PASS",
        "persistence|recovery)",
        "printf '%s=PASS",
        "ext4",
        "nodev",
        "nosuid",
        "127.0.0.1:3000",
        "configuration_sha256=",
    )
    if any(token not in live_validator for token in required_live_tokens):
        errors.append("Live validator must retain fail-closed positive, bypass, persistence, rollback, recovery, storage, and configuration-integrity checks")
    if (
        "socket.socketpair()" not in mtls_validator
        or "mtls_without_client" not in mtls_validator
        or "mtls_with_approved_client" not in mtls_validator
        or "grafana_false_basic" not in mtls_validator
        or "StrictHostKeyChecking=yes" not in mtls_validator
        or "shutil.copy" in mtls_validator
    ):
        errors.append("mTLS validator must keep client keys on the controller and test certificate and Grafana authentication denial")
    required_campaign_tokens = (
        "zt_vis_002_live_validation_authorized: false",
        "zt_vis_002_persistence_restart_authorized: false",
        "zt_vis_002_rollback_validation_authorized: false",
        "zt_vis_002_recovery_authorized: false",
        "ansible.builtin.reboot",
        "Record that bounded rollback has started",
        "Best-effort recovery when failure occurred after bounded rollback",
        "Remove the temporary target validator",
    )
    if any(token not in live_validation_playbook for token in required_campaign_tokens):
        errors.append("Live-validation playbook must default-deny restart, rollback, and recovery and retain failure recovery and cleanup")
    reviewed_images = {
        "grafana": "docker.io/grafana/grafana@sha256:6ea068891652aa6a65ca9065c26b89de939653803c836426970305c11fd00534",
        "loki": "docker.io/grafana/loki@sha256:ac6ad1d73bd4c3c38edc93f91ebc217672fa657c20a5dc7b4b0e25baeec7bebb",
        "alloy": "docker.io/grafana/alloy@sha256:eb21f4c0858edffcdd1b385910ddeef26f692fc2c282f61baa724fc09d274a17",
        "prometheus": "docker.io/prom/prometheus@sha256:2024d7bdfc559f6254de22d65e62d799eaa8eb818fe5dbeca212d3f200b70890",
        "blackbox": "docker.io/prom/blackbox-exporter@sha256:43027b43fb785b7c5adc53bd3b5dbc1a258270a2e8aff24f477b45c4e38dac68",
    }
    for component, image in reviewed_images.items():
        if f'{component}: "{image}"' not in defaults or f"zt_vis_002_images.{component} == '{image}'" not in tasks:
            errors.append(f"Ansible must default to and enforce the reviewed {component} Linux AMD64 manifest")
    readiness_images = {
        item.get("component"): item.get("runtime_reference")
        for item in readiness.get("artifact_policy", {}).get("images", [])
    }
    expected_readiness_images = {
        "Grafana": reviewed_images["grafana"],
        "Loki": reviewed_images["loki"],
        "Alloy": reviewed_images["alloy"],
        "Prometheus": reviewed_images["prometheus"],
        "Blackbox Exporter": reviewed_images["blackbox"],
    }
    if readiness_images != expected_readiness_images:
        errors.append("Readiness contract and Ansible must use the same five reviewed Linux AMD64 manifests")
    expected_image_metadata = {
        "Grafana": ("13.1.0", "docker.io/grafana/grafana:13.1.0"),
        "Loki": ("3.7.0", "docker.io/grafana/loki:3.7.0"),
        "Alloy": ("v1.18.0", "docker.io/grafana/alloy:v1.18.0"),
        "Prometheus": ("v3.9.1", "docker.io/prom/prometheus:v3.9.1"),
        "Blackbox Exporter": ("v0.28.0", "docker.io/prom/blackbox-exporter:v0.28.0"),
    }
    actual_image_metadata = {
        item.get("component"): (item.get("version"), item.get("tag_reference"))
        for item in readiness.get("artifact_policy", {}).get("images", [])
    }
    if actual_image_metadata != expected_image_metadata:
        errors.append("Readiness contract image versions and source tags must match the reviewed manifest resolution")
    artifact_policy = readiness.get("artifact_policy", {})
    if (
        artifact_policy.get("decision") != "LOCAL_SELECTION_VALIDATED"
        or artifact_policy.get("tag_only_allowed") is not False
        or artifact_policy.get("mutable_fallback_allowed") is not False
        or artifact_policy.get("pre_deploy_registry_revalidation_required") is not True
        or artifact_policy.get("signature_verified") is not False
        or artifact_policy.get("vulnerability_assessed") is not False
    ):
        errors.append("Artifact policy must pin manifests, require pre-deploy revalidation, and avoid signature or vulnerability overclaims")
    access_policy = readiness.get("access_policy", {})
    role_map = {item.get("role"): item for item in access_policy.get("roles", [])}
    if (
        access_policy.get("authentication") != "MUTUAL_TLS_AT_PROXY_PLUS_GRAFANA_LOGIN"
        or access_policy.get("anonymous_access_allowed") is not False
        or access_policy.get("direct_service_access_allowed") is not False
        or set(role_map) != {"VISIBILITY_VIEWER", "VISIBILITY_ADMINISTRATOR", "RECOVERY_OPERATOR"}
        or role_map.get("RECOVERY_OPERATOR", {}).get("host_recovery_allowed") is not True
        or any(role_map.get(role, {}).get("host_recovery_allowed") is not False for role in ("VISIBILITY_VIEWER", "VISIBILITY_ADMINISTRATOR"))
    ):
        errors.append("Access policy must preserve private mTLS, deny direct/anonymous access, and separate viewer, administrator, and recovery roles")
    retention = readiness.get("retention_restore_policy", {})
    if (
        retention.get("retention") != "PT336H"
        or retention.get("primary_storage") != "DEDICATED_CINDER_VOLUME"
        or retention.get("recovery_method") != "REATTACH_PRESERVED_VOLUME_TO_REBUILT_MONITORING_VM"
        or retention.get("rollback_checkpoint") != "CINDER_SNAPSHOT_BEFORE_BOUNDED_DEPLOYMENT_TEST"
        or retention.get("independent_backup_backend") != "NONE_APPROVED"
        or retention.get("retention_runtime_accepted") is not False
        or retention.get("restore_runtime_accepted") is not False
        or retention.get("rpo") != "NOT_CLAIMED"
        or retention.get("rto") != "NOT_CLAIMED"
    ):
        errors.append("Retention and restore policy must keep the bounded Cinder design and all runtime, backup, RPO, and RTO claims open")
    if any(readiness.get(key) is not False for key in (
        "runtime_executed", "central_monitoring_completed", "package_runtime_promoted",
        "maturity_assessed", "compliance_assessed",
    )):
        errors.append("Readiness contract cannot claim runtime, completion, promotion, maturity, or compliance")
    forbidden_ansible = ("ansible.builtin.shell", "ansible.builtin.get_url", "ansible.builtin.uri", "ansible.builtin.package", "ansible.builtin.apt", "ansible.builtin.dnf")
    if any(token in tasks or token in handlers for token in forbidden_ansible):
        errors.append("Ansible role must not use shell, downloads, network APIs, or package installation")
    if "role: ../roles/zt_vis_002" not in deploy:
        errors.append("Ansible deploy playbook must use the repository-relative role path")
    services_block = compose.split("services:\n", 1)[-1].split("\nnetworks:\n", 1)[0]
    services = set(re.findall(r"^  ([a-z]+):$", services_block, flags=re.MULTILINE))
    if services != {"grafana", "loki", "alloy", "prometheus", "blackbox"}:
        errors.append(f"Compose template must contain exactly the fixed five services, got {sorted(services)}")
    if compose.count("restart: always") != 5 or "restart: unless-stopped" in compose:
        errors.append("Every visibility component must use the Podman-compatible always reboot policy")
    port_lines = [line.strip() for line in compose.splitlines() if line.strip().startswith("ports:")]
    if len(port_lines) != 5 or any('127.0.0.1:' not in line for line in port_lines):
        errors.append("Every visibility host port must bind to loopback")
    for token in ("GF_AUTH_ANONYMOUS_ENABLED: \"false\"", "GF_SECURITY_COOKIE_SECURE: \"true\"", "no-new-privileges=true", "cap_drop: [\"ALL\"]"):
        if token not in compose:
            errors.append(f"Compose security boundary is missing: {token}")
    if "zt_vis_002_rollback_authorized: false" not in rollback or "- down" not in rollback:
        errors.append("Rollback must default-deny and stop only the bounded Compose project")
    if any(token in rollback for token in ("state: absent", "rm -", "openstack ", "terraform destroy")):
        errors.append("Rollback playbook must preserve VM, data, configuration, and secrets")

    required_control_node_tokens = (
        'b9dc4dea4bdb09c1e08e40cce34fbd3d8fe252ff71bd9be979ef8b15256d80e8',
        'ethernet0.connectionType = "nat"',
        'ethernet1.vnet = "VMnet1"',
        'sharedFolder.maxNum = "0"',
        'ssh_pwauth: false',
        'PasswordAuthentication no',
        'PermitRootLogin no',
        'AllowUsers ztansible',
        'ufw, default, deny, incoming',
    )
    if any(token not in control_node_provisioner for token in required_control_node_tokens):
        errors.append("VMware control-node provisioner is missing an image, network, SSH, sharing, or firewall boundary")
    if any(token in control_node_provisioner for token in ('connectionType = "bridged"', 'ssh_pwauth: true', 'PasswordAuthentication yes', 'NOPASSWD:ALL')):
        errors.append("VMware control-node provisioner contains a public, password, or unrestricted-sudo boundary")
    if re.search(r"(?:\d{1,3}\.){3}\d{1,3}", control_node_evidence_text) or re.search(r"[0-9a-fA-F]{2}(?::[0-9a-fA-F]{2}){5}", control_node_evidence_text):
        errors.append("Sanitized control-node evidence must not contain DHCP or MAC addresses")
    if control_node_evidence.get("sanitization_status") != "PASS" or control_node_evidence.get("control_node", {}).get("wsl_control_node_used") is not False:
        errors.append("Control-node evidence must be sanitized and must not retain WSL as an active authority")
    if any(control_node_evidence.get("package_runtime", {}).get(key) is not False for key in (
        "openstack_inventory_created", "openstack_credentials_loaded", "terraform_plan_created",
        "terraform_apply_executed", "ansible_deploy_playbook_executed",
        "ansible_rollback_playbook_executed", "protected_openstack_target_changed",
        "central_monitoring_completed", "package_runtime_promoted",
    )):
        errors.append("Control-node evidence cannot claim OpenStack or package runtime execution")

    sensitive_runtime_patterns = (
        r"(?:\d{1,3}\.){3}\d{1,3}",
        r"[0-9a-fA-F]{2}(?::[0-9a-fA-F]{2}){5}",
        r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b",
        r"\b[0-9a-fA-F]{32}\b",
    )
    if any(re.search(pattern, live_gate_discovery_text) for pattern in sensitive_runtime_patterns):
        errors.append("Sanitized live-gate discovery must not contain addresses, MACs, resource IDs, or project IDs")
    service_catalog = live_gate_discovery.get("findings", {}).get("service_catalog", {})
    terraform_controller = live_gate_discovery.get("findings", {}).get("terraform_controller", {})
    if (
        live_gate_discovery.get("decision") != "NO_GO_LIVE_DEPLOYMENT"
        or service_catalog.get("block_storage") is not False
        or service_catalog.get("volume_v3_endpoint") is not False
        or terraform_controller.get("external_cloud_profile") != "ABSENT"
    ):
        errors.append("Live-gate discovery must preserve the Cinder and external-cloud-profile blockers")
    if any(live_gate_discovery.get(key) is not False for key in (
        "raw_output_committed", "credential_material_exposed", "live_target_changed",
        "terraform_plan_created", "terraform_apply_executed", "ansible_playbook_executed",
    )):
        errors.append("Live-gate discovery cannot claim raw evidence, credentials, plan, apply, playbook, or target mutation")

    if any(re.search(pattern, cinder_evidence_text) for pattern in sensitive_runtime_patterns):
        errors.append("Sanitized Cinder prerequisite evidence must not contain addresses, MACs, resource IDs, or project IDs")
    cinder_change = cinder_evidence.get("change_scope", {})
    cinder_validation = cinder_evidence.get("validation", {})
    cinder_boundary = cinder_evidence.get("package_boundary", {})
    if (
        cinder_evidence.get("decision") != "CINDER_PREREQUISITE_ACCEPTED_CENTRAL_DEPLOYMENT_NO_GO"
        or cinder_change.get("dedicated_virtual_disk_size_gb") != 100
        or cinder_change.get("reviewed_scsi_slot") != "SCSI_0_2"
        or cinder_change.get("existing_nova_instance_storage_preserved") is not True
        or cinder_validation.get("positive") != "TEMPORARY_1_GIB_VOLUME_AVAILABLE_WITH_BACKEND_LV_PASS"
        or cinder_validation.get("persistence") != "AIO_REBOOT_DEVICE_VG_SERVICES_VOLUME_AND_BACKEND_LV_PASS"
        or cinder_validation.get("rollback") != "TEMPORARY_VOLUME_REMOVED_OPENSTACK_ZERO_BACKEND_LV_ZERO_PASS"
    ):
        errors.append("Cinder prerequisite evidence must preserve the dedicated-disk and bounded validation result")
    if any(cinder_boundary.get(key) is not False for key in (
        "package_runtime_executed", "terraform_plan_created", "terraform_apply_executed",
        "ansible_visibility_playbook_executed", "central_monitoring_completed",
        "package_runtime_promoted", "maturity_assessed", "compliance_assessed",
    )):
        errors.append("Cinder prerequisite evidence cannot claim visibility runtime, Terraform, playbook, promotion, maturity, or compliance")
    required_cinder_provisioner_tokens = (
        "[ValidateRange(40, 200)]",
        "[int]$DiskSizeGb = 100",
        "$running -contains $resolvedVmx",
        "scsi0:2.present",
        "SNSD-OpenStack-AIO-cinder.vmdk",
        "VMX backup retained",
        "-t 0 $diskPath",
    )
    if any(token not in cinder_disk_provisioner for token in required_cinder_provisioner_tokens):
        errors.append("Cinder disk provisioner is missing an exact path, stopped-VM, slot, size, thin-disk, or backup boundary")
    if any(token in cinder_disk_provisioner for token in ("Remove-Item -Recurse", "scsi0:3.present", "$HOME", "$env:HOME")):
        errors.append("Cinder disk provisioner contains an unsafe recursive, alternate-slot, or broad-home operation")
    required_external_input_tokens = (
        'readonly external_root="${HOME}/.config/snsd/zt-vis-002"',
        'umask 077',
        'PRESENT_VERIFIED',
        'openssl verify',
        '-checkhost zt-vis-002-monitoring.lab.internal',
        "install_stream",
        "install-cloud-profile",
        "install-tfvars",
        "chmod 0600",
        "refusing unsafe cleanup path",
    )
    if any(token not in external_input_initializer for token in required_external_input_tokens):
        errors.append("External-input initializer is missing a fixed path, permission, certificate, stream, or cleanup boundary")
    if any(token in external_input_initializer for token in ("curl ", "wget ", "terraform plan", "terraform apply", "ansible-playbook", "/etc/kolla/clouds.yaml")):
        errors.append("External-input initializer must not download, plan, apply, deploy, or embed the OpenStack source path")
    if any(re.search(pattern, external_input_evidence_text) for pattern in sensitive_runtime_patterns):
        errors.append("Sanitized external-input evidence must not contain addresses, MACs, resource IDs, or project IDs")
    external_authorization = external_input_evidence.get("authorization", {})
    external_cloud = external_input_evidence.get("cloud_profile", {})
    external_tfvars = external_input_evidence.get("terraform_inputs", {})
    external_trust = external_input_evidence.get("proxy_trust_material", {})
    external_boundary = external_input_evidence.get("execution_boundary", {})
    external_cleanup = external_input_evidence.get("cleanup", {})
    if (
        external_input_evidence.get("decision") != "EXTERNAL_INPUTS_AND_LOCAL_TRUST_MATERIAL_READY_LIVE_DEPLOYMENT_NO_GO"
        or external_authorization.get("administrator_profile_transfer") != "EXPLICIT_USER_APPROVAL"
        or external_authorization.get("live_deployment_authorized") is not False
        or external_authorization.get("live_validator_authorized") is not False
        or external_cloud.get("source_target_sha256_match") is not True
        or external_cloud.get("file_mode") != "0600"
        or external_cloud.get("authentication_attempted_from_control_node") is not False
        or external_cloud.get("credential_value_recorded") is not False
        or external_tfvars.get("rendered_hash_matches_selection") is not True
        or external_tfvars.get("placeholder_count") != 0
        or external_tfvars.get("credential_field_count") != 0
        or external_tfvars.get("file_mode") != "0600"
    ):
        errors.append("External-input evidence must preserve explicit transfer authorization, exact protected inputs, and no control-node authentication claim")
    if (
        external_trust.get("certificate_chain_verification") != "PASS"
        or external_trust.get("server_name_verification") != "PASS"
        or external_trust.get("private_key_file_mode") != "0600"
        or external_trust.get("proxy_runtime_verified") is not False
        or external_cleanup.get("local_intermediate_credential_file_created") is not False
        or external_cleanup.get("temporary_control_script_present") is not False
        or external_cleanup.get("repository_secret_material_created") is not False
        or external_cleanup.get("tracked_runtime_created") is not False
    ):
        errors.append("External-input evidence must preserve verified local trust material, cleanup, and the unverified proxy runtime boundary")
    if any(external_boundary.get(key) is not False for key in (
        "protected_openstack_target_changed", "terraform_plan_created", "terraform_apply_executed",
        "ansible_playbook_executed", "image_pull_executed", "central_monitoring_completed",
        "package_runtime_promoted", "maturity_assessed", "compliance_assessed",
    )):
        errors.append("External-input readiness cannot claim target mutation, plan, apply, deployment, completion, promotion, maturity, or compliance")

    if any(re.search(pattern, terraform_preflight_evidence_text) for pattern in sensitive_runtime_patterns):
        errors.append("Sanitized Terraform preflight evidence must not contain addresses, MACs, resource IDs, or project IDs")
    preflight_authorization = terraform_preflight_evidence.get("authorization", {})
    terraform_cli = terraform_preflight_evidence.get("terraform_cli", {})
    provider_lock_evidence = terraform_preflight_evidence.get("provider_lock", {})
    preflight = terraform_preflight_evidence.get("preflight", {})
    plan_review = terraform_preflight_evidence.get("plan_review", {})
    preflight_boundary = terraform_preflight_evidence.get("execution_boundary", {})
    expected_plan_changes = {
        ("openstack_networking_port_v2", "create", 1),
        ("openstack_compute_instance_v2", "create", 1),
        ("openstack_blockstorage_volume_v3", "create", 1),
        ("openstack_compute_volume_attach_v2", "create", 1),
    }
    actual_plan_changes = {
        (item.get("resource_type"), item.get("action"), item.get("count"))
        for item in plan_review.get("expected_changes", [])
    }
    if (
        terraform_preflight_evidence.get("decision") != "NO_APPLY_PLAN_ACCEPTED_LIVE_DEPLOYMENT_STILL_NO_GO"
        or preflight_authorization.get("instruction") != "EXPLICIT_NEXT_TASK_APPROVAL_AFTER_SCOPE_DISCLOSURE"
        or preflight_authorization.get("terraform_apply_authorized") is not False
        or preflight_authorization.get("ansible_deployment_authorized") is not False
        or preflight_authorization.get("live_validator_authorized") is not False
        or terraform_cli.get("version") != "1.15.8"
        or terraform_cli.get("signature_verification") != "PASS"
        or terraform_cli.get("archive_sha256_verification") != "PASS"
        or provider_lock_evidence.get("version") != "3.4.0"
        or provider_lock_evidence.get("linux_amd64_hash_added") is not True
        or provider_lock_evidence.get("provider_version_changed") is not False
    ):
        errors.append("Terraform preflight must preserve the reviewed CLI, provider lock, explicit no-apply authorization, and NO-GO decision")
    if (
        preflight.get("terraform_init") != "PASS"
        or preflight.get("terraform_validate") != "PASS"
        or preflight.get("openstack_authentication_via_provider") != "PASS"
        or preflight.get("terraform_plan") != "PASS"
        or preflight.get("terraform_show_json") != "PASS"
        or preflight.get("backend_initialization") != "DISABLED"
        or preflight.get("refresh_enabled") is not False
        or preflight.get("state_lock_enabled") is not False
        or preflight.get("raw_plan_file_mode") != "0600"
        or preflight.get("raw_plan_transferred_to_repository") is not False
    ):
        errors.append("Terraform preflight must record a protected backend-disabled no-apply plan without importing raw plan data")
    if (
        actual_plan_changes != expected_plan_changes
        or len(plan_review.get("expected_changes", [])) != 4
        or plan_review.get("prior_resource_count") != 0
        or plan_review.get("resource_change_count") != 4
        or plan_review.get("destructive_action_count") != 0
        or plan_review.get("policy_decision") != "PASS"
        or plan_review.get("raw_values_recorded") is not False
    ):
        errors.append("Terraform plan review must contain exactly four create actions, no prior resources, and no destructive or raw-value claim")
    if (
        preflight_boundary.get("openstack_read_only_provider_calls_executed") is not True
        or preflight_boundary.get("terraform_plan_created") is not True
        or preflight_boundary.get("terraform_state_file_count") != 0
        or any(preflight_boundary.get(key) is not False for key in (
            "terraform_apply_executed", "ansible_playbook_executed", "image_pull_executed",
            "protected_openstack_target_changed", "central_monitoring_completed",
            "package_runtime_promoted", "maturity_assessed", "compliance_assessed",
        ))
    ):
        errors.append("Terraform preflight must distinguish provider read-only calls and plan creation from target mutation or runtime execution")

    if any(re.search(pattern, bounded_deployment_evidence_text) for pattern in sensitive_runtime_patterns):
        errors.append("Sanitized bounded deployment evidence must not contain addresses, MACs, resource IDs, or project IDs")
    deployment_authorization = bounded_deployment_evidence.get("authorization", {})
    deployment_terraform = bounded_deployment_evidence.get("terraform", {})
    recovery_plan = deployment_terraform.get("recovery_plan_review", {})
    deployment_ansible = bounded_deployment_evidence.get("ansible", {})
    deployment_boundary = bounded_deployment_evidence.get("validation_boundary", {})
    if (
        bounded_deployment_evidence.get("sanitization_status") != "PASS"
        or deployment_authorization.get("terraform_apply_authorized") is not True
        or deployment_authorization.get("ansible_deployment_authorized") is not True
        or deployment_authorization.get("bounded_deployment_checks_authorized") is not True
        or deployment_authorization.get("live_validator_authorized") is not False
        or deployment_authorization.get("rollback_authorized") is not False
        or deployment_authorization.get("package_status_promotion_authorized") is not False
    ):
        errors.append("Bounded deployment evidence must preserve apply authorization and the separate validator, rollback, and promotion boundaries")
    if (
        deployment_terraform.get("initial_apply_result") != "PARTIAL_FAILURE_INVALID_FLAVOR_REFERENCE"
        or deployment_terraform.get("apply_result") != "PASS"
        or deployment_terraform.get("final_resource_count") != 4
        or set(deployment_terraform.get("resource_types", [])) != expected_resources
        or recovery_plan.get("prior_resource_count") != 2
        or recovery_plan.get("create_count") != 2
        or recovery_plan.get("no_op_count") != 2
        or recovery_plan.get("destructive_action_count") != 0
        or recovery_plan.get("policy_decision") != "PASS"
        or deployment_terraform.get("tracked_state_created") is not False
        or deployment_terraform.get("floating_ip_created") is not False
        or deployment_terraform.get("public_endpoint_created") is not False
    ):
        errors.append("Bounded Terraform evidence must record the reviewed recovery apply, four private resources, protected external state, and no destructive or public resource")
    if (
        deployment_ansible.get("host_bootstrap") != "PASS"
        or deployment_ansible.get("service_deployment") != "PASS"
        or deployment_ansible.get("offline_oci_archives_verified") != 5
        or deployment_ansible.get("target_registry_access_used") is not False
        or deployment_ansible.get("running_component_count") != 5
        or deployment_ansible.get("component_health_endpoints") != "PASS"
        or deployment_ansible.get("dedicated_mount") != "EXT4_NODEV_NOSUID_PASS"
        or deployment_ansible.get("component_listener_scope") != "LOOPBACK_ONLY_PASS"
        or deployment_ansible.get("proxy_listener_scope") != "PRIVATE_ADDRESS_ONLY_PASS"
        or deployment_ansible.get("mtls_without_client") != "REJECTED"
        or deployment_ansible.get("mtls_with_approved_client") != "PASS"
        or deployment_ansible.get("temporary_access_cleanup") != "PASS"
        or deployment_ansible.get("repository_private_key_created") is not False
        or deployment_ansible.get("raw_runtime_output_tracked") is not False
    ):
        errors.append("Bounded Ansible evidence must preserve offline artifacts, five healthy private services, mTLS enforcement, and temporary-access cleanup")
    if (
        bounded_deployment_evidence.get("decision") != "DEPLOYMENT_EXECUTED_LIVE_VALIDATOR_AND_STATUS_PROMOTION_PENDING"
        or deployment_boundary.get("evidence_scope") != "BOUNDED_DEPLOYMENT_OBSERVATION_ONLY"
        or deployment_boundary.get("runtime_executed") is not True
        or deployment_boundary.get("protected_openstack_target_changed") is not True
        or deployment_boundary.get("full_live_validator_executed") is not False
        or any(deployment_boundary.get(key) != "NOT_RUN" for key in (
            "positive_acceptance_case", "negative_acceptance_case", "bypass_acceptance_case",
            "persistence_acceptance_case", "rollback_acceptance_case",
        ))
        or any(deployment_boundary.get(key) is not False for key in (
            "central_monitoring_completed", "package_runtime_promoted", "maturity_assessed", "compliance_assessed",
        ))
    ):
        errors.append("Bounded deployment evidence must not claim the separate live validator, acceptance cases, package promotion, completion, maturity, or compliance")

    if any(re.search(pattern, live_validation_evidence_text) for pattern in sensitive_runtime_patterns):
        errors.append("Sanitized live validation evidence must not contain addresses, MACs, resource IDs, or project IDs")
    live_authorization = live_validation_evidence.get("authorization", {})
    live_attempts = live_validation_evidence.get("execution_attempts", [])
    live_infrastructure = live_validation_evidence.get("infrastructure", {})
    live_integrity = live_validation_evidence.get("integrity", {})
    live_cleanup = live_validation_evidence.get("cleanup", {})
    live_boundary = live_validation_evidence.get("package_boundary", {})
    if (
        live_validation_evidence.get("sanitization_status") != "PASS"
        or any(live_authorization.get(key) is not True for key in (
            "live_validator_authorized", "target_restart_authorized",
            "stack_rollback_authorized", "stack_recovery_authorized",
        ))
        or live_authorization.get("package_status_promotion_authorized") is not False
    ):
        errors.append("Live validation evidence must preserve explicit live, restart, rollback, and recovery authorization without package-promotion authority")
    if (
        len(live_attempts) != 2
        or live_attempts[0].get("attempt") != 1
        or live_attempts[0].get("accepted") is not False
        or live_attempts[0].get("result") != "FAILED_REBOOT_CONTROL_CHANNEL_REMEDIATED"
        or len(live_attempts[0].get("findings", [])) < 2
        or live_attempts[1].get("attempt") != 2
        or live_attempts[1].get("accepted") is not True
        or live_attempts[1].get("result") != "PASS"
        or len(live_attempts[1].get("remediations", [])) < 4
    ):
        errors.append("Live validation evidence must transparently retain the rejected first attempt, remediation, and accepted second PASS")
    expected_live_cases = {
        "POSITIVE", "NEGATIVE", "BYPASS", "PERSISTENCE",
        "ROLLBACK", "EVIDENCE_INTEGRITY", "RECOVERY",
    }
    live_cases = live_validation_evidence.get("acceptance_cases", [])
    if (
        {item.get("case_type") for item in live_cases} != expected_live_cases
        or len(live_cases) != len(expected_live_cases)
        or any(item.get("result") != "PASS" for item in live_cases)
    ):
        errors.append("Live validation evidence must record exactly seven accepted positive, denial, persistence, rollback, integrity, and recovery cases")
    if (
        live_infrastructure.get("terraform_resource_count") != 4
        or live_infrastructure.get("instance_status") != "ACTIVE"
        or live_infrastructure.get("port_status") != "ACTIVE"
        or live_infrastructure.get("volume_status") != "IN_USE"
        or live_infrastructure.get("floating_ip_count") != 0
        or live_infrastructure.get("running_component_count") != 5
        or live_infrastructure.get("fixed_image_count") != 5
        or live_infrastructure.get("dedicated_mount") != "EXT4_NODEV_NOSUID_PASS"
        or live_infrastructure.get("public_endpoint_created") is not False
    ):
        errors.append("Live validation evidence must preserve the exact private four-resource, five-component runtime baseline")
    if (
        live_integrity.get("synthetic_record_count") != 1
        or live_integrity.get("forbidden_field_scan") != "PASS"
        or any(live_integrity.get(key) != "PASS" for key in (
            "baseline_positive_hash_match", "persistence_hash_match",
            "rollback_preservation_hash_match", "recovery_hash_match",
        ))
    ):
        errors.append("Live validation evidence must retain the single sanitized record and all configuration-integrity comparisons")
    required_cleanup = (
        "target_temporary_key_removed", "target_validator_removed",
        "target_synthetic_input_removed", "aio_forced_proxy_removed",
        "aio_sudoers_rule_removed", "controller_private_keys_removed",
        "controller_temporary_inventory_removed", "protected_state_preserved",
        "protected_pki_preserved", "protected_oci_archives_preserved",
        "external_raw_log_preserved",
    )
    if any(live_cleanup.get(key) is not True for key in required_cleanup):
        errors.append("Live validation evidence must record complete temporary-access cleanup and protected-artifact preservation")
    if (
        live_validation_evidence.get("decision") != "LIVE_VALIDATOR_EXECUTED_STATUS_PROMOTION_PENDING"
        or any(live_boundary.get(key) is not False for key in (
            "package_runtime_promoted", "central_monitoring_completed",
            "full_cinder_snapshot_restore_executed", "scheduled_or_continuous_validation",
            "maturity_assessed", "compliance_assessed", "production_readiness_claimed",
        ))
    ):
        errors.append("Live validation evidence must withhold package promotion, full snapshot restore, monitoring completion, scheduling, maturity, compliance, and production claims")
    for artifact in live_validation_evidence.get("source_artifacts", []):
        relative = Path(artifact.get("path", ""))
        candidate = root / relative
        actual = hashlib.sha256(candidate.read_bytes()).hexdigest() if candidate.is_file() else None
        if actual != artifact.get("sha256"):
            errors.append(f"Live validation source hash mismatch: {relative}")

    if any(re.search(pattern, partial_promotion_decision_text) for pattern in sensitive_runtime_patterns):
        errors.append("Sanitized partial promotion decision must not contain addresses, MACs, resource IDs, or project IDs")
    promoted = partial_promotion_decision.get("promoted_status", {})
    promotion_boundary = partial_promotion_decision.get("claim_boundary", {})
    expected_promotion = {
        "planning_status": "IN_PROGRESS",
        "implementation_status": "PARTIALLY_IMPLEMENTED",
        "local_validation_status": "LOCAL_VALIDATED",
        "runtime_validation_status": "PARTIALLY_VALIDATED",
        "runtime_acceptance_status": "PARTIALLY_ACCEPTED",
        "evidence_status": "PARTIAL_RUNTIME_RECORDED",
        "maturity_status": "UNASSESSED",
        "compliance_status": "NOT_ASSESSED",
    }
    expected_open_gaps = {
        "FULL_CINDER_SNAPSHOT_REBUILD_AND_REATTACH_RESTORE",
        "ALERT_RULE_AND_NOTIFICATION_DELIVERY_RUNTIME_VALIDATION",
        "RETENTION_WINDOW_ELAPSED_BEHAVIOR_VALIDATION",
    }
    decision_source = partial_promotion_decision.get("source_evidence", {})
    actual_live_hash = hashlib.sha256((root / LIVE_VALIDATION_EVIDENCE).read_bytes()).hexdigest()
    if (
        partial_promotion_decision.get("decision") != "PARTIAL_RUNTIME_STATUS_PROMOTED_WITH_OPEN_GAPS"
        or promoted != expected_promotion
        or set(partial_promotion_decision.get("open_gaps", [])) != expected_open_gaps
        or decision_source.get("path") != str(LIVE_VALIDATION_EVIDENCE).replace("\\", "/")
        or decision_source.get("sha256") != actual_live_hash
        or decision_source.get("accepted_result") != "PASS"
        or decision_source.get("evidence_continuity") != "EC3_ONE_TIME_RUNTIME"
    ):
        errors.append("Partial promotion must be hash-bound to the accepted one-time evidence and retain all three open gaps")
    if any(promotion_boundary.get(key) is not False for key in (
        "p2_vis_001_completed", "central_visibility_fully_accepted", "phase_2_completed",
        "oidc_or_central_identity_implemented", "scheduled_or_continuous_validation",
        "maturity_assessed", "compliance_assessed", "production_readiness_claimed",
    )):
        errors.append("Partial promotion cannot claim package completion, full acceptance, Phase 2 completion, identity, scheduling, maturity, compliance, or production readiness")

    required_authorities = {
        "docs/adr/0015-use-vmware-ansible-control-node.md",
        "docs/adr/0016-enable-dedicated-cinder-lvm-prerequisite.md",
        "docs/adr/0017-fix-phase-2-visibility-deployment-readiness.md",
        "docs/zero-trust/phase-2-visibility-deployment-contract.yaml",
        "docs/zero-trust/phase-2-visibility-readiness-contract.yaml",
        "docs/zero-trust/phase-2-visibility-native-validation.yaml",
        "docs/zero-trust/phase-2-visibility-alert-validation-plan.yaml",
        "docs/evidence/zero-trust/zt-vis-002-alert-validation.sanitized.json",
        "docs/evidence/zero-trust/zt-vis-002-control-node.sanitized.json",
        "docs/evidence/zero-trust/zt-vis-002-live-gate-discovery.sanitized.json",
        "docs/evidence/zero-trust/zt-vis-002-cinder-prerequisite-activation.sanitized.json",
        "docs/evidence/zero-trust/zt-vis-002-external-input-readiness.sanitized.json",
        "docs/evidence/zero-trust/zt-vis-002-terraform-preflight.sanitized.json",
        "docs/evidence/zero-trust/zt-vis-002-bounded-deployment.sanitized.json",
        "docs/evidence/zero-trust/zt-vis-002-live-validation.sanitized.json",
        "docs/evidence/zero-trust/zt-vis-002-partial-promotion-decision.sanitized.json",
        "schemas/phase-2-visibility-live-gate-discovery.schema.json",
        "schemas/phase-2-visibility-cinder-prerequisite.schema.json",
        "schemas/phase-2-visibility-readiness-contract.schema.json",
        "schemas/phase-2-visibility-external-input-readiness.schema.json",
        "schemas/phase-2-visibility-terraform-preflight.schema.json",
        "schemas/phase-2-visibility-bounded-deployment-evidence.schema.json",
        "schemas/phase-2-visibility-live-validation.schema.json",
        "schemas/phase-2-visibility-partial-promotion-decision.schema.json",
        "schemas/phase-2-visibility-alert-validation-plan.schema.json",
        "schemas/phase-2-visibility-alert-validation-evidence.schema.json",
        "terraform/modules/zt-vis-002-openstack/README.md",
        "terraform/envs/zt-vis-002-openstack/README.md",
        "terraform/envs/zt-vis-002-openstack/.terraform.lock.hcl",
        "ansible/roles/zt_vis_002/README.md",
        "ansible/roles/zt_vis_002_host/README.md",
        "ansible/playbooks/zt-vis-002-bootstrap.yml",
        "ansible/playbooks/zt-vis-002-deploy.yml",
        "ansible/playbooks/zt-vis-002-live-validation.yml",
        "ansible/playbooks/zt-vis-002-alert-validation.yml",
        "tools/oci/export_digest_to_oci.py",
        "tools/live-validation/remote/validate-zt-vis-002-runtime.sh.example",
        "tools/live-validation/remote/validate-zt-vis-002-alert-delivery.py.example",
        "tools/live-validation/validate_zt_vis_002_mtls.py",
        "tools/local-vm/New-AnsibleControlVm.ps1",
        "tools/local-vm/Add-CinderDiskToOpenStackAio.ps1",
        "tools/local-vm/Initialize-ZtVis002ExternalInputs.sh",
        "tools/validate_p2_vis_001_artifacts.py",
    }
    if not required_authorities.issubset(set(package.get("source_authorities", []))):
        errors.append("ZT-VIS-002 package must reference the local artifact authorities and validator")

    alert_target = alert_validation_plan.get("target", {})
    alert_api = alert_validation_plan.get("api_contract", {})
    alert_execution = alert_validation_plan.get("execution", {})
    alert_evidence_record = alert_validation_plan.get("evidence_record", {})
    alert_claims = alert_validation_plan.get("claim_boundary", {})
    if (
        alert_validation_plan.get("status") != "EXECUTED_STATUS_REVIEW_PENDING"
        or alert_target.get("grafana_version") != "13.1.0"
        or alert_target.get("permanent_component_count") != 5
        or alert_target.get("permanent_receiver_added") is not False
        or alert_target.get("public_listener_added") is not False
        or alert_api.get("webhook_integration_version") != "v1"
        or alert_api.get("legacy_receiver_test_used") is not False
        or alert_api.get("temporary_rule_paused") is not True
        or any(value is not True for value in alert_execution.values())
        or alert_evidence_record.get("path") != str(ALERT_VALIDATION_EVIDENCE).replace("\\", "/")
        or alert_evidence_record.get("validation_id") != alert_validation_evidence.get("validation_id")
        or any(value is not False for value in alert_claims.values())
    ):
        errors.append("Alert validation plan must record the evidence-bound execution while remaining five-component, private, paused, status-pending, and claim-free")
    required_alert_validator_tokens = (
        'EXPECTED_GRAFANA_VERSION = "13.1.0"',
        'ALERT_RULE_COLLECTION = "/api/v1/provisioning/alert-rules"',
        'RECEIVER_TEST = "/apis/notifications.alerting.grafana.app/v1beta1/namespaces/default/receivers/-/test"',
        '"version": "v1"',
        '"ZT_VIS_002_ALERT_VALIDATION_AUTHORIZED"',
        '"ZT_VIS_002_ALERT_RULE_MUTATION_AUTHORIZED"',
        '"ZT_VIS_002_NOTIFICATION_DELIVERY_AUTHORIZED"',
        '"ZT_VIS_002_ALERT_CLEANUP_AUTHORIZED"',
        '"isPaused": True',
        'ThreadingHTTPServer((gateway, 0), Handler)',
        'wrong_path_denied(gateway, port)',
        'markers.append("cleanup=PASS")',
        'print("validation=FAIL")',
    )
    if any(token not in alert_validator for token in required_alert_validator_tokens):
        errors.append("Alert validator is missing a version, authorization, private receiver, paused-rule, denial, or cleanup boundary")
    if (
        "/api/alertmanager/grafana/config/api/v1/receivers/test" in alert_validator
        or "ThreadingHTTPServer((\"0.0.0.0\"" in alert_validator
        or re.search(r"print\([^\n]*(?:password|gateway|one_time_path)", alert_validator, flags=re.IGNORECASE)
    ):
        errors.append("Alert validator must not use the removed receiver API, a wildcard listener, or secret/runtime detail output")

    alert_authorization = alert_validation_evidence.get("authorization", {})
    alert_credential = alert_validation_evidence.get("credential_reconciliation", {})
    alert_runtime = alert_validation_evidence.get("execution", {})
    alert_cleanup = alert_validation_evidence.get("cleanup", {})
    alert_time = alert_validation_evidence.get("time_integrity", {})
    alert_boundary = alert_validation_evidence.get("package_boundary", {})
    expected_alert_cases = {
        "POSITIVE_RULE_LIFECYCLE", "POSITIVE_NOTIFICATION_DELIVERY",
        "NEGATIVE_AUTHENTICATION", "BYPASS", "PERSISTENCE_BOUNDARY", "ROLLBACK",
    }
    if any(re.search(pattern, alert_validation_evidence_text) for pattern in sensitive_runtime_patterns):
        errors.append("Sanitized alert validation evidence must not contain addresses, MACs, resource IDs, or project IDs")
    if (
        alert_validation_evidence.get("decision") != "ALERT_VALIDATION_EXECUTED_STATUS_REVIEW_PENDING"
        or any(alert_authorization.get(key) is not True for key in (
            "alert_validation", "rule_mutation", "notification_delivery", "cleanup",
            "grafana_credential_reconciliation",
        ))
        or alert_authorization.get("package_status_promotion") is not False
        or alert_credential.get("result") != "PASS"
        or alert_credential.get("authenticated_api_status") != 200
        or alert_credential.get("password_stdin_only") is not True
        or alert_credential.get("credential_value_logged") is not False
    ):
        errors.append("Alert validation evidence must retain explicit authorization, protected stdin credential reconciliation, and pending status authority")
    raw_alert_log = alert_runtime.get("raw_log", {})
    sanitized_alert_log = alert_runtime.get("sanitized_log", {})
    if (
        alert_runtime.get("grafana_version") != "13.1.0"
        or alert_runtime.get("webhook_integration_version") != "v1"
        or alert_runtime.get("ansible_failed") != 0
        or alert_runtime.get("ansible_unreachable") != 0
        or alert_runtime.get("permanent_component_count") != 5
        or alert_runtime.get("permanent_receiver_added") is not False
        or alert_runtime.get("public_listener_added") is not False
        or raw_alert_log.get("tracked") is not False
        or raw_alert_log.get("secret_scan") != "PASS"
        or raw_alert_log.get("protected_value_matches") != 0
        or sanitized_alert_log.get("tracked") is not False
        or sanitized_alert_log.get("verification") != "PASS"
    ):
        errors.append("Alert validation runtime must retain the exact Grafana v13.1.0 private five-component and sanitized-log boundary")
    alert_cases = alert_validation_evidence.get("acceptance_cases", [])
    if (
        {item.get("case_type") for item in alert_cases} != expected_alert_cases
        or len(alert_cases) != len(expected_alert_cases)
        or any(item.get("result") != "PASS" for item in alert_cases)
    ):
        errors.append("Alert validation evidence must pass exactly six positive, denial, bypass, persistence, and rollback cases")
    if (
        alert_cleanup.get("temporary_rule_count") != 0
        or alert_cleanup.get("temporary_folder_count") != 0
        or any(alert_cleanup.get(key) is not True for key in (
            "temporary_listener_absent", "target_validator_absent", "target_recovery_key_rejected",
            "aio_recovery_key_rejected", "control_recovery_key_rejected",
            "controller_transient_keys_removed", "windows_recovery_artifacts_removed",
            "protected_raw_log_preserved",
        ))
    ):
        errors.append("Alert validation evidence must record exact temporary-resource and recovery-access cleanup")
    if (
        alert_time.get("status") != "OPEN_REVIEW_REQUIRED"
        or alert_time.get("clock_correction_executed") is not False
        or alert_time.get("upstream_packet_count") != 0
        or alert_time.get("target_clock_skew_seconds_observed", 0) <= 0
    ):
        errors.append("Alert validation evidence must preserve the open target-clock finding without claiming correction")
    if any(alert_boundary.get(key) is not False for key in (
        "alert_gap_closed", "package_status_promoted", "p2_vis_001_completed",
        "central_visibility_fully_accepted", "retention_validated", "snapshot_restore_validated",
        "scheduled_or_continuous_validation", "maturity_assessed", "compliance_assessed",
        "production_readiness_claimed",
    )):
        errors.append("Alert validation evidence cannot close the gap, promote package status, or claim completion, retention, restore, scheduling, maturity, compliance, or production readiness")
    for artifact in alert_validation_evidence.get("source_artifacts", []):
        relative = Path(artifact.get("path", ""))
        candidate = root / relative
        actual = hashlib.sha256(candidate.read_bytes()).hexdigest() if candidate.is_file() else None
        if actual != artifact.get("sha256"):
            errors.append(f"Alert validation source hash mismatch: {relative}")
    for gate in (
        "zt_vis_002_alert_validation_authorized",
        "zt_vis_002_alert_rule_mutation_authorized",
        "zt_vis_002_notification_delivery_authorized",
        "zt_vis_002_alert_cleanup_authorized",
    ):
        if f"{gate}: false" not in alert_validation_playbook:
            errors.append(f"Alert validation playbook must default-deny {gate}")
    if (
        "all four explicit alert-validation authorizations" not in alert_validation_playbook
        or "state: absent" not in alert_validation_playbook
        or "cleanup=PASS" not in alert_validation_playbook
        or "validation=PASS" not in alert_validation_playbook
    ):
        errors.append("Alert validation playbook must require all gates, verify cleanup, and remove the temporary validator")
    infrastructure_prerequisite = contract.get("infrastructure_prerequisite", {})
    if (
        contract.get("contract_status") != "BOUNDED_DEPLOYMENT_AND_LIVE_VALIDATOR_PARTIALLY_ACCEPTED"
        or contract.get("deployment_authorized") is not True
        or contract.get("runtime_validation_status") != "PARTIALLY_VALIDATED"
        or contract.get("runtime_executed") is not True
        or contract.get("prerequisite_runtime_executed") is not True
        or contract.get("live_target_changed") is not True
        or contract.get("central_monitoring_completed") is not False
        or contract.get("package_runtime_promoted") is not True
        or infrastructure_prerequisite.get("cinder_lvm_status") != "RUNTIME_VALIDATED"
        or infrastructure_prerequisite.get("full_infrastructure_rollback_executed") is not False
    ):
        errors.append("Deployment contract must record partial runtime acceptance while withholding full infrastructure rollback and completion")
    terraform_validation = native_validation.get("terraform", {})
    ansible_validation = native_validation.get("ansible", {})
    if (
        terraform_validation.get("validate") != "PASS"
        or terraform_validation.get("plan") != "NOT_RUN_MISSING_APPROVED_OPENSTACK_INPUTS"
        or terraform_validation.get("apply") != "NOT_RUN"
    ):
        errors.append("Native validation must preserve Terraform validate PASS while plan and apply remain unexecuted")
    if (
        ansible_validation.get("install_status") != "INSTALLED"
        or ansible_validation.get("version") != "2.16.3"
        or ansible_validation.get("target_control_node") != "VMWARE_WORKSTATION_UBUNTU_24_04"
        or ansible_validation.get("virtualization_platform") != "VMWARE_WORKSTATION_17_6_4"
        or ansible_validation.get("control_node_runtime_created") is not True
        or ansible_validation.get("control_user_class") != "NON_ADMINISTRATIVE_LOCAL"
        or ansible_validation.get("windows_hypervisor_present") is not False
        or ansible_validation.get("existing_vmware_workloads_preserved") is not True
        or ansible_validation.get("wsl_control_node_used") is not False
        or ansible_validation.get("network_boundary") != "VMNET8_NAT_AND_VMNET1_HOST_ONLY_PASS"
        or ansible_validation.get("ssh_boundary") != "KEY_ONLY_PRIVATE_SUBNETS_PASS"
        or ansible_validation.get("ansible_local_ping") != "PASS"
        or ansible_validation.get("syntax_check") != "PASS"
        or ansible_validation.get("restart_persistence") != "PASS"
        or ansible_validation.get("playbook_execution") != "NOT_RUN"
        or native_validation.get("control_node_bootstrap_executed") is not True
        or native_validation.get("package_runtime_executed") is not False
        or native_validation.get("protected_openstack_target_changed") is not False
        or native_validation.get("openstack_credentials_loaded") is not False
    ):
        errors.append("Native validation must preserve the VMware Ansible control-node result without claiming OpenStack or playbook execution")
    return errors


def main() -> int:
    try:
        errors = validate()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors = [str(exc)]
    for error in errors:
        print(f"[FAIL] {error}")
    if errors:
        print(f"P2-VIS-001 artifact summary: passed=0, failed={len(errors)}")
        return 1
    print("[PASS] P2-VIS-001 partial runtime promotion is evidence-bound; completion and full acceptance remain blocked by three open gaps.")
    print("P2-VIS-001 artifact summary: passed=1, failed=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
