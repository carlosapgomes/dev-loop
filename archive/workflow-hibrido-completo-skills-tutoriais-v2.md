# Workflow Hibrido Completo v2 (Base Original + Skills + Tutoriais)

Data: 2026-03-02  
Objetivo: consolidar um workflow unico, pratico e duravel, melhor que as versoes isoladas, mantendo a base teorica do original e incorporando skills e tutoriais completos.

> **Status:** documento histórico. Para uso atual, adotar `SOP.md`.

---

## 1) Fundacao teorica (base original, mantida)

Principios obrigatorios:

1. LLM executa, arquivos em disco guardam memoria de longo prazo.
2. Evidencia no Git > intencao no chat.
3. Rigor proporcional ao risco.
4. Um change por vez, dividido em slices pequenos.
5. Um slice = um commit.
6. Retomada apos semanas/meses deve ser rapida e previsivel.

OpenSpec continua como espinha dorsal:

- `openspec/specs/` para comportamento canonico.
- `openspec/changes/active/` para trabalho em andamento.
- `openspec/changes/archive/` para historico.

---

## 2) Modo de uso por perfil (PUBLIC vs SAAS)

Defina no topo de `AGENTS.md`:

- `PROFILE_PUBLIC`
- `PROFILE_SAAS`

Regra:

- Mesmo processo base, muda apenas nivel de evidencia e formalidade.

### 2.1 PROFILE_PUBLIC (setor publico/cliente)

- Default de trabalho: `FEATURE`.
- `Release Evidence Pack` quase sempre obrigatorio.
- ADR mais frequente.
- Rastreabilidade e auditabilidade acima de velocidade.

### 2.2 PROFILE_SAAS (produto proprio)

- Default de trabalho: `QUICK` para experimento.
- Promote para `FEATURE` quando entrar no core do produto.
- ADR apenas para decisoes de fundacao (auth, billing, tenancy, dados).
- Velocidade com guardrails.

---

## 3) Classificacao de risco e artefatos

Pontue 1 por criterio:

- auth/autorizacao
- dados persistidos/migracao
- API/contrato externo
- seguranca
- performance critica
- refatoracao ampla (>5 arquivos)
- rollback caro
- impacto regulatorio/documental

Resultado:

- `0-1` = `QUICK`
- `2-3` = `FEATURE`
- `4+` = `HIGH/ARCH`

Artefatos por nivel:

### QUICK

- `proposal.md` curto
- `tasks.md` curto

### FEATURE

- `proposal.md`
- delta specs
- `design.md`
- `tasks.md`

### HIGH/ARCH

- tudo de FEATURE
- ADR obrigatoria
- plano de rollback

Release Evidence Pack obrigatorio quando:

- perfil PUBLIC, ou
- risco HIGH/ARCH, ou
- mudou contrato externo/dados sensiveis.

---

## 4) Estrutura minima recomendada

```text
projeto/
├── AGENTS.md
├── PROJECT_CONTEXT.md
├── README.md
├── prompts/
│   └── handoff.md
├── docs/
│   ├── adr/
│   └── releases/
├── openspec/
│   ├── config.yaml
│   ├── specs/
│   └── changes/
│       ├── active/
│       └── archive/
├── scripts/
├── .githooks/
│   └── pre-commit
├── .markdownlintignore
└── tests/
```

`PROJECT_CONTEXT.md` passa a ser obrigatorio neste hibrido para facilitar retomada.

Padrao recomendado para documentacao:

- `scripts/markdown-format.sh` (autofix)
- `scripts/markdown-lint.sh` (validacao)
- `.githooks/pre-commit` para formatar/lintar `.md` staged automaticamente
- Templates prontos em `templates/markdown-automation/` (`install.sh` para setup rapido)
- Template de CI em `templates/ci/github-actions-markdown.yml`

---

## 5) Catalogo completo de skills (com status)

## 5.1 Skills executaveis agora (base DeepSeek, com scripts Python)

1. `setup-solopreneur-project`

- Script: `setup_project.py`
- Inclui bootstrap de lint/fix Markdown (`scripts/markdown-*.sh` + pre-commit hook)
- Uso:

```bash
python3 setup_project.py --project-root . --include-openspec
python3 setup_project.py --project-root . --check --format json
```

1. `agents-md-generator`

- Script: `generate_agents_md.py`
- Uso:

```bash
python3 generate_agents_md.py --project-root .
python3 generate_agents_md.py --project-root . --check
```

1. `project-context-maintainer`

- Script: `maintain_project_context.py`
- Uso:

```bash
python3 maintain_project_context.py --project-root .
python3 maintain_project_context.py --project-root . --check
```

1. `classify-change-risk`

- Script: `classify_risk.py`
- Uso:

```bash
python3 classify_risk.py "Implementar integracao com API externa" --format json
```

