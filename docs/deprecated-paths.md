# Deprecated Paths

This document records structural paths that remain recognizable for compatibility but are not canonical in DevLoop v2.

## OpenSpec

Canonical OpenSpec change layout:

```text
openspec/changes/active/   # changes in progress
openspec/changes/archive/  # completed/archived changes
```

Deprecated/invalid patterns:

```text
openspec/changes/<change-id>/        # ambiguous: missing active/archive phase
.gitignore rule: openspec/changes/*/ # hides active change context
```

Rule: active OpenSpec changes are versioned context. Do not hide `openspec/changes/active/` with gitignore rules.

## Skills

Canonical paths:

```text
.devloop/skills/        # source bundle in this repository
~/.pi/agent/skills/     # Pi runtime install target
```

Compatibility adapter:

```text
skills -> .devloop/skills
```

Deprecated compatibility paths:

```text
.pi/skills
.codex/skills
~/.pi/skills
```

These paths may appear in old projects or legacy documentation, but they must not define lifecycle policy or architectural authority.
