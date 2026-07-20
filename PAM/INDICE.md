# ÍNDICE COMPLETO — O Voto Final | PAM

> *Mapa de toda a estrutura: onde cada coisa está e como se relaciona*

---

## 📍 Raiz da história: Arquivos principais

```
PAM/
├── README.md ........................ Guia geral de estrutura
├── HISTORIA.md ...................... 🔥 ARQUIVO CENTRAL — Romance completo
├── TESE.md .......................... Tese resumida (ponto 1 de 2)
├── METODO.md ........................ Método argumentativo (Toulmin + Popper)
├── ENTROPIA.md ...................... Fundação física (Prigogine, estruturas dissipativas)
├── CALCULO-MARXISTA.md .............. Fundação econômica (Marx, mais-valia, tributação)
└── ARCO-FINAL.md .................... ⚠️ SPOILER — O que vem depois (Caps. XVII–XXII)
```

---

## 🔬 Investigações temáticas

```
investigacoes/
├── README.md ........................ Guia desta seção
├── REFERENCIAS.md ................... 📚 Todas as fontes primárias e secundárias
│
├── ADI/ ............................ 🏢 CORPORAÇÃO FICTÍCIA
│   └── ADI.md ...................... Fundadores, modelo, revenue, infraestrutura, modelos preditivos
│   └── [futuro] .................... Documentos internos, tech-stack, cronograma
│
├── economia/ ....................... 🧮 APROFUNDAMENTO ECONÔMICO
│   ├── CALCULO-MARXISTA-expandido.md  Dados, elasticidades, dependência fiscal
│   └── [futuro] .................... Comparações internacionais, simulações
│
└── fisica/ ......................... ⚛️ APROFUNDAMENTO FÍSICO
    ├── ENTROPIA-expandido.md ....... Equações, estruturas dissipativas, série de dados
    └── [futuro] .................... Validação empírica, epidemiologia do vício
```

---

## 📖 Hierarquia de leitura

### Linha 1: Para leitores gerais

```
HISTORIA.md (romance inteiro)
    ↓
TESE.md (entender o ponto)
    ↓
ENTROPIA.md + CALCULO-MARXISTA.md (entender por quê)
```

### Linha 2: Para pesquisadores

```
METODO.md (epistemologia)
    ↓
TESE.md (resumo tese)
    ↓
HISTORIA.md (prova narrativa)
    ↓
CALCULO-MARXISTA.md + ENTROPIA.md (fundamentação)
    ↓
investigacoes/economia/ + investigacoes/fisica/ (dados brutos)
    ↓
REFERENCIAS.md (validação)
```

### Linha 3: Para ficcionistas

```
HISTORIA.md (story)
    ↓
ARCO-FINAL.md (onde termina)
    ↓
ADI.md (entender antagonista)
    ↓
HISTORIA.md — seção PERSONAGENS
```

---

## 🎭 Mapa de personagens & POVs

| Emoji | Nome | POV | Aparições principais | Arquivo |
|-------|------|-----|----------------------|---------|
| 🩶 | Você (narrador) | 2ª pessoa | Caps. 1–16, todas partes | HISTORIA.md inteiro |
| 🕯️ | O irmão | Flashback + revelação | Cap. 5, 2.4, 17 | HISTORIA.md |
| 🖤 | A mãe | Suporte | Caps. 5, 8, 11 | HISTORIA.md |
| ⛏️ | O coveiro | Voz do sistema | Caps. 9, 17 | HISTORIA.md |
| 🚬 | A senhora de preto | Dignidade | Cap. 8 | HISTORIA.md |
| 💼 | O trader | POV corporativo | Aprof. 15.1, 15.2 | HISTORIA.md |
| 🎲 | ADI Predictstreet | Antagonista sistêmica | Toda a história | HISTORIA.md, ADI.md |

---

## 🔗 Conexões entre arquivos

### HISTORIA.md referencia

```
Cap. 7 (Cálculo)
  ↓
  "Ver CALCULO-MARXISTA.md — nota sobre mais-valia"
  
Cap. 10 (Nota Fiscal)
  ↓
  "Ver FUNDAMENTAÇÃO ponto 6 — Estado como sócio silencioso"

Cap. 12 (Todo Dia)
  ↓
  "A extinção transformada em base tributável. É a Regra do Mundo 
   se fechando sobre a tese. Ver FUNDAMENTAÇÃO ponto 2."

Aprof. 15.1 (O trader)
  ↓
  "Ver investigacoes/economia/ — como lucra a indignação pobre"

Aprof. 15.2 (A pá no cifrão)
  ↓
  "Ver ENTROPIA.md — dissipação de ordem via oral"
```

### ARCO-FINAL referencia

```
Cap. 17 (O Prédio por Dentro)
  ↓
  "Ver ADI.md — sede fictícia, infraestrutura, 'O Votador'"

Cap. 20 (Trader percebe)
  ↓
  "Ver investigacoes/economia/dependencia-fiscal.md 
   — cascata de liquidação"

Cap. 21 (Estrutura Dissipativa Colapsa)
  ↓
  "Ver ENTROPIA.md + CALCULO-MARXISTA.md — modelo de colapso"
```

