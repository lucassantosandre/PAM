# Handoff — 2026-07-20 — estrutura-agente-caliope

## Objetivo da próxima sessão

Continuar o desenvolvimento do projeto PAM — retomar criação de conteúdo narrativo
(ARCO-FINAL.md, ADI.md, novos aprofundamentos) ou evoluir a estrutura de agentes/skills
conforme necessidade do escritor.

---

## Estado atual da história

- **Título**: O Voto Final
- **Estrutura**: Partes I–VIII completas — Capítulos I–XXVII + FIM
- **Narrador**: Segunda pessoa ("Você")
- **Arquivo principal**: `PAM/PAM/HISTORIA.md`
- **Aprofundamentos ativos**:

| Número | Título | Tipo | Cap. âncora |
|---|---|---|---|
| 2.1 | *(expansão cap. II)* | 🔎 | II |
| 2.2 | *(expansão cap. II)* | 📍 | II |
| 2.3 | *(expansão cap. II)* | 🔎 | II |
| 2.4 | *(expansão cap. II — O irmão)* | 📍 | II |
| 2.5 | *(expansão cap. II)* | 🔎 | II |
| 4.1 | A Precificação | 🔎 | IV |
| 5.1 | A Liquidação | 📍 | V |
| 5.2 | O Executor | 📍 | V |
| 5.3 | Portfólio | 🔎 | V |
| 15.1 | Do outro lado | 📍 | XV |
| 18.1 | O Registro | 🔎 | XVIII |
| 23.1 | *(filha do coveiro)* | 📍 | — Parte VIII |
| 25.1 | *(servidor 4h17)* | 🔎 | — Parte VIII |

---

## Personagens (tabela HISTORIA.md)

| Emoji | Nome/Código | Primeira aparição |
|---|---|---|
| 🩶 | Você (narrador) | Cap. I |
| 🕯️ | O irmão | Aprof. 2.4; Cap. V |
| 🖤 | A mãe | Cap. V, XI |
| ⛏️ | O coveiro | Cap. IX → |
| 🚬 | A senhora de preto | Cap. VIII |
| 💼 | O trader | Aprof. 15.1 |
| 🧹 | O faxineiro | Cap. XX |
| 🤍 | A mulher da Casa | Cap. XVIII |
| 🏛️ | A Casa | Cap. XVIII → |
| 🎲 | ADI Predictstreet | Cap. I → |
| ⚙️ | Executor #2081-C | Aprof. 5.2 |

**Regra crítica**: o nome próprio do irmão aparece **somente no Cap. XIV**. Em todo o resto: "o irmão".

---

## Decisões narrativas ativas

- **Arquivo único**: HISTORIA.md é o único arquivo de narrativa. Nunca criar capítulos separados.
- **Numeração romana**: todos os capítulos em romano (I…XXVII). Inline: "Cap. XII", nunca "Cap. 12".
- **Estrutura de seções**: H3 para Partes, H4 para Capítulos, H4 para Aprofundamentos individuais.
- **Segunda pessoa**: narrador principal invariavelmente em segunda pessoa. Aprofundamentos de outros POVs podem usar terceira.
- **Emojis**: zero no texto corrido. Emoji-marca de personagem só no primeiro aparecimento de peso da cena. Emojis de notificação só dentro de blocos `> citação`.
- **Metáforas**: financeiras (spread, liquidação, portfólio), físicas (entropia, temperatura) e cotidianas — integradas, nunca explicadas.
- **FAQ**: seção `## PERGUNTAS FREQUENTES` entre PERSONAGENS e A HISTÓRIA responde a 3 perguntas estruturais do lore (por que apostar; por que existe o limiar; por que expor não muda nada).
- **Limiar ENTROPIA**: o protocolo de saída da Casa só abre quando SIM global > ~30%. As apostas são mecanismo de aceleração da entropia. Os derivativos são entropy-linked e não liquidam antes.

---

## Arquivos-chave

| Arquivo | Estado |
|---|---|
| `PAM/PAM/HISTORIA.md` | ✅ Completo — Caps. I–XXVII + FIM + FAQ + 13 aprofundamentos + FUNDAMENTAÇÃO |
| `PAM/PAM/ENTROPIA.md` | ✅ Criado nesta sessão — 9 seções + 9 fontes primárias (Clausius…Prigogine) |
| `PAM/PAM/TESE.md` | Estado incerto — editado pelo usuário entre sessões |
| `PAM/PAM/CALCULO-MARXISTA.md` | Intacto (escrito pelo usuário) |
| `PAM/PAM/METODO.md` | Intacto (escrito pelo usuário) |

---

## Arquivos referenciados mas não criados

| Arquivo | O que se sabe |
|---|---|
| `PAM/PAM/ARCO-FINAL.md` | "Spoiler cofre" — identidade completa da Casa, plano de saída, eventos concretos do arco ENTROPIA, o que "já compramos o depois" significa. Referenciado em PERSONAGENS e CALCULO-MARXISTA.md. **Alta prioridade.** |
| `PAM/PAM/ADI.md` | Dossier da ADI Predictstreet. Referenciado em PERSONAGENS ("Empresa real") e CALCULO-MARXISTA.md ("a ADI em Gibraltar"). |
| `PAM/PAM/EPSTEIN.md` | Criado em sessão anterior, não encontrado na pasta na sessão atual. |

