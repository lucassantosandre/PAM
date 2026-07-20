"""
extract_diff.py
===============
Extrai toda a prosa narrativa de PAM/HISTORIA.md para análise de autoria.

Analisa sempre o arquivo completo — não depende de PR nem de comparação
entre commits. Roda em qualquer push, em qualquer branch.

Uso:
  python tests/extract_diff.py

Saída:
  tests/.diff_text.txt  — texto limpo para análise por run_analysis.py
"""
from __future__ import annotations

import sys
from pathlib import Path

TARGET_FILE = Path(__file__).resolve().parent.parent / "PAM" / "HISTORIA.md"
OUTPUT_FILE = Path(__file__).parent / ".diff_text.txt"

# Prefixos de linha Markdown que NÃO são prosa narrativa
_SKIP_PREFIXES = ("#", "|", "```", "---", "===", "!!!", "[[", ">")


def _is_prose(line: str) -> bool:
    """Retorna True se a linha contiver prosa narrativa válida."""
    stripped = line.strip()
    if not stripped:
        return False
    for prefix in _SKIP_PREFIXES:
        if stripped.startswith(prefix):
            return False
    return len(stripped.split()) >= 4


def extract_prose() -> str:
    """
    Lê PAM/HISTORIA.md completo e extrai todas as linhas de prosa narrativa.
    Salva em OUTPUT_FILE e retorna o texto limpo.
    """
    if not TARGET_FILE.is_file():
        print(f"[extract_prose] Arquivo não encontrado: {TARGET_FILE}", file=sys.stderr)
        OUTPUT_FILE.write_text("", encoding="utf-8")
        return ""

    prose_lines: list[str] = []
    for line in TARGET_FILE.read_text(encoding="utf-8").splitlines():
        if _is_prose(line):
            prose_lines.append(line.strip())

    text = "\n".join(prose_lines)
    OUTPUT_FILE.write_text(text, encoding="utf-8")

    word_count = len(text.split())
    print(f"[extract_prose] {word_count} palavras extraídas de {TARGET_FILE.name}")
    return text


if __name__ == "__main__":
    extracted = extract_prose()
    if len(extracted.split()) < 50:
        print("[extract_prose] Prosa insuficiente no arquivo — verifique PAM/HISTORIA.md.")
        sys.exit(1)
