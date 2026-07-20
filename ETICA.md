# Código de Ética — Autoria Assistida por IA
## Projeto PAM / "O Voto Final"

> Este documento define os princípios éticos para o uso de inteligência artificial
> no processo criativo deste repositório e serve como referência para escritores
> que utilizem esta estrutura como modelo para seus próprios projetos literários.

---

## 1. Princípios Fundamentais

### 1.1 Transparência
Todo uso de IA no processo criativo deve ser declarado — seja no prefácio da obra,
nos metadados do repositório (como este documento) ou nas notas editoriais.

### 1.2 Primado da Voz Humana
A voz narrativa, a intenção temática, as escolhas políticas e estéticas
são do autor humano. A IA é ferramenta — não autora.

### 1.3 Responsabilidade Editorial
O autor é integralmente responsável pelo conteúdo publicado, independentemente
de qual ferramenta foi utilizada na criação.

### 1.4 Integridade Criativa
IA não substitui a visão criativa, o posicionamento político-cultural
e a experiência vivida do autor. Ela amplifica — não inventa.

### 1.5 Não-substituição da Experiência
Temas como classe, trabalho, violência e pertencimento exigem
ancoragem na vivência. IA pode articular; não pode sentir.

---

## 2. Classificação de Autoria

| Nível | Nome | Estimativa de IA | Declaração obrigatória |
|---|---|---|---|
| 1 | **Humano** | < 30% | Nenhuma |
| 2 | **Assistido** | 30–60% | `"com assistência de IA"` |
| 3 | **Co-autoria** | 60–80% | `"co-autoria: [Autor] + IA"` |
| 4 | **IA Supervisionado** | > 80% | `"gerado por IA, supervisionado por [Autor]"` |
| 5 | **IA Puro** | ~100% sem revisão humana | **Não publicável como autoria humana** |

---

## 3. Este Projeto e a IA

### 3.1 Uso declarado de IA no PAM

"O Voto Final" utiliza o agente **Calíope** (GitHub Copilot + Claude Sonnet)
como ferramenta criativa assistida para:

- Geração de rascunhos de capítulos e aprofundamentos
- Verificação de consistência narrativa e numeração
- Calibração de estilo a partir de amostras do autor
- Handoffs de sessão e documentação interna

**Classificação declarada deste projeto**: Nível 2–3 (Assistido / Co-autoria)

A visão, o tema, a direção político-literária e a curadoria final
são integralmente do autor humano (Lucas Santos).

### 3.2 O que o revisor automático detectará

O revisor instalado em `.github/workflows/pr-reviewer.yml` **sinalizará** textos
gerados por Calíope como "Misto / Assistido por IA" ou "Provável Geração por IA"
em muitos PRs — isso é **esperado e correto**.

O projeto **não viola** este código de ética porque:

1. O uso de IA está **declarado** neste documento
2. A visão criativa e o posicionamento narrativo são do autor
3. Todo texto passa por **revisão e curadoria humana** antes de entrar em `release-candidate`
4. O revisor existe justamente para **monitorar e documentar** esse uso com transparência

### 3.3 O que configuraria violação deste código

- Apresentar texto gerado por IA como puramente humano, sem qualquer declaração
- Publicar conteúdo de nível 5 (IA puro, sem revisão) como autoria humana
- Usar IA para plagiar obras de outros autores ou reproduzir sem atribuição
- Remover ou contornar intencionalmente o revisor de autoria
- Usar IA para fabricar referências bibliográficas (viola também as regras de `fonte-primaria`)

---

## 4. Para Escritores que Utilizarem Este Repositório como Modelo

Se você fizer fork ou adaptar esta estrutura para seu próprio projeto literário:

1. **Mantenha o revisor** — ele é parte do contrato ético com seus leitores
2. **Atualize a Seção 3.1** com o seu uso declarado de IA
3. **Ajuste os limiares** em `tests/metrics.py` para seu estilo e idioma
4. **Adicione padrões** em `_PT_AI_PATTERNS` que sejam relevantes para seu registro narrativo
5. **Documente exceções** no prefácio da obra quando necessário

---

## 5. Limitações do Revisor Automático

O revisor usa métricas estatísticas (burstiness, TTR, repetição de n-gramas,
padrões de frase). Ele é **indicativo, não definitivo**:

| Limitação | Descrição |
|---|---|
| Falso positivo | Pode classificar texto humano uniforme como IA |
| Falso negativo | Pode não detectar IA bem calibrada ao estilo do autor |
| Dependência de volume | Análises com < 50 palavras não são realizadas |
| Sem modelo de linguagem | Não usa perplexidade de LLM — apenas estatística local |

**O revisor não é árbitro legal ou editorial.** É uma ferramenta de consciência
e transparência, não de censura ou bloqueio de PR.

---

## 6. Referências

- Association of Writers & Writing Programs (AWP): *Statement on the Use of AI in Creative Writing*
- PEN America: *AI and the Future of Creative Work* (2023)
- [AGENTS.md](AGENTS.md) — regras operacionais deste repositório
- `.github/skills/fonte-primaria/SKILL.md` — integridade de fontes

---

*Versão: 1.0 | Data: 2026-07-20 | Projeto: O Voto Final (PAM)*
