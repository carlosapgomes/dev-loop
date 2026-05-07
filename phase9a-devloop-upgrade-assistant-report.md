# Phase 9A Implementation Report — DevLoop Upgrade Assistant

## Summary

Implemented a conservative DevLoop v2 upgrade assistant for projects already using older DevLoop structures.

New skill:

```text
.devloop/skills/core/devloop-upgrader/
```

## What Was Added

- `SKILL.md`
- `upgrade_devloop.py`
- unit tests in `tests/test_upgrade_devloop.py`

## Supported Modes

```bash
python3 .devloop/skills/core/devloop-upgrader/upgrade_devloop.py --project-root <project> --check
python3 .devloop/skills/core/devloop-upgrader/upgrade_devloop.py --project-root <project> --plan
python3 .devloop/skills/core/devloop-upgrader/upgrade_devloop.py --project-root <project> --apply-safe
```

## Safety Model

The upgrader follows the agreed strategy:

- Detect much.
- Apply little.
- Never rewrite active planning artifacts silently.
- Never rewrite `AGENTS.md` or `PROJECT_CONTEXT.md`.
- Back up existing markdown automation scripts before replacing them.
- Report risky/manual actions instead of applying them silently.

## Safe Changes Applied by `--apply-safe`

- creates canonical OpenSpec directories
- creates missing repository law/foundation/compatibility docs
- installs missing templates when running from the DevLoop source repo
- updates markdown automation to `markdownlint-cli2`
- appends safe `.gitignore` rules for `.pi/` and `.codex/`

## Manual / Risky Items Reported

- unsafe `.gitignore` rules hiding `openspec/changes/*/`
- ambiguous `openspec/changes/<change-id>/` directories
- active `design.md` missing Contract Freeze
- missing or existing `AGENTS.md` / `PROJECT_CONTEXT.md` requiring human review

## Files Changed

- `.devloop/skills/core/devloop-upgrader/SKILL.md`
- `.devloop/skills/core/devloop-upgrader/upgrade_devloop.py`
- `.devloop/skills/core/devloop-upgrader/tests/test_upgrade_devloop.py`
- `.devloop/skills/README.md`
- `docs/using-devloop.md`
- `refactoring-roadmap.md`
- `scripts/smoke-skills.sh`

## Validation

Commands run successfully:

```bash
python3 .devloop/skills/core/devloop-upgrader/tests/test_upgrade_devloop.py
python3 .devloop/skills/core/devloop-upgrader/upgrade_devloop.py --help
./scripts/smoke-skills.sh --quick
npx --yes markdownlint-cli2 .devloop/skills/core/devloop-upgrader/SKILL.md docs/using-devloop.md refactoring-roadmap.md .devloop/skills/README.md
```

## Status

Phase 9A is implemented.

Phase 9B lifecycle validators are not implemented yet; they should be a separate slice.

## Required Chat Output

```text
REPORT_PATH=phase9a-devloop-upgrade-assistant-report.md
```
