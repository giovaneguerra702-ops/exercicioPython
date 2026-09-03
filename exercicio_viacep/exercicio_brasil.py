# Lista de exercicios - catalogo de clientes (APIs com requests)
# Pre-requisito: a aula de dicionario.
#
# A ideia da lista: uma API eh um endereco que, em vez de devolver uma
# pagina, devolve DADOS - e em Python esses dados chegam como um
# DICIONARIO. Entao quase tudo aqui eh o que voce ja sabe fazer: ler
# dicionario. De requests voce so vai usar uma linha.
#
# ATENCAO: esta lista baixa dados da internet do comeco ao fim. Sem rede,
# ela nao roda.

# === Helper de verificacao (pode ignorar) ===
# A funcao `verifica` compara o seu valor com a resposta correta (que
# fica escondida em formato de hash). Voce nao precisa entender ela -
# se voce errou, ela imprime "Valor errado: voce colocou X" e o assert
# logo abaixo dispara.
import hashlib
def verifica(valor, codigo, ordem_importa=False, nome_questao=''):
    if isinstance(valor, tuple):
        valor = list(valor)
    if isinstance(valor, dict):
        valor = sorted(valor.items())
    valores = [valor]
    if isinstance(valor, list):
        valores = [valor if ordem_importa else sorted(valor)]
    elif isinstance(valor, int) and not isinstance(valor, bool):
        valores.append(float(valor))
    elif isinstance(valor, float):
        valores.append(int(valor))
    def _hash(v):
        s = f'{nome_questao}:{v}' if nome_questao else str(v)
        return hashlib.sha224(s.encode('utf-8')).hexdigest()
    respostas = [_hash(v) == codigo for v in valores]
    if not any(respostas):
        print(f'Valor errado: voce colocou "{valor}" na variavel')
        return False
    return True
# fim do helper


# A funcao explicar() te ajuda quando voce travar numa questao. Embaixo de
# cada questao tem uma linha `# explicar('nome')` comentada - descomente
# ela para ler a discussao da resposta.
def explicar(questao):
    try:
        from explicacao_brasil import EXPLICACOES
    except ImportError:
        print("Arquivo 'explicacao_brasil.py' nao foi encontrado.")
        print("Esse arquivo vem JUNTO com este exercicio - peca ao")
        print("professor. Ele contem as explicacoes das questoes.")
        return
    import codecs
    if questao not in EXPLICACOES:
        print(f"Nao tenho explicacao para '{questao}'.")
        print(f"Questoes disponiveis: {sorted(EXPLICACOES.keys())}")
        return
    print(codecs.decode(EXPLICACOES[questao], 'rot_13'))
    input("aperte enter para continuar")


import requests


# === Rede (pode ignorar) ===
# Guarda o que ja foi baixado, pra nao pedir a mesma coisa pra internet
# toda vez que voce roda, e traduz os erros de rede pra portugues. Voce
# nao precisa entender isso - continue escrevendo requests.get(url).json()
# do jeito que o enunciado ensina.
import os
_PASTA = os.path.dirname(os.path.abspath(__file__))
try:
    import requests_cache
    requests_cache.install_cache(os.path.join(_PASTA, 'cache_api'),
                                 expire_after=43200, stale_if_error=True)
except ImportError:
    print('AVISO: a biblioteca requests_cache nao esta instalada nesta maquina.')
    print('       A lista roda normalmente assim mesmo, com o cache de reserva.')
    print('       Rode no cmd:  pip install -r requirements.txt')
    print()
try:
    import apoio_rede
except ImportError:
    print('AVISO: o arquivo apoio_rede.py nao esta nesta pasta.')
    print('       Ele vem JUNTO com este exercicio - peca ao professor.')
    print('       A lista nao roda sem ele')
    exit()
# fim da rede


# Alguns testes desta lista dependem de o ViaCEP continuar respondendo
# exatamente como respondia quando a lista foi escrita: a CONTAGEM de
# campos da resposta (o exercicio quantas_chaves_no_cep, da Fase 1) e o
# conteudo exato de dois enderecos - o logradouro da Mirtes e do Cicero, e
# o complemento deles (os testes do endereco_curto e do tem_complemento,
# na Fase 2).
#
# Se o site acrescentar um campo, ou corrigir um daqueles enderecos, a sua
# resposta certa passa a ser reprovada, sem ser erro seu. Se isso
# acontecer, eu vou te avisar em sala. Nesse caso,
# Mude a linha abaixo para True: esses testes ficam desligados
# e o resto da lista continua valendo normalmente.
desligar_testes_frageis = False

