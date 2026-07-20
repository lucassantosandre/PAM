---
name: perfil-escritor
description: >
  Mapeia o perfil estratégico completo do escritor: influências, leitor imaginado,
  temas obsessivos, áreas de crescimento e monitoramento de auto-plágio. Complementa
  a skill estilo (DNA mecânico) com o nível de intenção criativa. Alimenta o ciclo de
  aprendizado contínuo Calíope↔escritor.
argument-hint: "calibrar (leitura + entrevista), ou atualizar (só entrevista), ou revisar (comparar perfil com texto novo)"
---

# Skill: perfil-escritor

Mapeia **quem é o escritor como artista** — não apenas como ele escreve agora
(isso é função de `estilo`), mas o que ele quer escrever, de onde vem, para onde vai,
quem é seu leitor e como crescer sem se perder.

---

## Por que esta skill existe

Escrever um romance longo é um ato de auto-formação. O escritor que começa o Cap. I
não é o mesmo que termina o Cap. XXVII. Sem mapeamento explícito:
- Padrões não examinados se repetem sem intenção (*auto-plágio*)
- Influências entram sem declaração (*plágio inconsciente*)
- O leitor imaginado vaga — e a voz perde destino

A base científica é o **modelo de prática deliberada** (Ericsson & Pool, *Peak*, 2016):
crescimento real exige diagnóstico → prática focada → feedback → ajuste. Esta skill
estrutura esse ciclo para a escrita literária.

---

## Complemento com skill `estilo`

| Skill | Foco | O que gera |
|---|---|---|
| `estilo` | Mecânico | DNA de frase, parágrafo, pontuação, vocabulário |
| `perfil-escritor` | Estratégico | Influências, leitor, temas, crescimento, anti-plágio |

Ambos alimentam `roteiro`. Nenhum substitui o outro.

---

## Workflow — calibração completa

1. **`🎭📖 lendo HISTORIA.md`** — ler Caps. I, V, VII, IX, XV, XVI como amostra representativa
2. **`🎭🔍 verificando memory/{user}/estilo.md`** — integrar DNA mecânico já mapeado
3. **Entrevista** — fazer as perguntas da seção "Entrevista estruturada" abaixo (uma por vez, via `vscode_askQuestions`)
4. **Síntese** — cruzar leitura + respostas
5. **`🎭📝 inserindo em memory/{user}/perfil.md`** — salvar perfil completo
6. **Apresentar** — resumo ao escritor para validação; perguntar o que alterar
7. **Retroalimentar** — skill `roteiro` e skill `estilo` passam a ler `perfil.md` antes de gerar

## Workflow — atualização pontual

1. Ler `memory/{user}/perfil.md` atual
2. Aplicar entrevista só nas dimensões relevantes à sessão
3. Fazer `str_replace` nas seções que mudaram
4. Registrar data da atualização

## Workflow — revisão de texto novo

1. Ler o trecho indicado
2. Cruzar com `perfil.md` → identificar divergências
3. Para cada divergência: *"Isso é escolha consciente ou padrão não-examinado?"*
4. Atualizar perfil se for escolha; sinalizar se for padrão a corrigir

---

## Entrevista estruturada

### Bloco A — Identidade e intenção

1. **"Qual frase resume o que este livro quer fazer com o leitor?"**
   *(não o tema — o efeito. Ex: "quero que ele nunca mais aposte sem pensar nisso")*

2. **"Quem é seu leitor ideal? Descreva a pessoa, não a categoria."**
   *(Ex: "35 anos, periferia de SP, nunca leu Kafka mas assistiu Narcos")*

3. **"O que seu leitor sabe antes de abrir o livro? O que ele deve sentir ao fechar?"**

### Bloco B — Influências

4. **"Cite 3 obras/autores que você quer que ENTREM neste livro conscientemente."**
   *(influências declaradas — o que você toma emprestado e por quê)*

5. **"Cite 2 obras/autores que você quer EVITAR — por risco de influência não-desejada."**
   *(anti-referências — podem ser livros que você ama mas não quer imitar aqui)*

6. **"Tem alguma imagem, cena ou frase que você sabe que escreve sempre de um jeito só — e quer quebrar isso?"**
   *(padrão próprio recorrente — auto-plágio potencial)*

### Bloco C — Crescimento

7. **"O que você estava aprendendo a escrever no começo deste projeto que ainda está aprendendo?"**

8. **"Qual é a cena mais difícil que você já escreveu neste projeto? O que fez ela difícil?"**

9. **"Como você quer que Calíope te dê feedback? (direta, socrática, por comparação, por exemplos?)"**

### Bloco D — Projeto como argumento

10. **"Você quer que alguém leia HISTORIA.md e TESE.md como dois textos do mesmo autor — ou como textos de autores diferentes?"**
    *(decide quanto de "assinatura" coloca nos dois textos)*

---

## Dimensões do perfil — estrutura do arquivo

