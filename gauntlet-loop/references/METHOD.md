# AI OS Gauntlet Loop — Operational Methodology (Stages 0–9)

## Overview
The Gauntlet Loop executes a structured, adversarial tournament between candidate solutions against an explicit reference bar. It eliminates cognitive confirmation bias by isolating builders, separating critics, concealing candidate identities, and enforcing hard non-regression boundaries.

---

## Detailed Stage Protocol

### Stage 0: Routing Gate
The orchestrator must verify that the task justifies adversarial overhead:
- **Positive Indicators:** Multi-candidate search space, architectural trade-offs, subjective visual quality boundaries, critical non-regression requirements, or repeated failure under standard loops.
- **Negative Indicators:** Mechanical refactoring, single-line patches, deterministic unit test fixes, factual lookups.
- **Action:** If negative indicators dominate, immediately bypass Gauntlet and return to direct or Fable Method execution.

### Stage 1: Define the Bar
Freeze all parameters before generating code or design artifacts:
1. **Goal:** One-sentence functional mandate with explicit file/system boundaries.
2. **Reference Bar:** Concrete benchmark (e.g. baseline code, design mockup, competitor standard, specification RFC). If none exists, abort with `GAUNTLET_BLOCKED_REFERENCE_BAR_UNDEFINED`.
3. **Hard Invariants:** Binary pass/fail criteria (compilation, memory safety, security constraints, deterministic test passing, ABI stability).
4. **Target Dimensions:** Continuously scored dimensions (e.g. latency, memory footprint, visual hierarchy, ergonomics).
5. **Protected Dimensions:** Baseline dimensions that must not regress (e.g. existing test suite pass rate, backwards compatibility).
6. **Resource Budget:** Max iterations (default 3), candidate concurrency (default 2, max 3), token ceiling.
7. **Stop Rules:** Explicit termination states.

### Stage 2: Baseline Evidence
Capture pre-mutation evidence on all dimensions. Record concrete metrics:
- Test pass count and coverage.
- CPU/Memory/Latency profiles.
- Visual screenshots or DOM states.
- Static analysis and lint diagnostics.

### Stage 3: Isolated Candidate Generation
Dispatch builders in parallel.
- **Prompt Isolation:** Deliver only the frozen spec ([templates/BUILDER_BRIEF.md](../templates/BUILDER_BRIEF.md)).
- **No Cross-Pollination:** Candidate Alpha must not inspect Candidate Beta's scratchpad or implementation.
- **Non-Nesting Enforced:** Every brief contains `NESTED_ORCHESTRATION = PROHIBITED`.

### Stage 4: Independent Harsh Critic
Dispatch a fresh or role-separated critic ([templates/CRITIC_BRIEF.md](../templates/CRITIC_BRIEF.md)):
- **Refutation Orientation:** The critic's objective is to refute candidate claims and uncover counterexamples.
- **Order of Evaluation:**
  1. Hard Invariants (Immediate disqualification on failure).
  2. Protected Dimensions (Flag any regression).
  3. Target Dimensions (Measure differential delta).
- **Epistemic Classification:** Claims without concrete empirical backing are labelled `UNKNOWN`.

### Stage 5: Blind Comparison
When technically supported by the host harness, the evaluator receives candidate outputs stripped of author tags (Candidate Alpha vs Candidate Beta):
- Evaluate strictly against the frozen Stage 1 rubric.
- Calculate net ranking based on hard invariant compliance, non-regression, and target gains.

### Stage 6: Counterexample Extraction
Isolate the primary failing counterexample of the leading candidate:
- State the counterexample concretely: input, expected behavior, observed failure, and root mechanism.

### Stage 7: Surgical Next Mutation
Formulate the next round as a targeted repair:
- Focus solely on eliminating the primary counterexample.
- Constrain mutation blast radius to prevent collateral regression.

### Stage 8: Non-Regression Check
Verify that the repair did not regress previously verified strengths:
- If a protected dimension fails, reject the mutation (`REJECTED_NON_REGRESSION`) and revert.

### Stage 9: Bounded Stop
Evaluate termination criteria:
- `GAUNTLET_ACCEPTED`: Reference bar reached, all hard invariants met, zero open critical counterexamples, zero regressions.
- `GAUNTLET_BUDGET_EXHAUSTED`: Maximum iterations reached without reaching the bar.
- `GAUNTLET_PLATEAU`: Two consecutive rounds show zero measurable delta on target counterexamples.
- `GAUNTLET_INSUFFICIENT_EVIDENCE`: Verification tools cannot conclusively evaluate the candidates.
- `GAUNTLET_EVALUATOR_DISAGREEMENT`: Unresolvable conflict between independent critics.
- `GAUNTLET_REFERENCE_GAP` / `GAUNTLET_SPEC_AMBIGUITY`: Reference or specification is contradictory or under-specified.
- `GAUNTLET_CRITICAL_BLOCKER`: Environmental or dependency block.
- `GAUNTLET_RECURSIVE_REPAIR`: Circular mutation loop detected.
- `GAUNTLET_OWNER_STOP`: Aborted by owner.
