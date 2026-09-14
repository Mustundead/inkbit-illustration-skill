#!/usr/bin/env python3
"""Offline package checks. This does not evaluate rendered illustration quality."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit("Install development dependencies: python -m pip install -r requirements-dev.txt")


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    skill = root / "skills/inkbit-illustration"

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    pairs = [
        (root / "README.md", root / "README.zh-CN.md"),
        (skill / "SKILL.md", skill / "SKILL.zh-CN.md"),
        *[(skill / f"references/{name}.md", skill / f"references/{name}.zh-CN.md")
          for name in ("style-guide", "prompts", "quality")],
    ]
    for pair in pairs:
        for file in pair:
            require(file.is_file(), f"Missing locale file: {file.relative_to(root)}")

    versions = []
    for file, language in ((skill / "SKILL.md", "en"), (skill / "SKILL.zh-CN.md", "zh-CN")):
        if not file.is_file():
            continue
        text = file.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        require(match is not None, f"Invalid frontmatter: {file.name}")
        if not match:
            continue
        try:
            data = yaml.safe_load(match[1])
        except yaml.YAMLError as exc:
            errors.append(f"Invalid YAML: {file.name}: {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"Frontmatter must be a mapping: {file.name}")
            continue
        name, description = data.get("name"), data.get("description")
        require(name == skill.name, f"Skill name must match directory: {file.name}")
        require(isinstance(name, str) and len(name) <= 64 and bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)), f"Invalid skill name: {file.name}")
        require(isinstance(description, str) and 1 <= len(description) <= 1024, f"Invalid description: {file.name}")
        require(data.get("license") == "CC-BY-4.0", f"License mismatch: {file.name}")
        metadata = data.get("metadata", {})
        require(isinstance(metadata, dict) and all(isinstance(v, str) for v in metadata.values()), f"Metadata values must be strings: {file.name}")
        if isinstance(metadata, dict):
            require(metadata.get("language") == language, f"Language mismatch: {file.name}")
            versions.append(metadata.get("version"))
        require("[TODO:" not in text, f"Unfinished scaffold: {file.name}")

    for name in ("LICENSE", "NOTICE.md"):
        require((root / name).is_file(), f"Missing repository {name}")
        require((skill / name).is_file(), f"Missing distributable {name}")
    if (root / "LICENSE").exists() and (skill / "LICENSE").exists():
        require((root / "LICENSE").read_bytes() == (skill / "LICENSE").read_bytes(), "License copies differ")

    for file in root.rglob("*.md"):
        if any(part in (".git", ".venv", "dist") for part in file.relative_to(root).parts):
            continue
        content = file.read_text(encoding="utf-8")
        require(not re.search(r"/Users/|/home/[A-Za-z0-9_-]+/|codex://threads/|\.codex/generated_images/", content), f"Private local reference: {file.relative_to(root)}")
        for link in re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", content):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", link) or link.startswith("#"):
                continue
            target = (file.parent / link.split("#", 1)[0]).resolve()
            require(target.is_relative_to(root.resolve()), f"Link escapes package: {file.relative_to(root)} -> {link}")
            require(target.exists(), f"Broken link: {file.relative_to(root)} -> {link}")
            if file.is_relative_to(skill):
                require(target.is_relative_to(skill.resolve()), f"Skill link escapes standalone folder: {file.name} -> {link}")

    try:
        manifest = json.loads((skill / "assets/provenance.json").read_text(encoding="utf-8"))
        versions.append(manifest["version"])
        for entry in manifest["assets"]:
            file = (skill / entry["file"]).resolve()
            if not file.is_relative_to(skill.resolve()):
                errors.append("Asset path escapes skill")
                continue
            require(file.is_file(), f"Missing asset: {entry['file']}")
            if file.is_file():
                require(hashlib.sha256(file.read_bytes()).hexdigest() == entry["sha256"], f"Asset hash mismatch: {entry['file']}")
            require(bool(entry.get("provenance")) and bool(entry.get("license")), "Missing asset provenance/license")
        require(bool(manifest["assets"]), "No declared reference asset")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"Invalid asset manifest: {exc}")
    require(len(versions) == 3 and len(set(versions)) == 1 and isinstance(versions[0], str), "Version mismatch")

    try:
        ui = yaml.safe_load((skill / "agents/openai.yaml").read_text(encoding="utf-8"))["interface"]
        require("$inkbit-illustration" in ui["default_prompt"], "UI prompt must invoke skill")
        require(25 <= len(ui["short_description"]) <= 64, "UI short description must be 25–64 characters")
    except (OSError, yaml.YAMLError, KeyError, TypeError) as exc:
        errors.append(f"Invalid UI metadata: {exc}")
    try:
        cases = json.loads((root / "evals/cases.json").read_text(encoding="utf-8"))["cases"]
        require(len({case["id"] for case in cases}) == len(cases), "Duplicate evaluation IDs")
        require(all(case.get("input") and case.get("expectations") for case in cases), "Incomplete evaluation case")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"Invalid evaluation cases: {exc}")
    return errors


if __name__ == "__main__":
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    issues = validate(root)
    if issues:
        print("\n".join(f"FAIL: {issue}" for issue in issues))
        raise SystemExit(1)
    print("PASS: metadata, bilingual file pairs, package links, licenses, asset hashes, UI metadata, evaluation cases")
    print("Boundary: no rendered-art quality or cross-host runtime claim")
