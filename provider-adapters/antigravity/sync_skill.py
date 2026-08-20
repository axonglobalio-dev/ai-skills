#!/usr/bin/env python3
"""
AI OS — Antigravity Physical Skill Mirror Adapter
Synchronizes canonical AI OS skills (~/.ai-skills/<skill>) to physical Antigravity
mirrors (~/.gemini/config/skills/<skill>) with cryptographic SHA-256 provenance manifests.
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from typing import Dict, Any, Tuple, Optional

MANIFEST_FILENAME = ".ai-os-mirror-manifest.json"
LEGACY_MANIFEST_FILENAME = ".gauntlet-ai-os-mirror.json"

DEFAULT_CANONICAL_ROOT = "/Users/jrcalaca/.ai-skills"
DEFAULT_TARGET_ROOT = "/Users/jrcalaca/.gemini/config/skills"

def compute_sha256(filepath: str) -> str:
    """Compute SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(65536)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()

def get_git_provenance(repo_path: str, skill_name: Optional[str] = None) -> Tuple[str, str]:
    """
    Get (canonical_skill_commit, source_repository_commit).
    canonical_skill_commit: last commit modifying the specific skill directory.
    source_repository_commit: HEAD commit of the source repository.
    """
    repo_commit = "UNKNOWN"
    skill_commit = "UNKNOWN"
    try:
        res_repo = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=True
        )
        repo_commit = res_repo.stdout.strip()
    except Exception:
        pass

    if skill_name:
        try:
            res_skill = subprocess.run(
                ["git", "log", "-1", "--format=%H", "--", skill_name],
                cwd=repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            out = res_skill.stdout.strip()
            if out:
                skill_commit = out
            else:
                skill_commit = repo_commit
        except Exception:
            skill_commit = repo_commit
    else:
        skill_commit = repo_commit

    return skill_commit, repo_commit

def parse_frontmatter(skill_md_path: str) -> Dict[str, str]:
    """Extract basic YAML frontmatter from SKILL.md without external dependencies."""
    if not os.path.exists(skill_md_path):
        raise FileNotFoundError(f"SKILL.md not found at {skill_md_path}")
    
    with open(skill_md_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if not content.startswith("---"):
        raise ValueError(f"SKILL.md at {skill_md_path} missing frontmatter start delimiter (---)")
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"SKILL.md at {skill_md_path} missing frontmatter closing delimiter (---)")
    
    frontmatter_text = parts[1]
    metadata = {}
    current_key = None
    multiline_value = []
    
    for line in frontmatter_text.splitlines():
        trimmed = line.strip()
        if not trimmed or trimmed.startswith("#"):
            continue
        if ":" in line and not line.startswith(" ") and not line.startswith("	"):
            if current_key and multiline_value:
                metadata[current_key] = " ".join(multiline_value).strip()
                multiline_value = []
            k, v = line.split(":", 1)
            current_key = k.strip()
            val_clean = v.strip()
            if val_clean in [">", ">-", "|", "|-"]:
                multiline_value = []
            elif val_clean:
                metadata[current_key] = val_clean.strip("\x27\x22")
                current_key = None
        elif current_key:
            multiline_value.append(trimmed)
            
    if current_key and multiline_value:
        metadata[current_key] = " ".join(multiline_value).strip()
        
    if "name" not in metadata or not metadata["name"]:
        raise ValueError("Frontmatter missing required 'name' field")
    if "description" not in metadata or not metadata["description"]:
        raise ValueError("Frontmatter missing required 'description' field")
        
    return metadata

def scan_source_files(source_dir: str) -> Dict[str, str]:
    """Scan all canonical source files and compute relative path -> sha256 map."""
    file_hashes = {}
    for root, dirs, files in os.walk(source_dir):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "__pycache__"]
        for file in sorted(files):
            if file.startswith(".") or file == ".DS_Store" or file.endswith(".pyc"):
                continue
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, source_dir)
            file_hashes[rel_path] = compute_sha256(full_path)
    return file_hashes

