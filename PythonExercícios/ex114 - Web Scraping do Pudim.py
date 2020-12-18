# DESAFIO 114 - Crie um código em Python que teste se o site Pudim está acessível no computador usado.

import requests

url = 'http://pudim.com.br'
try:
    response = requests.get(url)
    print(response.status_code)
except:
    print(f'O site {url} não pôde ser alcançado!')
else:
    print(f'O site {url} está funcionando!')