---

## Estrutura do agente Calíope (criada nesta sessão)

```
PAM/
  .github/
    copilot-instructions.md              ✅ 8 regras críticas do projeto
    agents/
      caliope.agent.md                   ✅ musa orquestradora — entry point
    skills/
      handoff/SKILL.md                   ✅ comprime sessão → handoffs/
      roteiro/SKILL.md                   ✅ modos: capitulo e aprofundamento
      templates/
        SKILL.md                         ✅ biblioteca + workflow de evolução
        capitulo.md                      ✅ template + 2 variantes comentadas
        aprofundamento.md                ✅ template + 2 variantes comentadas
        personagem.md                    ✅ tabela + descrição + checklist
      estilo/SKILL.md                    ✅ análise de DNA + perfil YAML
      fonte-primaria/SKILL.md            ✅ mapa interno + Chicago + regra de ouro
    instructions/
      pam-escrita.instructions.md        ✅ applyTo: PAM/PAM/**/*.md
  handoffs/                              ✅ criado
  memory/                                ✅ criado
```

### Lógica do agente

**Calíope** (musa da poesia épica grega) é o ponto único de entrada para todo trabalho criativo.
Detecta a intenção e ativa a skill correta via callout obrigatório:

| Intenção | Skill |
|---|---|
| Novo capítulo | `roteiro` modo `capitulo` |
| Aprofundamento (📍/🔎) | `roteiro` modo `aprofundamento` |
| Template | `templates` |
| Fonte a citar/verificar | `fonte-primaria` |
| Análise de estilo | `estilo` |
| Handoff de sessão | `handoff` |

Callout padrão antes de cada ação:
- `🎭✨ ativando skill {nome}`
- `🎭📖 lendo {arquivo}`
- `🎭✍️ gerando {tipo} — {título}`
- `🎭🔍 verificando {elemento}`
- `🎭📝 inserindo em {arquivo}`

### Padrão de estilo capturado (parcial — calibração completa pendente)

```yaml
voz: segunda pessoa ("Você")
tom: direto, seco, sem floreio — jornalístico-literário
abertura_de_capitulo: hora exata + ação em andamento, OU notificação de celular
fechamento_de_capitulo: frase seca, OU nota italic, OU silêncio/pergunta aberta
comprimento_de_paragrafo: 2–4 linhas típico; máximo 6
metaforas_dominantes:
  - financeiras: spread, liquidação, posição, portfólio
  - físicas: entropia, temperatura, sistema fechado
  - cotidianas: copo d'água, foto plastificada, Celta com amasso
dialogo: travessão sem aspas; fala curta; narrador não interpreta emoções
elementos_evitar:
  - adjetivos em excesso
  - explicar a metáfora depois de usá-la
  - heroísmo explícito
  - onisciência emocional
```

---

## Ganchos em aberto (📍)

| Aprof. | Gancho | Status |
|---|---|---|
| 2.2 | *(conteúdo pendente de confirmação)* | plantado |
| 2.4 | O irmão — decisão de apostar | plantado |
| 5.1 | A Liquidação — executor e 12 credores | parcialmente puxado em 5.2 |
| 5.2 | O Executor #2081-C — foto da filha no dashboard | aberto |
| 15.1 | O trader — "Emoção não move o preço" | aberto |
| 23.1 | Filha do coveiro — +0.03%/month | aberto (conecta ao arco ENTROPIA) |

---

## Fontes primárias registradas

| Arquivo | Fontes |
|---|---|
| ENTROPIA.md | Clausius (1850/1865), Boltzmann (1872), Kelvin (1851), Schrödinger (1944), Wiener (1948), Shannon (1948), Prigogine (1979/1984) |
| CALCULO-MARXISTA.md | Marx (*Das Kapital*), Harvey, Streeck |
| METODO.md | Toulmin, Popper |
| HISTORIA.md §FUNDAMENTAÇÃO | AGA, *Murphy v. NCAA*, dados cannabis Colorado, Marx, Harvey, Streeck |

---

## Próximas ações sugeridas (por prioridade)

1. **Criar `ARCO-FINAL.md`** — spoiler cofre da Casa; necessário para fechar o arco ENTROPIA
2. **Criar `ADI.md`** — dossier da empresa; referenciado em dois arquivos existentes
3. **Calibrar estilo** — rodar skill `estilo` lendo caps. I, V, IX, XVIII, XXVI, XXVII para gerar `memory/lucassantos/estilo.md`
4. **Novos aprofundamentos sugeridos**:
   - `11.x` — POV da mãe ("A culpa tem endereço")
   - `27.x` — o voto global às 8h03 — humanidade de SIM e NÃO
   - `26.x` — o dia depois da conversa com o coveiro
5. **EPSTEIN.md** — recriar se ainda relevante para o projeto

---

## Skills sugeridas para a próxima sessão

- `fonte-primaria` — ao criar ARCO-FINAL.md ou ADI.md
- `roteiro` modo `aprofundamento` — para 11.x, 27.x ou 26.x
- `estilo` — calibração completa antes do próximo capítulo longo
