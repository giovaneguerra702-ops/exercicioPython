agenda = {
    'lucas': {'email': 'lucas@exemplo.com', 'telefones': [11999888999, 1177788899]},
    'maria': {'email': 'maria@exemplo.com', 'telefones': [84999777444]},
    'marta': {'telefones': [1177788899]},   # repare: a marta NAO tem email!
}

# dicionario inteiro do lucas
a = agenda['lucas']
assert a == {'email': 'lucas@exemplo.com', 'telefones': [11999888999, 1177788899]}

# string: o email do lucas
b = agenda['lucas']['email'] # se preferir: agenda['lucas']['email']
assert b == 'lucas@exemplo.com'

c = agenda['lucas']['telefones'][0] #primeiro telefone do lucas
assert c == 11999888999

d = 'email' in agenda['maria'].keys() #valor booleano: maria tem um email?
assert d == True

e = 'email' in agenda['marta'].keys() #valor booleano: marta tem um email?
assert e == False

print("tudo ok")