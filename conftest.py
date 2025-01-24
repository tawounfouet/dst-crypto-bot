import sys
from pathlib import Path

# Ajoute le répertoire racine du projet au PYTHONPATH
root_dir = Path(__file__).parent
sys.path.append(str(root_dir))
