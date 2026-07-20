"""
PAM Authorship Metrics
======================
Métricas estatísticas para estimar probabilidade de geração por IA
em texto literário em português brasileiro.

Nenhuma dependência externa — apenas stdlib Python 3.9+.
"""
import re
import math
from collections import Counter
from typing import Dict, List, Tuple


# ── Tokenização ───────────────────────────────────────────────────────────────

def _split_sentences(text: str) -> List[str]:
    """Quebra texto em frases usando pontuação terminal."""
    text = re.sub(r"\n+", " ", text)
    raw = re.split(r"(?<=[.!?…])\s+", text.strip())
    return [s.strip() for s in raw if len(s.split()) >= 3]


def _tokenize(text: str) -> List[str]:
    """Extrai tokens de palavras ignorando números e pontuação."""
    return re.findall(
        r"\b[a-záéíóúàâêôãõüçA-ZÁÉÍÓÚÀÂÊÔÃÕÜÇ]+\b",
        text,
    )


# ── Métricas individuais ──────────────────────────────────────────────────────

def sentence_burstiness(text: str) -> float:
    """
    Mede a variação no comprimento das frases.

    Texto humano tende a ser 'bursty' (alta variância).
    Texto de IA tende a ser uniforme (baixa variância).

    Retorna 0.0–1.0 onde 1.0 = máxima variância (mais humano).
    """
    sentences = _split_sentences(text)
    if len(sentences) < 5:
        return 0.5  # inconclusivo

    lengths = [len(s.split()) for s in sentences]
    mean = sum(lengths) / len(lengths)
    if mean == 0:
        return 0.5

    variance = sum((l - mean) ** 2 for l in lengths) / len(lengths)
    std = math.sqrt(variance)

    # Coeficiente de burstiness B ∈ [-1, 1]
    # B > 0 → bursty (humano); B < 0 → regular (IA)
    B = (std - mean) / (std + mean) if (std + mean) > 0 else 0.0
    return (B + 1.0) / 2.0  # normaliza para [0, 1]


def vocabulary_richness(text: str) -> float:
    """
    Type-Token Ratio (TTR): palavras únicas / total de palavras.

    Proxy de diversidade lexical. IA tende a uma faixa específica de TTR.
    Retorna 0.0–1.0.
    """
    tokens = _tokenize(text.lower())
    if not tokens:
        return 0.5
    return len(set(tokens)) / len(tokens)


def repetition_index(text: str, n: int = 4) -> float:
    """
    Fração de n-gramas que aparecem mais de uma vez.

    IA tende a repetir padrões de palavras.
    Retorna 0.0–1.0 onde maior = mais repetitivo = mais IA.
    """
    tokens = _tokenize(text.lower())
    if len(tokens) < n * 3:
        return 0.0

    ngrams = [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]
    counts = Counter(ngrams)
    repeated = sum(c for c in counts.values() if c > 1)
    return min(repeated / len(ngrams), 1.0)


# Padrões de transição e frases comuns em texto PT gerado por IA
_PT_AI_PATTERNS = [
    r"\bainda assim\b",
    r"\balém disso\b",
    r"\bpor outro lado\b",
    r"\bno entanto\b",
    r"\bé importante (?:notar|destacar|ressaltar|mencionar)\b",
    r"\bpara concluir\b",
    r"\bem suma\b",
    r"\bprofundamente\b",
    r"\bimensamente\b",
    r"\bde certa forma\b",
    r"\bpode-se (?:dizer|afirmar|concluir)\b",
    r"\bnão há dúvida\b",
    r"\bpor fim\b",
    r"\bsendo assim\b",
    r"\bnesse sentido\b",
    r"\bé fundamental que\b",
    r"\bcom efeito\b",
]


def portuguese_ai_patterns(text: str) -> float:
    """
    Densidade de padrões típicos de texto PT gerado por IA.

    Retorna 0.0–1.0 onde maior = mais padrões de IA detectados.
    """
    if not text.strip():
        return 0.0

    word_count = max(len(text.split()), 1)
    total_matches = sum(
        len(re.findall(p, text, re.IGNORECASE)) for p in _PT_AI_PATTERNS
    )
    # Normaliza: >10 ocorrências por 1000 palavras → score máximo
    density = total_matches / (word_count / 1000)
    return min(density / 10.0, 1.0)


# ── Combinação e veredito ─────────────────────────────────────────────────────

def compute_metrics(text: str) -> Dict[str, float]:
    """
    Computa todas as métricas de autoria para o texto fornecido.

    Retorna dict com todas as métricas e 'ai_probability' (0.0–1.0).
    Retorna {'error': str} se o texto for insuficiente (< 50 palavras).
    """
    words = text.split()
    if len(words) < 50:
        return {"error": "Texto insuficiente — mínimo 50 palavras para análise"}

    B = sentence_burstiness(text)
    ttr = vocabulary_richness(text)
    rep = repetition_index(text)
    pat = portuguese_ai_patterns(text)

    # TTR → contribuição para probabilidade de IA
    if ttr > 0.70:
        ai_from_ttr = 0.10
    elif ttr < 0.45:
        ai_from_ttr = 0.70
    else:
        ai_from_ttr = 0.40

    # Combinação ponderada
    ai_probability = (
        0.40 * (1.0 - B)
        + 0.30 * rep
        + 0.20 * pat
        + 0.10 * ai_from_ttr
    )
    ai_probability = round(min(max(ai_probability, 0.0), 1.0), 3)

    return {
        "burstiness": round(B, 3),
        "vocabulary_richness_ttr": round(ttr, 3),
        "repetition_index": round(rep, 3),
        "ai_patterns": round(pat, 3),
        "ai_probability": ai_probability,
        "word_count": len(words),
    }


def verdict(ai_probability: float) -> Tuple[str, str]:
    """
    Retorna (rótulo, emoji) para a probabilidade de IA fornecida.

    Limiares:
      < 0.35 → Provavelmente Humano
      0.35–0.65 → Misto / Assistido por IA
      > 0.65 → Provável Geração por IA
    """
    if ai_probability < 0.35:
        return "Provavelmente Humano", "✅"
    elif ai_probability < 0.65:
        return "Misto / Assistido por IA", "⚠️"
    else:
        return "Provável Geração por IA", "🤖"
