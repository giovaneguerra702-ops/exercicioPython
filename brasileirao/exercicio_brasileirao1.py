# Versao nova
# Lista de exercicios - brasileirao1 (leitura de json e dicionarios)
# Dados reais do campeonato brasileiro 2018, num arquivo ano2018.json.
# Aprender: ler dicionarios e estruturas aninhadas (dict dentro de dict,
# lista dentro de dict), e reutilizar funcoes ja feitas.

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


# A funcao checa_erro() confere que uma chamada se comporta como o esperado
# quanto a excecoes - e, quando NAO se comporta, EXPLICA o que houve. Voce nao
# precisa entender ela. O 2o argumento eh o que voce espera que aconteca:
#     checa_erro(lambda: id_do_time(dados, 'Time Fantasma'), KeyError)  # espera esse erro
#     checa_erro(lambda: id_do_time(dados, 'Santos'), None)             # espera que NAO levante
def checa_erro(funcao, excecao_esperada):
    """Roda funcao() e devolve True se o que aconteceu bate com excecao_esperada
    (uma classe de erro, ou None para 'nao deve levantar nada'). Se nao bater,
    imprime uma explicacao e devolve False."""
    try:
        funcao()
    except Exception as e:
        if excecao_esperada is None:
            print(f'Esperava que NAO levantasse nada, mas levantou {type(e).__name__}: {e}')
            return False
        if isinstance(e, excecao_esperada):
            return True    # levantou o erro esperado
        print(f'Esperava {excecao_esperada.__name__}, mas levantou {type(e).__name__}: {e}')
        return False
    # nao levantou nada
    if excecao_esperada is None:
        return True        # certo: nao devia levantar
    print(f'Esperava {excecao_esperada.__name__}, mas nao levantou erro nenhum')
    return False


# A funcao explicar() ajuda nas questoes teoricas. Se voce travar numa
# questao, descomente a linha `explicar('nome')` logo abaixo dela para
# ler a resolucao comentada.
def explicar(questao):
    try:
        from explicacao_brasileirao1 import EXPLICACOES
    except ImportError:
        print("Arquivo 'explicacao_brasileirao1.py' nao foi encontrado.")
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


# ===== FASE 1 - Conhecendo o dicionario =====

'''
EXPLICACAO

Os dados do campeonato estao todos num dicionario `dados`, carregado do
arquivo ano2018.json. Os caminhos mais usados:

    dados['equipes'][id]
                               -> a ficha do time que tem aquela id, com
                                  nome-comum, sigla, e outros dados
    dados['fases']['2700']['classificacao']['grupo']['unico']
                               -> a LISTA do 1o ao 20o colocado. Usa as ids
                                  definidas no item acima
    dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa']
                               -> '1-6' (zona da libertadores: do primeiro ao 6o)
    dados['fases']['2700']['faixas-classificacao']['classifica3']['faixa']
                               -> '17-20' (zona de rebaixamento: do decimo setimo
                                   em diante)

A id do campeao eh o PRIMEIRO elemento da lista de classificacao:

    dados['fases']['2700']['classificacao']['grupo']['unico'][0]

As ids sao STRINGS ('17', nao 17). O campeonato tem 20 times.
'''

breakpoint_aqui = 42

# PARE
# Experimente olhar os dados por dentro, de dois jeitos:
#
# 1) No VS Code: ponha um breakpoint na linha `breakpoint_aqui = 42` acima,
#    rode com 'debug python file' e use o debug console para digitar coisas
#    como:
#
print(dados2018['equipes'])
print(dados2018['equipes']['6'])
print(dados2018['equipes']['6']['nome-comum'])
print(dados2018['equipes']['6']['sigla'])
print(len(dados2018['equipes']))
print(dados2018['fases']['2700']['classificacao']['grupo']['unico'])
print(dados2018['fases']['2700']['classificacao']['grupo']['unico'][0])
print(dados2018['fases']['2700']['faixas-classificacao']['classifica1']['faixa'])
print(dados2018['fases']['2700']['faixas-classificacao']['classifica3']['faixa'])
#
#    Cada print desce um nivel a mais na estrutura - sao os MESMOS caminhos
#    do mapa la em cima (EXPLICACAO). Os tres primeiros descem o dicionario
#    de equipes (dict inteiro, ficha do time, nome-comum); o len conta as
#    equipes; os dois do 'unico' mostram a lista de classificacao e o
#    primeiro colocado; os dois de faixa mostram as faixas da libertadores
#    e do rebaixamento.
#
# 2) No navegador: abra o arquivo ano2018.json no firefox (menu
#    arquivo > "abrir arquivo"). A visualizacao do firefox deixa expandir
#    e recolher cada dicionario, e a correspondencia com o que o python
#    imprime fica facil de conferir. E tem um campo de FILTRO la no topo
#    ("Filter items"): digite um trecho (ex: 'unico', 'nome-comum',
#    'Palmeiras', 'placar1') e a arvore mostra so os itens que batem -
#    util pra achar um caminho sem descer nivel por nivel.
#
# (PyCharm, se um dia voce usar: File > Open na PASTA onde estao o
# exercicio_brasileirao1.py e o ano2018.json, e 'run file in python
# console'. O resto das instrucoes de pycharm de versoes antigas desta
# atividade nao vale mais - o debugger que usamos agora eh o do VS Code.)


