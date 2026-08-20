---
name: gauntlet-loop
description: Bounded, adversarial, evidence-driven multi-candidate improvement protocol for difficult quality boundaries, architectural trade-offs, reference-comparable designs, and high-value non-regression requirements. Uses isolated candidate generation, independent harsh critics, blind comparison, counterexample tracking, and hard invariant enforcement. Use when the user requests "/gauntlet-loop", "run gauntlet", "adversarial evaluation", or when standard iterative loops plateau on complex quality thresholds.
---

# AI OS Gauntlet Loop (v1)

A bounded, adversarial, evidence-driven multi-candidate improvement protocol.

The Gauntlet Loop is designed for tasks where standard single-threaded iteration plateaus, where multiple viable architectures or implementations compete, or where meeting a difficult quality boundary requires independent, un-blinded counterexample search and strict non-regression enforcement.

---

## Stage 0 — Routing Gate

Before initiating a Gauntlet run, evaluate if the task warrants adversarial multi-candidate overhead:

### Use Gauntlet When:
- Multiple plausible candidate architectures or implementations exist.
- A difficult quality boundary exists with high subjective or objective stakes.
- A reference-comparable artifact (design, spec, benchmark, gold standard) is available.
- High-value non-regression requirements apply (security, latency, correctness, accessibility).
- Standard iterative loops (e.g. `fable-loop`) have plateaued or failed repeatedly.
- The owner explicitly invokes `/gauntlet-loop` or requests an adversarial gauntlet.

### Reject Gauntlet (Return to Normal Execution) For:
- Mechanical edits, syntax repairs, renames, typos, or localized refactoring.
- Deterministic bug fixes with existing unambiguous unit tests.
- Factual question answering, documentation lookup, or routine code audits.
- Situations where no defensible reference bar or evaluation rubric can be defined.

*Detailed routing decision tree: see [references/ROUTING.md](references/ROUTING.md).*

---

## Stage 1 — Define the Bar

Before any builder operates, freeze the evaluation specification:

1. **GOAL:** Explicit functional objective and scope boundary.
2. **REFERENCE_BAR:** Concrete reference artifact, benchmark, gold standard, or specification.
   - *If no defensible reference bar can be defined, STOP immediately with:*
     `GAUNTLET_BLOCKED_REFERENCE_BAR_UNDEFINED`
3. **HARD_INVARIANTS:** Non-negotiable binary constraints (correctness, safety, security, build integrity, ABI stability).
4. **TARGET_DIMENSIONS:** Quantifiable or observable properties to improve (e.g. latency, elegance, maintainability, visual fidelity).
5. **PROTECTED_DIMENSIONS:** Existing properties that must NOT regress under any optimization.
6. **EVIDENCE_REQUIRED:** Exact tests, profiling data, renders, or outputs required to substantiate claims.
7. **RESOURCE_BUDGET:** Maximum rounds (default: 3), maximum candidate fan-out per round (default: 2, max: 3), and token budget.
8. **STOP_RULES:** Explicit convergence and abort criteria.

*Use [templates/GAUNTLET_SPEC.md](templates/GAUNTLET_SPEC.md) to record the frozen bar.*

---

## Stage 2 — Baseline Evidence

Before modifying code or generating candidates, capture pre-mutation baseline evidence against the frozen rubric whenever comparison is meaningful:
- Run existing test suites, benchmarks, linters, or visual captures.
- Record baseline metrics on all Target and Protected dimensions.
- If no baseline exists (greenfield task), declare `BASELINE = GREENFIELD`.

---

## Stage 3 — Isolated Candidate Generation

Generate the minimum necessary candidate solutions independently:
- **Default:** 1 candidate when the search space is narrow; 2 candidates when distinct architectural/design strategies exist; 3 candidates maximum only when high information gain justifies the cost.
- **Isolation Constraint:** Builders receive identical frozen specifications ([templates/BUILDER_BRIEF.md](templates/BUILDER_BRIEF.md)) and work in parallel without knowledge of each other's work or real-time critic feedback.
- **Mandatory Child Rule:** Every builder prompt must enforce:
  `NESTED_ORCHESTRATION = PROHIBITED`

---

## Stage 4 — Independent Harsh Critic

A builder cannot certify its own output. Evaluation must be performed by an independent critic using fresh or role-separated context ([templates/CRITIC_BRIEF.md](templates/CRITIC_BRIEF.md)):
1. **Hard Invariants First:** Test binary non-negotiables immediately. Any hard invariant failure disqualifies the candidate or forces an immediate fix.
2. **Counterexample Search:** The critic must aggressively search for edge cases, failure inputs, visual regressions, architectural flaws, or spec contradictions.
3. **Evidence vs Interpretation:** The critic must cite tangible evidence (test output, diff line, benchmark number, visual capture). Unsupported subjective praise is rejected.
4. **Epistemic Honesty:** The critic must classify unverified claims as `UNKNOWN`, not `FAIL` or `PASS`.

