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


# === Helper de dicas (pode ignorar o codigo) ===
# As questoes de papel-e-lapis desta lista (as que voce responde
# preenchendo uma variavel) tem uma explicacao guardada (embaralhada) no
# arquivo explicacao_arvores.py, que vem junto com este. Quando travar
# numa questao, descomente a linha `# explicar('nome')` logo abaixo dela
# e rode o arquivo: a explicacao aparece.
'''def explicar(questao):
    try:
        from explicacao_arvores import EXPLICACOES
    except ImportError:
        print("Arquivo 'explicacao_arvores.py' nao foi encontrado.")
        print("Esse arquivo vem JUNTO com este exercicio - peca ao")
        print("professor.")
        return
    import codecs
    if questao not in EXPLICACOES:
        print(f"Nao tenho explicacao para '{questao}'.")
        print(f"Questoes disponiveis: {sorted(EXPLICACOES.keys())}")
        return
    print(codecs.decode(EXPLICACOES[questao], 'rot_13'))
    input("aperte enter para continuar")
# fim do helper de dicas
'''

r'''
EXPLICACAO

Uma arvore eh uma estrutura como

      10
     /  \
    5    20
   / \   / \
  2   7 12  30

Observe que 10 tem elementos a sua "esquerda" (5, 2 e 7)
e a sua "direita" (20, 12 e 30).

Os elementos a esquerda sao numeros MENORES que 10,
e os elementos a direita, MAIORES que 10.

(O mesmo vale para o 5: a esquerda temos 2, que eh menor,
e a direita 7, que eh maior.)
'''


# ===== FASE 1 - Andando na arvore (a mao) =====

r'''
EXPLICACAO

Perceba que, para verificar se um numero esta nessa arvore, precisamos
usar apenas 3 consultas.

      10
     /  \
    5    20
   / \   / \
  2   7 12  30

O 12 esta na arvore?

    Olho pro 10. Se o 12 estiver, esta na arvore da direita
    (onde estao todos os numeros maiores que 10 da arvore).
    Olho pro 20. Se o 12 estiver, esta na arvore da esquerda
    (onde estao todos os numeros menores que 20 da "subarvore").
    Olho pro 12, e achei!

    A resposta eh True.
    A sequencia de numeros visitados foi [10, 20, 12]

O 9 esta na arvore?

    Olho pro 10. Se o 9 estiver, esta na arvore da esquerda
    (onde estao todos os numeros menores que 10 da arvore).
    Olho pro 5. Se o 9 estiver, esta na arvore da direita
    (onde estao todos os numeros maiores que 5 da "subarvore").
    Olho pro 7. Queria procurar "a direita" dele, mas nao tem ninguem.

    A resposta eh False.
    A sequencia de numeros visitados foi [10, 5, 7]

Repare que a sequencia lista os numeros que voce OLHOU - e nao o numero
que voce procurava.
'''

r'''
EXERCICIO

      10
     /  \
    5    20
   / \   / \
  2   7 12  30

Se eu quiser procurar o 40 nessa arvore, que numeros visitarei?

Responda com a lista dos numeros visitados, na ordem em que voce olha
para eles - como o [10, 20, 12] do exemplo acima.
'''
busca40 = [10,20,30]

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('busca40')

assert verifica(busca40, 'feb9e440ff56772c4479f005489fe8b7b914bee97e9742b1fa01eb0c', ordem_importa=True), 'busca40 incorreta'

r'''
EXERCICIO

Mesma arvore:

      10
     /  \
    5    20
   / \   / \
  2   7 12  30

E se eu quiser buscar o 15? Que numeros visitarei?
'''
busca15 = [10,20,12]

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('busca15')

assert verifica(busca15, 'ab437c0e9544f634d919fff8592eef327db3ed8567cad06c8b1d9afc', ordem_importa=True), 'busca15 incorreta'

r'''
EXERCICIO

Mesma arvore:

      10
     /  \
    5    20
   / \   / \
  2   7 12  30

E o 3?
'''
busca3 = [10,5,2]

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('busca3')

assert verifica(busca3, 'e8f50d09a2838980b07dc396e5f5767e85c90e0dd100700bb2f638b8', ordem_importa=True), 'busca3 incorreta'

r'''
EXERCICIO

Mesma arvore:

      10
     /  \
    5    20
   / \   / \
  2   7 12  30

E o 5?
'''
busca5 = [10,5]

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('busca5')