1. `quality-gate-executor`

- Script: `quality_gate.py`
- Uso:

```bash
python3 quality_gate.py --list
python3 quality_gate.py --format markdown
```

1. `adr-generator`

- Script: `adr_generator.py`
- Uso:

```bash
python3 adr_generator.py --project-root . --title "Escolha de estrategia de autenticacao"
python3 adr_generator.py --project-root . --list-next --format json
```

1. `artifacts-consistency-checker`

- Script: `check_consistency.py`
- Uso:

```bash
python3 check_consistency.py --root . --format markdown
```

1. `release-evidence-pack-generator`

- Skill de processo/template (sem script principal unico no pacote atual)
- Uso: seguir template de `docs/releases/YYYY-MM-DD_vX.Y.Z.md`.

1. `changelog-updater`

- Skill de processo/template (scripts utilitarios descritos em SKILL.md).

1. `refactor-sprint-suggester`

- Skill de processo/template para diagnostico e plano de refactor.

## 5.2 Skills de alto valor conceitual (base K2.5, majoritariamente em SKILL.md)

Use como protocolo manual agora, ou implemente scripts depois:

1. `esaa-project-resurrection`

```bash
/esaa-project-resurrection [--warmup]
```

1. `esaa-validate-agents`

```bash
/esaa-validate-agents [arquivos...] [--fix]
```

1. `esaa-django-insights`

```bash
/esaa-django-insights [--app=nome] [--focus=performance,security,architecture]
```

1. `esaa-suggest-adr`

```bash
/esaa-suggest-adr [change-id] [--auto-create]
```

1. `esaa-generate-agents`, `esaa-generate-context`, `esaa-classify-risk`

- podem ser mantidos como referencia de prompts/templates.

## 5.3 Ordem recomendada de adocao de skills

Fase 1 (imediata):

1. `setup-solopreneur-project`
2. `agents-md-generator`
3. `project-context-maintainer`
4. `classify-change-risk`
5. `quality-gate-executor`

Fase 2 (consolidacao):

1. `adr-generator`
2. `artifacts-consistency-checker`
3. protocolo `esaa-project-resurrection`

Fase 3 (maturidade):

1. `release-evidence-pack-generator`
2. `changelog-updater`
3. `refactor-sprint-suggester`
4. `esaa-django-insights`

---

## 6) Tutorial completo Greenfield (passo a passo)

Meta: sair de zero para primeiro change com qualidade em 1 dia.

## Fase G1 - Descoberta (30-60 min)

- Definir problema, usuarios, stack, constraints, riscos.
- Registrar em `prompts/handoff.md`.

Checklist:

- [ ] objetivo de negocio claro
- [ ] escopo de MVP claro
- [ ] restricoes nao-negociaveis claras

## Fase G2 - Setup estrutural (30-45 min)

```bash
npm install -g @fission-ai/openspec@latest
openspec init
mkdir -p docs/adr docs/releases prompts scripts tests/unit tests/integration .githooks
```

Executar skills:

```bash
python3 esaa-deepseek/skills/setup-solopreneur-project/setup_project.py --project-root . --include-openspec
python3 esaa-deepseek/skills/agents-md-generator/generate_agents_md.py --project-root .
python3 esaa-deepseek/skills/project-context-maintainer/maintain_project_context.py --project-root .

# garantir hook ativo
git config core.hooksPath .githooks

# validar markdown do repositorio
./scripts/markdown-format.sh
```

Checklist:

- [ ] `AGENTS.md` valido
- [ ] `PROJECT_CONTEXT.md` criado
- [ ] estrutura `openspec/` pronta
- [ ] hook `.githooks/pre-commit` ativo (`git config core.hooksPath .githooks`)
- [ ] `./scripts/markdown-lint.sh` passando

## Fase G3 - Primeiro change (60-120 min)

1. Classificar risco da feature inicial:

```bash
python3 esaa-deepseek/skills/classify-change-risk/classify_risk.py "Primeiro endpoint funcional" --format markdown
```

1. Criar change (`/opsx:propose` ou manual).
2. Produzir artefatos conforme risco.
3. Implementar 1-2 slices no maximo.
4. Rodar gate:

```bash
python3 esaa-deepseek/skills/quality-gate-executor/quality_gate.py --format markdown
```

## Fase G4 - Fechamento do dia (15 min)

- [ ] tasks atualizadas
- [ ] commits atomicos feitos
- [ ] contexto atualizado (2-5 linhas)
- [ ] proximo slice definido para retomada

---

## 7) Tutorial completo Brownfield (passo a passo)

Meta: adotar processo sem quebrar sistema existente.

## Fase B0 - Seguranca inicial (20 min)

```bash
git checkout -b bootstrap-esaa
git status
git log --oneline -20
```

Checklist:

- [ ] branch dedicado
- [ ] estado atual registrado

