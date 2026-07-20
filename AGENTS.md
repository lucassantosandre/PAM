# AGENTS.md — O Voto Final (PAM)

Repositório do projeto literário **PAM** — romance distópico híbrido narrado em segunda
pessoa, com tese acadêmica embutida. Leia este arquivo antes de qualquer tarefa.

---

## O que é este projeto

- **Gênero**: Romance distópico literário com fundamentação acadêmica
- **Título**: O Voto Final
- **Narrador**: Segunda pessoa ("Você") — invariável no arco principal
- **Tema**: Apostas esportivas como instrumento de aceleração de entropia social;
  sistema de votação global controlado por derivativos entropy-linked

---

## Estrutura do repositório

```
PAM/
  AGENTS.md                        ← este arquivo
  .github/
    copilot-instructions.md        ← regras de edição para VS Code
    agents/caliope.agent.md        ← agente Calíope (VS Code)
    skills/                        ← handoff, roteiro, templates, estilo, fonte-primaria
    instructions/pam-escrita.instructions.md
  PAM/
    HISTORIA.md                    ← ARQUIVO CENTRAL — romance completo
    ENTROPIA.md                    ← fundamentação física (entropia, Prigogine)
    CALCULO-MARXISTA.md            ← fundamentação econômica (Marx, Harvey)
    METODO.md                      ← fundamento metodológico (Toulmin, Popper)
    TESE.md                        ← tese acadêmica embutida
  handoffs/lucassantos/            ← handoffs de sessão
  memory/                          ← perfis de estilo e lições
```

**Arquivo central**: `PAM/PAM/HISTORIA.md` — todo conteúdo narrativo vive aqui.
Nunca criar capítulos em arquivos separados.

---

## Regras obrigatórias para qualquer agente

### Narrativa

- Capítulos numerados em **romano** (I, II … XXVII). Inline: "Cap. XII", nunca "Cap. 12"
- Aprofundamentos em **decimal** (2.1, 5.1, 18.1)
- Aprofundamentos têm tipo obrigatório: `📍` (gancho) ou `🔎` (paralelo puro)
- Narrador principal em **segunda pessoa** — nunca quebrar para terceira ou primeira
- O **nome do irmão** aparece somente no Cap. XIV — em todo o resto: "o irmão"

### Fontes

- **Nunca inventar ou completar dados bibliográficos** — reportar gaps ao escritor
- Fontes primárias registradas em ENTROPIA.md, CALCULO-MARXISTA.md, METODO.md e HISTORIA.md §FUNDAMENTAÇÃO

### Estrutura de seções em HISTORIA.md

- `## PERSONAGENS` — tabela de personagens
- `## PERGUNTAS FREQUENTES` — FAQ do lore
- `## A HISTÓRIA` → `### PARTE {ROMANO}` → `#### Capítulo {ROMANO} — {TÍTULO}`
- `## APROFUNDAMENTOS` → `### Expansões do Capítulo {ROMANO}` → `#### {decimal} — {TÍTULO} {📍/🔎}`
- `## FUNDAMENTAÇÃO` — base teórica com fontes primárias

### Emojis

- **Zero emojis** no texto corrido de narração ou diálogo
- Emoji-marca de personagem: só no **primeiro aparecimento de peso** da cena
- Emojis de notificação: somente dentro de blocos `> citação` (telas de celular/app)

### Fórmulas

- Inline: `$formula$` (KaTeX)
- Bloco: `$$formula$$`

---

## Personagens existentes — emojis reservados

| Emoji | Personagem         |
| ----- | ------------------ |
| 🩶    | Você (narrador)    |
| 🕯️    | O irmão            |
| 🖤    | A mãe              |
| ⛏️    | O coveiro          |
| 🚬    | A senhora de preto |
| 💼    | O trader           |
| 🧹    | O faxineiro        |
| 🤍    | A mulher da Casa   |
| 🏛️    | A Casa             |
| 🎲    | ADI Predictstreet  |
| ⚙️    | Executor #2081-C   |

Ao adicionar personagem novo: escolher emoji **não listado acima**.

---

## Convenção de branches e versionamento

| Tipo           | Prefixo de branch        | Bump                  |
| -------------- | ------------------------ | --------------------- |
| Nova Parte     | `parte/{romano}-{slug}`  | major (v1→v2)         |
| Novo Capítulo  | `cap/{romano}-{slug}`    | minor (v0.1→v0.2)     |
| Aprofundamento | `aprof/{decimal}-{slug}` | patch (v0.0.1→v0.0.2) |
| Infra / Skills | `chore/{slug}`           | patch                 |
| Correção       | `fix/{slug}`             | patch                 |

Exemplos: `cap/XIV-o-nome`, `aprof/5-4-o-portfolio`, `parte/IX-o-limiar`

O merge de qualquer PR em `main` dispara `.github/workflows/release.yml` que cria
a tag semântica (`vX.Y.Z`) e a Release automaticamente.

---

## O que o agente pode fazer

- Ler qualquer arquivo do repositório para contexto
- Propor novos aprofundamentos seguindo os templates em `.github/skills/templates/`
- Verificar consistência de numeração romana e emojis
- Sugerir fontes a registrar (nunca registrar sem confirmação do escritor)
- Criar handoff em `handoffs/lucassantos/`
- Rodar skill `git-commit` para commit + push + orientar abertura de PR
- Rodar skill `metodo` para validar argumentos com Toulmin/Popper antes de commitar
- Rodar skill `grill` para interrogação socrática de ideias narrativas e acadêmicas
- Rodar skill `grill` **antes de qualquer arco novo** que faça afirmações sobre o mundo real

## O que o agente NÃO pode fazer

- Criar arquivos de capítulo separados de HISTORIA.md
- Inventar ou completar citações bibliográficas
- Alterar o FAQ sem instrução explícita
- Revelar o nome do irmão fora do Cap. XIV
- Modificar CALCULO-MARXISTA.md, METODO.md ou TESE.md sem instrução explícita
  (são documentos do escritor)

---

## Skills disponíveis

| Skill            | Quando usar                                         |
| ---------------- | --------------------------------------------------- |
| `roteiro`        | Novo capítulo ou aprofundamento narrativo           |
| `templates`      | Consultar ou criar template de cap/aprof/personagem |
| `estilo`         | Calibrar DNA de escrita do escritor                 |
| `fonte-primaria` | Verificar ou registrar citação bibliográfica        |
| `handoff`        | Compactar sessão para retomada futura               |
| `git-commit`     | Gerar branch + commit + PR padronizados             |
| `metodo`         | Validar argumento com Toulmin + Popper              |
| `grill`          | Interrogação socrática de ideias antes de commitar  |

## Arquivos referenciados mas ainda não criados

| Arquivo                        | Status                                            |
| ------------------------------ | ------------------------------------------------- |
| `PAM/ARCO-FINAL.md`            | ✅ Criado — arco das máfias adicionado (setor IX) |
| `PAM/investigacoes/ADI/ADI.md` | ✅ Criado — dossier corporativo                   |
