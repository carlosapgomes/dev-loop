---
name: esaa-classify-risk
description: [LEGACY] Classifica risco de change. Preferir classify-change-risk.
---

# Skill: esaa-classify-risk

**Propósito:** Classificar automaticamente o risco de um change baseado no SOP ESAA Solopreneur v4.1

**Quando usar:**

- Após criar um proposal.md
- Antes de decidir quais artefatos gerar
- Quando há dúvida sobre o nível de formalidade necessário

---

## Uso

```bash
/esaa-classify-risk [change-id]
```

Se `change-id` não for fornecido, usa o change ativo mais recente.

---

## Comportamento

1. Lê o arquivo `openspec/changes/active/{change-id}/proposal.md`
2. Analisa o conteúdo em busca de palavras-chave de risco
3. Verifica a estrutura do projeto para impacto (models, APIs, auth)
4. Calcula score (0-8) baseado nos critérios do SOP ESAA
5. Classifica como QUICK, FEATURE ou HIGH/ARCH
6. Recomenda quais artefatos são necessários

---

## Critérios de Risco (SOP ESAA v4.1)

1 ponto para cada item presente:

| Critério | Keywords | Verificação Adicional |
|----------|----------|---------------------|
| Autenticação/autorização | auth, login, permission, jwt, oauth, session, token, password | Verifica se existe `auth/` ou `users/` no projeto |
| Dados persistidos/migração | migration, migrate, model, schema, database, table, column | Verifica pasta `migrations/` |
| API pública/contrato externo | api, endpoint, webhook, integration, rest, graphql, endpoint | Verifica `urls.py`, `api/`, `views.py` |
| Segurança | security, encrypt, hash, password, token, xss, csrf, ssl, https | - |
| Performance crítica | cache, optimize, slow, query, n+1, performance, bottleneck | - |
| Refatoração ampla | refactor, rewrite, restructure, cleanup, remove, delete, move | Conta arquivos mencionados (>5 = +1) |
| Rollback caro/complexo | rollback, revert, undo, migration, data-loss | Se migração de dados |
| Impacto regulatório | compliance, audit, log, gdpr, lgpd, regulation, legal | - |

---

## Classificação

| Score | Classe | Artefatos Obrigatórios |
|-------|--------|----------------------|
| 0-1 | **QUICK** | proposal.md, tasks.md |
| 2-3 | **FEATURE** | proposal.md, specs/, design.md, tasks.md |
| 4+ | **HIGH/ARCH** | proposal.md, specs/, design.md, tasks.md, **ADR** |

---

## Exemplo de Saída

```
$ /esaa-classify-risk add-user-auth

🔍 Analisando change: add-user-auth
📄 Lendo: openspec/changes/active/add-user-auth/proposal.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 CLASSIFICAÇÃO DE RISCO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Change: add-user-auth
Score: 5 pontos
Classe: 🔴 HIGH/ARCH

Critérios atendidos:
  ✓ Autenticação/autorização (auth, login, password)
  ✓ Dados persistidos (model, migration)
  ✓ API pública (endpoint)
  ✓ Segurança (security, token)
  ✓ Rollback caro (migration de dados de usuário)

Artefatos recomendados:
  ✅ proposal.md (já existe)
  ⏳ specs/ (delta specs obrigatórias)
  ⏳ design.md (obrigatório para HIGH)
  ⏳ tasks.md (obrigatório)
  ⚠️  ADR (obrigatório para HIGH/ARCH)

⚠️  ATENÇÃO: Este change afeta autenticação e dados de usuário.
   Recomendações:
   • Criar ADR em docs/adr/ADR-XXXX-auth-strategy.md
   • Plano de rollback para dados migrados
   • Testes de segurança adicionais

Próximo passo sugerido:
  /opsx:continue add-user-auth  (para gerar specs e design)
  ou
  /esaa-suggest-adr add-user-auth
```

---

## Implementação

### Dependências

- Python 3.8+
- Acesso ao filesystem do projeto
- (Opcional) GitPython para análise de impacto

### Estrutura de Arquivos

