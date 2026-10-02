#!/usr/bin/env python3
"""Read-only validation for the approved composite service catalog."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CATALOG = Path("docs/platform/composite-service-catalog.yaml")
EXECUTION_CATALOG = Path("applications/internal-iaas-portal/terraform/catalog.json")
ADR = Path("docs/adr/0019-approved-composite-service-catalog.md")
SAAS_PAAS = Path("docs/platform/financial-saas-development-paas.yaml")
SECURITIES_PROFILE = Path("docs/platform/securities-domain-profile.yaml")
SAAS_PAAS_ADR = Path("docs/adr/0021-financial-saas-development-paas.md")
RESOLVER = Path("applications/internal-iaas-portal/services/request-api/request_api/blueprints.py")
SAAS_RESOLVER = Path("applications/internal-iaas-portal/services/request-api/request_api/saas_paas.py")
REQUEST_MAIN = Path("applications/internal-iaas-portal/services/request-api/request_api/main.py")
REQUEST_CONFIG = Path("applications/internal-iaas-portal/services/request-api/request_api/config.py")
RESOLVER_TEST = Path("applications/internal-iaas-portal/tests/api/test_blueprint_resolver.py")
SAAS_TEST = Path("applications/internal-iaas-portal/tests/api/test_financial_saas_paas.py")
FLOW_TEST = Path("applications/internal-iaas-portal/tests/integration/test_composite_blueprint_flow.py")
USER_PORTAL = Path("applications/internal-iaas-portal/services/user-portal/assets/app.js")
REQUIRED_FILES = (
    CATALOG,
    EXECUTION_CATALOG,
    ADR,
    SAAS_PAAS,
    SECURITIES_PROFILE,
    SAAS_PAAS_ADR,
    RESOLVER,
    SAAS_RESOLVER,
    REQUEST_MAIN,
    REQUEST_CONFIG,
    RESOLVER_TEST,
    SAAS_TEST,
    FLOW_TEST,
    USER_PORTAL,
)
EXPECTED_COMPONENTS = {
    "COMPUTE_VM",
    "VDI_WORKSPACE",
    "K3S_RUNTIME",
    "APPLICATION_RUNTIME",
    "POSTGRESQL",
    "CACHE",
    "MESSAGE_QUEUE",
    "OBJECT_STORAGE",
    "NAS_FILE_EXCHANGE",
    "LOAD_BALANCER",
    "NETWORK_POLICY",
    "OPERATIONS_PROFILE",
}
EXPECTED_BLUEPRINTS = {
    "DEVELOPER_WORKSPACE",
    "SECURE_ADMIN_WORKSPACE",
    "WEB_APPLICATION_STACK",
    "API_DEVELOPMENT_STACK",
    "VM_APPLICATION_STACK",
    "AI_AGENT_SANDBOX",
    "DATA_PROCESSING_LAB",
    "SYNTHETIC_MARKET_DATA_LAB",
}
EXPECTED_INPUTS = {"blueprint_id", "environment", "size", "duration_hours", "purpose"}
EXPECTED_EXECUTION_PROFILES = {
    "DEV-OS-VM-S",
    "DEV-OS-VM-M",
    "DEV-OS-VM-L",
    "DEV-OS-K3S-S",
    "DEV-OS-K3S-M",
}


@dataclass
class Result:
    passes: list[str] = field(default_factory=list)
    failures: list[str] = field(default_factory=list)

    def require(self, condition: bool, message: str) -> None:
        (self.passes if condition else self.failures).append(message)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(root: Path) -> Result:
    result = Result()
    for relative in REQUIRED_FILES:
        result.require((root / relative).is_file(), f"required catalog authority exists: {relative.as_posix()}")
    if result.failures:
        return result
    try:
        catalog = load(root / CATALOG)
        execution = load(root / EXECUTION_CATALOG)
    except (OSError, json.JSONDecodeError) as exc:
        result.failures.append(f"catalog authority cannot be loaded: {exc}")
        return result

    result.require(catalog.get("schema_version") == "1.0.0", "catalog schema version is pinned")
    result.require(catalog.get("status") == "PARTIALLY_IMPLEMENTED_LOCAL", "catalog status remains bounded local implementation")
    result.require(catalog.get("model") == "APPROVED_COMPOSITE_BLUEPRINTS", "catalog model is approved composite blueprints")
    result.require(
        catalog.get("portal_integration_status")
        == "VM_APPLICATION_REQUEST_PATH_LOCAL_IMPLEMENTED",
        "portal integration is limited to one local blueprint request path",
    )
    result.require(catalog.get("runtime_validation_status") == "NOT_VALIDATED", "catalog runtime is not overclaimed")

    policy = catalog.get("construction_policy", {})
    expected_policy = {
        "components_user_selectable": False,
        "free_form_composition": False,
        "arbitrary_hcl": False,
        "raw_provider_identifiers": False,
        "blueprint_selection_only": True,
        "resolved_manifest_immutable": True,
        "deployment_transaction": "ALL_OR_NOTHING",
        "rollback_order": "REVERSE_DEPENDENCY_ORDER",
    }
    for key, value in expected_policy.items():
        result.require(policy.get(key) == value, f"construction policy preserved: {key}={value}")

    components = catalog.get("components", [])
    component_map = {item.get("component_id"): item for item in components if isinstance(item, dict)}
    result.require(len(components) == 12 and set(component_map) == EXPECTED_COMPONENTS, "exactly twelve hidden internal service components are fixed")
    result.require(all(item.get("user_visible") is False for item in component_map.values()), "internal components are not directly user visible")
    result.require(all(item.get("owner") and item.get("provider_binding") for item in component_map.values()), "every component has an owner and provider binding")

    blueprints = catalog.get("blueprints", [])
    blueprint_map = {item.get("blueprint_id"): item for item in blueprints if isinstance(item, dict)}
    result.require(len(blueprints) == 8 and set(blueprint_map) == EXPECTED_BLUEPRINTS, "exactly eight approved user-facing blueprints are fixed")
    mandatory = set(catalog.get("mandatory_blueprint_components", []))
    result.require(mandatory == {"NETWORK_POLICY", "OPERATIONS_PROFILE"}, "network and operations controls are mandatory")
    for blueprint_id, blueprint in blueprint_map.items():
        selected = set(blueprint.get("components", []))
        result.require(bool(selected) and selected <= EXPECTED_COMPONENTS, f"{blueprint_id} uses only approved components")
        result.require(mandatory <= selected, f"{blueprint_id} includes network and operations controls")
        result.require(bool(blueprint.get("network_profile")), f"{blueprint_id} has a fixed network profile")
        result.require(bool(blueprint.get("allowed_environments")) and "PROD" not in blueprint.get("allowed_environments", []), f"{blueprint_id} is bounded to non-production environments")
        result.require(bool(blueprint.get("allowed_sizes")) and bool(blueprint.get("allowed_duration_hours")), f"{blueprint_id} has bounded size and duration inputs")
        result.require(bool(blueprint.get("user_summary")), f"{blueprint_id} has a user-facing summary without raw components")

    result.require(set(catalog.get("allowed_user_inputs", [])) == EXPECTED_INPUTS, "user inputs are limited to five fixed fields")
    market = blueprint_map.get("SYNTHETIC_MARKET_DATA_LAB", {})
    result.require(market.get("network_profile") == "SYNTHETIC_MULTICAST_BOUNDED", "multicast exists only as the synthetic bounded profile")
    other_multicast = [
        blueprint_id
        for blueprint_id, blueprint in blueprint_map.items()
        if blueprint_id != "SYNTHETIC_MARKET_DATA_LAB" and "MULTICAST" in str(blueprint.get("network_profile", ""))
    ]
    result.require(not other_multicast, "no other blueprint inherits multicast")
    sandbox = blueprint_map.get("AI_AGENT_SANDBOX", {})
    result.require(
        sandbox.get("network_profile") == "AI_AGENT_EGRESS_BROKERED",
        "AI agent sandbox uses the brokered egress profile",
    )
    result.require(
        sandbox.get("components")
        == ["K3S_RUNTIME", "OBJECT_STORAGE", "NETWORK_POLICY", "OPERATIONS_PROFILE"],
        "AI agent sandbox composition is fixed",
    )
    saas = blueprint_map.get("API_DEVELOPMENT_STACK", {})
    result.require(saas.get("display_name") == "Financial SaaS Development PaaS", "financial SaaS PaaS is the approved API development product")
    result.require(saas.get("network_profile") == "PRIVATE_SAAS_INGRESS", "financial SaaS PaaS uses private ingress")
    expected_domain_profiles = {
        "API_DEVELOPMENT_STACK": [
            "SECURITIES_ORDER_API_SIMULATION",
            "SECURITIES_POST_TRADE_SIMULATION",
        ],
        "DATA_PROCESSING_LAB": ["SECURITIES_PORTFOLIO_RISK_SIMULATION"],
        "SYNTHETIC_MARKET_DATA_LAB": ["SECURITIES_MARKET_DATA_SIMULATION"],
    }
    for blueprint_id, profiles in expected_domain_profiles.items():
        result.require(
            blueprint_map.get(blueprint_id, {}).get("business_domain_profiles") == profiles,
            f"{blueprint_id} has the approved securities business-domain profiles",
        )
    result.require(
        saas.get("components")
        == ["K3S_RUNTIME", "APPLICATION_RUNTIME", "POSTGRESQL", "CACHE", "MESSAGE_QUEUE", "OBJECT_STORAGE", "NAS_FILE_EXCHANGE", "LOAD_BALANCER", "NETWORK_POLICY", "OPERATIONS_PROFILE"],
        "financial SaaS PaaS composition is fixed",
    )
    try:
        saas_authority = load(root / SAAS_PAAS)
    except (OSError, json.JSONDecodeError) as exc:
        result.failures.append(f"financial SaaS PaaS authority cannot be loaded: {exc}")
        return result
    result.require(saas_authority.get("blueprint_id") == "API_DEVELOPMENT_STACK", "financial SaaS authority is bound to the catalog product")
    result.require(
        saas_authority.get("business_domain_profiles")
        == expected_domain_profiles["API_DEVELOPMENT_STACK"],
        "financial SaaS authority includes the bounded securities profiles",
    )
    try:
        securities_authority = load(root / SECURITIES_PROFILE)
    except (OSError, json.JSONDecodeError) as exc:
        result.failures.append(f"securities authority cannot be loaded: {exc}")
        return result
    mapped_profiles = {
        item.get("capability_id"): item.get("blueprint_id")
        for item in securities_authority.get("capabilities", [])
        if isinstance(item, dict)
    }
    result.require(
        mapped_profiles
        == {
            profile: blueprint_id
            for blueprint_id, profiles in expected_domain_profiles.items()
            for profile in profiles
        },
        "securities capabilities map only to approved composite blueprints",
    )
    result.require(saas_authority.get("mini_ona_relationship") == {
        "role": "INTERNAL_AUTOMATION_SERVICE",
        "paas_runtime_dependency": False,
        "kata_required_for_saas_workloads": False,
        "kata_required_for_untrusted_agent_execution": True,
    }, "Mini-Ona and ordinary SaaS workloads remain separate")
    result.require(saas_authority.get("status", {}).get("runtime") == "NOT_VALIDATED", "financial SaaS PaaS runtime is not overclaimed")
    result.require(saas_authority.get("tenant_bundle") == {
        "status": "INERT_LOCAL_IMPLEMENTED",
        "service_endpoint": "/internal/v1/financial-saas/tenant-bundle",
        "namespace_derivation": "SOURCE_MANIFEST_DIGEST",
        "pod_security": "RESTRICTED_V1_36",
        "quota_by_size": True,
        "service_account_token_default": "DISABLED",
        "network_policies": ["DEFAULT_DENY", "CLUSTER_DNS", "PRIVATE_INGRESS", "APPROVED_DATA_SERVICES"],
        "runtime_authorized": False,
        "deployable": False,
    }, "financial SaaS tenant bundle remains inert and bounded")

    binding = catalog.get("execution_profile_catalog", {})
    result.require(binding.get("path") == EXECUTION_CATALOG.as_posix(), "execution-profile catalog path is pinned")
    result.require(binding.get("role") == "INTERNAL_PROVIDER_BOUND_EXECUTION_PROFILES", "existing five entries are internal execution profiles")
    result.require(binding.get("direct_user_exposure") == "SERVICE_ONLY", "execution profiles are service-only")
    result.require(set(execution.get("products", {})) == EXPECTED_EXECUTION_PROFILES, "five existing OpenStack execution profiles remain exact")
    result.require(execution.get("deployment_authorized") is False, "execution catalog remains fail-closed")

    prohibited = set(catalog.get("prohibited_scope", []))
    required_prohibited = {
        "PRODUCTION_FINANCIAL_DATA",
        "REAL_SECURITIES_ORDERS",
        "REAL_MARKET_CONNECTIVITY",
        "REAL_CUSTOMER_OR_ACCOUNT_DATA",
        "PRODUCTION_CLEARING_OR_SETTLEMENT",
        "USER_DEFINED_COMPONENT_GRAPH",
        "USER_SUPPLIED_PROVIDER_ID",
        "USER_SUPPLIED_HCL",
        "PARTIAL_SUCCESS_GRANT",
        "MULTI_SITE_DR",
        "ACTIVE_PUBLIC_CLOUD_PROVIDER",
    }
    result.require(prohibited == required_prohibited, "prohibited catalog scope is exact")

    resolver_text = (root / RESOLVER).read_text(encoding="utf-8")
    saas_resolver_text = (root / SAAS_RESOLVER).read_text(encoding="utf-8")
    main_text = (root / REQUEST_MAIN).read_text(encoding="utf-8")
    config_text = (root / REQUEST_CONFIG).read_text(encoding="utf-8")
    test_text = (root / RESOLVER_TEST).read_text(encoding="utf-8")
    saas_test_text = (root / SAAS_TEST).read_text(encoding="utf-8")
    flow_test_text = (root / FLOW_TEST).read_text(encoding="utf-8")
    portal_text = (root / USER_PORTAL).read_text(encoding="utf-8")
    for token in (
        "BLOCKED_UNIMPLEMENTED_COMPONENTS",
        "ADAPTER_NOT_IMPLEMENTED",
        "ALL_OR_NOTHING",
        "rollback_component_order",
        "BLUEPRINT_RUNTIME_GATES",
        "K3S_TENANT_BASELINE",
        "MESSAGE_QUEUE_ADAPTER",
        "SANDBOX_RUNTIME_CLASS",
        "FQDN_EGRESS_BROKER",
        "AGENT_BUDGET_ENFORCER",
        "manifest_digest",
        "business_domain_profiles",
        '"runtime_authorized": False',
    ):
        result.require(token in resolver_text, f"resolver preserves fail-closed contract: {token}")
    result.require('/api/v1/blueprints"' in main_text, "user-facing blueprint catalog endpoint exists")
    result.require('/api/v1/blueprints/resolve"' in main_text, "user-facing resolver endpoint exists")
    result.require('/internal/v1/blueprints/resolve"' in main_text, "service-only manifest endpoint exists")
    result.require('/internal/v1/financial-saas/tenant-bundle"' in main_text, "service-only financial SaaS tenant-bundle endpoint exists")
    result.require('/api/v1/blueprint-requests"' in main_text, "bounded blueprint request endpoint exists")
    result.require('/internal/v1/execution-profiles"' in main_text, "execution profiles moved to a service-only endpoint")
    result.require(
        "enable_legacy_execution_profile_requests: bool = False" in config_text,
        "legacy direct-profile requests default to disabled",
    )
    result.require(
        "direct execution-profile requests are disabled" in main_text,
        "legacy direct-profile request path fails closed",
    )
    for token in ("free_form_inputs", "reverse_rollback", "hides_internal_profile"):
        result.require(token in test_text, f"resolver regression coverage exists: {token}")
    for token in ("tampering_is_denied", "manifest_digest", "POLICY_DENIED"):
        result.require(token in flow_test_text, f"integrated manifest-flow coverage exists: {token}")
    result.require("/api/v1/blueprint-requests" in portal_text, "user portal submits blueprint requests")
    result.require(
        all(profile not in portal_text for profile in EXPECTED_EXECUTION_PROFILES),
        "user portal contains no internal execution-profile identifier",
    )
    result.require(
        all(component not in portal_text for component in EXPECTED_COMPONENTS),
        "user portal contains no hidden internal component identifier",
    )
    for token in (
        "FINANCIAL_SAAS_TENANT_BASELINE",
        "pod-security.kubernetes.io/enforce",
        "default-deny",
        "allow-cluster-dns",
        "allow-private-ingress",
        "allow-approved-data-services",
        "EXTERNAL_SECRET_REFERENCES_ONLY",
        '"runtime_authorized": False',
        '"deployable": False',
    ):
        result.require(token in saas_resolver_text, f"financial SaaS resolver preserves tenant boundary: {token}")
    for token in ("deterministic_inert", "secretless", "fail_closed", "denies_user"):
        result.require(token in saas_test_text, f"financial SaaS regression coverage exists: {token}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()
    result = validate(args.root.resolve())
    for message in result.passes:
        print(f"[PASS] {message}")
    for message in result.failures:
        print(f"[FAIL] {message}")
    print(f"Composite service catalog summary: passed={len(result.passes)} failed={len(result.failures)}")
    return 1 if result.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
