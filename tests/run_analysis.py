"""
run_analysis.py
===============
Lê o texto extraído pelo extract_diff.py, executa as métricas de autoria
e gera tests/report.md para ser postado como comentário no PR.

Uso:
  python tests/run_analysis.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from metrics import compute_metrics, verdict  # noqa: E402

_TESTS_DIR = Path(__file__).parent
DIFF_TEXT_FILE = _TESTS_DIR / ".diff_text.txt"
REPORT_FILE = _TESTS_DIR / "report.md"


def _bar(value: float, width: int = 20) -> str:
    filled = round(min(max(value, 0.0), 1.0) * width)
    return "█" * filled + "░" * (width - filled)


def _format_report(metrics: dict, label: str, emoji: str) -> str:
    ai_pct = int(metrics["ai_probability"] * 100)
    B = metrics["burstiness"]
    ttr = metrics["vocabulary_richness_ttr"]
    rep = metrics["repetition_index"]
    pat = metrics["ai_patterns"]

    b_note = "↑ Variado (humano)" if B > 0.5 else "↓ Uniforme (IA)"
    t_note = "↑ Diverso" if ttr > 0.65 else ("→ Neutro" if ttr > 0.45 else "↓ Repetitivo")
    r_note = "↑ Repetitivo (IA)" if rep > 0.10 else "↓ Variado (humano)"
    p_note = "↑ Detectados" if pat > 0.30 else "↓ Poucos"

    return f"""## 🎭 Revisor de Autoria — PAM

### Resultado: {emoji} {label}

```
Probabilidade de IA: [{_bar(metrics['ai_probability'])}] {ai_pct}%
```

| Métrica | Valor | Interpretação |
|---|---|---|
| Burstiness (variância de frases) | `{B:.3f}` | {b_note} |
| Riqueza lexical (TTR) | `{ttr:.3f}` | {t_note} |
| Repetição de 4-gramas | `{rep:.3f}` | {r_note} |
| Padrões PT-IA | `{pat:.3f}` | {p_note} |
| **Probabilidade IA** | **`{metrics['ai_probability']:.3f}`** | {emoji} {label} |
| Palavras analisadas | `{metrics['word_count']}` | — |

> ⚠️ **Este revisor é heurístico** — métricas estatísticas indicativas, não determinísticas.
> Consulte [`ETICA.md`](ETICA.md) para o código de conduta completo sobre uso de IA.
>
> Um resultado elevado **não bloqueia** o push — serve para consciência e transparência.

---
*PAM Authorship Reviewer v1.0 · Analisa `PAM/HISTORIA.md` completo a cada push*
"""


def _format_skip_report() -> str:
    return """## 🎭 Revisor de Autoria — PAM

> **Prosa insuficiente** em `PAM/HISTORIA.md` (menos de 50 palavras detectadas).
> Nenhuma avaliação realizada.

*PAM Authorship Reviewer v1.0*
"""


def main() -> None:
    if not DIFF_TEXT_FILE.exists():
        report = _format_skip_report()
    else:
        text = DIFF_TEXT_FILE.read_text(encoding="utf-8")

        metrics = compute_metrics(text)

        if "error" in metrics:
            report = _format_skip_report()
        else:
            label, emoji = verdict(metrics["ai_probability"])
            report = _format_report(metrics, label, emoji)
            print(
                f"[run_analysis] Probabilidade IA: {metrics['ai_probability']:.1%} — {label}"
            )

    REPORT_FILE.write_text(report, encoding="utf-8")
    print(f"[run_analysis] Relatório salvo em: {REPORT_FILE}")


if __name__ == "__main__":
    main()
