# Lista de exercicios - viagem (APIs com requests)
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
        from explicacao_viagem import EXPLICACOES
    except ImportError:
        print("Arquivo 'explicacao_viagem.py' nao foi encontrado.")
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
# do jeito que o enunciado manda.
import os
_PASTA = os.path.dirname(os.path.abspath(__file__))
try:
    import requests_cache
    requests_cache.install_cache(os.path.join(_PASTA, 'cache_api'),
                                 expire_after=43200, stale_if_error=True)
except ImportError:
    print('AVISO: a biblioteca requests_cache nao esta instalada nesta maquina.')
    print('       A lista roda normalmente assim mesmo, com o cache de reserva.')
    print('       Quando puder, rode:  pip install -r requirements.txt')
    print()
try:
    import apoio_rede
except ImportError:
    print('AVISO: o arquivo apoio_rede.py deveria estar nesta pasta.')
    print('       Ele vem JUNTO com este exercicio - peca ao professor.')
    print('       A lista nao roda sem ele')
    exit()
# fim da rede


# So mude a variavel abaixo se o professor pedir
desligar_testes_frageis = False

if desligar_testes_frageis:
    print('ATENCAO: os testes frageis estao desligados (4 exercicios nao serao conferidos)')


# ===== FASE 1 - A primeira API: o cambio =====

'''
EXPLICACAO

A Helena vai viajar pra Lisboa e o Helio vai pra Toquio. Os dois querem
saber as mesmas duas coisas antes de fechar a mala: quanto vale o
dinheiro deles la, e que tempo faz la.

Comecamos pelo dinheiro. Abra este endereco no seu navegador, agora:

    https://api.frankfurter.dev/v1/2024-07-01?from=BRL&to=EUR,USD,JPY

Voce vai ver um dicionario. Ele diz quanto valia um real em euro, dolar e
iene no dia 1 de julho de 2024, e eh EXATAMENTE ele que estas duas linhas
trazem pra dentro do Python:

    import requests
    cambio = requests.get('https://api.frankfurter.dev/v1/2024-07-01?from=BRL&to=EUR,USD,JPY').json()

`requests.get(url)` busca o endereco. `.json()` transforma a resposta num
dicionario Python. E acabou - eh so isso que voce precisa saber de API
nesta lista. Todo o resto eh ler dicionario, que voce ja sabe.

Repare em duas partes do endereco, porque a sua funcao vai montar as
duas:

    o pedaco antes do `?` eh a DATA. Pode ser um dia (2024-07-01) ou a
    palavra `latest`, que quer dizer "a cotacao de hoje".

    o `from=BRL` eh a moeda que voce TEM (real), e o `to=EUR,USD,JPY` sao
    as que voce QUER - separadas por virgula, sem espaco.
'''

'''
EXERCICIO

Faca a funcao busca_cambio(moeda_base, moedas, data) que monta o endereco
do cambio com esses tres pedacos e devolve o dicionario que a API
responder.

Dica: monte a url com f-string, colocando os tres no meio.

    >>> busca_cambio('BRL', 'EUR', '2024-07-01')
    {'amount': 1.0, 'base': 'BRL', 'date': '2024-07-01', 'rates': {'EUR': 0.16662}}
'''
def busca_cambio(moeda_base, moedas, data):
    pass


cambio_julho = busca_cambio('BRL', 'EUR,USD,JPY', '2024-07-01')
cambio_de_hoje = busca_cambio('BRL', 'EUR,USD,JPY', 'latest')

assert cambio_julho != None, 'busca_cambio ainda nao devolve nada - complete a funcao acima'
assert cambio_julho['date'] == '2024-07-01', 'pedimos a cotacao daquele dia'
assert cambio_julho['rates']['EUR'] == 0.16662, 'o euro daquele dia'
assert cambio_de_hoje['base'] == 'BRL', 'pedimos a partir do real'
print(f'Baixado agora, do Frankfurter: {cambio_julho}')
print(f'E o de hoje: {cambio_de_hoje}')
print('Exercicio busca_cambio: OK')


breakpoint_aqui = 42

# PARE
# Voce acabou de baixar um dicionario. Antes de responder qualquer coisa,
# olhe ele por dentro - via pythontutor ou via o debug console do vscode
# (ponha um breakpoint na linha `breakpoint_aqui = 42` acima, rode com
# 'debug python file').
# Digite coisas como print(cambio_julho), print(cambio_julho['rates'])
# Depois tente chegar nos valores 0.16662, 'BRL' e 28.851.
# Experimente tambem print(cambio_julho.keys()) e veja a cara disso.
# Compare com o que aparece no navegador - eh o mesmo dicionario.
# Se nao conseguir, me chame.


'''
EXERCICIO

Considere o cambio_julho que voce acabou de baixar. Repare que ele tem
dicionario DENTRO de dicionario: 'rates' eh uma chave cujo valor eh outro
dicionario, de moeda -> numero.

Preencha as variaveis com uma EXPRESSAO Python que produz o valor (em vez
do valor literal). Se nao conseguir, comece pelo valor, mas depois tente
a expressao.

1) Qual a cotacao do euro?          Dica: ...['rates']['EUR']
2) Qual a moeda base?
3) De que dia eh essa cotacao?
4) Quantas chaves tem o dicionario de cima (o cambio_julho inteiro)?
                                    Dica: len(cambio_julho.keys())
5) Quantas moedas vieram na resposta?
                                    Dica: eh o len do dicionario de dentro
'''
cotacao_do_euro          = 'coloque o valor aqui'
moeda_base               = 'coloque o valor aqui'
data_do_cambio           = 'coloque o valor aqui'
quantas_chaves_no_cambio = 'coloque o valor aqui'
quantas_moedas           = 'coloque o valor aqui'

# Travou? Descomente a linha da questao para ler a explicacao:
# explicar('cotacao_do_euro')
# explicar('moeda_base')
# explicar('data_do_cambio')
# explicar('quantas_chaves_no_cambio')
# explicar('quantas_moedas')

assert verifica(cotacao_do_euro, '5f8aec8c9bf9517edd63e5371824083fd1d1cbf1bb43b9289bac4a29', nome_questao='cotacao_do_euro'), 'cotacao_do_euro incorreta'
assert verifica(moeda_base, 'bcedd974cf9a909f0af6b0ac1300ee7d2fe777bb686f685cb8747139', nome_questao='moeda_base'), 'moeda_base incorreta'
assert verifica(data_do_cambio, 'bf11c45d55211e1e620810d0f9d5309c35a928f8118ac5c7f2d1e89a', nome_questao='data_do_cambio'), 'data_do_cambio incorreta'
if not desligar_testes_frageis:
    assert verifica(quantas_chaves_no_cambio, 'aec23b5d2f077ce829ab926c633d9ea401359a0637cbaacafa9980d7', nome_questao='quantas_chaves_no_cambio'), 'quantas_chaves_no_cambio incorreta'
assert verifica(quantas_moedas,'ea78d996b0e8015f4a435b479717ceb50ccee50a54883a20b1543026', nome_questao='quantas_moedas'), 'quantas_moedas incorreta'
print('Exercicio lendo o cambio: OK')