assert verifica(busca5, '37bc87547ee4ffb1b04a4927e097209938ffb3f7d1b7a49360e09d61', ordem_importa=True), 'busca5 incorreta'
print('Exercicio buscas a mao: OK')


# ===== FASE 2 - Onde cada numero entra (a mao) =====

r'''
EXPLICACAO

Uma outra questao importante eh a insercao.

        20
     /      \
    10      30
   /  \    /  \
  8   C   D    E
 / \
A  B

As letras A, B, C, D e E sao as posicoes VAZIAS da arvore - os lugares
onde um numero novo pode entrar.

Se eu quiser inserir o numero 40 nessa arvore, a posicao correta para
fazer isso eh a posicao E (40 eh maior que 20, tem que estar a direita
do 20; tambem eh maior que 30, entao tem que estar a direita do 30).

Se eu quiser inserir o numero 12, a posicao correta eh C (ele tem que
estar a esquerda do 20, mas a direita do 10).
'''

r'''
EXERCICIO (examplo ja respondido, so para voce conferir)

        20
     /      \
    10      30
   /  \    /  \
  8   C   D    E
 / \
A  B

Se eu te der uma lista de numeros, quero uma lista que diga onde eles
devem ser inseridos. Por exemplo, para

    numeros1 = [2, 11, 25]

a resposta eh

    letras1 = ['A', 'C', 'D']

    o 2  eh menor que 20 -> esquerda; menor que 10 -> esquerda;
                            menor que 8 -> esquerda  ...... A
    o 11 eh menor que 20 -> esquerda; maior que 10 -> direita ... C
    o 25 eh maior que 20 -> direita;  menor que 30 -> esquerda .. D

Estas duas ja estao preenchidas - sao o exemplo. As duas de baixo sao
com voce.
'''
numeros1 = [2, 11, 25]
letras1 = ['A', 'C', 'D']

r'''
EXERCICIO

Mesma arvore:

        20
     /      \
    10      30
   /  \    /  \
  8   C   D    E
 / \
A  B

Faca o mesmo para

    numeros2 = [19, 21, 33, 7]

Responda com uma lista de letras, na mesma ordem dos numeros - como o
['A', 'C', 'D'] do exemplo.
'''
numeros2 = [19, 21, 33, 7]
letras2 = ['C','D','E','A']

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('letras2')

assert verifica(letras2, 'cd144b3ba1fd2bc639eef7ae6f04c98a09ebecf7ec6f53d1874ec199', ordem_importa=True), 'letras2 incorreta'

r'''
EXERCICIO

Mesma arvore:

        20
     /      \
    10      30
   /  \    /  \
  8   C   D    E
 / \
A  B

E agora para

    numeros3 = [9, 11, 7, 50]
'''
numeros3 = [9, 11, 7, 50]
letras3 = ['B','C','A','E']

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('letras3')

assert verifica(letras3, '80150a2e2007176ea15ba99718131cace42a660947208280340a5df4', ordem_importa=True), 'letras3 incorreta'
print('Exercicio insercoes a mao: OK')


# ===== FASE 3 - A arvore em Python =====

# Para o que vem a seguir, eh legal usar a funcao pprint, que imprime
# dicionarios de uma forma legivel.
from pprint import pprint

r'''
EXPLICACAO

Para representar arvores em Python, usamos DICIONARIOS - os mesmos das
aulas de agenda, so que agora um dicionario guarda outro dicionario
dentro dele.

Cada arvore eh um dicionario com tres chaves: 'raiz', 'esquerda' e
'direita'. Por exemplo, para representar uma arvore que so contem o 30,
fazemos

    arvore = {'raiz': 30, 'esquerda': {}, 'direita': {}}

As chaves 'esquerda' e 'direita' guardam OUTRAS ARVORES. Aqui as duas
estao vazias - e uma arvore vazia eh so o dicionario vazio, {}.

Usando essa ideia recursivamente, nao eh dificil representar

     30
    /  \
   20   40
        / \
      35   45

    arvore = {'raiz': 30,
              'esquerda': {'raiz': 20,
                           'esquerda': {},
                           'direita': {}},
              'direita': {'raiz': 40,
                          'esquerda': {'raiz': 35, 'esquerda': {}, 'direita': {}},
                          'direita': {'raiz': 45, 'esquerda': {}, 'direita': {}}},
              }

Leia de fora para dentro: a raiz eh 30; a esquerda dela eh uma arvore
cuja raiz eh 20 e que nao tem filhos; a direita dela eh uma arvore cuja
raiz eh 40, e essa por sua vez tem duas arvores penduradas.
'''

