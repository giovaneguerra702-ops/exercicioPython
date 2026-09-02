# Lista de exercicios - brasileirao2 (leitura de json e dicionarios)
# Pre-requisito: Lista 1 (brasileirao1). Dados reais do campeonato
# brasileiro 2018, num arquivo ano2018.json. Aprender: ler o dicionario
# de jogos (ficha do jogo vs lista por data), reutilizar funcoes da
# Lista 1, contagens com dicionario (estadios, gols) e busca por trecho.

import json

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
        # DIFERENTE do boilerplate padrao (so nesta lista): antes de
        # ordenar, converte as chaves que sao strings numericas ('72')
        # em numeros (72). Assim responder {'72': 2} ou {72: 2} vale
        # igual. NAO propagar esta mudanca para outras listas.
        valor = {int(k) if isinstance(k, str) and k.isdigit() else k: v
                 for k, v in valor.items()}
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


# A funcao explicar() ajuda nas questoes de multipla escolha (Fase 1).
# Se voce travar numa questao, descomente a linha `explicar('nome')`
# que aparece logo abaixo dela para ler a discussao das alternativas.
def explicar(questao):
    try:
        from explicacao_brasileirao2 import EXPLICACOES
    except ImportError:
        print("Arquivo 'explicacao_brasileirao2.py' nao foi encontrado.")
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


# Os dados do campeonato ficam todos no arquivo ano2018.json (na mesma
# pasta deste arquivo). A funcao pega_dados le o arquivo pra voce - nao
# se preocupe com como ela funciona.
def pega_dados():
    with open('ano2018.json', encoding="utf-8") as f:
        dados = json.load(f)
    return dados


dados2018 = pega_dados()


# ===== FASE 1 - Aquecimento: o dicionario de jogos =====

'''
EXPLICACAO

Na Lista 1 voce leu o dicionario de EQUIPES (dados['equipes']) e a
CLASSIFICACAO. Agora vamos ler o dicionario de JOGOS. Ele mora em:

    dados['fases']['2700']['jogos']

Dentro dele ha DOIS dicionarios, cada um guarda os jogos de um jeito:

    dados['fases']['2700']['jogos']['id'][id_jogo]
        -> a FICHA do jogo com aquela id. Exemplo, se eu colocar id_jogo como 102094
           (Cruzeiro x Gremio, 0x1, no Mineirao):

               {'data': '2018-04-14', 'time1': '9', 'time2': '13',
                'placar1': '0', 'placar2': '1', 'estadio_id': '116',
                ...}

    dados['fases']['2700']['jogos']['data'][data]
        -> a LISTA de ids dos jogos daquele dia 
        Por exemplo, se eu substituir data por '2018-04-14'

               dados2018['fases']['2700']['jogos']['data']['2018-04-14']
               -> ['102094', '102097', '102101']

Na ficha, o campo 'time1' eh a id do MANDANTE (time de casa) e 'time2'
a do visitante. Os campos 'placar1'/'placar2' sao os gols de cada um.

Repare: as ids (de jogos e de times) sao STRINGS ('102094', '9'), e os
placares tambem ('0', '1'). Isso pode encher um pouco na hora de fazer contas.

O campeonato tem 380 jogos em 107 datas.
'''

breakpoint_aqui = 42

# PARE
# Experimente olhar os dados por dentro, de dois jeitos:
#
# 1) No VS Code: ponha um breakpoint na linha `breakpoint_aqui = 42` acima,
#    rode com 'debug python file' e use o debug console para digitar coisas
#    como:
#
#        print(dados2018['fases']['2700']['jogos'])
#        print(dados2018['fases']['2700']['jogos']['id']['102094'])
#        print(dados2018['fases']['2700']['jogos']['id']['102094']['data'])
#        print(dados2018['fases']['2700']['jogos']['data']['2018-04-14'])
#        print(len(dados2018['fases']['2700']['jogos']['id']))
#
#    Cada print desce um nivel a mais na estrutura - sao os MESMOS caminhos
#    do mapa la em cima (EXPLICACAO). O primeiro mostra o dicionario de
#    jogos inteiro; o segundo, a ficha de um jogo; o terceiro, a data
#    dentro da ficha; o quarto, os jogos de um dia; o len conta os jogos.
#
# 2) No navegador: abra o arquivo ano2018.json no firefox (menu
#    arquivo > "abrir arquivo"). A visualizacao do firefox deixa expandir
#    e recolher cada dicionario, e a correspondencia com o que o python
#    imprime fica facil de conferir. E tem um campo de FILTRO la no topo
#    ("Filter items"): digite um trecho (ex: '102094', 'estadio_id') e a
#    arvore mostra so os itens que batem - util pra achar um caminho sem
#    descer nivel por nivel.
#
# (PyCharm, se um dia voce usar: File > Open na PASTA onde estao o
# exercicio_brasileirao2.py e o ano2018.json, e 'run file in python
# console'.)


'''
EXERCICIO

Preencha as variaveis abaixo usando uma EXPRESSAO Python que produz o
valor (em vez do valor literal) - as expressoes vao ler do dicionario
dados2018, que ja esta carregado no comeco do arquivo.

1) O PAR de ids dos times do jogo 102094 (time1, time2).
   Dica: dados2018['fases']['2700']['jogos']['id']['102094']['time1']
2) A data do jogo 102132.
3) Quantos jogos tem o campeonato.        Dica: len(...)
4) Quantas DATAS de jogo tem o campeonato.
5) As ids dos jogos de 2018-04-14.
'''
times_do_jogo_102094 = (dados2018['fases']['2700']['jogos']['id']['102094']['time1'], dados2018['fases']['2700']['jogos']['id']['102094']['time2'])
data_do_jogo_102132 = dados2018['fases']['2700']['jogos']['id']['102132']['data']
quantos_jogos_no_ano = len(dados2018['fases']['2700']['jogos']['id'])
quantas_datas_de_jogo = len(dados2018['fases']['2700']['jogos']['data'])
jogos_de_2018_04_14 = dados2018['fases']['2700']['jogos']['data']['2018-04-14']

# Travou? Descomente a linha abaixo para ler a resolucao comentada:
#explicar('times_do_jogo_102094')
# explicar('data_do_jogo_102132')
# explicar('quantos_jogos_no_ano')
# explicar('quantas_datas_de_jogo')
#explicar('jogos_de_2018_04_14')

