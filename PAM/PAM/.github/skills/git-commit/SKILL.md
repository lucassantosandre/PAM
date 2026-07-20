---
name: git-commit
description: >
  Gera os comandos de versionamento do projeto PAM para o escritor revisar e executar —
  branch criada a partir de main atualizado, commit, push e PR abrindo de {tipo/ref-slug}
  para release-candidate. Não executa nada automaticamente.
argument-hint: "Tipo e referência do conteúdo finalizado. Ex: 'cap XIV — O Nome', 'aprof 5.4', 'parte IX', 'chore: skills'"
---

# Git Commit

Gera o roteiro completo de commit + push + PR para o escritor executar no terminal.
**Nunca executa comandos automaticamente** — apresenta tudo para revisão antes.
O merge do PR em `main` dispara `.github/workflows/release.yml` que cria tag e Release
nomeadas pelo capítulo lançado.

# Convenção de branches e versionamento

| Tipo | Prefixo de branch | Bump | Tag resultante |
|---|---|---|---|
| Nova Parte | `parte/{romano}-{slug}` | **major** (v1→v2) | `v2.0.0 — Parte IX — O Limiar` |
| Novo Capítulo | `cap/{romano}-{slug}` | **minor** (v0.1→v0.2) | `v0.2.0 — Cap. XIV — O Nome` |
| Aprofundamento | `aprof/{decimal}-{slug}` | **patch** (v0.0.1→v0.0.2) | `v0.0.2 — Aprof. 5.4 — O Portfólio` |
| Infra / Skills | `chore/{slug}` | **patch** | `v0.0.3 — chore: {slug}` |
| Correção | `fix/{slug}` | **patch** | `v0.0.4 — fix: {slug}` |

# Inputs

| Campo | Descrição |
|---|---|
| `tipo` | `cap`, `aprof`, `parte`, `chore`, `fix` |
| `referencia` | Romano/decimal (ex: `XIV`, `5.4`, `IX`) |
| `titulo` | Título do capítulo ou conteúdo (ex: `O Nome do Irmão`) |
| `slug` | 2–4 palavras kebab-case (ex: `o-nome`, `o-portfolio`) |
| `resumo` | O que foi escrito/alterado nesta sessão — vira body do PR |

# Workflow — o que a skill entrega

A skill gera um bloco de comandos prontos para copiar + o texto completo do PR.
O escritor revisa e executa no terminal.

## 1. Atualizar main local antes de criar a branch

```bash
git checkout main
git pull origin main
```

## 2. Criar branch a partir de main atualizado

```bash
git checkout -b {tipo}/{referencia}-{slug}
```

Exemplos:
- `git checkout -b cap/XIV-o-nome`
- `git checkout -b aprof/5-4-o-portfolio`
- `git checkout -b parte/IX-o-limiar`

## 3. Stage e commit

```bash
git add -A
git commit -m "{tipo}({referencia}): {titulo}"
```

Exemplos de mensagem de commit:
- `cap(XIV): O nome do irmão — primeira revelação`
- `aprof(5.4): Portfólio — a credora passiva acorda`
- `chore(infra): add release workflow and git-commit skill`

## 4. Push

```bash
git push origin {tipo}/{referencia}-{slug}
```

## 5. Abrir PR — título e body gerados pela skill

**Título do PR** (este título vira o nome da Release):
```
{Tipo humano} {referencia} — {Título completo}
```
Exemplos:
- `Cap. XIV — O Nome do Irmão`
- `Aprof. 5.4 — Portfólio: a credora passiva acorda`
- `Parte IX — O Limiar`
- `Chore — Estrutura de agentes e skills`

**Body do PR** (vira a descrição da Release):
```markdown
## O que foi escrito / alterado

{resumo do que foi feito nesta sessão}

## Arquivos modificados principais

- `PAM/HISTORIA.md` — {detalhe}
- `.github/skills/...` — {se aplicável}

## Ganchos abertos (📍) nesta entrega

- {lista de ganchos plantados, se houver}

## Conexão com a fundamentação

- {referência a ENTROPIA.md / CALCULO-MARXISTA.md / TESE.md, se aplicável}
```

**Link direto para abrir o PR** (base `release-candidate`):
```
https://github.com/lucassantosandre/PAM/compare/release-candidate...{tipo}/{referencia}-{slug}?expand=1
```

# O que acontece ao mergar o PR

O PR é aberto de `{tipo}/{referencia}-{slug}` **→ `release-candidate`** (não em `main`).
O workflow `release.yml` dispara ao mergar em `release-candidate` e:
1. Detecta o prefixo da branch → define o bump (major/minor/patch)
2. Extrai o título do PR
3. Calcula a próxima versão a partir da última tag
4. Cria a tag `vX.Y.Z` no GitHub
5. Cria a Release com nome: `vX.Y.Z — {título do PR}`
   - Ex: `v0.2.0 — Cap. XIV — O Nome do Irmão`
   - Ex: `v2.0.0 — Parte IX — O Limiar`

# Regras

- **Nunca commitar diretamente em `main` nem em `release-candidate`** — sempre via PR
- **Branch sempre criada de `main` atualizado** — `git pull origin main` antes do `checkout -b`
- **PR abre de `{tipo}/{ref}-{slug}` → `release-candidate`** (nunca → `main` diretamente)
- **Um PR por sessão** (ou por capítulo/aprofundamento se preferir granularidade)
- **Slug da branch** vem do conteúdo, não da data
- **Título do PR em português** — é o que aparece na Release
- Commits em inglês técnico; mensagem do PR em português