arvore_exemplo = {'raiz': 30,
                  'esquerda': {'raiz': 20,
                               'esquerda': {},
                               'direita': {}},
                  'direita': {'raiz': 40,
                              'esquerda': {'raiz': 35, 'esquerda': {}, 'direita': {}},
                              'direita': {'raiz': 45, 'esquerda': {}, 'direita': {}}},
                  }

breakpoint_aqui = 42

# PARE
# Experimente acessar esse dicionario, via pythontutor ou via o REPL
# do vscode (ponha um breakpoint na linha `breakpoint_aqui = 42` acima,
# rode com 'debug python file', use o debug console)
# digite coisas como print(arvore_exemplo),
# pprint(arvore_exemplo), print(arvore_exemplo['raiz'])
# Depois tente usar o dicionario para printar coisas como
# 40, 35, {'raiz': 45, 'esquerda': {}, 'direita': {}} e depois 20
# -- ou seja, faca os acessos usando esse dicionario para revelar esses
# valores.
# Se nao conseguir, me chame

r'''
EXERCICIO

Agora voce monta uma arvore.

Insira o 100, depois o 30, depois o 40, depois o 110. Voce deve acabar
com esta arvore aqui:

      100
     /   \
    30    110
     \
      40

Ja vou iniciar pra voce - complete as chaves 'esquerda' e 'direita'.

Se quiser conferir o que voce montou, use pprint(arvore100): ele imprime
o dicionario identado, de um jeito mais facil de ler.
'''
arvore100 = {'raiz': 100, 'esquerda': {'raiz': 30, 'esquerda':{}, 'direita':{'raiz': 40, 'esquerda':{}, 'direita':{}}}, 'direita': {'raiz':110, 'esquerda':{}, 'direita':{}}}

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('arvore100')

assert arvore100['raiz'] == 100, f"arvore100['raiz'] deveria ser 100, esta {arvore100.get('raiz')}"

assert arvore100['esquerda'] != {}, 'arvore100: o 30 deveria estar pendurado a esquerda do 100, mas o lado esquerdo esta vazio'
assert arvore100['esquerda'].get('raiz') == 30, f"arvore100['esquerda']['raiz'] deveria ser 30, esta {arvore100['esquerda'].get('raiz')}"
assert arvore100['esquerda'].get('esquerda') == {}, "arvore100: a esquerda do 30 deveria ser a arvore vazia, {} - nao entrou numero nenhum menor que 30"

assert arvore100['esquerda'].get('direita') != {}, 'arvore100: o 40 deveria estar pendurado a direita do 30, mas ali esta vazio'
assert arvore100['esquerda']['direita'].get('raiz') == 40, f"arvore100['esquerda']['direita']['raiz'] deveria ser 40, esta {arvore100['esquerda']['direita'].get('raiz')}"
assert arvore100['esquerda']['direita'].get('esquerda') == {}, 'arvore100: o 40 nao deveria ter ninguem pendurado a esquerda dele - e ele precisa ter a chave, valendo {}'
assert arvore100['esquerda']['direita'].get('direita') == {}, 'arvore100: o 40 nao deveria ter ninguem pendurado a direita dele - e ele precisa ter a chave, valendo {}'

assert arvore100['direita'] != {}, 'arvore100: o 110 deveria estar pendurado a direita do 100, mas o lado direito esta vazio'
assert arvore100['direita'].get('raiz') == 110, f"arvore100['direita']['raiz'] deveria ser 110, esta {arvore100['direita'].get('raiz')}"
assert arvore100['direita'].get('esquerda') == {}, 'arvore100: o 110 nao deveria ter ninguem pendurado a esquerda dele - e ele precisa ter a chave, valendo {}'
assert arvore100['direita'].get('direita') == {}, 'arvore100: o 110 nao deveria ter ninguem pendurado a direita dele - e ele precisa ter a chave, valendo {}'
print('Exercicio arvore100: OK')

'''
EXPLICACAO

Representar uma arvore vazia eh bem facil:
'''
vazia = {}
'''
(se voce notar, ja fizemos isso varias vezes!)
'''


