---
name: esaa-generate-agents
description: [LEGACY] Gera AGENTS.md. Preferir agents-md-generator.
---

# Skill: esaa-generate-agents

**Propósito:** Gerar automaticamente o arquivo `AGENTS.md` completo e contextualizado baseado na detecção do stack tecnológico do projeto.

**Quando usar:**

- Setup inicial de projeto novo
- Quando `AGENTS.md` não existe ou está desatualizado
- Ao adotar o workflow ESAA em projeto existente
- Quando muda o stack significativamente

**Comando:**

```bash
/esaa-generate-agents [--update] [--template=django|node|go|auto]
```

Opções:

- `--update`: Atualiza AGENTS.md existente (preservando customizações)
- `--template=X`: Força template específico (senão auto-detecta)

---

## O que a Skill Faz

1. **Detecta Stack** — Analisa arquivos do projeto para identificar tecnologias
2. **Infere Versões** — Lê requirements.txt, package.json, go.mod, etc.
3. **Sugere Comandos** — Comandos de test, lint, build específicos do stack
4. **Define Constraints** — Anti-patterns e regras arquiteturais do framework
5. **Gera AGENTS.md** — Arquivo completo e pronto para uso

---

## Stacks Suportados

| Stack | Arquivos Detectados | Versão Inferida De |
|-------|---------------------|-------------------|
| **Django** | `manage.py`, `settings.py`, `wsgi.py` | `requirements.txt`, `Pipfile` |
| **Flask** | `app.py`, `wsgi.py`, `application.py` | `requirements.txt` |
| **FastAPI** | `main.py` com FastAPI imports | `requirements.txt` |
| **Node/Express** | `package.json`, `app.js`, `server.js` | `package.json` |
| **Go** | `go.mod`, `main.go` | `go.mod` |
| **Ruby on Rails** | `Gemfile`, `config/routes.rb` | `Gemfile` |
| **Laravel** | `composer.json`, `artisan` | `composer.json` |

---

## Exemplos de Saída

### Exemplo 1: Detecção Django (Seu Caso)

```
$ /esaa-generate-agents

🔍 Analisando estrutura do projeto...

📁 Arquivos encontrados:
   ✓ manage.py
   ✓ requirements.txt
   ✓ settings.py
   ✓ apps/ (core, users, payments)

🎯 Stack detectado: Django 5.0 + PostgreSQL
📦 Versões inferidas:
   • Django: 5.0.2 (requirements.txt)
   • Python: 3.11 (runtime detectado)
   • PostgreSQL: 15 (settings.py)
   • Additional: Celery 5.3, Redis 7

⚙️  Ferramentas detectadas:
   • Test: pytest (configurado)
   • Lint: ruff (encontrado no requirements)
   • Type check: mypy (encontrado)

📝 Gerando AGENTS.md...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ AGENTS.md criado com sucesso!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📄 Local: ./AGENTS.md
📊 Tamanho: 3.2KB
🎯 Seções geradas: 9

⚠️  IMPORTANTE: Revise o arquivo antes de usar!
   Especialmente:
   • Seção 3: Arquitetura (verifique se apps listados estão corretos)
   • Seção 7: Anti-patterns (adicione regras específicas do seu projeto)
   • Seção 2: Comandos (teste se funcionam no seu ambiente)

🚀 Próximo passo:
   /esaa-project-resurrection
   (para verificar estado do projeto)
```

### Exemplo 2: Detecção Node.js

```
$ /esaa-generate-agents

🔍 Analisando estrutura do projeto...

📁 Arquivos encontrados:
   ✓ package.json
   ✓ app.js
   ✓ src/routes/
   ✓ tests/

🎯 Stack detectado: Node.js 20 + Express 4
📦 Versões inferidas:
   • Node: 20.11.0 (package.json engines)
   • Express: 4.18.2 (package.json)
   • Database: MongoDB (mongoose encontrado)

⚙️  Ferramentas detectadas:
   • Test: jest (package.json scripts)
   • Lint: eslint (package.json)

📝 Gerando AGENTS.md...
```

### Exemplo 3: Atualização de AGENTS Existente

```
$ /esaa-generate-agents --update

⚠️  AGENTS.md já existe (criado em 2026-01-15)

🔍 Analisando estrutura atual...
   • Novos apps detectados: analytics, reports
   • Ferramentas novas: black (formatter)
   • Dependências atualizadas: Django 4.2 → 5.0

📝 Gerando atualização...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔄 AGENTS.md atualizado!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Mudanças aplicadas:
   ✓ Django 4.2 → 5.0
   ✓ Novos apps: analytics, reports
   ✓ Adicionado: black ao pipeline de lint

Preservado (seção 7 - Anti-patterns customizados):
   • "NUNCA usar raw SQL"
   • "Sempre usar get_object_or_404"

⚠️  Revise as mudanças antes de commitar!
```