'''
EXERCICIO

Preencha as variaveis abaixo usando uma EXPRESSAO Python que produz o
valor (em vez do valor literal) - as expressoes vao ler do dicionario
dados2018, que ja esta carregado no comeco do arquivo.

1) O nome-comum do time de id '6'.            Dica: dados2018['equipes']['6']['nome-comum']
2) Quantos times tem o campeonato.            Dica: len(...)
3) A id do PRIMEIRO colocado.                 
4) A faixa da libertadores.                   
5) O nome-comum do PRIMEIRO colocado - essa
   eh a mais dificil: junte o caminho da 3
   com o caminho do 1 (o [0] vira a CHAVE
   do dicionario de equipes).
'''
nome_comum_do_time_6= dados2018['equipes']['6']['nome-comum']
quantos_times_no_campeonato = len(dados2018['equipes'])
id_do_primeiro_colocado     = dados2018['fases']['2700']['classificacao']['grupo']['unico'][0]
faixa_da_libertadores       = dados2018['fases']['2700']['faixas-classificacao']['classifica1']['faixa']
nome_comum_do_primeiro_colocado = dados2018['equipes'][id_do_primeiro_colocado]['nome-comum']

# Travou na 5? Descomente a linha abaixo para ler a explicacao:
# explicar('nome_comum_do_primeiro_colocado')

assert verifica(nome_comum_do_time_6, '4eeda438b4e375b9045910882b2123481e8d39f9cc4b534aa77d1238', nome_questao='nome_comum_do_time_6'), 'nome_comum_do_time_6 incorreta'
assert verifica(quantos_times_no_campeonato, '7d23c5bebd10d202909e7bd814a791cf2bee0cca62e3c89843098eef', nome_questao='quantos_times_no_campeonato'), 'quantos_times_no_campeonato incorreta'
assert verifica(id_do_primeiro_colocado, 'f8710a62da9145a2e59066443658c4b87d9eef195cd1e69cbca0488e', nome_questao='id_do_primeiro_colocado'), 'id_do_primeiro_colocado incorreta'
assert verifica(faixa_da_libertadores, '4b06d68696e90e7bbeaf7707d40b8400a89b3f1823b2b4fa14f0d192', nome_questao='faixa_da_libertadores'), 'faixa_da_libertadores incorreta'
assert verifica(nome_comum_do_primeiro_colocado, '3208576cd41336181c491d75459a76a221c5b91cf18395fb2bb1b8b9', nome_questao='nome_comum_do_primeiro_colocado'), 'nome_comum_do_primeiro_colocado incorreta'
print('Exercicio conhecendo o dicionario: OK')


'''
EXERCICIO

Tres questoes de multipla escolha sobre o dicionario de equipes.
Se travar, descomente o `explicar(...)` da questao.

Q1 - o_que_e_dados_equipes

O que eh `dados['equipes']`?

    a) uma lista com os nomes dos 20 times
    b) uma lista com as ids dos 20 times
    c) um dicionario: para cada id de time, a ficha dele
       (nome-comum, sigla, nome, ...)
    d) um dicionario: para cada nome de time, a id dele
'''
o_que_e_dados_equipes = 'c'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('o_que_e_dados_equipes')

assert verifica(o_que_e_dados_equipes, 'fb8684d9b6d50caf61aea3dd963a6cc7b6b8881b8d75e7d4f0a1788c', nome_questao='o_que_e_dados_equipes'), 'o_que_e_dados_equipes incorreta'