---

## 📊 Estatísticas do projeto

| Métrica | Número |
|---------|--------|
| Capítulos narrativos (HISTORIA.md) | 16 |
| Aprofundamentos narrativos | 15 |
| Partes | 5 (+ 3 planejadas em ARCO-FINAL) |
| Arquivos de fundamentação | 4 (TESE, METODO, ENTROPIA, CALCULO) |
| Arquivos de investigação | 6+ |
| Personagens nomeados | 8 |
| Emojis de marca (personagens) | 11 |
| Linhas em HISTORIA.md | 677+ |
| Branches de trabalho | cap/*, aprof/*, chore/* |

---

## ⚙️ Workflow de contribuição

### Novo capítulo

```
1. git checkout -b cap/{romano}-{slug}
2. Escrever em HISTORIA.md (seção "A HISTÓRIA")
3. Referências verificadas em REFERENCIAS.md
4. PR: "Cap. {n} — {Título}"
5. Merge → release v?.?.? automática
```

### Nova investigação

```
1. Criar /investigacoes/{tema}/novo-arquivo.md
2. Adicionar fonte em REFERENCIAS.md
3. Linkback em HISTORIA.md (se aplicável)
4. Atualizar README.md de investigacoes/
5. PR, merge
```

### Novo aprofundamento

```
1. git checkout -b aprof/{decimal}-{slug}
2. Escrever em HISTORIA.md (seção "APROFUNDAMENTOS")
3. Tipo obrigatório: 📍 (gancho) ou 🔎 (paralelo)
4. PR: "Aprof. {n} — {Título}"
5. Merge → patch bump
```

---

## 🚀 Próximas fases (planejadas)

### Fase 1 — Consolidação (atual)
- [x] HISTORIA.md (Caps. 1–16)
- [x] TESE, METODO, ENTROPIA, CALCULO
- [x] Aprofundamentos 2.1–2.5, 15.1, 15.2
- [x] ADI.md
- [ ] ARCO-FINAL.md completo (Caps. XVII–XXII)

### Fase 2 — Investigação profunda (próxima)
- [ ] investigacoes/economia/ — dados Brasil 2024–2026
- [ ] investigacoes/fisica/ — validação de modelos
- [ ] investigacoes/ADI/ — documentos internos (fictícios)
- [ ] REFERENCIAS.md — verificação de todas as citações

### Fase 3 — Distribuição (futuro)
- [ ] HISTORIA.md → ePub com notas de rodapé
- [ ] Versão acadêmica com apêndices
- [ ] Audiobook (segunda pessoa mantida)
- [ ] Adaptação visual / HQ

---

## 📝 Guia rápido — Onde encontro X?

| Pergunta | Resposta |
|----------|----------|
| "Quero ler o romance" | → HISTORIA.md |
| "Qual é a tese?" | → TESE.md |
| "Por que o Estado legaliza?" | → CALCULO-MARXISTA.md |
| "Como a entropia se acelera?" | → ENTROPIA.md |
| "Quem é a ADI?" | → ADI.md |
| "Qual é o final?" | → ARCO-FINAL.md (spoiler) |
| "Onde estão as referências?" | → REFERENCIAS.md |
| "Como contribuo?" | → README.md de investigacoes/ |
| "Qual é a estrutura geral?" | → Este arquivo (ÍNDICE) |

---

## 🔐 Acesso

| Arquivo | Público? | Razão |
|---------|----------|-------|
| HISTORIA.md | ✅ SIM | Obra principal |
| TESE.md | ✅ SIM | Fundação |
| METODO.md | ✅ SIM | Epistemologia |
| ENTROPIA.md | ✅ SIM | Fundamentação |
| CALCULO-MARXISTA.md | ✅ SIM | Fundamentação |
| ARCO-FINAL.md | ⚠️ PRIVADO | Spoilers; apenas escritor |
| ADI.md | ✅ SIM | Worldbuilding |
| investigacoes/ | ✅ SIM | Pesquisa aberta |
| REFERENCIAS.md | ✅ SIM | Transparência |

---

## 📞 Perguntas frequentes

**P: Em que ordem leio tudo?**  
R: Se quer história, começa HISTORIA.md. Se quer entender a tese, depois TESE.md → fundamentação. Para pesquisa profunda, siga "Linha 2" acima.

**P: Posso contribuir novos dados?**  
R: Sim! Cria arquivo em `/investigacoes/{tema}/`. Atualiza REFERENCIAS.md. Faz PR.

**P: ARCO-FINAL é realmente spoiler?**  
R: Sim — contém Caps. XVII–XXII inteiros. Só abra se souber que quer saber como termina.

**P: Como cito uma fonte?**  
R: Padrão Chicago. Verifica em REFERENCIAS.md. Se não tá, adiciona com URL permanente + ano.

---

**Última atualização:** 20 de julho de 2026  
**Versão do projeto:** 0.0.4  
**Status:** Em desenvolvimento — narrativa 5/8 partes; investigação 3/5 tópicos