'''
EXERCICIO

Q1 - o_que_o_json_devolve

    cambio = requests.get(url).json()

Depois dessa linha, o que a variavel `cambio` guarda?

    a) o endereco do site
    b) uma lista
    c) um dicionario
    d) o texto da pagina em HTML
'''
o_que_o_json_devolve = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('o_que_o_json_devolve')

assert verifica(o_que_o_json_devolve, 'f8d0a4a3523f9bcf1d5c1d18d8666b7b9dfd708de7edcd052280e575', nome_questao='o_que_o_json_devolve'), 'o_que_o_json_devolve incorreta'


'''
EXERCICIO

Q2 - chave_que_nao_existe

O cambio_julho nao tem nenhuma chave 'GBP' (a libra) - a gente nao pediu
a libra no endereco. O que o Python faz com

    cambio_julho['rates']['GBP']

    a) devolve None
    b) devolve uma string vazia
    c) devolve 0
    d) levanta KeyError e o programa para
'''
chave_que_nao_existe = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('chave_que_nao_existe')

assert verifica(chave_que_nao_existe, '1c6f5e7b80f0b7b13a04e0411ba1d827010a04fea098697524f5a27b', nome_questao='chave_que_nao_existe'), 'chave_que_nao_existe incorreta'


'''
EXERCICIO

Q3 - cambio_do_passado

Repare numa coisa estranha: logo depois do download, esta escrito no
arquivo

    assert cambio_julho['rates']['EUR'] == 0.16662

Um assert com o numero exato, em cima de dado que veio da internet agora.
Como isso pode dar certo sempre?

    a) porque o euro esta parado desde 2024
    b) porque aquele dia ja passou, e a cotacao dele nao muda mais
    c) porque a API inventa um numero fixo quando a data eh antiga
'''
cambio_do_passado = 'coloque o valor aqui'   # 'a', 'b' ou 'c'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('cambio_do_passado')

assert verifica(cambio_do_passado, 'faaeec925574d1e14888f0dcf2a16b178f3e5a3a5ff489d8a6b0ed99', nome_questao='cambio_do_passado'), 'cambio_do_passado incorreta'
print('Exercicio multipla escolha da Fase 1: OK')


# ===== FASE 2 - Os pares do cambio =====

'''
EXPLICACAO

Daqui pra frente as funcoes vem aos PARES.

A primeira de cada par eh PURA: ela recebe o dicionario por parametro e
so le. Nao vai a internet e nao sabe de onde veio o dicionario - por isso
a mesma funcao serve pro cambio de julho, pro de hoje e pro que voce
baixar daqui a um ano.

    cotacao(cambio_julho, 'EUR')     le um dicionario cambio_julho pronto

A segunda vai a API: ela nao recebe dicionario nenhum. Ela BUSCA um (com
a busca_cambio que voce acabou de escrever) e entrega pra irma pura fazer
a leitura.

    cotacao_de_hoje('EUR')           busca o de hoje, e ai le

Repare que a segunda costuma ser uma linha so, e que ela CHAMA a
primeira. Ninguem escreve o acesso ao dicionario duas vezes.
'''

'''
EXERCICIO

Faca a funcao cotacao(cambio, moeda) que devolve a cotacao daquela moeda
de dentro do dicionario recebido.

    >>> cotacao(cambio_julho, 'EUR')
    0.16662
'''
def cotacao(cambio, moeda):
    pass


# comeca num dicionario escrito aqui: a funcao tem que servir pra QUALQUER
# dicionario de cambio, inclusive um que nao veio da internet - e assim da
# pra conferir no valor exato, que eh mais facil de debugar
cambio_t = {'amount': 1.0, 'base': 'BRL', 'date': '1999-01-04', 'rates': {'EUR': 0.5}}
assert cotacao(cambio_t, 'EUR') == 0.5, 'a funcao tem que ler o dicionario que RECEBEU'

# e agora no dado de verdade que voce baixou, o cambio daquele 1 de julho
assert cotacao(cambio_julho, 'EUR') == 0.16662, 'cotacao do euro em 2024-07-01'
assert cotacao(cambio_julho, 'USD') == 0.17904, 'cotacao do dolar em 2024-07-01'
assert cotacao(cambio_julho, 'JPY') == 28.851, 'cotacao do iene em 2024-07-01'
print('Exercicio cotacao: OK')


'''
EXERCICIO

Agora a irma da API: faca a funcao cotacao_de_hoje(moeda) que devolve a
cotacao de HOJE daquela moeda, a partir do real.

Ela nao recebe dicionario: ela busca um. Sao duas funcoes que voce ja
tem - a busca_cambio traz o dicionario de hoje ('latest', a partir de
'BRL'), e a cotacao le ele.

    >>> cotacao_de_hoje('EUR')
    0.16632      # ou o que estiver valendo hoje
'''
def cotacao_de_hoje(moeda):
    pass


# guardamos numa variavel porque cada chamada dessas vai a internet - nao
# adianta pedir a mesma coisa quatro vezes
euro_hoje_t = cotacao_de_hoje('EUR')
assert euro_hoje_t > 0, 'a cotacao do euro eh um numero positivo'
assert euro_hoje_t == cotacao(cambio_de_hoje, 'EUR'), 'a irma da API tem que dar o mesmo que a pura'
print(f'Hoje 1 real vale {euro_hoje_t} euros')
print('Exercicio cotacao_de_hoje: OK')


'''
EXERCICIO

Q4 - o_que_significa_a_cotacao

No cambio_julho, 'base' eh 'BRL' e 'rates' tem 'EUR': 0.16662. O que esse
numero quer dizer?

    a) 1 real compra 0.16662 euros
    b) 1 euro custa 0.16662 reais
    c) a Helena tem 0.16662 euros
    d) o euro subiu 0.16662% naquele dia
'''
o_que_significa_a_cotacao = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('o_que_significa_a_cotacao')

assert verifica(o_que_significa_a_cotacao, '996daf2198855274892d05cf09be5b1f905cdf5e421a39aa889ecb3b', nome_questao='o_que_significa_a_cotacao'), 'o_que_significa_a_cotacao incorreta'


'''
EXERCICIO

De novo o calculo a mao antes da funcao - agora preenchendo com a
EXPRESSAO Python (a conta), nao com o numero ja calculado. Use as
cotacoes de 2024-07-01, que voce ja tem:

    1 real compra 0.16662 euros
    1 real compra 28.851 ienes

Quantos euros voce compra com 1000 reais? E quantos ienes? Escreva a
multiplicacao, e arredonde ela usando round, para dar as duas casas
decimais que é correto de se usar quando falamos de dinheiro

    round(numero, casas)   arredonda `numero` para `casas` casas decimais

    >>> round(3.14159, 2)
    3.14

Aqui 1000 * 0.16662 ja da 166.62 certinho e o round nao muda nada - mas eh
o habito certo, e no converte, logo abaixo, voce vai ver ele consertar uma
conta que sai com lixo de casas no fim.
'''

euros_de_1000_reais = 'coloque o valor aqui'   # a conta, tipo round(... * ..., 2)
ienes_de_1000_reais = 'coloque o valor aqui'   # idem

# Travou? Descomente a linha da questao para ler a explicacao:
# explicar('euros_de_1000_reais')
# explicar('ienes_de_1000_reais')

