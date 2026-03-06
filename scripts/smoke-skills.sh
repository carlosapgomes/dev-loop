#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

RUN_TESTS=true
INCLUDE_LEGACY=false

for arg in "$@"; do
  case "$arg" in
    --quick|--no-tests)
      RUN_TESTS=false
      ;;
    --include-legacy)
      INCLUDE_LEGACY=true
      ;;
    *)
      echo "Uso: scripts/smoke-skills.sh [--quick|--no-tests] [--include-legacy]" >&2
      exit 1
      ;;
  esac
done

log() {
  echo "[smoke] $*"
}

assert_exit_code() {
  local expected="$1"
  shift
  local out_file err_file
  out_file="$(mktemp)"
  err_file="$(mktemp)"

  set +e
  "$@" >"$out_file" 2>"$err_file"
  local code=$?
  set -e

  if [[ "$code" -ne "$expected" ]]; then
    echo "[smoke] ERRO: comando retornou $code, esperado $expected" >&2
    echo "[smoke] Comando: $*" >&2
    echo "[smoke] --- stdout ---" >&2
    cat "$out_file" >&2 || true
    echo "[smoke] --- stderr ---" >&2
    cat "$err_file" >&2 || true
    rm -f "$out_file" "$err_file"
    exit 1
  fi

  rm -f "$out_file" "$err_file"
}

log "1) Validando frontmatter dos SKILL.md"
python3 - <<'PY'
from pathlib import Path
import re

root = Path("skills")
issues = []
for skill_md in sorted(root.rglob("SKILL.md")):
    txt = skill_md.read_text(encoding="utf-8", errors="ignore")
    stripped = txt.lstrip()
    if not stripped.startswith("---"):
        issues.append(f"{skill_md}: frontmatter ausente")
        continue
    name = re.search(r"^name:\s*(.+)$", txt, re.M)
    desc = re.search(r"^description:\s*(.+)$", txt, re.M)
    if not name:
        issues.append(f"{skill_md}: campo name ausente")
    if not desc:
        issues.append(f"{skill_md}: campo description ausente")
if issues:
    print("\n".join(issues))
    raise SystemExit(1)
print("frontmatter ok")
PY

log "2) Compilando scripts Python"
python3 - <<'PY'
from pathlib import Path
import py_compile

for p in sorted(Path("skills").rglob("*.py")):
    py_compile.compile(str(p), doraise=True)
print("py_compile ok")
PY

log "3) Smoke de CLI (--help)"
mapfile -t cli_scripts < <(find skills -type f -name '*.py' -not -path '*/tests/*' | sort)
for script in "${cli_scripts[@]}"; do
  python3 "$script" --help >/dev/null
  echo "  - ok: $script"
done

if [[ "$RUN_TESTS" == "true" ]]; then
  log "4) Executando testes"
  mapfile -t test_scripts < <(find skills -type f -path '*/tests/test_*.py' | sort)
  for t in "${test_scripts[@]}"; do
    python3 "$t"
  done
else
  log "4) Testes pulados (--quick)"
fi

log "5) Testando instalador de skills"
TMP_INSTALL="$(mktemp -d)"
trap 'rm -rf "$TMP_INSTALL"' EXIT

bash skills/install_all_skills.sh "$TMP_INSTALL" >/dev/null

for required in \
  adr-generator \
  agents-md-generator \
  artifacts-consistency-checker \
  classify-change-risk \
  project-context-maintainer \
  quality-gate-executor \
  setup-solopreneur-project \
  changelog-updater \
  release-evidence-pack-generator \
  refactor-sprint-suggester \
  suggest-adr \
  validate-agents \
  project-resurrection \
  django-insights
  do
  [[ -d "$TMP_INSTALL/$required" ]] || { echo "[smoke] skill faltando: $required" >&2; exit 1; }
done

if [[ "$INCLUDE_LEGACY" == "true" ]]; then
  bash skills/install_all_skills.sh "$TMP_INSTALL" --include-legacy >/dev/null
  for legacy in esaa-classify-risk esaa-generate-agents esaa-generate-context esaa-django-insights esaa-project-resurrection esaa-suggest-adr esaa-validate-agents; do
    [[ -d "$TMP_INSTALL/$legacy" ]] || { echo "[smoke] legacy faltando: $legacy" >&2; exit 1; }
  done
fi

log "6) Smoke de policy exit codes (esperado: 2)"

TMP_POL="$(mktemp -d)"
trap 'rm -rf "$TMP_INSTALL" "$TMP_POL"' EXIT

# validate-agents policy fail
cat > "$TMP_POL/AGENTS.md" <<'EOF'
# AGENTS.md

## 8. Anti-patterns Proibidos
- sem segredo hardcoded
EOF
cat > "$TMP_POL/app.py" <<'EOF'
API_KEY = "abc12345"
EOF
assert_exit_code 2 python3 skills/playbooks/validate-agents/validate_agents.py --project-root "$TMP_POL" "$TMP_POL/app.py"

# changelog empty policy fail
mkdir -p "$TMP_POL/repo"
git -C "$TMP_POL/repo" init -q
assert_exit_code 2 python3 skills/playbooks/changelog-updater/update_changelog.py --project-root "$TMP_POL/repo" --dry-run --fail-on empty

# release pack missing-any policy fail
assert_exit_code 2 python3 skills/playbooks/release-evidence-pack-generator/generate_release_pack.py --project-root "$TMP_POL/repo" --version v0.0.1 --dry-run --fail-on missing-any

# suggest-adr recommendation policy fail
mkdir -p "$TMP_POL/repo/openspec/changes/active/risky"
cat > "$TMP_POL/repo/openspec/changes/active/risky/proposal.md" <<'EOF'
# Risco alto
Mudança de arquitetura com migration database e auth HIGH/ARCH.
EOF
assert_exit_code 2 python3 skills/playbooks/suggest-adr/suggest_adr.py --project-root "$TMP_POL/repo" risky --fail-on recommendation

log "✅ Smoke tests concluídos com sucesso"