assert verifica(times_do_jogo_102094, 'a6e8e6c5f72a640d20910240a7af7b2f0f9117cc5c2bdf0f60b9f86f', nome_questao='times_do_jogo_102094'), 'times_do_jogo_102094 incorreta'
assert verifica(data_do_jogo_102132, '474ff7ad78c9f17e0b306ebf6c166f669b51edd925afa67269c7ef1a', nome_questao='data_do_jogo_102132'), 'data_do_jogo_102132 incorreta'
assert verifica(quantos_jogos_no_ano, '5a59419d1a83cf4784f9bb155a8706c5cd64b13c8ef8f85fbf1598de', nome_questao='quantos_jogos_no_ano'), 'quantos_jogos_no_ano incorreta'
assert verifica(quantas_datas_de_jogo, '67e9ffd5ba5d97e1515207451ee515a6d4aa473648c8442494cdab54', nome_questao='quantas_datas_de_jogo'), 'quantas_datas_de_jogo incorreta'
assert verifica(jogos_de_2018_04_14, '1fea1dd9ff8911667a741314f885ba31cbbc84a5853334aedd053a67', nome_questao='jogos_de_2018_04_14'), 'jogos_de_2018_04_14 incorreta'
print('Exercicio lendo o dicionario de jogos: OK')


'''
EXERCICIO

Tres questoes de multipla escolha sobre o dicionario de jogos.
Se travar, descomente o `explicar(...)` da questao.

Q1 - o_que_e_jogos_id

O que eh `dados['fases']['2700']['jogos']['id']`?

    a) um dicionario: para cada id de jogo, a ficha dele (data, time1,
       time2, placares, estadio_id, ...)
    b) uma lista com as ids de todos os jogos do campeonato
    c) um dicionario: para cada data, a lista de ids dos jogos daquele dia
    d) uma lista com as datas em que houve jogo
'''
o_que_e_jogos_id = 'a'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('o_que_e_jogos_id')

assert verifica(o_que_e_jogos_id, '08bf4614c220ab771763bc293a640931e4ab30d9a579c194b274a483', nome_questao='o_que_e_jogos_id'), 'o_que_e_jogos_id incorreta'


'''
EXERCICIO

Q2 - o_que_e_jogos_data

O que eh `dados['fases']['2700']['jogos']['data']`?

    a) uma lista com todas as datas em que houve jogo
    b) um dicionario: para cada data, a ficha do jogo daquele dia
    c) um dicionario: para cada data, a lista de ids dos jogos daquele dia
    d) um dicionario: para cada id de jogo, a data em que ele aconteceu
'''
o_que_e_jogos_data = 'c'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('o_que_e_jogos_data')

assert verifica(o_que_e_jogos_data, 'd0ca07d91c033bf82c75c13ba6f94b066d504df7ba497f24716a75a0', nome_questao='o_que_e_jogos_data'), 'o_que_e_jogos_data incorreta'


'''
EXERCICIO

Q3 - placar_e_string

A ficha do jogo 102094 tem 'placar1': '0' - repare nas ASPAS: o placar
eh uma STRING, nao um numero. O que acontece com `0 + placar1`?

    a) funciona sozinho: o python percebe que '0' eh um numero e
       converte a string em numero (devolve 0)
    b) da erro de tipo (TypeError), e o jeito certo eh str(0) - ou
       seja, transformar o 0 em string
    c) funciona, mas devolve a string '00' (os dois juntados)
    d) da erro de tipo (TypeError), e o jeito certo eh int(placar1) -
       ou seja, transformar o placar em numero
'''
placar_e_string = 'd'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('placar_e_string')

assert verifica(placar_e_string, '58d96888ba0ec23d61b3f5a025580e7e20e8c9b4f72cb979e7d76cc7', nome_questao='placar_e_string'), 'placar_e_string incorreta'

print('Exercicio multipla escolha (dicionario de jogos): OK')


# ===== FASE 2 - ids_dos_times_de_um_jogo + nomes_dos_times_de_um_jogo =====

'''
EXPLICACAO

Na ficha de cada jogo, o campo 'time1' guarda a id do MANDANTE (o time
de casa) e 'time2' a do visitante. Para devolver as DUAS num return so,
o python usa a tupla (time1, time2). Por exemplo

    return (time1, time2)

Nos testes, a ordem nao importa: responder (time1, time2) ou
(time2, time1) vale igual - o que importa eh o PAR de times.
'''


'''
EXERCICIO

Calculo a mao. Considere o dicionario trecho_jogo_102099 (a ficha do
jogo 102099, so com os campos que interessam):

    trecho_jogo_102099 = {'time1': '5', 'time2': '17'}

Monte uma tupla de ids dos times desse jogo usando uma expressao python
'''
trecho_jogo_102099 = {'time1': '5', 'time2': '17'}

par_de_ids_a_mao = (trecho_jogo_102099['time1'],trecho_jogo_102099['time2'])

# Travou? Descomente a linha abaixo para ler a resolucao comentada:
# explicar('par_de_ids_a_mao')

assert verifica(par_de_ids_a_mao, 'b89b138e95731077fb1d5813082ccd0b9fcaa461085136d8e1e5e89b', nome_questao='par_de_ids_a_mao'), 'par_de_ids_a_mao incorreta'
print('Exercicio calculo a mao (par de ids): OK')


'''
EXERCICIO

Faca a funcao ids_dos_times_de_um_jogo(dados, id_jogo) que devolve uma
tupla com as ids dos dois times do jogo.

    >>> ids_dos_times_de_um_jogo(dados, '102099')
    ('5', '17')
'''
def ids_dos_times_de_um_jogo(dados, id_jogo):
    time1 = dados['fases']['2700']['jogos']['id'][id_jogo]['time1']
    time2 = dados['fases']['2700']['jogos']['id'][id_jogo]['time2']
    ids = (time1,time2)
    return ids

t1, t2 = ids_dos_times_de_um_jogo(dados2018, '102099')
assert {t1, t2} == {'5', '17'}, f'ids do jogo 102099: obteve ({t1}, {t2})'
t1, t2 = ids_dos_times_de_um_jogo(dados2018, '102109')
assert {t1, t2} == {'1', '26'}, f'ids do jogo 102109: obteve ({t1}, {t2})'
print('Exercicio ids_dos_times_de_um_jogo: OK')


'''
EXPLICACAO

Voce fez a funcao nome_do_time na Lista 1: ela devolve o nome-comum do
time com aquela id. Ela vem pronta de novo:

    >>> nome_do_time(dados, '5')
    'Botafogo'

def nome_do_time(dados, id_numerica):
    return dados['equipes'][id_numerica]['nome-comum']
'''


def nome_do_time(dados, id_numerica):
    return dados['equipes'][id_numerica]['nome-comum'] #nao mexa aqui. Ela ja esta pronta
    # so estou te lembrando como ela eh pra voce poder usar


