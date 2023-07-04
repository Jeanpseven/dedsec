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

                                                            
import os
import shutil

# Função para renomear as pastas removendo o sufixo "-main"
def renomear_pastas():
    script_dir = "scripts"  # Diretório dos scripts
    subpastas = next(os.walk(script_dir))[1]  # Lista as subpastas na pasta

    if not subpastas:
        print("Nenhuma subpasta encontrada na pasta 'scripts'.")
    else:
        for subpasta in subpastas:
            nova_subpasta = subpasta.replace("-main", "")  # Remove o sufixo "-main" do nome da pasta
            subpasta_dir = os.path.join(script_dir, subpasta)
            nova_subpasta_dir = os.path.join(script_dir, nova_subpasta)

            try:
                os.rename(subpasta_dir, nova_subpasta_dir)  # Renomeia a pasta
                print(f"Pasta '{subpasta}' renomeada para '{nova_subpasta}'.")
            except Exception as e:
                print(f"Erro ao renomear a pasta '{subpasta}': {str(e)}")

# Função para listar e executar os scripts nas subpastas da pasta "scripts"
def listar_e_executar_scripts():
    script_dir = "scripts"  # Diretório dos scripts
    subpastas = next(os.walk(script_dir))[1]  # Lista as subpastas na pasta

    if not subpastas:
        print("Nenhuma subpasta encontrada na pasta 'scripts'.")
    else:
        print("Subpastas disponíveis:")
        for i, subpasta in enumerate(subpastas):
            print(f"{i+1}. {subpasta}")

            # Lista os arquivos de script na subpasta
            subpasta_dir = os.path.join(script_dir, subpasta)
            scripts = [f for f in os.listdir(subpasta_dir) if os.path.isfile(os.path.join(subpasta_dir, f))]

            if not scripts:
                print("   Nenhum script encontrado na subpasta.")
            else:
                print("   Scripts disponíveis:")
                for script in scripts:
                    print(f"   - {script}")

    # Solicitar ao usuário para escolher um script
    escolha_subpasta = input("Escolha o número da subpasta: ")

    if escolha_subpasta.isdigit() and int(escolha_subpasta) <= len(subpastas):
        subpasta_escolhida = subpastas[int(escolha_subpasta) - 1]
        subpasta_dir = os.path.join(script_dir, subpasta_escolhida)

        scripts = [f for f in os.listdir(subpasta_dir) if os.path.isfile(os.path.join(subpasta_dir, f))]

        if not scripts:
            print(f"Nenhum script encontrado na subpasta '{subpasta_escolhida}'.")
        else:
            print(f"Scripts disponíveis na subpasta '{subpasta_escolhida}':")
            for i, script in enumerate(scripts):
                print(f"{i+1}. {script}")

            # Solicitar ao usuário para escolher um script
            escolha_script = input("Escolha o número do script para executar (ou '0' para sair): ")

            if escolha_script == "0":
                print("Encerrando o programa.")
            elif escolha_script.isdigit() and int(escolha_script) <= len(scripts):
                script_escolhido = scripts[int(escolha_script) - 1]
                script_path = os.path.join(subpasta_dir, script_escolhido)
                print(f"Executando o script '{script_escolhido}':")
                try:
                    exec(open(script_path).read())
                except Exception as e:
                    print(f"Erro ao executar o script '{script_escolhido}': {str(e)}")
            else:
                print("Opção inválida. Por favor, escolha um número válido.")
    else:
        print("Opção inválida. Por favor, escolha um número válido.")

# Renomear as pastas antes de listar e executar os scripts
renomear_pastas()

# Listar e executar os scripts nas subpastas da pasta "scripts"
listar_e_executar_scripts()

