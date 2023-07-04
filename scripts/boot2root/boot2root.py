import os
import requests
import subprocess
import motd

motd.display_random_hacker_quote()

def get_sudo_permissions():
    try:
        output = subprocess.check_output(['sudo', '-l'], stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return e.output

def search_gtfo_bins(program):
    base_url = 'https://gtfobins.github.io/gtfobins/{}/'
    url = base_url.format(program)

    try:
        response = requests.get(url)
        if response.ok:
            return response.text
        else:
            print('Error querying GTFOBins.')
    except requests.exceptions.RequestException as e:
        print('Connection error:', e)

def main():
    # Get binaries with root permissions
    sudo_permissions = get_sudo_permissions()
    print('Binaries with root permissions:')
    print(sudo_permissions)

    # Extract program names from sudo permissions
    programs = []
    lines = sudo_permissions.splitlines()
    for line in lines:
        if line.startswith('(ALL') or line.startswith('(root'):
            words = line.split()
            if len(words) >= 3:
                program = words[1]
                programs.append(program)

    # Search GTFOBins for each found program
    print('\nGTFOBins search results:')
    for program in programs:
        print('\n---', program, '---')
        result = search_gtfo_bins(program)
        if result:
            print(result)

if __name__ == '__main__':
    main()
