#!/usr/bin/env python3
"""Conservative DevLoop v2 upgrade assistant."""

from __future__ import annotations

import argparse
import json
import shutil
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence


@dataclass
class Action:
    id: str
    level: str
    path: str
    status: str
    message: str
    safe: bool


ESSENTIAL_DIRS = [
    "openspec/specs",
    "openspec/changes/active",
    "openspec/changes/archive",
    "docs/foundations",
    "templates/openspec",
    "templates/slices",
    "templates/reports",
    "templates/prompts",
    "templates/markdown-automation",
]

ESSENTIAL_FILES: Dict[str, str] = {
    "openspec/project.md": """# Project Laws\n\nPermanent engineering constraints for low-drift agent work.\n\nCanonical principle interpretation: `docs/foundations/llm-engineering-principles.md`.\n\n## Authority\n\n1. `openspec/project.md` — repository laws\n2. Active `design.md#contract-freeze` — frozen change contracts\n3. Active `tasks.md` and slice handoff — execution scope\n4. `AGENTS.md` — local commands and agent rules\n\n## Documentation Quality\n\n- Every created or edited Markdown file must pass `markdownlint-cli2` before delivery or commit.\n\n## Engineering Principles\n\nUse `docs/foundations/llm-engineering-principles.md` as canonical interpretation.\n""",
    "docs/foundations/llm-engineering-principles.md": """# LLM Engineering Principles\n\nCanonical principle interpretation for low-drift agent work.\n\n- Clean Code: semantic predictability.\n- DRY: avoid semantic divergence.\n- SOLID: explicit boundaries.\n- YAGNI: context control.\n- TDD: constrain behavioral search.\n- KISS: minimize coordination cost.\n""",
    "docs/openspec-compatibility.md": """# OpenSpec Compatibility\n\nDevLoop treats OpenSpec as upstream protocol/framework, not internal implementation.\n\nSupported baseline: `@fission-ai/openspec` 1.2.x.\n\nDevLoop extensions are additive governance artifacts: Contract Freeze, slice handoffs, implementation reports, planner reviews, and repository laws.\n""",
    "docs/deprecated-paths.md": """# Deprecated Paths\n\nCanonical OpenSpec paths:\n\n```text\nopenspec/changes/active/\nopenspec/changes/archive/\n```\n\nDeprecated skills paths: `.pi/skills`, `.codex/skills`, `~/.pi/skills`.\n""",
}

MARKDOWN_FORMAT = """#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

if ! command -v npx >/dev/null 2>&1; then
  echo "Erro: npx nao encontrado. Instale Node.js/npm para formatar markdown." >&2
  exit 1
fi

mapfile -d '' files < <(find . -type f -name '*.md' \
  -not -path './node_modules/*' \
  -not -path './.pi/*' \
  -not -path './.codex/*' \
  -not -path './.git/*' \
  -print0)

if [ ${#files[@]} -eq 0 ]; then
  echo "Nenhum arquivo .md encontrado."
  exit 0
fi

npx --yes prettier --write "${files[@]}"
npx --yes markdownlint-cli2 --fix "${files[@]}"
npx --yes markdownlint-cli2 "${files[@]}"
"""

MARKDOWN_LINT = """#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

if ! command -v npx >/dev/null 2>&1; then
  echo "Erro: npx nao encontrado. Instale Node.js/npm para validar markdown." >&2
  exit 1
fi

mapfile -d '' files < <(find . -type f -name '*.md' \
  -not -path './node_modules/*' \
  -not -path './.pi/*' \
  -not -path './.codex/*' \
  -not -path './.git/*' \
  -print0)

if [ ${#files[@]} -eq 0 ]; then
  echo "Nenhum arquivo .md encontrado."
  exit 0
fi

npx --yes markdownlint-cli2 "${files[@]}"
"""

