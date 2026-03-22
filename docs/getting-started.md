# Getting Started do DevLoop

Guia prático para responder: **o que rodar e em qual momento**.

## Pré-requisitos

- Git
- Python 3.11+
- Repositório `dev-loop` clonado localmente

Defina um atalho para facilitar os comandos:

```bash
export DEVLOOP_HOME="/caminho/para/dev-loop"
```

---

## Fluxo A — Projeto novo

### 1) Criar repositório/projeto

```bash
mkdir meu-projeto && cd meu-projeto
git init
```

### 2) Bootstrap do SOP

```bash
python3 "$DEVLOOP_HOME/skills/core/setup-solopreneur-project/setup_project.py" \
  --project-root . \
  --include-openspec
```

Isso cria estrutura base (`AGENTS.md`, `PROJECT_CONTEXT.md`, `docs/`, `scripts/markdown-*.sh`, `.githooks/pre-commit`, etc.).

### 3) Instalar skills no projeto

```bash
bash "$DEVLOOP_HOME/skills/install_all_skills.sh" .pi/skills
```

Opcional (compatibilidade com nomes antigos):

```bash
bash "$DEVLOOP_HOME/skills/install_all_skills.sh" .pi/skills --include-legacy
```

### 4) Ativar hook e validar setup

```bash
git config core.hooksPath .githooks
./scripts/markdown-format.sh
./scripts/markdown-lint.sh
python3 "$DEVLOOP_HOME/skills/core/setup-solopreneur-project/setup_project.py" \
  --project-root . \
  --check --format text
```

### 5) Rodar primeiro change piloto

1. Classificar risco do change.
2. Criar artefatos OpenSpec conforme risco.
   QUICK sem `design.md` so para bugfix simples; nos demais casos, incluir `design.md`.
3. Implementar 1 slice vertical por vez (end-to-end, sem slicing horizontal por camada).
4. Ao fechar cada slice: validar, atualizar artefatos, commitar e dar push.
5. Parar e so continuar com confirmacao explicita.

---

## Fluxo B — Projeto existente (adoção gradual)

### 1) Diagnóstico sem alterar nada

```bash
python3 "$DEVLOOP_HOME/skills/core/setup-solopreneur-project/setup_project.py" \
  --project-root . \
  --check --format json
```

Se faltar estrutura, simule antes:

```bash
python3 "$DEVLOOP_HOME/skills/core/setup-solopreneur-project/setup_project.py" \
  --project-root . \
  --dry-run --include-openspec --format text
```

### 2) Aplicar bootstrap incremental

```bash
python3 "$DEVLOOP_HOME/skills/core/setup-solopreneur-project/setup_project.py" \
  --project-root . \
  --include-openspec
```

### 3) Ajustar AGENTS.md para a stack real

Revise principalmente:

- comandos de teste/lint/type-check/build
- DoD
- anti-patterns específicos do projeto

### 4) Instalar skills e ativar hook

```bash
bash "$DEVLOOP_HOME/skills/install_all_skills.sh" .pi/skills
git config core.hooksPath .githooks
```

### 5) Pilotar em 1 change real pequeno

Adote o DevLoop em um change de baixo risco primeiro. Depois expanda para todo o time/projeto.

---

## O que rodar em cada momento

| Momento | Comando sugerido | Objetivo |
|---|---|---|
| Antes de abrir change | `python3 .pi/skills/classify-change-risk/classify_risk.py "<descrição>" --format markdown` | Definir risco e nível de rigor |
| Antes de implementar | validar artefatos do change (`proposal.md`, `tasks.md`, `design.md` quando aplicável) | Evitar cair em QUICK indevido |
| Ao preparar change FEATURE/HIGH | `python3 .pi/skills/suggest-adr/suggest_adr.py --project-root . --fail-on recommendation` | Sinalizar necessidade de ADR |
| Durante cada slice | comandos de teste/lint do `AGENTS.md` em um fluxo vertical | Garantir qualidade incremental com entrega end-to-end |
| Antes de commit | `python3 .pi/skills/validate-agents/validate_agents.py --project-root . --staged --fail-on medium` | Evitar anti-patterns críticos |
| Fechamento de slice | `git commit -m "<tipo>: <slice>"` + `git push origin <branch>` | Registrar evidencia remota e forcar pausa consciente |
| Antes de archivar change | `python3 .pi/skills/changelog-updater/update_changelog.py --project-root . --dry-run --fail-on empty` | Verificar evidência de mudança |
| Pré-release | `python3 .pi/skills/release-evidence-pack-generator/generate_release_pack.py --project-root . --version vX.Y.Z --dry-run --fail-on missing-any` | Garantir pacote mínimo de evidências |
| Rotina periódica (mensal) | `python3 .pi/skills/refactor-sprint-suggester/suggest_refactor_sprint.py --project-root . --fail-on high` | Mapear dívida técnica prioritária |

> Convenção de exit code dos scripts: `0=ok`, `1=erro de execução`, `2=policy/gate violado`.

---

## Atalhos úteis

- Convenções de CLI: `docs/cli-conventions.md`
- Fluxo macro do processo: `SOP.md`
- Catálogo de skills: `skills/README.md`
- Smoke test do kit (para mantenedores): `./scripts/smoke-skills.sh`
