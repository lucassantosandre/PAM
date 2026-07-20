---
name: metodo
description: >
  Valida argumentos, ideias narrativas e afirmações da história contra o método Toulmin
  e o critério de falseabilidade de Popper. Responde se um argumento sustenta a tese
  do projeto, se tem warrant, se é falsificável, e aponta lacunas. Também aplica
  grilo socrático a cenas e diálogos para detectar inconsistências antes de commitar.
argument-hint: "Ex: 'valide o argumento do Cap. XV sobre morte como aposta' ou 'tese: mafias controlam odds de morte — valide'"
---

# Skill: método

Aplica o **modelo de Toulmin** e o **critério de Popper** a qualquer afirmação do
projeto — seja uma tese acadêmica, uma ideia narrativa, um diálogo de personagem,
ou um arco de capítulo.

---

## Quando usar esta skill

- Antes de escrever um capítulo com argumento novo
- Quando uma cena faz uma afirmação implícita sobre o mundo (ex: "mafia controla taxa de morte")
- Quando a fundamentação acadêmica precisa ser verificada antes de entrar na narrativa
- Quando o escritor tem dúvida se uma ideia narrativa é coerente com a tese central
- Ao revisar aprofundamentos para garantir que alimentam o argumento, não o contradizem

---

## O modelo de Toulmin — 6 componentes

```
CLAIM (Afirmação)
  └─ o que você está defendendo

GROUNDS (Fundamento)
  └─ os dados/fatos que sustentam a claim

WARRANT (Licença)
  └─ o princípio geral que conecta grounds → claim
  └─ "por que esses dados provam essa afirmação?"

BACKING (Suporte)
  └─ a autoridade/teoria que valida o warrant

QUALIFIER (Qualificador)
  └─ o grau de certeza ("provavelmente", "em geral", "sempre que...")

REBUTTAL (Refutação antecipada)
  └─ quando a claim não vale / contra-argumento que você já conhece
```

---

## Workflow

### Passo 1 — extrair os componentes

Dado o argumento bruto do escritor, identificar:

1. **Claim** — isolar a afirmação principal (1 frase)
2. **Grounds** — listar os dados que a suportam (verificar contra [REFERENCIAS.md](../../PAM/investigacoes/REFERENCIAS.md))
3. **Warrant** — explicitar o princípio implícito
4. **Backing** — indicar qual autor/teoria responde por ele (Marx, Prigogine, Harvey, Hanson...)
5. **Qualifier** — avaliar o grau de generalização
6. **Rebuttal** — levantar pelo menos 2 objeções sérias

### Passo 2 — teste de Popper

Perguntar: **o que poderia falsificar essa afirmação?**

- Se nada pode falsificá-la → não é argumento, é dogma. Reportar ao escritor.
- Se existe um cenário falsificador → registrar como `[EM ABERTO]` em REFERENCIAS.md.

### Passo 3 — verificar coerência com a tese central

A tese é: _"O Estado capitalista não proíbe o vício por princípio; administra-o por
cálculo fiscal."_ ([TESE.md](../../PAM/TESE.md))

- O argumento **confirma**, **enfraquece** ou **é neutro** para a tese?
- Se enfraquece: o escritor deve decidir se inclui mesmo assim (fortalece credibilidade)
  ou se reformula.

### Passo 4 — verificar coerência narrativa

Para argumentos implícitos em cenas ou diálogos:

- O personagem saberia isso neste ponto da história?
- A afirmação contradiz algo já estabelecido?
- Requer fonte primária para não ser invenção? Se sim → acionar skill `fonte-primaria`.

### Passo 5 — output estruturado

```
## Validação de argumento — [TÍTULO]

**Claim:** ...
**Grounds:** ...
**Warrant:** ...
**Backing:** ...
**Qualifier:** ...
**Rebuttal 1:** ...
**Rebuttal 2:** ...

**Teste Popper:** ...
**Relação com tese central:** confirma / enfraquece / neutro
**Lacunas detectadas:** ...
**Recomendação:** [APROVADO] / [REVISAR] / [PRECISA FONTE]
```

---

## Regras

- Nunca aprovar argumento sem warrant explícito
- Nunca inventar backing — se não existir autor/teoria verificável, marcar `[PRECISA FONTE]`
- Se o argumento é narrativo (não-acadêmico), validar coerência interna, não rigor científico
- Argumentos físicos ou econômicos precisam passar também pela skill `fonte-primaria`
- Reportar resultado ao escritor antes de qualquer inserção na HISTORIA.md

---

## Referências

- **Toulmin**, S. (1958). _The Uses of Argument_. Cambridge University Press.
- **Popper**, K. (1959). _The Logic of Scientific Discovery_. Hutchinson.
- [METODO.md](../../PAM/METODO.md) — fundação metodológica do projeto
- [TESE.md](../../PAM/TESE.md) — tese central que todos os argumentos devem alimentar
