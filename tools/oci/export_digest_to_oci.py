#!/usr/bin/env python3
"""Export one Docker Hub manifest digest as a verified OCI image archive."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import tarfile
import tempfile
import time
from typing import BinaryIO
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


DIGEST = re.compile(r"^sha256:([0-9a-f]{64})$")
REFERENCE = re.compile(
    r"^docker\.io/(?P<repository>[a-z0-9][a-z0-9._/-]*)@(?P<digest>sha256:[0-9a-f]{64})$"
)
MANIFEST_ACCEPT = ", ".join(
    (
        "application/vnd.oci.image.manifest.v1+json",
        "application/vnd.docker.distribution.manifest.v2+json",
    )
)


class ExportError(RuntimeError):
    """Raised when registry content violates the fixed export contract."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def request_bytes(url: str, *, headers: dict[str, str] | None = None) -> tuple[bytes, dict[str, str]]:
    last: Exception | None = None
    for attempt in range(4):
        try:
            request = Request(url, headers=headers or {})
            with urlopen(request, timeout=60) as response:
                return response.read(), {key.lower(): value for key, value in response.headers.items()}
        except (HTTPError, URLError, TimeoutError) as exc:
            last = exc
            if attempt == 3:
                break
            time.sleep(2**attempt)
    raise ExportError(f"Registry request failed after bounded retries: {type(last).__name__}")


def request_to_file(url: str, destination: Path, *, headers: dict[str, str], expected_digest: str) -> int:
    match = DIGEST.fullmatch(expected_digest)
    if not match:
        raise ExportError("Blob digest is not sha256")
    last: Exception | None = None
    for attempt in range(4):
        try:
            digest = hashlib.sha256()
            size = 0
            request = Request(url, headers=headers)
            with urlopen(request, timeout=120) as response, destination.open("wb") as output:
                while True:
                    block = response.read(1024 * 1024)
                    if not block:
                        break
                    digest.update(block)
                    output.write(block)
                    size += len(block)
            if digest.hexdigest() != match.group(1):
                raise ExportError("Downloaded blob digest mismatch")
            return size
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            last = exc
            destination.unlink(missing_ok=True)
            if attempt == 3:
                break
            time.sleep(2**attempt)
    if isinstance(last, ExportError):
        raise last
    raise ExportError(f"Blob request failed after bounded retries: {type(last).__name__}")


def registry_bearer_for(repository: str) -> str:
    query = urlencode(
        {
            "service": "registry.docker.io",
            "scope": f"repository:{repository}:pull",
        }
    )
    body, _ = request_bytes(f"https://auth.docker.io/token?{query}")
    value = json.loads(body)
    bearer = value.get("token") or value.get("access_token")
    if not isinstance(bearer, str) or not bearer:
        raise ExportError("Registry token response omitted a token")
    return bearer


def blob_descriptors(manifest: dict[str, object]) -> list[dict[str, object]]:
    config = manifest.get("config")
    layers = manifest.get("layers")
    if not isinstance(config, dict) or not isinstance(layers, list) or not layers:
        raise ExportError("Manifest omitted config or layers")
    values = [config, *layers]
    for value in values:
        if not isinstance(value, dict):
            raise ExportError("Manifest descriptor is not an object")
        digest = value.get("digest")
        size = value.get("size")
        if not isinstance(digest, str) or not DIGEST.fullmatch(digest):
            raise ExportError("Manifest descriptor digest is invalid")
        if not isinstance(size, int) or size < 0:
            raise ExportError("Manifest descriptor size is invalid")
    return values


def add_to_tar(archive: tarfile.TarFile, source: Path, name: str) -> None:
    info = archive.gettarinfo(str(source), arcname=name)
    info.uid = 0
    info.gid = 0
    info.uname = "root"
    info.gname = "root"
    info.mtime = 0
    if source.is_dir():
        archive.addfile(info)
    else:
        with source.open("rb") as stream:
            archive.addfile(info, stream)