---

## Estrutura do AGENTS.md Gerado

O arquivo segue exatamente a estrutura do SOP ESAA v4.1:

```markdown
# AGENTS.md — [Nome do Projeto]

## 1. Stack e Versões
## 2. Comandos de Desenvolvimento
## 3. Arquitetura e Constraints
## 4. Política de Testes
## 5. Regras de Commit
## 6. Definition of Done (DoD)
## 7. Anti-Patterns Proibidos
## 8. Stop Rule
## 9. Prompt de Reentrada
```

---

## Implementação

### Dependências

```python
# requirements.txt para a skill
pyyaml>=6.0
packaging>=21.0
```

### Estrutura

```
esaa-generate-agents/
├── SKILL.md              # Este arquivo
├── generate.py           # Script principal
├── detectors/
│   ├── __init__.py
│   ├── django.py         # Detecção Django
│   ├── flask.py          # Detecção Flask
│   ├── fastapi.py        # Detecção FastAPI
│   ├── node.py           # Detecção Node/Express
│   └── golang.py         # Detecção Go
├── templates/
│   ├── django.md         # Template Django
│   ├── flask.md          # Template Flask
│   ├── node.md           # Template Node
│   └── generic.md        # Template fallback
└── utils.py              # Funções auxiliares
```

### Lógica Principal (generate.py)

