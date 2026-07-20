"""
test_metrics.py
===============
Testes unitários para as métricas de detecção de autoria (tests/metrics.py).
Roda via: pytest tests/test_metrics.py -v
"""
from __future__ import annotations

import pytest
from metrics import (
    sentence_burstiness,
    vocabulary_richness,
    repetition_index,
    portuguese_ai_patterns,
    compute_metrics,
    verdict,
)

# ── Textos de referência ──────────────────────────────────────────────────────

TEXTO_HUMANO = """
Você parou na calçada. A chuva caía em diagonal, batendo nos vidros dos carros
com um ruído que lembrava dedos impacientes. Às três da manhã a rua estava vazia.
Nunca silenciosa. Havia sempre aquele zumbido das máquinas de apostas nas janelas,
acesas, com alguém dentro que não dormia.

Seu irmão sabia o que estava em jogo — isso você nunca duvidou. O que ficava girando
na sua cabeça, enquanto esperava o ônibus que não vinha, era se ele havia escolhido
ou simplesmente caído naquele sistema que prometia recompensa e entregava dependência.
O frio cortava. Você não sabia o que fazer com isso. A calçada molhada refletia
um neon vermelho piscando no ritmo de alguém que já desistiu de dormir.
"""

TEXTO_IA = (
    "Além disso, é importante notar que o sistema de apostas representa uma forma de controle social. "
    "Por outro lado, os trabalhadores são profundamente afetados por essas estruturas de dominação. "
    "No entanto, é possível que mudanças ocorram no contexto social mais amplo. "
    "Em suma, a situação é imensamente complexa para todos os envolvidos nas decisões. "
    "Sendo assim, é importante destacar que as soluções devem ser abrangentes e sistemáticas. "
    "Portanto, não há dúvida que uma análise mais profunda e abrangente se faz necessária. "
    "Além disso, por outro lado, é importante ressaltar que a realidade é profundamente desafiadora. "
    "Nesse sentido, pode-se dizer que o problema exige atenção imediata dos responsáveis políticos. "
    "Por fim, sendo assim, é fundamental que medidas sejam adotadas com celeridade e profundidade. "
    "Em suma, além disso, no entanto, a questão permanece imensamente em aberto e profundamente complexa."
)


# ── Testes de métricas individuais ───────────────────────────────────────────

class TestSentenceBurstiness:
    def test_human_higher_than_ai(self):
        h = sentence_burstiness(TEXTO_HUMANO)
        a = sentence_burstiness(TEXTO_IA)
        assert h > a, f"Esperado humano ({h:.3f}) > IA ({a:.3f})"

    def test_returns_float_in_range(self):
        score = sentence_burstiness(TEXTO_HUMANO)
        assert 0.0 <= score <= 1.0

    def test_short_text_returns_half(self):
        score = sentence_burstiness("Frase curta.")
        assert score == 0.5


class TestVocabularyRichness:
    def test_returns_float_in_range(self):
        ttr = vocabulary_richness(TEXTO_HUMANO)
        assert 0.0 <= ttr <= 1.0

    def test_repetitive_text_lower_ttr(self):
        repetitive = "gato gato gato gato gato gato gato gato gato gato"
        varied = "gato cachorro pássaro peixe cavalo leão tigre urso raposa lobo"
        assert vocabulary_richness(repetitive) < vocabulary_richness(varied)

    def test_empty_text_returns_half(self):
        assert vocabulary_richness("") == 0.5


class TestRepetitionIndex:
    def test_ai_higher_than_human(self):
        h = repetition_index(TEXTO_HUMANO)
        a = repetition_index(TEXTO_IA)
        assert a >= h, f"Esperado IA ({a:.3f}) >= humano ({h:.3f})"

    def test_returns_float_in_range(self):
        score = repetition_index(TEXTO_HUMANO)
        assert 0.0 <= score <= 1.0

    def test_short_text_returns_zero(self):
        assert repetition_index("ab") == 0.0


class TestPortugueseAiPatterns:
    def test_ai_text_higher_than_human(self):
        h = portuguese_ai_patterns(TEXTO_HUMANO)
        a = portuguese_ai_patterns(TEXTO_IA)
        assert a > h, f"Esperado IA ({a:.3f}) > humano ({h:.3f})"

    def test_returns_float_in_range(self):
        score = portuguese_ai_patterns(TEXTO_HUMANO)
        assert 0.0 <= score <= 1.0

    def test_empty_text_returns_zero(self):
        assert portuguese_ai_patterns("") == 0.0


# ── Testes de compute_metrics ─────────────────────────────────────────────────

class TestComputeMetrics:
    def test_all_keys_present(self):
        m = compute_metrics(TEXTO_HUMANO)
        assert "error" not in m
        for key in (
            "burstiness",
            "vocabulary_richness_ttr",
            "repetition_index",
            "ai_patterns",
            "ai_probability",
            "word_count",
        ):
            assert key in m, f"Chave ausente: {key}"

    def test_short_text_returns_error(self):
        m = compute_metrics("Texto curto demais.")
        assert "error" in m

    def test_probability_in_valid_range(self):
        m = compute_metrics(TEXTO_HUMANO)
        assert 0.0 <= m["ai_probability"] <= 1.0

    def test_human_lower_probability_than_ai(self):
        mh = compute_metrics(TEXTO_HUMANO)
        ma = compute_metrics(TEXTO_IA)
        assert mh["ai_probability"] < ma["ai_probability"], (
            f"Humano {mh['ai_probability']:.3f} deveria ser < IA {ma['ai_probability']:.3f}"
        )

    def test_word_count_matches(self):
        m = compute_metrics(TEXTO_HUMANO)
        expected = len(TEXTO_HUMANO.split())
        assert m["word_count"] == expected


# ── Testes de verdict ─────────────────────────────────────────────────────────

class TestVerdict:
    @pytest.mark.parametrize(
        "prob, expected_substring",
        [
            (0.10, "Humano"),
            (0.34, "Humano"),
            (0.35, "Misto"),
            (0.50, "Misto"),
            (0.64, "Misto"),
            (0.65, "IA"),
            (0.90, "IA"),
        ],
    )
    def test_label_thresholds(self, prob: float, expected_substring: str):
        label, _ = verdict(prob)
        assert expected_substring in label, (
            f"prob={prob}: '{label}' não contém '{expected_substring}'"
        )

    @pytest.mark.parametrize("prob", [0.0, 0.35, 0.65, 1.0])
    def test_returns_tuple(self, prob: float):
        result = verdict(prob)
        assert isinstance(result, tuple) and len(result) == 2
