# Skill: esaa-generate-context

**Propósito:** Gerar automaticamente o arquivo `PROJECT_CONTEXT.md` — o resumo executivo do projeto para retomada rápida de contexto.

**Quando usar:**
- Setup inicial de projeto (após criar estrutura base)
- Quando `PROJECT_CONTEXT.md` não existe ou está desatualizado
- Após grandes mudanças no projeto (novos apps, integrações)
- Periodicamente (mensal) para manter sincronizado

**Comando:**
```bash
/esaa-generate-context [--update] [--full]
```

Opções:
- `--update`: Atualiza existente, preservando seções manuais
- `--full`: Gera versão completa (senão, gera versão essencial)

---

## O que é PROJECT_CONTEXT.md

Segundo o SOP ESAA v4.1, o `PROJECT_CONTEXT.md` é:

> **Resumo executivo para retomar sessões rapidamente.** Lido em toda sessão pelo LLM. Elimina a necessidade de "recap" longo.

**Diferença de AGENTS.md:**
- **AGENTS.md**: Regras de execução (como fazer)
- **PROJECT_CONTEXT.md**: Contexto de negócio (o que fazer e por quê)

---

## O que a Skill Faz

1. **Extrai informações** de múltiplas fontes:
   - README.md (propósito do projeto)
   - openspec/specs/ (regras de negócio)
   - Código-fonte (estrutura de apps/módulos)
   - Configurações (settings, requirements)
   - Histórico git (atividade recente)

2. **Gera seções** do PROJECT_CONTEXT.md:
   - Purpose (propósito em 1-2 parágrafos)
   - Authoritative Sources (onde encontrar detalhes)
   - Project Goal (objetivo principal)
   - Architecture (componentes principais)
   - Non-Negotiable Rules (regras de negócio)
   - Technical Constraints (limitações)
   - Quality Bar (padrões de qualidade)

3. **Mantém atualizado** (com `--update`):
   - Preserva edições manuais
   - Atualiza seções automáticas
   - Adiciona novos apps/módulos detectados

---

## Exemplos de Saída

### Exemplo 1: Geração Inicial (Django)

```
$ /esaa-generate-context

🔍 Analisando projeto para gerar contexto...

📄 Fontes analisadas:
   ✓ README.md (encontrado, 450 palavras)
   ✓ openspec/specs/ (3 specs encontradas)
   ✓ Estrutura de código (5 apps Django)
   ✓ requirements.txt (32 dependências)
   ✓ settings.py (configurações extraídas)

🎯 Informações extraídas:
   • Propósito: Sistema de gestão de processos para órgão público
   • Domínio: Jurídico/Administrativo
   • Usuários: Servidores públicos, cidadãos
   • Apps: core, processes, users, reports, notifications
   • Integrações: LDAP, Email, SMS
   • Regras detectadas: 8 regras de negócio

📝 Gerando PROJECT_CONTEXT.md...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ PROJECT_CONTEXT.md criado com sucesso!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📄 Local: ./PROJECT_CONTEXT.md
📊 Estatísticas:
   • 7 seções geradas
   • 850 palavras
   • 5 apps documentados
   • 8 regras de negócio extraídas

⚠️  IMPORTANTE: Revise e ajuste!
   Especialmente:
   • Seção "Purpose" — verifique se reflete visão atual
   • Seção "Non-Negotiable Rules" — adicione regras específicas
   • Seção "Project Goal" — ajuste objetivos mensuráveis

💡 Dica: Atualize este arquivo mensalmente ou após mudanças significativas.
   /esaa-generate-context --update

🚀 Próximo passo:
   /esaa-project-resurrection
   (teste a retomada de contexto)
```

### Exemplo 2: Conteúdo Gerado