# ===== FASE 4 - Lendo a arvore =====

# As arvores que os testes das proximas fases usam. Nao mexa nelas -
# elas ja estao prontas, e os asserts contam com o formato delas.
#
#       10
#      /  \
#     5    20
#    / \   / \
#   2   7 12  30
arvore2 = {'raiz': 2, 'esquerda': {}, 'direita': {}}
arvore7 = {'raiz': 7, 'esquerda': {}, 'direita': {}}
arvore5 = {'raiz': 5, 'esquerda': arvore2, 'direita': arvore7}
arvore12 = {'raiz': 12, 'esquerda': {}, 'direita': {}}
arvore30 = {'raiz': 30, 'esquerda': {}, 'direita': {}}
arvore20 = {'raiz': 20, 'esquerda': arvore12, 'direita': arvore30}
arvore10 = {'raiz': 10, 'esquerda': arvore5, 'direita': arvore20}

#       10                    10              90                400
#      /  \                  /               /  \              /   \
#     5    15               3               5    120         12     1000
#    / \   / \             /                 \   /          /  \    /  \
#   2   7 12  20          2                  10 110        6   300 500  2000
#                                                              /  \
#                                                            150   301
ex1 = {'raiz': 10,
       'esquerda': {'raiz': 5,
                    'esquerda': {'raiz': 2, 'esquerda': {}, 'direita': {}},
                    'direita': {'raiz': 7, 'esquerda': {}, 'direita': {}}},
       'direita': {'raiz': 15,
                   'esquerda': {'raiz': 12, 'esquerda': {}, 'direita': {}},
                   'direita': {'raiz': 20, 'esquerda': {}, 'direita': {}}},
       }

ex2 = {'raiz': 10,
       'esquerda': {'raiz': 3,
                    'esquerda': {'raiz': 2, 'esquerda': {}, 'direita': {}},
                    'direita': {}},
       'direita': {},
       }

ex3 = {'raiz': 90,
       'esquerda': {'raiz': 5,
                    'esquerda': {},
                    'direita': {'raiz': 10, 'esquerda': {}, 'direita': {}}},
       'direita': {'raiz': 120,
                   'esquerda': {'raiz': 110, 'esquerda': {}, 'direita': {}},
                   'direita': {}},
       }

ex4 = {'raiz': 400,
       'esquerda': {'raiz': 12,
                    'esquerda': {'raiz': 6, 'esquerda': {}, 'direita': {}},
                    'direita': {'raiz': 300,
                                'esquerda': {'raiz': 150, 'esquerda': {}, 'direita': {}},
                                'direita': {'raiz': 301, 'esquerda': {}, 'direita': {}}}},
       'direita': {'raiz': 1000,
                   'esquerda': {'raiz': 500, 'esquerda': {}, 'direita': {}},
                   'direita': {'raiz': 2000, 'esquerda': {}, 'direita': {}}},
       }

#    12
#   /
#  11
#  /
# 10
# /
# 9
arv_torta = {'raiz': 12,
             'esquerda': {'raiz': 11,
                          'esquerda': {'raiz': 10,
                                       'esquerda': {'raiz': 9, 'esquerda': {}, 'direita': {}},
                                       'direita': {}},
                          'direita': {}},
             'direita': {},
             }

'''
EXERCICIO

A primeira funcao que vamos fazer nesse arquivo recebe uma arvore e
retorna a sua raiz.

Se a arvore for vazia, sua funcao deve retornar a string 'nao tem raiz'.

    >>> raiz({'raiz': 5, 'esquerda': {}, 'direita': {}})
    5
    >>> raiz({})
    'nao tem raiz'
'''
def raiz(arvore):
    if 'raiz' not in arvore:
        return 'nao tem raiz'
    raiz = arvore['raiz']
    return raiz

assert raiz(arvore5) == 5, f'raiz(arvore5) deveria ser 5, voce retornou {raiz(arvore5)}'
assert raiz(ex1) == 10, f'raiz(ex1) deveria ser 10, voce retornou {raiz(ex1)}'
assert raiz(ex2) == 10, f'raiz(ex2) deveria ser 10, voce retornou {raiz(ex2)}'
assert raiz(ex3) == 90, f'raiz(ex3) deveria ser 90, voce retornou {raiz(ex3)}'
assert raiz(arvore2) == 2, f'raiz(arvore2) deveria ser 2, voce retornou {raiz(arvore2)}'
assert raiz({}) == 'nao tem raiz', f"raiz({{}}) deveria ser a string 'nao tem raiz', voce retornou {raiz({})}"
print('Exercicio raiz: OK')