def build_archive(reference: str, tag_name: str, output: Path) -> dict[str, object]:
    matched = REFERENCE.fullmatch(reference)
    if not matched:
        raise ExportError("Reference must be docker.io/repository@sha256:<64 lowercase hex>")
    repository = matched.group("repository")
    expected_manifest = matched.group("digest")
    bearer = registry_bearer_for(repository)
    headers = {"Authorization": f"Bearer {bearer}", "Accept": MANIFEST_ACCEPT}
    manifest_url = f"https://registry-1.docker.io/v2/{repository}/manifests/{expected_manifest}"
    manifest_body, response_headers = request_bytes(manifest_url, headers=headers)
    actual_manifest = "sha256:" + hashlib.sha256(manifest_body).hexdigest()
    if actual_manifest != expected_manifest:
        raise ExportError("Manifest body does not match the requested digest")
    header_digest = response_headers.get("docker-content-digest")
    if header_digest and header_digest != expected_manifest:
        raise ExportError("Registry manifest digest header mismatch")
    manifest = json.loads(manifest_body)
    media_type = manifest.get("mediaType")
    if media_type not in {
        "application/vnd.oci.image.manifest.v1+json",
        "application/vnd.docker.distribution.manifest.v2+json",
    }:
        raise ExportError("Requested digest did not resolve to a single image manifest")
    descriptors = blob_descriptors(manifest)

    with tempfile.TemporaryDirectory(prefix="zt-vis-002-oci-") as temporary:
        root = Path(temporary)
        blob_root = root / "blobs" / "sha256"
        blob_root.mkdir(parents=True)
        manifest_path = blob_root / expected_manifest.split(":", 1)[1]
        manifest_path.write_bytes(manifest_body)
        os.chmod(manifest_path, 0o600)
        for descriptor in descriptors:
            digest = str(descriptor["digest"])
            path = blob_root / digest.split(":", 1)[1]
            size = request_to_file(
                f"https://registry-1.docker.io/v2/{repository}/blobs/{digest}",
                path,
                headers=headers,
                expected_digest=digest,
            )
            if size != descriptor["size"]:
                raise ExportError("Downloaded blob size mismatch")
            os.chmod(path, 0o600)

        config_digest = str(descriptors[0]["digest"])
        config = json.loads((blob_root / config_digest.split(":", 1)[1]).read_bytes())
        if config.get("os") != "linux" or config.get("architecture") != "amd64":
            raise ExportError("Image config is not linux/amd64")

        (root / "oci-layout").write_text('{"imageLayoutVersion":"1.0.0"}\n', encoding="utf-8")
        index = {
            "schemaVersion": 2,
            "manifests": [
                {
                    "mediaType": media_type,
                    "digest": expected_manifest,
                    "size": len(manifest_body),
                    "annotations": {"org.opencontainers.image.ref.name": tag_name},
                    "platform": {"os": "linux", "architecture": "amd64"},
                }
            ],
        }
        (root / "index.json").write_text(
            json.dumps(index, separators=(",", ":"), sort_keys=True) + "\n",
            encoding="utf-8",
        )
        output.parent.mkdir(parents=True, exist_ok=True)
        temporary_output = output.with_suffix(output.suffix + ".tmp")
        temporary_output.unlink(missing_ok=True)
        with tarfile.open(temporary_output, "w", format=tarfile.PAX_FORMAT) as archive:
            for directory in (root / "blobs", blob_root):
                add_to_tar(archive, directory, directory.relative_to(root).as_posix())
            for path in sorted(blob_root.iterdir(), key=lambda item: item.name):
                add_to_tar(archive, path, path.relative_to(root).as_posix())
            for name in ("index.json", "oci-layout"):
                add_to_tar(archive, root / name, name)
        os.chmod(temporary_output, 0o600)
        temporary_output.replace(output)

    return {
        "reference": reference,
        "tag_name": tag_name,
        "archive_sha256": sha256_file(output),
        "archive_size": output.stat().st_size,
        "blob_count": len(descriptors),
        "platform": "linux/amd64",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", required=True)
    parser.add_argument("--tag-name", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--summary", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        summary = build_archive(args.reference, args.tag_name, args.output)
    except (ExportError, HTTPError, URLError, json.JSONDecodeError, OSError) as exc:
        print(f"[FAIL] OCI export: {exc}")
        return 1
    if args.summary:
        args.summary.parent.mkdir(parents=True, exist_ok=True)
        args.summary.write_text(json.dumps(summary, sort_keys=True) + "\n", encoding="utf-8")
        os.chmod(args.summary, 0o600)
    print(
        "[PASS] OCI export: digest, descriptor sizes, blob hashes, and linux/amd64 config verified; "
        f"blobs={summary['blob_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
