import os
import requests

def ascii():
    # Obtém o nome de usuário local
    username = os.getlogin()

    # Define a cor vermelha para a barra
    red = "\033[48;5;196m"
    reset = "\033[0m"

    # Define o conteúdo do MOTD
    motd_content = f"{red}=================================================={reset}\n" \
                   f"          root@{username}\n" \
                   f"{red}=================================================={reset}\n" \
                   "/ $$$$$$   /$$$$$$$$ /$$$$$$$   /$$$$$$   /$$$$$$$$  /$$$$$$\n" \
                   "| $$__ $$ | $$_____/| $$__  $$ /$$__  $$ | $$_____/ /$$__  $$\n" \
                   "| $$ \\ $$| $$      | $$  \\ $$|$$  \\__/| $$      | $$  \\__/\n" \
                   "| $$  | $$| $$$$$   | $$  |  $$|  $$$$$$ | $$$$$   | $$      \n" \
                   "| $$  | $$| $$__/   | $$  |  $$ \\____ $$| $$__/   | $$      \n" \
                   "| $$  | $$| $$      | $$  |  $$ /$$  \\$$| $$      | $$    $$\n" \
                   "| $$$$$$$/| $$$$$$$$| $$$$$$$/|  $$$$$$/ | $$$$$$$$|  $$$$$$/\n" \
                   "|_______/ |________/|_______/  \\______/ |________/ \\______/  \n"

    # Define o caminho do arquivo MOTD
    motd_path = "/etc/motd"

    print(motd_content)

    # Escreve o conteúdo no arquivo MOTD
    with open(motd_path, "w") as motd_file:
        motd_file.write(motd_content)


def get_repo_list(username, page):
    per_page = 100  # Número máximo de repositórios por página (limite da API)
    url = f"https://api.github.com/users/{username}/repos?page={page}&per_page={per_page}"
    response = requests.get(url)
    repos = response.json()
    return repos


def download_repo(repo_name, download_url):
    response = requests.get(download_url)
    with open(repo_name, 'wb') as f:
        f.write(response.content)
    print(f"Repositório '{repo_name}' baixado com sucesso.")


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

# Obtém o nome de usuário local
username = os.getlogin()

# Chama a função ascii()
ascii()

# Obtém a lista de repositórios do usuário
page = 1
repos = get_repo_list(username, page)

while True:
    # Exibe a lista numerada de repositórios
    print(f"Repositórios disponíveis para {username} (Página {page}):")
    for index, repo in enumerate(repos, start=1):
        print(f"{index}. {repo['name']}")

    print("\nOpções:")
    print("1. Baixar um repositório")
    print("2. Listar mais repositórios")
    print("3. Sair")

    choice = input("Escolha uma opção (1/2/3): ")

    if choice == '1':
        repo_number = input("Digite o número do repositório para baixar: ")
        try:
            repo_index = int(repo_number) - 1
            if 0 <= repo_index < len(repos):
                repo = repos[repo_index]
                repo_name = repo['name']
                repo_download_url = repo['html_url'] + "/archive/master.zip"
                download_repo(repo_name, repo_download_url)
            else:
                print("Número de repositório inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    elif choice == '2':
        page += 1
        repos = get_repo_list(username, page)
        if not repos:
            print("Não há mais repositórios disponíveis.")
            page -= 1

    elif choice == '3':
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")