r'''
EXERCICIO

Uma arvore tem tipicamente 2 arvores "penduradas" nela, a da direita e a
da esquerda.

Faca uma funcao que, dada uma arvore, retorna a arvore da esquerda.

Se a arvore a esquerda for vazia, pode devolver ela mesma (ou seja, {}).

Se nao houver arvore a esquerda - porque a arvore que voce recebeu eh
ela mesma vazia, e nem chave 'esquerda' tem -, sua funcao deve retornar
a string 'esquerda vazia'.

    >>> arvore_esquerda({'raiz': 5, 'esquerda': {'raiz': 2, 'esquerda': {}, 'direita': {}}, 'direita': {}})
    {'raiz': 2, 'esquerda': {}, 'direita': {}}
    >>> arvore_esquerda({})
    'esquerda vazia'
'''
def arvore_esquerda(arvore):
    if 'esquerda' not in arvore:
        return 'esquerda vazia'
    esquerda = arvore['esquerda']
    return esquerda

assert arvore_esquerda(arvore5) == arvore2, f'arvore_esquerda(arvore5) deveria ser a arvore do 2, voce retornou {arvore_esquerda(arvore5)}'
assert arvore_esquerda(arvore10) == arvore5, f'arvore_esquerda(arvore10) deveria ser a arvore do 5, voce retornou {arvore_esquerda(arvore10)}'
assert arvore_esquerda(arvore20) == arvore12, f'arvore_esquerda(arvore20) deveria ser a arvore do 12, voce retornou {arvore_esquerda(arvore20)}'
assert arvore_esquerda(arvore12) == {}, f'arvore_esquerda(arvore12) deveria ser a arvore vazia, voce retornou {arvore_esquerda(arvore12)}'
assert arvore_esquerda({}) == 'esquerda vazia', f"arvore_esquerda({{}}) deveria ser a string 'esquerda vazia', voce retornou {arvore_esquerda({})}"
print('Exercicio arvore_esquerda: OK')

r'''
EXERCICIO

O proximo passo: uma funcao que recebe uma arvore A, vai andando para a
esquerda "ate nao poder mais" (ate estar em uma arvore que nao tem filho
esquerdo) e devolve a raiz correspondente a essa arvore mais a esquerda.

CUIDADO: se a raiz nao tiver um filho a esquerda, a resposta correta eh
a propria raiz.

    >>> tudo_a_esquerda({'raiz': 5, 'esquerda': {'raiz': 2, 'esquerda': {}, 'direita': {}}, 'direita': {}})
    2
    >>> tudo_a_esquerda({'raiz': 7, 'esquerda': {}, 'direita': {}})
    7
'''
def tudo_a_esquerda(arvore):
    while arvore['esquerda'] != {}:
        arvore = arvore['esquerda']
    return arvore['raiz']

def tudo_a_direita(arvore):
    while arvore['direita'] != {}:
        arvore = arvore['direita']
    return arvore['raiz']

    

print('  iniciando testes de tudo_a_esquerda')
print('  (Se travar aqui, voce tem um loop infinito - rode no pythontutor para ver o que esta acontecendo.)')
assert tudo_a_esquerda(arvore5) == 2, f'tudo_a_esquerda(arvore5) deveria ser 2, voce retornou {tudo_a_esquerda(arvore5)}'
assert tudo_a_esquerda(arvore10) == 2, f'tudo_a_esquerda(arvore10) deveria ser 2, voce retornou {tudo_a_esquerda(arvore10)}'
assert tudo_a_esquerda(arvore20) == 12, f'tudo_a_esquerda(arvore20) deveria ser 12, voce retornou {tudo_a_esquerda(arvore20)}'
assert tudo_a_esquerda(arvore7) == 7, f'tudo_a_esquerda(arvore7) deveria ser 7 (o 7 nao tem filho a esquerda - a resposta eh ele mesmo), voce retornou {tudo_a_esquerda(arvore7)}'
assert tudo_a_esquerda(ex3) == 5, f'tudo_a_esquerda(ex3) deveria ser 5 (o 5 nao tem filho a esquerda), voce retornou {tudo_a_esquerda(ex3)}'
assert tudo_a_esquerda(arv_torta) == 9, f'tudo_a_esquerda(arv_torta) deveria ser 9, voce retornou {tudo_a_esquerda(arv_torta)}'
print('Exercicio tudo_a_esquerda: OK')


