# AI OS Gauntlet Loop — Provider Integration & Independence Matrix

## Subagent Independence Hierarchy

| Level | Name | Description | Host Applicability |
| :--- | :--- | :--- | :--- |
| **L0** | Same-Context Review | Model reviews its own previous turn in the same thread. Lowest adversarial rigor. | Basic CLI / fallback |
| **L1** | Role-Separated Session | Sequential prompting with distinct system roles in the same conversation. | Single-session LLMs |
| **L2** | Fresh-Context Worker | Separate subagent or API call with clean context for each worker. | Claude Code (`Task`), Antigravity (`browser_subagent`) |
| **L3** | Isolated Candidate Worker | Subagent workers receive only the spec without author or peer information. | Multi-agent platforms |
| **L4** | Blind Evaluator with Sealed Rubric | Critic receives only anonymized candidate outputs and frozen rubric. | Fully orchestrated AI OS |

---

## Host Integration Matrix

### 1. Codex (App / CLI / IDE)
- **Discovery Location:** `/Users/jrcalaca/.agents/skills/gauntlet-loop`
- **Execution:** Runs natively via standard subagent dispatch or role-separated turns.
- **Independence Level:** L2 / L3.

### 2. Claude Code (CLI)
- **Discovery Location:** `/Users/jrcalaca/.claude/skills/gauntlet-loop`
- **Execution:** Dispatched via native `Task` tool for parallel builders and critics.
- **Independence Level:** L3 / L4.

### 3. Claude App / Cowork
- **Distribution:** Packaged as `/Users/jrcalaca/.ai-skills/dist/gauntlet-loop.zip`.
- **Execution:** Uploaded as a Custom Agent Skill in the Claude UI.
- **Independence Level:** L1 / L2.

### 4. Google Antigravity IDE (Gemini)
- **Global Discovery Location:** `/Users/jrcalaca/.gemini/config/skills/gauntlet-loop`
- **Workspace Discovery Location:** `<workspace>/.agents/skills/gauntlet-loop`
- **Execution:** Orchestrates native tasks and tool invocations.
- **Independence Level:** L2 / L3.