assert verifica(euros_de_1000_reais, '8c8fd17150505b04df452eb2eaba92f50cf230613a4c51064db1cce4', nome_questao='euros_de_1000_reais'), 'euros_de_1000_reais incorreta'
assert verifica(ienes_de_1000_reais, 'a9061a321357cd9948e25925f4e9099c033eabf0f4f425bda6d5308d', nome_questao='ienes_de_1000_reais'), 'ienes_de_1000_reais incorreta'
print('Exercicio conversao a mao: OK')


'''
EXERCICIO

Faca a funcao converte(cambio, moeda, valor) que devolve quanto o valor
(em reais) vira naquela moeda, arredondado para 2 casas com round(x, 2).

Dica: use a funcao cotacao que voce acabou de fazer.

    >>> converte(cambio_julho, 'EUR', 1000)
    166.62
'''
def converte(cambio, moeda, valor):
    pass


# primeiro num cambio escrito aqui, com cotacao redonda, pra conferir a
# conta no valor exato
cambio_t = {'amount': 1.0, 'base': 'BRL', 'date': '1999-01-04',
            'rates': {'EUR': 0.2, 'JPY': 30.0}}
assert converte(cambio_t, 'EUR', 100) == 20.0, '100 reais a 0.2 sao 20 euros'
assert converte(cambio_t, 'JPY', 0) == 0, 'zero real vira zero em qualquer moeda'
# 0.2 * 3 em float da 0.6000000000000001 - eh o round(x, 2) que devolve 0.6
assert converte(cambio_t, 'EUR', 3) == 0.6, 'faltou o round(x, 2)'

# e agora no cambio de verdade daquele 1 de julho
assert converte(cambio_julho, 'EUR', 1000) == 166.62, '1000 reais em euros'
assert converte(cambio_julho, 'JPY', 1000) == 28851.0, '1000 reais em ienes'
assert converte(cambio_julho, 'EUR', 0) == 0, 'zero real vira zero euro'
# 2500 * 0.16662 da 416.54999999999995 - o round(x, 2) devolve 416.55
assert converte(cambio_julho, 'EUR', 2500) == 416.55, 'faltou o round(x, 2)'
print('Exercicio converte: OK')


'''
EXERCICIO

E a irma dela: faca a funcao converte_hoje(moeda, valor) que devolve
quanto aquele valor em reais vira naquela moeda, com o cambio de HOJE.

De novo eh buscar e delegar - a busca_cambio traz, a converte faz a
conta.

    >>> converte_hoje('EUR', 1000)
    166.32      # ou o que der com a cotacao de hoje
'''
def converte_hoje(moeda, valor):
    pass


euros_hoje_t = converte_hoje('EUR', 1000)
assert euros_hoje_t > 0, '1000 reais viram algum dinheiro em euro'
assert euros_hoje_t == converte(cambio_de_hoje, 'EUR', 1000), 'a irma da API tem que dar o mesmo que a pura'
assert converte_hoje('EUR', 0) == 0, 'zero real vira zero euro em qualquer dia'
print(f'Hoje 1000 reais compram {euros_hoje_t} euros')
print('Exercicio converte_hoje: OK')


'''
EXERCICIO

Faca a funcao moeda_disponivel(cambio, moeda) que devolve True se aquela
moeda esta entre as que vieram na resposta.

Essa nao tem irma na API: ela existe pra perguntar sobre um dicionario
que voce JA baixou, antes de tentar ler uma chave que pode nao estar la.

    >>> moeda_disponivel(cambio_julho, 'EUR')
    True
    >>> moeda_disponivel(cambio_julho, 'GBP')
    False
'''
def moeda_disponivel(cambio, moeda):
    pass


# primeiro num cambio escrito aqui
cambio_t = {'amount': 1.0, 'base': 'BRL', 'date': '1999-01-04',
            'rates': {'EUR': 0.2, 'USD': 0.18}}
assert moeda_disponivel(cambio_t, 'EUR') == True, 'o euro esta em rates'
assert moeda_disponivel(cambio_t, 'GBP') == False, 'a libra nao esta em rates'
assert moeda_disponivel(cambio_t, 'BRL') == False, 'o real eh a base, nao entra em rates'

# e agora no cambio de verdade
assert moeda_disponivel(cambio_julho, 'EUR') == True, 'o euro veio'
assert moeda_disponivel(cambio_julho, 'JPY') == True, 'o iene veio'
assert moeda_disponivel(cambio_julho, 'GBP') == False, 'a libra nao foi pedida, entao nao veio'
assert moeda_disponivel(cambio_julho, 'BRL') == False, 'o real eh a BASE, nao esta em rates'
assert moeda_disponivel(cambio_de_hoje, 'USD') == True, 'o dolar de hoje tambem veio'
print('Exercicio moeda_disponivel: OK')


# ===== FASE 3 - A segunda API: o clima =====

'''
EXPLICACAO

Segunda API, mesma historia. Abra no navegador:

    https://api.open-meteo.com/v1/forecast?latitude=38.72&longitude=-9.14&current_weather=true

De novo um dicionario, e de novo sao as mesmas duas linhas pra trazer ele
pro Python. Essa API eh de clima, e aquelas duas coordenadas sao Lisboa.

Mas ha uma diferenca grande em relacao ao cambio de 2024-07-01: este dado
MUDA. A resposta eh o tempo de AGORA, e ela se atualiza a cada 15
minutos. A temperatura que voce vir hoje nao serve de resposta amanha.

Por isso, nesta fase, as perguntas com resposta fixa nao sao sobre os
NUMEROS - sao sobre a FORMA da resposta: em que unidade vem cada coisa,
quantas chaves tem, que chave existe e que chave nao existe. Isso nao
muda quando o tempo muda.

Repare tambem que a resposta tem dois dicionarios GEMEOS por dentro:

    'current_weather'        o que esta acontecendo    -> 25.7
    'current_weather_units'  em que unidade            -> '°C'

Os dois tem as mesmas chaves dentro. Um guarda o numero, o outro guarda a
unidade daquele numero.
'''

'''
EXERCICIO

Faca a funcao busca_clima(latitude, longitude) que monta o endereco do
clima com essas coordenadas e devolve o dicionario que a API responder.

    >>> busca_clima(38.72, -9.14)['current_weather']['temperature']
    25.7      # ou o que estiver fazendo agora em Lisboa
'''
def busca_clima(latitude, longitude):
    pass


clima_lisboa = busca_clima(38.72, -9.14)      # a Helena vai pra Lisboa
clima_toquio = busca_clima(35.68, 139.69)     # o Helio vai pra Toquio

assert clima_lisboa != None, 'busca_clima ainda nao devolve nada - complete a funcao acima'
assert 'current_weather' in clima_lisboa.keys(), 'a resposta tem que ter a chave current_weather'
assert -60 < clima_lisboa['current_weather']['temperature'] < 60, 'isso nao eh uma temperatura da Terra'
assert -60 < clima_toquio['current_weather']['temperature'] < 60, 'isso nao eh uma temperatura da Terra'
print(f'Baixado agora, do open-meteo: {clima_lisboa["current_weather"]}')
print('Exercicio busca_clima: OK')

# Olhe esse dicionario por dentro tambem, como voce fez com o do cambio -
# ele tem um nivel a mais de coisas pra explorar. Experimente
# print(clima_lisboa.keys()) e print(clima_lisboa['current_weather_units'])