# ===== FASE 5 - Buscar e inserir =====

r'''
EXERCICIO

Agora, facamos uma funcao que recebe uma arvore e um numero, e faz uma
busca para ver se o numero esta ou nao na arvore - a mesma busca que
voce fez a mao na Fase 1.

Ela retorna True se o numero esta na arvore, False caso contrario.

    >>> busca({'raiz': 5, 'esquerda': {'raiz': 2, 'esquerda': {}, 'direita': {}}, 'direita': {}}, 2)
    True
    >>> busca({'raiz': 5, 'esquerda': {'raiz': 2, 'esquerda': {}, 'direita': {}}, 'direita': {}}, 3)
    False
'''
def busca(arvore,procurado):
    while True:
        if arvore == {}:
            return False
        elif arvore['raiz'] == procurado:
            return True
        elif arvore['raiz'] > procurado:
            if arvore['esquerda'] == {}:
                return False
            arvore = arvore['esquerda']
        elif arvore['raiz'] < procurado:
            if arvore['direita'] == {}:
                return False
            arvore = arvore['direita']
            
print('  iniciando testes de busca')
print('  (Se travar aqui, voce tem um loop infinito - rode no pythontutor para ver o que esta acontecendo.)')
assert busca(arvore10, 10) == True, 'busca(arvore10, 10) deveria ser True - o 10 eh a propria raiz'
assert busca(arvore10, 15) == False, 'busca(arvore10, 15) deveria ser False - o 15 nao esta na arvore'
assert busca(ex3, 91) == False, 'busca(ex3, 91) deveria ser False'
assert busca(ex3, 90) == True, 'busca(ex3, 90) deveria ser True'
assert busca(arvore5, 5) == True, 'busca(arvore5, 5) deveria ser True'
assert busca(arvore10, 20) == True, 'busca(arvore10, 20) deveria ser True'
assert busca(arvore10, 7) == True, 'busca(arvore10, 7) deveria ser True - o 7 eh uma folha, la embaixo a esquerda'
assert busca(arvore10, 8) == False, 'busca(arvore10, 8) deveria ser False - o 8 cairia embaixo do 7, onde nao tem ninguem'
assert busca(arvore10, 12) == True, 'busca(arvore10, 12) deveria ser True'
assert busca(arv_torta, 10) == True, 'busca(arv_torta, 10) deveria ser True'
assert busca(arv_torta, 9) == True, 'busca(arv_torta, 9) deveria ser True - o 9 eh o ultimo da fila, la no fundo'
assert busca(arv_torta, 8) == False, 'busca(arv_torta, 8) deveria ser False'
assert busca(ex4, 301) == True, 'busca(ex4, 301) deveria ser True'
assert busca(ex4, 299) == False, 'busca(ex4, 299) deveria ser False'
assert busca({}, 12) == False, 'busca em arvore vazia deveria ser False - nao tem ninguem la'
assert busca({}, 10) == False, 'busca em arvore vazia deveria ser False - nao tem ninguem la'
assert busca({}, 9) == False, 'busca em arvore vazia deveria ser False - nao tem ninguem la'
assert busca({}, 8) == False, 'busca em arvore vazia deveria ser False - nao tem ninguem la'
print('Exercicio busca: OK')

r'''
EXPLICACAO

Agora, vamos fazer uma funcao para inserir um elemento em uma arvore.

Por exemplo, ao pegarmos a arvore

      10
     /  \
    5    20
   / \   / \
  2   7 12  30

e inserirmos o elemento 15, temos

      10
     /  \
    5    20
   / \   / \
  2   7 12  30
        \
        15

(Estamos mantendo as propriedades: o 15 tem que estar a direita do 10, a
esquerda do 20 e a direita do 12.)

(Outra coisa: se inserirmos o 5, nada acontece, porque ele ja esta na
arvore.)

Se quiser, depois de cada insercao, pode usar pprint(arvore). O pprint eh
legal para voce ver as arvores: ele imprime a arvore identada, de uma
maneira mais facil de ler.
'''

