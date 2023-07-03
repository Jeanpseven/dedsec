import os

def ascii():
   print("""
/$$$$$$$  /$$$$$$$$ /$$$$$$$   /$$$$$$  /$$$$$$$$  /$$$$$$ 
| $$__  $$| $$_____/| $$__  $$ /$$__  $$| $$_____/ /$$__  $$
| $$  \ $$| $$      | $$  \ $$| $$  \__/| $$      | $$  \__/
| $$  | $$| $$$$$   | $$  | $$|  $$$$$$ | $$$$$   | $$      
| $$  | $$| $$__/   | $$  | $$ \____  $$| $$__/   | $$      
| $$  | $$| $$      | $$  | $$ /$$  \ $$| $$      | $$    $$
| $$$$$$$/| $$$$$$$$| $$$$$$$/|  $$$$$$/| $$$$$$$$|  $$$$$$/
|_______/ |________/|_______/  \______/ |________/ \______/ """


ascii()
                                                            
# Obtém o diretório atual do script
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Obtém a lista de arquivos no diretório atual
arquivos = os.listdir(diretorio_atual)

# Filtra apenas os arquivos com extensão .py
scripts_python = [arquivo for arquivo in arquivos if arquivo.endswith('.py')]

# Imprime os nomes e números dos scripts Python
print("Scripts Python disponíveis:")
for i, script in enumerate(scripts_python, start=1):
    print(f"{i}. {script}")

# Solicita ao usuário o número do script a ser executado
numero_script = input("Digite o número do script a ser executado (0 para sair): ")

# Valida a entrada do usuário
if numero_script.isdigit():
    numero_script = int(numero_script)
    if numero_script >= 1 and numero_script <= len(scripts_python):
        # Executa o script selecionado
        script_selecionado = scripts_python[numero_script - 1]
        comando_execucao = f"python {script_selecionado}"
        os.system(comando_execucao)
    elif numero_script == 0:
        print("Saindo do programa.")
    else:
        print("Número inválido. Saindo do programa.")
else:
    print("Entrada inválida. Saindo do programa.")