'''
EXERCICIO

Considere o clima_lisboa que voce acabou de baixar. Use EXPRESSAO Python.

Todas estas cinco perguntas sao sobre coisas que NAO mudam com o tempo -
por isso elas tem resposta fixa, mesmo o dicionario sendo baixado na
hora.

1) Em que unidade vem a temperatura?
                              Dica: esta no dicionario gemeo, o de units
2) E em que unidade vem a velocidade do vento?
3) Quantas chaves tem o dicionario de cima (o clima_lisboa inteiro)?
                              Dica: len(clima_lisboa.keys()) - e conte
                              todas, ate as que voce acha inuteis
4) Qual a elevacao (altitude, em metros) daquele ponto?
                              Dica: essa esta no topo, um colchete so
5) Existe previsao de amanha nessa resposta? Ou seja: 'daily' eh uma das
   chaves do clima_lisboa?    Dica: 'daily' in clima_lisboa.keys()
'''
unidade_da_temperatura  = 'coloque o valor aqui'
unidade_do_vento        = 'coloque o valor aqui'
quantas_chaves_no_clima = 'coloque o valor aqui'
elevacao_de_lisboa      = 'coloque o valor aqui'
tem_previsao_de_amanha  = 'coloque o valor aqui'

# Travou? Descomente a linha da questao para ler a explicacao:
# explicar('unidade_da_temperatura')
# explicar('unidade_do_vento')
# explicar('quantas_chaves_no_clima')
# explicar('elevacao_de_lisboa')
# explicar('tem_previsao_de_amanha')

assert verifica(unidade_da_temperatura, 'e0748c0b87fc5eb0e030bcc0413cce8a0d653cfba5a244203a8d4dc9', nome_questao='unidade_da_temperatura'), 'unidade_da_temperatura incorreta'
assert verifica(unidade_do_vento, 'ace6299fb7f60f864276c5d3093ad7e72564622e46d405af98bf6fdc', nome_questao='unidade_do_vento'), 'unidade_do_vento incorreta'
if not desligar_testes_frageis:
    assert verifica(quantas_chaves_no_clima, 'bbc6cab5b80e71a1d2cda842d08e13bb46fa8193159f90b427a6f998', nome_questao='quantas_chaves_no_clima'), 'quantas_chaves_no_clima incorreta'
    assert verifica(elevacao_de_lisboa, 'fa1c11a0ae63a9d2f6bcd5adf4203e342aa053d0604f68e9fd614573', nome_questao='elevacao_de_lisboa'), 'elevacao_de_lisboa incorreta'
assert verifica(tem_previsao_de_amanha,'007b5398eaa221447d643cb79d9dcbe3c685317d39ed4f20d180d663', nome_questao='tem_previsao_de_amanha'), 'tem_previsao_de_amanha incorreta'
print('Exercicio lendo o clima: OK')


'''
EXERCICIO

Q5 - onde_esta_a_temperatura

Qual destas expressoes devolve o NUMERO da temperatura de agora (algo
como 25.7)?

    a) clima_lisboa['temperature']
    b) clima_lisboa['current_weather_units']['temperature']
    c) clima_lisboa['current_weather']['temperature']
    d) clima_lisboa[0]['temperature']
'''
onde_esta_a_temperatura = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('onde_esta_a_temperatura')

assert verifica(onde_esta_a_temperatura, '0d6f6ea84c9595ff322f97e5f77560b49ec4381d6f8639f68f95a070', nome_questao='onde_esta_a_temperatura'), 'onde_esta_a_temperatura incorreta'


'''
EXERCICIO

Q6 - por_que_faixa

Repare no teste do busca_clima: em vez de comparar a temperatura com um
numero, ele confere se ela esta ENTRE -60 e 60. Por que aqui nao da pra
fazer como no cambio de 2024-07-01, que foi conferido no valor exato?

    a) porque assert nao funciona com float
    b) porque a API do clima devolve um numero aleatorio
    c) porque a temperatura vem como texto e nao da pra comparar
    d) porque a temperatura de agora muda - o valor de hoje nao serviria
       de resposta amanha e o teste ia quebrar
'''
por_que_faixa = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('por_que_faixa')

assert verifica(por_que_faixa, '37fd59d96ed726d516c7d962ca6cd0010dbb244c07b442be754a7ef0', nome_questao='por_que_faixa'), 'por_que_faixa incorreta'
print('Exercicio multipla escolha da Fase 3: OK')


# ===== FASE 4 - Os pares do clima =====

'''
EXPLICACAO

Mesma dupla de antes: a funcao pura recebe uma previsao ja baixada e le;
a irma da API vai buscar uma previsao e entrega pra ela.

Uma diferenca em relacao ao cambio: como o tempo muda, os testes das
funcoes puras usam previsoes pequenas escritas aqui no arquivo, com
numeros fixos. Assim da pra conferir o resultado exato. Depois, a mesma
funcao roda em cima do clima de verdade que voce baixou - e ai o teste so
confere o que nao muda.
'''

'''
EXERCICIO

Faca a funcao temperatura(previsao) que devolve a temperatura de dentro
da previsao. Eh o acesso de dois passos da fase anterior.

    >>> temperatura(clima_lisboa)
    25.7      # ou o que estiver fazendo agora
'''
def temperatura(previsao):
    pass


previsao_t = {'current_weather': {'temperature': 17.2, 'windspeed': 2.9, 'weathercode': 2}}
assert temperatura(previsao_t) == 17.2, 'a temperatura dessa previsao eh 17.2'
previsao_t = {'current_weather': {'temperature': 8.6, 'windspeed': 5.0, 'weathercode': 3}}
assert temperatura(previsao_t) == 8.6, 'a temperatura dessa previsao eh 8.6'
# e agora no dado de verdade, onde so da pra conferir a faixa
assert -60 < temperatura(clima_lisboa) < 60, 'a temperatura de Lisboa agora'
assert -60 < temperatura(clima_toquio) < 60, 'a temperatura de Toquio agora'
print('Exercicio temperatura: OK')


'''
EXERCICIO

A irma da API: faca a funcao temperatura_agora(latitude, longitude) que
devolve quantos graus estao fazendo AGORA naquele ponto do mundo.

De novo eh buscar e delegar, numa linha so.

    >>> temperatura_agora(38.72, -9.14)
    25.7      # ou o que estiver fazendo agora em Lisboa
'''
def temperatura_agora(latitude, longitude):
    pass


lisboa_agora_t = temperatura_agora(38.72, -9.14)
toquio_agora_t = temperatura_agora(35.68, 139.69)
assert -60 < lisboa_agora_t < 60, 'a temperatura de Lisboa agora'
assert -60 < toquio_agora_t < 60, 'a temperatura de Toquio agora'
print(f'Agora em Lisboa: {lisboa_agora_t} graus, e em Toquio: {toquio_agora_t} graus')
print('Exercicio temperatura_agora: OK')


'''
EXERCICIO

Faca a funcao esta_ventando(previsao, limite) que devolve True se a
velocidade do vento (windspeed) for MAIOR que o limite.

    >>> esta_ventando({'current_weather': {'windspeed': 5.0}}, 4)
    True
'''
def esta_ventando(previsao, limite):
    pass


