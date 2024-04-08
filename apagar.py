import subprocess

# Obtém a lista de todas as bibliotecas instaladas
completed_process = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
installed_packages = completed_process.stdout.strip().split("\n")

# Desinstala cada biblioteca individualmente
for package in installed_packages:
    subprocess.run(["pip", "uninstall", "-y", package.split("==")[0]])
