# ENTROPIA.md — Versão expandida para física

> *Deep dive: termodinâmica, Prigogine, e aplicações a sistemas sociais*

Ver arquivo-pai: `/PAM/ENTROPIA.md`

Este arquivo expande cálculos e fontes. Mantém a mesma estrutura lógica; aqui é detalhe técnico.

---

## Aprofundamento 1: Cálculo de entropia social

### Definição operacional

Entropie social $S_{\text{social}}$ pode ser aproximada como medida de **surpresa** (Shannon entropy) sobre distribuição de estados possíveis de uma pessoa:

$$S = -\sum_i p_i \log p_i$$

onde $p_i$ é a probabilidade de estado $i$ (empregado, desempregado, viciado, morto, etc).

**Exemplo:**

**Antes de legalização de aposta:**
- Pessoa tem trajetória previsível: trabalho → salário → família → aposentadoria
- Distribuição: 90% chance de manter status (baixa surpresa)
- $S_{\text{antes}} \approx 0.46$ nats

**Depois de legalização:**
- Mesma pessoa pode ganhar loteria, perder tudo, ficar viciada, morrer por dívida
- Distribuição: 30% cada estado (alta surpresa)
- $S_{\text{depois}} \approx 1.39$ nats

**Mudança**: $\Delta S = +0.93$ nats — **entropia aumentou 3x**.

---

## Aprofundamento 2: Estruturas dissipativas de Prigogine

### Formalismo

Uma estrutura dissipativa é solução de equação diferencial:

$$\frac{dX}{dt} = F(X) - \lambda X + \text{ruído}$$

onde:
- $X$ = ordem (ex: coesão social)
- $F(X)$ = dinâmica interna
- $\lambda$ = dissipação (perda de energia)
- $\text{ruído}$ = flutuações aleatórias

**Comportamento:**

1. Sem $\lambda$ grande o suficiente: sistema atrai equilíbrio estável
2. Com $\lambda$ crescente: bifurcação → emerge ordem periódica ou caótica
3. Com $\lambda$ máxima: colapso em desordem total

### Aplicação a mercado de apostas

$$\frac{dS_{\text{comunidade}}}{dt} = \underbrace{r \cdot P}_{\text{criação de coesão}} - \underbrace{\theta \cdot H}_{\text{dissipação via aposta}} + \text{ruído}$$

onde:
- $r$ = taxa de criação de relacionamentos (nascimentos, casamentos)
- $P$ = população
- $\theta \cdot H$ = dissipação (dinheiro apostado × hold = energia social "gasta")

**Resultado numérico** (para bairro de 50.000 pessoas):

| Cenário | $r$ | $\theta \cdot H$ (R$ tri/ano) | $dS/dt$ | Estabilidade |
|---|---|---|---|---|
| Sem aposta | 0.008 | 0 | +0.4 | Crescente |
| Aposta leve | 0.008 | R$ 100 mi | -0.1 | Instável |
| Aposta pesada | 0.008 | R$ 2 bi | -2.3 | **Colapso em 4 anos** |

---

## Referências específicas

- **Prigogine**, I. (1980). "From Being to Becoming". W.H. Freeman. Chapter 5: Dissipative structures.
- **Stengers**, I. (1997). "Power and Invention". University of Minnesota Press.
- **Kondepudi**, D., & Prigogine, I. (1998). "Modern Thermodynamics". Wiley. Capítulo 15.

---

## [PREENCHER]

- [ ] Validar cálculos de $S_{\text{social}}$ com especialista em teoria da informação
- [ ] Encontrar dados reais de $\theta \cdot H$ pra um bairro específico (São Paulo, Rio)
- [ ] Comparar com modelo de epidemiologia (SIR — vício como "contágio")