```yaml
# memory/{user}/perfil.md
# Gerado por skill perfil-escritor
# Atualizar a cada sessão longa — registrar data

projeto:
  titulo: "O Voto Final"
  genero: roman à thèse / distopia literária
  lingua: português brasileiro
  tese_central: >
    O Estado capitalista não proíbe o vício por princípio,
    mas o administra por cálculo fiscal.

intencao_do_livro:
  efeito_no_leitor: ""  # o que deve sentir ao fechar
  frase_resumo: ""      # uma frase que resume o projeto inteiro

leitor_imaginado:
  descricao: ""         # pessoa concreta, não categoria
  o_que_sabe_antes: []
  o_que_leva_depois: []

influencias_declaradas:
  - obra: ""
    autor: ""
    o_que_empresta: ""  # específico — um padrão, uma técnica, uma voz

anti_referencias:
  - obra: ""
    autor: ""
    por_que_evitar: ""

temas_obsessivos:
  - ""  # os temas que aparecem sem você convocar

padroes_proprios_recorrentes:
  # imagens, frases, estruturas que o escritor usa sempre — monitorar para não repetir
  - padrao: ""
    onde_aparece: []
    status: "ativo" | "monitorar" | "aposentar"

areas_de_crescimento:
  - habilidade: ""
    estado_atual: ""    # uma frase honesta
    estado_desejado: ""
    como_praticar: ""   # o que Calíope vai focar nessa área

como_receber_feedback:
  estilo: ""            # direta / socrática / por comparação / por exemplos
  o_que_ajuda: []
  o_que_trava: []

dois_textos_ou_um_autor:
  resposta: ""          # "dois textos do mesmo autor" ou "assinaturas diferentes"
  implicacao: ""        # o que isso muda na geração

historico_de_crescimento:
  # log de evolução — alimentado a cada sessão
  - data: ""
    habilidade: ""
    evidencia: ""       # cap/trecho onde o avanço é visível
    observacao: ""

notas_do_escritor: []
ultima_atualizacao: ""
```

---

## Monitoramento de auto-plágio e influências

### Por que monitorar

Harold Bloom (1973, *The Anxiety of Influence*) argumenta que todo escritor produz
em relação a predecessores — consciente ou inconscientemente. O risco duplo aqui:

1. **Plágio inconsciente de outros:** uma imagem, estrutura ou frase absorvida de
   leitura anterior que emerge sem citação e sem consciência.
2. **Auto-plágio:** repetição de próprios padrões — a mesma metáfora, o mesmo tipo
   de fechamento de capítulo, a mesma voz de personagem secundário.

### Como Calíope monitora

- A cada novo capítulo ou aprofundamento gerado: comparar contra `padroes_proprios_recorrentes`
- Se padrão aparece > 3 vezes sem intenção declarada: sinalizar
- Registro em `historico_de_crescimento` com data e evidência

### Referências bibliográficas desta dimensão

- **Bloom, Harold** (1973). *The Anxiety of Influence: A Theory of Poetry*. Oxford UP.
- **Leech, Geoffrey; Short, Mick** (2007). *Style in Fiction: A Linguistic Introduction
  to English Fictional Prose*. Pearson. — análise sistemática de estilo literário

---

## O ciclo de aprendizado Calíope ↔ escritor

Baseado no modelo de **aprendizagem cognitiva** (Collins, Brown & Newman, 1989,
*Cognitive Apprenticeship*):

```
MODELAGEM    → Calíope gera um trecho a partir do perfil
COACHING     → escritor lê, reage, aponta o que funcionou/quebrou
SCAFFOLDING  → Calíope adapta próxima geração ao feedback
FADING       → Calíope intervém menos; escritor guia mais
ARTICULAÇÃO  → escritor explica suas escolhas (consolida aprendizado)
REFLEXÃO     → Calíope compara estado atual com perfil — o que mudou?
```

Para ativar um ciclo completo:
1. Gerar trecho (via `roteiro`)
2. Escritor dá feedback explícito ("essa frase soa estranha porque..." / "aqui estava certo")
3. Calíope atualiza `perfil.md` `historico_de_crescimento` + `padroes_proprios_recorrentes`
4. Próxima geração incorpora o ajuste

---

## Regra de ouro

O perfil é um instrumento de liberdade, não de restrição.
Quando o escritor quebra conscientemente um padrão, ele evolui.
Quando quebra sem perceber, ele se repete.
A diferença está na consciência — e é isso que esta skill rastreia.

---

## Referências científicas

- **Ericsson, K.A.; Pool, R.** (2016). *Peak: Secrets from the New Science of Expertise*.
  Houghton Mifflin. — prática deliberada, feedback, zona de desenvolvimento
- **Collins, A.; Brown, J.S.; Newman, S.E.** (1989). Cognitive Apprenticeship:
  Teaching the Crafts of Reading, Writing, and Mathematics. In: *Knowing, Learning,
  and Instruction* (L. Resnick, ed.). — modelagem, coaching, scaffolding
- **Bloom, Harold** (1973). *The Anxiety of Influence: A Theory of Poetry*. Oxford UP.
  — dinâmica de influência literária
- **Barthes, Roland** (1975). *The Pleasure of the Text*. Hill & Wang.
  — leitor como co-produtor de sentido; plaisir vs jouissance
- **Leech, G.; Short, M.** (2007). *Style in Fiction*. Pearson.
  — análise linguística sistemática de estilo literário

---

## Ligações

- Skill [`estilo`](../estilo/SKILL.md) — DNA mecânico (frases, parágrafos, pontuação)
- Skill [`roteiro`](../roteiro/SKILL.md) — usa perfil + estilo antes de gerar
- Skill [`grill`](../grill/SKILL.md) — pressiona ideias; usa perfil como referência de voz
- [METODO.md](../../PAM/METODO.md) — fundação epistemológica do projeto
- [memory/{user}/perfil.md](../../memory/) — arquivo gerado por esta skill
