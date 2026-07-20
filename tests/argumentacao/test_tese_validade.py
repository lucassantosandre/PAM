"""
tests/argumentacao/test_tese_validade.py
=========================================
Três testes argumentativos básicos que verificam se PAM/TESE.md constitui
uma tese *válida* — não uma tautologia, falsificável e com estrutura mínima
de argumento acadêmico.

Estes testes **não provam que a tese é verdadeira**; provam que ela está
construída corretamente como argumento — contestável, ancorada em evidência
e não circular.

Via PR: qualquer contestação à tese pode ser feita como pull request.
O pipeline roda estes testes automaticamente: se a mudança introduzir uma
lacuna argumentativa (remover contrapontos, apagar evidências, criar
circularidade), o CI reprova e o argumento do autor não passa.

Categorias
----------
- TestAntiTautologia     : a tese não é circular nem trivialmente verdadeira
- TestFalsificabilidade  : a tese pode ser refutada (critério de Popper, 1959)
- TestEstruturaToulmin   : claim / grounds / warrant / rebuttal presentes
                           (Toulmin, 1958)

Referências metodológicas
--------------------------
- Popper, K. (1959). *The Logic of Scientific Discovery*. Hutchinson.
- Toulmin, S. (1958). *The Uses of Argument*. Cambridge University Press.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest

# tests/argumentacao/ → tests/ → repo root
ROOT = Path(__file__).resolve().parent.parent.parent
TESE = ROOT / "PAM" / "TESE.md"


def _load() -> str:
    """Carrega TESE.md — falha com mensagem clara se o arquivo não existir."""
    if not TESE.is_file():
        pytest.fail(
            f"TESE.md não encontrado em {TESE}. "
            "O arquivo deve estar em PAM/TESE.md."
        )
    return TESE.read_text(encoding="utf-8")


# ─────────────────────────────────────────────────────────────────────────────
# 1. Anti-tautologia
#
#    Uma tautologia é verdadeira por definição — não pode ser refutada por
#    nenhuma evidência porque não diz nada novo sobre o mundo.
#    Exemplo de tautologia: "O Estado faz o que é fiscalmente vantajoso
#    para o Estado" (a conclusão está dentro da premissa).
#
#    Para não ser tautológica, a tese deve:
#      (a) citar dados empíricos externos à teoria (não derivados dela);
#      (b) ter uma conclusão que acrescenta conteúdo novo em relação
#          ao que foi declarado na abertura.
# ─────────────────────────────────────────────────────────────────────────────


class TestAntiTautologia:

    def test_cita_dado_empirico_externo(self):
        """
        Uma tese circular dispensa evidência — é verdadeira por definição.
        Para não ser tautológica, TESE.md deve conter ao menos 3 dados
        verificáveis externos: anos históricos, valores monetários, percentuais
        ou quantificações geográficas/estatísticas.

        Exemplos válidos presentes no arquivo: '2024', 'US$ 13,7 bi', '38 estados'.
        Se este teste falhar, o argumento central não tem sustentação empírica
        — apenas teórica — o que o torna circular.
        """
        text = _load()
        empirical = re.findall(
            r"\b(?:19|20)\d{2}\b"            # anos (1900–2099)
            r"|\bUS\$\s*[\d,.]+\s*\w*"       # valores em dólar
            r"|\d+\s*%"                       # percentuais
            r"|\d+\s+estado[s]?"             # quantificação geográfica
            r"|\d+\s+bilh",                  # valores por extenso
            text,
            re.IGNORECASE,
        )
        assert len(empirical) >= 3, (
            f"TESE.md tem menos de 3 dados empíricos verificáveis "
            f"(encontrados: {empirical}). "
            "Uma tese sem dados externos é circular: sua conclusão decorre apenas "
            "das próprias premissas teóricas, sem contato com o mundo real."
        )

    def test_conclusao_acrescenta_conteudo_novo(self):
        """
        Em tautologias, a conclusão é uma paráfrase da premissa — ela
        'fecha o círculo' sem sair dele.

        Este teste extrai os termos da 'Tese central' e os da 'Conclusão'
        e verifica que a conclusão introduz ao menos 5 palavras-chave novas
        (≥5 caracteres, em português) que não constavam na declaração inicial.

        Se a conclusão repetir apenas o que a abertura declarou, o argumento
        não *desenvolveu* nada — foi circular.
        """
        text = _load()

        claim_block = re.search(
            r"##\s+Tese\s+central\s*\n+(.*?)(?=\n##|\Z)",
            text,
            re.IGNORECASE | re.DOTALL,
        )
        conclusion_block = re.search(
            r"##\s+\d+[\.\s]*Conclus[ãa]o\s*\n+(.*?)(?=\n##|\Z)",
            text,
            re.IGNORECASE | re.DOTALL,
        )
        if not claim_block or not conclusion_block:
            pytest.skip(
                "Seção 'Tese central' ou 'Conclusão' ausente — "
                "TestEstruturaToulmin.test_claim_declarado_explicitamente cobrirá isso."
            )

        # palavras portuguesas com ≥ 5 caracteres (exclui stopwords curtas)
        _words = lambda s: set(
            re.findall(r"\b[a-záéíóúàâêôãõüç]{5,}\b", s.lower())
        )
        claim_words = _words(claim_block.group(1))
        conclusion_words = _words(conclusion_block.group(1))

        new_in_conclusion = conclusion_words - claim_words
        assert len(new_in_conclusion) >= 5, (
            f"Conclusão não acrescenta conteúdo novo em relação à tese central. "
            f"Termos exclusivos da conclusão: {sorted(new_in_conclusion)!r}. "
            "Se a conclusão repete a abertura, o argumento é circular."
        )


# ─────────────────────────────────────────────────────────────────────────────
# 2. Falsificabilidade (Popper, 1959)
#
#    Uma afirmação não falsificável não é uma tese científica — é um dogma.
#    Para ser falsificável, a tese deve:
#      (a) apresentar ao menos uma objeção legítima que, se verdadeira,
#          a refutaria;
#      (b) responder a essa objeção (réplica) — mostrando por que a tese
#          sobrevive, mesmo que modificada.
#
#    Obs: o próprio TESE.md reconhece isso: "Esta é uma afirmação discutível
#    (alguém pode contestá-la — ver §5), e é isso que a qualifica como tese."
# ─────────────────────────────────────────────────────────────────────────────


class TestFalsificabilidade:

    def test_possui_contrapontos_explicitos(self):
        """
        A tese deve nomear ao menos uma objeção que, se provada, a refutaria.
        Uma tese que não admite objeções é imune à evidência — portanto dogmática.

        Indicador: seção cujo título mencione 'contraponto', 'objeção',
        'limite', 'crítica' ou 'refuta'.
        """
        text = _load()
        section = re.search(
            r"##\s+\d+[\.\s]*.*(contraponto|obje[çc]|limite|cr[íi]tica|refuta)",
            text,
            re.IGNORECASE,
        )
        assert section, (
            "Não encontrada seção de contrapontos ou objeções em TESE.md. "
            "Pelo critério de Popper, uma tese sem refutação possível "
            "é dogma, não argumento. Adicione uma seção '## N. Contrapontos e limites'."
        )

    def test_replica_enfrenta_os_contrapontos(self):
        """
        Listar objeções sem respondê-las equivale a concedê-las.
        TESE.md deve conter linguagem de réplica — mostrando por que a tese
        sobrevive às objeções apresentadas, mesmo que em forma modificada.

        Palavras-chave de réplica: 'réplica', 'sobrevive', 'ainda assim',
        'mesmo assim', 'permanece', 'concedendo', 'tese modificada'.
        """
        text = _load()
        rebuttal = re.search(
            r"\b(r[ée]plica|sobrevive|ainda\s+assim|mesmo\s+assim|"
            r"permanece|persiste|concedendo|tese\s+(?:ainda|sobrevive|modificada))\b",
            text,
            re.IGNORECASE,
        )
        assert rebuttal, (
            "TESE.md lista contrapontos mas não apresenta réplica explícita. "
            "Objeções não respondidas implicam que elas refutam a tese. "
            "Adicione uma 'Réplica' após cada contraponto, explicando por que a "
            "tese sobrevive (possivelmente em forma modificada)."
        )


# ─────────────────────────────────────────────────────────────────────────────
# 3. Estrutura toulminiana mínima (Toulmin, 1958)
#
#    Todo argumento válido decompõe-se em:
#      - Claim    : a afirmação central (o que se defende)
#      - Grounds  : as evidências que sustentam o Claim
#      - Warrant  : o princípio causal que conecta Grounds ao Claim
#      - Rebuttal : as condições em que o Claim seria falso
#
#    Uma tese que omite qualquer um desses elementos tem lacuna argumentativa:
#    ela pode estar certa, mas não está *argumentada*.
# ─────────────────────────────────────────────────────────────────────────────


class TestEstruturaToulmin:

    def test_claim_declarado_explicitamente(self):
        """
        O Claim é a afirmação central — deve estar numa seção identificável,
        não apenas inferido do título do documento.
        Exige: cabeçalho '## Tese central' (ou variante).
        """
        text = _load()
        assert re.search(r"##\s+Tese\s+central", text, re.IGNORECASE), (
            "Não encontrada seção 'Tese central' (Claim no modelo de Toulmin). "
            "Adicione '## Tese central' com a afirmação principal em destaque."
        )

    def test_grounds_incluem_casos_historicos(self):
        """
        Os Grounds são as evidências. Para esta tese, evidência = casos históricos
        documentados que percorreram o ciclo proibição → legalização → tributação.

        Ao menos 2 dos 3 casos canônicos devem estar presentes:
          - Álcool / Lei Seca (EUA, 1920–1933)
          - Maconha / Cannabis (CO/WA, 2012–)
          - Apostas esportivas (Murphy v. NCAA, 2018–)

        Se este teste falhar, a afirmação não tem respaldo histórico —
        é apenas teoria sem evidência (Grounds ausentes).
        """
        text = _load()
        patterns = [
            r"\bálcool\b|\blei\s+seca\b",
            r"\bmaconha\b|\bcannabis\b",
            r"\baposta[s]?\b|\bmurphy\b|\bpaspa\b",
        ]
        found = [p for p in patterns if re.search(p, text, re.IGNORECASE)]
        assert len(found) >= 2, (
            f"Grounds insuficientes: {len(found)} de 3 casos históricos encontrados. "
            "Ao menos 2 casos (álcool/Lei Seca, maconha/cannabis, apostas/Murphy) "
            "são necessários como evidência histórica (Grounds)."
        )

    def test_warrant_explica_mecanismo_causal(self):
        """
        O Warrant é o princípio que torna a evidência relevante para a conclusão.
        Para esta tese: o mecanismo fiscal ('proibir → gerar mercado negro →
        legalizar → tributar').

        Sem Warrant, os casos históricos ficam desconectados da teoria —
        o argumento diz 'aconteceu' mas não explica 'por que era esperado'.
        Exige: seção cujo título mencione 'mecanismo', 'lógica', 'ciclo'
        ou 'por que'.
        """
        text = _load()
        warrant = re.search(
            r"##\s+\d+[\.\s]*.*(mecanismo|lógica|ciclo|como\s+funciona|por\s+que)",
            text,
            re.IGNORECASE,
        )
        assert warrant, (
            "Não encontrada seção de mecanismo causal (Warrant no modelo de Toulmin). "
            "Sem warrant, não há princípio que ligue os casos históricos à conclusão "
            "teórica — o argumento fica incompleto. "
            "Adicione seção '## N. O mecanismo: ...' explicando o ciclo causal."
        )
