import subprocess
import sys

python_command = sys.executable

# Executa o primeiro arquivo
subprocess.call([python_command, "main.py"])

# Executa o segundo arquivo
subprocess.call([python_command, "app.py"])