'''
EXERCICIO

Q2 - por_que_equipes_0_falha

O que acontece com `dados['equipes'][0]`?

    a) da KeyError - 0 nao eh a id de nenhum time
    b) devolve o primeiro time do campeonato
    c) devolve o Corinthians (que eh o time de "primeiro" no coracao)
    d) devolve uma lista com todos os times
'''
por_que_equipes_0_falha = 'a'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('por_que_equipes_0_falha')

assert verifica(por_que_equipes_0_falha, 'e9b61194c3559c5089d38b937016c827e4f80d6a6448dd79ce84c81a', nome_questao='por_que_equipes_0_falha'), 'por_que_equipes_0_falha incorreta'


'''
EXERCICIO

Q3 - caminho_ate_o_campeao

Cada alternativa tem DUAS linhas: a primeira guarda um pedaco da busca
numa variavel intermediaria (primeira_id), e a segunda linha usa essa
variavel. (Voce pode digitar assim no console do VS Code.)

Qual alternativa devolve o NOME-COMUM do campeao (o time que esta na
PRIMEIRA posicao da classificacao)?

    a) primeira_id = dados['equipes'][0]
       dados['equipes'][primeira_id]['nome-comum']
    b) primeira_id = dados['fases']['2700']['classificacao']['grupo']['unico']
       dados['equipes'][primeira_id]['nome-comum']
    c) primeira_id = dados['fases']['2700']['classificacao']['grupo']['unico'][1]
       dados['equipes'][primeira_id]['nome-comum']
    d) primeira_id = dados['fases']['2700']['classificacao']['grupo']['unico'][0]
       dados['equipes'][primeira_id]['nome']
    e) primeira_id = dados['fases']['2700']['classificacao']['grupo']['unico']['0']
       dados['equipes'][primeira_id]['nome-comum']
    f) primeira_id = dados['fases']['2700']['classificacao']['grupo']['unico'][0]
       dados['equipes'][primeira_id]['nome-comum']
    g) primeira_id = dados['classificacao']['grupo']['unico'][0]
       dados['equipes'][primeira_id]['nome-comum']
    h) primeira_id = '17'
       dados['equipes'][primeira_id]['nome-comum']
    i) primeira_id = dados['fases']['2700']['classificacao']['grupo']['unico'][2]
       dados['equipes'][primeira_id]['nome-comum']
    j) primeira_id = dados['fases']['2700']['classificacao']['grupo']['unico'][0]
       dados['equipes'][primeira_id]['sigla']
'''
caminho_ate_o_campeao = 'f'   # 'a' a 'j'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('caminho_ate_o_campeao')

assert verifica(caminho_ate_o_campeao, 'c1ef40d79e7fbf43e8498d2761bcd01afd0dbe04ba4c4efd2894fcd7', nome_questao='caminho_ate_o_campeao'), 'caminho_ate_o_campeao incorreta'
print('Exercicio multipla escolha (dicionario de equipes): OK')


# ===== FASE 2 - nome_do_time =====

'''
EXERCICIO

Faca a funcao nome_do_time(dados, id_numerica) que devolve o nome-comum
do time com aquela id. Eh o acesso simples: dados['equipes'][id] e depois
o campo 'nome-comum'.

    >>> nome_do_time(dados, '1')
    'Flamengo'
'''
def nome_do_time(dados, id_numerica):
    nome = dados['equipes'][id_numerica]['nome-comum']
    return nome

assert nome_do_time(dados2018, '1') == 'Flamengo', 'nome_do_time(dados2018, "1") deveria ser "Flamengo"'
assert nome_do_time(dados2018, '695') == 'Chapecoense', 'nome_do_time(dados2018, "695") deveria ser "Chapecoense"'
print('Exercicio nome_do_time: OK')


# ===== FASE 3 - id_campeao + nome_campeao (primeiro reuso) =====

'''
EXPLICACAO

De vez em quando os testes deste exercicio vao FALSIFICAR os dados:
criam uma copia, mudam alguma coisa nela (por exemplo, tiram o primeiro
da classificacao) e chamam a sua funcao de novo. Se a funcao continuar
respondendo certo com os dados mudados, eh porque ela esta LENDO o json
de verdade.

Eh a regra do jogo: suas funcoes tem que devolver dados oriundos do json,
nao valores decorados. Uma funcao que devolve '17' no id_campeao "porque
o Palmeiras ganhou" passa no teste normal, mas QUEBRA no teste com dados
falsificados - e a falsificacao revela que a funcao nao le a estrutura.

Os asserts de falsificacao usam uma copia separada (dados_falsificado) -
sua funcao nao precisa fazer nada de diferente: recebe os dados por
parametro e le deles, falsificados ou nao.
'''


