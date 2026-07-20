# INVESTIGAÇÕES — Deep Dives por Tema

> *Aprofundamentos temáticos que sustentam a narrativa*

---

## Estrutura

```
investigacoes/
├── README.md (este arquivo)
├─ REFERENCIAS.md ([todas as fontes](REFERENCIAS.md))
├─ ADI/
│   ├─ [ADI.md (dossier corporativo)](ADI/ADI.md)
│   └─ [futuro]
├─ economia/
│   ├─ [CALCULO-MARXISTA-expandido.md](economia/CALCULO-MARXISTA-expandido.md)
│   └─ [futuro]
└─ fisica/
    ├─ [ENTROPIA-expandido.md](fisica/ENTROPIA-expandido.md)
    └── [futuro]
```

---

## 🏢 ADI — Corporação fictícia

**Tema:** Quem lucra? Como?

**Arquivos:** [ADI.md](ADI/ADI.md) | Linkado: [PAM.md](PAM/PAM.md#7-o-dinheiro), [MAP.md](MAP/MAP.md#parte-b--como-saiu-do-governo-e-virou-mercado-privado), [HISTORIA.md](../HISTORIA.md)
- `ADI/ADI.md` — Fundadores, modelo, escala, infraestrutura

**Próximos:**
- `ADI/founding-docs.md` — Memorandos internos (fictícios)
- `ADI/tech-stack.md` — Infraestrutura computacional
- `ADI/revenue-projections.md` — Modelo de receita detalhado

**Conexão narrativa:**
- Cap. 15.1 (trader profissional)
- Cap. 15.2 (hedge de silêncio)
- Cap. 17 (infiltração no prédio)
- Cap. 20–21 (colapso da ADI)

---

## 🧮 ECONOMIA — Fundamentação econômica

**Tema:** Por que o Estado legaliza apostas? Qual é o ciclo?

**Arquivos:**
- `economia/CALCULO-MARXISTA-expandido.md` — Dados, modelos, elasticidades

**Próximos:**
- `economia/comparacoes-internacionais.md` — EUA, UK, EU, Brasil
- `economia/impacto-regressivo.md` — Tabelas por decil de renda
- `economia/dependencia-fiscal.md` — Modelo temporal

**Conexão narrativa:**
- Cap. 10 (nota fiscal — governo coleta imposto)
- Cap. 12 (votação = base tributável)
- Fundamentação, ponto 4 (dupla apropriação)

---

## ⚛️ FÍSICA — Fundação termodinâmica

**Tema:** Como a entropia acelera em sistemas sociais com apostas?

**Arquivos:**
- `fisica/ENTROPIA-expandido.md` — Equações, cálculos, Prigogine

**Próximos:**
- `fisica/validacao-empirica.md` — Dados reais (se aplicável)
- `fisica/epidemiologia-vicío.md` — Modelo SIR adaptado
- `fisica/collapse-dynamics.md` — Quando a estrutura dissipativa cai?

**Conexão narrativa:**
- Cap. 6 (multiplanetário — entropia sempre vence)
- Cap. 16 (boca em boca — ordem sem algoritmo)
- Fundamentação, ponto 2 (extinção = base tributável)

---

## 📚 REFERENCIAS

**Centro de fontes.**

- Todos os autores, livros, artigos citados em HISTORIA.md devem estar aqui
- Todas as estadísticas (US$ 13.7 bi em 2024, etc) devem ter fonte e ano
- Checklist: [ ] Verificado [ ] Tradução validada [ ] URL permanente

---

## 🔗 Fluxo de contribuição

### Pesquisador encontra novo dado

1. Cria arquivo em `/investigacoes/{tema}/novo-arquivo.md`
2. Adiciona fonte em `REFERENCIAS.md`
3. Se muda HISTORIA.md, adiciona linkback (ex: "ver `/investigacoes/economia/novo-arquivo.md`")
4. Atualiza este README.md com novo arquivo

### Linkback em HISTORIA.md

Exemplo:

```markdown
O governo cobrou imposto pra enterrar o irmão.

> _Ver Fundamentação, ponto 6; para dados completos, ver 
> `/investigacoes/economia/impacto-regressivo.md` — tabela de impostos por 
> serviço funerário (2024)._
```

---

## 📊 Dados de exemplo

Estes são placeholders — atualize com dados reais antes de publicar.

### Economia

| Métrica | 2024 | Fonte |
|---------|------|-------|
| Receita de apostas esportivas (EUA) | US$ 13.7 bi | AGA (2024) |
| Impostos sobre cannabis acumulados (EUA) | >US$ 28 bi | MPP (2025) |
| Receita de apostas (Brasil) | R$ 890 mi | [VERIFICAR] |

### Física

| Conceito | Valor | Unidade |
|----------|-------|---------|
| Entropia basal (comunidade pobre) | 0.46 | nats |
| Entropia pós-legalização | 1.39 | nats |
| Tempo de colapso estrutura dissipativa | 4–8 | anos |

---

## ✅ Checklist de qualidade

Antes de fazer merge de novos arquivo em `/investigacoes/`:

- [ ] Todas as fontes citadas estão em REFERENCIAS.md?
- [ ] Dados tem ano específico (não "recente")?
- [ ] Há linkback em HISTORIA.md se muda narrativa?
- [ ] README.md foi atualizado?
- [ ] Cálculos foram revisados por especialista (se aplicável)?
- [ ] Nenhuma invenção — tudo verificável?

---

## 📝 Template para novo arquivo

```markdown
# {TITULO} — {Subtítulo}

> *{Uma linha: o que resolve este arquivo?}*

Ver arquivo-pai: `/PAM/{ARQUIVO}.md`

---

## Seção 1

### Subseção

Conteúdo com dados, tabelas, cálculos.

---

## [PREENCHER / VERIFICAR]

- [ ] {Tarefa 1}
- [ ] {Tarefa 2}
```

---

**Status:** Em desenvolvimento  
**Última atualização:** 20 de julho de 2026