```markdown
# PROJECT_CONTEXT.md — Sistema de Processos

## Purpose

Sistema web para digitalização e gestão de processos administrativos 
em órgão público. Permite que cidadãos acompanhem solicitações e 
que servidores gerenciem tramitação de documentos.

Principais funcionalidades:
- Protocolo eletrônico de processos
- Acompanhamento em tempo real
- Emissão de certidões
- Integração com sistema legado de documentos

## Authoritative Sources

- **Especificação completa**: `prompts/handoff.md`
- **Regras de negócio detalhadas**: `openspec/specs/processes/`, `openspec/specs/reports/`
- **Decisões arquiteturais**: `docs/adr/`
- **APIs externas**: Documentação em `docs/integrations/`
- **Em caso de conflito**: Seguir handoff.md, depois specs/

## Project Goal

Digitalizar 100% dos processos administrativos até Q4 2026,
reduzindo tempo médio de tramitação de 45 para 15 dias.

## Architecture

### Apps Django Principais
- **core**: Configurações base, models compartilhados
- **processes**: Gestão de processos e tramitação
- **users**: Autenticação (LDAP), perfis, permissões
- **reports**: Geração de relatórios e certidões
- **notifications**: Email, SMS, alertas

### Fluxo de Dados Crítico
1. Cidadão cadastra solicitação (processes)
2. Sistema atribui protocolo único (core)
3. Servidor analisa e movimenta (processes)
4. Notificações automáticas enviadas (notifications)
5. Relatórios gerados para gestão (reports)

### Integrações Externas
- **LDAP/AD**: Autenticação de servidores
- **SMTP**: Envio de emails transacionais
- **SMS Gateway**: Alertas para cidadãos
- **S3**: Armazenamento de documentos digitalizados

## Non-Negotiable Rules

### Regras de Negócio
- Todo processo DEVE ter protocolo único gerado automaticamente
- NENHUMA exclusão física de dados — apenas marcação como cancelado
- Auditoria obrigatória para toda movimentação de processo
- SLA máximo de 5 dias para primeira resposta
- Campos sensíveis DEVEm ser criptografados (CPF, endereço)

### Constraints Técnicos
- Django 4.2 LTS (suporte longo prazo)
- PostgreSQL 14+ (para JSONB e queries complexas)
- Frontend: HTML vanilla + Bootstrap (sem frameworks JS pesados)
- Timeout máximo de requisições: 30 segundos
- Upload máximo de arquivos: 50MB

### Compliance
- LGPD: Dados pessoais criptografados e consentimento explícito
- INDA: Padrão de interoperabilidade para órgãos públicos
- Acessibilidade: WCAG 2.1 nível AA

## Technical Constraints

- **Deploy**: Docker em infraestrutura própria (não cloud pública)
- **SSL**: Obrigatório para todos os ambientes
- **Backup**: Diário, retenção de 90 dias
- **Monitoramento**: Logs centralizados, alertas para erros 500
- **Limite de usuários simultâneos**: 500 (planejado para 2000 em 2027)

## Quality Bar

### Comandos de Verificação
```bash
# Testes
python manage.py test --parallel

# Lint
ruff check . && ruff format .

# Type check (parcial)
mypy core/ users/

# Security check
bandit -r . -f json
```

### Critérios de Aceitação
- Cobertura de testes: mínimo 70% em lógica de negócio
- Zero vulnerabilidades críticas (bandit)
- Lighthouse score > 90 (performance, acessibilidade)
- Tempo de resposta médio < 500ms

---

*Gerado em: 2026-03-02*
*Última atualização: 2026-03-02*
*Gerado por: esaa-generate-context*
```

### Exemplo 3: Update (Atualização)

```
$ /esaa-generate-context --update

⚠️  PROJECT_CONTEXT.md já existe (última atualização: 2026-01-15, 46 dias atrás)

🔍 Analisando mudanças desde última atualização...

📊 Alterações detectadas:
   + Novo app: analytics (não estava documentado)
   + Nova integração: Webhook para sistema externo
   + Novas regras detectadas em specs/ (3 regras)
   ~ Apps modificados: reports (adicionado export PDF)
   ~ Stack atualizado: Django 4.2 → 5.0
   - App removido: legacy_import (não mais usado)

📝 Atualizando PROJECT_CONTEXT.md...
   ✓ Seção "Architecture" atualizada
   ✓ Seção "Non-Negotiable Rules" atualizada (+3 regras)
   ✓ Seção "Technical Constraints" atualizada (Django 5.0)
   ✓ Seção "Integrations" atualizada (+webhook)
   ○ Seção "Purpose" preservada (edição manual detectada)
   ○ Seção "Project Goal" preservada (edição manual detectada)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔄 PROJECT_CONTEXT.md atualizado!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Resumo de mudanças:
   + 1 app adicionado (analytics)
   + 1 integração adicionada (webhook)
   + 3 regras de negócio adicionadas
   ~ 1 app modificado (reports)
   ~ Stack atualizado (Django 5.0)
   - 1 app removido (legacy_import)

⚠️  Seções preservadas (edição manual detectada):
   • Purpose — mantido texto original
   • Project Goal — mantido texto original

💡 Revise as atualizações para garantir consistência.
```