if desligar_testes_frageis:
    print('ATENCAO: os testes frageis estao desligados (parte da Fase 1 e da Fase 2 nao sera conferida)')


# ===== FASE 1 - Baixando o primeiro dicionario =====

'''
EXPLICACAO

A Mirtes e o Cicero abriram uma loja de roupas, e o cadastro de clientes
vai funcionar assim: quando alguem chega, a atendente pergunta o CEP e o
sistema consulta uma API - o ViaCEP - que devolve o endereco completo.
Os dois primeiros clientes do cadastro sao a propria Mirtes, que mora no
Recife, e o Cicero, que mora em Belo Horizonte.

Abra este endereco no seu navegador, agora:

    https://viacep.com.br/ws/50030230/json/

Voce vai ver um dicionario. Esse dicionario eh a resposta do site pro CEP
50030-230 - o CEP da Mirtes. Como esses dados estao
num formato de dicionario, podemos
acessar eles também em python:

    # import requests - ja fizemos acima, voce teria que fazer se fosse
    # usar um arquivo python separado
    dic_endereco = requests.get('https://viacep.com.br/ws/50030230/json/').json()

`requests.get(url)` busca o endereco. `.json()` transforma a resposta num
dicionario Python. E acabou - eh so isso que voce precisa saber de API
nesta lista. Todo o resto eh ler dicionario, que voce ja sabe.
'''

'''
EXERCICIO

Faca a funcao busca_cep(cep) que monta o endereco do ViaCEP com esse cep
e devolve o dicionario que o site responder.

>>> busca_cep('50030230')['localidade']
    'Recife'

Repare que o CEP entra SEM o tracinho, e que o endereco termina em
`/json/`:

    https://viacep.com.br/ws/50030230/json/

Dica: monte a url com f-string, colocando o cep no meio.

So pra te lembrar da f-string:
>>> "2 mais dois resulta {2+2}"
'2 mais dois resulta {2+2}'
>>> f"2 mais dois resulta {2+2}"
'2 mais dois resulta 4'

O f antes da string faz o python expandir expressoes ou variaveis dentro da string

    
'''
def busca_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    endereco = requests.get(url).json()
    return endereco


# os dois CEPs do cadastro, como STRING - eh isso que a busca_cep recebe
cep_da_mirtes = '50030230'       # a Mirtes, mora no Cais do Apolo, no Recife
cep_do_cicero = '30140071'       # o Cicero, mora em Belo Horizonte

# e os dois DICIONARIOS que o ViaCEP devolveu pra cada um deles
endereco_da_mirtes = busca_cep(cep_da_mirtes)
endereco_do_cicero = busca_cep(cep_do_cicero)

assert endereco_da_mirtes != None, 'busca_cep ainda nao devolve nada - complete a funcao acima'
assert endereco_da_mirtes['localidade'] == 'Recife', 'o 50030230 eh no Recife'
assert endereco_da_mirtes['uf'] == 'PE', 'o 50030230 eh em Pernambuco'
assert endereco_do_cicero['localidade'] == 'Belo Horizonte', 'o 30140071 eh em BH'
print(f'Baixado agora, do ViaCEP: {endereco_da_mirtes}')
print('Exercicio busca_cep: OK')


breakpoint_aqui = 42

# PARE
# Voce acabou de baixar dois dicionarios. Antes de responder qualquer coisa,
# olhe ele por dentro - via pythontutor ou via o debug console do vscode
# (ponha um breakpoint na linha `breakpoint_aqui = 42` acima, rode com
# 'debug python file').
# Digite coisas como print(endereco_da_mirtes), print(endereco_da_mirtes['uf'])
# Depois tente chegar nos valores 'Recife', 'PE' e '81'.
# Experimente tambem print(endereco_da_mirtes.keys()) e veja a cara disso.
# Compare com o que aparece no navegador - eh o mesmo dicionario.
# Se nao conseguir, me chame.


'''
EXERCICIO

Considere o dicionario endereco_da_mirtes que voce acabou de baixar.

Preencha as variaveis com uma EXPRESSAO Python que produz o valor (em vez
do valor literal). Se nao conseguir, comece pelo valor, mas depois tente
a expressao.

1) Em que cidade a Mirtes mora?   Dica: a cidade esta na chave 'localidade'
2) Em que estado (a sigla)?
3) Em que bairro?
4) Quantas chaves tem esse dicionario?   Dica: comprimento de endereco_da_mirtes.keys()
5) Qual o DDD do telefone de la?
'''
cidade_da_mirtes      = busca_cep(cep_da_mirtes)['localidade']
uf_da_mirtes          = busca_cep(cep_da_mirtes)['uf']
bairro_da_mirtes      = busca_cep(cep_da_mirtes)['bairro']
quantas_chaves_no_cep = len(busca_cep(cep_da_mirtes).keys())
ddd_da_mirtes         = busca_cep(cep_da_mirtes)['ddd']

