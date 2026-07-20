"""
extract_diff.py
===============
Extrai linhas de prosa adicionadas em PAM/HISTORIA.md no contexto de um PR.

Uso (CI):
  BASE_SHA=<sha> HEAD_SHA=<sha> python tests/extract_diff.py

Saída:
  tests/.diff_text.txt  — texto limpo para análise
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

TARGET_FILE = "PAM/HISTORIA.md"
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


def extract_added_text() -> str:
    """
    Extrai texto adicionado em TARGET_FILE entre BASE_SHA e HEAD_SHA.
    Salva em OUTPUT_FILE e retorna o texto limpo.
    """
    base = os.environ.get("BASE_SHA", "").strip()
    head = os.environ.get("HEAD_SHA", "HEAD").strip()

    # github.event.before é '0000...000' no primeiro push de uma branch nova
    _NULL_SHA = "0" * 40
    if not base or base == _NULL_SHA:
        # tenta merge-base com main primeiro, depois release-candidate
        for ref in ("origin/main", "origin/release-candidate"):
            result = subprocess.run(
                ["git", "merge-base", ref, "HEAD"],
                capture_output=True,
                text=True,
            )
            base = result.stdout.strip()
            if base:
                print(f"[extract_diff] BASE_SHA ausente/nulo — usando merge-base com {ref}: {base[:8]}")
                break

    if not base:
        base = "HEAD~1"
        print("[extract_diff] Usando fallback HEAD~1 como base.")

    diff = subprocess.run(
        ["git", "diff", base, head, "--", TARGET_FILE],
        capture_output=True,
        text=True,
    )

    prose_lines: list[str] = []
    for raw_line in diff.stdout.splitlines():
        if raw_line.startswith("+") and not raw_line.startswith("+++"):
            content = raw_line[1:]
            if _is_prose(content):
                prose_lines.append(content.strip())

    text = "\n".join(prose_lines)
    OUTPUT_FILE.write_text(text, encoding="utf-8")

    print(f"[extract_diff] {len(text.split())} palavras extraídas de {TARGET_FILE}")
    return text


if __name__ == "__main__":
    extracted = extract_added_text()
    if len(extracted.split()) < 50:
        print("[extract_diff] Texto insuficiente — análise não será realizada.")
        sys.exit(0)
