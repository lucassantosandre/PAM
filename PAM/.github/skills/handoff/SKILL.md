---
name: handoff
description: >
  Compacta a sessão atual em um documento de handoff para o escritor retomar o trabalho
  num novo chat ou numa sessão futura sem precisar reler toda a conversa.
argument-hint: "Qual será o foco da próxima sessão? (ex: 'criar ARCO-FINAL.md', 'novo aprofundamento 27.1')"
---

# Handoff

Comprime o estado atual da sessão em um documento conciso e acionável — para retomar
o trabalho sem contexto de conversa anterior.

# Inputs

| Argumento            | Descrição                                                                          |
| -------------------- | ---------------------------------------------------------------------------------- |
| `focus` _(opcional)_ | Descrição curta do que a próxima sessão vai focar                                  |
| _(contexto no chat)_ | Estado atual, decisões tomadas, arquivos editados, ganchos abertos, próximas ações |

# Workflow

1. Identificar o objetivo da próxima sessão — do argumento ou da solicitação.
2. Resolver o usuário via `whoami` no terminal. Usar como subpasta `{user}`.
3. Resumir o que foi concluído, o que está em aberto e quais decisões estão ativas.
4. Registrar arquivos-chave, seções editadas e decisões críticas.
5. Preferir referências a artefatos existentes em vez de reescrever conteúdo.
6. Obter timestamp via `date +%Y-%m-%d_%H-%M-%S`.
7. Derivar slug kebab-case do tópico principal (ex: `aprofundamento-5x`, `arco-final`).
8. Salvar em `handoffs/{user}/{timestamp}_{slug}.md` (criar subpasta se não existir).

# Estrutura do documento

```markdown
# Handoff — {data} — {slug}

## Objetivo da próxima sessão

{focus ou objetivo inferido do chat}

## Estado atual da história

- Partes concluídas: I–VIII (Cap. I–XXVII + FIM)
- Aprofundamentos ativos: {lista com 📍/🔎 e números}
- Arquivo principal: PAM/PAM/HISTORIA.md
- Último conteúdo gerado: {tipo e título}

## Decisões narrativas ativas

{lista de decisões de estrutura ou lore que estão em vigor}

## Arquivos-chave

| Arquivo                     | Estado                                           |
| --------------------------- | ------------------------------------------------ |
| PAM/PAM/HISTORIA.md         | {resumo do estado — último cap, aprofundamentos} |
| PAM/PAM/ENTROPIA.md         | {intacto / editado em {data}}                    |
| PAM/PAM/TESE.md             | {intacto / editado em {data}}                    |
| PAM/PAM/CALCULO-MARXISTA.md | {intacto / editado em {data}}                    |

## Arquivos referenciados mas não criados

{lista de ARCO-FINAL.md, ADI.md, etc. com o que se sabe sobre cada um}

## Ganchos em aberto (📍)

{lista de 📍 plantados que ainda não foram puxados na narrativa principal}

## FAQ ativo

{resumo das perguntas/respostas do FAQ se houve mudança}

## Próximas ações sugeridas (ordenadas por prioridade)

1. {ação}
2. {ação}

## Skills sugeridas para a próxima sessão

{apenas quando genuinamente relevantes}
```