# Travou? Descomente a linha da questao para ler a explicacao:
# explicar('cidade_da_mirtes')
# explicar('uf_da_mirtes')
# explicar('bairro_da_mirtes')
# explicar('quantas_chaves_no_cep')
# explicar('ddd_da_mirtes')

assert verifica(cidade_da_mirtes, '7504c9ab59d1af4cd795b8fb203ea67b9460a9ba3fa036024ff0cd58', nome_questao='cidade_da_mirtes'), 'cidade_da_mirtes incorreta'
assert verifica(uf_da_mirtes, '89e5f5bde79a969e295697d5bcdfa73fa0766346fc7f2c194ba88c35', nome_questao='uf_da_mirtes'), 'uf_da_mirtes incorreta'
assert verifica(bairro_da_mirtes, '6d8657a5a76dd15928da4bc6d7d0b12acc025f02b04ebfb12b613c24', nome_questao='bairro_da_mirtes'), 'bairro_da_mirtes incorreta'
if not desligar_testes_frageis:
    assert verifica(quantas_chaves_no_cep, '64c64eba466f953f515e781ca40e70c60b7ba0dccd0676b22c29042a', nome_questao='quantas_chaves_no_cep'), 'quantas_chaves_no_cep incorreta'
assert verifica(ddd_da_mirtes, '6d71a63b70036ed308b007dcdacd04b673857d315415242fb6e8ce5d', nome_questao='ddd_da_mirtes'), 'ddd_da_mirtes incorreta'
print('Exercicio lendo o CEP: OK')


'''
EXERCICIO

Q1 - colchetes_ate_a_cidade

Quantos colchetes voce precisa pra chegar na cidade do endereco_da_mirtes?

    a) um:   endereco_da_mirtes['localidade']
    b) dois: endereco_da_mirtes['endereco']['localidade']
    c) tres: endereco_da_mirtes['endereco']['cidade']['nome']
    d) nenhum - a cidade nao vem nessa resposta
'''
colchetes_ate_a_cidade = 'a'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('colchetes_ate_a_cidade')

assert verifica(colchetes_ate_a_cidade, '7d788b56d8cf4d36bf17c544f62922a68108c2ccf9e54cdbb8b0f373', nome_questao='colchetes_ate_a_cidade'), 'colchetes_ate_a_cidade incorreta'


'''
EXERCICIO

Q2 - tipo_do_ddd

O que exatamente esta guardado em endereco_da_mirtes['ddd']?
Agora eh uma boa hora pra usar o debugger
e digitar type(endereco_da_mirtes['ddd'])

    a) o numero 81
    b) o numero 81.0
    c) a string '81'
    d) uma lista com o 8 e o 1
'''
tipo_do_ddd = 'c'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('tipo_do_ddd')

assert verifica(tipo_do_ddd, 'd9359d0650873ffaac5dfa3918bf88c443869b19d28c31455e82bfcc', nome_questao='tipo_do_ddd'), 'tipo_do_ddd incorreta'


'''
EXERCICIO

Q3 - chave_que_nao_veio

O endereco_da_mirtes nao tem nenhuma chave 'numero'. O que o Python faz com

    endereco_da_mirtes['numero']

    a) devolve 0
    b) levanta KeyError e o programa para
    c) devolve None
    d) devolve uma string vazia, como acontece com 'gia'
'''
chave_que_nao_veio = 'b'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('chave_que_nao_veio')

assert verifica(chave_que_nao_veio, 'd7f40f576c85f0b51882e3e4752f04af145ac61557dc9b71bb0c8489', nome_questao='chave_que_nao_veio'), 'chave_que_nao_veio incorreta'
print('Exercicio multipla escolha da Fase 1: OK')


# ===== FASE 2 - Os pares do CEP =====

