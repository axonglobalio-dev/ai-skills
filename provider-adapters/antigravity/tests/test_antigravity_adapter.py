#!/usr/bin/env python3
"""
Test Suite for Antigravity Skill Mirror Adapter
Validates synchronization, isolation, hash manifests, drift detection, and idempotency.
"""

import hashlib
import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sync_skill import (
    compute_sha256,
    parse_frontmatter,
    scan_source_files,
    sync_skill,
    verify_target_drift,
    MANIFEST_FILENAME,
)

class TestAntigravityAdapter(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp(prefix="ai_os_adapter_test_")
        self.mock_canonical_root = os.path.join(self.test_dir, "canonical")
        self.mock_target_root = os.path.join(self.test_dir, "target")
        os.makedirs(self.mock_canonical_root, exist_ok=True)
        os.makedirs(self.mock_target_root, exist_ok=True)

        # Setup mock skill
        self.skill_name = "test-skill"
        self.source_dir = os.path.join(self.mock_canonical_root, self.skill_name)
        os.makedirs(self.source_dir, exist_ok=True)
        os.makedirs(os.path.join(self.source_dir, "references"), exist_ok=True)

        self.skill_md_content = (
            "---\n"
            "name: test-skill\n"
            "description: Test skill description for unit testing adapter.\n"
            "---\n\n"
            "# Test Skill Content\n"
        )
        with open(os.path.join(self.source_dir, "SKILL.md"), "w") as f:
            f.write(self.skill_md_content)

        with open(os.path.join(self.source_dir, "references", "DOC.md"), "w") as f:
            f.write("# Reference Doc\nSome details here.\n")

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_a_canonical_to_physical_mirror(self):
        """A: Verify sync creates physical directory and copies files."""
        success, result = sync_skill(self.mock_canonical_root, self.mock_target_root, self.skill_name)
        self.assertTrue(success)
        target_dir = os.path.join(self.mock_target_root, self.skill_name)
        self.assertTrue(os.path.exists(target_dir))
        self.assertTrue(os.path.isdir(target_dir))

    def test_b_target_is_not_symlink(self):
        """B: Verify target is a real physical directory and NOT a symlink."""
        # Pre-create symlink to test replacement
        target_dir = os.path.join(self.mock_target_root, self.skill_name)
        os.symlink(self.source_dir, target_dir)
        self.assertTrue(os.path.islink(target_dir))

        # Run sync
        success, result = sync_skill(self.mock_canonical_root, self.mock_target_root, self.skill_name)
        self.assertTrue(success)
        self.assertFalse(os.path.islink(target_dir))
        self.assertTrue(os.path.isdir(target_dir))

    def test_c_all_files_hash_match(self):
        """C: Verify all files in mirror match source byte-for-byte."""
        sync_skill(self.mock_canonical_root, self.mock_target_root, self.skill_name)
        source_hashes = scan_source_files(self.source_dir)
        target_dir = os.path.join(self.mock_target_root, self.skill_name)
        target_hashes = scan_source_files(target_dir)

        self.assertEqual(source_hashes, target_hashes)

    def test_d_manifest_hashes_correct(self):
        """D: Verify manifest exists and contains accurate SHA-256 signatures."""
        sync_skill(self.mock_canonical_root, self.mock_target_root, self.skill_name)
        target_dir = os.path.join(self.mock_target_root, self.skill_name)
        manifest_path = os.path.join(target_dir, MANIFEST_FILENAME)
        self.assertTrue(os.path.exists(manifest_path))

        with open(manifest_path, "r") as f:
            manifest = json.load(f)

        self.assertEqual(manifest["skill"], self.skill_name)
        self.assertEqual(manifest["provider"], "antigravity")
        self.assertTrue(manifest["generated"])

        for rel_path, expected_hash in manifest["files"].items():
            actual_file = os.path.join(target_dir, rel_path)
            self.assertTrue(os.path.exists(actual_file))
            self.assertEqual(compute_sha256(actual_file), expected_hash)

    def test_e_check_returns_in_sync(self):
        """E: Verify --check returns IN_SYNC when clean."""
        sync_skill(self.mock_canonical_root, self.mock_target_root, self.skill_name)
        status, report = verify_target_drift(self.mock_canonical_root, self.mock_target_root, self.skill_name)
        self.assertEqual(status, "IN_SYNC")

    def test_f_intentional_drift_detected(self):
        """F: Verify modified file or added file triggers DRIFT_DETECTED."""
        sync_skill(self.mock_canonical_root, self.mock_target_root, self.skill_name)
        target_dir = os.path.join(self.mock_target_root, self.skill_name)

        # Mutate a file in target
        with open(os.path.join(target_dir, "SKILL.md"), "a") as f:
            f.write("\n# Mutated Content\n")

        status, report = verify_target_drift(self.mock_canonical_root, self.mock_target_root, self.skill_name)
        self.assertEqual(status, "DRIFT_DETECTED")

    def test_g_sync_restores_drift(self):
        """G: Verify sync overwrites drifted mirror back to IN_SYNC."""
        sync_skill(self.mock_canonical_root, self.mock_target_root, self.skill_name)
        target_dir = os.path.join(self.mock_target_root, self.skill_name)

        # Tamper target
        with open(os.path.join(target_dir, "references", "DOC.md"), "w") as f:
            f.write("corrupted content")

        status, _ = verify_target_drift(self.mock_canonical_root, self.mock_target_root, self.skill_name)
        self.assertEqual(status, "DRIFT_DETECTED")

        # Re-sync
        success, _ = sync_skill(self.mock_canonical_root, self.mock_target_root, self.skill_name)
        self.assertTrue(success)

        status, _ = verify_target_drift(self.mock_canonical_root, self.mock_target_root, self.skill_name)
        self.assertEqual(status, "IN_SYNC")

    def test_h_canonical_source_remains_untouched(self):
        """H: Verify sync never modifies canonical source files."""
        src_hashes_before = scan_source_files(self.source_dir)
        sync_skill(self.mock_canonical_root, self.mock_target_root, self.skill_name)
        src_hashes_after = scan_source_files(self.source_dir)
        self.assertEqual(src_hashes_before, src_hashes_after)

    def test_i_unrelated_target_entries_untouched(self):
        """I: Verify unrelated sibling entries in target root are untouched."""
        unrelated_file = os.path.join(self.mock_target_root, "other_skill.txt")
        with open(unrelated_file, "w") as f:
            f.write("unrelated")

        sync_skill(self.mock_canonical_root, self.mock_target_root, self.skill_name)
        self.assertTrue(os.path.exists(unrelated_file))
        with open(unrelated_file, "r") as f:
            self.assertEqual(f.read(), "unrelated")

if __name__ == "__main__":
    unittest.main()