'''
EXERCICIO

Faca a funcao id_campeao(dados) que devolve a id do time campeao: o
PRIMEIRO elemento da lista de classificacao.

    >>> id_campeao(dados)
    '17'
'''
def id_campeao(dados):
    id_venc = dados['fases']['2700']['classificacao']['grupo']['unico'][0]
    return id_venc

assert id_campeao(dados2018) == '17', 'id_campeao(dados2018) deveria ser "17"'

# FALSIFICACAO: removo o primeiro da classificacao - a funcao tem que ler
# a estrutura, nao devolver um valor decorado
dados_falsificado = pega_dados()
dados_falsificado['fases']['2700']['classificacao']['grupo']['unico'].pop(0)
assert id_campeao(dados_falsificado) == '1', 'id_campeao deve ler a classificacao dos dados (o campeao falsificado eh o "1")'
print('Exercicio id_campeao: OK')


'''
EXPLICACAO

Repare no que o nome_campeao precisa: o nome-comum do time que esta na
primeira posicao. Isso ja se resolveu em dois pedacos:

    - qual a id do campeao?    -> id_campeao(dados)
    - qual o nome dessa id?    -> nome_do_time(dados, id)

Chamar uma funcao DENTRO da outra:

    nome_do_time(dados, id_campeao(dados))

O Python resolve de dentro pra fora: primeiro calcula id_campeao(dados)
(eh a id, uma string), e so depois passa esse resultado pro nome_do_time.
'''


'''
EXERCICIO

Faca a funcao nome_campeao(dados) que devolve o nome-comum do campeao,
USANDO as funcoes id_campeao e nome_do_time (nao leia a estrutura de novo).

    >>> nome_campeao(dados)
    'Palmeiras'
'''
def nome_campeao(dados):
    campeao = id_campeao(dados)
    nome_campeao = dados['equipes'][campeao]['nome-comum']
    return nome_campeao

assert nome_campeao(dados2018) == 'Palmeiras', 'nome_campeao(dados2018) deveria ser "Palmeiras"'
assert nome_campeao(dados_falsificado) == 'Flamengo', 'nome_campeao deve reusar id_campeao (no campeonato falsificado o campeao eh o Flamengo)'
print('Exercicio nome_campeao: OK')


# ===== FASE 4 - qtos_libertadores + ids_dos_melhor_classificados =====

'''
EXPLICACAO

A faixa vem como TEXTO: '1-6'. Quantos times cabem nela? 6 - mas a conta
tem que ser feita pelo python, a partir do texto:

    faixa = '1-6'
    partes = faixa.split('-')    # ['1', '6']
    ultima = int(partes[1])      # 6

Ou seja: a funcao NAO pode chumbar o 6 - ela tem que ler a faixa dos
dados (e o teste falsifica a faixa justamente pra conferir isso).
'''


'''
EXERCICIO

Calculo a mao (de leitura). A faixa do classifica1 vale '1-6' nos dados:
quantos times ela cobre? (primeira posicao ate a sexta posicao)
'''
quantos_libertadores_a_mao = 6

assert verifica(quantos_libertadores_a_mao, '45c4470b227bfbf724de91f50c3d9ede4154335bb79d1e8d058a6b02', nome_questao='quantos_libertadores_a_mao'), 'quantos_libertadores_a_mao incorreta'
print('Exercicio calculo a mao (faixa da libertadores): OK')


'''
EXERCICIO

Faca a funcao qtos_libertadores(dados) que devolve quantos times o
brasileirao classifica para a libertadores. Leia a faixa do classifica1
e use split e int (como na EXPLICACAO acima).

    >>> qtos_libertadores(dados)
    6
'''
def qtos_libertadores(dados):
    classificados = dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa']
    classificados = int(classificados[-1])
    return classificados


assert qtos_libertadores(dados2018) == 6, 'qtos_libertadores(dados2018) deveria ser 6'

# FALSIFICACAO: mudo a faixa nos dados - a funcao tem que ler a faixa
dados_falsificado = pega_dados()
dados_falsificado['fases']['2700']['faixas-classificacao']['classifica1']['faixa'] = '1-8'
assert qtos_libertadores(dados_falsificado) == 8, 'qtos_libertadores deve ler a faixa dos dados (falsifiquei para 1-8)'
print('Exercicio qtos_libertadores: OK')


