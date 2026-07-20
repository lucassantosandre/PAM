"""
test_repo_structure.py
======================
Testes de integridade estrutural do repositório PAM.
Verifica convenções obrigatórias definidas em AGENTS.md.
Roda via: pytest tests/test_repo_structure.py -v
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
HISTORIA = ROOT / "PAM" / "HISTORIA.md"


# ── Arquivo central ───────────────────────────────────────────────────────────

class TestHistoriaMd:
    def test_exists(self):
        assert HISTORIA.is_file(), "PAM/HISTORIA.md não encontrado"

    def test_has_personagens_section(self):
        content = HISTORIA.read_text(encoding="utf-8")
        assert "## PERSONAGENS" in content, "Seção '## PERSONAGENS' ausente"

    def test_has_a_historia_section(self):
        content = HISTORIA.read_text(encoding="utf-8")
        assert "## A HISTÓRIA" in content, "Seção '## A HISTÓRIA' ausente"

    def test_no_arabic_numerals_in_chapter_headers(self):
        """Capítulos devem usar numeração romana, não arábica."""
        content = HISTORIA.read_text(encoding="utf-8")
        arabic = re.findall(r"####\s+Cap[íi]tulo\s+\d+", content)
        assert not arabic, f"Cabeçalhos de capítulo com numeração arábica: {arabic}"

    def test_no_first_person_narrator(self):
        """O narrador é 'Você' (segunda pessoa) — nunca 'Eu' narrativo na abertura de parágrafo."""
        lines = HISTORIA.read_text(encoding="utf-8").splitlines()
        violations: list[tuple[int, str]] = [
            (i + 1, line.strip())
            for i, line in enumerate(lines)
            if not line.strip().startswith(("#", "|", ">", "-", "*", "```"))
            and re.match(r"^Eu\b", line.strip())
        ]
        assert not violations, (
            f"Narração em primeira pessoa detectada em linha(s): {violations[:3]}"
        )


# ── Sem capítulos em arquivos separados ──────────────────────────────────────

class TestNoOrphanFiles:
    def test_no_orphan_chapter_files_in_pam_dir(self):
        """Conteúdo narrativo deve estar somente em PAM/HISTORIA.md."""
        pam_dir = ROOT / "PAM"
        cap_re = re.compile(r"^cap(i[tí]ulo)?[-_\s]", re.IGNORECASE)
        violations = [
            p.name
            for p in pam_dir.iterdir()
            if cap_re.match(p.name) and p.name != "HISTORIA.md"
        ]
        assert not violations, f"Capítulos em arquivos separados: {violations}"


# ── Infraestrutura obrigatória ────────────────────────────────────────────────

class TestRequiredInfra:
    def test_pr_reviewer_workflow_exists(self):
        assert (ROOT / ".github" / "workflows" / "pr-reviewer.yml").is_file(), (
            ".github/workflows/pr-reviewer.yml não encontrado"
        )

    def test_release_workflow_exists(self):
        assert (ROOT / ".github" / "workflows" / "release.yml").is_file(), (
            ".github/workflows/release.yml não encontrado"
        )

    def test_ethics_file_exists(self):
        assert (ROOT / "ETICA.md").is_file(), "ETICA.md não encontrado na raiz do projeto"

    def test_skills_directory_exists(self):
        assert (ROOT / ".github" / "skills").is_dir(), ".github/skills/ não encontrado"

    def test_agents_md_exists(self):
        assert (ROOT / "AGENTS.md").is_file(), "AGENTS.md não encontrado na raiz"

    def test_tests_directory_exists(self):
        assert (ROOT / "tests").is_dir(), "tests/ não encontrado na raiz"

    def test_requirements_file_exists(self):
        assert (ROOT / "requirements-test.txt").is_file(), (
            "requirements-test.txt não encontrado na raiz"
        )


# ── Convenções de numeração ───────────────────────────────────────────────────

class TestNamingConventions:
    def test_aprofundamentos_use_decimal_notation(self):
        """Aprofundamentos devem usar notação decimal (ex: 5.1, 18.1)."""
        content = HISTORIA.read_text(encoding="utf-8")
        bad_aprof = re.findall(r"####\s+[IVXLCDM]+\.[IVXLCDM]+\s+—", content)
        assert not bad_aprof, f"Aprofundamentos com notação romana: {bad_aprof}"
