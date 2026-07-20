---
name: git-commit
description: >
  Encapsula o ciclo completo de versionamento do projeto PAM — após finalizar escrita
  ou atualizações no chat: cria a branch com nomenclatura correta, commita, faz push
  e orienta a abertura do PR para main (que dispara o workflow de release automático).
argument-hint: "Tipo e referência do conteúdo finalizado. Ex: 'cap XIV', 'aprof 5.4', 'parte IX', 'infra: skills'"
---

# Git Commit

Ciclo completo de commit, push e abertura de PR após finalização de escrita ou estrutura.
O merge do PR em `main` dispara o workflow `.github/workflows/release.yml` que cria a
tag e a Release automaticamente.

# Convenção de branches e versionamento

| Tipo de conteúdo | Prefixo de branch | Bump de versão |
|---|---|---|
| Nova Parte (I, II…) | `parte/{romano}-{slug}` | **major** (v1→v2) |
| Novo Capítulo | `cap/{romano}-{slug}` | **minor** (v0.1→v0.2) |
| Aprofundamento | `aprof/{decimal}-{slug}` | **patch** (v0.0.1→v0.0.2) |
| Infraestrutura / Skills / Agents | `chore/{slug}` | **patch** |
| Correção | `fix/{slug}` | **patch** |

Exemplos de branches válidas:
- `cap/XIV-o-nome` → Capítulo XIV — bump minor
- `aprof/5-4-o-portfolio` → Aprofundamento 5.4 — bump patch
- `parte/IX-o-limiar` → Parte IX — bump major
- `chore/skill-git-commit` → infra — bump patch

# Inputs

| Campo | Descrição |
|---|---|
| `tipo` | `cap`, `aprof`, `parte`, `chore`, `fix` |
| `referencia` | Número romano/decimal ou slug (ex: `XIV`, `5.4`, `IX`) |
| `slug` | 2–4 palavras kebab-case do conteúdo (ex: `o-nome`, `o-portfolio`) |
| `mensagem` | Descrição do commit (padrão: gerada automaticamente) |

# Workflow

1. **Verificar estado** — `git status` para confirmar o que está pendente.
2. **Nomear a branch**:
   ```
   {tipo}/{referencia}-{slug}
   ```
   Exemplos: `cap/XIV-o-nome`, `aprof/5-4-o-portfolio`
3. **Criar e mudar para a branch** (se ainda não existir):
   ```bash
   git checkout -b {branch} 2>/dev/null || git checkout {branch}
   ```
4. **Stage de todos os arquivos modificados**:
   ```bash
   git add -A
   ```
5. **Commit com mensagem padronizada**:
   ```bash
   git commit -m "{tipo}({referencia}): {mensagem}"
   ```
   Exemplos:
   - `cap(XIV): O nome do irmão — primeira revelação`
   - `aprof(5.4): Portfólio — a credora passiva acorda`
   - `chore(skills): add git-commit skill and release workflow`
6. **Push**:
   ```bash
   git push origin {branch}
   ```
7. **Orientar abertura do PR**:
   - Título sugerido: `{Tipo} {referencia} — {título do conteúdo}`
   - Body sugerido: resumo do que foi escrito/alterado nesta sessão
   - Base: `main`
   - Link direto: `https://github.com/lucassantosandre/PAM/pull/new/{branch}`

# O que acontece ao mergar o PR

O workflow `release.yml` dispara automaticamente e:
- Detecta o prefixo da branch → define o bump (major/minor/patch)
- Calcula a próxima versão semântica a partir da última tag
- Cria a tag `vX.Y.Z` no GitHub
- Cria uma Release com título, branch, número do PR e body do PR

# Regras

- Nunca commitar diretamente em `main` — sempre via PR
- Branch nomeada antes do primeiro commit da sessão
- Um PR por sessão de escrita (ou por capítulo/aprofundamento, se preferir granularidade)
- O slug da branch vem do conteúdo principal — não da data ou do autor
- Commits em inglês técnico; mensagem do PR em português (é o que aparece na Release)
