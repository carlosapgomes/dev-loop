# OpenSpec Compatibility

DevLoop treats OpenSpec as an upstream protocol/framework, not as internal implementation code.

## Supported OpenSpec Version

Baseline supported CLI: `@fission-ai/openspec` **1.2.x**.

Current local audit version: `openspec --version` -> `1.2.0`.

Projects may use newer OpenSpec versions only after running the upgrade process below.

## DevLoop Extensions

DevLoop adds workflow artifacts around OpenSpec changes:

- `design.md#contract-freeze`
- slice handoffs
- implementation reports
- planner/reviewer reviews
- repository laws in `openspec/project.md`
- evidence and archive gates

These extensions must preserve OpenSpec's base lifecycle and directory intent.

## Compatibility Boundaries

DevLoop may rely on stable filesystem-level OpenSpec concepts:

```text
openspec/project.md
openspec/specs/
openspec/changes/active/
openspec/changes/archive/
```

DevLoop must not rely on:

- undocumented OpenSpec internals
- private command implementation details
- generated file formatting that OpenSpec does not guarantee
- monkey-patching OpenSpec commands
- redefining OpenSpec semantics directly

If OpenSpec changes its canonical layout, DevLoop adapts through compatibility docs/templates rather than forking behavior silently.

## Upstream Sync Strategy

- Track OpenSpec as upstream.
- Keep DevLoop extensions additive and file-based.
- Prefer templates and review gates over command overrides.
- Record any compatibility change in this document.
- Keep deprecated paths documented in `docs/deprecated-paths.md`.

## Upgrade Process

Before adopting a newer OpenSpec version:

1. Record current and target versions.
2. Run `openspec init` in a temporary repo.
3. Compare generated structure with DevLoop expectations.
4. Verify `openspec/specs`, `openspec/changes/active`, and `openspec/changes/archive` behavior.
5. Run DevLoop smoke tests.
6. Update this document if compatibility assumptions change.
7. Only then update install instructions or supported version.

Minimum validation:

```bash
openspec --version
./scripts/smoke-skills.sh --quick
```

## Rule

Do not fork OpenSpec aggressively. Extend it with DevLoop governance artifacts while preserving upstream compatibility.
