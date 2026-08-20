# AI OS Gauntlet Loop — Routing Doctrine & Decision Tree

## Decision Tree

```
                       [ Incoming Task ]
                               |
            Is it a mechanical edit / simple fix?
             /                                          YES                                NO
           /                                      [ Fast Direct Edit ]               Are there multiple plausible approaches,
                                    a difficult quality bar, or high non-regression risk?
                                     /                                                                     NO                                   YES
                                   /                                                              [ Fable Method / Loop ]             Is a defensible Reference Bar
                                                            and Evaluation Rubric definable?
                                                             /                                                                                      NO                            YES
                                                           /                                                                         [ STOP: BLOCKED_BAR_UNDEFINED ]         [ GAUNTLET LOOP ]
```

---

## Positive Routing Triggers
1. **Architectural Trade-Offs:** Choosing between competing patterns (e.g. Actor model vs CSP, SQL schema topologies, distributed state synchronizers).
2. **Visual & UI Refinement:** Aligning layout, typography, motion causality, and micro-interactions against a high-fidelity reference design.
3. **High-Stakes Non-Regression:** Performance optimizations where correctness, concurrency safety, or security invariants must remain absolute.
4. **Plateau Recovery:** A task that has failed 2+ iterations under single-threaded refinement (`fable-loop`).
5. **Explicit Owner Mandate:** The user explicitly requests `/gauntlet-loop` or an adversarial tournament.

---

## Negative Routing Triggers (Reject Gauntlet)
1. **Mechanical Refactoring:** Renaming variables, updating imports, formatting styles.
2. **Deterministic Bugfixes:** Fixing an issue with an existing failing unit test that has an unambiguous fix.
3. **Simple Inquiries:** Answering factual questions or reading documentation.
4. **Unspecified Open-Ended Brainstorming:** Tasks lacking a clear quality bar or evaluation criteria.
