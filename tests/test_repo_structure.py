"""
test_repo_structure.py
======================
Testes de integridade estrutural do repositório PAM.
Verifica convenções obrigatórias definidas em AGENTS.md.
Roda via: pytest tests/test_repo_structure.py -v
"""
import os
import re
import pytest

# Raiz do repositório — um nível acima de tests/
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HISTORIA = os.path.join(ROOT, "PAM", "HISTORIA.md")


# ── Arquivo central ───────────────────────────────────────────────────────────

class TestHistoriaMd:
    def test_exists(self):
        assert os.path.isfile(HISTORIA), "PAM/HISTORIA.md não encontrado"

    def test_has_personagens_section(self):
        with open(HISTORIA, encoding="utf-8") as f:
            content = f.read()
        assert "## PERSONAGENS" in content, "Seção '## PERSONAGENS' ausente"

    def test_has_a_historia_section(self):
        with open(HISTORIA, encoding="utf-8") as f:
            content = f.read()
        assert "## A HISTÓRIA" in content, "Seção '## A HISTÓRIA' ausente"

    def test_no_arabic_numerals_in_chapter_headers(self):
        """Capítulos devem usar numeração romana, não arábica."""
        with open(HISTORIA, encoding="utf-8") as f:
            content = f.read()
        arabic = re.findall(r"####\s+Cap[íi]tulo\s+\d+", content)
        assert not arabic, f"Cabeçalhos de capítulo com numeração arábica: {arabic}"

    def test_no_first_person_narrator(self):
        """O narrador é 'Você' (segunda pessoa) — nunca 'Eu' narrativo na abertura de parágrafo."""
        with open(HISTORIA, encoding="utf-8") as f:
            lines = f.readlines()
        prose_with_first_person = [
            (i + 1, line.strip())
            for i, line in enumerate(lines)
            if not line.strip().startswith(("#", "|", ">", "-", "*", "```"))
            and re.match(r"^Eu\b", line.strip())
        ]
        assert not prose_with_first_person, (
            f"Narração em primeira pessoa detectada em linha(s): "
            f"{prose_with_first_person[:3]}"
        )


# ── Sem capítulos em arquivos separados ──────────────────────────────────────

class TestNoOrphanFiles:
    def test_no_orphan_chapter_files_in_pam_dir(self):
        """Conteúdo narrativo deve estar somente em PAM/HISTORIA.md."""
        pam_dir = os.path.join(ROOT, "PAM")
        cap_re = re.compile(r"^cap(i[tí]ulo)?[-_\s]", re.IGNORECASE)
        violations = [
            f for f in os.listdir(pam_dir)
            if cap_re.match(f) and f != "HISTORIA.md"
        ]
        assert not violations, f"Capítulos em arquivos separados: {violations}"


# ── Infraestrutura obrigatória ────────────────────────────────────────────────

class TestRequiredInfra:
    def test_pr_reviewer_workflow_exists(self):
        wf = os.path.join(ROOT, ".github", "workflows", "pr-reviewer.yml")
        assert os.path.isfile(wf), ".github/workflows/pr-reviewer.yml não encontrado"

    def test_release_workflow_exists(self):
        wf = os.path.join(ROOT, ".github", "workflows", "release.yml")
        assert os.path.isfile(wf), ".github/workflows/release.yml não encontrado"

    def test_ethics_file_exists(self):
        etica = os.path.join(ROOT, "ETICA.md")
        assert os.path.isfile(etica), "ETICA.md não encontrado na raiz do projeto"

    def test_skills_directory_exists(self):
        skills = os.path.join(ROOT, ".github", "skills")
        assert os.path.isdir(skills), ".github/skills/ não encontrado"

    def test_agents_md_exists(self):
        agents = os.path.join(ROOT, "AGENTS.md")
        assert os.path.isfile(agents), "AGENTS.md não encontrado na raiz"

    def test_tests_directory_exists(self):
        assert os.path.isdir(os.path.join(ROOT, "tests")), "tests/ não encontrado na raiz"

    def test_requirements_file_exists(self):
        req = os.path.join(ROOT, "requirements-test.txt")
        assert os.path.isfile(req), "requirements-test.txt não encontrado na raiz"


# ── Convenções de numeração ───────────────────────────────────────────────────

class TestNamingConventions:
    def test_aprofundamentos_use_decimal_notation(self):
        """Aprofundamentos devem usar notação decimal (ex: 5.1, 18.1)."""
        with open(HISTORIA, encoding="utf-8") as f:
            content = f.read()
        bad_aprof = re.findall(r"####\s+[IVXLCDM]+\.[IVXLCDM]+\s+—", content)
        assert not bad_aprof, f"Aprofundamentos com notação romana: {bad_aprof}"