previsao_t = {'current_weather': {'temperature': 8.6, 'windspeed': 5.0, 'weathercode': 3}}
assert esta_ventando(previsao_t, 4) == True, 'vento 5.0 passa de 4'
assert esta_ventando(previsao_t, 5) == False, 'vento 5.0 NAO passa de 5 (tem que ser maior)'
previsao_t = {'current_weather': {'temperature': 17.2, 'windspeed': 2.9, 'weathercode': 2}}
assert esta_ventando(previsao_t, 2) == True, 'vento 2.9 passa de 2'
assert esta_ventando(previsao_t, 10) == False, 'vento 2.9 nao passa de 10'
print('Exercicio esta_ventando: OK')


'''
EXPLICACAO

A previsao nao vem com "parcialmente nublado" escrito. Vem com um NUMERO,
na chave 'weathercode' - eh um codigo internacional. Quem traduz o codigo
pra portugues eh um dicionario nosso, este aqui:
'''

# Este dicionario ja vem pronto. Nao mexa aqui.
CODIGOS_DO_TEMPO = {
    0: 'ceu limpo',
    1: 'quase limpo',
    2: 'parcialmente nublado',
    3: 'nublado',
    51: 'chuvisco fraco',
    53: 'chuvisco',
    55: 'chuvisco forte',
    61: 'chuva fraca',
    63: 'chuva',
    80: 'pancadas de chuva',
}

'''
EXERCICIO

Q7 - como_perguntar_pelo_codigo

Repare que a tabela acima esta INCOMPLETA de proposito: existem codigos
do tempo que nao estao nela (o 45, por exemplo, que eh nevoa).

A funcao que voce vai escrever daqui a pouco recebe `codigos` (essa
tabela) e precisa se defender de um codigo que nao esta la. Qual destas
linhas pergunta "esse codigo esta no dicionario?" sem estourar?

    a) if codigos[codigo] != None:
    b) if codigo in codigos.keys():
    c) if codigo in codigos.values():
    d) if codigos.keys() == codigo:
'''
como_perguntar_pelo_codigo = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('como_perguntar_pelo_codigo')

assert verifica(como_perguntar_pelo_codigo, '1d4ee8318fa742992ad9b8ec8ce27ef26747da4bdcfa3c6bcd6d27a0', nome_questao='como_perguntar_pelo_codigo'), 'como_perguntar_pelo_codigo incorreta'


'''
EXERCICIO

Calculo a mao, antes da proxima funcao.

Voce vai escrever uma funcao que recebe uma previsao e devolve o texto do
tempo, usando a tabela CODIGOS_DO_TEMPO acima. Quando o codigo nao
estiver na tabela, ela devolve a string 'nao sei dizer'.

O que essa funcao responderia para estas duas previsoes? (Olhe no dicionario
que definimos acima os weathercodes)

    {'current_weather': {'temperature': 8.6, 'weathercode': 3}}
    {'current_weather': {'temperature': 12.0, 'weathercode': 45}}
'''
descricao_do_codigo_3  = 'coloque o valor aqui'
descricao_do_codigo_45 = 'coloque o valor aqui'

# Travou? Descomente a linha da questao para ler a explicacao:
# explicar('descricao_do_codigo_3')
# explicar('descricao_do_codigo_45')

assert verifica(descricao_do_codigo_3, 'd02ad71347f8820623e55a0fc6537508d97ab453f720f9ef15fbf17b', nome_questao='descricao_do_codigo_3'), 'descricao_do_codigo_3 incorreta'
assert verifica(descricao_do_codigo_45, '5b1493f0042bb57d962a02dd6f72689bb0e097b1a454d21cdbbb837d', nome_questao='descricao_do_codigo_45'), 'descricao_do_codigo_45 incorreta'
print('Exercicio traduzindo o codigo do tempo: OK')


'''
EXERCICIO

Faca a funcao descricao_do_tempo(previsao, codigos) que devolve o texto
correspondente ao 'weathercode' da previsao. Se o codigo NAO estiver no
dicionario de codigos, devolva a string 'nao sei dizer'.

    >>> descricao_do_tempo({'current_weather': {'weathercode': 3}}, CODIGOS_DO_TEMPO)
    'nublado'
'''
def descricao_do_tempo(previsao, codigos):
    pass


previsao_t = {'current_weather': {'temperature': 17.2, 'windspeed': 2.9, 'weathercode': 2}}
assert descricao_do_tempo(previsao_t, CODIGOS_DO_TEMPO) == 'parcialmente nublado', 'codigo 2'
previsao_t = {'current_weather': {'temperature': 8.6, 'windspeed': 5.0, 'weathercode': 3}}
assert descricao_do_tempo(previsao_t, CODIGOS_DO_TEMPO) == 'nublado', 'codigo 3'

# um dia de nevoa: o codigo 45 nao esta na nossa tabela
previsao_t = {'current_weather': {'temperature': 12.0, 'windspeed': 1.0, 'weathercode': 45}}
assert descricao_do_tempo(previsao_t, CODIGOS_DO_TEMPO) == 'nao sei dizer', 'codigo fora da tabela'

# e uma tabela menor ainda, so pra confirmar que a funcao usa o dicionario
# que RECEBEU, e nao o CODIGOS_DO_TEMPO por fora
codigos_t = {2: 'sol entre nuvens'}
previsao_t = {'current_weather': {'temperature': 17.2, 'windspeed': 2.9, 'weathercode': 2}}
assert descricao_do_tempo(previsao_t, codigos_t) == 'sol entre nuvens', 'a funcao tem que usar o dicionario recebido'
previsao_t = {'current_weather': {'temperature': 8.6, 'windspeed': 5.0, 'weathercode': 3}}
assert descricao_do_tempo(previsao_t, codigos_t) == 'nao sei dizer', 'o 3 nao esta na tabela pequena'

# no dado de verdade nao da pra saber que tempo vai estar fazendo - mas da
# pra conferir que a funcao devolve algum texto
assert descricao_do_tempo(clima_lisboa, CODIGOS_DO_TEMPO) != '', 'alguma descricao tem que sair'
print(f'Tempo agora em Lisboa: {descricao_do_tempo(clima_lisboa, CODIGOS_DO_TEMPO)}')
print('Exercicio descricao_do_tempo: OK')


'''
EXERCICIO

Calculo a mao, antes da ultima funcao da fase.

A regra da Helena eh simples: ela leva casaco se a temperatura for MENOR
que 15 graus.

Estas sao tres temperaturas que a API ja devolveu, em dias diferentes:

    Lisboa    17.2 graus
    Toquio    31.4 graus
    Reykjavik  8.6 graus

Responda True ou False para cada uma: leva casaco?
'''
casaco_em_lisboa    = 'coloque o valor aqui'
casaco_em_toquio    = 'coloque o valor aqui'
casaco_em_reykjavik = 'coloque o valor aqui'

# Travou? Descomente a linha da questao para ler a explicacao:
# explicar('casaco_em_lisboa')
# explicar('casaco_em_toquio')
# explicar('casaco_em_reykjavik')