'''
EXPLICACAO

No cadastro da loja, a ficha de um cliente guarda o dicionario que o
ViaCEP devolveu. Daqui pra frente, cada capacidade desta lista aparece em
DUAS funcoes.

A primeira eh a PURA: ela RECEBE o dicionario ja baixado e so le. Nao vai
a internet e nao procura variavel nenhuma por conta propria - por isso a
mesma funcao serve pra ficha da Mirtes, pra do Cicero e pra qualquer
outro cliente que voce cadastrar depois.

A segunda eh a IRMA: ela nao recebe dicionario nenhum. Recebe o CEP,
BUSCA o dicionario e entrega pra pura. 

    cidade_do_dict(endereco_da_mirtes)   le um dicionario que voce ja tem
    cidade_do_cep('50030230')                busca o dicionario, e ai le

Repare que o NOME diz o que a funcao RECEBE:

    termina em _do_dict  ->  recebe dicionario, nao vai a internet
    termina em _do_cep   ->  recebe o CEP, e vai buscar

Voce ja tem dois enderecos baixados pra testar: endereco_da_mirtes e
endereco_do_cicero. Eles sao diferentes num ponto importante: o
'complemento' do Cicero veio preenchido, e o da Mirtes veio vazio.

As funcoes _do_cep quase sempre tem duas linhas, uma para baixar
os dados e a outra para decifrar eles usando a funcao _do_dict
'''

'''
EXERCICIO

A pura. Faca a funcao cidade_do_dict(endereco) que recebe um
dicionario de endereco e devolve a cidade dele.

Olhe no dicionario (no firefox, ou no debugger) para ver qual a chave 
do dicionario que você deve usar

    >>> cidade_do_dict(endereco_do_cicero)
    'Belo Horizonte'
'''
def cidade_do_dict(endereco):
    cidade = endereco['localidade']
    return cidade

# um endereco inventado, que nao veio do ViaCEP - prova que a funcao le o
# dicionario que RECEBEU, e nao alguma variavel la de cima
endereco_t = {'localidade': 'Olinda', 'uf': 'PE'}
assert cidade_do_dict(endereco_t) == 'Olinda', 'a funcao tem que ler o dicionario que recebeu'


assert cidade_do_dict(endereco_da_mirtes) == 'Recife', 'cidade da Mirtes'
assert cidade_do_dict(endereco_do_cicero) == 'Belo Horizonte', 'cidade do Cicero'

print('Exercicio cidade_do_dict: OK')


'''
EXERCICIO

E agora a irma. Faca a funcao cidade_do_cep(cep) que recebe o CEP (a
string, sem tracinho), busca o endereco e devolve a cidade.

Ela eh uma linha: use a busca_cep e a cidade_do_dict que voce ja fez.

    >>> cidade_do_cep('30140071')
    'Belo Horizonte'
'''

cep_da_mirtes = '50030230'       # a Mirtes, mora no Cais do Apolo, no Recife
cep_do_cicero = '30140071'       # o Cicero, mora em Belo Horizonte
def cidade_do_cep(cep):
    cidade = busca_cep(cep)['localidade']
    return cidade


assert cidade_do_cep(cep_da_mirtes) == 'Recife', 'o CEP da Mirtes eh no Recife'
print('Exercicio cidade_do_cep: OK')


'''
EXERCICIO

O mesmo par, agora pra sigla do estado.

Faca as duas: uf_do_dict(endereco), que le o dicionario, e
uf_do_cep(cep), que busca e le.

    >>> uf_do_dict(endereco_do_cicero)
    'MG'
    >>> uf_do_cep('50030230')
    'PE'
'''
def uf_do_dict(endereco):
    uf = endereco['uf']
    return uf

endereco_t = {'localidade': 'Olinda', 'uf': 'PE'}
assert uf_do_dict(endereco_t) == 'PE', 'a funcao tem que ler o dicionario que recebeu'

assert uf_do_dict(endereco_da_mirtes) == 'PE', 'uf da Mirtes'
assert uf_do_dict(endereco_do_cicero) == 'MG', 'uf do Cicero'


def uf_do_cep(cep):
    uf = busca_cep(cep)['uf']
    return uf

cep_da_mirtes = '50030230'       # a Mirtes, mora no Cais do Apolo, no Recife
cep_do_cicero = '30140071'       # o Cicero, mora em Belo Horizonte
assert uf_do_cep(cep_do_cicero) == 'MG', 'o CEP do Cicero eh em Minas'
print('Exercicio uf_do_dict e uf_do_cep: OK')


'''
EXERCICIO

Faca a funcao endereco_curto(endereco) que junta quatro campos numa
string so, exatamente neste formato:

    logradouro, bairro - cidade/UF

    >>> endereco_curto(endereco2)
    'Cais do Apolo, Lapa - Recife/PE'

Dica: monte seu return com f-string. E olha so - o bairro da Mirtes se
chama "Recife", igual a cidade. Nao eh erro seu.

Esta nao ganha irma, e a Fase 4 vai mostrar por que: quem imprime o
endereco curto ja tem o dicionario na mao.
'''
def endereco_curto(endereco):
    rua = endereco['logradouro']
    bairro = endereco['bairro']
    cidade = endereco['localidade']
    uf = endereco['uf']
    return f'{rua}, {bairro} - {cidade}/{uf}'


