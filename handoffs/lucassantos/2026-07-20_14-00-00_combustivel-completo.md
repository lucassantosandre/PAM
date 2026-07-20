# Handoff — 2026-07-20 — combustível-completo

> **Para Calíope (nova sessão):** Este é o documento de contexto máximo do projeto PAM.
> Lê este arquivo inteiro antes de qualquer geração. Depois lê `memory/lucassantos/perfil.md`
> para o DNA de escrita do autor. Com os dois, você tem combustível suficiente para continuar
> qualquer linha do projeto sem quebrar continuidade.

---

## 1. O que é este projeto — em três frases

**"O Voto Final"** é um romance distópico narrado em segunda pessoa ("Você"), voz da
classe trabalhadora, onde apostas esportivas evoluem até uma votação global que decide
o fim do mundo. A ficção demonstra uma tese acadêmica embutida: *o Estado capitalista não
proíbe o vício por princípio, mas o administra por cálculo fiscal*. Os dois textos
(romance + tese) coexistem no mesmo repositório — cada um tornando o outro mais difícil
de rejeitar.

---

## 2. Arquitetura dos três textos

```
HISTORIA.md           → demonstra  (emoção, segunda pessoa, classe trabalhadora)
DEMONSTRACAO.md       → conecta    (mapeia cenas → mecanismos → provas)
TESE.md               → argumenta  (Toulmin, Popper, fórmulas, objeções)
```

Os três textos são complementares, nunca redundantes. A mesma verdade em três modos de
acesso. Nunca misturar: explicações acadêmicas não entram em HISTORIA.md; emoção bruta
não entra em TESE.md sem tradução formal.

**Arquivos de fundamento:**

| Arquivo | Função |
|---|---|
| [PAM/HISTORIA.md](../PAM/HISTORIA.md) | Arquivo central — todo conteúdo narrativo vive aqui |
| [PAM/TESE.md](../PAM/TESE.md) | Tese acadêmica standalone |
| [PAM/DEMONSTRACAO.md](../PAM/DEMONSTRACAO.md) | Bridge explícita ficção↔teoria — 6 pontos mapeados |
| [PAM/ENTROPIA.md](../PAM/ENTROPIA.md) | Fundação física (Prigogine, termodinâmica, analogias) |
| [PAM/CALCULO-MARXISTA.md](../PAM/CALCULO-MARXISTA.md) | Fundação econômica (mais-valia, $E = s + \theta\alpha v$) |
| [PAM/METODO.md](../PAM/METODO.md) | Fundação metodológica (Toulmin, Popper) |
| [PAM/ARCO-FINAL.md](../PAM/ARCO-FINAL.md) | Spoiler privado — arco Caps. XVII–XXVII |
| [PAM/investigacoes/MAP/MAP.md](../PAM/investigacoes/MAP/MAP.md) | Dossier factual mercados de previsão |
| [PAM/investigacoes/PAM/PAM.md](../PAM/investigacoes/PAM/PAM.md) | Policy Analysis Market |
| [PAM/investigacoes/ADI/ADI.md](../PAM/investigacoes/ADI/ADI.md) | Dossier ADI Predictstreet (ficção) |

---

## 3. Estado narrativo atual

### Progresso

- **Caps. I–XVI completos** (Partes I–V)
- Narrador: Você 🩶 — INVARIÁVEL, nunca quebrar para primeira ou terceira pessoa
- **Nome do irmão**: ainda não revelado — só aparece no Cap. XIV (regra inviolável)

### Aprofundamentos existentes

| # | Título | Tipo | Cap. âncora |
|---|---|---|---|
| 2.1–2.5 | Expansões Cap. II | 🔎📍 | II |
| 4.1 | A Precificação | 🔎 | IV |
| 5.1 | A Liquidação | 📍 | V |
| 5.2 | O Executor | 📍 | V |
| 5.3 | Portfólio | 🔎 | V |
| 15.1 | Do outro lado | 📍 | XV |
| 15.2 | _(existente)_ | 📍 | XV |

### Próximo capítulo planejado

**Cap. XVII — "O Prédio por Dentro"** (Parte VI)
Ver ARCO-FINAL.md PARTE IX para a estrutura da máfia que controla contratos da ADI.
**Obrigatório antes de escrever:** rodar skill `grill` + `metodo` na premissa
*"máfias controlam os contratos do balcão silencioso da ADI"*.

### Aprofundamentos planejados

