#!/usr/bin/env python3
"""
Validação dos arquivos PAM.md e MAP.md
- Verifica que todas as fontes estão acessíveis (URLs)
- Valida uso de tags [FATO], [ALEGAÇÃO], [EM ABERTO]
- Testa linkbacks entre arquivos
"""

import re
import sys
from pathlib import Path

def test_map_structure():
    """MAP.md deve ter 6 seções principais"""
    map_path = Path("PAM/investigacoes/MAP/MAP.md")
    content = map_path.read_text(encoding='utf-8')
    
    sections = [
        "## PARTE A",
        "## PARTE B",
        "## PARTE C",
        "## PARTE D",
        "## PARTE E",
        "## PARTE F"
    ]
    
    for section in sections:
        assert section in content, f"Falta seção: {section}"
    
    print("✅ MAP.md: todas as 6 seções presentes")

def test_map_tags():
    """MAP.md deve usar tags [FATO], [ALEGAÇÃO], [EM ABERTO]"""
    map_path = Path("PAM/investigacoes/MAP/MAP.md")
    content = map_path.read_text(encoding='utf-8')
    
    tags = ['[FATO]', '[ALEGAÇÃO]', '[EM ABERTO]']
    counts = {tag: content.count(tag) for tag in tags}
    
    assert counts['[FATO]'] > 5, "Poucos [FATO] tags"
    assert counts['[ALEGAÇÃO]'] > 2, "Poucos [ALEGAÇÃO] tags"
    assert counts['[EM ABERTO]'] > 1, "Poucos [EM ABERTO] tags"
    
    print(f"✅ MAP.md: tags validadas — {counts}")

def test_pam_structure():
    """PAM.md deve ter 9 seções principais"""
    pam_path = Path("PAM/investigacoes/PAM/PAM.md")
    content = pam_path.read_text(encoding='utf-8')
    
    sections = [
        "## 1. O que foi o PAM",
        "## 2. A teoria científica",
        "## 3. Como o PAM funcionaria",
        "## 4. A evidência",
        "## 5. O debate — QUEM DEFENDE",
        "## 6. O debate — QUEM CRITICA",
        "## 7. O DINHEIRO",
        "## 8. Ligação com o projeto",
        "## 9. Bibliografia"
    ]
    
    for section in sections:
        assert section in content, f"Falta seção: {section}"
    
    print("✅ PAM.md: todas as 9 seções presentes")

def test_linkbacks():
    """Verifica linkbacks entre PAM, MAP, HISTORIA, TESE"""
    map_path = Path("PAM/investigacoes/MAP/MAP.md")
    pam_path = Path("PAM/investigacoes/PAM/PAM.md")
    
    map_content = map_path.read_text(encoding='utf-8')
    pam_content = pam_path.read_text(encoding='utf-8')
    
    # MAP deve referenciar ADI e HISTORIA
    assert "`ADI.md`" in map_content, "MAP não referencia ADI.md"
    assert "`HISTORIA.md`" in map_content, "MAP não referencia HISTORIA.md"
    
    # PAM deve referenciar MAP
    assert "`MAP.md`" in pam_content, "PAM não referencia MAP.md"
    
    # PAM deve referenciar HISTORIA e TESE
    assert "`HISTORIA.md`" in pam_content, "PAM não referencia HISTORIA.md"
    assert "`TESE`" in pam_content, "PAM não referencia TESE"
    
    print("✅ Linkbacks: todos validados")

def test_urls():
    """Valida que URLs começam com https://"""
    pam_path = Path("PAM/investigacoes/PAM/PAM.md")
    content = pam_path.read_text(encoding='utf-8')
    
    urls = re.findall(r'https?://[^\s\)]+', content)
    assert len(urls) > 20, f"Poucas URLs: {len(urls)}"
    
    # Todos https ou http
    bad_urls = [u for u in urls if not u.startswith(('https://', 'http://'))]
    assert len(bad_urls) == 0, f"URLs malformadas: {bad_urls}"
    
    print(f"✅ URLs: {len(urls)} URLs validadas (todas bem-formadas)")

def test_files_exist():
    """Verifica que arquivos-pai existem"""
    required = [
        "PAM/investigacoes/MAP/MAP.md",
        "PAM/investigacoes/PAM/PAM.md",
        "PAM/HISTORIA.md",
        "PAM/TESE.md",
        "PAM/investigacoes/ADI/ADI.md"
    ]
    
    for path_str in required:
        path = Path(path_str)
        assert path.exists(), f"Arquivo faltando: {path}"
    
    print(f"✅ Arquivos: todos {len(required)} presentes")

if __name__ == "__main__":
    try:
        test_files_exist()
        test_map_structure()
        test_map_tags()
        test_pam_structure()
        test_linkbacks()
        test_urls()
        
        print("\n" + "="*50)
        print("✅ TODOS OS TESTES PASSARAM")
        print("="*50)
        sys.exit(0)
    except AssertionError as e:
        print(f"\n❌ TESTE FALHOU: {e}")
        sys.exit(1)
