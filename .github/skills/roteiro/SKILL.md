---
name: roteiro
description: >
  Gera capítulos, cenas e aprofundamentos estruturados para "O Voto Final" usando os
  templates do projeto e o padrão de estilo calibrado. Modo `capitulo` para capítulos
  principais, modo `aprofundamento` para POVs paralelos (📍 ou 🔎).
argument-hint: "Ex: 'Cap. XXVIII — modo capitulo' ou 'Aprof. 27.1 📍 — POV do algoritmo às 8h03'"
---

# Roteiro

Gera conteúdo narrativo estruturado para "O Voto Final" usando os templates do projeto
e respeitando o DNA de escrita estabelecido.

# Inputs

| Campo         | Descrição                                                     |
| ------------- | ------------------------------------------------------------- |
| `modo`        | `capitulo` ou `aprofundamento`                                |
| `numero`      | Romano para cap. (ex: XXVIII), decimal para aprof. (ex: 27.1) |
| `titulo`      | Título proposto ou palavra-chave orientadora                  |
| `resumo`      | O que acontece — frase ou bullet points                       |
| `personagens` | Quem aparece — emojis-marca e nomes                           |
| `ancora`      | Cap. ou evento que este conteúdo expande ou segue             |
| `tipo_aprof`  | Somente no modo aprofundamento: `📍` ou `🔎`                  |

# Workflow — modo: capitulo

1. `🎭📖 lendo HISTORIA.md` — ler último capítulo para capturar ritmo e momentum.
2. `🎭📖 lendo PERSONAGENS` — verificar emojis-marca dos personagens ativos.
3. Carregar template: `.github/skills/templates/capitulo.md`.
4. Carregar perfil de estilo: `memory/{user}/estilo.md` (se existir).
5. Preencher template com inputs + estilo calibrado.
6. Gerar o capítulo em segunda pessoa, parágrafos curtos, metáforas econômicas naturais.
7. Adicionar nota italic ao final se o capítulo conecta à Fundamentação.
8. `🎭📝 inserindo em HISTORIA.md` — inserir ANTES da seção `## APROFUNDAMENTOS`.

# Workflow — modo: aprofundamento

1. `🎭📖 lendo HISTORIA.md` — verificar que o capítulo-âncora existe.
2. Determinar numeração: verificar aprofundamentos existentes, usar próximo disponível.
3. Classificar: `📍` (gancho que será puxado) ou `🔎` (paralelo puro, opcional).
4. Carregar template: `.github/skills/templates/aprofundamento.md`.
5. Gerar o POV no tempo/lugar especificado — pode ser terceira pessoa se for outro POV.
6. Inserir na seção `### Expansões do Capítulo {romano}` correta.
7. Atualizar a **Linha do tempo** em APROFUNDAMENTOS se o aprof. tiver selo de tempo novo.
8. Atualizar a tabela `### Expansões do Capítulo {X}` — criar a seção se não existir.

# Regras de geração

| Regra                | Detalhe                                                                  |
| -------------------- | ------------------------------------------------------------------------ |
| Segunda pessoa       | Narrador principal = "Você". Aprofundamentos podem usar terceira pessoa. |
| Parágrafos curtos    | 2–4 linhas. Sem floreio. Estilo jornalístico/punchy.                     |
| Metáforas            | Financeiras, físicas e cotidianas — integradas, nunca explicadas.        |
| Emojis na narração   | Zero. Só em notificações dentro de blocos `> citação`.                   |
| Emojis de personagem | Só no primeiro aparecimento importante da cena.                          |
| Nota italic          | `> *...*` quando conecta à fundamentação ou a outro arquivo.             |
| Hora/local           | Aprofundamentos abrem sempre com `> *{hora} — {lugar}.*`                 |

# Verificações pós-geração

- [ ] Número romano correto no título
- [ ] Nenhum emoji de personagem usado em excesso
- [ ] Segunda pessoa mantida (ou terceira só em aprofundamentos de outro POV)
- [ ] Nota italic presente se há conexão com fundamentação
- [ ] Inserido no lugar correto em HISTORIA.md
- [ ] Linha do tempo atualizada se necessário
