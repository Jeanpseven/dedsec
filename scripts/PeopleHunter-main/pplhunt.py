import requests
from googlesearch import search
import os
import googlemaps
from decouple import config

def search_username(username):
    query = f'intext:"{username}"'
    try:
        # Realiza a pesquisa no Google
        results = search(query, num_results=10, lang='en')
        
        # Itera sobre os resultados e exibe as URLs encontradas
        for url in results:
            print(url)
    
    except Exception as e:
        print(f"Ocorreu um erro na pesquisa: {str(e)}")

def check_username(username):
    sites = [
        ("GitHub", f"https://github.com/{username}"),
        ("Twitter", f"https://twitter.com/{username}"),
        ("Instagram", f"https://www.instagram.com/{username}"),
        ("Facebook", f"https://www.facebook.com/{username}"),
        ("LinkedIn", f"https://www.linkedin.com/in/{username}"),
        ("Pinterest", f"https://www.pinterest.com/{username}"),
        ("Snapchat", f"https://www.snapchat.com/add/{username}"),
        ("Tumblr", f"https://{username}.tumblr.com"),
        ("Reddit", f"https://www.reddit.com/user/{username}"),
        ("Flickr", f"https://www.flickr.com/people/{username}"),
        # Adicione outros sites aqui
    ]

    for site, url in sites:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"O nome de usuário '{username}' está em uso no {site}.")
        else:
            print(f"O nome de usuário '{username}' está disponível no {site}.")

def check_phone_number(phone_number):
    sites = [
        ("Whitepages", f"https://www.whitepages.com/phone/{phone_number}"),
        ("AnyWho", f"https://www.anywho.com/phone/{phone_number}"),
        # Adicione outros sites aqui
    ]

    for site, url in sites:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"O número de telefone '{phone_number}' foi encontrado no {site}.")
        else:
            print(f"O número de telefone '{phone_number}' não foi encontrado no {site}.")

def check_email(email):
    sites = [
        ("Have I Been Pwned", f"https://haveibeenpwned.com/unifiedsearch/{email}"),
        ("Check if Email Exists", f"https://check-if-email-exists.com/check/{email}"),
        # Adicione outros sites aqui
    ]

    for site, url in sites:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"O endereço de e-mail '{email}' foi encontrado no {site}.")
        else:
            print(f"O endereço de e-mail '{email}' não foi encontrado no {site}.")

def search_user_comments(username):
    api_key = config('API_KEY')

    if not api_key:
        print("Chave de API não configurada.")
        return

    gmaps = googlemaps.Client(key=api_key)

    result = gmaps.places(query=f"{username} no Google Maps")

    if 'results' in result:
        places = result['results']

        if places:
            for place in places:
                place_name = place['name']
                print(f"Esse usuário {username} frequenta {place_name}")
        else:
            print(f"Nenhum lugar encontrado para o usuário {username}")
    else:
        print("Ocorreu um erro na busca")

def main():
    option = input("Escolha a opção:\n1 - Procurar nome de usuário\n2 - Procurar número de telefone\n3 - Procurar endereço de e-mail\n")
    
    if option == "1":
        username = input("Digite o nome de usuário que deseja verificar: ")
        check_username(username)
        search_username(username)
        search_user_comments(username)
    elif option == "2":
        phone_number = input("Digite o número de telefone que deseja verificar: ")
        check_phone_number(phone_number)
    elif option == "3":
        email = input("Digite o endereço de e-mail que deseja verificar: ")
        check_email(email)
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
