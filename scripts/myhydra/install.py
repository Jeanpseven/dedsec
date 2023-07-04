import subprocess
import sys

print("fazendo a instalação correta do script...")

def install_pip():
    try:
        # Baixa o arquivo get-pip.py
        subprocess.run(['curl', 'https://bootstrap.pypa.io/get-pip.py', '-o', 'get-pip.py'])
        print("pip baixado com sucesso!")

        # Executa o arquivo get-pip.py para instalar o pip
        subprocess.run([sys.executable, 'get-pip.py'])
        print("pip instalado com sucesso!")
    except Exception as e:
        print("Erro ao instalar o pip:", e)

def install_requirements():
    try:
        # Instala as dependências do arquivo requirements.txt
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
        print("Dependências instaladas com sucesso!")
    except Exception as e:
        print("Erro ao instalar as dependências:", e)

def main():
    try:
        # Verifica se o pip está instalado
        result = subprocess.run(['pip', '--version'], capture_output=True, text=True)
        if result.returncode != 0:
            print("pip não encontrado. Instalando o pip...")
            install_pip()
        else:
            print("pip encontrado.")

        install_requirements()
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    main()
