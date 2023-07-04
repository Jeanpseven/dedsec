import subprocess

def iniciar_vnc_acompanhamento():
    print("Iniciando o servidor VNC para acompanhamento...")
    subprocess.run(["vncserver", ":0", "-geometry", "1280x720", "-depth", "24", "-localhost"])

def abrir_vnc_acompanhado():
    ip = input("Digite o IP do servidor VNC a ser acompanhado (padrão: localhost): ") or "localhost"
    porta = input("Digite a porta do servidor VNC a ser acompanhado (padrão: 5901): ") or "5901"

    print(f"Abrindo o servidor VNC em {ip}:{porta} para acompanhamento...")
    subprocess.run(["vncviewer", f"{ip}:{porta}"])

def parar_vnc():
    print("Parando o servidor VNC...")
    subprocess.run(["vncserver", "-kill", ":0"])

# Loop principal do script
while True:
    print("""
    === Script do Servidor VNC ===

    Opções:
    1. Iniciar o servidor VNC para acompanhamento(listener)
    2. Abrir um servidor VNC para ser acompanhado
    3. Parar o servidor VNC
    4. Sair
    """)
    
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        iniciar_vnc_acompanhamento()
    elif opcao == "2":
        abrir_vnc_acompanhado()
    elif opcao == "3":
        parar_vnc()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Tente novamente.")
