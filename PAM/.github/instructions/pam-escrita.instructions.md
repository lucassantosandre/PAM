---
applyTo: "PAM/PAM/**/*.md"
---

# Regras de escrita — O Voto Final

Instruções aplicadas automaticamente a todos os arquivos Markdown dentro de `PAM/PAM/`.

## Estrutura de capítulos

- **Partes** usam `### PARTE {ROMANO} — {TÍTULO}` (H3)
- **Capítulos** usam `#### Capítulo {ROMANO} — {TÍTULO}` (H4)
- **Números de capítulo**: sempre em algarismos romanos maiúsculos (I, II, III … XXVII)
- Inline: `Cap. XII`, nunca `Cap. 12`

## Voz narrativa

- Narrador principal em **segunda pessoa**: "Você acorda", "Você vê"
- Aprofundamentos de outros POVs podem usar terceira pessoa
- Parágrafos curtos: 2–4 linhas; máximo 6 (apenas em acumulação intencional)
- Sem ornamentos emocionais explícitos — mostrar, não nomear sentimentos

## Emojis — regras estritas

- **Emoji-marca de personagem**: só no primeiro aparecimento de peso de cada cena
- **Emojis de notificação** (📱 ⚙️ sistema): somente dentro de blocos `> citação`
- **Nenhum emoji** no texto corrido de narração ou diálogo

## Nota italic de fundamentação

Quando um capítulo ou aprofundamento conecta com a fundamentação teórica, fechar com:
```
> *{nota conectando ao conceito ou ao arquivo de referência}*
```

## Aprofundamentos

- Numeração decimal: `{cap}.{sequência}` (ex: `5.2`, `18.1`)
- Tipo obrigatório no título: `📍` (gancho que será puxado) ou `🔎` (paralelo puro)
- Âncora temporal obrigatória: `> *{hora} — {local}.*`
- Seção de inserção: `### Expansões do Capítulo {romano}` dentro de `## APROFUNDAMENTOS`

## Nome do irmão

- O nome próprio do irmão aparece **somente no Capítulo XIV**
- Em todo o restante do texto: "o irmão", "ele", nunca o nome próprio

## Diálogo

- Travessão em lugar de aspas: `— Texto. — resposta.`
- Fala curta, direta
- Narrador não interpreta emoções das falas

## Metáforas

- Financeiras, físicas e cotidianas — integradas naturalmente, **nunca explicadas** em seguida
- Exemplos canônicos: spread, liquidação, posição, portfólio, entropia, temperatura

## Fórmulas matemáticas

- Inline: `$formula$`
- Bloco: `$$formula$$`
- Fontes físicas/econômicas com citação completa (Chicago adaptado) via skill `fonte-primaria`

## Língua

- Português brasileiro em todo o texto narrativo
- Termos técnicos em inglês apenas quando são termos do sistema (ex: NÃO, SIM como votos)
- Sem mistura casual de línguas no texto corrido

## Arquivo único

- `HISTORIA.md` é o único arquivo de narrativa principal — não criar capítulos em arquivos separados
- Outros arquivos (ENTROPIA.md, CALCULO-MARXISTA.md, etc.) são documentação de suporte