r'''
EXERCICIO

Faca a funcao insere(arvore, elemento).

Ela nao precisa retornar nada - basta MODIFICAR o dicionario que ela
recebeu. Repare que isso inclui o caso da arvore vazia: receber {} e
deixar ele com raiz, esquerda e direita.

    >>> t = {}
    >>> insere(t, 5)
    >>> t
    {'raiz': 5, 'esquerda': {}, 'direita': {}}
    >>> insere(t, 2)
    >>> t
    {'raiz': 5, 'esquerda': {'raiz': 2, 'esquerda': {}, 'direita': {}}, 'direita': {}}
'''
def insere(arvore,elemento):
    while True:
        if arvore == {}: #se estiver vazia ele adiciona
            arvore['raiz'] = elemento
            arvore['esquerda'] = {}
            arvore['direita'] = {}
            return
        elif arvore['raiz'] == elemento: #inicio da verificaçao caso, ja exista algum item adicionado na arvre
            return
        elif arvore['raiz'] > elemento:
            arvore =arvore['esquerda']
        elif arvore['raiz'] < elemento:
            arvore = arvore['direita']



print('  iniciando testes de insere')
print('  (Se travar aqui, voce tem um loop infinito - rode no pythontutor para ver o que esta acontecendo.)')

d5 = {'raiz': 5, 'esquerda': {}, 'direita': {}}
insere(d5, 2)
insere(d5, 7)
assert d5 == arvore5, f'depois de inserir 2 e 7 no 5, esperado {arvore5}, obteve {d5}'

d10 = {'raiz': 10, 'esquerda': {}, 'direita': {}}
insere(d10, 10)
insere(d10, 5)
insere(d10, 2)
insere(d10, 7)
insere(d10, 20)
insere(d10, 12)
insere(d10, 30)
assert d10 == arvore10, f'depois de inserir 10, 5, 2, 7, 20, 12 e 30, esperado a arvore do desenho, obteve {d10}'

d2 = {}
insere(d2, 2)
assert d2 == arvore2, f'insere(  {{}}, 2) deveria deixar {arvore2}, obteve {d2}'

d5b = {}
insere(d5b, 5)
insere(d5b, 2)
insere(d5b, 7)
assert d5b == arvore5, f'comecando do vazio e inserindo 5, 2 e 7, esperado {arvore5}, obteve {d5b}'

d10b = {}
insere(d10b, 10)
insere(d10b, 5)
insere(d10b, 2)
insere(d10b, 7)
insere(d10b, 20)
insere(d10b, 12)
insere(d10b, 30)
assert d10b == arvore10, f'comecando do vazio, esperado a arvore do desenho, obteve {d10b}'

d10c = {}
insere(d10c, 10)
insere(d10c, 5)
insere(d10c, 2)
insere(d10c, 7)
insere(d10c, 20)
insere(d10c, 12)
insere(d10c, 30)
insere(d10c, 10)
insere(d10c, 5)
insere(d10c, 20)
insere(d10c, 30)
assert d10c == arvore10, f'inserir um numero que JA esta na arvore nao pode mudar nada, mas mudou: obteve {d10c}'
print('Exercicio insere: OK')

r'''
EXPLICACAO

De brinde, agora que voce tem o insere: com ele da pra montar uma arvore
a partir de uma lista qualquer, sem escrever dicionario nenhum a mao.

    >>> cria_simples([10, 5, 20])
    {'raiz': 10, 'esquerda': {'raiz': 5, 'esquerda': {}, 'direita': {}}, 'direita': {'raiz': 20, 'esquerda': {}, 'direita': {}}}

def cria_simples(lista):
    arvore = {}
    for e in lista:
        insere(arvore, e)
    return arvore
'''


def cria_simples(lista):   # nao mexa aqui. Ela ja esta pronta
    arvore = {}
    for e in lista:
        insere(arvore, e)
    return arvore
    # so estou te lembrando como ela eh pra voce poder usar: ela comeca
    # de uma arvore vazia e vai inserindo um numero da lista por vez


assert cria_simples([10, 5, 2, 7, 20, 12, 30]) == arvore10, 'cria_simples com os numeros do desenho deveria dar a arvore do desenho'
print('Exercicio cria_simples: OK')


# ===== FASE 6 - A arvore inteira =====

