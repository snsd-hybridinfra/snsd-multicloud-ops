#!/usr/bin/env python3
"""Validate the bounded OpenStack/k3s protected-system candidate."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "applications" / "internal-iaas-portal"
MODULE_ROOT = APP / "terraform" / "modules"
EXPECTED_PRODUCTS = {
    "DEV-OS-VM-S": "openstack-dev-vm-small",
    "DEV-OS-VM-M": "openstack-dev-vm-medium",
    "DEV-OS-VM-L": "openstack-dev-vm-large",
    "DEV-OS-K3S-S": "openstack-dev-k3s-small",
    "DEV-OS-K3S-M": "openstack-dev-k3s-medium",
}
PACKAGE_IDS = {
    "ZT-FND-001",
    "ZT-NET-001",
    "ZT-VIS-001",
    "ZT-ID-001",
    "ZT-APP-001",
    "ZT-DATA-001",
    "ZT-SYS-001",
    "ZT-AUTO-001",
    "ZT-CV-001",
}


def module_digest(directory: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in directory.rglob("*") if item.is_file()):
        digest.update(path.relative_to(directory).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return f"sha256:{digest.hexdigest()}"


def validate() -> tuple[list[str], list[str]]:
    passed: list[str] = []
    failures: list[str] = []

    def check(condition: bool, label: str) -> None:
        (passed if condition else failures).append(label)

    required = [
        APP / "README.md",
        APP / "zero-trust-protection-profile.yaml",
        APP / "terraform" / "catalog.json",
        APP / "services" / "terraform-runner" / "terraform_runner" / "executor.py",
        ROOT / "docs" / "adr" / "0012-openstack-protected-portal-and-k3s-paas.md",
        ROOT / "docs" / "evidence" / "zero-trust" / "internal-iaas-portal-candidate.sanitized.txt",
    ]
    check(all(path.is_file() for path in required), "required candidate authorities exist")
    if failures:
        return passed, failures

    catalog = json.loads((APP / "terraform" / "catalog.json").read_text(encoding="utf-8"))
    profile = json.loads(
        (APP / "zero-trust-protection-profile.yaml").read_text(encoding="utf-8")
    )
    products = catalog.get("products", {})
    check(catalog.get("provider") == "openstack", "catalog provider is OpenStack")
    check(catalog.get("authority_state") == "LOCAL_CANDIDATE", "catalog is candidate-only")
    check(catalog.get("deployment_authorized") is False, "catalog deployment defaults denied")
    check(
        {key: value.get("module_name") for key, value in products.items()}
        == EXPECTED_PRODUCTS,
        "internal catalog contains exactly three VM and two k3s execution profiles",
    )
    check(
        {path.name for path in MODULE_ROOT.iterdir() if path.is_dir()}
        == set(EXPECTED_PRODUCTS.values()),
        "Terraform module set matches the catalog",
    )

    forbidden_tf = (
        'resource "openstack_networking_floatingip_v2"',
        'resource "openstack_networking_network_v2"',
        'resource "openstack_networking_subnet_v2"',
        'resource "openstack_networking_router_v2"',
        'resource "openstack_networking_secgroup_v2"',
        'resource "openstack_identity_',
        "remote-exec",
        "local-exec",
        "admin_pass",
    )
    modules_ok = True
    k3s_ok = True
    ansible_digest = module_digest(APP / "ansible")
    for product_id, module_name in EXPECTED_PRODUCTS.items():
        module = MODULE_ROOT / module_name
        main = (module / "main.tf").read_text(encoding="utf-8")
        outputs = (module / "outputs.tf").read_text(encoding="utf-8")
        product = products.get(product_id, {})
        modules_ok &= module_digest(module) == product.get("artifact_digest")
        modules_ok &= main.count('resource "openstack_networking_port_v2"') == 1
        modules_ok &= main.count('resource "openstack_compute_instance_v2"') == 1
        modules_ok &= all(value not in main for value in forbidden_tf)
        modules_ok &= bool(re.search(r"port_security_enabled\s*=\s*true", main))
        modules_ok &= "private-only" in main
        modules_ok &= "floating_ip" in outputs and "value = false" in outputs
        if "k3s" in module_name:
            k3s_ok &= "user_data" not in main
            k3s_ok &= 'ConfigurationOwner  = "ANSIBLE"' in main
            k3s_ok &= 'value = "CONFIGURATION_REQUIRED"' in outputs
            k3s_ok &= "token" not in outputs.lower() and "kubeconfig" not in outputs.lower()
    check(modules_ok, "module digests and private Nova/Neutron boundaries match")
    check(k3s_ok, "k3s Terraform handoff is Ansible-owned and validation-gated")
    ansible_tasks = (
        APP / "ansible" / "roles" / "k3s_single_node" / "tasks" / "main.yaml"
    ).read_text(encoding="utf-8")
    ansible_config = (
        APP
        / "ansible"
        / "roles"
        / "k3s_single_node"
        / "templates"
        / "config.yaml.j2"
    ).read_text(encoding="utf-8")
    ansible_baseline = (
        APP
        / "ansible"
        / "roles"
        / "k3s_single_node"
        / "templates"
        / "dev-baseline.yaml.j2"
    ).read_text(encoding="utf-8")
    check(
        all(
            product.get("configuration_digest") == ansible_digest
            for product_id, product in products.items()
            if "K3S" in product_id
        )
        and "checksum_algorithm: sha256" in ansible_tasks
        and "k3s_airgap_images_sha256" in ansible_tasks
        and "get --raw=/readyz" in ansible_tasks
        and all(
            value in ansible_tasks
            for value in ("coredns", "metrics-server", "local-path-provisioner")
        )
        and 'write-kubeconfig-mode: "0600"' in ansible_config
        and "secrets-encryption: true" in ansible_config
        and all(
            value in ansible_baseline
            for value in ("kind: ResourceQuota", "kind: LimitRange", "kind: NetworkPolicy")
        ),
        "Ansible k3s configuration is digest-pinned offline and locally validated",
    )

    synced_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (
            APP / "services" / "request-api" / "request_api" / "catalog.py",
            APP / "services" / "approval-api" / "approval_api" / "provisioning.py",
            APP / "services" / "terraform-runner" / "terraform_runner" / "executor.py",
        )
    )
    sync_ok = all(
        product_id in synced_text
        and module_name in synced_text
        and products[product_id]["artifact_digest"] in synced_text
        for product_id, module_name in EXPECTED_PRODUCTS.items()
    )
    check(sync_ok, "request approval runner and catalog authorities are synchronized")

    runner = (
        APP / "services" / "terraform-runner" / "terraform_runner" / "executor.py"
    ).read_text(encoding="utf-8")
    config = (
        APP / "services" / "terraform-runner" / "terraform_runner" / "config.py"
    ).read_text(encoding="utf-8")
    compose = (APP / "compose.mvp.yaml").read_text(encoding="utf-8")
    check(
        'runner_mode: str = "mock"' in config
        and 'deployment_authorized: bool = False' in config
        and 'TF_OPENSTACK_DEPLOYMENT_AUTHORIZED: "false"' in compose,
        "real OpenStack execution is fail-closed by default",
    )
    check(
        "k3s configuration requires separate runtime authorization" in runner
        and '"BOOTSTRAP_VALIDATION_REQUIRED"' in runner
        and '"CONFIGURATION_FAILED"' in runner
        and '"ROLLBACK_FAILED"' in runner,
        "k3s automation requires separate approval and automatic rollback",
    )
    check(
        all(f'"127.0.0.1:${{{name}' in compose for name in (
            "MVP_REQUEST_API_PORT",
            "MVP_APPROVAL_API_PORT",
            "MVP_GRANT_API_PORT",
            "MVP_USER_PORTAL_PORT",
            "MVP_ADMIN_PORTAL_PORT",
        )),
        "local service ports bind to loopback",
    )

    relationships = profile.get("package_relationships", [])
    check(profile.get("provider") == "OPENSTACK", "protection profile targets OpenStack")
    check(
        profile.get("implementation_status") == "LOCAL_CANDIDATE"
        and profile.get("deployment_status") == "NOT_AUTHORIZED"
        and profile.get("runtime_validation_status") == "NOT_VALIDATED"
        and profile.get("package_status_promotion") == "NONE"
        and profile.get("phase_1_status_change") == "NONE",
        "profile preserves authority and status boundaries",
    )
    check(
        {item.get("package_id") for item in relationships} == PACKAGE_IDS
        and all(item.get("candidate_only") is True for item in relationships),
        "profile reuses only approved package authorities",
    )

    active_suffixes = {".py", ".tf", ".yaml", ".yml", ".json", ".js", ".html", ".ps1", ".sh", ".j2"}
    provider_patterns = re.compile(
        r'provider\s+"aws"|resource\s+"aws_|\bimport\s+boto3\b|amazonaws\.com|arn:aws:',
        re.IGNORECASE,
    )
    secret_patterns = re.compile(
        r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\bAKIA[0-9A-Z]{16}\b|\bgh[opsu]_[A-Za-z0-9]{20,}\b"
    )
    tracked_app_files = {
        line.strip()
        for line in subprocess.run(
            ["git", "ls-files", "applications/internal-iaas-portal"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.splitlines()
        if line.strip()
    }
    provider_hits: list[str] = []
    secret_hits: list[str] = []
    unsafe_files: list[str] = []
    for path in APP.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(APP).as_posix()
        lower = relative.lower()
        if any(part.lower() in {".venv", "venv", "__pycache__"} for part in path.relative_to(APP).parts):
            continue
        repository_path = f"applications/internal-iaas-portal/{relative}"
        if repository_path in tracked_app_files and (
            path.name == ".env"
            or "/.venv/" in f"/{lower}/"
            or "__pycache__" in lower
            or path.suffix.lower() in {".pyc", ".tfstate", ".pem", ".key", ".p12"}
        ):
            unsafe_files.append(relative)
        if path.suffix.lower() in active_suffixes and "__pycache__" not in lower:
            text = path.read_text(encoding="utf-8", errors="replace")
            if provider_patterns.search(text):
                provider_hits.append(relative)
            if secret_patterns.search(text):
                secret_hits.append(relative)
    check(not provider_hits, "active candidate code contains no former provider implementation")
    check(not secret_hits, "candidate contains no detected credential material")
    check(not unsafe_files, "candidate contains no runtime state or sensitive file types")

    release_text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in (APP / "kubernetes").rglob("*.yaml")
    )
    check(
        "registry.example.com" in release_text and "@sha256:" + "0" * 64 in release_text,
        "unapproved cluster artifacts keep release readiness closed",
    )
    check(not any((APP / name).exists() for name in ("scenarios", "scenario")), "no scenario framework was introduced")

    tracked_runtime = subprocess.run(
        ["git", "ls-files", ".runtime", "applications/internal-iaas-portal/.runtime"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    check(not tracked_runtime, "no runtime path is tracked")
    return passed, failures


def main() -> int:
    passed, failures = validate()
    for label in passed:
        print(f"PASS: {label}")
    for label in failures:
        print(f"FAIL: {label}")
    print(f"SUMMARY: {len(passed)} PASS / {len(failures)} FAIL")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
