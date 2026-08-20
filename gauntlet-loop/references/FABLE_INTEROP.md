# AI OS Gauntlet Loop — Fable Interoperability & Anti-Recursion Governance

## Methodological Boundaries

The AI OS provides distinct, complementary protocols for different operational scopes:

```
+-------------------------------------------------------------------------------+
|                                 AI OS METHODS                                 |
+-------------------------------------------------------------------------------+
| 1. fable-method:  Behavioral discipline & rules of engagement (WHAT to do)    |
| 2. fable-loop:    Linear multi-step orchestration (WHO does standard tasks)   |
| 3. fable-judge:   Post-execution claims verification & fraud detection        |
| 4. gauntlet-loop: Adversarial multi-candidate tournament & quality boundary   |
+-------------------------------------------------------------------------------+
```

---

## Cross-Nesting Invariants (MANDATORY)

To prevent infinite recursion, harness deadlock, and token exhaustion, the following rules are non-negotiable:

1. **Root Ownership Only:** Only the root orchestrator may own a loop.
2. **Gauntlet Child Invariant:** A child builder, critic, or evaluator spawned by `gauntlet-loop` MUST NOT invoke `gauntlet-loop`, `fable-loop`, or spawn child orchestration trees.
3. **Fable Child Invariant:** A child subagent spawned by `fable-loop` MUST NOT invoke `gauntlet-loop`.
4. **Fable Judge Interoperability:** `fable-judge` MAY be invoked by the root orchestrator as a post-mortem audit AFTER a `gauntlet-loop` terminates, but NEVER inside an active candidate round.

### Violation State:
If a child attempts to instantiate a recursive loop:
```
GAUNTLET_CHILD_LOOP_VIOLATION
```
The orchestrator terminates the offending child immediately without attempting recursive recovery.
