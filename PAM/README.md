# PAM — O Voto Final | Estrutura do Repositório

> *"Um mundo onde é possível apostar em tudo — inclusive no próprio fim."*

---

## 📖 Arquivo Central

| Arquivo | Conteúdo | Público? |
|---------|----------|---------|
| **HISTORIA.md** | [Romance completo: Partes I–V, 16 capítulos, 5 aprofundamentos, narrativa central](HISTORIA.md) | ✅ SIM — Leitura principal |
| **TESE.md** | [Tese resumida (ponto 1 de 2)](TESE.md) | ✅ SIM — Intro para fundamentação |
| **METODO.md** | [Método argumentativo (Toulmin + Popper)](METODO.md) | ✅ SIM — Epistemologia |

---

## 🔬 Fundamentação — Temas Científicos

| Arquivo | Tema | Ponto na tese | Público? |
|---------|------|---|---------|
| **ENTROPIA.md** | [Física; segunda lei; Prigogine; estruturas dissipativas](ENTROPIA.md) | Conexão: aposta como motor de entropia | ✅ Arquivo central |
| **CALCULO-MARXISTA.md** | [Economia; mais-valia; tripla exploração; dependência fiscal](CALCULO-MARXISTA.md) | Dupla apropriação (produção + consumo) | ✅ Arquivo central |
| **ARCO-FINAL.md** | [Estrutura narrativa dos Caps. XVII–22](ARCO-FINAL.md) | Cofre: o que está dentro, spoilers | ⚠️ Privado (escritor) |

---

## 📁 Pastas de Investigação

Estrutura: `/investigacoes/` subdivide-se por tema.

### 🏢 `/investigacoes/ADI/`

Dossier da corporação ADI Predictstreet — empresa fictícia que opera votação global.

| Arquivo | Conteúdo |
|---------|----------|
| **ADI.md** | Visão geral, fundadores, modelo de receita, infraestrutura, modelos preditivos |
| **[futuro]** | Documentos internos (leaks) |
| **[futuro]** | Cronograma: 2018–2026 |

### 🧮 `/investigacoes/economia/`

Aprofundamento econômico — série histórica, modelos, dados.

| Arquivo | Conteúdo |
|---------|----------|
| **CALCULO-MARXISTA-expandido.md** | Tabelas históricas, elasticidade-renda, modelo de dependência fiscal, validação empírica |
| **[futuro]** | Comparações internacionais |
| **[futuro]** | Simulações econométricas |

### ⚛️ `/investigacoes/fisica/`

Aprofundamento físico — cálculos, formalismo, validação teórica.

| Arquivo | Conteúdo |
|---------|----------|
| **ENTROPIA-expandido.md** | Equações diferenciais, estruturas dissipativas, série de dados |
| **[futuro]** | Validação experimental (se aplicável) |
| **[futuro]** | Comparação com epidemiologia (vício como "contágio") |

### 📚 `/investigacoes/`

Centro de referências.

| Arquivo | Conteúdo |
|---------|----------|
| **REFERENCIAS.md** | Todas as fontes primárias e secundárias; checklist de verificação |

---

## 🎭 Personagens

**Tabela em HISTORIA.md (seção PERSONAGENS)**

| Emoji | Nome | POV | Arquivos |
|-------|------|-----|----------|
| 🩶 | Você (narrador) | Primeira pessoa | Todo HISTORIA.md |
| 🕯️ | O irmão | Backstory (2.4); revelação (17) | HISTORIA.md, aprofundamentos |
| 🖤 | A mãe | Suporte moral | Caps. 5, 8, 11 |
| ⛏️ | O coveiro | Voz do sistema | Caps. 9, 17 |
| 🚬 | A senhora de preto | Dignidade | Cap. 8 |
| 💼 | O trader | POV corporativo | Aprofundamentos 15.1, 15.2 |
| 🧹 | O faxineiro | [futuro] | — |
| 🎲 | ADI Predictstreet | Antagonista sistêmica | ADI.md, HISTORIA.md |

---

## 📖 Fluxo de Leitura Recomendado

### Para leitores gerais

1. Começar: **HISTORIA.md** (romance)
2. Depois: **TESE.md** (entender a tese)
3. Profundo: **ENTROPIA.md** + **CALCULO-MARXISTA.md** (fundamentação)

### Para pesquisadores / academicistas

1. **METODO.md** (como é argumentado?)
2. **TESE.md** (resumo da tese)
3. **CALCULO-MARXISTA.md** (evidência econômica)
4. **ENTROPIA.md** (evidência física)
5. **REFERENCIAS.md** (verificar cada citação)
6. **/investigacoes/** (dados brutos, expansões)

### Para worldbuilding / ficção

1. **HISTORIA.md** (story)
2. **ARCO-FINAL.md** (onde vai terminar)
3. **ADI.md** (entender a corporação)
4. **PERSONAGENS** em HISTORIA.md

---

## 🔄 Ciclo de trabalho

### Escrita

1. Novo capítulo em branch `cap/{romano}-{slug}`
2. Referências verificadas contra `/investigacoes/REFERENCIAS.md`
3. Se novo personagem: update `/investigacoes/personagens/` (futuro)
4. PR com título `Cap. X — Título` → review → merge

### Investigação

1. Nova descoberta ou dado em `/investigacoes/{tema}/`
2. Atualizar `/investigacoes/REFERENCIAS.md` com fonte
3. Linkback em HISTORIA.md relevante (ex: Cap. 7 → "ver CALCULO-MARXISTA")

### Release

1. Merge de branch em `main`
2. Release workflow calcula semver (branch prefix)
3. Tag `vX.Y.Z` gerada; release notes = PR title

---

## 🔗 Créditos de Inspiração

- **Prigogine** — entropia e estruturas dissipativas
- **Marx** — mais-valia e exploração
- **Piketty** — desigualdade e tributação
- **Georgescu-Roegen** — economia como termodinâmica
- **Gibson, Atwood, Stephenson** — ficção corporativa

---

## 📋 Próximas Etapas

- [ ] Preencher **ARCO-FINAL.md** (Caps. XVII–XXII completos)
- [ ] Expandir **/investigacoes/economia/** com dados Brasil 2024–2026
- [ ] Criar **aprofundamento 15.3** (POV trader + quebra de modelo)
- [ ] Validação: todas as citações em REFERENCIAS.md
- [ ] Design visual: HISTORIA.md → epub/pdf com notas de rodapé

---

## 📞 Perguntas comuns

**P: Qual é a ordem correta de leitura?**  
R: Começa em HISTORIA.md. Se quer entender a tese, depois lê TESE.md + fundamentação. Para aprofundo, siga para `/investigacoes/`.

**P: ARCO-FINAL.md é spoiler?**  
R: Sim. Escritor apenas. Leitores não devem ter acesso até publicação.

**P: Como adiciono nova descoberta?**  
R: Cria arquivo em `/investigacoes/{tema}/`. Depois atualiza REFERENCIAS.md. Se muda história, linkback em HISTORIA.md.

**P: Como cito uma fonte?**  
R: Usa padrão Chicago (autor-ano). Verifica em REFERENCIAS.md. Se não está, adiciona com verificação.

---

**Última atualização:** 20 de julho de 2026  
**Versão:** 0.0.4  
**Status:** Em desenvolvimento — Parte V completa; Parte VI planejada
