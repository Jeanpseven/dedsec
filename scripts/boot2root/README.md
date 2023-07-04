O script "boot2root" é uma poderosa ferramenta desenvolvida em Python que automatiza o processo de pesquisa e escalada de privilégios em sistemas com permissão root. Com esse script, você pode facilmente identificar e explorar vulnerabilidades para obter acesso privilegiado ao sistema.

O funcionamento do script é simples e intuitivo. Ele utiliza a API do GTFOBins, uma valiosa fonte de informações sobre técnicas de escalada de privilégios, e realiza uma verificação automática dos binários com permissão root disponíveis no sistema, obtidos por meio do comando "sudo -l".

Após identificar os binários com permissão root, o script pesquisa na API do GTFOBins por métodos de escalada de privilégios associados a esses binários, fornecendo opções e sugestões de comandos que podem ser utilizados para obter acesso de superusuário.

Para utilizar o script, basta clonar o repositório, instalar as dependências necessárias e executar o script Python. O resultado será uma lista de possíveis técnicas de escalada de privilégios que podem ser exploradas.

O "boot2root" é uma ferramenta versátil e flexível, que pode ser facilmente adaptada e expandida. Contribuições são bem-vindas para aprimorar o script e adicionar novas funcionalidades.

Lembre-se de respeitar as leis e políticas de segurança ao utilizar o script. Ele deve ser utilizado apenas para fins educacionais e em sistemas em que você tenha permissão para realizar os testes de escalada de privilégios.

Aproveite o poder do "boot2root" para aprimorar seus conhecimentos em segurança da informação e entender as possíveis vulnerabilidades em sistemas com permissão root.

Licença: MIT License

Repositório do script: https://github.com/Jeanpseven/boot2root

![quehacker](assets/que-hacker.gif)
