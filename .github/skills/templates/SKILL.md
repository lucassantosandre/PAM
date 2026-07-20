---
name: templates
description: >
  Gerencia a biblioteca de templates reutilizáveis do projeto PAM. Consulta, preenche
  e evolui os templates de capítulo, aprofundamento e personagem. Templates crescem com
  a história — retroalimentados conforme novos padrões emergem.
argument-hint: "Qual template? (capitulo / aprofundamento / personagem) ou 'listar' para ver todos"
---

# Templates

Biblioteca de templates reutilizáveis para "O Voto Final". Cada template define a estrutura
canônica do elemento narrativo — preenchível por variáveis `{{NOME_VARIAVEL}}`.

# Biblioteca

| Template       | Arquivo                                      | Uso                              |
| -------------- | -------------------------------------------- | -------------------------------- |
| Capítulo       | `.github/skills/templates/capitulo.md`       | Capítulos principais da história |
| Aprofundamento | `.github/skills/templates/aprofundamento.md` | POVs paralelos 📍 ou 🔎          |
| Personagem     | `.github/skills/templates/personagem.md`     | Entrada de novo personagem       |

# Variáveis padrão

| Variável                 | Descrição                                                             |
| ------------------------ | --------------------------------------------------------------------- |
| `{{PARTE}}`              | Número romano da Parte (ex: IX)                                       |
| `{{NUMERO}}`             | Número romano do capítulo (ex: XXVIII) ou decimal do aprof. (ex: 5.4) |
| `{{TITULO}}`             | Título do capítulo ou aprofundamento                                  |
| `{{ANCORA_TEMPORAL}}`    | Hora e local (ex: `8h03. O celular apita.`)                           |
| `{{PERSONAGENS_ATIVOS}}` | Emojis-marca dos personagens presentes                                |
| `{{TIPO_APROF}}`         | 📍 ou 🔎                                                              |
| `{{BEAT_ABERTURA}}`      | Primeiro parágrafo — o que acontece agora                             |
| `{{BEAT_CLIMAX}}`        | A virada ou revelação central                                         |
| `{{BEAT_FECHAMENTO}}`    | O que o narrador/POV carrega ao sair                                  |
| `{{NOTA_ITALIC}}`        | Referência à fundamentação (texto após `> *`)                         |
| `{{EMOJI_MARCA}}`        | Emoji do novo personagem                                              |
| `{{PAPEL}}`              | Uma linha sobre o papel do personagem                                 |

# Workflow — consultar template

1. Ler o arquivo de template correspondente.
2. Apresentar ao escritor com as variáveis em destaque.
3. Preencher as variáveis com base nos inputs do escritor.
4. Entregar o template preenchido para revisão antes de inserir.

# Workflow — evoluir template

Quando um novo padrão narrativo surgir e se repetir ≥ 2 vezes:

1. Identificar o padrão (ex: "capítulo com notificação de múltiplas telas simultâneas").
2. Criar variante no arquivo de template existente como `## Variante: {nome}`.
3. Documentar quando usar a variante.
4. Atualizar a tabela da Biblioteca acima.

# Workflow — criar template novo

Quando o escritor pedir um tipo de conteúdo sem template existente:

1. Identificar a estrutura recorrente do tipo.
2. Criar arquivo `.github/skills/templates/{nome}.md`.
3. Definir variáveis necessárias.
4. Adicionar à tabela da Biblioteca.