assert verifica(casaco_em_lisboa, 'fc6ff660924581b0eda1acabe6560e616c2b682dac475eaee9855260', nome_questao='casaco_em_lisboa'), 'casaco_em_lisboa incorreta'
assert verifica(casaco_em_toquio, '9889fd2628cd4b72f748008c26a64c0f1c3554885bd9edf66e474853', nome_questao='casaco_em_toquio'), 'casaco_em_toquio incorreta'
assert verifica(casaco_em_reykjavik, '1cbc6c2cabb23adfae25747ff02d52af02d448f0031279ec941c1de8', nome_questao='casaco_em_reykjavik'), 'casaco_em_reykjavik incorreta'
print('Exercicio casaco a mao: OK')


'''
EXERCICIO

Faca a funcao leva_casaco(previsao) que devolve True se a temperatura for
menor que 15.

Dica: voce ja tem a funcao temperatura(previsao). Use ela aqui dentro -
nao repita o acesso aos dois colchetes.

    >>> leva_casaco({'current_weather': {'temperature': 8.6}})
    True
'''
def leva_casaco(previsao):
    pass


previsao_t = {'current_weather': {'temperature': 17.2, 'windspeed': 2.9, 'weathercode': 2}}
assert leva_casaco(previsao_t) == False, '17.2 nao leva casaco'
previsao_t = {'current_weather': {'temperature': 8.6, 'windspeed': 5.0, 'weathercode': 3}}
assert leva_casaco(previsao_t) == True, '8.6 leva casaco'

# quase passa: 15 nao eh MENOR que 15
previsao_t = {'current_weather': {'temperature': 15, 'windspeed': 0, 'weathercode': 0}}
assert leva_casaco(previsao_t) == False, 'exatamente 15 nao leva casaco'
previsao_t = {'current_weather': {'temperature': 14.9, 'windspeed': 0, 'weathercode': 0}}
assert leva_casaco(previsao_t) == True, '14.9 leva casaco'
print('Exercicio leva_casaco: OK')


'''
EXERCICIO

A ultima irma da API: faca a funcao leva_casaco_agora(latitude,
longitude) que responde se, AGORA, quem esta naquele ponto do mundo
precisa de casaco.

    >>> leva_casaco_agora(64.15, -21.94)
    True      # ou False, dependendo do dia em Reykjavik
'''
def leva_casaco_agora(latitude, longitude):
    pass


# aqui nao da pra conferir True nem False: depende do tempo de agora. O
# que da pra exigir eh que a resposta seja uma das duas.
casaco_lisboa_t = leva_casaco_agora(38.72, -9.14)
casaco_reykjavik_t = leva_casaco_agora(64.15, -21.94)
assert casaco_lisboa_t in [True, False], 'a resposta tem que ser True ou False'
assert casaco_reykjavik_t in [True, False], 'a resposta tem que ser True ou False'
print(f'Casaco agora em Lisboa? {casaco_lisboa_t}. E em Reykjavik? {casaco_reykjavik_t}')
print('Exercicio leva_casaco_agora: OK')


# ===== FASE 5 - A viagem da Helena e a do Helio =====

'''
EXERCICIO

Calculo a mao antes da simulacao. Use as cotacoes de 2024-07-01
(1 real = 0.16662 euros, 1 real = 28.851 ienes) e arredonde para 2 casas.

A Helena vai levar 2500 reais para Lisboa. Quantos euros ela compra?
O Helio vai levar 4000 reais para Toquio. Quantos ienes ele compra?
'''
euros_da_helena = 'coloque o valor aqui'
ienes_do_helio  = 'coloque o valor aqui'

# Travou? Descomente a linha da questao para ler a explicacao:
# explicar('euros_da_helena')
# explicar('ienes_do_helio')

assert verifica(euros_da_helena, '03cd2ab1594ef3c01f34976de6e305da1fc73070fd6f64f2d702fdef', nome_questao='euros_da_helena'), 'euros_da_helena incorreta'
assert verifica(ienes_do_helio, 'fbc34cc74c9153f0397214446acf6d12092e2eccfc044eb2e6710619', nome_questao='ienes_do_helio'), 'ienes_do_helio incorreta'
print('Exercicio dinheiro a mao: OK')


# Agora o fluxo inteiro, com TODAS as funcoes da lista, para os dois
# viajantes. Repare que a mesma funcao serve aos dois - o que muda sao os
# argumentos.

reais_helena = 2500
reais_helio = 4000

# 1) com as funcoes PURAS, em cima do cambio daquele 1 de julho. Como
#    aquele dia nao muda mais, da pra conferir o valor exato.
assert converte(cambio_julho, 'EUR', reais_helena) == 416.55, 'euros da Helena em 2024-07-01'
assert converte(cambio_julho, 'JPY', reais_helio) == 115404.0, 'ienes do Helio em 2024-07-01'
assert moeda_disponivel(cambio_julho, 'EUR') == True, 'a Helena pediu euro'
assert moeda_disponivel(cambio_julho, 'JPY') == True, 'o Helio pediu iene'

# 2) e agora no mundo de hoje.
#
#    Repare no que acontece aqui: sao QUATRO perguntas sobre cada viajante
#    (temperatura, tempo, casaco, dinheiro), e cada uma delas tem uma irma
#    na API. Se a gente chamasse as irmas, seriam oito idas a internet
#    buscar as mesmas quatro respostas.
#
#    Entao baixa-se UMA vez cada dicionario, e daqui pra baixo eh tudo
#    funcao pura. Eh pra isso que elas existem. As irmas da API valem
#    quando a pergunta eh uma so - eh o caso do menu, la embaixo.
previsao_helena = busca_clima(38.72, -9.14)      # Lisboa
previsao_helio = busca_clima(35.68, 139.69)      # Toquio
cambio_helena = busca_cambio('BRL', 'EUR', 'latest')
cambio_helio = busca_cambio('BRL', 'JPY', 'latest')

print()
print('=== A VIAGEM DA HELENA (Lisboa) ===')
print(f'tempo agora:  {temperatura(previsao_helena)} graus, '
      f'{descricao_do_tempo(previsao_helena, CODIGOS_DO_TEMPO)}')
print(f'leva casaco:  {leva_casaco(previsao_helena)}')
print(f'na carteira:  {converte(cambio_helena, "EUR", reais_helena)} euros')

print()
print('=== A VIAGEM DO HELIO (Toquio) ===')
print(f'tempo agora:  {temperatura(previsao_helio)} graus, '
      f'{descricao_do_tempo(previsao_helio, CODIGOS_DO_TEMPO)}')
print(f'leva casaco:  {leva_casaco(previsao_helio)}')
print(f'ventando?     {esta_ventando(previsao_helio, 10)}   (mais de 10 km/h)')
print(f'na carteira:  {converte(cambio_helio, "JPY", reais_helio)} ienes')
print()

# e aqui, sim, uma pergunta solta - uma so, sobre nada que ja esta na mao.
# Esse eh o caso em que a irma da API eh o caminho curto:
print(f'(so por curiosidade: hoje 1 real vale {cotacao_de_hoje("JPY")} ienes)')
print()

# o que da pra conferir no dado de hoje eh o que nao muda
assert moeda_disponivel(cambio_helena, 'EUR') == True, 'a Helena pediu euro'
assert moeda_disponivel(cambio_helio, 'JPY') == True, 'o Helio pediu iene'
assert converte(cambio_helena, 'EUR', reais_helena) > 0, 'a Helena tem algum dinheiro em euro'
assert converte(cambio_helio, 'JPY', reais_helio) > converte(cambio_helena, 'EUR', reais_helena), \
    'o iene eh uma moeda "pequena": 4000 reais viram MUITOS ienes'
