# SOP

Este é o procedimento operacional padrão (SOP) do **DevLoop** (`dev-loop`).

## Princípios

1. IA executa; artefatos em disco preservam contexto.
2. Evidência no Git > intenção no chat.
3. Um change por vez, dividido em slices pequenos e verticais.
4. Um slice vertical = um commit + push.
5. Retomada deve ser possível com baixo tempo de aquecimento.
6. Leis permanentes do repositório vivem em `openspec/project.md`.
7. Interpretação de princípios vive em `docs/foundations/llm-engineering-principles.md`.
8. Compatibilidade OpenSpec vive em `docs/openspec-compatibility.md`.

## Fluxo padrão por change

Lifecycle canônico DevLoop/OpenSpec:

```text
Proposal
→ Design
→ Contract Freeze
→ Task Planning
→ Slice Execution
→ Evidence Report
→ Reviewer Gate
→ Archive
```

1. Classificar risco do change (`QUICK`, `FEATURE`, `HIGH/ARCH`).
2. Criar `proposal.md` no OpenSpec.
3. Criar `design.md` quando aplicável; FEATURE/HIGH exigem Design.
4. Formalizar **Contract Freeze** dentro do `design.md` antes de planejar tasks.
5. Planejar `tasks.md` em slices verticais que herdam o Contract Freeze.
6. Executar cada slice com handoff de contexto zero.
7. Implementador gera implementation report com evidências diff-oriented.
8. Reviewer/planner distinto avalia o report e registra aprovação/rejeição.
9. Arquivar change após aprovação.
10. Se necessário, gerar evidence pack de release.

## Risco e artefatos

### QUICK (0-1)

- `proposal.md`
- `tasks.md`
- permitido somente para bugfix simples, localizado e reversivel
- sem alteracao estrutural, sem novo contrato externo e sem migracao de dados

### FEATURE (2-3)

- `proposal.md`
- delta specs
- `design.md` com seção Contract Freeze
- `tasks.md`
- default para mudancas que nao sejam bugfix simples

### HIGH/ARCH (4+)

- tudo de FEATURE
- ADR
- plano de rollback
- reviewer/planner gate explícito antes de archive

Regra de decisao: em caso de duvida entre QUICK e FEATURE, use FEATURE com `design.md`.

## Stop Rule

Após cada slice:

1. confirmar que o slice e vertical (fluxo end-to-end com valor entregue)
2. validar comandos de qualidade
3. atualizar tasks/artefatos
4. commitar com mensagem rastreavel
5. dar push da branch
6. parar e decidir conscientemente o próximo slice
7. nao continuar sem confirmacao explicita

Regra anti-pattern: nao fazer slice horizontal por camada (ex.: "so backend", "so frontend", "so banco") sem entregar fluxo vertical completo.

## Contrato de planejamento de slice (obrigatorio)

Todo slice deve ser planejado para execucao por **LLM com contexto zero** e deve herdar o Contract Freeze do `design.md`.

Checklist obrigatorio do slice:

1. objetivo vertical claro (valor end-to-end)
2. escopo enxuto: tocar poucos arquivos, apenas o necessario (se ampliar escopo, justificar)
3. Contract Freeze herdado (`design.md#contract-freeze`)
4. handoff funcional e de negocio no proprio arquivo do slice
5. prompt pronto para implementacao (copiar/colar)
6. criterios de sucesso objetivos
7. gates de autoavaliacao (teste/lint/type-check/consistencia de artefatos)
8. aderencia às leis do repositório em `openspec/project.md` durante o REFACTOR
9. relatorio de implementacao conciso e diff-oriented
10. salvar o relatorio em markdown temporario e informar o caminho para avaliacao do planner

Formato de saida obrigatorio ao concluir slice:
- Implementador: `REPORT_PATH=<caminho-do-arquivo-temporario.md>`
- Reviewer/planner: usar `templates/reports/planner-review.md` e decidir aprovado/rejeitado.

Regra: o agente implementador nao aprova o proprio trabalho; avaliação e implementação são responsabilidades separadas.

## TDD Red/Green/Refactor

Para cada slice vertical:

1. RED: escrever teste que falha e representa comportamento esperado/bug.
2. GREEN: implementar o minimo para passar o teste.
3. REFACTOR: limpar codigo mantendo toda suite verde.
4. repetir o ciclo no proximo slice (sem pular direto para implementacao).

## Templates canônicos

- `templates/openspec/proposal.md`
- `templates/openspec/design.md`
- `templates/openspec/tasks.md`
- `templates/slices/slice-handoff.md`
- `templates/reports/implementation-report.md` — evidência concisa do implementador
- `templates/reports/planner-review.md` — aprovação/rejeição por reviewer distinto

## Quality baseline

- testes do escopo alterado
- lint e type-check do escopo
- markdown lint quando houver alteração em `.md`

## Setup mínimo de repositório

- `AGENTS.md`
- `PROJECT_CONTEXT.md`
- `openspec/project.md`
- `openspec/` com `changes/active/` e `changes/archive/`
- `docs/adr/`
- `docs/releases/`
- scripts de automação de markdown (`scripts/markdown-*.sh`, `.githooks/pre-commit`)

## Retomada rápida

1. ler `openspec/project.md`, `AGENTS.md` e `PROJECT_CONTEXT.md`
2. verificar change ativo e próximo slice
3. rodar validação rápida
4. executar apenas o próximo slice

## Quando aumentar rigor

Não usamos perfil fixo (ex: público/saas) no núcleo do SOP.

Use o apêndice para calibrar rigor por contexto:

- [`docs/appendices/rigor-by-complexity.md`](docs/appendices/rigor-by-complexity.md)