---

## Stage 5 — Blind Comparison

When host capabilities permit, conceal candidate identities (Candidate Alpha vs Candidate Beta) and evaluate candidates against the reference bar and each other:
- Evaluate strictly against the frozen rubric defined in Stage 1.
- Moving the goalposts after inspecting candidate outputs is prohibited.
- Rank candidates by hard invariant compliance first, protected dimension preservation second, and target dimension gains third.

*See [references/EVALUATION.md](references/EVALUATION.md) for scoring and comparison matrices.*

---

## Stage 6 — Counterexample Extraction & Selection

Select the surviving candidate and isolate its **strongest unresolved counterexample**:
- Do not ask broadly: *"How can this be better?"*
- Ask specifically: *"What is the strongest concrete evidence that this candidate has not yet met the reference bar?"*

---

## Stage 7 — Surgical Next Mutation

If the surviving candidate has not yet met the reference bar and budget remains:
- Design the next iteration targeting the **smallest possible mutation surface** required to eliminate the primary counterexample.
- Avoid wholesale rewrites when a targeted, hypothesis-driven repair suffices.

---

## Stage 8 — Non-Regression Enforcement

All previously verified strengths and baseline measurements become protected dimensions:
- A performance or aesthetic gain in a target dimension cannot silently break correctness, security, backwards compatibility, or accessibility.
- Aggregate scores cannot compensate for hard invariant violations (`REJECTED_NON_REGRESSION`).

---

## Stage 9 — Bounded Convergence & Stop

The loop MUST terminate deterministically. Valid terminal stop states:

### Successful Stop:
- `GAUNTLET_ACCEPTED` — All hard invariants satisfied, reference bar achieved, zero critical counterexamples remain, zero protected dimensions regressed.

### Bounded Non-Successful Stops:
- `GAUNTLET_BUDGET_EXHAUSTED` — Maximum iterations or resource budget reached before meeting the reference bar.
- `GAUNTLET_PLATEAU` — Two consecutive rounds yield negligible measurable delta on the primary counterexample.
- `GAUNTLET_INSUFFICIENT_EVIDENCE` — Available tools/runtime cannot verify or refute the required claims.
- `GAUNTLET_EVALUATOR_DISAGREEMENT` — Irreconcilable conflict between independent critic evaluations.
- `GAUNTLET_REFERENCE_GAP` — Target spec or reference artifact contains internal contradictions.
- `GAUNTLET_SPEC_AMBIGUITY` — Requirements lack specificity needed to judge candidate correctness.
- `GAUNTLET_CRITICAL_BLOCKER` — Unresolvable external dependency, infrastructure failure, or missing tool.
- `GAUNTLET_RECURSIVE_REPAIR` — Iteration attempts circular patches without addressing the root failure.
- `GAUNTLET_OWNER_STOP` — Explicit user abort.

---

## Absolute Non-Nesting Invariant

**Only the root orchestrator owns the loop.**
- Child subagents (builders, critics, evaluators) are workers, not orchestrators.
- If any child attempts to invoke `gauntlet-loop`, `fable-loop`, or launch its own recursive orchestration sub-tree, the orchestrator must immediately terminate that child with:
  `GAUNTLET_CHILD_LOOP_VIOLATION`
- Do not attempt recursive recovery of broken recursion.

---

## Subagent Independence Reporting

The orchestrator must declare the achieved independence level in all evaluations:
- **L0:** Single-context self-review (lowest rigor, used only when subagents are unavailable).
- **L1:** Role-separated sequential prompting in the same session.
- **L2:** Fresh-context isolated subagent worker.
- **L3:** Isolated subagent without candidate provenance or author identity.
- **L4:** Blind evaluator receiving only candidate outputs and a sealed, frozen rubric.

---

## AI OS Integration & Fable Interoperability

`gauntlet-loop` operates alongside existing AI OS methods without merging or collision:
- `fable-method`: Rules of engagement, behavioral discipline, intent and recall gates.
- `fable-loop`: Standard linear orchestration with bounded evidence gathering and attacker verification.
- `fable-judge`: Post-execution independent claim verification and audit.
- `gauntlet-loop`: Multi-candidate adversarial tournament and high-stakes quality boundary protocol.

*Cross-nesting rules:*
- Fable Loop inside Gauntlet Worker = **PROHIBITED**
- Gauntlet Loop inside Fable Worker = **PROHIBITED**
- Gauntlet Loop inside Gauntlet Worker = **PROHIBITED**

*See [references/FABLE_INTEROP.md](references/FABLE_INTEROP.md) for full interoperability governance.*