'''
EXERCICIO

Calculo a mao. Agora juntamos a ficha de um jogo com o dicionario de
equipes - o MESMO caminho que a funcao nome_do_time usa:

    trecho_equipes_102106 = {
        '695': {'nome-comum': 'Chapecoense'},
        '25':  {'nome-comum': 'Vasco'},
    }

    trecho_jogo_102106 = {'time1': '695', 'time2': '25'}

Monte uma tupla de NOMES dos times desse jogo usando uma expressao
python: passe pela ficha do jogo pra achar as ids, e pelo dicionario de
equipes pra achar os nomes. A ordem nao importa.
'''
trecho_equipes_102106 = {
    '695': {'nome-comum': 'Chapecoense'},
    '25':  {'nome-comum': 'Vasco'},
}
trecho_jogo_102106 = {'time1': '695', 'time2': '25'}

par_de_nomes_a_mao = (trecho_equipes_102106['695']['nome-comum'],trecho_equipes_102106['25']['nome-comum'])
#se voce achar essa expressao muito grande pra escrever de uma vez, pode escrever em etapas,
# definindo variaveis intermediarias. E pode usar o debugger também pra ir testando!

# Travou? Descomente a linha abaixo para ler a resolucao comentada:
# explicar('par_de_nomes_a_mao')

assert verifica(par_de_nomes_a_mao, '8d94011dad5bd45d5866936b08a2f33b54243d66aab119a436708958', nome_questao='par_de_nomes_a_mao'), 'par_de_nomes_a_mao incorreta'
print('Exercicio calculo a mao (nomes dos times): OK')


'''
EXERCICIO

Faca a funcao nomes_dos_times_de_um_jogo(dados, id_jogo) que devolve
uma tupla com os NOMES dos dois times do jogo. A cadeia de reuso tem
DOIS degraus:

    ids_dos_times_de_um_jogo(dados, id_jogo)  -> recebe a id do jogo e
        devolve a tupla (id do time1, id do time2)
    nome_do_time(dados, id_time)              -> recebe a id de um time
        e devolve o nome-comum dele

O primeiro degrau se encaixa no segundo pra cada time:

    time1, time2 = ids_dos_times_de_um_jogo(dados, id_jogo)
    nome_do_time(dados, time1)
    nome_do_time(dados, time2)

    >>> nomes_dos_times_de_um_jogo(dados, '102099')
    ('Botafogo', 'Palmeiras')
'''
def nomes_dos_times_de_um_jogo(dados, id_jogo):
    ids = ids_dos_times_de_um_jogo(dados,id_jogo)
    nome1 = ids[0]
    nome1 = dados['equipes'][nome1]['nome-comum']
    nome2 = ids[1]
    nome2 = dados['equipes'][nome2]['nome-comum']
    return (nome1,nome2)


n1, n2 = nomes_dos_times_de_um_jogo(dados2018, '102099')
assert {n1, n2} == {'Botafogo', 'Palmeiras'}, f'nomes do jogo 102099: obteve ({n1}, {n2})'
n1, n2 = nomes_dos_times_de_um_jogo(dados2018, '102106')
assert {n1, n2} == {'Chapecoense', 'Vasco'}, f'nomes do jogo 102106: obteve ({n1}, {n2})'
print('Exercicio nomes_dos_times_de_um_jogo: OK')


# ===== FASE 3 - datas_de_jogo + data_de_um_jogo =====

'''
EXPLICACAO

O dicionario de jogos tem as DUAS faces - e cada uma responde uma
pergunta diferente:

- O dicionario ['data'] guarda as DATAS: cada data aponta para a lista
  de jogos daquele dia. Para LISTAR todas as datas, basta percorrer as
  chaves dele:

      for data in dados['fases']['2700']['jogos']['data']:
          ...

- A FICHA guarda a 'data' de cada jogo. Para descobrir a data de UM
  jogo, olhe dentro da ficha dele.

  >>> dados['fases']['2700']['jogos']['id']['102132']['data']
  '2018-05-06'
'''


'''
EXERCICIO

Faca a funcao datas_de_jogo(dados) que devolve uma LISTA com todas as
datas em que houve jogo (as chaves do dicionario ['data']).

Aqui vai o tamanho dessa lista, mas voce que tem que obter a lista em si
    >>> len(datas_de_jogo(dados))
    107
'''
def datas_de_jogo(dados):
    data = dados['fases']['2700']['jogos']['data']
    return data

datas = datas_de_jogo(dados2018)
assert len(datas) == 107, f'quantidade de datas: obteve {len(datas)}'
assert '2018-04-14' in datas, '2018-04-14 deveria estar na lista'
assert '2018-07-26' in datas, '2018-07-26 deveria estar na lista'
assert '2018-10-26' in datas, '2018-10-26 deveria estar na lista'

# FALSIFICACAO: apago uma data e os 3 jogos dela - a funcao tem que ler
# a estrutura, nao devolver uma lista decorada
dados_falsificado = pega_dados()
del dados_falsificado['fases']['2700']['jogos']['data']['2018-04-14']
del dados_falsificado['fases']['2700']['jogos']['id']['102094']
del dados_falsificado['fases']['2700']['jogos']['id']['102097']
del dados_falsificado['fases']['2700']['jogos']['id']['102101']
datas = datas_de_jogo(dados_falsificado)
assert len(datas) == 106, f'apos falsificar, as datas deveriam ser 106 (obteve {len(datas)})'
assert '2018-04-14' not in datas, 'a data apagada nao pode aparecer'
print('Exercicio datas_de_jogo: OK')


'''
EXERCICIO

Faca a funcao data_de_um_jogo(dados, id_jogo) que devolve a data em que
o jogo aconteceu. Se a id nao for de nenhum jogo, devolva a string
'nao encontrado'.

    >>> data_de_um_jogo(dados, '102132')
    '2018-05-06'
'''
def data_de_um_jogo(dados, id_jogo):
    ids = dados['fases']['2700']['jogos']['id']
    if id_jogo not in ids:
        return 'nao encontrado'
    data = dados['fases']['2700']['jogos']['id'][id_jogo]['data']
    return data

assert data_de_um_jogo(dados2018, '102132') == '2018-05-06', 'data do jogo 102132'
assert data_de_um_jogo(dados2018, '102187') == '2018-06-06', 'data do jogo 102187'
assert data_de_um_jogo(dados2018, '102540') == 'nao encontrado', 'id inexistente devolve "nao encontrado"'
print('Exercicio data_de_um_jogo: OK')


# ===== FASE 4 - dicionario_id_estadio_e_nro_jogos (primeira CONTAGEM) =====

'''
EXPLICACAO

Agora vamos CONTAR: quantas vezes cada estadio recebeu um jogo. A ficha
tem o campo 'estadio_id'. A resposta eh um DICIONARIO:

    estadio_id -> quantas vezes aquele estadio aparece

Esse eh o padrao de CONTAGEM (voce usou ele na agenda_melhor, no
conta_ocorrencias):

    contagem = {}
    for ...:
        se o estadio ainda NAO esta em contagem:
            comece a contagem dele em zero
        some 1 na contagem dele

Antes de codar, vamos contar A MAO.
'''


