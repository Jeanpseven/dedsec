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

                                                            
# Função para listar os scripts na pasta "scripts"
def listar_scripts():
    script_dir = "scripts"  # Diretório dos scripts
    scripts = os.listdir(script_dir)  # Lista os arquivos na pasta

    if not scripts:
        print("Nenhum script encontrado na pasta.")
    else:
        print("Scripts disponíveis:")
        for i, script in enumerate(scripts):
            print(f"{i+1}. {script}")

# Função para executar um script específico
def executar_script(script):
    script_dir = "scripts"  # Diretório dos scripts
    script_path = os.path.join(script_dir, script)  # Caminho completo do script

    if os.path.isfile(script_path):
        try:
            exec(open(script_path).read())
        except Exception as e:
            print(f"Erro ao executar o script {script}: {str(e)}")
    else:
        print(f"O script {script} não existe.")

# Listar os scripts disponíveis
listar_scripts()

# Solicitar ao usuário para escolher um script
escolha = input("Escolha o número do script para executar (ou '0' para sair): ")

if escolha == "0":
    print("Encerrando o programa.")
else:
    scripts = os.listdir("scripts")
    if escolha.isdigit() and int(escolha) <= len(scripts):
        script = scripts[int(escolha) - 1]
        print(f"Executando o script {script}:")
        executar_script(script)
    else:
        print("Opção inválida. Por favor, escolha um número válido.")

