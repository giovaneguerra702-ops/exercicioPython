# Exemplo de abertura - lista de APIs (viagem), o lado da moeda.
#
# Conceitos: um endereco que devolve dados em vez de pagina, o .json() que
# transforma a resposta num dicionario, o acesso por chave - que eh o
# mesmo de sempre - e o dado que muda contra o dado que ja parou.

import requests
import apoio_rede   # rede a prova de sala (timeout, cache, certificado) - nao precisa entender
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def busca_cotacao(data, moeda):
    url = f'https://api.frankfurter.dev/v1/{data}?from=BRL&to={moeda}'
    cambio = requests.get(url, verify=False).json()
    return cambio['rates'][moeda]


hoje = busca_cotacao('latest', 'EUR')
naquele_dia = busca_cotacao('2024-07-01', 'EUR')

print(f'1 real vale hoje:            {hoje} euros')
print(f'1 real valia em 2024-07-01:  {naquele_dia} euros')

assert naquele_dia == 0.16662, 'a cotacao daquele dia nao muda mais'
print('OK: o dia que ja passou responde sempre a mesma coisa')