---

## Estrutura do Arquivo Gerado

```markdown
# PROJECT_CONTEXT.md — [Nome do Projeto]

## Purpose
[1-2 parágrafos sobre o que o sistema faz, para quem, principais funcionalidades]

## Authoritative Sources
[Links para documentações detalhadas]

## Project Goal
[Objetivo mensurável do projeto]

## Architecture
[Apps/módulos principais, fluxo de dados, integrações]

## Non-Negotiable Rules
[Regras de negócio que não podem ser violadas]

## Technical Constraints
[Limitações técnicas, requisitos de compliance]

## Quality Bar
[Comandos de verificação, critérios de aceitação]
```

---

## Fontes de Informação

A skill extrai dados de:

| Fonte | O que Extrai | Confiança |
|-------|--------------|-----------|
| `README.md` | Propósito, descrição geral | Alta |
| `openspec/specs/` | Regras de negócio, capabilities | Alta |
| `docs/adr/` | Decisões arquiteturais | Média |
| Estrutura de diretórios | Apps, módulos | Alta |
| `requirements.txt`/`package.json` | Stack, dependências | Alta |
| `settings.py`/`config.*` | Configurações, integrações | Média |
| Git history | Atividade recente, contribuidores | Baixa |
| `AGENTS.md` (se existir) | Constraints técnicos | Média |

---

## Implementação

### Dependências

```python
# requirements.txt
pyyaml>=6.0
python-frontmatter>=1.0.0  # Para parsear markdown com metadata
```

### Estrutura

```
esaa-generate-context/
├── SKILL.md              # Este arquivo
├── generate.py           # Script principal
├── extractors/
│   ├── __init__.py
│   ├── readme.py         # Extrai do README
│   ├── specs.py          # Extrai das specs OpenSpec
│   ├── codebase.py       # Analisa estrutura de código
│   └── config.py         # Extrai de configurações
├── templates/
│   ├── full.md           # Template versão completa
│   └── essential.md      # Template versão essencial
└── utils.py              # Funções auxiliares
```

### Lógica Principal (generate.py)