'''
EXERCICIO

Calculo a mao. Considere o dicionario trecho_estadios (a ficha de 3
jogos, so com o estadio_id de cada um):

    trecho_estadios = {
        '102098': {'estadio_id': '72'},
        '102128': {'estadio_id': '72'},
        '102094': {'estadio_id': '116'},
    }

Quantas vezes cada estadio aparece? (dict estadio_id -> contagem; a
ordem das chaves nao importa, e a chave pode ser '72' ou 72 - vale
igual)
'''
trecho_estadios = {
    '102098': {'estadio_id': '72'},
    '102128': {'estadio_id': '72'},
    '102094': {'estadio_id': '116'},
}

contagem_estadios_a_mao = {72: 2, 116: 1} 

# Travou? Descomente a linha abaixo para ler a resolucao comentada:
#explicar('contagem_estadios_a_mao')

assert type(contagem_estadios_a_mao) == dict, 'contagem a mao deve ser um dict'
assert verifica(contagem_estadios_a_mao, '14734d79c0ecd2746fb95e47ce7bc24e783af3950ef5605829cb5b80', nome_questao='contagem_estadios_a_mao'), 'contagem_estadios_a_mao incorreta'
print('Exercicio calculo a mao (contagem de estadios): OK')


'''
EXPLICACAO - FASE PONTE (da ideia para o codigo)

Voce ja sabe a IDEIA (contar os estadios) e ja contou a mao. Falta
traduzir para Python. Veja o pseudocodigo:

       contagem = dicionario vazio
       for jogo em todos os jogos:
           estadio = o estadio_id do jogo da vez
           se o estadio ainda NAO esta em contagem:
               comece a contagem desse estadio em zero
           some 1 na contagem desse estadio
       retorne contagem

As 7 questoes abaixo perguntam, peca por peca, qual eh a traducao correta.
Em cada questao o pseudocodigo aparece de novo, com a linha em foco
MARCADA com -->. A cada questao, as linhas que ja foram perguntadas-e-
respondidas aparecem na forma CONCRETA (o Python que era a resposta).
Alternativas 'a', 'b', 'c' ou 'd'. Se travar, descomente o
`explicar(...)` logo abaixo da variavel.
'''


'''
EXERCICIO

Q1 - init_contagem

Pseudocodigo (linha em foco marcada com -->):

  -->  contagem = dicionario vazio
       for jogo em todos os jogos:
           estadio = o estadio_id do jogo da vez
           se o estadio ainda NAO esta em contagem:
               comece a contagem desse estadio em zero
           some 1 na contagem desse estadio
       retorne contagem

Como criar a contagem inicial (um dicionario vazio)?

    a) contagem = {}
    b) contagem = []
    c) contagem = 0
    d) contagem = [{}]
'''
init_contagem = 'a'
# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('init_contagem')

assert verifica(init_contagem, '7f55cea2029e15b6f66ced4cb50bee94884759b31f4e0f199ea942de', nome_questao='init_contagem'), 'init_contagem incorreta'


'''
EXERCICIO

Q2 - percorre_jogos

Pseudocodigo (linha em foco marcada com -->):

       contagem = {}
  -->  for jogo em todos os jogos:
           estadio = o estadio_id do jogo da vez
           se o estadio ainda NAO esta em contagem:
               comece a contagem desse estadio em zero
           some 1 na contagem desse estadio
       retorne contagem

Como percorrer TODOS os jogos (pra chegar na ficha de cada um)?

    a) for jogo in dados['fases']['2700']['jogos']['id']:
    b) for jogo in dados['fases']['2700']['jogos']:
    c) for jogo in dados['fases']['2700']['jogos']['id'].values():
    d) for jogo in dados['fases']['2700']['jogos']['data']:
'''
percorre_jogos = 'c'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
#explicar('percorre_jogos')

assert verifica(percorre_jogos, '888d7cfbde5b9644fe0819b97d7345a45874645b3a497e1cb0fd52a5', nome_questao='percorre_jogos'), 'percorre_jogos incorreta'


'''
EXERCICIO

Q3 - pega_estadio

Pseudocodigo (linha em foco marcada com -->):

       contagem = {}
       for jogo in dados['fases']['2700']['jogos']['id'].values():
  -->      estadio = o estadio_id do jogo da vez
           se o estadio ainda NAO esta em contagem:
               comece a contagem desse estadio em zero
           some 1 na contagem desse estadio
       retorne contagem

Dentro do laco, `jogo` eh a ficha de um jogo. Como pegar o estadio da
vez?

    a) estadio = jogo['estadio']
    b) estadio = jogo['estadio_id']
    c) estadio = dados['estadio_id']
    d) estadio = dados['fases']['2700']['jogos']['id']['estadio_id']
'''
pega_estadio = 'b'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('pega_estadio')

assert verifica(pega_estadio, '228aa06314e6ee962fc31412c14ab3ddc953c52e31d0171c8a808fb6', nome_questao='pega_estadio'), 'pega_estadio incorreta'


'''
EXERCICIO

Q4 - por_que_checar

Pseudocodigo (linha em foco marcada com -->):

       contagem = {}
       for jogo in dados['fases']['2700']['jogos']['id'].values():
           estadio = jogo['estadio_id']
  -->      se o estadio ainda NAO esta em contagem:
               comece a contagem desse estadio em zero
           some 1 na contagem desse estadio
       retorne contagem

Por que essa checagem precisa existir? Ou seja: se a gente tirasse ela e
fizesse `contagem[estadio] = contagem[estadio] + 1` direto, o que
aconteceria?

    a) nada muda, funciona igual
    b) o programa fica lento
    c) conta tudo em dobro
    d) na PRIMEIRA vez que o estadio aparece, contagem[estadio] da
       KeyError (a chave ainda nao existe)
'''
por_que_checar = 'd'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('por_que_checar')

assert verifica(por_que_checar, 'b118963e86cb0267c22204dac624e61343b0f1e06df14463009ac79d', nome_questao='por_que_checar'), 'por_que_checar incorreta'


'''
EXERCICIO

Q5 - como_checar

Pseudocodigo (linha em foco marcada com -->):

       contagem = {}
       for jogo in dados['fases']['2700']['jogos']['id'].values():
           estadio = jogo['estadio_id']
  -->      se o estadio ainda NAO esta em contagem:
               comece a contagem desse estadio em zero
           some 1 na contagem desse estadio
       retorne contagem

A questao anterior explicou POR QUE a checagem precisa existir. Agora:
como ela se ESCREVE em Python?

    a) if estadio not in contagem.keys():
    b) if estadio not in contagem.values():
    c) if contagem[estadio] == 0:
    d) if estadio not in dados.keys():
'''
como_checar = 'a'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('como_checar')