```
esaa-classify-risk/
├── SKILL.md              # Este arquivo
├── classify.py           # Script principal
├── criteria.yaml         # Definição de critérios e keywords
└── test_classify.py      # Testes
```

### Lógica Principal (classify.py)

```python
#!/usr/bin/env python3
"""
Classificador de risco para SOP ESAA Solopreneur v4.1
"""

import os
import re
import sys
from pathlib import Path
import yaml

CRITERIA = {
    "auth": {
        "keywords": ["auth", "login", "permission", "jwt", "oauth", "session", "token", "password", "user", "group"],
        "paths": ["auth", "users", "accounts", "authentication"]
    },
    "migration": {
        "keywords": ["migration", "migrate", "model", "schema", "database", "table", "column", "field"],
        "paths": ["migrations"]
    },
    "api_public": {
        "keywords": ["api", "endpoint", "webhook", "integration", "rest", "graphql", "endpoint", "url"],
        "paths": ["api", "urls.py"]
    },
    "security": {
        "keywords": ["security", "encrypt", "hash", "password", "token", "xss", "csrf", "ssl", "https", "sanitize"],
        "paths": []
    },
    "performance": {
        "keywords": ["cache", "optimize", "slow", "query", "n+1", "performance", "bottleneck", "index"],
        "paths": []
    },
    "refactor": {
        "keywords": ["refactor", "rewrite", "restructure", "cleanup", "remove", "delete", "move", "rename"],
        "paths": [],
        "file_threshold": 5  # Se menciona >5 arquivos
    },
    "rollback": {
        "keywords": ["rollback", "revert", "undo", "data-loss", "backup"],
        "paths": []
    },
    "regulatory": {
        "keywords": ["compliance", "audit", "log", "gdpr", "lgpd", "regulation", "legal", "privacy"],
        "paths": []
    }
}

def read_proposal(change_path):
    """Lê o proposal.md do change"""
    proposal_file = Path(change_path) / "proposal.md"
    if not proposal_file.exists():
        return None
    return proposal_file.read_text().lower()

def detect_project_structure(project_root):
    """Detecta estrutura relevante do projeto"""
    structure = {
        "has_auth_app": any(Path(project_root).glob("**/auth/")),
        "has_migrations": list(Path(project_root).glob("**/migrations/")),
        "has_api": any(Path(project_root).glob("**/api/")),
        "is_django": (Path(project_root) / "manage.py").exists(),
        "is_node": (Path(project_root) / "package.json").exists(),
    }
    return structure

def count_files_mentioned(text):
    """Conta arquivos mencionados no proposal"""
    # Regex para detectar padrões de arquivo
    patterns = [
        r'\b\w+\.py\b',
        r'\b\w+\.js\b',
        r'\b\w+\.ts\b',
        r'\b\w+\.html\b',
        r'`([^`]+\.(py|js|ts|html|css|json|yaml|yml))`'
    ]
    files = set()
    for pattern in patterns:
        files.update(re.findall(pattern, text))
    return len(files)

def classify_risk(change_id, project_root="."):
    """Classifica o risco de um change"""
    change_path = Path(project_root) / "openspec" / "changes" / "active" / change_id
    
    if not change_path.exists():
        print(f"❌ Change '{change_id}' não encontrado em openspec/changes/active/")
        return None
    
    proposal_content = read_proposal(change_path)
    if not proposal_content:
        print(f"❌ proposal.md não encontrado para '{change_id}'")
        return None
    
    structure = detect_project_structure(project_root)
    
    score = 0
    matched_criteria = []
    
    for criterion, config in CRITERIA.items():
        matched = False
        
        # Verifica keywords
        if any(kw in proposal_content for kw in config["keywords"]):
            matched = True
        
        # Verifica paths (se aplicável)
        for path_pattern in config.get("paths", []):
            if any(path_pattern in str(p) for p in Path(project_root).rglob("*")):
                matched = True
        
        # Verifica threshold de arquivos (para refactor)
        if "file_threshold" in config:
            file_count = count_files_mentioned(proposal_content)
            if file_count > config["file_threshold"]:
                matched = True
                matched_criteria.append(f"{criterion} ({file_count} arquivos)")
                score += 1
                continue
        
        if matched:
            matched_criteria.append(criterion)
            score += 1
    
    # Determina classe
    if score <= 1:
        level = "QUICK"
        level_emoji = "🟢"
    elif score <= 3:
        level = "FEATURE"
        level_emoji = "🟡"
    else:
        level = "HIGH/ARCH"
        level_emoji = "🔴"
    
    return {
        "change_id": change_id,
        "score": score,
        "level": level,
        "level_emoji": level_emoji,
        "criteria": matched_criteria,
        "proposal_length": len(proposal_content),
        "structure": structure
    }

def print_report(result):
    """Imprime relatório formatado"""
    if not result:
        return
    
    print(f"\n{'━'*50}")
    print("📊 CLASSIFICAÇÃO DE RISCO")
    print(f"{'━'*50}\n")
    
    print(f"Change: {result['change_id']}")
    print(f"Score: {result['score']} pontos")
    print(f"Classe: {result['level_emoji']} {result['level']}\n")
    
    print("Critérios atendidos:")
    for criterion in result['criteria']:
        print(f"  ✓ {criterion}")
    
    if result['score'] == 0:
        print("  (Nenhum critério de risco identificado)")
    
    print(f"\nArtefatos recomendados:")
    print("  ✅ proposal.md (sempre necessário)")
    
    if result['level'] in ["FEATURE", "HIGH/ARCH"]:
        print("  ⏳ specs/ (delta specs)")
        print("  ⏳ design.md (arquitetura)")
    
    print("  ⏳ tasks.md (sempre necessário)")
    
    if result['level'] == "HIGH/ARCH":
        print("  ⚠️  ADR (obrigatório para HIGH/ARCH)")
    
    # Recomendações específicas
    print(f"\n{'━'*50}")
    if result['level'] == "HIGH/ARCH":
        print("⚠️  ATENÇÃO: Change de alto risco detectado!")
        print("\nRecomendações:")
        print("  • Criar ADR em docs/adr/")
        print("  • Plano de rollback explícito")
        print("  • Testes de segurança/performance")
        print("  • Considerar revisão cruzada (/esaa-cross-review)")
    elif result['level'] == "FEATURE":
        print("💡 Dica: Modo FEATURE é o padrão profissional.")
        print("   Garanta que specs estão claras antes de implementar.")
    else:
        print("✅ Modo QUICK: Mantenha simples e rápido.")
        print("   Se começar a crescer, reclassifique com /esaa-classify-risk")
    
    print(f"{'━'*50}\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Tenta detectar change ativo mais recente
        changes_dir = Path("openspec/changes/active")
        if changes_dir.exists():
            changes = sorted(changes_dir.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)
            if changes:
                change_id = changes[0].name
                print(f"📝 Usando change mais recente: {change_id}")
            else:
                print("❌ Nenhum change ativo encontrado.")
                sys.exit(1)
        else:
            print("❌ Diretório openspec/changes/active/ não encontrado.")
            sys.exit(1)
    else:
        change_id = sys.argv[1]
    
    result = classify_risk(change_id)
    print_report(result)
```

---

## Instalação

1. Copiar esta pasta para `.skills/esaa-classify-risk/`
2. Garantir que Python 3 está disponível
3. Skill estará disponível como `/esaa-classify-risk`

---

## Integração com Workflow

Esta skill deve ser usada **logo após** criar um change:

```
# Fluxo recomendado
1. /opsx:new add-feature         # Cria change
2. (edita proposal.md brevemente)
3. /esaa-classify-risk           # Classifica risco
4. (baseado na classificação, decide artefatos)
5. /opsx:continue                # Gera artefatos necessários
```

Ou integrada ao `/opsx:propose` via hook (se OpenSpec suportar hooks no futuro).

---

## Testes

```bash
# Testar com change específico
python classify.py add-user-auth

# Testar com change mais recente
python classify.py
```

---

*Skill criada para SOP ESAA Solopreneur v4.1*