```python
#!/usr/bin/env python3
"""
Gerador de PROJECT_CONTEXT.md para SOP ESAA Solopreneur v4.1
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class ContextExtractor:
    """Extrai informações do projeto de várias fontes"""
    
    def __init__(self, project_root: str = "."):
        self.root = Path(project_root).resolve()
        self.data = {
            "name": self.root.name,
            "purpose": "",
            "sources": [],
            "goal": "",
            "architecture": {},
            "rules": [],
            "constraints": {},
            "quality": {}
        }
    
    def extract_all(self) -> Dict:
        """Extrai todas as informações disponíveis"""
        self._extract_from_readme()
        self._extract_from_specs()
        self._extract_from_codebase()
        self._extract_from_configs()
        self._extract_from_agents()
        return self.data
    
    def _extract_from_readme(self):
        """Extrai propósito do README.md"""
        readme = self.root / "README.md"
        if not readme.exists():
            return
        
        content = readme.read_text()
        lines = content.split('\n')
        
        # Tenta extrair primeira seção significativa
        purpose_lines = []
        in_purpose = False
        
        for line in lines:
            # Pula linhas iniciais (badges, título)
            if line.startswith('# ') and not purpose_lines:
                continue
            if line.startswith('!['):  # Badges
                continue
            
            # Começa a capturar após título ou na primeira linha não-vazia
            if line.strip() and not purpose_lines:
                in_purpose = True
            
            # Para em próxima seção ou após parágrafo vazio + nova seção
            if in_purpose:
                if line.startswith('##') or line.startswith('# '):
                    break
                if len(purpose_lines) > 50:  # Limite de segurança
                    break
                purpose_lines.append(line)
        
        purpose = '\n'.join(purpose_lines).strip()
        # Limita a 2-3 parágrafos
        paragraphs = [p for p in purpose.split('\n\n') if p.strip()]
        self.data["purpose"] = '\n\n'.join(paragraphs[:3])
    
    def _extract_from_specs(self):
        """Extrai regras de negócio das specs OpenSpec"""
        specs_dir = self.root / "openspec" / "specs"
        if not specs_dir.exists():
            return
        
        rules = []
        sources = ["openspec/specs/"]
        
        for spec_file in specs_dir.rglob("*.md"):
            content = spec_file.read_text()
            
            # Extrai regras (linhas com "must", "should", "NUNCA", etc.)
            for line in content.split('\n'):
                line = line.strip()
                if any(kw in line.lower() for kw in ['must', 'should', 'deve', 'nunca', 'sempre', 'obrigatório']):
                    if len(line) < 200:  # Evita parágrafos longos
                        rules.append(line.lstrip('- ').lstrip('* '))
        
        self.data["rules"] = list(set(rules))[:15]  # Remove duplicatas, limita
        self.data["sources"].extend(sources)
    
    def _extract_from_codebase(self):
        """Analisa estrutura do código"""
        architecture = {
            "apps": [],
            "modules": [],
            "integrations": []
        }
        
        # Detecta Django apps
        if (self.root / "manage.py").exists():
            for path in self.root.iterdir():
                if path.is_dir() and not path.name.startswith('.'):
                    # Verifica se é app Django
                    if (path / "models.py").exists() or (path / "apps.py").exists():
                        architecture["apps"].append({
                            "name": path.name,
                            "has_models": (path / "models.py").exists(),
                            "has_views": (path / "views.py").exists()
                        })
        
        # Detecta Node.js modules
        elif (self.root / "package.json").exists():
            src_dir = self.root / "src"
            if src_dir.exists():
                for path in src_dir.iterdir():
                    if path.is_dir():
                        architecture["modules"].append(path.name)
        
        # Detecta integrações por keywords em arquivos
        settings = self.root / "settings.py"
        if settings.exists():
            content = settings.read_text().lower()
            integrations = []
            if 'ldap' in content:
                integrations.append("LDAP")
            if 'email' in content or 'smtp' in content:
                integrations.append("Email/SMTP")
            if 'stripe' in content:
                integrations.append("Stripe")
            if 's3' in content or 'boto' in content:
                integrations.append("AWS S3")
            if 'celery' in content:
                integrations.append("Celery")
            architecture["integrations"] = integrations
        
        self.data["architecture"] = architecture
    
    def _extract_from_configs(self):
        """Extrai constraints de arquivos de configuração"""
        constraints = {}
        
        # Django settings
        settings = self.root / "settings.py"
        if settings.exists():
            content = settings.read_text()
            if 'DEBUG = False' in content:
                constraints["production_ready"] = True
            if 'DATABASES' in content and 'postgres' in content.lower():
                constraints["database"] = "PostgreSQL"
        
        # requirements.txt
        req = self.root / "requirements.txt"
        if req.exists():
            content = req.read_text()
            if 'django' in content.lower():
                match = re.search(r'Django[=<>~!]+([0-9.]+)', content)
                if match:
                    constraints["django_version"] = match.group(1)
        
        self.data["constraints"] = constraints
    
    def _extract_from_agents(self):
        """Extrai quality bar do AGENTS.md se existir"""
        agents = self.root / "AGENTS.md"
        if not agents.exists():
            return
        
        content = agents.read_text()
        quality = {}
        
        # Extrai comandos de verificação
        if 'test:' in content.lower() or 'pytest' in content.lower():
            # Tenta extrair comando de teste
            for line in content.split('\n'):
                if 'test:' in line.lower() or 'pytest' in line or 'manage.py test' in line:
                    quality["test_command"] = line.strip().lstrip('- ').lstrip('* ')
                    break
        
        if 'lint:' in content.lower() or 'ruff' in content.lower():
            for line in content.split('\n'):
                if 'lint:' in line.lower() or 'ruff' in line or 'flake8' in line:
                    quality["lint_command"] = line.strip().lstrip('- ').lstrip('* ')
                    break
        
        self.data["quality"] = quality


class ContextGenerator:
    """Gera o conteúdo do PROJECT_CONTEXT.md"""
    
    def __init__(self, data: Dict, template_type: str = "essential"):
        self.data = data
        self.template_type = template_type
    
    def generate(self) -> str:
        """Gera conteúdo completo"""
        if self.template_type == "full":
            return self._generate_full()
        return self._generate_essential()
    
    def _generate_essential(self) -> str:
        """Versão essencial (mais curta)"""
        return f"""# PROJECT_CONTEXT.md — {self.data['name'].title()}

## Purpose

{self.data.get('purpose', '[Descreva o propósito do projeto]')}

## Authoritative Sources

- **Handoff completo**: `prompts/handoff.md` (se existir)
- **Specs**: `openspec/specs/`
- **ADRs**: `docs/adr/`
- **Em caso de conflito**: Seguir specs/

## Project Goal

[Defina o objetivo principal do projeto de forma mensurável]

## Architecture

### Componentes Principais
{self._format_apps()}

### Integrações
{self._format_integrations()}

## Non-Negotiable Rules

### Regras de Negócio
{self._format_rules()}

### Constraints Técnicos
{self._format_constraints()}

## Quality Bar

### Comandos de Verificação
{self._format_quality()}

---

*Gerado em: {datetime.now().strftime('%Y-%m-%d')}*
*Por: esaa-generate-context*
"""
    
    def _generate_full(self) -> str:
        """Versão completa (mais detalhada)"""
        # Similar ao essential mas com mais seções
        return self._generate_essential()  # Simplificado para exemplo
    
    def _format_apps(self) -> str:
        """Formata lista de apps"""
        apps = self.data.get('architecture', {}).get('apps', [])
        if not apps:
            return "- [Liste os apps/módulos principais]"
        
        lines = []
        for app in apps[:10]:  # Limita
            name = app['name']
            components = []
            if app.get('has_models'):
                components.append("models")
            if app.get('has_views'):
                components.append("views")
            
            if components:
                lines.append(f"- **{name}**: {', '.join(components)}")
            else:
                lines.append(f"- **{name}**")
        
        return '\n'.join(lines)
    
    def _format_integrations(self) -> str:
        """Formata lista de integrações"""
        integrations = self.data.get('architecture', {}).get('integrations', [])
        if not integrations:
            return "- [Liste integrações externas, se houver]"
        return '\n'.join(f"- {i}" for i in integrations)
    
    def _format_rules(self) -> str:
        """Formata regras de negócio"""
        rules = self.data.get('rules', [])
        if not rules:
            return "- [Defina regras de negócio críticas]"
        return '\n'.join(f"- {r}" for r in rules[:10])
    
    def _format_constraints(self) -> str:
        """Formata constraints"""
        constraints = self.data.get('constraints', {})
        if not constraints:
            return "- [Liste constraints técnicos]"
        
        lines = []
        if 'django_version' in constraints:
            lines.append(f"- Django {constraints['django_version']}")
        if 'database' in constraints:
            lines.append(f"- Banco de dados: {constraints['database']}")
        if 'production_ready' in constraints:
            lines.append("- Configurado para produção")
        
        return '\n'.join(lines) if lines else "- [Liste constraints técnicos]"
    
    def _format_quality(self) -> str:
        """Formata quality bar"""
        quality = self.data.get('quality', {})
        lines = []
        
        if 'test_command' in quality:
            lines.append(f"- **Testes**: `{quality['test_command']}`")
        else:
            lines.append("- **Testes**: `[comando de teste]`")
        
        if 'lint_command' in quality:
            lines.append(f"- **Lint**: `{quality['lint_command']}`")
        else:
            lines.append("- **Lint**: `[comando de lint]`")
        
        return '\n'.join(lines)


def main():
    """Função principal da skill"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Gera PROJECT_CONTEXT.md")
    parser.add_argument("--update", action="store_true", help="Atualiza arquivo existente")
    parser.add_argument("--full", action="store_true", help="Gera versão completa")
    parser.add_argument("--output", "-o", default="PROJECT_CONTEXT.md", help="Nome do arquivo")
    args = parser.parse_args()
    
    output_path = Path(args.output)
    
    # Verifica se existe
    if output_path.exists() and not args.update:
        print(f"⚠️  {args.output} já existe!")
        print("   Use --update para atualizar")
        print("   Ou delete o arquivo para gerar do zero")
        return 1
    
    # Extrai dados
    print("🔍 Analisando projeto para gerar contexto...\n")
    
    extractor = ContextExtractor()
    data = extractor.extract_all()
    
    print(f"📄 Fontes analisadas:")
    print(f"   • README.md: {'✓' if data.get('purpose') else '✗'}")
    print(f"   • Specs: {len(data.get('rules', []))} regras encontradas")
    print(f"   • Apps: {len(data.get('architecture', {}).get('apps', []))} detectados")
    print(f"   • Integrações: {len(data.get('architecture', {}).get('integrations', []))}")
    
    # Gera conteúdo
    template = "full" if args.full else "essential"
    generator = ContextGenerator(data, template)
    content = generator.generate()
    
    # Salva
    output_path.write_text(content)
    
    print(f"\n{'━'*50}")
    print("✅ PROJECT_CONTEXT.md gerado com sucesso!")
    print(f"{'━'*50}")
    print(f"📄 Local: {output_path.absolute()}")
    print(f"📊 Tamanho: {len(content)} caracteres")
    
    print("\n⚠️  IMPORTANTE: Revise e ajuste as seções:")
    print("   • Purpose — verifique se reflete visão atual")
    print("   • Project Goal — defina objetivos mensuráveis")
    print("   • Non-Negotiable Rules — adicione regras específicas")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

---

## Diferença: Essential vs Full

### Essential (padrão)
- ~500-800 palavras
- 7 seções básicas
- Foco em retomada rápida
- Geração em segundos

### Full (--full)
- ~1500+ palavras
- 10+ seções
- Inclui diagramas de fluxo
- Análise detalhada de dependências
- Seção de troubleshooting
- Geração em 10-20s

**Recomendação:** Use `essential` para projetos pequenos/médios. `full` para projetos enterprise ou com muitas integrações.

---

## Integração com Workflow

```
# Setup de novo projeto
1. django-admin startproject meu_projeto
2. cd meu_projeto
3. /esaa-generate-agents      # Cria AGENTS.md
4. /esaa-generate-context     # Cria PROJECT_CONTEXT.md
5. openspec init              # Inicializa OpenSpec
6. git add . && git commit    # Commit inicial