'''
EXERCICIO

Calculo a mao. A classificacao comeca assim:

    ['17', '1', '15', '13', '24', ...]
    #   0    1    2     3     4

Quais as ids dos 3 MELHORES classificados? (os 3 primeiros da lista)
'''
tres_melhor_a_mao = ['17', '1', '15']

assert verifica(tres_melhor_a_mao, '994de72a1db8662510676551e6a12a37c4e2209eb1dda0cb546e357f', ordem_importa=True, nome_questao='tres_melhor_a_mao'), 'tres_melhor_a_mao incorreta'
print('Exercicio calculo a mao (3 melhores): OK')


'''
EXERCICIO

Faca a funcao ids_dos_melhor_classificados(dados, numero_de_times) que
devolve uma lista com as ids dos N melhores classificados (N = o numero
de times pedido). A lista de classificacao pode ser FATIADA:
classificacao[:numero_de_times] devolve os numero_de_times primeiros.

    >>> ids_dos_melhor_classificados(dados, 3)
    ['17', '1', '15']
'''
def ids_dos_melhor_classificados(dados, numero_de_times):
    classificados = []
    contador = 0
    for i in range(numero_de_times):
        dado = dados['fases']['2700']['classificacao']['grupo']['unico'][contador]
        contador = contador + 1
        classificados.append(dado)
    return classificados



assert ids_dos_melhor_classificados(dados2018, 10) == ['17', '1', '15', '13', '24', '4', '3', '9', '5', '22'], '10 melhores'
assert ids_dos_melhor_classificados(dados2018, 5) == ['17', '1', '15', '13', '24'], '5 melhores'
assert ids_dos_melhor_classificados(dados2018, 3) == ['17', '1', '15'], '3 melhores'
print('Exercicio ids_dos_melhor_classificados: OK')


# ===== FASE 5 - classificados_libertadores + nomes_classificados_libertadores (reuso duplo) =====

'''
EXPLICACAO

classificados_libertadores junta as duas fases anteriores, chamando uma
funcao DENTRO da outra:

    ids_dos_melhor_classificados(dados, qtos_libertadores(dados))

- qtos_libertadores(dados) descobre QUANTOS sao (le a faixa);
- ids_dos_melhor_classificados(dados, n) pega os n primeiros.

E nomes_classificados_libertadores da o passo final: para cada id dos
classificados, o nome (reusando nome_do_time).
'''


'''
EXERCICIO

Faca a funcao classificados_libertadores(dados) que devolve as ids dos
times classificados para a libertadores, reusando as duas funcoes da
Fase 4.

    >>> classificados_libertadores(dados)
    ['17', '1', '15', '13', '24', '4']
'''
def classificados_libertadores(dados):
    libertadores = dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa']
    libertadores = int(libertadores[-1])
    resposta = ids_dos_melhor_classificados(dados,libertadores)
    return resposta

assert classificados_libertadores(dados2018) == ['17', '1', '15', '13', '24', '4'], 'classificados_libertadores(dados2018)'

# FALSIFICACAO: mudo a faixa para 1-8 - os classificados tem que mudar junto
dados_falsificado = pega_dados()
dados_falsificado['fases']['2700']['faixas-classificacao']['classifica1']['faixa'] = '1-8'
assert classificados_libertadores(dados_falsificado) == ['17', '1', '15', '13', '24', '4', '3', '9'], 'classificados_libertadores deve ler a faixa dos dados (falsifiquei para 1-8)'
print('Exercicio classificados_libertadores: OK')


'''
EXERCICIO

Calculo a mao. Os 4 primeiros da classificacao:

    id:    '17'    '1'    '15'    '13'
    nome:  Palmeiras  Flamengo  Internacional  Gremio

Quais os nomes dos 3 primeiros? (na ordem)
'''
tres_nomes_a_mao = ['Palmeiras', 'Flamengo', 'Internacional']

assert verifica(tres_nomes_a_mao, 'ae5225bb79abab3f38d2e6ed314844e59d2f376104a631735ad1c474', ordem_importa=True, nome_questao='tres_nomes_a_mao'), 'tres_nomes_a_mao incorreta'
print('Exercicio calculo a mao (nomes dos 3 melhores): OK')