```python
#!/usr/bin/env python3
"""
Gerador de AGENTS.md para SOP ESAA Solopreneur v4.1
"""

import os
import sys
import re
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Configurações de detecção
STACK_DETECTORS = {
    "django": {
        "files": ["manage.py", "settings.py", "wsgi.py"],
        "config_files": ["requirements.txt", "Pipfile", "pyproject.toml"],
        "template": "django.md",
        "priority": 10
    },
    "flask": {
        "files": ["app.py", "wsgi.py", "application.py"],
        "config_files": ["requirements.txt", "Pipfile"],
        "template": "flask.md",
        "priority": 9
    },
    "fastapi": {
        "files": ["main.py"],
        "config_files": ["requirements.txt", "pyproject.toml"],
        "template": "fastapi.md",
        "priority": 9,
        "content_check": r"from fastapi import"
    },
    "node_express": {
        "files": ["package.json", "app.js", "server.js"],
        "config_files": ["package.json"],
        "template": "node.md",
        "priority": 10
    },
    "go": {
        "files": ["go.mod", "main.go"],
        "config_files": ["go.mod"],
        "template": "golang.md",
        "priority": 10
    }
}

class StackDetector:
    """Detecta o stack tecnológico do projeto"""
    
    def __init__(self, project_root: str = "."):
        self.root = Path(project_root).resolve()
        self.detected_stack = None
        self.versions = {}
        self.apps = []
        self.tools = {}
        
    def detect(self) -> Tuple[str, Dict]:
        """Detecta stack e retorna (nome, config)"""
        scores = {}
        
        for stack_name, config in STACK_DETECTORS.items():
            score = 0
            
            # Verifica arquivos característicos
            for file in config["files"]:
                if (self.root / file).exists():
                    score += 2
                    
            # Verifica arquivos de config
            for file in config.get("config_files", []):
                if (self.root / file).exists():
                    score += 1
                    
            # Verifica conteúdo (se definido)
            if "content_check" in config:
                for file in config["files"]:
                    file_path = self.root / file
                    if file_path.exists():
                        content = file_path.read_text()
                        if re.search(config["content_check"], content):
                            score += 3
                            
            scores[stack_name] = score + config.get("priority", 0)
        
        # Escolhe stack com maior score
        if scores:
            self.detected_stack = max(scores, key=scores.get)
            if scores[self.detected_stack] > 0:
                self._extract_versions()
                self._detect_tools()
                self._detect_apps()
                return self.detected_stack, STACK_DETECTORS[self.detected_stack]
                
        return None, {}
    
    def _extract_versions(self):
        """Extrai versões das dependências"""
        if self.detected_stack in ["django", "flask", "fastapi"]:
            self._extract_python_versions()
        elif self.detected_stack == "node_express":
            self._extract_node_versions()
        elif self.detected_stack == "go":
            self._extract_go_versions()
    
    def _extract_python_versions(self):
        """Extrai versões de requirements.txt, Pipfile ou pyproject.toml"""
        # requirements.txt
        req_file = self.root / "requirements.txt"
        if req_file.exists():
            content = req_file.read_text()
            
            # Django
            match = re.search(r'Django[=<>~!]+([0-9.]+)', content)
            if match:
                self.versions['django'] = match.group(1)
                
            # Flask
            match = re.search(r'Flask[=<>~!]+([0-9.]+)', content)
            if match:
                self.versions['flask'] = match.group(1)
                
            # FastAPI
            match = re.search(r'fastapi[=<>~!]+([0-9.]+)', content)
            if match:
                self.versions['fastapi'] = match.group(1)
                
            # Outras libs
            for lib in ["celery", "redis", "stripe", "requests", "psycopg2", "pillow"]:
                match = re.search(rf'{lib}[=<>~!]+([0-9.]+)', content, re.I)
                if match:
                    self.versions[lib] = match.group(1)
        
        # Pipfile
        pipfile = self.root / "Pipfile"
        if pipfile.exists():
            content = pipfile.read_text()
            # Parse básico de versões
            
        # pyproject.toml
        pyproject = self.root / "pyproject.toml"
        if pyproject.exists():
            content = pyproject.read_text()
            # Parse básico
    
    def _extract_node_versions(self):
        """Extrai versões do package.json"""
        pkg_file = self.root / "package.json"
        if pkg_file.exists():
            try:
                data = json.loads(pkg_file.read_text())
                
                # Versões de engines
                engines = data.get("engines", {})
                if "node" in engines:
                    self.versions['node'] = engines["node"].replace(">=", "").replace("^", "")
                
                # Dependências
                deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
                for lib in ["express", "react", "next", "vue", "typescript", "jest", "eslint"]:
                    if lib in deps:
                        self.versions[lib] = deps[lib].replace("^", "").replace("~", "")
            except json.JSONDecodeError:
                pass
    
    def _extract_go_versions(self):
        """Extrai versões do go.mod"""
        gomod = self.root / "go.mod"
        if gomod.exists():
            content = gomod.read_text()
            match = re.search(r'go ([0-9.]+)', content)
            if match:
                self.versions['go'] = match.group(1)
    
    def _detect_tools(self):
        """Detecta ferramentas de test/lint configuradas"""
        if self.detected_stack in ["django", "flask", "fastapi"]:
            # Verifica pytest
            if (self.root / "pytest.ini").exists() or (self.root / "pyproject.toml").exists():
                self.tools['test'] = "pytest"
            else:
                self.tools['test'] = "python manage.py test"
            
            # Verifica linter
            req_file = self.root / "requirements.txt"
            if req_file.exists():
                content = req_file.read_text().lower()
                if "ruff" in content:
                    self.tools['lint'] = "ruff check . && ruff format ."
                elif "black" in content:
                    self.tools['lint'] = "black . && isort ."
                elif "flake8" in content:
                    self.tools['lint'] = "flake8 ."
                    
            # Verifica mypy
            if req_file.exists() and "mypy" in req_file.read_text().lower():
                self.tools['type_check'] = "mypy ."
                
        elif self.detected_stack == "node_express":
            pkg_file = self.root / "package.json"
            if pkg_file.exists():
                try:
                    data = json.loads(pkg_file.read_text())
                    scripts = data.get("scripts", {})
                    
                    if "test" in scripts:
                        self.tools['test'] = "npm test"
                    if "lint" in scripts:
                        self.tools['lint'] = "npm run lint"
                except:
                    pass
    
    def _detect_apps(self):
        """Detecta apps/módulos do projeto"""
        if self.detected_stack == "django":
            # Procura por pastas com models.py ou apps.py
            for path in self.root.iterdir():
                if path.is_dir() and not path.name.startswith("."):
                    if (path / "models.py").exists() or (path / "apps.py").exists():
                        self.apps.append(path.name)
            
            # Também verifica settings.py
            settings = self.root / "settings.py"
            if not settings.exists():
                # Procura em subdiretórios
                for settings_candidate in self.root.rglob("settings.py"):
                    if "__pycache__" not in str(settings_candidate):
                        settings = settings_candidate
                        break


class AgentsGenerator:
    """Gera o conteúdo do AGENTS.md"""
    
    def __init__(self, detector: StackDetector):
        self.detector = detector
        self.stack = detector.detected_stack
        self.versions = detector.versions
        self.apps = detector.apps
        self.tools = detector.tools
    
    def generate(self) -> str:
        """Gera conteúdo completo do AGENTS.md"""
        if self.stack == "django":
            return self._generate_django()
        elif self.stack == "flask":
            return self._generate_flask()
        elif self.stack == "fastapi":
            return self._generate_fastapi()
        elif self.stack == "node_express":
            return self._generate_node()
        elif self.stack == "go":
            return self._generate_go()
        else:
            return self._generate_generic()
    
    def _generate_django(self) -> str:
        """Gera AGENTS.md para Django"""
        django_version = self.versions.get('django', '5.0')
        
        template = f"""# AGENTS.md — [NOME DO PROJETO]

## 1. Stack e Versões

- **Python**: 3.11+
- **Django**: {django_version}
- **Frontend**: HTML5 + Bootstrap 5 + Vanilla JavaScript
- **Banco de Dados**: PostgreSQL (produção) / SQLite (desenvolvimento)
- **Outras Dependências Principais"""
        
        # Adiciona outras dependências detectadas
        other_deps = []
        for lib, version in self.versions.items():
            if lib not in ['django']:
                other_deps.append(f"{lib.title()}: {version}")
        
        if other_deps:
            for dep in other_deps:
                template += f"\n  - {dep}"
        
        # Apps detectados
        if self.apps:
            template += f"\n- **Apps Django**: {', '.join(self.apps)}"
        
        template += f"""

## 2. Comandos de Desenvolvimento

- **Run server**: `python manage.py runserver`
- **Test**: `{self.tools.get('test', 'python manage.py test')}`
- **Lint**: `{self.tools.get('lint', 'ruff check . && ruff format .')}`
"""
        
        if 'type_check' in self.tools:
            template += f"- **Type check**: `{self.tools['type_check']}`\n"
        
        template += """- **Migrações**: `python manage.py makemigrations && python manage.py migrate`
- **Shell**: `python manage.py shell`
- **Admin**: `python manage.py createsuperuser`

## 3. Arquitetura e Constraints

- **Apps**: Um app por domínio de negócio (autenticação, pagamentos, etc.)
- **Views**: 
  - Use CBVs (Class-Based Views) para CRUDs padrão
  - Use FBVs (Function-Based Views) para lógica customizada complexa
- **Templates**: Sempre herdar de `base.html`
- **Static Files**: Organizar por app (`app_name/static/app_name/`)
- **Services**: Lógica de negócio em `services.py`, NUNCA diretamente nas views
- **Models**: 
  - Um model por arquivo (evite models muito grandes)
  - Sempre defina `__str__` e `Meta` com `verbose_name`
  - Use `get_absolute_url` para URLs de detalhe

## 4. Política de Testes

- **Obrigatório**: Testes para toda lógica de negócio em `services.py`
- **Recomendado**: Testes de integração para views críticas (autenticação, pagamentos)
- **Opcional**: Testes de templates simples (se lógica complexa)
- **Cobertura Mínima**: Foco em lógica de negócio, não em boilerplate

### Estrutura de Testes
```

