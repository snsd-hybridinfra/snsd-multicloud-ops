#!/usr/bin/env python3
"""Read-only validation for the Financial Hybrid-Ready IDP architecture."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
BASELINE = Path("docs/platform/architecture-baseline.yaml")
INVENTORY = Path("docs/platform/asset-reconciliation.yaml")
COMPOSITE_CATALOG = Path("docs/platform/composite-service-catalog.yaml")
SECURITIES_PROFILE = Path("docs/platform/securities-domain-profile.yaml")
AI_AGENT_SANDBOX = Path("docs/platform/ai-agent-sandbox.yaml")
TERRAFORM_SUPPLY_CHAIN = Path("docs/platform/terraform-supply-chain.yaml")
CONTAINER_SUPPLY_CHAIN = Path("docs/platform/container-supply-chain.yaml")
PROGRESS = Path("docs/platform/project-progress.md")
REQUIRED_FILES = (
    Path("README.md"),
    Path("docs/project-definition.md"),
    Path("docs/architecture.md"),
    Path("docs/scope-lock.md"),
    Path("docs/excluded-scope.md"),
    Path("docs/platform/README.md"),
    Path("docs/platform/target-architecture.md"),
    Path("docs/platform/implementation-roadmap.md"),
    PROGRESS,
    INVENTORY,
    COMPOSITE_CATALOG,
    SECURITIES_PROFILE,
    AI_AGENT_SANDBOX,
    TERRAFORM_SUPPLY_CHAIN,
    CONTAINER_SUPPLY_CHAIN,
    Path("docs/platform/private-iaas-golden-path.yaml"),
    Path("docs/adr/0018-financial-hybrid-ready-idp.md"),
    Path("docs/adr/0019-approved-composite-service-catalog.md"),
    Path("docs/adr/0020-persistent-ai-agent-sandbox.md"),
    Path("docs/adr/0022-managed-terraform-supply-chain.md"),
    Path("docs/adr/0023-container-image-supply-chain-and-k3s-delivery.md"),
    BASELINE,
)
EXPECTED_LAYERS = {
    "DEVELOPER_EXPERIENCE": "PARTIAL",
    "CONTROL_PLANE": "PARTIAL",
    "AUTOMATION": "PARTIAL",
    "PRIVATE_IAAS": "PARTIAL",
    "PAAS": "PARTIAL",
    "FINANCIAL_NETWORK": "DESIGN_ONLY",
    "INTEGRATED_OPERATIONS": "PARTIAL",
    "PUBLIC_CLOUD_ADAPTER": "DEFERRED",
}


@dataclass
class Result:
    failures: list[str] = field(default_factory=list)
    passes: list[str] = field(default_factory=list)

    def require(self, condition: bool, message: str) -> None:
        (self.passes if condition else self.failures).append(message)


def load_baseline(root: Path) -> dict[str, Any]:
    return json.loads((root / BASELINE).read_text(encoding="utf-8"))


def validate(root: Path) -> Result:
    result = Result()
    for relative in REQUIRED_FILES:
        result.require((root / relative).is_file(), f"required authority exists: {relative.as_posix()}")
    if result.failures:
        return result

    try:
        data = load_baseline(root)
    except (OSError, json.JSONDecodeError) as exc:
        result.failures.append(f"baseline is not valid JSON-compatible YAML: {exc}")
        return result

    authority = data.get("authority", {})
    project = data.get("project", {})
    truth = data.get("truth_boundaries", {})
    layers = data.get("layers", [])
    layer_map = {item.get("name"): item for item in layers if isinstance(item, dict)}

    result.require(data.get("schema_version") == "1.0.0", "baseline schema version is pinned")
    result.require(authority.get("architecture_owner") == "ZT-ARC-001", "ZT-ARC-001 remains the architecture security owner")
    result.require(authority.get("asset_inventory") == INVENTORY.as_posix(), "asset inventory authority is pinned")
    result.require(authority.get("composite_service_catalog") == COMPOSITE_CATALOG.as_posix(), "composite service catalog authority is pinned")
    result.require(authority.get("securities_domain_profile") == SECURITIES_PROFILE.as_posix(), "securities domain profile authority is pinned")
    result.require(authority.get("ai_agent_sandbox") == AI_AGENT_SANDBOX.as_posix(), "AI agent sandbox authority is pinned")
    result.require(authority.get("private_iaas_contract") == "docs/platform/private-iaas-golden-path.yaml", "private IaaS contract authority is pinned")
    result.require(authority.get("terraform_supply_chain") == TERRAFORM_SUPPLY_CHAIN.as_posix(), "Terraform supply-chain authority is pinned")
    result.require(authority.get("container_supply_chain") == CONTAINER_SUPPLY_CHAIN.as_posix(), "container supply-chain authority is pinned")
    result.require(authority.get("status") == "LOCAL_GOVERNANCE_VALIDATED", "architecture decision is locally governance validated")
    result.require(project.get("operating_claim") == "HYBRID_READY", "operating claim remains Hybrid-Ready")
    result.require(project.get("integrated_runtime_validation") == "NOT_VALIDATED", "integrated runtime is not overclaimed")
    expected_business_domains = {
        "SECURITIES_ORDER_API_SIMULATION",
        "SECURITIES_POST_TRADE_SIMULATION",
        "SECURITIES_PORTFOLIO_RISK_SIMULATION",
        "SECURITIES_MARKET_DATA_SIMULATION",
    }
    result.require(set(project.get("business_domains", [])) == expected_business_domains, "virtual securities business domains are exact")
    result.require(set(layer_map) == set(EXPECTED_LAYERS), "platform layer set is exact")
    for name, status in EXPECTED_LAYERS.items():
        result.require(layer_map.get(name, {}).get("status") == status, f"{name} status remains {status}")
        result.require(bool(layer_map.get(name, {}).get("components")), f"{name} has bounded components")

    expected_truth = {
        "public_cloud_provider": "UNSELECTED",
        "active_hybrid_cloud": False,
        "production_financial_workload": False,
        "real_securities_orders": False,
        "real_market_connectivity": False,
        "regulated_customer_data": False,
        "multi_site_dr": False,
        "licensed_network_images_in_git": False,
        "platform_status_promotes_zero_trust_status": False,
        "zero_trust_status_promotes_platform_status": False,
        "live_mutation_authorized_by_architecture": False,
    }
    for key, value in expected_truth.items():
        result.require(truth.get(key) == value, f"truth boundary preserved: {key}={value}")

    synchronized = {
        Path("README.md"): ("Hybrid-Ready", "OpenStack", "k3s", "Nexus", "Zero Trust", "Approved Composite Blueprints", "AI_AGENT_SANDBOX", "증권"),
        Path("docs/project-definition.md"): ("Hybrid-Ready", "Internal Developer Platform", "L3_ADVANCED", "L4_OPTIMAL", "approved composite blueprint", "AI_AGENT_SANDBOX", "증권"),
        Path("docs/architecture.md"): ("Hybrid-Ready", "PUBLIC", "NOT_VALIDATED", "approved composite blueprint"),
        Path("docs/platform/target-architecture.md"): ("OpenStack", "k3s", "Nexus", "multicast", "deferred", "approved composite", "Project Mini-Ona", "Securities business profile"),
        Path("docs/platform/implementation-roadmap.md"): ("Stage A", "Stage F", "DEFERRED", "eight-blueprint", "AI_AGENT_SANDBOX"),
        PROGRESS: ("IN_PROGRESS", "NOT_VALIDATED", "COMPLETED_LOCAL", "IN_PROGRESS_LOCAL", "DESIGN_ONLY", "DEFERRED", "합성 주문 API", "합성 시세 피드"),
    }
    for relative, tokens in synchronized.items():
        text = (root / relative).read_text(encoding="utf-8")
        result.require(all(token.casefold() in text.casefold() for token in tokens), f"architecture terms synchronized in {relative.as_posix()}")

    try:
        securities = json.loads((root / SECURITIES_PROFILE).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        result.failures.append(f"securities domain profile is not valid JSON-compatible YAML: {exc}")
        return result
    result.require(securities.get("domain_id") == "VIRTUAL_SECURITIES_COMPANY", "virtual securities domain is pinned")
    capability_ids = {
        item.get("capability_id")
        for item in securities.get("capabilities", [])
        if isinstance(item, dict)
    }
    result.require(capability_ids == expected_business_domains, "securities capability set matches architecture baseline")
    controls = securities.get("controls", {})
    result.require(
        controls == {
            "non_production_only": True,
            "synthetic_data_default": True,
            "real_order_execution": False,
            "external_market_connectivity": False,
            "regulated_personal_data": False,
            "runtime_authorized": False,
        },
        "securities controls remain synthetic, non-production and fail-closed",
    )

    try:
        inventory = json.loads((root / INVENTORY).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        result.failures.append(f"asset inventory is not valid JSON-compatible YAML: {exc}")
        return result
    result.require(inventory.get("status") == "LOCAL_INVENTORY_COMPLETE", "asset inventory is locally complete")
    rules = inventory.get("rules", {})
    for key in (
        "file_presence_is_implementation",
        "historical_runtime_claims_are_inherited",
        "provider_specific_assets_are_active",
        "destructive_reorganization_authorized",
    ):
        result.require(rules.get(key) is False, f"asset inventory safety rule preserved: {key}=False")
    assets = {item.get("path"): item for item in inventory.get("assets", []) if isinstance(item, dict)}
    required_assets = {
        "applications/internal-iaas-portal/": "ADOPT_AS_FOUNDATION",
        "platform/gitops/": "ADAPT_SELECTIVELY",
        "eve-ng/": "ADAPT",
        "docs/zero-trust/": "KEEP_AUTHORITATIVE",
    }
    for path, disposition in required_assets.items():
        item = assets.get(path, {})
        result.require(item.get("disposition") == disposition, f"asset disposition preserved: {path}={disposition}")
        result.require(bool(item.get("owner")) and bool(item.get("required_work")), f"asset ownership and required work defined: {path}")
    aws_asset = assets.get("platform/infra/aws/")
    result.require(
        aws_asset is None or aws_asset.get("disposition") == "DEFER_PROVIDER_SPECIFIC",
        "provider-specific asset remains inactive: platform/infra/aws/",
    )
    required_owners = {"catalog", "identity", "network", "terraform_state", "telemetry", "backup_restore", "cost_allocation", "security_status"}
    result.require(set(inventory.get("domain_owners", {})) == required_owners, "platform domain owners are complete")

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
    print(f"Financial IDP architecture summary: passed={len(result.passes)} failed={len(result.failures)}")
    return 1 if result.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
