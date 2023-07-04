import random

def display_random_hacker_quote():
    # Lista de frases de hackers relacionadas a controle e boot2root
    control_quotes = [
        ("Quem está no controle? Responda: eu estou.", "Mr. Robot"),
        ("A revolução começa em casa.", "Mr. Robot"),
        ("Nossos destinos estão selados. Porque essa é a natureza do poder. Total, completo, absoluto. - White Rose", "Mr. Robot"),
        ("Fique de pé, caia, levante novamente. E repita até que você não possa mais levantar. Aí você saberá que você está vivo.", "Mr. Robot"),
        ("Controle é poder. Prepare-se para dominar!", "Autor Desconhecido"),
        ("O mundo é uma matriz e você é o hacker. Controle-o!", "Autor Desconhecido"),
        ("Boot2root - conquiste o sistema, domine o mundo.", "Autor Desconhecido"),
        ("A busca pelo controle total nunca termina. Continue escalando.", "Autor Desconhecido"),
        ("Descubra os segredos ocultos, ganhe o controle absoluto.", "Autor Desconhecido"),
        ("No mundo dos hackers, o controle é a chave para a vitória.", "Autor Desconhecido")
    ]
    # Exibe uma frase aleatória relacionada a controle e boot2root
    random_index = random.randint(0, len(control_quotes) - 1)
    quote, author = control_quotes[random_index]
    print(quote)
    print("- ", author)
# Exibe o MOTD
    print("==== Bem-vindo ====")
    print("Controle é poder. Prepare-se para dominar!")
    print("====================")
    print()

# Chama a função para exibir uma frase aleatória de hackers relacionada a controle e boot2root
display_random_hacker_quote()