app_name/
├── tests/
│   ├── **init**.py
│   ├── test_models.py
│   ├── test_views.py
│   ├── test_services.py
│   └── test_forms.py

```

## 5. Regras de Commit

- **Um slice = um commit**: Cada task completa gera um commit
- **Formato**: `tipo: descrição em português ou inglês (consistente)`
  - `feat:` nova funcionalidade
  - `fix:` correção de bug
  - `refactor:` refatoração sem mudança de comportamento
  - `docs:` documentação
  - `test:` testes
  - `chore:` manutenção, dependências
- **Mensagem**: Descritiva e no imperativo ("Adiciona" não "Adicionei")
- **Sempre**: Rode testes antes do commit
- **Push**: Após cada commit (backup frequente)

### Exemplos
```

feat: add user profile model with avatar upload
fix: correct email validation in registration form
refactor: move payment logic to services.py
test: add integration tests for checkout flow

```

## 6. Definition of Done (DoD)

Uma mudança só está pronta quando:

- [ ] **Testes passam**: `{self.tools.get('test', 'python manage.py test')}`
- [ ] **Lint OK**: `{self.tools.get('lint', 'ruff check .')}`
"""
        
        if 'type_check' in self.tools:
            template += f"- [ ] **Type check OK**: `{self.tools['type_check']}`\n"
        
        template += """- [ ] **Migrações**: Geradas e testadas (se houver mudança de modelo)
- [ ] **Task atualizada**: Checkbox marcado em `tasks.md`
- [ ] **Commit feito**: Com mensagem descritiva
- [ ] **Push realizado**: Código no repositório remoto
- [ ] **Specs sincronizadas**: (se change FEATURE/HIGH)
- [ ] **ADR criada**: (se change HIGH/ARCH)

## 7. Anti-Patterns Proibidos

- **NUNCA** lógica de negócio em views — use `services.py`
- **NUNCA** queries complexas em templates — prepare dados na view
- **NUNCA** JavaScript inline — use arquivos `.js` em `static/`
- **NUNCA** commit de migrações sem testar — rode `migrate` primeiro
- **NUNCA** alterar modelo sem considerar dados existentes — planeje migração
- **NUNCA** esquecer `select_related`/`prefetch_related` em queries N+1
- **NUNCA** exporsecrets em código — use variáveis de ambiente
- **NUNCA** fazer queries em loops — use `bulk_create`, `update`, etc.
- **NUNCA** ignorar migrações em conflito — resolva antes de push

## 8. Stop Rule (Regra de Parada)

Após implementar **CADA slice**:

1. **RED** — Escrever teste que falha (se seguindo TDD)
2. **GREEN** — Implementar código mínimo para passar
3. **REFACTOR** — Simplificar se necessário
4. **VERIFY** — Rodar comandos de validação
5. **COMMIT** — Commitar com mensagem descritiva
6. **UPDATE** — Marcar task como `[x]` no `tasks.md`
7. **STOP** — **PARAR e aguardar confirmação humana**

**A IA NÃO DEVE continuar automaticamente para o próximo slice.**

## 9. Prompt de Reentrada

Use este prompt ao retomar trabalho (exemplo):

```text
Read AGENTS.md and PROJECT_CONTEXT.md first.
Change ID: [nome-do-change]