assert verifica(como_checar, '1de3e5a37a94ca92bd3d462d1095e99d8aa1151cccde0003f9f9ae38', nome_questao='como_checar'), 'como_checar incorreta'


'''
EXERCICIO

Q6 - estadio_novo

Pseudocodigo (linha em foco marcada com -->):

       contagem = {}
       for jogo in dados['fases']['2700']['jogos']['id'].values():
           estadio = jogo['estadio_id']
           if estadio not in contagem.keys():
  -->            comece a contagem desse estadio em zero
           some 1 na contagem desse estadio
       retorne contagem

Quando o estadio ainda NAO esta em contagem, o que fazer antes de somar
1? (igual conta_letras da agenda)

    a) contagem[estadio] = 1
    b) contagem[estadio] = 0
    c) contagem.append(estadio)
    d) contagem[0] = estadio
'''
estadio_novo = 'b'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('estadio_novo')

assert verifica(estadio_novo, 'dc76e84f4c559ca4bd91f796b7b65c14fb646a77d25fd116ea2547e7', nome_questao='estadio_novo'), 'estadio_novo incorreta'


'''
EXERCICIO

Q7 - incremento_estadios

Pseudocodigo (linha em foco marcada com -->):

       contagem = {}
       for jogo in dados['fases']['2700']['jogos']['id'].values():
           estadio = jogo['estadio_id']
           if estadio not in contagem.keys():
               contagem[estadio] = 0
  -->      some 1 na contagem desse estadio
       retorne contagem

Como somar 1 na contagem do estadio (a chave dele ja existe agora)?

    a) contagem[estadio] = 1
    b) contagem = contagem + 1
    c) contagem[estadio] = contagem[estadio] + 1
    d) contagem.append(estadio)
'''
incremento_estadios = 'c'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('incremento_estadios')

assert verifica(incremento_estadios, '6e03a4ddb59f51f4433d0abeefd7978173a6c84f36ffcd1777ee2046', nome_questao='incremento_estadios'), 'incremento_estadios incorreta'

print('Exercicio ponte dicionario_id_estadio_e_nro_jogos: OK')


'''
EXERCICIO

Faca a funcao dicionario_id_estadio_e_nro_jogos(dados) que devolve um
dicionario: para cada estadio (a id dele), quantos jogos aconteceram
nele. Assim o retorno eh um dicionario, e

    >>> dicionario_id_estadio_e_nro_jogos(dados)['72']
    16

revela que o estadio 72 recebeu 16 jogos.
'''
def dicionario_id_estadio_e_nro_jogos(dados):
    contagem = {}
    for jogo in dados['fases']['2700']['jogos']['id'].values():
        estadio = jogo['estadio_id']
        if estadio not in contagem.keys():
            contagem[estadio] = 0
        contagem[estadio] = contagem[estadio] + 1
    return contagem

estadios = dicionario_id_estadio_e_nro_jogos(dados2018)
assert estadios['72'] == 16, 'o estadio 72 recebeu 16 jogos'

# FALSIFICACAO: mudo o estadio de um jogo - a contagem tem que mudar junto
dados_falsificado = pega_dados()
dados_falsificado['fases']['2700']['jogos']['id']['102097']['estadio_id'] = '72'
estadios = dicionario_id_estadio_e_nro_jogos(dados_falsificado)
assert estadios['72'] == 17, 'apos falsificar, o estadio 72 deveria ter 17 jogos'
print('Exercicio dicionario_id_estadio_e_nro_jogos: OK')


# ===== FASE 5 - ids_de_jogos_de_um_time + datas_de_jogos_de_um_time =====

'''
EXERCICIO

Calculo a mao. Considere o dicionario trecho_jogos_time_25 (dois jogos,
com o time1 e o time2 de cada um; o time '25' joga nos dois):

    trecho_jogos_time_25 = {
        '102098': {'data': '2018-04-15', 'time1': '25', 'time2': '4'},
        '102128': {'data': '2018-05-05', 'time1': '25', 'time2': '26'},
    }

Quais as ids dos jogos em que o time '25' jogou? (a ordem nao importa)
'''
trecho_jogos_time_25 = {
    '102098': {'data': '2018-04-15', 'time1': '25', 'time2': '4'},
    '102128': {'data': '2018-05-05', 'time1': '25', 'time2': '26'},
}

ids_dos_jogos_do_25_a_mao = ('102098','102128')

# Travou? Descomente a linha abaixo para ler a resolucao comentada:
# explicar('ids_dos_jogos_do_25_a_mao')

assert verifica(ids_dos_jogos_do_25_a_mao, '054f8865276399bcacc8e05c34207101c148ee98f8dee38421e804a9', nome_questao='ids_dos_jogos_do_25_a_mao'), 'ids_dos_jogos_do_25_a_mao incorreta'
print('Exercicio calculo a mao (jogos de um time): OK')


'''
EXERCICIO

Faca a funcao ids_de_jogos_de_um_time(dados, time_id) que devolve uma
LISTA com as ids de todos os jogos em que o time jogou (como time1 OU
como time2).

    >>> len(ids_de_jogos_de_um_time(dados, '695'))
    38
'''
def ids_de_jogos_de_um_time(dados, time_id):
    jogos_time = []
    jogos = dados['fases']['2700']['jogos']['id']
    for jogo in jogos.items(): #aqui cria uma tupla, (chave,valores)
        if jogo[1]['time1'] == time_id:
            jogos_time.append(jogo[0])
        elif jogo[1]['time2'] == time_id:
            jogos_time.append(jogo[0])
        else:
            'nao tem'
    return jogos_time



jogos_chapeco = ids_de_jogos_de_um_time(dados2018, '695')
assert len(jogos_chapeco) == 38, f'a Chapecoense (695) jogou 38 vezes (obteve {len(jogos_chapeco)})'
assert '102330' in jogos_chapeco, 'o jogo 102330 deveria estar nos jogos da Chapecoense'
assert '102422' in jogos_chapeco, 'o jogo 102422 deveria estar nos jogos da Chapecoense'
assert '102208' not in jogos_chapeco, 'o jogo 102208 eh do Santos, nao da Chapecoense'
jogos_santos = ids_de_jogos_de_um_time(dados2018, '22')
assert len(jogos_santos) == 38, f'o Santos (22) jogou 38 vezes (obteve {len(jogos_santos)})'
assert '102208' in jogos_santos, 'o jogo 102208 deveria estar nos jogos do Santos'
assert '102259' in jogos_santos, 'o jogo 102259 deveria estar nos jogos do Santos'
assert '102330' not in jogos_santos, 'o jogo 102330 eh da Chapecoense, nao do Santos'
print('Exercicio ids_de_jogos_de_um_time: OK')