PRE_COMMIT = """#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

if ! command -v npx >/dev/null 2>&1; then
  echo "Erro: npx nao encontrado. Instale Node.js/npm para rodar markdown lint no pre-commit." >&2
  exit 1
fi

mapfile -t staged_md < <(
  git diff --cached --name-only --diff-filter=ACMR \
    | grep -E '\\.md$' \
    | grep -vE '^(\\.pi/|\\.codex/)' \
    || true
)

if [ ${#staged_md[@]} -eq 0 ]; then
  exit 0
fi

npx --yes prettier --write "${staged_md[@]}"
npx --yes markdownlint-cli2 --fix "${staged_md[@]}"
npx --yes markdownlint-cli2 "${staged_md[@]}"
git add "${staged_md[@]}"
"""

MARKDOWN_AUTOMATION = {
    "scripts/markdown-format.sh": MARKDOWN_FORMAT,
    "scripts/markdown-lint.sh": MARKDOWN_LINT,
    ".githooks/pre-commit": PRE_COMMIT,
    ".markdownlintignore": ".pi/**\n.codex/**\nnode_modules/**\n.git/**\n",
}


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def devloop_root() -> Optional[Path]:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "templates").is_dir() and (parent / ".devloop" / "skills").is_dir():
            return parent
    return None


def add_action(actions: List[Action], id_: str, level: str, path: str, status: str, message: str, safe: bool) -> None:
    actions.append(Action(id=id_, level=level, path=path, status=status, message=message, safe=safe))


def analyze(root: Path) -> List[Action]:
    actions: List[Action] = []

    for rel in ESSENTIAL_DIRS:
        path = root / rel
        if path.exists():
            add_action(actions, "dir", "info", rel, "exists", "canonical directory present", True)
        else:
            add_action(actions, "dir", "warning", rel, "missing", "create directory", True)

    for rel in ESSENTIAL_FILES:
        path = root / rel
        if path.exists():
            add_action(actions, "file", "info", rel, "exists", "canonical file present", True)
        else:
            add_action(actions, "file", "warning", rel, "missing", "create canonical file", True)

    for rel, desired in MARKDOWN_AUTOMATION.items():
        path = root / rel
        txt = read_text(path)
        if not path.exists():
            add_action(actions, "markdown_automation", "warning", rel, "missing", "create markdown automation file", True)
        elif rel.endswith(".sh") or rel.endswith("pre-commit"):
            if "markdownlint-cli2" in txt:
                add_action(actions, "markdown_automation", "info", rel, "ok", "uses markdownlint-cli2", True)
            else:
                add_action(actions, "markdown_automation", "warning", rel, "outdated", "replace with markdownlint-cli2 version, with backup", True)

    gitignore = read_text(root / ".gitignore")
    for line in [".pi/", ".codex/"]:
        if line not in gitignore.splitlines():
            add_action(actions, "gitignore", "warning", ".gitignore", "missing_rule", f"append {line}", True)
    if "openspec/changes/*/" in gitignore:
        add_action(actions, "gitignore", "error", ".gitignore", "unsafe_rule", "manual removal recommended: do not hide active OpenSpec changes", False)

    # Risky/manual existing structures.
    changes = root / "openspec" / "changes"
    if changes.exists():
        for child in sorted(changes.iterdir()):
            if child.is_dir() and child.name not in {"active", "archive"}:
                add_action(actions, "manual", "warning", str(child.relative_to(root)), "ambiguous_change_path", "manual review before moving into active/archive", False)

    for rel in ["AGENTS.md", "PROJECT_CONTEXT.md"]:
        if (root / rel).exists():
            add_action(actions, "manual", "info", rel, "exists", "do not rewrite; review suggested references manually", False)
        else:
            add_action(actions, "manual", "warning", rel, "missing", "generate manually or with project-specific context", False)

    active = root / "openspec" / "changes" / "active"
    if active.exists():
        for design in sorted(active.glob("*/design.md")):
            if "## Contract Freeze" not in read_text(design):
                add_action(actions, "manual", "warning", str(design.relative_to(root)), "missing_contract_freeze", "add Contract Freeze manually; do not auto-approve", False)

    return actions


def backup_path(root: Path, backup_dir: Optional[Path], rel: str) -> Path:
    base = backup_dir or (root / ".devloop-upgrade-backup" / datetime.now().strftime("%Y%m%d-%H%M%S"))
    return base / rel