assert -60 < temperatura(previsao_helena) < 60, 'a temperatura de Lisboa agora'
assert leva_casaco(previsao_helio) in [True, False], 'casaco em Toquio'
assert esta_ventando(previsao_helena, -1) == True, 'vento nenhum ainda eh maior que -1'
print('Exercicio simulacao integrada: OK')


# ===== A interface =====

def main():
    while True:
        print()
        print('=== PLANEJADOR DE VIAGEM ===')
        print('1. Quantos euros a Helena compra hoje')
        print('2. Que tempo faz agora em Lisboa (Helena)')
        print('3. Quantos ienes o Helio compra hoje')
        print('4. Que tempo faz agora em Toquio (Helio)')
        print('5. Sair')
        opcao = input('Opcao: ')

        if opcao == '1':
            # FUNCIONALIDADE 1 - perguntar quantos reais a Helena vai
            # levar e mostrar quanto isso da em euros com o cambio de
            # hoje. Repare que aqui voce nao tem dicionario nenhum na mao:
            # eh o caso das irmas da API.
            # Organize as pecas abaixo na ordem certa:
            #
            #     reais = int(input('  quantos reais? '))
            #     print(f'  da {converte_hoje("EUR", reais)} euros')
            #
            pass  # COMPLETE: monte a funcionalidade 1 com as pecas acima

        elif opcao == '2':
            # FUNCIONALIDADE 2 - mostrar a temperatura de agora em Lisboa
            # (latitude 38.72, longitude -9.14), se leva casaco e como
            # esta o tempo. Repare que a descricao precisa da PREVISAO
            # inteira, entao aqui uma das pecas baixa o dicionario e as
            # outras leem ele.
            # Organize as pecas abaixo na ordem certa:
            #
            #     previsao = busca_clima(38.72, -9.14)
            #     print(f'  {temperatura(previsao)} graus')
            #     print(f'  {descricao_do_tempo(previsao, CODIGOS_DO_TEMPO)}')
            #     print(f'  leva casaco: {leva_casaco(previsao)}')
            #
            pass  # COMPLETE: monte a funcionalidade 2 com as pecas acima

        elif opcao == '3':
            print('  [implementar: igual a opcao 1, mas com JPY no lugar de EUR]')

        elif opcao == '4':
            print('  [implementar: igual a opcao 2, mas com Toquio - latitude 35.68, longitude 139.69]')

        elif opcao == '5':
            break

        else:
            print('Opcao invalida')


# Pra rodar a interface, descomente:
# main()


print('\n=== PARABENS! Todos os exercicios completos! ===')


# ===== FASE 6 - DESAFIO (opcional) =====

'''
EXPLICACAO

Ate aqui voce sempre soube a latitude e a longitude do destino. E se o
usuario so souber o NOME da cidade?

Existe um terceiro endereco, da mesma casa do clima, que procura cidade
por nome. Abra no navegador:

    https://geocoding-api.open-meteo.com/v1/search?name=Recife&count=1&language=pt&format=json

Ele traz uma novidade: a resposta tem uma LISTA de dicionarios dentro, na
chave 'results' - porque pode existir mais de uma cidade com o mesmo
nome. Com `count=1` pedimos so a primeira.

Os asserts da Fase 6 ficam DESLIGADOS por padrao. Para ligar (e ver "OK"
conforme acerta), mude a flag `desafio` abaixo de False para True. Se nao
quiser fazer o desafio, deixe False.
'''


desafio = False    # ligue o desafio mudando para True


'''
EXERCICIO (a)

Faca a funcao busca_cidade(nome) que monta o endereco da busca por nome e
devolve o dicionario que a API responder. Eh a terceira funcao de busca
da lista, e a mais comprida - so nao se perca no meio da f-string.

    >>> busca_cidade('Recife')['results'][0]['name']
    'Recife'
'''
def busca_cidade(nome):
    pass


busca_recife = busca_cidade('Recife')

if desafio:
    assert busca_recife != None, 'busca_cidade ainda nao devolve nada'
    assert 'results' in busca_recife.keys(), 'a resposta tem que ter a chave results'
    print(f'Baixado agora, do geocoding: {busca_recife["results"][0]["name"]}')
    print('Desafio - busca_cidade: OK')


'''
EXERCICIO (b)

Q8 - results_eh_o_que

Olhe no navegador o que veio em 'results'. O que eh
`busca_recife['results']`?

    a) uma lista de dicionarios
    b) um dicionario
    c) uma string com o nome da cidade
'''
results_eh_o_que = 'coloque o valor aqui'   # 'a', 'b' ou 'c'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('results_eh_o_que')


'''
EXERCICIO (c)

Ainda sobre a resposta da busca por 'Recife': agora sao TRES passos ate o
valor - a chave 'results', a posicao [0] da lista, e a chave que voce
quer.

Use expressao Python. A variavel busca_recife eh o que a sua busca_cidade
trouxe, logo ali em cima.

1) Qual o nome da cidade achada?  Dica: ...['results'][0]['name']
2) Em que pais ela fica?
3) Qual a latitude dela?
4) Quantas cidades vieram na resposta?  Dica: len(...['results'])
'''
nome_da_cidade          = 'coloque o valor aqui'
pais_da_cidade          = 'coloque o valor aqui'
latitude_de_recife      = 'coloque o valor aqui'
quantas_cidades_achadas = 'coloque o valor aqui'

# Travou? Descomente a linha da questao para ler a explicacao:
# explicar('nome_da_cidade')
# explicar('pais_da_cidade')
# explicar('latitude_de_recife')
# explicar('quantas_cidades_achadas')

if desafio:
    assert verifica(results_eh_o_que, '546d046b2035ff62f592a284defac856d03d1e05e4a5a5fb2a0702ef', nome_questao='results_eh_o_que'), 'results_eh_o_que incorreta'
    assert verifica(nome_da_cidade, 'cf6147aaefdb7751a1826f34f2e371afcb86d1782b5f90a9211eaf44', nome_questao='nome_da_cidade'), 'nome_da_cidade incorreta'
    assert verifica(pais_da_cidade, '9c81b463c93ee5f075bca2549cd243865b113961139a6ee443f5ac88', nome_questao='pais_da_cidade'), 'pais_da_cidade incorreta'
    if not desligar_testes_frageis:
        assert verifica(latitude_de_recife, '7e33987de1ac31d5ec3ae204ca6d8629fab3f87e88e83e20ca033385', nome_questao='latitude_de_recife'), 'latitude_de_recife incorreta'
    assert verifica(quantas_cidades_achadas,'2e9d22ea3367c298afadb529ec026acfea06080b0db1a94d866d527c', nome_questao='quantas_cidades_achadas'), 'quantas_cidades_achadas incorreta'
    print('Desafio - lendo a busca por nome: OK')


'''
EXERCICIO (d)

Mais um par. Primeiro a funcao PURA: faca primeira_cidade(resposta) que
recebe uma resposta da busca por nome e devolve o DICIONARIO da primeira
cidade da lista.

    >>> primeira_cidade(busca_recife)['name']
    'Recife'
'''
def primeira_cidade(resposta):
    pass