'''
EXPLICACAO

Voce fez a funcao id_do_time na Lista 1: a busca ao contrario, do NOME
do time para a id dele. Ela vem pronta de novo:

    >>> id_do_time(dados, 'Santos')
    '22'

def id_do_time(dados, nome_time):
    for id_time in dados['equipes']:
        if dados['equipes'][id_time]['nome-comum'] == nome_time:
            return id_time
    raise KeyError('nao encontrado')
'''


def id_do_time(dados, nome_time):
    for id_time in dados['equipes']:
        if dados['equipes'][id_time]['nome-comum'] == nome_time:
            return id_time
    raise KeyError('nao encontrado')


'''
EXPLICACAO

A proxima funcao recebe o NOME do time (nao a id) e devolve as datas em
que ele jogou. A cadeia de reuso tem TRES degraus:

    id_do_time(dados, nome)                  -> recebe o nome e devolve a id do time
    ids_de_jogos_de_um_time(dados, id_time)  -> recebe a id_time e devolve as ids_jogos dele
    data_de_um_jogo(dados, id_jogo)          -> recebe uma id_jogo e devolve a data dele

O primeiro degrau se encaixa no segundo (o python resolve de dentro
pra fora), e o resultado eh a lista dos jogos do time:

    ids_de_jogos_de_um_time(dados, id_do_time(dados, nome))

Depois, um `for` percorre essa lista chamando data_de_um_jogo de cada
jogo e juntando as datas.
'''


'''
EXERCICIO

Calculo a mao. De novo o trecho_jogos_time_25 acima - so que agora
repare tambem na 'data' de cada jogo.

    trecho_jogos_time_25 = {
        '102098': {'data': '2018-04-15', 'time1': '25', 'time2': '4'},
        '102128': {'data': '2018-05-05', 'time1': '25', 'time2': '26'},
    }

Em que dias o time '25' jogou? (a ordem nao importa)
'''
datas_do_25_a_mao = ('2018-04-15','2018-05-05')

# Travou? Descomente a linha abaixo para ler a resolucao comentada:
# explicar('datas_do_25_a_mao')

assert verifica(datas_do_25_a_mao, '229aa4cb4bedd36ac8afe2001cca3748f76b98a249b3b855542aa197', nome_questao='datas_do_25_a_mao'), 'datas_do_25_a_mao incorreta'
print('Exercicio calculo a mao (datas de um time): OK')


'''
EXERCICIO

Faca a funcao datas_de_jogos_de_um_time(dados, nome_time) que devolve
uma LISTA com as datas em que o time jogou. Use a cadeia de tres
funcoes da explicacao acima.

    >>> len(datas_de_jogos_de_um_time(dados, 'Santos'))
    38
'''
def datas_de_jogos_de_um_time(dados, nome_time):
    datas = []
    time_id = id_do_time(dados,nome_time)
    ids_jogos = ids_de_jogos_de_um_time(dados, time_id)
    for id in ids_jogos:
        data = dados['fases']['2700']['jogos']['id'][id]['data']
        datas.append(data)
    return datas
    

datas_santos = datas_de_jogos_de_um_time(dados2018, 'Santos')
assert len(datas_santos) == 38, f'o Santos jogou em 38 datas (obteve {len(datas_santos)})'
assert '2018-04-21' in datas_santos, '2018-04-21 deveria estar nas datas do Santos'
assert '2018-10-13' in datas_santos, '2018-10-13 deveria estar nas datas do Santos'
datas_chapeco = datas_de_jogos_de_um_time(dados2018, 'Chapecoense')
assert len(datas_chapeco) == 38, f'a Chapecoense jogou em 38 datas (obteve {len(datas_chapeco)})'
assert '2018-11-25' in datas_chapeco, '2018-11-25 deveria estar nas datas da Chapecoense'
assert '2018-12-02' in datas_chapeco, '2018-12-02 deveria estar nas datas da Chapecoense'
print('Exercicio datas_de_jogos_de_um_time: OK')


# ===== FASE 6 - dicionario_de_gols + time_que_fez_mais_gols =====

'''
EXPLICACAO

Os PLACARES sao strings: a ficha do jogo 102096 tem 'placar1': '3'.
Antes de somar, precisamos converter com int() - e o erro classico aqui
eh esquecer disso:

    0 + '3'    # TypeError - nao da pra somar numero com string
    0 + int('3')   # 3 - funciona

A contagem eh igual a da Fase 4, so que agora somamos os GOLS de cada
time em todos os jogos: para cada jogo, int(placar1) vai para o time1 e
int(placar2) para o time2. Com uma ficha na mao:

    jogo = {'time1': '26', 'time2': '76', 'placar1': '3', 'placar2': '0'}
    gols['26'] = gols['26'] + int(jogo['placar1'])   # 3 gols pro time1
    gols['76'] = gols['76'] + int(jogo['placar2'])   # 0 gols pro time2

Repare: cada placar vai pro SEU dono - o placar1 eh SEMPRE do time1, o
placar2 SEMPRE do time2.
'''


'''
EXERCICIO

Calculo a mao. Considere o dicionario trecho_gols (3 jogos, com os dois
times e os dois placares de cada um):

    trecho_gols = {
        '102096': {'time1': '26', 'time2': '76', 'placar1': '3', 'placar2': '0'},
        '102098': {'time1': '25', 'time2': '4',  'placar1': '2', 'placar2': '1'},
        '102102': {'time1': '6',  'time2': '11', 'placar1': '2', 'placar2': '1'},
    }

1) Quantos gols cada time fez nesses 3 jogos? (dict time_id -> gols; a
   ordem das chaves nao importa, e a chave pode ser '26' ou 26 - vale
   igual)
2) Qual time fez MAIS gols nesses 3 jogos?
'''
trecho_gols = {
    '102096': {'time1': '26', 'time2': '76', 'placar1': '3', 'placar2': '0'},
    '102098': {'time1': '25', 'time2': '4',  'placar1': '2', 'placar2': '1'},
    '102102': {'time1': '6',  'time2': '11', 'placar1': '2', 'placar2': '1'},
}

gols_por_time_a_mao = {26: 3, 76: 0, 25: 2, 4: 1, 6: 2, 11: 1}
time_mais_gols_a_mao = '26'

# Travou? Descomente as linhas abaixo para ler as resolucoes comentadas:
#explicar('gols_por_time_a_mao')
#explicar('time_mais_gols_a_mao')

