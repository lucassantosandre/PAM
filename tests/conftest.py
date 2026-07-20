# Adiciona tests/ ao sys.path para que os test files possam
# importar `metrics` diretamente sem prefixo de pacote.
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