'''
EXERCICIO

Faca a funcao nomes_classificados_libertadores(dados) que devolve os
NOMES dos classificados para a libertadores, reusando
classificados_libertadores e nome_do_time.

    >>> nomes_classificados_libertadores(dados)[:3]
    ['Palmeiras', 'Flamengo', 'Internacional']
'''
def nomes_classificados_libertadores(dados):
    resposta = []
    contador = 0
    id_classificados = classificados_libertadores(dados)
    qtd = len(id_classificados)
    for i in range(qtd):
        dado = dados['equipes'][id_classificados[contador]]['nome-comum']
        contador = contador + 1
        resposta.append(dado)
    return resposta

# FALSIFICACAO: faixa para 1-3 - agora os classificados sao so 3
dados_falsificado = pega_dados()
dados_falsificado['fases']['2700']['faixas-classificacao']['classifica1']['faixa'] = '1-3'
assert nomes_classificados_libertadores(dados_falsificado) == ['Palmeiras', 'Flamengo', 'Internacional'], 'nomes_classificados_libertadores com faixa 1-3'

dados_falsificado2 = pega_dados()
dados_falsificado2['fases']['2700']['faixas-classificacao']['classifica1']['faixa'] = '1-2'
assert nomes_classificados_libertadores(dados_falsificado2) == ['Palmeiras', 'Flamengo'], 'nomes_classificados_libertadores com faixa 1-2'


print('Exercicio nomes_classificados_libertadores: OK')


# ===== FASE 6 - rebaixados + classificacao_do_time_por_id + id_do_time =====

'''
EXERCICIO

Faca a funcao rebaixados(dados) que devolve as ids dos times na zona de
rebaixamento. Leia a faixa do classifica3 (mesma logica da Fase 4) e
fatia a classificacao.

    >>> rebaixados(dados)
    ['76', '26', '21', '18']
'''
def rebaixados(dados):
    faixa = dados['fases']['2700']['faixas-classificacao']['classifica3']['faixa']
    inicio, fim = faixa.split('-')
    inicio = int(inicio) - 1
    fim = int(fim)
    classificacao = dados['fases']['2700']['classificacao']['grupo']['unico'][inicio:fim]
    return classificacao


assert rebaixados(dados2018) == ['76', '26', '21', '18'], 'rebaixados(dados2018)'

# FALSIFICACAO: mudo a faixa do rebaixamento para 15-20 - os rebaixados mudam
dados_falsificado = pega_dados()
dados_falsificado['fases']['2700']['faixas-classificacao']['classifica3']['faixa'] = '15-20'
assert rebaixados(dados_falsificado) == ['33', '25', '76', '26', '21', '18'], 'rebaixados deve ler a faixa dos dados (falsifiquei para 15-20)'
print('Exercicio rebaixados: OK')


'''
EXERCICIO

Calculo a mao. A classificacao comeca assim, com a POSICAO contada a
partir de 1 (nao de 0):

    posicao:   1        2         3            4        5
    id:       '17'     '1'      '15'         '13'     '24'
    nome:     Palmeiras  Flamengo  Internacional  Gremio  Sao Paulo

Exemplo: a posicao do '17' eh 1 (ele ocupa a primeira posicao).

Qual a posicao do '15'?
'''
posicao_do_15_a_mao = 3

assert verifica(posicao_do_15_a_mao, '87faf03d567a1ca0cdc9483c100044addcc8c6f4c1d445ad69d2aa7d', nome_questao='posicao_do_15_a_mao'), 'posicao_do_15_a_mao incorreta'
print('Exercicio calculo a mao (posicao): OK')


'''
EXERCICIO

Faca a funcao classificacao_do_time_por_id(dados, time_id) que devolve a
POSICAO do time na classificacao (a primeira posicao eh 1, nao 0). Se a
id nao estiver na classificacao, devolva a string 'nao encontrado'.

    >>> classificacao_do_time_por_id(dados, '17')
    1
'''
def classificacao_do_time_por_id(dados, time_id):
    id_time = dados['fases']['2700']['classificacao']['grupo']['unico']
    resposta = id_time.index(time_id)
    resposta = resposta + 1
    return resposta

assert classificacao_do_time_por_id(dados2018, '17') == 1, 'o Palmeiras eh o 1o'
assert classificacao_do_time_por_id(dados2018, '30') == 11, 'o Bahia (30) eh o 11o'
assert classificacao_do_time_por_id(dados2018, '695') == 14, 'a Chapecoense (695) eh a 14a'
#assert classificacao_do_time_por_id(dados2018, '1313') == 'nao encontrado', 'id inexistente devolve "nao encontrado"'
print('Exercicio classificacao_do_time_por_id: OK')


