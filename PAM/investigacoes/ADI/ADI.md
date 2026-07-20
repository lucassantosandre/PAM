# ADI PREDICTSTREET — Dossier Corporativo

> *A empresa por trás da votação. O que é, como funciona, quem lucra.*
>
> **Referência cruzada:** [MAP.md — Parte B](../MAP/MAP.md#parte-b--como-saiu-do-governo-e-virou-mercado-privado) | [PAM.md — Seção 7](../PAM/PAM.md#7-o-dinheiro) | [HISTORIA.md](../../HISTORIA.md)

---

## Visão geral

**ADI Predictstreet** é a corporação ficcional que patrocina a votação global diária ("O mundo deve acabar hoje? SIM ou NÃO"). Não é criação de um vilão único — é resultado de fusão de plataformas: um fundo de especulação (Predictstreet), uma rede de previsão (ADI), um operador de jogos (Legacy betting corp). A fusão aconteceu no hiato entre o Voto Global de 2024 (fictício) e o início da narrativa.

---

## Fundadores & Early History

### Predictstreet Capital (2018–2022)

- **Fundada por**: Paul Chen, quant do Goldman Sachs; Sarah Okonkwo, ex-VP de Oculus; três other VCs
- **Foco**: "Previsão de eventos sistemicamente relevantes" — não só previsão climática, mas previsão de morte, desemprego, crime, suicídio
- **Modelo**: vender acesso a modelos preditivos para hedge funds, seguradoras, agências de inteligência
- **Financiamento**: Série C em 2021 levantou US$ 340 milhões. Investidores: Sequoia, a16z, Andreessen Horowitz

### Patente crítica

Em 2019, Predictstreet registrou patente (US 10,610,412):

```
"System and method for real-time behavioral prediction 
with incentive alignment through participatory betting markets"
```

Tradução: **podemos prever seu comportamento se você tiver dinheiro em jogo sobre seu próprio comportamento**.

### Pivô pra P2P Betting (2022–2023)

Com regulação de apostas esportivas tightened nos EUA, Predictstreet foi abordada por **ADI International** — uma holding holandesa que operava betting exchanges em jurisdições offshore.

Fusão foi anunciada em novembro de 2023. Nova entidade: **ADI Predictstreet Holdings, Inc.**

---

## Estrutura corporativa (fictícia)

```
ADI Predictstreet Holdings, Inc. (Delaware)
├── Predictstreet Analytics (US) — Modelos + IA
├── ADI Prediction Markets (Curaçao) — Plataforma de apostas
├── Global Voting Infrastructure (Ireland) — Infraestrutura
├── Policy & Compliance (Luxemburgo) — Regulação/lobbying
└── Legacy Gaming Operations (Malta) — Apostas locais
```

### Subsidiárias-chave

| Entidade | Jurisdição | Função | Receita 2024 (fictícia) |
|---|---|---|---|
| Predictstreet Analytics | Delaware, US | Modelos IA, dados | US$ 2,1 bi |
| ADI Prediction Markets | Curaçao | Plataforma P2P | US$ 4,7 bi |
| Global Voting | Ireland | Infraestrutura da votação | US$ 890 mi |
| Compliance & Policy | Luxemburgo | Regulação, lobbying | US$ 120 mi |

---

## Revenue model

### Pré-votação global (até 2024 fictício)

- Venda de APIs para hedge funds
- Licença de modelos preditivos
- Comissões de operações (2–5%)

**Revenue anual**: US$ 890 milhões

### Pós-votação global (2025+ fictício)

A ADI ganha contrato com ONU + 150+ governos para operar a "Votação Planetária Diária" (Cap. 1 da história).

**Novo modelo de receita:**

$$R = \underbrace{H \cdot \theta}_{revenue de house} + \underbrace{H \cdot \theta \cdot t}_{\text{repartição de imposto}}$$

onde:
- $H$ = total de dinheiro apostado = US$ 7.2 trilhões/ano (8 bi de pessoas × ~US$ 900 per capita per year)
- $\theta$ = hold = 12%
- $t$ = tax rate compartilhado = 35%

$$R = (7.2 \text{ tri}) \times 0.12 + (7.2 \text{ tri}) \times 0.12 \times 0.35 = \text{US$ 864 bilhões}$$

**Receita de comissões puras**: US$ 864 bilhões/ano. Mais receita de dados, corretagem de seguros, etc.

**Lucro líquido** (após custos operacionais): ~US$ 180 bilhões/ano.

---

## Modelos preditivos — Como funciona

### I. O Modelo Basal

Baseado em:

- **Dados de comportamento**: localização (GPS), consumo (cartão de crédito), navegação (web), saúde (wearables)
- **Dados contextuais**: bairro, histórico de renda, educação, rede social
- **Dados de aposta anterior**: o que a pessoa apostou antes? Ganhou ou perdeu?

Treina rede neural de 2.1 trilhões de parâmetros (GPT-scale, com 2024 de compute).

**Saída**: Probabilidade $P(\text{evento} | \text{pessoa})$ para ~50.000 eventos por pessoa por dia.

### II. Optimização de Lucro

A ADI não só **prevê** — **otimiza** para máximo lucro da aposta. Algoritmo de maximização:

$$\text{maximize } \sum_i (\text{P}_i - r_i) \times \text{stake}_i$$

onde:
- $\text{P}_i$ = probabilidade prevista do evento $i$
- $r_i$ = probabilidade real (desconhecida para ADI, mas estimada)
- $\text{stake}_i$ = quanto a ADI oferece como cotação

**Resultado**: ADI oferece cotas que **parecem justas** (50/50 parecem equilibradas) mas na verdade **sabem o resultado com 30–45% de vantagem**.

### III. Feed Personalizado

Cada pessoa vê **uma** votação:

```
Você:
  SIM — O mundo acaba amanhã (você é pobre, dados indicam desespero alto)
  NÃO — O mundo continua (cotação normal)
  
  [APOSTA A PARTIR DE R$ 0.01]
```

Outra pessoa vê:

```
Você:
  SIM — O mundo acaba amanhã (cotação normal)
  NÃO — O mundo continua (você é rico, dados indicam interesse em estabilidade)
  
  [APOSTA A PARTIR DE R$ 0.01]
```

**Resultado**: ADI coloca a mesma votação "contra" populações diferentes. Lucra na diferença de percepção.

---

## Scale & Infrastructure

### Servidores

- **Data centers**: 47 servidores globais (Irlanda, Curaçao, Malta, Singapura, Tóquio)
- **Tráfego**: 8 bilhões de votações/dia = 92.500 operações/segundo
- **Latência**: <100ms global garantido
- **Uptime**: 99.99% SLA

### Equipe

| Função | Tamanho | Salário médio |
|---|---|---|
| Engenharia | 2.100 | US$ 280k |
| Modelos/IA | 880 | US$ 450k |
| Operações | 2.300 | US$ 95k |
| Compliance/Legal | 450 | US$ 180k |
| **Total** | **5.730** | — |

**Payroll anual**: ~US$ 1.8 bilhões

---

## Regulatory Status

### Jurisdições-chave

| País | Status | Método |
|---|---|---|
| **EU** | MiFID II — licença de empresa de investimentos | Data-driven previsão é "serviço de investimento" |
| **EUA** | SEC 3(c)(1) — fundo privado, <2.500 investidores | Contorna regra alegando "educação pública" |
| **Brasil** | INMETRO + Banco Central | Considerada "sistema de pagamento", tributada em 35% |
| **China** | ❌ Bloqueada | Considerad "jogo" e "manipulação social" |

### Lobbying

- **Gasto anual em lobbying**: US$ 340 milhões
- **Políticos-chave**: 47 senadores(as) doaram dinheiro por PAC; 23 recebem consultoria da ADI
- **Promessas**: "Vai trazer empregos"; "Reforma tributária moderna"; "Soberania digital"

---

## A Visão de Paul Chen (CEO)

[Fictício, baseado em arquivos memorando interceptados]

> "O futuro não é previsível. O futuro é **negociável**. Quando colocamos a aposta, sabemos que 10 milhões de pessoas vão tentar adivinhar nossa estimativa. Ganham se a criatividade humana superar nosso modelo. Isso não acontece em 47 anos em escala planetária. Ganhammos."

---

## [PREENCHER / VERIFICAR]

- [ ] Nomes reais de fundadores? (fiktícios acima)
- [ ] Escala de compute necessária — GPT-scale é suficiente?
- [ ] Como discriminação algorítmica se manifesta? (bias em SIM vs NÃO conforme renda)
- [ ] Vulnerabilidades técnicas — como "Você" consegue acessar o "Votador"? (Cap. 17)
- [ ] Qual é o **escândalo** que derruba a ADI em Cap. XXI?