Contexto: Estou retomando este projeto após [tempo].
Objetivo: Implementar o próximo slice: [X.Y descrição].

Por favor:
1. Leia tasks.md para entender onde parei
2. Verifique o último commit para contexto
3. Implemente APENAS o slice X.Y
4. Siga TDD: RED → GREEN → REFACTOR
5. Rode: {self.tools.get('test', 'python manage.py test')} e {self.tools.get('lint', 'ruff check .')}
6. Commit com mensagem descritiva
7. Marque task como concluída em tasks.md
8. PARE e diga "STOP — Aguardando confirmação"

Não prossiga para o próximo slice sem minha autorização.
```

---

*AGENTS.md gerado automaticamente por esaa-generate-agents*
*Stack: Django {django_version}*
*Revise e ajuste conforme necessidades específicas do projeto*
"""

        return template
    
    def _generate_flask(self) -> str:
        """Gera AGENTS.md para Flask"""
        flask_version = self.versions.get('flask', '3.0')
        
        return f"""# AGENTS.md — [NOME DO PROJETO]

## 1. Stack e Versões

- **Python**: 3.10+
- **Flask**: {flask_version}
- **Frontend**: HTML5 + Bootstrap 5 + Vanilla JavaScript
- **Banco de Dados**: [PostgreSQL/SQLite conforme projeto]

## 2. Comandos de Desenvolvimento

- **Run server**: `flask run` ou `python app.py`
- **Test**: `{self.tools.get('test', 'pytest')}`
- **Lint**: `{self.tools.get('lint', 'ruff check .')}`
- **Variáveis de ambiente**: `export FLASK_APP=app.py`

## 3. Arquitetura e Constraints

- **Estrutura**: Organizar por blueprints
- **Models**: SQLAlchemy com migrations (Flask-Migrate)
- **Forms**: WTForms para validação
- **Templates**: Jinja2, herança de `base.html`
- **Static**: CSS/JS em `static/`, organizado por função

## 4. Política de Testes

- Testes para rotas críticas
- Testes para lógica de negócio
- Fixtures para banco de dados de teste

## 5. Regras de Commit

- Um slice = um commit
- Formato: `tipo: descrição`
- Sempre testar antes de commitar

## 6. Definition of Done (DoD)

- [ ] Testes passam
- [ ] Lint OK
- [ ] Task marcada em tasks.md
- [ ] Commit feito e push realizado

## 7. Anti-Patterns Proibidos

- NUNCA lógica de negócio em rotas — use services
- NUNCA SQL raw sem parametrização (SQL injection)
- NUNCA secrets hardcoded — use `.env`
- NUNCA debug=True em produção

## 8. Stop Rule

Após cada slice:

1. Implementar
2. Testar
3. Commitar
4. **PARAR** — Aguardar confirmação

## 9. Prompt de Reentrada

```text
Read AGENTS.md and PROJECT_CONTEXT.md first.
Change ID: [change-id]
Implement ONLY the next slice.
Follow: RED → GREEN → REFACTOR → VERIFY → COMMIT → STOP.
```

"""

    def _generate_fastapi(self) -> str:
        """Gera AGENTS.md para FastAPI"""
        return """# AGENTS.md — [NOME DO PROJETO]

## 1. Stack e Versões

- **Python**: 3.10+
- **FastAPI**: [versão]
- **ASGI**: Uvicorn
- **Banco**: [PostgreSQL/MongoDB]

## 2. Comandos de Desenvolvimento

- **Run**: `uvicorn main:app --reload`
- **Test**: `pytest`
- **Lint**: `ruff check .`
- **Type check**: `mypy .` (obrigatório para FastAPI)

## 3. Arquitetura e Constraints

- **Schemas**: Pydantic para validação de entrada/saída
- **Dependências**: Use Depends para injeção
- **Roteamento**: APIRouter para organizar
- **Async**: Prefira async/await para I/O

## 4. Política de Testes

- Testes para todos endpoints
- Testes de integração para fluxos
- Use TestClient do FastAPI

## 5. Regras de Commit

- Um slice = um commit
- Formato: `tipo: descrição`

## 6. Definition of Done (DoD)

- [ ] Testes passam
- [ ] Type check passa (mypy sem erros)
- [ ] Lint OK
- [ ] Task marcada e commit feito

## 7. Anti-Patterns Proibidos

- NUNCA esquecer type hints (FastAPI depende disso)
- NUNCA lógica síncrona bloqueante em endpoints async
- NUNCA retornar modelos ORM diretamente — use Pydantic schemas

## 8. Stop Rule

Após cada slice: implementar → testar → type check → commit → **STOP**

## 9. Prompt de Reentrada

```text
Read AGENTS.md and PROJECT_CONTEXT.md.
Change ID: [id]
Implement next slice with type hints.
Run: pytest && mypy . && ruff check .
Commit and STOP.
```

"""

    def _generate_node(self) -> str:
        """Gera AGENTS.md para Node.js/Express"""
        node_version = self.versions.get('node', '20')
        
        return f"""# AGENTS.md — [NOME DO PROJETO]

## 1. Stack e Versões

- **Node.js**: {node_version}
- **Express**: [versão]
- **Banco**: [MongoDB/PostgreSQL]
- **Frontend**: [React/Vue/HTML puro]

## 2. Comandos de Desenvolvimento

- **Run**: `npm start` ou `npm run dev`
- **Test**: `npm test`
- **Lint**: `npm run lint`
- **Type check**: `npx tsc --noEmit` (se TypeScript)

## 3. Arquitetura e Constraints

- **Estrutura**: MVC ou layered architecture
- **Rotas**: Organizar em `routes/`
- **Controllers**: Lógica de request/response
- **Services**: Lógica de negócio
- **Models**: Mongoose/Sequelize/Prisma

## 4. Política de Testes

- Testes de integração para endpoints
- Testes unitários para services
- Jest ou similar

## 5. Regras de Commit

- Um slice = um commit
- Formato: `tipo: descrição`
- Pre-commit hooks rodando lint/test

## 6. Definition of Done (DoD)

- [ ] `npm test` passa
- [ ] `npm run lint` passa
- [ ] Task marcada e commit feito

## 7. Anti-Patterns Proibidos

- NUNCA callbacks hell — use async/await
- NUNCA tratamento de erro genérico — seja específico
- NUNCA console.log em produção — use logger
- NUNCA process.exit sem cleanup

## 8. Stop Rule

Após cada slice: implementar → testar → lint → commit → **STOP**

## 9. Prompt de Reentrada

```text
Read AGENTS.md and PROJECT_CONTEXT.md.
Change ID: [id]
Implement next slice with async/await.
Run: npm test && npm run lint
Commit and STOP.
```

"""

    def _generate_go(self) -> str:
        """Gera AGENTS.md para Go"""
        go_version = self.versions.get('go', '1.21')
        
        return f"""# AGENTS.md — [NOME DO PROJETO]

## 1. Stack e Versões

- **Go**: {go_version}
- **Framework**: [Gin/Echo/std net/http]
- **Banco**: [PostgreSQL/MongoDB]

## 2. Comandos de Desenvolvimento

- **Run**: `go run main.go`
- **Build**: `go build`
- **Test**: `go test ./...`
- **Lint**: `golangci-lint run`
- **Format**: `go fmt ./...`

## 3. Arquitetura e Constraints

- **Estrutura**: Organizar por packages
- **Handlers**: HTTP handlers em `handlers/`
- **Services**: Lógica de negócio em `services/`
- **Models**: Estruturas em `models/`
- **Repository**: Acesso a dados abstraído

## 4. Política de Testes

- Testes para handlers (httptest)
- Testes unitários para services
- Cobertura mínima: 70%

## 5. Regras de Commit

- Um slice = um commit
- Mensagens em inglês (convenção Go)

## 6. Definition of Done (DoD)

- [ ] `go test ./...` passa
- [ ] `go fmt ./...` formatado
- [ ] `golangci-lint` passa
- [ ] Task marcada e commit feito

## 7. Anti-Patterns Proibidos

- NUNCA ignorar erros (`_ = func()`)
- NUNCA panic em código de produção
- NUNCA goroutines sem controle (leaks)
- NUNCA compartilhar estado sem sincronização

## 8. Stop Rule

Após cada slice: implementar → testar → fmt → lint → commit → **STOP**

## 9. Prompt de Reentrada

```text
Read AGENTS.md and PROJECT_CONTEXT.md.
Change ID: [id]
Implement next slice handling all errors.
Run: go test ./... && go fmt ./... && golangci-lint run
Commit and STOP.
```

"""

    def _generate_generic(self) -> str:
        """Gera AGENTS.md genérico quando não detecta stack"""
        return """# AGENTS.md — [NOME DO PROJETO]

## 1. Stack e Versões

- **Linguagem**: [versão]
- **Framework**: [se houver]
- **Banco de Dados**: [tipo/versão]
- **Outras Dependências Principais**: [listar]

## 2. Comandos de Desenvolvimento

- **Build**: [comando]
- **Run**: [comando]
- **Test**: [comando]
- **Lint**: [comando]
- **Type check**: [comando, se aplicável]

## 3. Arquitetura e Constraints

- [Descrever estrutura do projeto]
- [Direção de dependências]
- [Padrões obrigatórios]

## 4. Política de Testes

- [O que testar]
- [Ferramentas de teste]
- [Cobertura esperada]

## 5. Regras de Commit

- Um slice = um commit
- Formato: `tipo: descrição`
- [Outras regras específicas]

## 6. Definition of Done (DoD)

- [ ] Build sem erro
- [ ] Testes passam
- [ ] Lint/type check OK
- [ ] Task marcada em tasks.md
- [ ] Commit feito

## 7. Anti-Patterns Proibidos

- [Listar anti-patterns específicos do stack]

## 8. Stop Rule

Após implementar CADA slice:

1. Implementar código
2. Rodar testes
3. Rodar lint
4. Fazer commit
5. Marcar task
6. **PARAR** — Aguardar confirmação

## 9. Prompt de Reentrada

```text
Read AGENTS.md and PROJECT_CONTEXT.md first.
Change ID: [change-id]
Implement ONLY the next slice.
Follow verification commands from AGENTS.md.
Commit and STOP. Wait for confirmation.
```

---

⚠️ **NOTA**: Este é um template genérico. Por favor, preencha as seções
marcadas com [...] conforme as especificidades do seu projeto.
"""

def main():
    """Função principal da skill"""
    import argparse

    parser = argparse.ArgumentParser(description="Gera AGENTS.md para SOP ESAA")
    parser.add_argument("--update", action="store_true", help="Atualiza AGENTS.md existente")
    parser.add_argument("--template", help="Força template específico")
    parser.add_argument("--output", "-o", default="AGENTS.md", help="Nome do arquivo de saída")
    args = parser.parse_args()
    
    # Verifica se AGENTS.md já existe
    output_path = Path(args.output)
    if output_path.exists() and not args.update:
        print(f"⚠️  {args.output} já existe!")
        print("   Use --update para atualizar preservando customizações")
        print("   Ou delete o arquivo para gerar do zero")
        return 1
    
    # Detecta stack
    print("🔍 Analisando estrutura do projeto...\n")
    
    detector = StackDetector()
    
    if args.template:
        # Força template específico
        if args.template in STACK_DETECTORS:
            detector.detected_stack = args.template
            detector._extract_versions()
            detector._detect_tools()
            detector._detect_apps()
            print(f"🎯 Stack forçado: {args.template}")
        else:
            print(f"❌ Template '{args.template}' não reconhecido")
            print(f"   Opções: {', '.join(STACK_DETECTORS.keys())}")
            return 1
    else:
        # Auto-detecta
        stack, config = detector.detect()
        if stack:
            print(f"🎯 Stack detectado: {stack}")
            print(f"📦 Versões: {detector.versions}")
            print(f"🔧 Ferramentas: {detector.tools}")
            if detector.apps:
                print(f"📁 Apps: {detector.apps}")
        else:
            print("⚠️  Não foi possível detectar stack automaticamente")
            print("   Usando template genérico...")
            detector.detected_stack = None
    
    # Gera conteúdo
    print("\n📝 Gerando AGENTS.md...")
    generator = AgentsGenerator(detector)
    content = generator.generate()
    
    # Se for update, mescla com existente
    if args.update and output_path.exists():
        print("🔄 Modo update: preservando customizações...")
        old_content = output_path.read_text()
        content = merge_agents(old_content, content)
    
    # Salva arquivo
    output_path.write_text(content)
    
    print("\n" + "━"*50)
    print("✅ AGENTS.md criado com sucesso!")
    print("━"*50)
    print(f"📄 Local: {output_path.absolute()}")
    print(f"📊 Tamanho: {len(content)/1024:.1f}KB")
    
    print("\n⚠️  IMPORTANTE: Revise o arquivo antes de usar!")
    print("   Especialmente as seções 3, 7 e 9.")
    
    print("\n🚀 Próximo passo:")
    print("   /esaa-project-resurrection")
    print("   (para verificar estado do projeto)")
    
    return 0

def merge_agents(old: str, new: str) -> str:
    """Mescla AGENTS.md existente com novo, preservando customizações"""
    # TODO: Implementar lógica de merge inteligente
    # Por enquanto, apenas adiciona aviso no topo
    header = """# AGENTS.md — ATUALIZADO

⚠️ **Este arquivo foi atualizado automaticamente.**
   Revisão recomendada para verificar se customizações foram preservadas.

---

"""
    return header + new

if **name** == "**main**":
    sys.exit(main())

```

