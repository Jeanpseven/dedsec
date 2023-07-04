#!/bin/sh

# Função para iniciar o servidor VNC para acompanhamento
iniciar_vnc_acompanhamento() {
  echo "Iniciando o servidor VNC para acompanhamento..."
  vncserver :0 -geometry 1280x720 -depth 24 -localhost
}

# Função para abrir um servidor VNC para ser acompanhado em um determinado IP e porta
abrir_vnc_acompanhado() {
  echo "Digite o IP do servidor VNC a ser acompanhado (padrão: localhost):"
  read ip
  ip=${ip:-localhost}  # Utiliza "localhost" como padrão se nenhum IP for fornecido

  echo "Digite a porta do servidor VNC a ser acompanhado (padrão: 5901):"
  read porta
  porta=${porta:-5901}  # Utiliza "5901" como padrão se nenhuma porta for fornecida

  echo "Abrindo o servidor VNC em $ip:$porta para acompanhamento..."
  vncviewer $ip:$porta
}

# Função para parar o servidor VNC
parar_vnc() {
  echo "Parando o servidor VNC..."
  vncserver -kill :0
}

# Loop principal do script
while true; do
  echo "
  ==== Script do Servidor VNC ====

  Opções:
  1. Iniciar o servidor VNC para acompanhamento(listener)
  2. Abrir um servidor VNC para ser acompanhado
  3. Parar o servidor VNC
  4. Sair

  Digite a opção desejada:"
  read opcao

  case $opcao in
    1)
      iniciar_vnc_acompanhamento
      ;;
    2)
      abrir_vnc_acompanhado
      ;;
    3)
      parar_vnc
      ;;
    4)
      break
      ;;
    *)
      echo "Opção inválida. Tente novamente."
      ;;
  esac
done
