import requests

def search_social_media_profiles(name):
    social_media_sites = [
        "https://www.facebook.com/{}",
        "https://www.instagram.com/{}",
        "https://www.twitter.com/{}",
        "https://www.linkedin.com/in/{}",
        # Adicione aqui outros sites de redes sociais que deseja verificar
    ]

    found_profiles = []

    # Testar nome original
    found_profiles += check_profile_exists(name, social_media_sites)

    # Testar variações do nome
    variations = generate_name_variations(name)
    for variation in variations:
        found_profiles += check_profile_exists(variation, social_media_sites)

    return found_profiles

def check_profile_exists(name, social_media_sites):
    profiles = []
    for site in social_media_sites:
        url = site.format(name)
        response = requests.get(url)
        if response.status_code == 200:
            profiles.append(url)
    return profiles

def generate_name_variations(name):
    variations = []
    # Adicionar underline
    variations.append(name.replace(" ", "_"))
    # Adicionar pontos
    variations.append(name.replace(" ", "."))
    # Adicionar underline e pontos
    variations.append(name.replace(" ", "_").replace(".", "_"))
    return variations

# Exemplo de uso:
name = input("Digite o nome para pesquisa: ")
profiles = search_social_media_profiles(name)

if profiles:
    print("Perfis encontrados nas redes sociais:")
    for profile in profiles:
        print(profile)
else:
    print("Nenhum perfil encontrado nas redes sociais.")
