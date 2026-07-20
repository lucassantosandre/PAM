---
name: estilo
description: >
  Analisa o DNA de escrita do escritor a partir dos capítulos existentes em HISTORIA.md
  e salva um perfil de estilo em memory/{user}/estilo.md. Esse perfil alimenta todas
  as skills de geração para manter consistência de voz.
argument-hint: "Calibrar estilo completo, ou analisar trecho específico? (ex: 'calibrar', ou 'analisar Cap. XXVI')"
---

# Estilo

Captura e mantém o DNA narrativo do escritor — para que toda geração de conteúdo seja
consistente com a voz estabelecida nos capítulos existentes.

# Workflow — calibração completa

1. `🎭📖 lendo HISTORIA.md` — ler amostra representativa (Caps. I, V, IX, XVIII, XXVI, XXVII).
2. Analisar cada dimensão do perfil (ver abaixo).
3. Salvar perfil em `memory/{user}/estilo.md`.
4. Apresentar o perfil ao escritor para validação/ajuste.
5. O perfil passa a ser lido automaticamente pela skill `roteiro` antes de qualquer geração.

# Workflow — análise pontual

1. Ler o trecho indicado.
2. Comparar com o perfil existente em `memory/{user}/estilo.md`.
3. Reportar divergências e perguntar se o padrão deve ser incorporado.

# Dimensões do perfil de estilo

```yaml
# memory/{user}/estilo.md
# Gerado por skill estilo — atualizar a cada sessão longa

voz: segunda pessoa ("Você")
tom: direto, seco, sem floreio — jornalístico-literário
perspectiva_narrativa: subjetiva mas contida (sem ornamentos emocionais explícitos)

abertura_de_capitulo:
  padrao: hora exata + ação em andamento, OU notificação de celular
  exemplo: "22h17. A final da Copa estava empatada na prorrogação."

fechamento_de_capitulo:
  padrao: frase de efeito seca, OU nota italic em itálico, OU silêncio/pergunta aberta
  exemplo: "O mundo não acaba hoje."

comprimento_de_paragrafo:
  tipico: 2-4 linhas
  maximo: 6 linhas (exceção para acumulação intencional)

metaforas_dominantes:
  - financeiras (spread, liquidação, posição, portfólio)
  - físicas (entropia, sistema fechado, temperatura)
  - cotidianas (copo d'água, foto plastificada, Celta com amasso)

vocabulario_chave: [] # preencher após calibração

padroes_de_pontuacao:
  - travessão narrativo para fala (— Não. — ele disse.)
  - ponto final seco após revelação
  - reticências evitadas (usadas só em suspense genuíno)
  - itálico para termos do sistema (liquidação de posição, spread)

elementos_evitar:
  - adjetivos em excesso
  - explicar a metáfora depois de usá-la
  - onisciência emocional (dizer o que o personagem sente em vez de mostrar)
  - heroísmo explícito (a resistência é pequena e cara — nunca grandiosa)

padrao_de_dialogo:
  - travessão, sem aspas
  - fala curta, direta
  - narrador não interpreta a fala — só reporta

notas_do_escritor: [] # observações adicionadas manualmente pelo escritor
```

# Regra de ouro

O perfil é um espelho — não uma prisão. Se o escritor deliberadamente quebra um padrão,
anotar como exceção intencional, não corrigir.
