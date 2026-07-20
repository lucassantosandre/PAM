"""Shared configuration for the PAM test suite."""
from __future__ import annotations

import sys
from pathlib import Path

# Torna tests/ importável diretamente (para `import metrics` etc.)
sys.path.insert(0, str(Path(__file__).parent))