# um endereco inventado, que nao veio do ViaCEP - assim a funcao continua
# sendo testada mesmo se os testes mais frageis estiverem desligados
endereco_t = {'logradouro': 'Rua do Sol', 'bairro': 'Carmo',
              'localidade': 'Olinda', 'uf': 'PE'}
assert endereco_curto(endereco_t) == 'Rua do Sol, Carmo - Olinda/PE', 'endereco curto montado a mao'

if not desligar_testes_frageis:
    assert endereco_curto(endereco_da_mirtes) == 'Cais do Apolo, Recife - Recife/PE', 'endereco curto da Mirtes'
    assert endereco_curto(endereco_do_cicero) == 'Rua dos Aimorés, Boa Viagem - Belo Horizonte/MG', 'endereco curto do Cicero'
print('Exercicio endereco_curto: OK')


'''
EXERCICIO

Calculo a mao, antes da proxima funcao.

O 'complemento' do endereco do Cicero eh a string 'de 971/972 a
1399/1400'. O da Mirtes eh a string vazia, ''.

Pensando numa funcao que responde "esse endereco tem complemento?", o que
ela responderia pro Cicero? (True ou False)
'''
complemento_do_cicero_a_mao = True

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('complemento_do_cicero_a_mao')

assert verifica(complemento_do_cicero_a_mao, '5b3e0dc664ce99f25456cb86efeeaf8603f5eeca8fe0563b30b79c71', nome_questao='complemento_do_cicero_a_mao'), 'complemento_do_cicero_a_mao incorreta'
print('Exercicio complemento a mao: OK')


'''
EXERCICIO

Faca a funcao tem_complemento(endereco) que devolve True se o campo
'complemento' NAO estiver vazio.

Repare na diferenca: a chave 'complemento' existe nos dois enderecos. O
que muda eh que num deles ela veio com string vazia ('') e no outro veio
preenchida.

Esta tambem nao ganha irma: "me diga se esse endereco tem complemento"
nao eh uma pergunta "de verdade" - eh detalhe de um dicionario
que voce ja tem.

    >>> tem_complemento(endereco_da_mirtes)
    False
    >>> tem_complemento(endereco_do_cicero)
    True
'''
def tem_complemento(endereco):
    complemento = endereco['complemento']
    if  complemento == '':
        return False
    else:
        return True

endereco_t = {'complemento': 'fundos', 'localidade': 'Olinda', 'uf': 'PE'}
assert tem_complemento(endereco_t) == True, 'complemento preenchido'
endereco_t = {'complemento': '', 'localidade': 'Olinda', 'uf': 'PE'}
assert tem_complemento(endereco_t) == False, 'complemento vazio'

if not desligar_testes_frageis:
    assert tem_complemento(endereco_da_mirtes) == False, 'a Mirtes veio sem complemento'
    assert tem_complemento(endereco_do_cicero) == True, 'o Cicero veio com complemento'

print('Exercicio tem_complemento: OK')


# ===== FASE 3 - Quando a API nao acha =====

'''
EXPLICACAO

E quando a atendente digita um CEP que nao existe? Abra este no navegador:

    https://viacep.com.br/ws/99999999/json/

O site nao quebra e nao devolve vazio. Ele devolve um dicionario com UMA
chave so:

    {'erro': 'true'}

Ou seja: pra saber se deu certo, voce pergunta se a chave 'erro' esta na
resposta - com o mesmo `in ... .keys()` que voce ja usou.

Repare que isso eh uma escolha ESTRANHA do ViaCEP: a resposta chega como
se tivesse dado tudo certo, e o aviso de que nao achou vem escondido
dentro dos dados. Existe um jeito mais comum de uma API dizer "nao achei",
e ele nao esta aqui - eh o assunto do desafio da Fase 5, no fim do
arquivo, se voce quiser ir ver.
'''

'''
EXERCICIO

Q4 - valor_do_erro

Olhe de novo a resposta do CEP que nao existe: {'erro': 'true'}. O valor
da chave 'erro' eh...

    a) a string 'true' - repare nas aspas; nao eh o True do Python
    b) o booleano True
    c) o numero 1
'''
valor_do_erro = 'a'   # 'a', 'b' ou 'c'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('valor_do_erro')

assert verifica(valor_do_erro, 'b41e7cea98801696dd9f4aaa71ad5258376ff6f3fdf77a436bc95906', nome_questao='valor_do_erro'), 'valor_do_erro incorreta'


