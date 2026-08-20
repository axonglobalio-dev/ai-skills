# AI OS Gauntlet Loop Contract Verification Suite
# Tests contract rules, routing gates, evaluator invariants, and Cases A through H

import unittest
import os
import re

SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class GauntletDecisionEngine:
    """Reference simulator implementing the Gauntlet Loop v1 specification contract."""

    @staticmethod
    def evaluate_routing(task_type: str, has_multiple_candidates: bool, has_difficult_bar: bool, has_non_regression_req: bool, is_mechanical: bool, is_deterministic_fix: bool, reference_bar_defined: bool):
        if is_mechanical or is_deterministic_fix:
            return "GAUNTLET_NOT_JUSTIFIED"
        if not reference_bar_defined:
            return "GAUNTLET_BLOCKED_REFERENCE_BAR_UNDEFINED"
        if has_multiple_candidates or has_difficult_bar or has_non_regression_req:
            return "GAUNTLET_JUSTIFIED"
        return "GAUNTLET_NOT_JUSTIFIED"

    @staticmethod
    def check_child_invocation(prompt_text: str, child_commands: list):
        for cmd in child_commands:
            if "gauntlet-loop" in cmd or "fable-loop" in cmd:
                return "GAUNTLET_CHILD_LOOP_VIOLATION"
        return "CHILD_EXECUTION_PERMITTED"

    @staticmethod
    def evaluate_candidate(candidate_data: dict):
        # 1. Hard invariants
        if not candidate_data.get("hard_invariants_pass", True):
            return {"status": "REJECTED_HARD_INVARIANT_FAIL", "winner": False}
        
        # 2. Protected dimensions (non-regression)
        if candidate_data.get("protected_dimension_regressed", False):
            return {"status": "REJECTED_NON_REGRESSION", "winner": False}
        
        # 3. Evidence sufficiency
        if candidate_data.get("evidence_ambiguous", False):
            return {"status": "GAUNTLET_INSUFFICIENT_EVIDENCE", "winner": None}
            
        return {"status": "EVALUATION_SUCCESS", "score": candidate_data.get("target_score", 0)}

    @staticmethod
    def run_campaign_simulation(rounds: int, max_rounds: int, met_bar_round: int = None, plateau_round: int = None):
        for r in range(1, max_rounds + 1):
            if met_bar_round and r == met_bar_round:
                return "GAUNTLET_ACCEPTED"
            if plateau_round and r >= plateau_round + 1:
                return "GAUNTLET_PLATEAU"
        return "GAUNTLET_BUDGET_EXHAUSTED"