assert type(gols_por_time_a_mao) == dict, 'gols a mao deve ser um dict'
assert verifica(gols_por_time_a_mao, '81d0900b2abdc502ffb2e51929c19b73e3e9d18f31c34822c2c7dac4', nome_questao='gols_por_time_a_mao'), 'gols_por_time_a_mao incorreta'
assert verifica(time_mais_gols_a_mao, 'c6435173e6fdccaca0e7dd588627bcc0e76e4f9093acf7239fbfd8f8', nome_questao='time_mais_gols_a_mao'), 'time_mais_gols_a_mao incorreta'
print('Exercicio calculo a mao (gols): OK')

'''
EXERCICIO

Faca a funcao dicionario_de_gols(dados) que devolve um dicionario: para
cada time (a id dele), o total de gols que ele fez no campeonato
inteiro. Nao esqueca do int() nos placares!

    >>> dicionario_de_gols(dados)['695']
    34
'''
def dicionario_de_gols(dados):
    pass

gols = dicionario_de_gols(dados2018)
assert gols['695'] == 34, 'a Chapecoense (695) fez 34 gols'

# FALSIFICACAO em etapas: mudo placares - o total tem que mudar junto
dados_falsificado = pega_dados()
dados_falsificado['fases']['2700']['jogos']['id']['102330']['placar2'] = '1'
assert dicionario_de_gols(dados_falsificado)['695'] == 35, 'apos o 1o placar falsificado, a Chapecoense tem 35 gols'
dados_falsificado['fases']['2700']['jogos']['id']['102422']['placar2'] = '12'
assert dicionario_de_gols(dados_falsificado)['695'] == 46, 'apos o 2o placar falsificado, a Chapecoense tem 46 gols'
print('Exercicio dicionario_de_gols: OK')


'''
EXERCICIO

Faca a funcao time_que_fez_mais_gols(dados) que devolve a id do time
que fez mais gols no campeonato. Dica: voce ja tem a funcao que monta o
dicionario de gols. Percorra ele mantendo o MELHOR time visto ate
agora - uma variavel pra id dele, outra pra marca dele - e, quando achar
um time com mais gols que o melhor atual, atualize as duas:

       melhor_time  = a id do melhor time ate agora
       melhor_marca = os gols do melhor time ate agora
       se os gols do time da vez passarem a melhor_marca:
           atualize as duas variaveis

    >>> time_que_fez_mais_gols(dados)
    '17'
'''
def time_que_fez_mais_gols(dados):
    pass

assert time_que_fez_mais_gols(dados2018) == '17', 'o time que mais fez gols eh o 17 (Palmeiras)'

# FALSIFICACAO: mudo um placar da Chapecoense para um valor absurdo - o
# artilheiro tem que mudar
dados_falsificado = pega_dados()
dados_falsificado['fases']['2700']['jogos']['id']['102422']['placar2'] = '120'
assert time_que_fez_mais_gols(dados_falsificado) == '695', 'apos falsificar, o artilheiro vira a Chapecoense (695)'
print('Exercicio time_que_fez_mais_gols: OK')


# ===== FASE 7 - busca_imprecisa =====

'''
EXPLICACAO

Agora a busca "fuzzy": procurar por 'Paulo' e achar o Sao Paulo, ou por
'Fla' e achar o Flamengo. Voce recebe um TRECHO de nome e compara com
QUATRO campos de cada time:

    'nome-comum', 'nome-slug', 'sigla' e 'nome'

Se o trecho aparecer DENTRO do campo, o time entra na resposta. O `in`
de strings faz exatamente isso:

    'Paulo' in 'Sao Paulo'      # True
    'Paulo' in 'Santos'         # False

Com a ficha de um time na mao (o Sao Paulo, id '24'):

    time = {'nome-comum': 'Sao Paulo', 'nome-slug': 'sao-paulo',
            'sigla': 'SPA', 'nome': 'Sao Paulo Futebol Clube'}
    'Paulo' in time['nome-comum']    # True - entra na resposta
    'Paulo' in time['sigla']         # False - 'Paulo' nao esta em 'SPA'
    'SPA'   in time['sigla']         # True - por isso 'SPA' acha o time

Repare: 'SPA' tambem acha o Sao Paulo (eh a sigla dele). A resposta eh
uma LISTA de ids - e ela PODE ser vazia, se ninguem bater.
'''


'''
EXERCICIO

Faca a funcao busca_imprecisa_por_nome_de_time(dados, nome_time) que
devolve a lista de ids dos times que "batem" com o trecho buscado (nos
4 campos acima). Se ninguem bater, devolva uma lista vazia.

    >>> '24' in busca_imprecisa_por_nome_de_time(dados, 'Paulo')
    True
'''
def busca_imprecisa_por_nome_de_time(dados, nome_time):
    pass

ids_times = busca_imprecisa_por_nome_de_time(dados2018, 'Paulo')
assert '24' in ids_times, f"'Paulo' deveria achar o Sao Paulo (24); obteve {ids_times}"
ids_times = busca_imprecisa_por_nome_de_time(dados2018, 'SPA')
assert '24' in ids_times, f"'SPA' deveria achar o Sao Paulo (24) pela sigla; obteve {ids_times}"
ids_times = busca_imprecisa_por_nome_de_time(dados2018, 'anto')
assert '22' in ids_times, f"'anto' deveria achar o Santos (22); obteve {ids_times}"
print('Exercicio busca_imprecisa_por_nome_de_time: OK')


# ===== FASE 8 - Simulacao integrada =====

'''
EXPLICACAO

Fechando a lista: vamos "rodar o campeonato" usando TODAS as funcoes em
ordem natural - times de um jogo, nomes, data, datas, jogos de um time,
gols e artilheiro - sobre os MESMOS dados.

Para cada resposta abaixo, PRIMEIRO preveja (calcule com a cabeca,
consultando os dados se precisar) - e so depois os asserts confirmam,
rodando as funcoes de verdade.
'''


'''
EXERCICIO

Preveja os valores (so depois os asserts abaixo conferem com as funcoes):

1) o PAR de ids dos times do jogo 102099   (ids_dos_times_de_um_jogo)
2) o PAR de NOMES dos times do jogo 102099 (nomes_dos_times_de_um_jogo)
3) a data do jogo 102132                   (data_de_um_jogo)
4) quantas datas de jogo tem o ano         (datas_de_jogo)
5) quantos jogos o Santos jogou            (ids_de_jogos_de_um_time)
6) em quantas datas o Santos jogou         (datas_de_jogos_de_um_time)
7) quantos gols o Santos fez               (dicionario_de_gols)
8) a id do time que fez mais gols          (time_que_fez_mais_gols)
'''
times_102099_previsto = 'coloque o valor aqui'
nomes_102099_previsto = 'coloque o valor aqui'
data_102132_previsto = 'coloque o valor aqui'
quantas_datas_previsto = 'coloque o valor aqui'
jogos_do_santos_previsto = 'coloque o valor aqui'
datas_do_santos_previsto = 'coloque o valor aqui'
gols_do_santos_previsto = 'coloque o valor aqui'
artilheiro_previsto = 'coloque o valor aqui'

