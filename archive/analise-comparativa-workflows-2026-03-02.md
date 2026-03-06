# Análise Comparativa dos 3 Workflows (LLM1 vs LLM2 vs LLM3)

Data: 2026-03-02
Contexto considerado: dev independente, trabalhos ocasionais para setor público, tentativa de SaaS, foco em durabilidade, retomada após meses e redução de drift/débito.

## Método de avaliação

Critérios usados (com peso para seu cenário):

1. Retomada e memória de longo prazo (30%)
2. Simplicidade de adoção diária para solo dev (30%)
3. Fit para SaaS (20%)
4. Compliance/rastreabilidade para setor público (10%)
5. Automação pronta para uso (10%)

## Resultado rápido

- LLM1 (base teórica OpenSpec): **6.5/10**
- LLM2 (v4.1 otimizado): **8.3/10**
- LLM3 (v4.2 DeepSeek): **8.0/10**

## Diagnóstico por versão

## LLM1 (`esaa/`)

Pontos fortes:

- Base conceitual sólida e completa.
- Bootstrap brownfield/greenfield muito bem estruturado.
- Boa cobertura de OpenSpec, ADR, release e reentrada.

Limitações:

- Parte crítica de classificação de risco é "opcional", o que reduz disciplina prática.
- Menos automação operacional pronta.
- Mais "manual", menos orientado para rotina rápida.

Veredito:

- Excelente referência-mãe, mas não é a melhor versão para começar no dia a dia.

## LLM2 (`esaa-k2.5/`)

Pontos fortes:

- Melhor equilíbrio entre rigor e velocidade para solo dev.
- Três modos (QUICK/FEATURE/HIGH), Stop Rule, Context Hygiene e Resurrection muito claros.
- Traz seção explícita para diferenciar **cliente público vs SaaS próprio**, alinhada ao seu cenário.
- Tutorial brownfield é pragmático e incremental.

Limitações:

- As skills do diretório estão em `SKILL.md` (sem scripts `.py` prontos no repositório).
- Há inconsistência interna: README diz skills "implementadas", mas índice marca partes como pendentes.

Veredito:

- **Melhor base de processo para você começar já**, com baixa fricção.

## LLM3 (`esaa-deepseek/`)

Pontos fortes:

- Forte para contexto público: compliance, evidências de release e forkabilidade.
- Maior maturidade de automação: várias skills com scripts Python + testes.
- Testes locais das skills passaram (7 suítes executadas com sucesso).

Limitações:

- Mais pesado para rotina SaaS inicial (pode virar overhead se aplicar tudo sempre).
- Linguagem e fluxo mais centrados em setor público/Pi.dev.

Veredito:

- Excelente para contratos públicos e rastreabilidade forte; potencialmente excessivo para fases de MVP SaaS.

## Recomendação final

Recomendo começar pelo **LLM2** como workflow principal.

Motivo:

- É o melhor compromisso entre disciplina (durabilidade/retomada) e velocidade (SaaS).
- Já traz explicitamente a adaptação entre projetos de cliente público e produto próprio.
- Você reduz risco de abandonar o processo por excesso de burocracia.

## Como usar na prática (sem reinventar)

1. Adote o SOP do LLM2 como padrão base.
2. Puxe do LLM3 apenas o que agrega alto valor imediato:

- `classify-change-risk`
- `quality-gate-executor`
- `agents-md-generator` / `project-context-maintainer`

1. Use o LLM1 como referência para prompts de bootstrap quando iniciar projeto novo ou organizar brownfield.

## Observações de evidência

- LLM2: `skills/` contém apenas `SKILL.md` (sem scripts executáveis no repositório).
- LLM3: há scripts Python e testes para várias skills; testes executados localmente passaram.
