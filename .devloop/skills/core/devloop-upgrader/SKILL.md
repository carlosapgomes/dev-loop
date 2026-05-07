---
name: devloop-upgrader
description: Conservatively upgrades existing projects from older DevLoop structures to DevLoop v2 by checking, planning, and applying only safe additive changes.
---

# Skill: DevLoop Upgrader

Upgrade assistant for projects already using an older DevLoop setup.

## Use Cases

- Existing project started with old DevLoop
- Brownfield project with partial DevLoop artifacts
- Need a safe migration plan before adopting DevLoop v2

## Documentation

Full operational guide: `docs/upgrading-existing-projects.md`.

## Commands

```bash
# inspect only
python3 upgrade_devloop.py --project-root /path/to/project --check

# generate markdown plan
python3 upgrade_devloop.py --project-root /path/to/project --plan --output devloop-upgrade-plan.md

# apply only safe additive changes
python3 upgrade_devloop.py --project-root /path/to/project --apply-safe
```

## Safety Rules

- Does not rewrite active changes.
- Does not rewrite `AGENTS.md` or `PROJECT_CONTEXT.md`.
- Does not move ambiguous OpenSpec changes unless a future explicit move mode is added.
- Backs up existing markdown automation scripts before replacing them.
- Reports risky/manual actions instead of applying them silently.