assert verifica(times_102099_previsto, 'f53085fb752ce1f8616e8830934dc1987f17c63420b0887a46dae5ce', nome_questao='times_102099_previsto'), 'times_102099_previsto incorreta'
assert verifica(nomes_102099_previsto, 'e0378094a3051dab75dab5f452cd55492c4b1626c2492b225bd71ff5', nome_questao='nomes_102099_previsto'), 'nomes_102099_previsto incorreta'
assert verifica(data_102132_previsto, '406bd9373c1fc59fcaec33805e4b38579bc23ea5a07d8d2188f33a84', nome_questao='data_102132_previsto'), 'data_102132_previsto incorreta'
assert verifica(quantas_datas_previsto, '06f1f19858cc83b06af943d6e91456d83d199f4b0f2c5014e8aff538', nome_questao='quantas_datas_previsto'), 'quantas_datas_previsto incorreta'
assert verifica(jogos_do_santos_previsto, '6a3e6a5f02a9a73ea3ea7be757fb93acf81a724425652ee777914ace', nome_questao='jogos_do_santos_previsto'), 'jogos_do_santos_previsto incorreta'
assert verifica(datas_do_santos_previsto, 'bf1ba6db73d4e62604bfca145ac736d899e3cb7ecc0022e3243a919c', nome_questao='datas_do_santos_previsto'), 'datas_do_santos_previsto incorreta'
assert verifica(gols_do_santos_previsto, '85a7f7ae733e722735ce7a405792ffafc7159be851ddd1b04da44225', nome_questao='gols_do_santos_previsto'), 'gols_do_santos_previsto incorreta'
assert verifica(artilheiro_previsto, '4216d6ace19c88269dc4a6f17b8aa3077420ab97e4fa3a935c91fafc', nome_questao='artilheiro_previsto'), 'artilheiro_previsto incorreta'
print('Exercicio simulacao integrada (previsao): OK')

# agora as funcoes confirmam a sua previsao
t1, t2 = ids_dos_times_de_um_jogo(dados2018, '102099')
assert {t1, t2} == {'5', '17'}, 'times do jogo 102099'
n1, n2 = nomes_dos_times_de_um_jogo(dados2018, '102099')
assert {n1, n2} == {'Botafogo', 'Palmeiras'}, 'nomes do jogo 102099'
assert data_de_um_jogo(dados2018, '102132') == '2018-05-06', 'data do jogo 102132'
assert len(datas_de_jogo(dados2018)) == 107, 'quantas datas'
assert len(ids_de_jogos_de_um_time(dados2018, '22')) == 38, 'quantos jogos do Santos'
assert len(datas_de_jogos_de_um_time(dados2018, 'Santos')) == 38, 'em quantas datas o Santos jogou'
assert dicionario_de_gols(dados2018)['22'] == 46, 'gols do Santos'
assert time_que_fez_mais_gols(dados2018) == '17', 'artilheiro'
print('Exercicio simulacao integrada (confirmacao): OK')


print('\n=== PARABENS! Todos os exercicios completos! ===')


# ===== CLI (opcional) =====

'''
EXPLICACAO

Para terminar, uma interface de consulta - um menu que usa as funcoes
da lista. Descomente a chamada `# main()` no fim do arquivo quando
quiser usar.

Cada opcao tem as PECAS soltas (em comentario) - voce so precisa
organiza-las na ordem certa. Nenhuma opcao precisa de try/except
(tratar erros eh materia de uma aula futura).
'''

def main():
    dados = pega_dados()

    while True:
        print()
        print('=== BRASILEIRAO 2018 - JOGOS ===')
        print('1. nomes dos times de um jogo (por id)')
        print('2. data de um jogo')
        print('3. ids dos jogos de um time (por id)')
        print('4. datas de jogos de um time (por NOME)')
        print('5. gols de um time (por id) e quem fez mais gols')
        print('6. Sair')
        opcao = input('Opcao: ')

        if opcao == '1':
            # FUNCIONALIDADE 1 - os nomes dos times de um jogo pela id
            # digitada. Nao precisa de try/except: id que nao existe da
            # KeyError, e tudo bem (isso eh materia da aula de erros).
            # Organize as pecas abaixo (na ordem certa):
            #
            #     id_jogo = input('  id do jogo: ')
            #     nome1, nome2 = nomes_dos_times_de_um_jogo(dados, id_jogo)
            #     print(f'  {nome1} x {nome2}')
            #
            pass  # COMPLETE: monte a funcionalidade 1 com as pecas acima

        elif opcao == '2':
            # FUNCIONALIDADE 2 - a data de um jogo pela id digitada.
            # Nao precisa de try/except: id que nao existe devolve a
            # string 'nao encontrado' (a funcao nao levanta).
            #
            #     id_jogo = input('  id do jogo: ')
            #     data = data_de_um_jogo(dados, id_jogo)
            #     print(f'  data: {data}')
            #
            pass  # COMPLETE: monte a funcionalidade 2

        elif opcao == '3':
            # FUNCIONALIDADE 3 - as ids dos jogos de um time pela id
            # digitada. Nao precisa de try/except.
            #
            #     id_time = input('  id do time: ')
            #     jogos = ids_de_jogos_de_um_time(dados, id_time)
            #     print(f'  {len(jogos)} jogos: {jogos}')
            #
            pass  # COMPLETE: monte a funcionalidade 3

        elif opcao == '4':
            # FUNCIONALIDADE 4 - as datas de jogos de um time pelo NOME
            # digitado (a funcao recebe o nome, nao a id). Nao precisa
            # de try/except: nome que nao existe da KeyError (a funcao
            # id_do_time levanta), e tudo bem.
            #
            #     nome = input('  nome do time: ')
            #     datas = datas_de_jogos_de_um_time(dados, nome)
            #     print(f'  {len(datas)} datas: {datas}')
            #
            pass  # COMPLETE: monte a funcionalidade 4

        elif opcao == '5':
            # FUNCIONALIDADE 5 - os gols de um time pela id digitada e o
            # time que fez mais gols no campeonato. Nao precisa de
            # try/except: id que nao existe da KeyError no dict de gols,
            # e tudo bem.
            #
            #     id_time = input('  id do time: ')
            #     gols = dicionario_de_gols(dados)
            #     print(f'  gols do time {id_time}: {gols[id_time]}')
            #     print(f'  quem fez mais gols: {time_que_fez_mais_gols(dados)}')
            #
            pass  # COMPLETE: monte a funcionalidade 5

        elif opcao == '6':
            break
        else:
            print('Opcao invalida')


# Pra rodar a interface, descomente:
# main()
