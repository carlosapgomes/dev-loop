# Upgrading Existing DevLoop Projects

Use this guide to migrate projects that already use an older or partial DevLoop setup.

The upgrade strategy is conservative: detect much, apply little, and never rewrite active planning artifacts silently.

## When to Use

Use this process for:

- projects started with an older DevLoop structure
- brownfield projects where DevLoop was introduced later
- projects with `.pi/skills`, `.codex/skills`, old OpenSpec paths, or older Markdown automation

Do not use it as a replacement for human review of active changes.

## Safety Rules

- Create a branch before upgrading.
- Run `--check` and `--plan` before `--apply-safe`.
- Do not run the upgrader directly on a dirty working tree.
- Review the diff before committing.
- Do not let the upgrader rewrite `AGENTS.md`, `PROJECT_CONTEXT.md`, active `design.md`, or active `tasks.md`.
- Treat active changes as manual review areas.

## Recommended Flow

From the target project:

```bash
git status --short
git checkout -b chore/upgrade-devloop-v2
```

Set DevLoop source path:

```bash
export DEVLOOP_HOME="/path/to/dev-loop"
```

### 1. Check current state

```bash
python3 "$DEVLOOP_HOME/.devloop/skills/core/devloop-upgrader/upgrade_devloop.py" \
  --project-root . \
  --check
```

Exit codes:

- `0`: no blocking problems detected
- `2`: warnings/errors require review

### 2. Generate an upgrade plan

```bash
python3 "$DEVLOOP_HOME/.devloop/skills/core/devloop-upgrader/upgrade_devloop.py" \
  --project-root . \
  --plan \
  --output devloop-upgrade-plan.md
```

Review the plan before applying anything.

### 3. Apply safe changes only

```bash
python3 "$DEVLOOP_HOME/.devloop/skills/core/devloop-upgrader/upgrade_devloop.py" \
  --project-root . \
  --apply-safe
```

Optional explicit backup directory:

```bash
python3 "$DEVLOOP_HOME/.devloop/skills/core/devloop-upgrader/upgrade_devloop.py" \
  --project-root . \
  --apply-safe \
  --backup-dir .devloop-upgrade-backup/manual-run
```

### 4. Run Markdown lint

Every Markdown file created or edited must pass `markdownlint-cli2`.

```bash
./scripts/markdown-format.sh
./scripts/markdown-lint.sh
```

### 5. Review and commit

```bash
git status --short
git diff
git add .
git commit -m "chore: upgrade DevLoop artifacts to v2"
```

## What `--apply-safe` May Do

Safe additive actions include:

- create `openspec/project.md` if missing
- create `openspec/specs/`
- create `openspec/changes/active/`
- create `openspec/changes/archive/`
- create `docs/foundations/llm-engineering-principles.md`
- create `docs/openspec-compatibility.md`
- create `docs/deprecated-paths.md`
- install missing templates
- update Markdown automation to `markdownlint-cli2`, with backup
- append safe `.gitignore` rules for `.pi/` and `.codex/`

## What It Must Not Do Automatically

The upgrader does not rewrite:

- `AGENTS.md`
- `PROJECT_CONTEXT.md`
- active `proposal.md`
- active `design.md`
- active `tasks.md`
- active slice handoffs

The upgrader does not automatically move ambiguous OpenSpec changes from:

```text
openspec/changes/<change-id>/
```

to:

```text
openspec/changes/active/<change-id>/
```

Those moves require human review.

## Handling Active Changes

If a project has active changes, upgrade infrastructure first and leave active planning artifacts untouched.

After safe upgrade, review each active change manually:

- Does `design.md` exist for FEATURE/HIGH work?
- Does `design.md` contain `## Contract Freeze`?
- Do slices inherit `design.md#contract-freeze`?
- Do slices define allowed/forbidden files?
- Do implementation reports and planner reviews exist for completed slices?

If Contract Freeze is missing, add it manually as draft and get planner approval before continuing execution.

## Rollback

If the upgrade introduced unwanted changes:

```bash
git restore .
```

If files were replaced by `--apply-safe`, inspect backups under:

```text
.devloop-upgrade-backup/
```

or the directory passed via `--backup-dir`.

## Checklist Before Merge

- [ ] Upgrade plan reviewed
- [ ] No active change was rewritten silently
- [ ] `AGENTS.md` custom commands preserved
- [ ] `PROJECT_CONTEXT.md` project-specific context preserved
- [ ] Markdown automation uses `markdownlint-cli2`
- [ ] Markdown lint passes
- [ ] Diff reviewed manually
- [ ] Follow-up manual migrations recorded
