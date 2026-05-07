# Phase 1 Continuation Report — Skills Canonicalization

## Summary

Implemented skills canonicalization for DevLoop v2 structural stabilization.

Canonical skills source is now:

```text
.devloop/skills/
```

Compatibility adapter preserved:

```text
skills -> .devloop/skills
```

This keeps existing `skills/...` commands working while making `.devloop/skills/` the single source of authority.

---

## Changes Made

### 1. Canonical source moved to `.devloop/skills/`

Moved the existing skills bundle from:

```text
skills/
```

to:

```text
.devloop/skills/
```

The internal skill layout was not redesigned:

```text
.devloop/skills/core/
.devloop/skills/playbooks/
.devloop/skills/domain/
.devloop/skills/legacy/
.devloop/skills/install_all_skills.sh
```

### 2. Compatibility adapter preserved

Created a symlink adapter:

```text
skills -> .devloop/skills
```

This preserves current users and scripts that still call paths such as:

```text
skills/install_all_skills.sh
skills/core/setup-solopreneur-project/setup_project.py
```

### 3. Installer/script references updated

Updated smoke validation to use the canonical source directly:

```text
.devloop/skills/
```

Affected file:

- `scripts/smoke-skills.sh`

The installer itself remains unchanged internally and continues to install from its own directory, so it works from both:

```text
.devloop/skills/install_all_skills.sh
skills/install_all_skills.sh
```

### 4. Documentation updated

Updated documentation to identify `.devloop/skills/` as the canonical source and `skills/` as compatibility only.

Affected docs:

- `README.md`
- `docs/README.md`
- `docs/getting-started.md`
- `docs/inventory-skills.md`
- `docs/migration-map.md`
- `docs/script-backlog.md`
- `docs/cli-conventions.md`
- `.devloop/skills/README.md`
- `docs/deprecated-paths.md`

### 5. Deprecated paths marked clearly

Updated `docs/deprecated-paths.md`.

Canonical paths:

```text
.devloop/skills/        # source bundle in this repository
~/.pi/agent/skills/     # Pi runtime install target
```

Compatibility adapter:

```text
skills -> .devloop/skills
```

Deprecated paths:

```text
.pi/skills
.codex/skills
~/.pi/skills
```

### 6. Legacy install snippets updated incrementally

Updated direct legacy/playbook examples that still pointed to `~/.pi/skills` so they now point to:

```text
~/.pi/agent/skills
```

No skill internals were redesigned.

---

## Backward Compatibility

Preserved:

- `skills/...` path usage via symlink adapter
- installer behavior
- legacy skill group installation via `--include-legacy`
- current runtime target `~/.pi/agent/skills`

Deprecated but documented:

- `.pi/skills`
- `.codex/skills`
- `~/.pi/skills`

---

## Validation

Commands run successfully:

```bash
python3 .devloop/skills/core/setup-solopreneur-project/tests/test_setup_project.py
python3 .devloop/skills/core/artifacts-consistency-checker/tests/test_check_consistency.py
python3 .devloop/skills/playbooks/suggest-adr/tests/test_suggest_adr.py
./scripts/smoke-skills.sh --quick
```

Compatibility adapter validation also passed:

```bash
test -L skills
bash skills/install_all_skills.sh "$(mktemp -d)"
python3 skills/core/setup-solopreneur-project/tests/test_setup_project.py
```

---

## Success Criteria Status

- One canonical source: done (`.devloop/skills/`)
- No contradictory active instructions: done in updated docs/scripts
- Updated documentation: done
- Tests still pass: done
- Current users not broken: preserved through `skills -> .devloop/skills`

---

## Notes / Deferred

Intentionally not done in this phase:

- no skill internals redesigned
- no lifecycle/workflow redesign
- no Contract Freeze implementation
- no full rewrite of legacy skill docs
- no removal of compatibility adapter