| # | Título | Tipo | Status |
|---|---|---|---|
| 15.3 | "O Risco Que Não Coube" | 🔎 | planejado — trader 💼, modelo quebra |
| 17.1 | _(operador anônimo — posição #4471-B)_ | 🔎 | estruturado em ARCO-FINAL.md |
| 20.50 | _(trader descobre contrapartes-máfia)_ | 📍 | estruturado em ARCO-FINAL.md |

---

## 4. Personagens — referência rápida

| Emoji | Personagem | Status |
|---|---|---|
| 🩶 | Você (narrador) | ativo |
| 🕯️ | O irmão | morto desde Cap. V — aparece em flashback |
| 🖤 | A mãe | presente |
| ⛏️ | O coveiro | testemunha lúcida |
| 🚬 | A senhora de preto | misteriosa |
| 💼 | O trader | dilema moral Cap. XV → Cap. XX |
| 🧹 | O faxineiro | resistência silenciosa |
| 🤍 | A mulher da Casa | interna ao sistema |
| 🏛️ | A Casa | instituição opaca |
| 🎲 | ADI Predictstreet | sistema de apostas (ficção) |
| ⚙️ | Executor #2081-C | braço do sistema |

**Regra de emoji:** aparece SOMENTE no primeiro aparecimento de peso da cena. Nunca a cada menção.

---

## 5. Regras narrativas invioláveis

1. **Segunda pessoa:** narrador é SEMPRE "Você" — nunca quebrar
2. **Nome do irmão:** somente no Cap. XIV — nunca antes, nunca fora
3. **Emojis de notificação** (🌍 💀 ⚖️ ⛏️ 🔴 🩸 ⚽): só em blocos `> citação` (telas de celular)
4. **Anotações acadêmicas:** FORA da narração. Ficção mostra; teoria explica em outro arquivo
5. **Fontes:** nunca inventar. Só via skill `fonte-primaria`
6. **Capítulos:** numerados em romano (I–XXVII). Aprofundamentos em decimal (2.1, 15.3)
7. **Grill obrigatório** antes de qualquer arco com afirmação sobre o mundo real (máfias, economia, física)
8. **Arquivo único:** HISTORIA.md — nunca fragmentar conteúdo narrativo

---

## 6. O que foi feito nesta sessão (2026-07-20)

| Arquivo | O que mudou |
|---|---|
| HISTORIA.md | 5 intrusões acadêmicas removidas dos caps.; links cruzados adicionados |
| TESE.md | 4 epígrafes + "Nota de linguagem" (tradição Marx); 3 correções de tom |
| ENTROPIA.md | Glossário corrigido (entropia ≠ desordem); disclaimers de analogia |
| ENTROPIA-expandido.md | Expansão massiva: sistema aberto/fechado, capitalismo + entropia, dados EUA 2024, FAQ 7 perguntas, diagramas Mermaid |
| ARCO-FINAL.md | PARTE IX (arco máfia): warrant Toulmin + Aprof. 17.1 + 20.50 + timeline |
| DEMONSTRACAO.md | **NOVO** — bridge explícita ficção↔teoria, 6 pontos, diagrama arquitetura |
| .github/skills/metodo/ | **NOVO** — skill Toulmin + Popper |
| .github/skills/grill/ | **NOVO** — skill interrogatório socrático |
| tests/test_calculos_economicos.py | **NOVO** — 14 testes das fórmulas-chave |
| AGENTS.md + copilot-instructions.md | Skills atualizadas; regra #9 (grill antes de arco) |
| MAP.md, PAM.md, ADI.md, REFERENCIAS.md, READMEs | Links cruzados substituindo backticks |

**Status git:** tudo local, nenhum commit nesta sessão.
Branch sugerida: `chore/session-refactor`

---

## 7. Tese central — para qualquer geração

> **O Estado capitalista contemporâneo não proíbe o vício por princípio, mas o
> administra por cálculo fiscal.**
>
> Ele proíbe enquanto não consegue tributar, e legaliza quando a arrecadação supera o
> custo político da proibição — convertendo o consumo de risco das classes trabalhadoras
> em fonte simultânea de lucro privado e receita pública.

**Fórmulas-chave:**
- Taxa de exploração: $s' = s/v$
- Captura fiscal no consumo: $R = t \cdot \theta \cdot H$
- Extração total do trabalhador: $E = s + \theta\alpha v$

---

## 8. Próximas ações — por prioridade

| # | Ação | Skill | Branch |
|---|---|---|---|
| 1 | Commitar tudo desta sessão | `git-commit` | `chore/session-refactor` |
| 2 | Grill da premissa do arco máfia | `grill` + `metodo` | — |
| 3 | Aprofundamento 15.3 "O Risco Que Não Coube" | `roteiro` modo `aprofundamento` | `aprof/15-3-o-risco-que-nao-coube` |
| 4 | Capítulo XVII "O Prédio por Dentro" | `roteiro` modo `capitulo` | `cap/XVII-o-predio-por-dentro` |
| 5 | Calibrar perfil de estilo do escritor | `perfil-escritor` (nova skill) | — |
| 6 | Verificar [PRECISA VERIFICAR] em REFERENCIAS.md | `fonte-primaria` | — |
| 7 | Adicionar dados Brasil 2024–2026 em investigacoes/economia/ | `fonte-primaria` | — |

---

## 9. Skills disponíveis — referência rápida

| Skill | Quando usar |
|---|---|
| `roteiro` | Novo capítulo ou aprofundamento |
| `templates` | Consultar ou criar template |
| `estilo` | Calibrar DNA mecânico de escrita (frases, parágrafos, diálogos) |
| `perfil-escritor` | Mapear perfil estratégico (influências, leitor, crescimento) |
| `fonte-primaria` | Verificar ou registrar citação bibliográfica |
| `handoff` | Compactar sessão para retomada futura |
| `git-commit` | Branch + commit + PR padronizados |
| `metodo` | Validar argumento com Toulmin + Popper |
| `grill` | Interrogação socrática antes de commitar ideia |

---

## 10. Arquitetura de conhecimento — o que está provado

| Camada | Status |
|---|---|
| Física (ENTROPIA.md) | Fundada — analogias com disclaimers explícitos |
| Econômica (CALCULO-MARXISTA.md) | Fundada — fórmulas com base em Marx/Harvey |
| Metodológica (METODO.md) | Fundada — Toulmin + Popper |
| Evidência empírica (investigacoes/) | Parcial — EUA 2024 OK; Brasil pendente |
| Ficção (HISTORIA.md) | Caps I–XVI completos |
| Tese (TESE.md) | Rascunho avançado — precisa revisão final |
| Bridge (DEMONSTRACAO.md) | Criada — 6 pontos mapeados |

---

## 11. Ponto de retomada narrativa

O Cap. XVI termina com o sinal chegando:
> "Foi aí que chegou o sinal."

A próxima cena (início do Cap. XVII) é a entrada de Você no prédio da ADI —
o confronto físico com a estrutura que administrou a morte do irmão.
Antes de escrever: grill da premissa das máfias (ARCO-FINAL.md PARTE IX).
