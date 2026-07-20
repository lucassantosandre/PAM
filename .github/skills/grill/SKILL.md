---
name: grill
description: >
  Aplica questionamento socrático agressivo a qualquer ideia, cena, diálogo ou argumento
  do projeto PAM. Faz as perguntas difíceis antes do escritor commitar. Funciona como
  "banca de defesa interna" — não para reprovar, mas para tornar o argumento à prova de
  ataque externo. Inspirado no método grill.me: confrontar ideias até restarem só as que
  aguentam pressão.
argument-hint: "Ex: 'grille a ideia de que mafias controlam odds de morte' ou 'grille o diálogo do Cap. XVII linha 3'"
---

# Skill: grill

O **grill** é um interrogatório socrático. Não elogia. Não valida automaticamente.
Faz as perguntas que um leitor cético, um revisor acadêmico, ou um advogado do diabo
fariam — antes que qualquer pessoa de fora faça.

---

## Quando usar esta skill

- Antes de commitar uma ideia narrativa nova
- Quando uma cena implica algo que o escritor não testou
- Quando um argumento parece "óbvio demais" (sinal de que pode não aguentar pressão)
- Quando um personagem diz algo que pode ser contestado internamente
- Ao criar novos arcos ou aprofundamentos que alteram o equilíbrio da história
- **Sempre que o escritor tiver dúvida** — o grill transforma dúvida em clareza

---

## Modo de operação

### Nível 1 — Clareza (sempre)

Perguntas básicas que qualquer leitor vai ter:

1. _"O que exatamente você está dizendo aqui?"_ → isolar a afirmação
2. _"Por que isso é verdade neste mundo?"_ → warrant narrativo
3. _"Quem poderia discordar — e por quê?"_ → rebuttal

### Nível 2 — Consistência interna

4. _"Isso contradiz algo que já foi estabelecido na história?"_
5. _"O personagem que diz isso saberia disso neste momento?"_
6. _"Se isso é verdade no Cap. X, o que implica para o Cap. Y?"_

### Nível 3 — Pressão estrutural

7. _"E se o leitor não aceitar esse pressuposto?"_
8. _"Qual é o contra-exemplo mais forte que destrói essa ideia?"_
9. _"Isso é necessário para a história ou apenas interessante?"_
10. _"Se remover isso, a tese ainda se sustenta?"_

### Nível 4 — Pressão tese central

11. _"Essa ideia confirma, enfaquece ou é indiferente à tese: 'O Estado administra o vício por cálculo fiscal'?"_
12. _"Se confirma: de que forma específica? Qual mecanismo?"_
13. _"Se enfraquece: é honesto incluir mesmo assim, ou distrai?"_

---

## Workflow

1. Receber o objeto a ser grillado (ideia, cena, diálogo, arco, argumento acadêmico)
2. Classificar: narrativo / acadêmico / misto
3. Aplicar perguntas de Nível 1 → 2 → 3 → 4, em sequência
4. Para cada pergunta, gerar a resposta mais forte possível **contra** a ideia
5. Ao final, produzir:
   - **Pontos sólidos** (resistiram ao grill)
   - **Pontos frágeis** (precisam de revisão)
   - **Pontos mortais** (comprometem a ideia — recomendar reescrever)
   - **Veredicto:** [PASSA] / [PASSA COM RESSALVAS] / [REPROVAR — REESCREVER]

---

## Output estruturado

```
## Grill — [OBJETO GRILLADO]

### Afirmação central
> "..."

### Perguntas e pressões
| # | Pergunta | Pressão mais forte contra |
|---|---------|--------------------------|
| 1 | ... | ... |
| 2 | ... | ... |
...

### Pontos sólidos
- ...

### Pontos frágeis
- ...

### Pontos mortais
- ...

### Veredicto
[PASSA] / [PASSA COM RESSALVAS] / [REPROVAR — REESCREVER]

### Próximos passos recomendados
- ...
```

---

## Regras do grill

- **Nunca elogiar sem antes pressionar** — o grill vem antes da aprovação
- **Perguntas, não afirmações** — o grill abre, não fecha
- **Sem misericórdia com pressupostos não examinados** — todo "óbvio" vira pergunta
- **O objetivo é fortalecer, não destruir** — se uma ideia sobrevive ao grill, ela está pronta
- Argumentos acadêmicos → escalar para skill `metodo` após o grill
- Fontes em dúvida → escalar para skill `fonte-primaria`

---

## Exemplos de objetos para grill

### Ideia narrativa: "mafias controlam as odds de morte"

**Grill imediato:**
- _"Como exatamente uma mafia 'controla' uma odd em sistema aberto e regulado?"_
- _"A ADI deixaria isso acontecer, ou ela própria É a mafia estrutural?"_
- _"O leitor vai aceitar isso como plausível ou vai quebrar a suspensão de descrença?"_
- _"Se mafias controlam odds, por que o trader do Cap. 15 não sabia?"_

### Diálogo de personagem: "O coveiro sabe do esquema das mafias"

**Grill imediato:**
- _"Por que o coveiro saberia disso? De onde vem essa informação?"_
- _"Ele revela isso de graça? Qual o custo narrativo de revelar?"_
- _"Isso muda o personagem do coveiro de 'testemunha lúcida' para 'informante' — é intencional?"_

---

## Referências metodológicas

- **Sócrates** via Platão — método da elenchus (refutação socrática)
- **Toulmin**, S. (1958). _The Uses of Argument_. — estrutura do argumento
- **Popper**, K. (1959). _The Logic of Scientific Discovery_. — falsificabilidade
- [METODO.md](../../PAM/METODO.md) — fundação metodológica do projeto
- Skill [metodo](../metodo/SKILL.md) — validação formal pós-grill