'''
EXERCICIO

Faca a funcao achou_endereco(resposta) que recebe o que o ViaCEP devolveu e
responde True se aquele CEP existe - ou seja, False quando veio a chave
'erro'.

Como a gente verifica mesmo quando uma chave veio em um dicionario?

    >>> achou_endereco(endereco_da_mirtes)
    True
    >>> achou_endereco({'erro': 'true'})
    False
'''
def achou_endereco(resposta):
    if 'cep' in resposta.keys():
        return True
    else:
        return False


# os dois formatos que ela precisa distinguir, lado a lado
resposta_t = {'erro': 'true'}
assert achou_endereco(resposta_t) == False, 'quando veio a chave erro, nao achou'
resposta_t = {'cep': '50030-230', 'localidade': 'Recife', 'uf': 'PE'}
assert achou_endereco(resposta_t) == True, 'sem a chave erro, achou'

assert achou_endereco(endereco_da_mirtes) == True, 'o CEP da Mirtes existe'
assert achou_endereco(endereco_do_cicero) == True, 'o CEP do Cicero existe'
print('Exercicio achou_endereco: OK')

# A irma desta - a cep_existe(cep), que busca e ja responde - mora no
# desafio da Fase 5, porque pra testar ela de verdade eh preciso pedir um
# CEP que NAO existe, e o ViaCEP anda instavel nessa rota.


'''
EXERCICIO

Q5 - qual_das_duas

A proxima fase vai imprimir QUATRO coisas sobre o MESMO endereco da
Mirtes: a cidade, a sigla do estado, o endereco curto e se tem
complemento.

Qual eh o jeito certo de fazer isso?

    a) chamar as quatro irmas (cidade_do_cep, uf_do_cep, ...), passando o
       CEP da Mirtes pra cada uma
    b) tanto faz - as duas formas escrevem a mesma quantidade de codigo
    c) usar as irmas nas duas primeiras e as puras nas outras duas
    d) baixar o endereco UMA vez com busca_cep e passar esse dicionario
       para as quatro puras
'''
qual_das_duas = 'd'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('qual_das_duas')

assert verifica(qual_das_duas, 'e4329aee340bb7cc29ce10767ac6e18b87612e17b6b16888d46a52f9', nome_questao='qual_das_duas'), 'qual_das_duas incorreta'
print('Exercicio multipla escolha da Fase 3: OK')


# ===== FASE 4 - O cadastro da Mirtes e do Cicero =====

# Agora o cadastro inteiro, com TODAS as funcoes da lista, para os dois
# primeiros clientes.
#
# Repare no que acontece daqui pra baixo: sao QUATRO perguntas sobre o
# mesmo endereco da Mirtes (cidade, uf, endereco curto, complemento) e
# cada uma tem uma irma. Se a gente chamasse as irmas, seriam quatro idas
# ao ViaCEP pra buscar o MESMO endereco.
#
# Entao baixa-se UMA vez cada dicionario - ja esta baixado, la em cima -
# e daqui pra baixo eh tudo funcao pura. Eh pra isso que elas existem. A
# irma vale quando a pergunta eh uma so.

print()
print('=== O CADASTRO ===')
print(f'Mirtes: {endereco_curto(endereco_da_mirtes)}')
print(f'  cidade: {cidade_do_dict(endereco_da_mirtes)}')
print(f'  uf: {uf_do_dict(endereco_da_mirtes)}')
print(f'  complemento no endereco: {tem_complemento(endereco_da_mirtes)}')
print(f'Cicero: {endereco_curto(endereco_do_cicero)}')
print(f'  cidade: {cidade_do_dict(endereco_do_cicero)}')
print(f'  uf: {uf_do_dict(endereco_do_cicero)}')
print(f'  complemento no endereco: {tem_complemento(endereco_do_cicero)}')
print()

assert achou_endereco(endereco_da_mirtes), 'o CEP da Mirtes existe'
assert achou_endereco(endereco_do_cicero), 'o CEP do Cicero existe'
assert cidade_do_dict(endereco_da_mirtes) == 'Recife', 'a Mirtes mora no Recife'
assert cidade_do_dict(endereco_do_cicero) == 'Belo Horizonte', 'o Cicero mora em BH'
assert uf_do_dict(endereco_da_mirtes) == 'PE', 'a Mirtes mora em PE'
assert uf_do_dict(endereco_do_cicero) == 'MG', 'o Cicero mora em MG'
if not desligar_testes_frageis:
    assert tem_complemento(endereco_da_mirtes) == False, 'o endereco da Mirtes vem sem complemento'
    assert tem_complemento(endereco_do_cicero) == True, 'o do Cicero vem com complemento'
