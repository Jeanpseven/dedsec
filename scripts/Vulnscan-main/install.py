import subprocess

def install_nmap():
    print("[+] Instalando o Nmap...")
    subprocess.call(["apt-get", "install", "-y", "nmap"])

def install_nikto():
    print("[+] Instalando o Nikto...")
    subprocess.call(["apt-get", "install", "-y", "nikto"])

def install_dependencies():
    install_nmap()
    install_nikto()

def main():
    print("===============================")
    print("   INSTALAÇÃO DE DEPENDÊNCIAS")
    print("===============================")
    install_dependencies()
    print("[+] Instalação concluída com sucesso.")

if __name__ == "__main__":
    main()