## Fase B1 - Auditoria rapida do legado (60-90 min)

Mapear:

- estrutura de diretorios
- stack e versoes
- comandos reais de teste/lint/build
- contratos externos e pontos criticos
- debt evidente

Documentar sem idealizar.

## Fase B2 - Contratos base (45-60 min)

Gerar/atualizar:

```bash
python3 esaa-deepseek/skills/agents-md-generator/generate_agents_md.py --project-root .
python3 esaa-deepseek/skills/project-context-maintainer/maintain_project_context.py --project-root .
```

Checklist:

- [ ] AGENTS reflete realidade atual (nao ideal)
- [ ] PROJECT_CONTEXT reflete arquitetura atual

## Fase B3 - OpenSpec gradual (20-30 min)

```bash
openspec init
```

Decidir estrategia de specs retroativas:

- A: completas
- B: apenas futuras
- C: hibrida (recomendado)

Recomendacao padrao Brownfield: `C`.

## Fase B4 - Primeiro change seguro (90-180 min)

Escolher melhoria de baixo risco e alta visibilidade.

Exemplos:

- endpoint/status
- teste de caracterizacao para fluxo estavel
- logging observavel em ponto critico

Fluxo:

1. classificar risco
2. criar artefatos minimos
3. implementar 1 slice
4. gate de qualidade
5. commit atomico
6. stop

## Fase B5 - Consolidacao (30 dias)

Semana 1:

- Setup e primeiro change completo.

Semana 2:

- QUICK wins + testes de caracterizacao.

Semana 3:

- primeira FEATURE com specs e design.

Semana 4:

- primeira ADR + primeiro release pack (se PUBLIC).

---

## 8) Tutorial de rotina diaria (operacao continua)

Inicio de sessao (5-10 min):

1. ler `AGENTS.md` e `PROJECT_CONTEXT.md`
2. verificar `openspec/changes/active/`
3. escolher um unico slice

Execucao (30-120 min):

1. RED
2. GREEN
3. REFACTOR
4. VERIFY
5. DOCS LINT (`./scripts/markdown-format.sh`) quando houver mudanca em `.md`
6. COMMIT
7. UPDATE task
8. STOP

Fim de sessao (5 min):

- [ ] proximo slice anotado
- [ ] contexto atualizado
- [ ] sem mudancas "perdidas"

---

## 9) Tutorial de release (completo)

Quando houver release relevante:

1. validar change finalizado

```bash
python3 esaa-deepseek/skills/quality-gate-executor/quality_gate.py --format markdown
python3 esaa-deepseek/skills/artifacts-consistency-checker/check_consistency.py --root . --format markdown
```

1. gerar ADR pendente (se houver decisao estrutural)

```bash
python3 esaa-deepseek/skills/adr-generator/adr_generator.py --project-root . --title "Decisao de release X"
```

1. atualizar changelog (processo do skill)
2. gerar `docs/releases/YYYY-MM-DD_vX.Y.Z.md` (template release evidence pack)

Checklist minimo do pack:

- [ ] changes incluidos
- [ ] specs afetadas
- [ ] ADRs afetadas
- [ ] evidencias de validacao
- [ ] plano de rollout/rollback

---

## 10) Definition of Done (DoD) hibrida

Um slice so fecha quando:

- [ ] implementacao funcional
- [ ] testes/lint/type-check do escopo ok
- [ ] markdown lint ok quando `.md` foi alterado
- [ ] task marcada
- [ ] commit atomico
- [ ] stop rule respeitada

Um change so fecha quando:

- [ ] artefatos coerentes com nivel de risco
- [ ] validacao completa passou
- [ ] ADR criada quando obrigatoria
- [ ] arquivado em `openspec/changes/archive/`

Uma release so fecha quando:

- [ ] consistencia de artefatos validada
- [ ] evidence pack gerado (conforme gatilho)
- [ ] changelog atualizado

---

## 11) Regras anti-burocracia (para nao abandonar o processo)

1. Nao criar documento sem uso pratico na proxima retomada/release.
2. QUICK nao vira FEATURE por paranoia.
3. FEATURE/HIGH nao vira QUICK por pressa.
4. Se um ritual nao gerou valor em 30 dias, simplifique.
5. Processo existe para reduzir retrabalho, nao para produzir papel.

---

## 12) Plano de adocao recomendado (60 dias)

Dias 1-7:

- fundamentos + estrutura + 5 skills core.

Dias 8-30:

- operacao diaria com classificacao de risco + quality gate + stop rule.

Dias 31-60:

- consistencia de artefatos + ADR madura + release pack quando necessario.

Resultado esperado:

- retomada em <20 min
- menor drift entre codigo e intencao
- menor risco de regressao
- evidencias suficientes para setor publico sem matar velocidade de SaaS.
