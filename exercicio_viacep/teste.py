import requests
 
 
def rua_do_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    endereco = requests.get(url).json() #pega url e tranforma em json(dicionario)
    return endereco['logradouro']
 
 
print(f'50030230 fica na: {rua_do_cep("50030230")}')
print(f'01310100 fica na: {rua_do_cep("01310100")}')
 
assert rua_do_cep('01310100') == 'Avenida Paulista', 'o 01310100 eh a Paulista'
print('OK: o ViaCEP respondeu, e a chave logradouro tinha a rua')