'''
EXPLICACAO

Desta vez a busca eh ao CONTRARIO: recebemos o NOME e procuramos a id.
Percorremos o dicionario de equipes comparando o nome-comum de cada time
com o nome pedido. O laço:

    for id_time in dados['equipes'].keys():
        ...

anda pelas CHAVES do dicionario de equipes (as ids). Pra cada uma,
comparamos dados['equipes'][id_time]['nome-comum'] com o nome procurado.

E se o nome nao existir? Temos que avisar de alguma forma. Aqui vamos
usar raise - mas eh uma RECEITA DE BOLO: se voce ainda nao aprendeu
raise (eh materia de uma aula futura), nao precisa entender os detalhes.
Eh so fazer colocar esse codigo na hora de notificar que
o time procurado nao existe.

    raise KeyError('nao encontrado')

Isso "interrompe" o programa no meio, avisando que o nome nao foi
encontrado. O teste usa a funcao checa_erro (no topo do arquivo) pra
conferir que isso acontece.
'''


'''
EXERCICIO

Faca a funcao id_do_time(dados, nome_time) que devolve a id do time com
aquele nome-comum. Se o nome nao existir, siga a receita: raise
KeyError('nao encontrado').

    >>> id_do_time(dados, 'Cruzeiro')
    '9'
'''
def id_do_time(dados, nome_time):
    times = dados['equipes']
    for id in times:
        if times[id]['nome-comum'] == nome_time:
            return id
    raise KeyError

assert id_do_time(dados2018, 'Cruzeiro') == '9', 'id_do_time(dados2018, "Cruzeiro") deveria ser "9"'
assert id_do_time(dados2018, 'Athletico') == '3', 'id_do_time(dados2018, "Athletico") deveria ser "3"'
assert checa_erro(lambda: id_do_time(dados2018, 'Time Fantasma'), KeyError), 'id_do_time deve dar KeyError para nome inexistente'
print('Exercicio id_do_time: OK')


# ===== FASE 7 - Simulacao integrada =====

'''
EXPLICACAO

Fechando a lista: vamos "rodar o campeonato" usando TODAS as funcoes em
ordem natural - campeao, classificados, rebaixados, posicao de um time,
id de um time - sobre os MESMOS dados.

Para cada resposta abaixo, PRIMEIRO preveja (calcule com a cabeca,
consultando os dados se precisar) - e so depois os asserts confirmam,
rodando as funcoes de verdade.
'''


'''
EXERCICIO

Preveja os valores (so depois os asserts abaixo conferem com as funcoes):

1) a id do campeao                       (id_campeao)
2) o nome do campeao                     (nome_campeao)
3) quantos times vao para a libertadores (qtos_libertadores)
4) as ids dos classificados              (classificados_libertadores)
5) os NOMES dos 3 primeiros classificados
   (nomes_classificados_libertadores - so os 3 primeiros)
6) as ids dos rebaixados                 (rebaixados)
7) a posicao do Flamengo (id '1')        (classificacao_do_time_por_id)
8) a id do Santos                        (id_do_time)
'''
campeao_id        = 'coloque o valor aqui'
campeao_nome      = 'coloque o valor aqui'
quantos_libertadores = 'coloque o valor aqui'
classificados_ids = 'coloque o valor aqui'
classificados_nomes_3 = 'coloque o valor aqui'
rebaixados_ids    = 'coloque o valor aqui'
posicao_do_flamengo = 'coloque o valor aqui'
id_do_santos      = 'coloque o valor aqui'

assert verifica(campeao_id, 'aa9aa404e11b68d75564f01fb3d2160eb5f19441f8232152edf47311', nome_questao='campeao_id'), 'campeao_id incorreta'
assert verifica(campeao_nome, '4b3d913e356bfa87685772913cba856dd56e58381b8dcd2dfd8075b4', nome_questao='campeao_nome'), 'campeao_nome incorreta'
assert verifica(quantos_libertadores, '4b137adddc6dd67fccb913911cd44ffd4b37043c0453254b3eaec64e', nome_questao='quantos_libertadores'), 'quantos_libertadores incorreta'
assert verifica(classificados_ids, 'c9a4745b8727a9811f82ed8f62d3d489e6e3e95c606df908b4a1914b', ordem_importa=True, nome_questao='classificados_ids'), 'classificados_ids incorreta'
assert verifica(classificados_nomes_3, 'd458c6527395e44485160c41bc96e060548461980df5c9a16d547ce1', ordem_importa=True, nome_questao='classificados_nomes_3'), 'classificados_nomes_3 incorreta'
assert verifica(rebaixados_ids, '752c67bf7b18d71bb24d10a7acbfca9333aea63b88a4f11abdbb8fe2', ordem_importa=True, nome_questao='rebaixados_ids'), 'rebaixados_ids incorreta'
assert verifica(posicao_do_flamengo, '2dc916ffbe61d8b125e78e6d293a3dfe10c57a5948e8f0b9fdcb5805', nome_questao='posicao_do_flamengo'), 'posicao_do_flamengo incorreta'
assert verifica(id_do_santos, 'a7529fe84f3100b14082650aa6251d0cd24293007393eccd8d652027', nome_questao='id_do_santos'), 'id_do_santos incorreta'
print('Exercicio simulacao integrada (previsao): OK')