def verify_target_drift(canonical_root: str, target_root: str, skill_name: str) -> Tuple[str, Dict[str, Any]]:
    """Check if target mirror is in sync, drifted, or missing."""
    source_dir = os.path.join(canonical_root, skill_name)
    target_dir = os.path.join(target_root, skill_name)
    
    report = {
        "skill": skill_name,
        "source_dir": source_dir,
        "target_dir": target_dir,
        "source_exists": os.path.exists(source_dir),
        "target_exists": os.path.exists(target_dir),
        "target_is_symlink": os.path.islink(target_dir),
        "details": {}
    }
    
    if not os.path.exists(source_dir):
        report["status"] = "SOURCE_MISSING"
        return "SOURCE_MISSING", report
        
    skill_md = os.path.join(source_dir, "SKILL.md")
    if not os.path.exists(skill_md):
        report["status"] = "INVALID_SOURCE"
        report["details"]["error"] = "Source SKILL.md missing"
        return "INVALID_SOURCE", report
        
    try:
        parse_frontmatter(skill_md)
    except Exception as e:
        report["status"] = "INVALID_SOURCE"
        report["details"]["error"] = f"Invalid frontmatter: {e}"
        return "INVALID_SOURCE", report

    if not os.path.exists(target_dir):
        report["status"] = "TARGET_MISSING"
        return "TARGET_MISSING", report
        
    if os.path.islink(target_dir):
        report["status"] = "DRIFT_DETECTED"
        report["details"]["reason"] = f"Target is a symlink pointing to {os.readlink(target_dir)}"
        return "DRIFT_DETECTED", report
        
    manifest_path = os.path.join(target_dir, MANIFEST_FILENAME)
    if not os.path.exists(manifest_path):
        manifest_path = os.path.join(target_dir, LEGACY_MANIFEST_FILENAME)
        
    if not os.path.exists(manifest_path):
        report["status"] = "DRIFT_DETECTED"
        report["details"]["reason"] = "Target missing provenance manifest"
        return "DRIFT_DETECTED", report
        
    try:
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest_data = json.load(f)
    except Exception as e:
        report["status"] = "DRIFT_DETECTED"
        report["details"]["reason"] = f"Corrupted manifest: {e}"
        return "DRIFT_DETECTED", report
        
    source_hashes = scan_source_files(source_dir)
    target_hashes = scan_source_files(target_dir)
    
    mismatches = []
    for rel_path, src_hash in source_hashes.items():
        tgt_hash = target_hashes.get(rel_path)
        if tgt_hash is None:
            mismatches.append(f"Missing file in target: {rel_path}")
        elif tgt_hash != src_hash:
            mismatches.append(f"Hash mismatch for {rel_path}: src={src_hash[:8]} tgt={tgt_hash[:8]}")
            
    for rel_path in target_hashes:
        if rel_path not in source_hashes:
            mismatches.append(f"Extraneous file in target: {rel_path}")
            
    if mismatches:
        report["status"] = "DRIFT_DETECTED"
        report["details"]["mismatches"] = mismatches
        return "DRIFT_DETECTED", report
        
    report["status"] = "IN_SYNC"
    report["details"]["file_count"] = len(source_hashes)
    report["details"]["canonical_skill_commit"] = manifest_data.get("canonical_skill_commit", manifest_data.get("source_git_commit"))
    report["details"]["source_repository_commit"] = manifest_data.get("source_repository_commit", manifest_data.get("source_git_commit"))
    return "IN_SYNC", report

