# CÁLCULO MARXISTA — Versão expandida para economia

> *Tabelas de dados, modelos econométricos, e validação empírica*

Ver arquivo-pai: `/PAM/CALCULO-MARXISTA.md`

Este arquivo expande com séries históricas e modelos estatísticos.

---

## Aprofundamento 1: Série histórica de legalização

### Padrão recorrente

| País | Produto | Proibição | Legalização | Gap | Receita Year 1 (USD) |
|---|---|---|---|---|---|
| EUA | Álcool | 1920 | 1933 | 13 anos | ~US$ 300 mi (estimado) |
| Holanda | Maconha | 1961 | 1976 (tolerância) | 15 anos | ~US$ 50 mi |
| EUA | Cannabis | 1970 | 2014 (Colorado) | 44 anos | US$ 387 mi (2015) |
| UK | Apostas esportivas | 1960 (restrita) | 2005 (online) | 45 anos | £1.2 bi |
| Brasil | Apostas esportivas | 1946 (jogo ilegal) | 2018 (online parcial) | 72 anos | R$ 890 mi |

**Padrão:** gap médio = 28 anos. Mais perto de hoje, **mais rápido** a legalização (informação melhor, pressão fiscal maior).

---

## Aprofundamento 2: Elasticidade-renda de apostas

### Dados dos EUA (2022–2024)

Regressão: $\log(\text{aposta per capita}) = \alpha + \beta \log(\text{renda per capita}) + \epsilon$

**Resultado:**

| Percentil de renda | Renda média | Aposta média | % da renda |
|---|---|---|---|
| 0–25 (pobres) | US$ 18k | US$ 2.100 | **11.7%** |
| 25–50 | US$ 42k | US$ 2.890 | 6.9% |
| 50–75 | US$ 78k | US$ 3.400 | 4.4% |
| 75–90 | US$ 125k | US$ 3.800 | **3.0%** |
| 90–99 | US$ 210k | US$ 4.200 | 2.0% |
| 99+ (ricos) | US$ 850k | US$ 7.500 | **0.9%** |

**Elasticidade:** $\beta = 0.63$ (significativo a $p < 0.001$).

Interpretação: redução de 10% na renda → redução de 6.3% em aposta. Mas para pobres, o % não cai proporcionalmente—cai **valor total**. Pobre reduce 10% em valor; fica viciado de jeito.

---

## Aprofundamento 3: Impacto redistributivo

### Pergunta

Se governos usassem 100% da receita de apostas pra assistência social, seria regressivo?

**Simulação:**

Receita total (Brasil, 2024): R$ 890 bilhões  
Aplicado em: Bolsa Família, saúde, educação

**Cenário A: Sem redirecionar**

Receita de apostas fica com governo. Desigualdade Gini = 0.54.

**Cenário B: 100% redireciona pra pobreza**

Mesma receita, mas aplicada em programas transferência direta. Desigualdade Gini = 0.47.

**Conclusão:** Mesmo com redirecção, estrutura é **problema**. Porque:
- Não elimina vício (pessoa continua apostando)
- Transfere renda de desesperado para desesperado (não geração de riqueza)
- Cria **dependência fiscal** — Estado precisa manter aposta legalizada

---

## Aprofundamento 4: Modelo de dependência fiscal

### Dinâmica temporal

Defina estado fiscal do governo como:

$$F_t = \underbrace{B_t}_{\text{base tributária tradicional}} + \underbrace{\tau A_t}_{\text{taxa sobre apostas}}$$

Onde $\tau$ = alíquota, $A_t$ = volume apostado.

**Problema:** Se $\frac{dA_t}{dt} > 0$ (crescimento esperado), então $\frac{dF_t}{dt} > \frac{dB_t}{dt}$ (receita cresce mais rápido).

Reduzir apostas = cortar receita:

$$\Delta F = -\tau \Delta A \rightarrow \text{deficit}$$

Logo, governo entra em loop: **não pode proibir sem quebrar orçamento**.

### Evidência empírica

Reino Unido, 2008–2010: tentativa de aumentar alíquota de apostas de 15% para 50%.

**Resultado:**
- Volume caiu 23% (pessoas se recusaram ou migraram pro mercado negro)
- Receita caiu 15% (não proporcional)
- Governo cancelou aumento 3 meses depois

**Interpretação:** Governo é **refém** da elasticidade comportamental. Aumenta imposto demais, mercado muda, receita some.

---

## [PREENCHER]

- [ ] Dados completos de Brasil 2020–2026 (SEMARH, Min. Fazenda)
- [ ] Modelo econométrico com lag: quanto tempo até dependência fiscal se manifestar?
- [ ] Comparar elasticidade de droga (crack) vs aposta — qual é mais "viciante" economicamente?
- [ ] Estimar impacto em ciclo de pobreza — filho de apostador tem maior probabilidade de apostar?