def write_file(root: Path, rel: str, content: str, backup_dir: Optional[Path], actions: List[Action]) -> None:
    path = root / rel
    if path.exists():
        old = read_text(path)
        if old == content:
            return
        bpath = backup_path(root, backup_dir, rel)
        bpath.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, bpath)
        add_action(actions, "backup", "info", str(bpath.relative_to(root)), "created", f"backup for {rel}", True)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    if rel.endswith(".sh") or rel.endswith("pre-commit"):
        path.chmod(path.stat().st_mode | 0o111)


def copy_templates(root: Path, actions: List[Action]) -> None:
    source_root = devloop_root()
    if not source_root:
        return
    source = source_root / "templates"
    if not source.exists():
        return
    for src in sorted(source.rglob("*")):
        if not src.is_file():
            continue
        rel = src.relative_to(source_root).as_posix()
        dst = root / rel
        if dst.exists():
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        add_action(actions, "template", "info", rel, "created", "copied DevLoop template", True)


def apply_safe(root: Path, backup_dir: Optional[Path]) -> List[Action]:
    actions: List[Action] = []

    for rel in ESSENTIAL_DIRS:
        path = root / rel
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            add_action(actions, "dir", "info", rel, "created", "created canonical directory", True)

    for rel, content in ESSENTIAL_FILES.items():
        path = root / rel
        if not path.exists():
            write_file(root, rel, content, backup_dir, actions)
            add_action(actions, "file", "info", rel, "created", "created canonical file", True)

    copy_templates(root, actions)

    for rel, content in MARKDOWN_AUTOMATION.items():
        path = root / rel
        if (not path.exists()) or (path.is_file() and "markdownlint-cli2" not in read_text(path) and rel != ".markdownlintignore"):
            write_file(root, rel, content, backup_dir, actions)
            add_action(actions, "markdown_automation", "info", rel, "updated", "installed markdownlint-cli2 automation", True)

    gi = root / ".gitignore"
    current = read_text(gi).splitlines()
    missing = [line for line in [".pi/", ".codex/"] if line not in current]
    if missing:
        prefix = "\n" if gi.exists() and read_text(gi) and not read_text(gi).endswith("\n") else ""
        with gi.open("a", encoding="utf-8") as f:
            f.write(prefix + "\n# DevLoop local/runtime paths\n" + "\n".join(missing) + "\n")
        add_action(actions, "gitignore", "info", ".gitignore", "updated", "appended safe runtime path ignores", True)

    return actions


def render_markdown(actions: Sequence[Action], title: str) -> str:
    lines = [f"# {title}", ""]
    for action in actions:
        marker = "SAFE" if action.safe else "MANUAL"
        lines.append(f"- **{action.level.upper()}** `{action.path}` — {action.status} ({marker}): {action.message}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Conservative DevLoop v2 upgrade assistant")
    parser.add_argument("--project-root", default=".", help="Target project root")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Inspect and return policy status")
    mode.add_argument("--plan", action="store_true", help="Render upgrade plan")
    mode.add_argument("--apply-safe", action="store_true", help="Apply safe additive changes only")
    parser.add_argument("--output", help="Write markdown output to file")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--backup-dir", help="Backup directory for replaced files")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    backup_dir = Path(args.backup_dir).resolve() if args.backup_dir else None

    if args.apply_safe:
        applied = apply_safe(root, backup_dir)
        actions = applied + analyze(root)
        title = "DevLoop Upgrade Apply-Safe Report"
    else:
        actions = analyze(root)
        title = "DevLoop Upgrade Check" if args.check else "DevLoop Upgrade Plan"

    if args.format == "json":
        payload = {"actions": [asdict(a) for a in actions]}
        out = json.dumps(payload, indent=2, ensure_ascii=False)
    else:
        out = render_markdown(actions, title)

    if args.output:
        Path(args.output).write_text(out, encoding="utf-8")
    else:
        print(out, end="")

    has_error = any(a.level == "error" for a in actions)
    has_warning = any(a.level == "warning" for a in actions)
    if args.check and (has_error or has_warning):
        return 2
    return 0 if not has_error else 2


if __name__ == "__main__":
    raise SystemExit(main())
