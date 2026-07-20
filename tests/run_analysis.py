"""
run_analysis.py
===============
Lê o texto extraído pelo extract_diff.py, executa as métricas de autoria
e gera tests/report.md para ser postado como comentário no PR.

Uso:
  python tests/run_analysis.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from metrics import compute_metrics, verdict  # noqa: E402

DIFF_TEXT_FILE = os.path.join(os.path.dirname(__file__), ".diff_text.txt")
REPORT_FILE = os.path.join(os.path.dirname(__file__), "report.md")


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
> Um resultado elevado **não bloqueia** o PR — serve para consciência e transparência.

---
*PAM Authorship Reviewer v1.0 · Roda automaticamente em PRs para `release-candidate`*
"""


def _format_skip_report() -> str:
    return """## 🎭 Revisor de Autoria — PAM

> **Texto novo insuficiente** para análise (menos de 50 palavras adicionadas em `PAM/HISTORIA.md`).
> Nenhuma avaliação realizada neste PR.

*PAM Authorship Reviewer v1.0*
"""


def main() -> None:
    if not os.path.exists(DIFF_TEXT_FILE):
        report = _format_skip_report()
    else:
        with open(DIFF_TEXT_FILE, encoding="utf-8") as f:
            text = f.read()

        metrics = compute_metrics(text)

        if "error" in metrics:
            report = _format_skip_report()
        else:
            label, emoji = verdict(metrics["ai_probability"])
            report = _format_report(metrics, label, emoji)
            print(
                f"[run_analysis] Probabilidade IA: {metrics['ai_probability']:.1%} — {label}"
            )

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"[run_analysis] Relatório salvo em: {REPORT_FILE}")


if __name__ == "__main__":
    main()
