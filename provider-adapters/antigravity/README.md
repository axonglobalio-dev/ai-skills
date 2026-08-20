# Antigravity Provider Adapter — AI OS Skill Mirror

This directory contains provider-level adapter tooling for **Google Antigravity IDE**.

## Background & Rationale

- **Canonical Skill Authority:** `~/.ai-skills/<skill>`
- **The Sandbox Boundary Problem:** Antigravity discovers skill names across directory symlinks, but its runtime file reader (`view_file`) resolves symlinks to their `realpath`. When symlinks point outside permitted runtime roots (`~/.gemini/config` and the active workspace), runtime reads fail with security sandbox errors (`Permission denied for read_file(...)`).
- **Solution:** A generated, hash-verified, physical mirror at `~/.gemini/config/skills/<skill>` that reproduces canonical files without altering canonical contracts or versions.

## Architecture

- **Canonical Authority:** `~/.ai-skills/` (FROZEN V1)
- **Target Mirror:** `~/.gemini/config/skills/<skill>/` (Generated Physical Directory)
- **Manifest:** `.ai-os-mirror-manifest.json` (SHA-256 integrity ledger + canonical git commit provenance)

## Usage

```bash
# Check drift without mutation
python3 sync_skill.py gauntlet-loop --check

# Synchronize physical mirror from canonical source
python3 sync_skill.py gauntlet-loop

# Emit machine-readable JSON
python3 sync_skill.py gauntlet-loop --json
```

## Governance Rule

**DO NOT EDIT GENERATED ANTIGRAVITY MIRRORS DIRECTLY.**
All canonical modifications belong in `~/.ai-skills/<skill>/`. After editing canonical skills, re-run `sync_skill.py` to regenerate the physical mirror.
