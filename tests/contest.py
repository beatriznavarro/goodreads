# tests/conftest.py
import sys
import os

# Obtém o caminho absoluto do diretório do conftest.py
current_dir = os.path.dirname(os.path.abspath(__file__))
# Adiciona o diretório do projeto ao sys.path
sys.path.append(os.path.join(current_dir, "..", "projeto"))