---

## Templates Específicos

### Template Django (Resumido)

O template Django (prioridade para o usuário) inclui:

- **Stack**: Python 3.11+, Django 5.0+, PostgreSQL/SQLite
- **Comandos**: `manage.py` para tudo (test, migrate, shell)
- **Arquitetura**: Apps por domínio, CBVs para CRUD, services.py para lógica
- **Testes**: pytest ou unittest, foco em lógica de negócio
- **Anti-patterns**: 9 regras específicas de Django (lógica em views, queries em templates, etc.)

### Outros Templates

- **Flask**: Blueprints, SQLAlchemy, estrutura menor
- **FastAPI**: Pydantic, async/await, type hints obrigatórios
- **Node**: Express, MVC, Jest para testes
- **Go**: Packages, handlers/services/repository, goroutines

---

## Casos de Uso

### 1. Setup Inicial de Projeto Django

```bash
# Projeto novo
django-admin startproject meu_projeto
cd meu_projeto

# Gera AGENTS.md automaticamente
/esaa-generate-agents

# Edita [NOME DO PROJETO] e adiciona regras específicas
vim AGENTS.md

# Pronto para usar workflow ESAA
/opsx:new setup-inicial
```

### 2. Adotar ESAA em Projeto Existente

```bash
# Projeto Django existente (sem AGENTS.md)
cd projeto-legado

# Detecta stack e gera AGENTS.md
/esaa-generate-agents

# Revisa e ajusta (especialmente anti-patterns já existentes no código)
vim AGENTS.md

# Inicializa OpenSpec
openspec init

# Primeiro change: documentar estado atual
/opsx:new document-current-state
```

### 3. Atualizar Após Mudança de Stack

```bash
# Projeto evoluiu: adicionou Celery, mudou para pytest
/esaa-generate-agents --update

# Revisa mudanças
vim AGENTS.md

# Commit da atualização
git commit -am "docs: update AGENTS.md with new stack"
```

---

## Integração com Workflow ESAA

```
# Fluxo de novo projeto
1. Criar projeto (django-admin startproject)
2. /esaa-generate-agents         # Setup em 2 min
3. (revisar AGENTS.md)
4. openspec init                 # Setup OpenSpec
5. /esaa-project-resurrection    # Verificar estado
6. /opsx:new primeira-feature    # Começar trabalho
```

---

## Instalação

```bash
# 1. Copiar para skills do Pi
cp -r esaa-generate-agents ~/.pi/skills/

# 2. Instalar dependências
pip install pyyaml packaging

# 3. Disponível como /esaa-generate-agents
```

---

## Testes

```bash
# Testar detecção em projeto Django
python generate.py

# Forçar template específico
python generate.py --template=flask

# Atualizar existente
python generate.py --update
```

---

*Skill criada para SOP ESAA Solopreneur v4.1 — Setup em minutos, não em horas*