'''
EXERCICIO (e)

E a irma da API: faca busca_coordenadas(cidade) que recebe o NOME da
cidade, baixa, e devolve a tupla (latitude, longitude) da primeira cidade
achada.

Dica: use a busca_cidade e a primeira_cidade que voce ja fez. E devolva a
tupla com parenteses: return (latitude, longitude).

    >>> busca_coordenadas('Recife')
    (-8.05389, -34.88111)
'''
def busca_coordenadas(cidade):
    pass


'''
EXERCICIO (f)

Junte tudo: faca clima_da_cidade(cidade) que recebe o NOME da cidade,
descobre as coordenadas dela e devolve a previsao do tempo de la.

Sao as duas APIs em sequencia - a saida de uma entra na outra.

    >>> temperatura(clima_da_cidade('Recife'))
    24.7      # ou o que estiver fazendo agora no Recife
'''
def clima_da_cidade(cidade):
    pass


if desafio:
    # primeiro numa resposta escrita aqui: primeira_cidade so pega o [0]
    # da lista que mora em 'results'
    resposta_t = {'results': [{'name': 'Olinda', 'country': 'Brasil'},
                              {'name': 'Olinda', 'country': 'Mexico'}]}
    assert primeira_cidade(resposta_t)['name'] == 'Olinda', 'a primeira da lista'
    assert primeira_cidade(resposta_t)['country'] == 'Brasil', 'a [0] eh a do Brasil'

    # e agora na resposta de verdade que voce baixou
    assert primeira_cidade(busca_recife)['name'] == 'Recife', 'a primeira cidade da busca por Recife'
    assert primeira_cidade(busca_recife)['country'] == 'Brasil', 'o pais da primeira cidade'

    if not desligar_testes_frageis:
        assert busca_coordenadas('Recife') == (-8.05389, -34.88111), 'coordenadas do Recife'

    previsao_recife = clima_da_cidade('Recife')
    assert 'current_weather' in previsao_recife.keys(), 'clima_da_cidade tem que devolver uma previsao'
    assert -60 < temperatura(previsao_recife) < 60, 'temperatura fora do que existe na Terra'
    print(f'Agora no Recife: {temperatura(previsao_recife)} graus, '
          f'{descricao_do_tempo(previsao_recife, CODIGOS_DO_TEMPO)}')
    print('Desafio - clima de qualquer cidade: OK')
    print('\n=== DESAFIO COMPLETO! ===')


# ===== FASE 7 - DESAFIO EXTRA: os parametros de url pela requests =====

'''
EXPLICACAO

Em toda funcao de busca desta lista voce montou o endereco INTEIRO com
f-string, colando o `?`, os `&` e o `=` na mao:

    url = f'https://api.frankfurter.dev/v1/{data}?from={base}&to={moedas}'
    url = f'https://geocoding-api.open-meteo.com/v1/search?name={nome}&count=1&language=pt&format=json'

Funciona. Mas a parte depois do `?` - os PARAMETROS - a propria requests poderia
montar pra voce. Voce passa um DICIONARIO no argumento `params=`:

    url = f'https://api.frankfurter.dev/v1/{data}'
    cambio = requests.get(url, params={'from': base, 'to': moedas}).json()

O dicionario `{'from': 'BRL', 'to': 'EUR,USD'}` vira `?from=BRL&to=EUR,USD`
sozinho - com o `?`, os `&` e ate o escape de caractere especial (a
virgula sai como %2C no endereco, e a API entende igual). Quanto mais
parametro o endereco tem, mais isso ajuda: a busca por cidade, com quatro,
eh o caso em que vale muito a pena.

Um cuidado no cambio: a `data` NAO vira parametro. Ela eh parte do
CAMINHO (`/v1/2024-07-01`), nao do `?...` - entao ela continua na
f-string. So o que ficava depois do `?` eh que vira dicionario.

Os asserts desta fase ficam DESLIGADOS por padrao. Para ligar, mude
`desafio_params` abaixo de False para True.
'''


desafio_params = False    # ligue o desafio extra mudando para True


'''
EXERCICIO (a)

Faca busca_cambio_params(moeda_base, moedas, data): o MESMO resultado da
busca_cambio da Fase 1, so que a f-string vai ate `/v1/{data}` e o resto
(`from`, `to`) entra num dicionario em params=.

    >>> busca_cambio_params('BRL', 'EUR', '2024-07-01')['rates']['EUR']
    0.16662
'''
def busca_cambio_params(moeda_base, moedas, data):
    pass


'''
EXERCICIO (b)

Faca busca_clima_params(latitude, longitude): o mesmo resultado da
busca_clima da Fase 3. Aqui o endereco antes do `?` eh so
`https://api.open-meteo.com/v1/forecast`; latitude, longitude e
current_weather sao os tres parametros.

Dica: current_weather entra no dicionario como a string 'true'.

    >>> busca_clima_params(38.72, -9.14)['current_weather']['temperature']
    25.7      # ou o que estiver fazendo agora em Lisboa
'''
def busca_clima_params(latitude, longitude):
    pass


'''
EXERCICIO (c)

Faca busca_cidade_params(nome): o mesmo resultado da busca_cidade do
desafio anterior. Sao QUATRO parametros - name, count, language, format -
e eh aqui que o dicionario deixa o codigo bem mais curto que a f-string.

    >>> busca_cidade_params('Recife')['results'][0]['name']
    'Recife'
'''
def busca_cidade_params(nome):
    pass


'''
EXERCICIO (d)

Q9 - o_que_params_monta

Rodando

    requests.get('https://api.open-meteo.com/v1/forecast',
                 params={'latitude': 38.72, 'longitude': -9.14})

o que a requests colou no endereco antes de bater na API?

    a) /forecast/38.72/-9.14
    b) ?latitude=38.72&longitude=-9.14
    c) {'latitude': 38.72, 'longitude': -9.14}
    d) nada - params so vale pra requisicao POST
'''
o_que_params_monta = 'coloque o valor aqui'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('o_que_params_monta')


if desafio_params:
    # cada _params tem que devolver EXATAMENTE o que a versao com f-string
    # devolve - por isso da pra comparar com o dicionario que voce ja tem
    assert busca_cambio_params('BRL', 'EUR,USD,JPY', '2024-07-01') == cambio_julho, \
        'busca_cambio_params tem que dar o mesmo que a busca_cambio'
    assert busca_cambio_params('BRL', 'EUR', 'latest')['base'] == 'BRL', 'o de hoje tambem'

    previsao_lisboa_params = busca_clima_params(38.72, -9.14)
    assert 'current_weather' in previsao_lisboa_params.keys(), 'a resposta tem que ter current_weather'
    assert -60 < previsao_lisboa_params['current_weather']['temperature'] < 60, 'a temperatura de Lisboa agora'

    resposta_recife_params = busca_cidade_params('Recife')
    assert resposta_recife_params['results'][0]['name'] == 'Recife', 'a busca por nome tambem'
    assert len(resposta_recife_params['results']) == 1, 'count=1 traz uma cidade so'

    assert verifica(o_que_params_monta, '7b8514e177d58d0d17fd36bb0258b7843c57c6fbd2ea41603a2b78d6', nome_questao='o_que_params_monta'), 'o_que_params_monta incorreta'

    print('Desafio extra - parametros pela requests: OK')
    print('\n=== DESAFIO EXTRA COMPLETO! ===')