print('Exercicio cadastro integrado: OK')


# E aqui, sim, uma pergunta solta - uma so, sobre nada que ja esta na mao.
# Esse eh o caso em que a irma eh o caminho curto. Repare que ela guarda,
# por dentro, exatamente aquele encadeamento que voce escreveu la em cima:
#
#     cidade_do_cep('01310100')  eh  cidade_do_dict(busca_cep('01310100'))
#
print(f'(so por curiosidade: o CEP da Paulista fica na {cidade_do_cep("01310100")})')
assert cidade_do_cep('01310100') == 'São Paulo', 'o 01310100 eh da Paulista, em Sao Paulo'
print('Exercicio a irma na pergunta solta: OK')


# ===== A interface final: o cadastro =====

# O cadastro inteiro, funcionando como CLI, mora no arquivo cadastro.py
# (que vem junto com esta lista). Ele esta PRONTO - adicionar cliente,
# editar, listar, tudo - MENOS uma parte: o preenchimento automatico do
# endereco a partir do CEP, que eh exatamente o assunto desta lista
# inteira.
#
# Faca assim: abra o cadastro.py, complete a funcao preenche_endereco
# (as instrucoes estao na docstring dela), e rode `python3 cadastro.py`.
# Teste adicionando um cliente com o CEP 50030230: o endereco inteiro
# preenche sozinho. E o CEP 99999999, que nao existe, precisa ser avisado
# em vez de preencher - o mesmo if/else que a Fase 3 ensinou.


print('\n=== PARABENS! Todos os exercicios completos! ===')


# ===== FASE 5 - DESAFIO (opcional) =====

'''
EXPLICACAO

Toda vez que voce pede alguma coisa na internet, a resposta volta com um
NUMERO junto, dizendo COMO foi. Ele nao aparece no navegador, mas esta
sempre la - e o requests guarda ele pra voce:

    resposta = requests.get(url)
    resposta.status_code       # o numero: como foi
    resposta.json()            # os dados: o que voce usou a lista inteira

Voce ja conhece pelo menos um desses numeros sem saber que conhece: o
**404**, daquelas paginas de "nao encontrado" que todo mundo ja viu na
web. Os quatro mais comuns:

    200   deu certo
    400   voce pediu errado (a url estava mal formada)
    404   nao existe isso que voce pediu
    500   o servidor quebrou do lado de la

O padrao da web eh esse: quem procura uma coisa que NAO EXISTE recebe 404.
Um site de CEP que seguisse o padrao responderia 404 pro 99999999.

O ViaCEP nao faz isso. O que ele faz eh o que voce vai descobrir agora.

(Se em algum momento aparecer um 502 por aqui, nao eh voce: eh o servidor
deles com problema, e acontece de verdade. Eh mais um motivo pra saber ler
esse numero.)

Os asserts desta fase - a opcional - ficam DESLIGADOS por padrao. Para
ligar (e ver "OK" conforme acerta), mude a flag `desafio` abaixo de False
para True.
'''


desafio = False    # ligue o desafio mudando para True


'''
EXERCICIO (a)

Q6 - status_certo_de_cep_que_nao_existe

Do ponto de vista do PADRAO da web, quando voce pede uma coisa que nao
existe, o servidor responde com o status de "nao encontrado" - o **404**,
daquelas paginas que todo mundo ja viu na web.

Entao a pergunta: para o CEP 99999999, que NAO existe, qual seria o
status CORRETO, de acordo com esse padrao?

    a) 404 - "nao existe isso que voce pediu"
    b) 200 - "deu certo" (mesmo sem ter achado nada)
    c) 500 - "o servidor quebrou"
    d) 204 - "deu certo, mas nao tem conteudo"
'''
status_certo_de_cep_que_nao_existe = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('status_certo_de_cep_que_nao_existe')


'''
EXERCICIO (b)

Q7 - status_viacep_de_cep_que_nao_existe

A teoria diz 404. E na pratica? Vamos ver com o navegador.

Abra o Firefox e aperte F12 para abrir as ferramentas do desenvolvedor.
Clique na aba "Network" (Rede) e DEIXE ela aberta. Depois navegue para:

    https://viacep.com.br/ws/99999999/json/

A linha da requisicao vai aparecer na lista (o endereco dela termina em
`/json/`). Olhe a coluna "Status" dessa linha - que numero esta la?

    a) 404, seguindo o padrao da web pra "nao existe"
    b) 200, o mesmo de quando o CEP existe
    c) 500, porque nao achar eh um erro do servidor
    d) 204, que quer dizer "deu certo, mas nao tem conteudo"

Se a lista estiver vazia, eh porque a aba abriu depois de a pagina
carregar: aperte F5 com ela aberta, e o pedido aparece.
'''
status_viacep_de_cep_que_nao_existe = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('status_viacep_de_cep_que_nao_existe')


