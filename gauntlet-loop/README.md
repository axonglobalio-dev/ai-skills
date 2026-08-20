# AI OS Gauntlet Loop (v1)

A bounded, adversarial, evidence-driven multi-candidate improvement protocol for AI OS agents.

## Overview

The **Gauntlet Loop** provides a rigorous, tournament-style improvement workflow for high-stakes software engineering, architecture, UX/UI, and research tasks. It forces candidates to compete against explicit reference bars and independent harsh critics before any work is promoted.

### Key Tenets
1. **Define the Bar First:** No generation begins until hard invariants, target dimensions, protected dimensions, and stop rules are frozen.
2. **Independent Adversarial Evaluation:** Builders never grade their own work. Critics search for counterexamples and refutations.
3. **Blind Comparison:** Candidates are evaluated without author bias against a sealed rubric.
4. **Non-Regression by Construction:** Gains in one dimension cannot silently regress correctness, security, or baseline invariants.
5. **Strict Non-Nesting Invariant:** Only the root orchestrator owns iteration. Children are leaf workers (`NESTED_ORCHESTRATION = PROHIBITED`).
6. **Provider Portability:** Operates seamlessly across Codex, Claude Code, Claude App/Cowork, and Google Antigravity without vendor lock-in.

---

## Directory Structure

```
gauntlet-loop/
├── SKILL.md                  # Compact router and operational protocol
├── README.md                 # Project documentation and architectural overview
├── references/
│   ├── METHOD.md             # In-depth operational methodology (Stages 0–9)
│   ├── ROUTING.md            # Routing decision trees and trigger conditions
│   ├── EVALUATION.md         # Blind comparison, scoring matrices, and counterexample selection
│   ├── PROVIDERS.md          # Provider mapping and independence levels (L0–L4)
│   ├── FABLE_INTEROP.md      # Demarcation and composition rules with Fable skills
│   └── PROVENANCE.md         # Architectural provenance and external design reconciliation
├── templates/
│   ├── GAUNTLET_SPEC.md      # Specification template for freezing the quality bar
│   ├── BUILDER_BRIEF.md      # Isolated worker instruction template
│   ├── CRITIC_BRIEF.md       # Independent critic and counterexample search template
│   ├── EVALUATION.md         # Blind scoring sheet and comparison matrix
│   └── CHECKPOINT.md         # Minimal state schema for multi-round campaigns
└── tests/
    └── test_gauntlet_contract.py # Python contract verification suite (Cases A–H)
```

---

## Quick Start & Usage

### Triggering Gauntlet
Invoke explicitly:
- `/gauntlet-loop`
- `"Run gauntlet on [target]"`
- `"Adversarially evaluate [architecture/design/implementation]"`

### Standard Routing Doctrine
- **Mechanical tasks / bugfixes:** Direct execution (No loop).
- **Structured implementation:** `fable-method` (Single thread, intent/recall gates).
- **Bounded multi-step workflows:** `fable-loop` (Standard linear fan-out).
- **Independent post-audit:** `fable-judge` (Claims verification).
- **High-stakes / Multi-candidate quality boundaries:** `gauntlet-loop` (Adversarial tournament).
