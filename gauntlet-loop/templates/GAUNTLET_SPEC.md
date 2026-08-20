# Gauntlet Specification

## 1. Objective & Scope
- **Goal:** [Concise functional goal statement]
- **Target Surfaces:** [Exact files, directories, or endpoints allowed to change]
- **Out-of-Scope:** [Explicitly excluded surfaces and behaviors]

---

## 2. Reference Bar
- **Reference Type:** [Benchmark / Reference File / Golden Mockup / Spec RFC]
- **Reference Location / URI:** [file:///path/to/reference or inline description]
- **Bar Description:** [Exact target criteria that defines meeting the bar]

---

## 3. Hard Invariants (Binary Non-Negotiables)
- [ ] Invariant 1: [e.g. Must compile with 0 warnings/errors]
- [ ] Invariant 2: [e.g. Existing unit tests must 100% pass]
- [ ] Invariant 3: [e.g. Zero new external dependencies]

---

## 4. Evaluation Rubric
### Target Dimensions (To Improve)
| Dimension | Metric / Evaluation Method | Baseline | Target Bar |
| :--- | :--- | :--- | :--- |
| Latency | Execution time in milliseconds | 25ms | <15ms |
| Complexity | Cyclomatic complexity / line count | 450 lines | <300 lines |

### Protected Dimensions (Must NOT Regress)
| Dimension | Required Guarantee |
| :--- | :--- |
| Correctness | Zero regression on edge cases A, B, C |
| Security | Zero memory leaks / memory safety violations |

---

## 5. Campaign Resource Budget
- **Max Rounds:** 3
- **Candidate Fan-out per Round:** 2
- **Token Ceiling:** Medium / High