'''
EXERCICIO (c)

Faca a funcao status_do_cep(cep) que monta a mesma url de sempre e devolve
o NUMERO da resposta, em vez dos dados.

Repare que ela nao chama .json(): o numero esta na propria resposta, antes
de olhar o conteudo.

    >>> status_do_cep('50030230')
    200
'''
def status_do_cep(cep):
    pass


if desafio:
    assert verifica(status_certo_de_cep_que_nao_existe, '0d00c351521d734672810c2bf16073c8fadcead160f9ea13e2425a52', nome_questao='status_certo_de_cep_que_nao_existe'), 'status_certo_de_cep_que_nao_existe incorreta'
    assert verifica(status_viacep_de_cep_que_nao_existe, '2c5d8e141873b5847aee02e8cbffa8119457b89e36d59738037c06c6', nome_questao='status_viacep_de_cep_que_nao_existe'), 'status_viacep_de_cep_que_nao_existe incorreta'
    print('Desafio - multipla escolha da Fase 5: OK')

    # uma chamada de cada, guardada numa variavel - dois pedidos, nao
    # quatro. Eh a mesma economia da Fase 4, agora no desafio.
    status_da_mirtes = status_do_cep(cep_da_mirtes)
    status_do_inventado = status_do_cep('99999999')

    assert status_da_mirtes == 200, 'o CEP da Mirtes existe: deu certo'
    assert status_do_inventado == status_da_mirtes, \
        'o ViaCEP responde o MESMO numero pros dois - eh essa a surpresa'

    print(f'CEP que existe    ({cep_da_mirtes}): {status_da_mirtes}')
    print(f'CEP que nao existe (99999999): {status_do_inventado}')
    print('Desafio - status_do_cep: OK')


'''
EXERCICIO (d)

Q8 - por_que_o_json_estourou

Um colega tentou buscar o CEP '123' (curto demais) e o programa dele
quebrou com esta mensagem:

    JSONDecodeError: Expecting value: line 1 column 1 (char 0)

Nesse caso o ViaCEP responde 400, e o corpo da resposta NAO eh um
dicionario: eh uma pagina HTML de erro, daquelas de olhar no navegador.

Por que o .json() estourou?

    a) porque o CEP '123' nao existe
    b) porque o requests recusa CEP com menos de 8 digitos
    c) porque o status 400 faz o .json() levantar erro sozinho
    d) porque o .json() tenta ler o corpo como dicionario, e o corpo era
       uma pagina HTML - nao ha dicionario nenhum ali pra ler
'''
por_que_o_json_estourou = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('por_que_o_json_estourou')

if desafio:
    assert verifica(por_que_o_json_estourou, '7fd1f90176c471cd3973d4507504ddf8df3d3e6e908d0f2a90a3f33a', nome_questao='por_que_o_json_estourou'), 'por_que_o_json_estourou incorreta'
    print('Desafio - por que o json estourou: OK')


'''
EXERCICIO (e)

Agora a irma que faltou la na Fase 3. Faca a funcao cep_existe(cep) que
recebe o CEP, busca, e responde se aquele CEP existe.

Ela eh a irma mais util da lista - "esse CEP existe?" eh pergunta que se
faz sozinha, sem voce ter baixado nada antes. E ela so pode aparecer
AQUI, porque testar ela de verdade exige pedir um CEP que nao existe.

Repare no que voce acabou de descobrir: o status NAO serve pra responder
isso - ele vem 200 nos dois casos. Quem sabe eh a achou_endereco, olhando
a chave 'erro'. Entao esta funcao eh a de sempre: busca, e entrega pra
pura.

    >>> cep_existe('50030230')
    True
    >>> cep_existe('99999999')
    False
'''
def cep_existe(cep):
    pass


if desafio:
    assert cep_existe(cep_da_mirtes) == True, 'o CEP da Mirtes existe'
    assert cep_existe('99999999') == False, 'o 99999999 nao existe'

    # a irma tem que dar o mesmo que a pura sobre o mesmo CEP
    assert cep_existe(cep_do_cicero) == achou_endereco(endereco_do_cicero), \
        'a irma tem que concordar com a pura'
    print('Desafio - cep_existe: OK')
    print('\n=== DESAFIO DA FASE 5 COMPLETO! ===')