def sync_skill(canonical_root: str, target_root: str, skill_name: str, force: bool = False) -> Tuple[bool, Dict[str, Any]]:
    """Deterministically mirror canonical skill to physical Antigravity location."""
    source_dir = os.path.join(canonical_root, skill_name)
    target_dir = os.path.join(target_root, skill_name)
    
    if not os.path.exists(source_dir):
        return False, {"error": f"Source canonical directory not found: {source_dir}", "status": "SOURCE_MISSING"}
        
    skill_md = os.path.join(source_dir, "SKILL.md")
    if not os.path.exists(skill_md):
        return False, {"error": f"SKILL.md not found in source: {skill_md}", "status": "INVALID_SOURCE"}
        
    try:
        frontmatter = parse_frontmatter(skill_md)
    except Exception as e:
        return False, {"error": f"Invalid SKILL.md frontmatter: {e}", "status": "INVALID_SOURCE"}
        
    source_hashes = scan_source_files(source_dir)
    canonical_commit, repo_commit = get_git_provenance(canonical_root, skill_name)
    
    os.makedirs(target_root, exist_ok=True)
    
    # Stage into temporary directory in target_root to allow atomic replacement
    staging_dir = tempfile.mkdtemp(prefix=f".tmp_mirror_{skill_name}_", dir=target_root)
    
    try:
        # Copy all files to staging directory
        for rel_path, src_hash in source_hashes.items():
            src_file = os.path.join(source_dir, rel_path)
            dst_file = os.path.join(staging_dir, rel_path)
            os.makedirs(os.path.dirname(dst_file), exist_ok=True)
            shutil.copy2(src_file, dst_file)
            staged_hash = compute_sha256(dst_file)
            if staged_hash != src_hash:
                raise ValueError(f"Staging hash verification failed for {rel_path}")
                
        # Generate mirror manifest with explicit dual provenance
        manifest_data = {
            "schema_version": 1,
            "provider": "antigravity",
            "skill": skill_name,
            "source_authority": os.path.abspath(source_dir),
            "canonical_skill_commit": canonical_commit,
            "source_repository_commit": repo_commit,
            "source_git_commit": canonical_commit,
            "canonical_skill_version": "v1.0.0",
            "generated": True,
            "do_not_edit_notice": "DO NOT EDIT GENERATED ANTIGRAVITY MIRROR. Canonical edits belong in ~/.ai-skills/",
            "files": source_hashes
        }
        
        manifest_path = os.path.join(staging_dir, MANIFEST_FILENAME)
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest_data, f, indent=2)
            
        # Verify staged content integrity
        staged_hashes = scan_source_files(staging_dir)
        for rel_path, src_hash in source_hashes.items():
            if staged_hashes.get(rel_path) != src_hash:
                raise ValueError(f"Pre-swap staged hash check failed for {rel_path}")
                
        # Handle existing target
        if os.path.islink(target_dir):
            target_link_dest = os.readlink(target_dir)
            if not force and os.path.abspath(target_link_dest) != os.path.abspath(source_dir):
                raise ValueError(f"Target symlink points to unexpected location: {target_link_dest}")
            os.unlink(target_dir)
        elif os.path.isdir(target_dir):
            backup_dir = tempfile.mkdtemp(prefix=f".backup_{skill_name}_", dir=target_root)
            os.replace(target_dir, os.path.join(backup_dir, "old"))
            shutil.rmtree(backup_dir, ignore_errors=True)
        elif os.path.exists(target_dir):
            os.remove(target_dir)
            
        # Atomic replace
        os.replace(staging_dir, target_dir)
        
        # Verify post-sync state
        if os.path.islink(target_dir):
            raise RuntimeError("Target unexpectedly remains a symlink after sync")
            
        final_hashes = scan_source_files(target_dir)
        for rel_path, src_hash in source_hashes.items():
            if final_hashes.get(rel_path) != src_hash:
                raise RuntimeError(f"Final target verification failed for {rel_path}")
                
        status_code, drift_report = verify_target_drift(canonical_root, target_root, skill_name)
        if status_code != "IN_SYNC":
            raise RuntimeError(f"Post-sync drift check returned {status_code}")
            
        return True, {
            "status": "SYNC_SUCCESSFUL",
            "skill": skill_name,
            "target_path": target_dir,
            "canonical_skill_commit": canonical_commit,
            "source_repository_commit": repo_commit,
            "file_count": len(source_hashes),
            "files": list(source_hashes.keys())
        }
    except Exception as e:
        if os.path.exists(staging_dir):
            shutil.rmtree(staging_dir, ignore_errors=True)
        return False, {"status": "SYNC_FAILED", "error": str(e)}

def main():
    parser = argparse.ArgumentParser(description="AI OS Antigravity Skill Mirror Sync Adapter")
    parser.add_argument("skill", help="Name of skill to sync (e.g. gauntlet-loop)")
    parser.add_argument("--check", action="store_true", help="Check drift without mutating")
    parser.add_argument("--canonical-root", default=DEFAULT_CANONICAL_ROOT, help="Path to canonical AI OS root")
    parser.add_argument("--target-root", default=DEFAULT_TARGET_ROOT, help="Path to Antigravity skills target root")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    parser.add_argument("--force", action="store_true", help="Force overwrite even if target symlink destination differs")
    
    args = parser.parse_args()
    
    if args.check:
        status, report = verify_target_drift(args.canonical_root, args.target_root, args.skill)
        if args.json:
            print(json.dumps(report, indent=2))
        else:
            print(f"STATUS: {status}")
            if status != "IN_SYNC":
                print(f"Details: {report.get('details')}")
        sys.exit(0 if status == "IN_SYNC" else 1)
    else:
        success, result = sync_skill(args.canonical_root, args.target_root, args.skill, force=args.force)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if success:
                print(f"SUCCESS: Mirrored {args.skill} to {result.get('target_path')}")
                print(f"  Canonical Skill Commit: {result.get('canonical_skill_commit')}")
                print(f"  Source Repo HEAD Commit: {result.get('source_repository_commit')}")
                print(f"  Files ({result.get('file_count')}): {result.get('files')}")
            else:
                print(f"FAILED: {result.get('error')}")
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
