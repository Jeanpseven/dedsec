import subprocess
import requests
from urllib.parse import urljoin
import ascii

ascii.exibir_ascii_art()

def banner():
    print("===============================")
    print("   VERIFICAÇÃO DE DIRETÓRIOS")
    print("===============================")

def carregar_diretorios():
    with open("lista_diretorios.txt", "r") as file:
        diretorios = file.readlines()
        diretorios = [diretorio.strip() for diretorio in diretorios]
    return diretorios

def procurar_diretorios_robots(site):
    url_robots = urljoin(site, "robots.txt")
    response = requests.get(url_robots)

    if response.status_code == 200:
        linhas = response.text.split("\n")
        diretorios_permitidos = []
        diretorios_desautorizados = []

        for linha in linhas:
            linha = linha.strip()
            if linha.startswith("Allow:"):
                diretorio = linha.split("Allow:")[1].strip()
                diretorios_permitidos.append(diretorio)
            elif linha.startswith("Disallow:"):
                diretorio = linha.split("Disallow:")[1].strip()
                diretorios_desautorizados.append(diretorio)

        print("[+] Diretórios permitidos encontrados no robots.txt:")
        for diretorio in diretorios_permitidos:
            print(urljoin(site, diretorio))
            analisar_exploit_db(diretorio)
        
        print("\n[-] Diretórios desautorizados encontrados no robots.txt:")
        for diretorio in diretorios_desautorizados:
            print(urljoin(site, diretorio))
            analisar_exploit_db(diretorio)
    elif response.status_code == 404:
        print("[-] Arquivo robots.txt não encontrado.")
    else:
        print(f"[?] Erro ao acessar o arquivo robots.txt. Código de status: {response.status_code}")

def analisar_exploit_db(diretorio):
    # Implemente a pesquisa no Exploit Database aqui

    print(f"    [-] Nenhuma exploração encontrada para {diretorio}.")

def verificar_diretorios(site, diretorios):
    for diretorio in diretorios:
        url = urljoin(site, diretorio)
        response = requests.get(url)

        if response.status_code == 200:
            print(f"[+] Diretório encontrado: {url}")
            analisar_exploit_db(diretorio)
        elif response.status_code == 403:
            print(f"[-] Acesso proibido: {url}")
        elif response.status_code == 404:
            print(f"[-] Diretório não encontrado: {url}")
        else:
            print(f"[?] Código de status desconhecido ({response.status_code}): {url}")

def analisar_portas_e_servicos(site):
    # Implemente a verificação de portas e serviços aqui

    print("    [-] Verificação de portas e serviços não implementada.")

def verificar_com_nikto(site):
    print("\n[+] Verificando com Nikto:")

    # Executar o comando do Nikto no terminal
    command = f"nikto -h {site}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Exibir a saída do Nikto
    print(output.decode())

    if error:
        print(f"[!] Ocorreu um erro ao executar o Nikto: {error.decode()}")

def main():
    banner()
    site = input("Digite o site para verificar os diretórios: ")
    diretorios = carregar_diretorios()
    verificar_diretorios(site, diretorios)
    procurar_diretorios_robots(site)
    analisar_portas_e_servicos(site)
    verificar_com_nikto(site)

if __name__ == "__main__":
    main()
