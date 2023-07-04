import requests

def search_profile_on_site(site, username):
    url = site.format(username)
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Profile found on {site}: {url}")
    else:
        print(f"Profile not found on {site}")

# Exemplo de uso
username = input("Digite o nome de usuário: ")

# Lista de sites
sites = [
    "https://www.facebook.com/{}",
    "https://www.instagram.com/{}",
    "https://www.twitter.com/{}",
    "https://www.linkedin.com/in/{}",
    "https://www.reddit.com/user/{}",
    "https://www.pinterest.com/{}",
    "https://www.telegram.me/{}",
    "https://www.tiktok.com/@{}",
    "https://www.youtube.com/{}",
    "https://www.wattpad.com/user/{}",
    "https://www.netflix.com/{}",
    "https://www.github.com/{}"
]

# Busca em sites específicos
for site in sites:
    search_profile_on_site(site, username)
