# AI OS Gauntlet Loop — Evaluation & Scoring Protocol

## Evaluation Philosophy
1. **Adversarial by Default:** The critic seeks counterexamples, edge cases, and hidden regressions rather than confirming happy paths.
2. **Hard Invariants Dominate:** No amount of aesthetic polish or target dimension score can compensate for a single broken hard invariant.
3. **Evidence Over Rhetoric:** Every score or critique must be anchored in tangible runtime output, test assertions, profiling traces, or visual artifacts.

---

## Blind Comparison Protocol

When host capabilities permit (Independence Levels L3–L4):
1. **Anonymization:** Candidate solutions are tagged as `Candidate Alpha`, `Candidate Beta`, etc.
2. **Rubric Sealing:** The evaluation rubric is frozen in Stage 1 and cannot be modified post-hoc based on candidate features.
3. **Direct Pairwise Matrix:**
   - Candidate A vs Reference Bar
   - Candidate B vs Reference Bar
   - Candidate A vs Candidate B

---

## Scoring Matrix Format

| Dimension | Weight | Candidate Alpha | Candidate Beta | Reference Bar | Tangible Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Hard Invariants** | Binary (Pass/Fail) | PASS | PASS | PASS | `tests/unit_suite.py` (100% pass) |
| **Protected: Security** | Binary (Pass/Fail) | PASS | PASS | PASS | Static analysis (0 findings) |
| **Protected: Backward Compat** | Binary (Pass/Fail) | PASS | FAIL | PASS | API schema contract test |
| **Target: Latency (p99)** | 40% | 14.2ms (+12%) | 11.8ms (+28%) | 16.0ms | Benchmark run trace (10k ops) |
| **Target: Memory Footprint** | 30% | 42MB | 58MB | 45MB | Valgrind / Heap profiler trace |
| **Target: Maintainability** | 30% | High | Medium | High | Cyclomatic complexity & LoC |

---

## Counterexample Ranking
Critics must rank counterexamples by severity:
1. **Level 1 (Critical):** Violates a Hard Invariant or regresses a Protected Dimension.
2. **Level 2 (Major):** Causes a significant failure against the Reference Bar under plausible edge conditions.
3. **Level 3 (Minor):** Sub-optimal performance, styling discrepancy, or non-critical friction.

*Only the highest-ranked counterexample is forwarded to the next mutation round (Stage 7).*
