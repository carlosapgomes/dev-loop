---
name: setup-solopreneur-project
description: Configura um novo projeto seguindo o SOP do DevLoop. Cria estrutura de diretórios, templates de AGENTS.md, PROJECT_CONTEXT.md e documentação inicial.
---

# Skill: Setup Solopreneur Project

Este skill ajuda a configurar um novo projeto (ou adaptar um existente) para seguir o SOP do DevLoop, com foco em rastreabilidade, retomada rápida e baixo atrito operacional.

## Quando usar

- Iniciando um novo projeto Python/Django/JavaScript com workflow estruturado
- Adaptando um projeto existente para maior rastreabilidade
- Preparando um repositório para ser forkável por outros departamentos
- Estabelecendo padrões de documentação para trabalho solo com LLMs

## 🐍 Método Recomendado: Script Python

Este skill inclui `setup_project.py` para bootstrap determinístico da estrutura do SOP.

```bash
# bootstrap padrão
python3 setup_project.py --project-root .

# incluir estrutura openspec mínima
python3 setup_project.py --project-root . --include-openspec

# validar se projeto já está conforme (exit 0=ok, 2=faltando itens)
python3 setup_project.py --project-root . --check --format json

# simular sem escrever nada
python3 setup_project.py --project-root . --dry-run --format json
```

## Estrutura de diretórios recomendada

O SOP do DevLoop recomenda a seguinte estrutura:

```
projeto/
├── AGENTS.md                      # [OBRIGATÓRIO] Contrato com IA
├── PROJECT_CONTEXT.md             # [RECOMENDADO] Resumo executivo
├── README.md                      # Documentação principal
├── openspec/                      # OpenSpec (gerado via `openspec init`)
│   ├── config.yaml
│   ├── specs/
│   ├── changes/
│   └── archive/
├── docs/                          # Documentação estruturada
│   ├── adr/                       # Architecture Decision Records
│   ├── releases/                  # Release Evidence Packs
│   ├── setup.md
│   ├── architecture.md
│   └── api/                       (opcional)
├── prompts/                       # Handoffs detalhados
│   └── handoff.md                 (.gitignore se sensível)
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── scripts/                       # Automações do projeto
│   ├── markdown-format.sh
│   └── markdown-lint.sh
├── .githooks/
│   └── pre-commit
├── .markdownlintignore
└── .codex/
    └── skills/                    # Skills do OpenSpec
```

## Passo a passo de configuração

### 1. Inicialização OpenSpec (opcional mas recomendado)

```bash
# Instalar OpenSpec globalmente
npm install -g @fission-ai/openspec@latest

# Na raiz do projeto
cd seu-projeto
openspec init
```

### 2. Criar diretórios base

```bash
# Criar estrutura de documentação
mkdir -p docs/adr docs/releases
mkdir -p tests/unit tests/integration tests/e2e
mkdir -p scripts
mkdir -p prompts
```

### 3. Criar AGENTS.md (template básico)

Crie `AGENTS.md` na raiz com este conteúdo mínimo:

```markdown
# AGENTS.md

## 1. Stack e Versoes
- Python: 3.12.x
- Django: 5.x
- Banco: PostgreSQL 15
- Frontend: JavaScript (ES2022), HTMX, Bootstrap 5

## 2. Comandos de Validacao (Quality Gate)
- Markdown (autofix): `./scripts/markdown-format.sh`
- Markdown (lint): `./scripts/markdown-lint.sh`
- Testes: `python3 -m pytest -q`
- Lint: `ruff check .`
- Type check: `mypy .` (se aplicavel)
- Build/Check: `python3 manage.py check`
- Migracoes (check): `python3 manage.py makemigrations --check --dry-run`

## 3. Comandos Essenciais (Operacao Local)
### Setup
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install -r requirements/dev.txt`

### Rodar local
- `python3 manage.py runserver`

### Testes rapidos
- `python3 -m pytest -q tests/unit`

### Migracoes
- `python3 manage.py migrate --plan`

### Hooks
- `git config core.hooksPath .githooks`

## 4. Arquitetura e Constraints
- Direcao: templates -> views -> services -> models
- Nao colocar logica de negocio em views
- Usar services para operacoes complexas
- Models focados em dados e invariantes

## 5. Politica de Testes
- TDD obrigatorio para novas funcionalidades
- 70% unit, 25% integration, 5% E2E
- Cobrir edge cases conhecidos

## 6. Stop Rule (CRUCIAL)
- Implementar UMA task slice por vez
- Exigir `design.md` para o change, exceto QUICK de bugfix simples
- Rodar validacoes da secao 2
- Atualizar `tasks.md` com [x]
- Fazer commit e push do slice concluido
- **PARAR e pedir confirmacao para proxima task**

## 7. Definition of Done (DoD)
- [ ] Build sem erro
- [ ] Testes passam (nova cobertura quando aplicavel)
- [ ] Markdown lint sem erros (`./scripts/markdown-lint.sh`)
- [ ] Lint/type check OK
- [ ] Tasks e specs atualizadas
- [ ] Commit feito com mensagem clara
- [ ] Push realizado

## 8. Anti-patterns Proibidos
- Nao criar God classes/services
- Nao acoplar template/UI com logica complexa
- Nao ignorar logs/telemetria em operacoes criticas