class GauntletContractTests(unittest.TestCase):

    def test_CASE_A_mechanical_rename(self):
        """CASE A: Mechanical rename -> Expected: GAUNTLET_NOT_JUSTIFIED"""
        verdict = GauntletDecisionEngine.evaluate_routing(
            task_type="rename_symbol",
            has_multiple_candidates=False,
            has_difficult_bar=False,
            has_non_regression_req=False,
            is_mechanical=True,
            is_deterministic_fix=False,
            reference_bar_defined=True
        )
        self.assertEqual(verdict, "GAUNTLET_NOT_JUSTIFIED")

    def test_CASE_B_architecture_candidates_with_hard_invariants(self):
        """CASE B: Two architecture candidates with hard invariants -> Expected: GAUNTLET_JUSTIFIED"""
        verdict = GauntletDecisionEngine.evaluate_routing(
            task_type="architecture_selection",
            has_multiple_candidates=True,
            has_difficult_bar=True,
            has_non_regression_req=True,
            is_mechanical=False,
            is_deterministic_fix=False,
            reference_bar_defined=True
        )
        self.assertEqual(verdict, "GAUNTLET_JUSTIFIED")

    def test_CASE_C_visual_ui_improvement_against_reference(self):
        """CASE C: Visual UI improvement against a supplied reference -> Expected: GAUNTLET_JUSTIFIED"""
        verdict = GauntletDecisionEngine.evaluate_routing(
            task_type="visual_ui_refinement",
            has_multiple_candidates=True,
            has_difficult_bar=True,
            has_non_regression_req=False,
            is_mechanical=False,
            is_deterministic_fix=False,
            reference_bar_defined=True
        )
        self.assertEqual(verdict, "GAUNTLET_JUSTIFIED")

    def test_CASE_D_builder_attempts_nested_gauntlet_call(self):
        """CASE D: Builder attempts to call gauntlet-loop -> Expected: GAUNTLET_CHILD_LOOP_VIOLATION"""
        verdict = GauntletDecisionEngine.check_child_invocation(
            prompt_text="NESTED_ORCHESTRATION = PROHIBITED",
            child_commands=["/gauntlet-loop --subtask", "run_tests"]
        )
        self.assertEqual(verdict, "GAUNTLET_CHILD_LOOP_VIOLATION")

    def test_CASE_E_iteration_reaches_budget_before_bar(self):
        """CASE E: Iteration reaches budget before bar -> Expected: GAUNTLET_BUDGET_EXHAUSTED"""
        terminal_state = GauntletDecisionEngine.run_campaign_simulation(
            rounds=3,
            max_rounds=3,
            met_bar_round=None
        )
        self.assertEqual(terminal_state, "GAUNTLET_BUDGET_EXHAUSTED")

    def test_CASE_F_insufficient_evidence_or_disagreement(self):
        """CASE F: Evidence cannot prove which candidate is better -> Expected: GAUNTLET_INSUFFICIENT_EVIDENCE"""
        eval_res = GauntletDecisionEngine.evaluate_candidate({
            "hard_invariants_pass": True,
            "protected_dimension_regressed": False,
            "evidence_ambiguous": True
        })
        self.assertEqual(eval_res["status"], "GAUNTLET_INSUFFICIENT_EVIDENCE")

    def test_CASE_G_candidate_improves_target_but_breaks_protected_invariant(self):
        """CASE G: Candidate improves target but breaks protected invariant -> Expected: REJECTED_NON_REGRESSION"""
        eval_res = GauntletDecisionEngine.evaluate_candidate({
            "hard_invariants_pass": True,
            "protected_dimension_regressed": True,  # Collateral regression
            "target_score": 98.5
        })
        self.assertEqual(eval_res["status"], "REJECTED_NON_REGRESSION")

    def test_CASE_H_no_usable_reference_bar(self):
        """CASE H: No usable reference/rubric can be established -> Expected: GAUNTLET_BLOCKED_REFERENCE_BAR_UNDEFINED"""
        verdict = GauntletDecisionEngine.evaluate_routing(
            task_type="vague_feature",
            has_multiple_candidates=True,
            has_difficult_bar=True,
            has_non_regression_req=False,
            is_mechanical=False,
            is_deterministic_fix=False,
            reference_bar_defined=False  # Undefined bar
        )
        self.assertEqual(verdict, "GAUNTLET_BLOCKED_REFERENCE_BAR_UNDEFINED")

    def test_skill_frontmatter_and_structure(self):
        """Verify SKILL.md has valid portable agent skill frontmatter and non-nesting directives."""
        skill_path = os.path.join(SKILL_ROOT, "SKILL.md")
        self.assertTrue(os.path.exists(skill_path), "SKILL.md must exist")
        
        with open(skill_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check YAML frontmatter bounds
        self.assertTrue(content.startswith("---\n"), "Must start with frontmatter")
        parts = content.split("---")
        self.assertGreaterEqual(len(parts), 3, "Frontmatter must be closed")
        frontmatter = parts[1]
        
        self.assertIn("name: gauntlet-loop", frontmatter)
        self.assertIn("description:", frontmatter)
        self.assertIn("NESTED_ORCHESTRATION = PROHIBITED", content)
        self.assertIn("GAUNTLET_CHILD_LOOP_VIOLATION", content)
        self.assertIn("GAUNTLET_ACCEPTED", content)
        self.assertIn("GAUNTLET_BUDGET_EXHAUSTED", content)

    def test_reference_and_template_files_present(self):
        """Verify all required references and templates exist with non-empty content."""
        expected_refs = ["METHOD.md", "ROUTING.md", "EVALUATION.md", "PROVIDERS.md", "FABLE_INTEROP.md", "PROVENANCE.md"]
        expected_tpls = ["GAUNTLET_SPEC.md", "BUILDER_BRIEF.md", "CRITIC_BRIEF.md", "EVALUATION.md", "CHECKPOINT.md"]
        
        for r in expected_refs:
            p = os.path.join(SKILL_ROOT, "references", r)
            self.assertTrue(os.path.exists(p), f"Missing reference: {r}")
            self.assertGreater(os.path.getsize(p), 100, f"Empty reference: {r}")

        for t in expected_tpls:
            p = os.path.join(SKILL_ROOT, "templates", t)
            self.assertTrue(os.path.exists(p), f"Missing template: {t}")
            self.assertGreater(os.path.getsize(p), 100, f"Empty template: {t}")


if __name__ == "__main__":
    unittest.main()
