---
name: fonte-primaria
description: >
  Gerencia fontes primárias do projeto PAM — consulta, valida e registra referências
  de livros, artigos e documentos internos. Garante que nenhuma citação entre no projeto
  sem verificação. Única skill autorizada a adicionar referências bibliográficas.
argument-hint: "Nome da fonte, autor ou tema a verificar/adicionar (ex: 'Prigogine', 'Murphy v. NCAA', 'dados apostas Colorado')"
---

# Fonte Primária

Garante rastreabilidade e integridade de todas as fontes do projeto — de Karl Marx a
Clausius, de decisões judiciais a dados públicos.

# Mapa de fontes internas

| Arquivo                       | Tema                    | Fontes cobertas                                                                                                   |
| ----------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `PAM/PAM/ENTROPIA.md`         | Física da entropia      | Clausius 1850/1865, Boltzmann 1872, Kelvin 1851, Schrödinger 1944, Wiener 1948, Shannon 1948, Prigogine 1979/1984 |
| `PAM/PAM/CALCULO-MARXISTA.md` | Economia crítica        | Marx (_Das Kapital_), Harvey, Streeck                                                                             |
| `PAM/PAM/METODO.md`           | Método científico       | Toulmin (argumento), Popper (falsificabilidade)                                                                   |
| `PAM/PAM/TESE.md`             | Tese tributária         | Fórmulas $R=t\cdot\theta\cdot H$ e $E=s+\theta\alpha v$; evidências históricas                                    |
| `PAM/PAM/HISTORIA.md` §7      | Fontes da fundamentação | AGA, _Murphy v. NCAA_, dados cannabis CO, _O Capital_, Harvey, Streeck                                            |

# Workflow — verificar fonte existente

1. Buscar autor/título nos arquivos listados acima.
2. Reportar: arquivo, seção, citação existente.
3. Se não encontrada → declarar ausência e oferecer opção de adicionar.

# Workflow — adicionar nova fonte

1. Solicitar do escritor (se não fornecido): autor, título completo, publicação, ano, URL ou
   ISBN.
2. Verificar se já existe em algum arquivo interno (evitar duplicata).
3. Formatar na citação padrão do projeto (Chicago adaptado):
   ```
   **Sobrenome, Nome**. *Título*. Cidade: Editora, Ano.
   ```
   Para artigos:
   ```
   **Sobrenome, Nome**. "Título do artigo." *Nome da Revista* Vol, n. N (Ano): pp–pp.
   ```
4. Adicionar no arquivo de fonte mais apropriado.
5. Se usada na tese → atualizar FUNDAMENTAÇÃO §7 de HISTORIA.md.

# Workflow — citar no texto

Quando o escritor precisar citar uma fonte dentro de um arquivo:

1. Verificar se a fonte está registrada nos arquivos internos.
2. Fornecer a citação formatada para inserção.
3. Adicionar link `ver ENTROPIA.md, §X` ou similar quando a fonte já está documentada.

# Regra de ouro

**Nunca inventar ou completar dados bibliográficos.** Se faltar autor, ano, volume ou
página, reportar o gap e perguntar ao escritor antes de registrar. Uma citação incompleta
com aviso é melhor do que uma citação fabricada.

# Fontes em espera (não criadas)

Os arquivos abaixo são referenciados no projeto mas ainda não existem — fontes que
entrariam neles precisam ser registradas em TESE.md §7 provisoriamente:

| Arquivo                 | Tema esperado                                               |
| ----------------------- | ----------------------------------------------------------- |
| `PAM/PAM/ARCO-FINAL.md` | Bastidores da Casa, plano de saída, lore do limiar ENTROPIA |
| `PAM/PAM/ADI.md`        | Dossier da ADI Predictstreet                                |