# Trabalho diário
1. cd meu_projeto
2. /esaa-project-resurrection # Lê PROJECT_CONTEXT.md automaticamente
3. (trabalha...)
4. git commit && git push

# Manutenção mensal
1. /esaa-generate-context --update
2. Revisa mudanças
3. git commit -am "docs: atualiza PROJECT_CONTEXT"
```

---

## Quando Atualizar

Atualize `PROJECT_CONTEXT.md` quando:

- [ ] Novo app/módulo adicionado
- [ ] Nova integração externa
- [ ] Mudança de stack (versões)
- [ ] Novas regras de negócio definidas
- [ ] Alteração de objetivos do projeto
- [ ] A cada 30 dias (manutenção preventiva)

---

## Relação com Outras Skills

| Skill | Arquivo Gerado | Propósito |
|-------|---------------|-----------|
| `esaa-generate-agents` | AGENTS.md | Como fazer (regras de execução) |
| `esaa-generate-context` | PROJECT_CONTEXT.md | O que fazer (contexto de negócio) |
| `esaa-project-resurrection` | — | Usa PROJECT_CONTEXT.md para retomada |

**Ambos são necessários:**
- AGENTS.md = manual de operação
- PROJECT_CONTEXT.md = briefing do projeto

---

## Instalação

```bash
# Copiar para skills do Pi
cp -r esaa-generate-context ~/.pi/skills/

# Disponível como /esaa-generate-context
```

---

*Skill criada para SOP ESAA Solopreneur v4.1 — Contexto sempre fresco*