# agora as funcoes confirmam a sua previsao
assert id_campeao(dados2018) == '17', 'id_campeao'
assert nome_campeao(dados2018) == 'Palmeiras', 'nome_campeao'
assert qtos_libertadores(dados2018) == 6, 'qtos_libertadores'
assert classificados_libertadores(dados2018) == ['17', '1', '15', '13', '24', '4'], 'classificados_libertadores'
assert nomes_classificados_libertadores(dados2018)[:3] == ['Palmeiras', 'Flamengo', 'Internacional'], 'nomes dos 3 primeiros classificados'
assert rebaixados(dados2018) == ['76', '26', '21', '18'], 'rebaixados'
assert classificacao_do_time_por_id(dados2018, '1') == 2, 'posicao do Flamengo'
assert id_do_time(dados2018, 'Santos') == '22', 'id do Santos'
print('Exercicio simulacao integrada (confirmacao): OK')


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
        print('=== BRASILEIRAO 2018 ===')
        print('1. nome de um time (por id)')
        print('2. campeao (id e nome)')
        print('3. classificados para a libertadores')
        print('4. rebaixados')
        print('5. classificacao de um time (por id)')
        print('6. Sair')
        opcao = input('Opcao: ')

        if opcao == '1':
            # FUNCIONALIDADE 1 - nome de um time pela id digitada. Nao
            # precisa de try/except: id que nao existe da KeyError, e
            # tudo bem (isso eh materia da aula de erros).
            # Organize as pecas abaixo (na ordem certa):
            #
            #     id_time = input('  id do time: ')
            #     nome = nome_do_time(dados, id_time)
            #     print(f'  {nome}')
            #
            pass  # COMPLETE: monte a funcionalidade 1 com as pecas acima

        elif opcao == '2':
            # FUNCIONALIDADE 2 - campeao: id e nome. Nao precisa de
            # try/except.
            #
            #     print('  campeao:')
            #     print(f'    id:   {id_campeao(dados)}')
            #     print(f'    nome: {nome_campeao(dados)}')
            #
            pass  # COMPLETE: monte a funcionalidade 2

        elif opcao == '3':
            # FUNCIONALIDADE 3 - classificados para a libertadores: ids
            # e nomes. Nao precisa de try/except.
            #
            #     classificados = classificados_libertadores(dados)
            #     nomes = nomes_classificados_libertadores(dados)
            #     print('  classificados para a libertadores:')
            #     print(f'    ids:   {classificados}')
            #     print(f'    nomes: {nomes}')
            #
            pass  # COMPLETE: monte a funcionalidade 3

        elif opcao == '4':
            # FUNCIONALIDADE 4 - rebaixados (ids). Nao precisa de
            # try/except.
            #
            #     rebaixados_lista = rebaixados(dados)
            #     print('  rebaixados (ids):')
            #     print(f'    {rebaixados_lista}')
            #
            pass  # COMPLETE: monte a funcionalidade 4

        elif opcao == '5':
            # FUNCIONALIDADE 5 - classificacao de um time pela id
            # digitada. Nao precisa de try/except: id que nao existe
            # devolve a string 'nao encontrado' (a funcao nao levanta).
            #
            #     id_time = input('  id do time: ')
            #     posicao = classificacao_do_time_por_id(dados, id_time)
            #     print(f'  posicao do time {id_time}: {posicao}')
            #
            pass  # COMPLETE: monte a funcionalidade 5

        elif opcao == '6':
            break
        else:
            print('Opcao invalida')


# Pra rodar a interface, descomente:
# main()


print('\n=== PARABENS! Todos os exercicios completos! ===')