## 9. Prompt de Reentrada
- Read AGENTS.md and PROJECT_CONTEXT.md first.
- Implement ONLY the next incomplete slice from tasks/spec.
- If the active change is not a simple QUICK bugfix, require design.md before implementation.
- Run section 2 validation commands and update artifacts for the completed slice.
- Commit and push the current branch.
- STOP and ask for explicit confirmation before starting the next slice.
```

### 4. Criar PROJECT_CONTEXT.md (template)

```markdown
# PROJECT_CONTEXT.md

## Propósito
Resumo executivo para retomar trabalho após pausas longas.

## Fontes Autoritativas
- Handoff completo: `prompts/handoff.md`
- Specs: `openspec/specs/`
- Em conflito: seguir handoff

## Objetivo do Sistema
[1-2 parágrafos: o que faz, para quem, valor principal]

## Arquitetura de Alto Nível
[Diagrama mental: containers, componentes, fluxo principal]

## Regras Não Negociáveis
- [Regras de negócio imutáveis]
- [Contratos externos obrigatórios]
- [Constraints de compliance]

## Quality Bar
- Testes rodam em < 2 minutos
- Cobertura mínima: 80%
- Zero warnings no lint
```

### 5. Configurar .gitignore (recomendações)

Adicione ao `.gitignore`:

```gitignore
# Dados sensíveis/contexto
prompts/
.env
*.secret

# OpenSpec (dados temporários)
openspec/changes/*/  # mantém apenas archive/
```

### 6. Automatizar lint/fix de Markdown

```bash
mkdir -p .githooks scripts

# se o setup script ja foi rodado, os arquivos abaixo ja existem
chmod +x scripts/markdown-format.sh scripts/markdown-lint.sh .githooks/pre-commit

# ativar hook do repositorio
git config core.hooksPath .githooks

# validar
./scripts/markdown-format.sh
```

### 7. Primeiro change teste

Execute para validar o setup:

```bash
# Criar change simples de validação
/opsx:propose setup-quality-gates

# Modo ESSENCIAL (apenas proposal + tasks)
# Implementar
/opsx:apply

# Verificar e arquivar
/opsx:verify
/opsx:archive
```

## Templates adicionais

### README.md inicial

```markdown
# Nome do Projeto

Breve descrição do projeto.

## Stack Tecnológica
- Backend: Python 3.12 + Django 5.0
- Banco: PostgreSQL 15
- Frontend: JavaScript, HTMX, Bootstrap 5
- Ferramentas: OpenSpec para workflow de desenvolvimento

## Workflow de Desenvolvimento

Este projeto segue o SOP do DevLoop para desenvolvimento assistido por IA com rastreabilidade completa.

### Artefatos Principais
- `AGENTS.md`: Contrato de execução com IAs
- `PROJECT_CONTEXT.md`: Resumo executivo do sistema
- `openspec/`: Especificações e changes
- `docs/adr/`: Registros de decisão arquitetural
- `docs/releases/`: Evidências de release

### Como Contribuir
1. Leia AGENTS.md antes de qualquer implementação
2. Use OpenSpec para criar changes (`/opsx:propose`)
3. Siga TDD e Stop Rule (uma slice por vez)
4. Crie ADRs para decisões arquiteturais

## Licença
[Informações de licença]
```

### docs/adr/README.md (índice)

```markdown
# Architecture Decision Records

Registros de decisões arquiteturais importantes.

## ADRs Ativas
- [ADR-0001: Escolha de Stack Tecnológica](ADR-0001-stack-choice.md)

## Template
Ver [template.md](template.md) para criar novas ADRs.
```

### docs/adr/template.md

```markdown
# ADR-XXXX: <Título>

## Status
[Proposed | Accepted | Deprecated | Superseded]

## Contexto
[Situação que motivou a decisão]

## Decisão
[O que foi decidido, com detalhes suficientes]

## Alternativas Consideradas
1. [Alternativa 1]: [por que não escolhida]
2. [Alternativa 2]: [por que não escolhida]

## Consequências
**Positivas:**
- [Benefício 1]
- [Benefício 2]

**Negativas/Trade-offs:**
- [Custo 1]
- [Custo 2]
```

## Checklist de validação

Após configurar, verifique:

- [ ] `AGENTS.md` criado e ajustado para stack real
- [ ] `PROJECT_CONTEXT.md` com informações básicas
- [ ] `docs/adr/` e `docs/releases/` criados
- [ ] `openspec init` executado (se usando OpenSpec)
- [ ] `.gitignore` atualizado para prompts/ se necessário
- [ ] `scripts/markdown-format.sh` e `scripts/markdown-lint.sh` presentes
- [ ] `.githooks/pre-commit` ativo (`git config core.hooksPath .githooks`)
- [ ] README.md com informações do workflow
- [ ] Primeiro change teste executado com sucesso

## Dicas para projetos do setor público

1. **Rastreabilidade completa**: Mantenha todos os artefatos no Git
2. **Documentação fork-friendly**: Explique "porquês" além de "comos"
3. **Release Evidence Packs**: Crie em `docs/releases/` para cada entrega
4. **ADRs justificadas**: Documente alternativas consideradas e trade-offs

## Próximos passos

1. Familiarize-se com os comandos OpenSpec (`/opsx:propose`, `/opsx:apply`, etc.)
2. Estabeleça rotinas de higiene de contexto (encerrar sessões após changes)
3. Configure CI/CD para rodar comandos de validação automaticamente (ex: `templates/ci/github-actions-markdown.yml`)
4. Revise AGENTS.md periodicamente conforme a stack evolui