'''
EXERCICIO

Agora, faca uma funcao que recebe uma arvore e diz quantos elementos ela
tem.

Acho q recursao pode ser util aqui. A gente nao viu isso ainda, mas vou
te apresentar agora.

    >>> conta({'raiz': 5, 'esquerda': {'raiz': 2, 'esquerda': {}, 'direita': {}}, 'direita': {}})
    2
    >>> conta({})
    0
'''
def conta(arvore):
    if arvore == {}:
        return 0
    return 1 + conta(arvore['direita']) + conta(arvore['esquerda'])


print('  iniciando testes de conta')
assert conta(arvore10) == 7, f'conta(arvore10) deveria ser 7, voce retornou {conta(arvore10)}'
assert conta(arvore5) == 3, f'conta(arvore5) deveria ser 3, voce retornou {conta(arvore5)}'
assert conta(arvore2) == 1, f'conta(arvore2) deveria ser 1, voce retornou {conta(arvore2)}'
assert conta({}) == 0, f'conta de uma arvore vazia deveria ser 0, voce retornou {conta({})}'
assert conta(ex3) == 5, f'conta(ex3) deveria ser 5, voce retornou {conta(ex3)}'
assert conta(ex4) == 9, f'conta(ex4) deveria ser 9, voce retornou {conta(ex4)}'
assert conta(arv_torta) == 4, f'conta(arv_torta) deveria ser 4, voce retornou {conta(arv_torta)}'
print('Exercicio conta: OK')

'''
EXERCICIO

Agora, vamos fazer uma funcao para calcular a soma de todos os numeros
presentes em uma arvore. Acho que recursao pode ser util aqui.

    >>> soma({'raiz': 5, 'esquerda': {'raiz': 2, 'esquerda': {}, 'direita': {}}, 'direita': {}})
    7
    >>> soma({})
    0
'''
def soma(arvore): 
    if arvore == {}:
        return 0
    soma_direita  = soma(arvore['direita']) #chama denovo a funcao soma para a arvore da direita
    soma_esquerda = soma(arvore['esquerda'])
    return arvore['raiz'] + soma_esquerda + soma_direita


print('  iniciando testes de soma')
assert soma(ex1) == 71, f'soma(ex1) deveria ser 71, voce retornou {soma(ex1)}'
assert soma(ex2) == 15, f'soma(ex2) deveria ser 15, voce retornou {soma(ex2)}'
assert soma(ex3) == 335, f'soma(ex3) deveria ser 335, voce retornou {soma(ex3)}'
assert soma({}) == 0, f'soma de uma arvore vazia deveria ser 0, voce retornou {soma({})}'
assert soma(ex4) == 4669, f'soma(ex4) deveria ser 4669, voce retornou {soma(ex4)}'
assert soma(arvore2) == 2, f'soma(arvore2) deveria ser 2, voce retornou {soma(arvore2)}'
print('Exercicio soma: OK')

r'''
EXERCICIO

Agora, facamos uma funcao que retorna o maior numero presente na arvore.

Voce nao precisa usar recursao (e se usar, seu algoritmo vai funcionar,
mas talvez fique lento).

Dica: pense em que lugar da arvore o maior numero de todos tem que estar.

    >>> maior({'raiz': 5, 'esquerda': {'raiz': 2, 'esquerda': {}, 'direita': {}}, 'direita': {'raiz': 7, 'esquerda': {}, 'direita': {}}})
    7
'''
def maior(arvore):
    return 12

print('  iniciando testes de maior')
print('  (Se travar aqui, voce tem um loop infinito - rode no pythontutor para ver o que esta acontecendo.)')
assert maior(ex1) == 20, f'maior(ex1) deveria ser 20, voce retornou {maior(ex1)}'
assert maior(ex2) == 10, f'maior(ex2) deveria ser 10 - o 10 eh a propria raiz, e ela nao tem nada a direita, voce retornou {maior(ex2)}'
assert maior(ex3) == 120, f'maior(ex3) deveria ser 120, voce retornou {maior(ex3)}'
assert maior(ex4) == 2000, f'maior(ex4) deveria ser 2000, voce retornou {maior(ex4)}'
assert maior(arvore2) == 2, f'maior(arvore2) deveria ser 2 - a arvore so tem o 2, voce retornou {maior(arvore2)}'
assert maior(arv_torta) == 12, f'maior(arv_torta) deveria ser 12 - a raiz, que nao tem nada a direita, voce retornou {maior(arv_torta)}'
print('Exercicio maior: OK')


print('\n=== PARABENS! Todos os exercicios completos! ===')
