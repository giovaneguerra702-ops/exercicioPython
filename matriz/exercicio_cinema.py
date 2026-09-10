# Exercicio - matrizes, aula 1: a bilheteria do cinema (A MATRIZ, E A FAIXA
# DE POLTRONAS JUNTAS).

'''
ENUNCIADO

Faca o miolo de uma BILHETERIA DE CINEMA.

A sala eh um retangulo de poltronas: varias filas, e a mesma quantidade
de poltronas em cada fila. Uma poltrona esta livre ('_') ou ocupada ('X').
Quem chega quer sentar JUNTO - de nada adianta a sala ter dez lugares
livres se eles estao todos espalhados.

Por um menu, o usuario pode:

  1) ver A SALA desenhada;
  2) procurar N LUGARES JUNTOS;
  3) ver QUANTOS LUGARES LIVRES a sala tem;
  4) ver QUAL A FILA MAIS VAZIA;
  5) RESERVAR n poltronas a partir de uma poltrona;
  6) SAIR.

Regras:

  - a fila e a poltrona comecam a contar do ZERO;
  - so da pra reservar poltrona que existe e que esta livre;
  - a procura vai da PRIMEIRA fila pra ultima, e da ESQUERDA pra direita:
    devolve o primeiro lugar que serve, nao o melhor.

O menu ja esta pronto la embaixo. O que falta sao as sete funcoes.
'''

'''
EXPLICACAO

A sala eh uma MATRIZ: uma lista cujos elementos sao listas.

    sala = [['_', 'X', '_'],      # fila 0
            ['X', 'X', '_']]      # fila 1

A lista de fora tem as FILAS. Cada fila eh uma lista de poltronas. Entao
sao dois colchetes pra chegar numa poltrona:

    sala[1]        ->  ['X', 'X', '_']    a fila 1 inteira (uma lista comum)
    sala[1][0]     ->  'X'           a poltrona 0 da fila 1

PRIMEIRO a fila, DEPOIS a poltrona. Sempre nessa ordem.
Na linguagem de matrizes, diriamos que essa matriz tem 2 linhas e 3 colunas
E o acesso é primeiro dizer a linha, depois a coluna

E sao dois tamanhos diferentes:

    len(sala)          ->  2   quantas FILAS a sala tem (quantas linhas a matriz tem)
    len(sala[1])       ->  3   quantas POLTRONAS a fila 1 tem (quantas colunas a matriz tem)

Escreva `len(sala[fila])` quando quiser o tamanho de uma fila, e nao
`len(sala[0])`. Nesta sala todas as filas tem o mesmo tamanho, entao os
dois dao o mesmo numero - mas o habito de perguntar A CADA FILA eh o que
salva no dia em que elas forem diferentes.

Pra varrer a sala inteira, um laco DENTRO do outro: o de fora anda nas
filas, o de dentro anda nas poltronas daquela fila.

    for fila in range(len(sala)):
        for poltrona in range(len(sala[fila])):
            ...   sala[fila][poltrona] eh a poltrona da vez
'''


# A sessao das 19h de "O Auto da Compadecida". A Mirtes e o Cicero acabaram
# de chegar na fila da bilheteria, e querem dois lugares juntos.

sala_exemplo = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],   # fila 0 - lotada
    ['_', 'X', '_', 'X', '_', 'X', '_', 'X'],   # fila 1 - 4 livres, nenhuma junto da outra
    ['X', 'X', '_', '_', 'X', 'X', 'X', '_'],   # fila 2 - 3 livres, no maximo 2 juntas
    ['X', '_', '_', '_', 'X', 'X', '_', 'X'],   # fila 3 - as poltronas 1, 2 e 3 sao 3 JUNTAS
    ['_', '_', '_', '_', '_', '_', '_', '_'],   # fila 4 - ninguem sentou ainda
]

breakpoint_aqui = 42

# PARE
# Experimente acessar essa matriz, via pythontutor ou via o REPL do vscode
# (ponha um breakpoint na linha `breakpoint_aqui = 42` acima, rode com
# 'debug python file', use o debug console)
# digite coisas como print(sala_exemplo), print(sala_exemplo[1]),
# print(sala_exemplo[1][0])
# Depois tente usar a matriz pra revelar valores como '_', 8 (quantas
# poltronas tem a fila 2?), 5 (quantas filas tem a sala?) e a fila 4 inteira.
# Repare no que acontece se voce trocar a ordem: sala_exemplo[7][1] da erro,
# mas sala_exemplo[1][3] e sala_exemplo[3][1] NAO dao - devolvem poltronas
# diferentes, e em silencio.
# Depois, no olho: a Mirtes e o Cicero querem DOIS lugares juntos. Em quais
# filas eles cabem? E se chegassem em quatro? Repare que a fila 1 tem quatro
# poltronas livres e mesmo assim nao serve nem pra dois - eh exatamente essa
# diferenca que as funcoes de baixo vao calcular.
# Se nao conseguir, me chame


'''
EXERCICIO

Faca uma funcao desenha_sala(sala) que devolve o desenho da sala como UMA
string, com um '\n' (quebra de linha) no fim de CADA fila.

Eh o laco dentro do laco: o de fora anda nas filas, o de dentro anda nas
poltronas. A quebra de linha entra quando a fila acabou - ou seja, no fim
do laco de dentro, e nao dentro dele.

    >>> desenha_sala([['_', 'X'], ['X', 'X']])
    '_X\nXX\n'
'''
def desenha_sala(sala):
    desenho = ''
    for linha in sala:
        for posicao in linha: #esse faz 2 vezes, uma pra cada poltrona da fila
            desenho = desenho + posicao
        desenho = desenho + '\n'
    return desenho


assert desenha_sala([['_', 'X'], ['X', 'X']]) == '_X\nXX\n', f'duas filas viram duas linhas, cada uma terminada em \\n; voce devolveu {desenha_sala([["_", "X"], ["X", "X"]])!r}'
assert desenha_sala([['_']]) == '_\n', f'uma fila de uma poltrona; voce devolveu {desenha_sala([["_"]])!r}'

# A sessao das 19h inteira. Relembrando a matriz, e o desenho que sai dela:
#
#     ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']   ->   XXXXXXXX
#     ['_', 'X', '_', 'X', '_', 'X', '_', 'X']   ->   _X_X_X_X
#     ['X', 'X', '_', '_', 'X', 'X', 'X', '_']   ->   XX__XXX_
#     ['X', '_', '_', '_', 'X', 'X', '_', 'X']   ->   X___XX_X
#     ['_', '_', '_', '_', '_', '_', '_', '_']   ->   ________
#
# Eh UMA string so, com um '\n' no fim de CADA fila - inclusive da ultima.
# Escrita em varias linhas aqui embaixo pra dar pra ler o desenho; o Python
# cola os pedacos numa string so.
desenho_esperado_t = (
    'XXXXXXXX\n'
    '_X_X_X_X\n'
    'XX__XXX_\n'
    'X___XX_X\n'
    '________\n'
)

assert desenha_sala(sala_exemplo) == desenho_esperado_t, f'a sessao das 19h inteira; voce devolveu {desenha_sala(sala_exemplo)!r}'
print('Exercicio 1 (desenha_sala): OK')


'''
EXERCICIO

Faca uma funcao lugares_livres(sala) que devolve quantas poltronas livres
('_') a sala INTEIRA tem.

Mesma varredura do desenho - so que em vez de escrever a poltrona, voce
conta ela.

    >>> lugares_livres([['_', 'X'], ['_', '_']])
    3
'''
def lugares_livres(sala):
    contador = 0
    for fila in sala:
        for posicao in fila:
            if posicao == '_':
                contador += 1
    return contador

    

assert lugares_livres([['_', 'X'], ['_', '_']]) == 3, f'tres poltronas livres nessa salinha; voce devolveu {lugares_livres([["_", "X"], ["_", "_"]])}'
assert lugares_livres([['X', 'X']]) == 0, f'sala lotada tem zero livres; voce devolveu {lugares_livres([["X", "X"]])}'
assert lugares_livres(sala_exemplo) == 19, f'a sessao das 19h tem 19 poltronas livres; voce devolveu {lugares_livres(sala_exemplo)}'
print('Exercicio 2 (lugares_livres): OK')


'''
EXERCICIO

Faca uma funcao livres_na_fila(sala, fila) que devolve quantas poltronas
livres UMA fila tem.

Agora eh um laco so: a fila ja veio escolhida por parametro, e sobra andar
pelas poltronas dela. Repare que `sala[fila]` eh uma lista comum - a lista
daquela fila.

    >>> livres_na_fila([['_', 'X'], ['_', '_']], 1)
    2
'''
def livres_na_fila(sala, fila):
    contador = 0
    for assento in sala[fila]:
        if assento == '_':
            contador += 1
    return contador


assert livres_na_fila([['_', 'X'], ['_', '_']], 1) == 2, f'a fila 1 dessa salinha tem duas livres; voce devolveu {livres_na_fila([["_", "X"], ["_", "_"]], 1)}'
assert livres_na_fila(sala_exemplo, 0) == 0, f'a fila 0 esta lotada; voce devolveu {livres_na_fila(sala_exemplo, 0)}'
assert livres_na_fila(sala_exemplo, 1) == 4, f'a fila 1 tem 4 livres; voce devolveu {livres_na_fila(sala_exemplo, 1)}'
assert livres_na_fila(sala_exemplo, 4) == 8, f'a fila 4 esta inteira livre; voce devolveu {livres_na_fila(sala_exemplo, 4)}'
print('Exercicio 3 (livres_na_fila): OK')


'''
EXERCICIO

Faca uma funcao fila_mais_vazia(sala) que devolve o NUMERO da fila com
mais poltronas livres.

Dica: voce nao precisa de laco aninhado aqui. O laco de dentro ja esta
pronto, dentro de `livres_na_fila` - chame ela. Uma funcao que ja funciona
vira o miolo da proxima.

    >>> fila_mais_vazia([['_', 'X'], ['_', '_']])
    1
'''
def fila_mais_vazia(sala):
    for i in range(len(sala)):
        pass


assert fila_mais_vazia([['_', 'X'], ['_', '_']]) == 1, f'a fila 1 tem mais livres; voce devolveu {fila_mais_vazia([["_", "X"], ["_", "_"]])}'
assert fila_mais_vazia([['_', '_'], ['X', 'X']]) == 0, f'quando a melhor eh a primeira, a resposta eh 0; voce devolveu {fila_mais_vazia([["_", "_"], ["X", "X"]])}'
assert fila_mais_vazia(sala_exemplo) == 4, f'a fila 4 eh a mais vazia da sessao; voce devolveu {fila_mais_vazia(sala_exemplo)}'
print('Exercicio 4 (fila_mais_vazia): OK')


'''
EXPLICACAO

Chegou a parte mais util

Contar quantas poltronas estao livres eh uma pergunta. A pergunta de quem
chega com a familia eh OUTRA: elas estao JUNTAS?

Olhe a fila 1 da sessao:

    ['_', 'X', '_', 'X', '_', 'X', '_', 'X']

Sao quatro poltronas livres, e a fila nao serve nem pra duas pessoas
sentarem lado a lado. "Quantas livres" e "quantas juntas" sao contas
diferentes, e a segunda eh a que vende ingresso.

A conta das juntas eh um contador que ANDA e ZERA:

    - poltrona livre  ->  o contador cresce 1;
    - poltrona ocupada ->  o contador VOLTA A ZERO, porque a faixa quebrou.

Quando o contador chega em `n`, achou. So que ele chega em `n` na ULTIMA
poltrona da faixa - e a pergunta eh onde ela COMECOU. Se a faixa tem `n`
poltronas e termina na poltrona `p`, ela comecou em `p - n + 1`:

    ['X', '_', '_', '_', 'X']
            1    2    3          <- o contador
                      ^          o contador chegou a 3 na poltrona 3
                 ^               e a faixa comecou na poltrona 3 - 3 + 1 = 1
'''

'''
EXERCICIO

Faca uma funcao onde_comeca_n_juntos(sala, fila, n) que devolve em que
poltrona comeca a PRIMEIRA faixa de `n` poltronas livres SEGUIDAS naquela
fila. Devolve -1 quando nao existe faixa nenhuma desse tamanho.

    >>> onde_comeca_n_juntos([['X', '_', '_']], 0, 2)
    1
'''
def onde_comeca_n_juntos(sala, fila, n):
    pass


assert onde_comeca_n_juntos([['X', '_', '_']], 0, 2) == 1, f'as duas juntas comecam na poltrona 1; voce devolveu {onde_comeca_n_juntos([["X", "_", "_"]], 0, 2)}'
assert onde_comeca_n_juntos([['_', '_', 'X']], 0, 2) == 0, f'quando a faixa comeca na primeira poltrona, a resposta eh 0; voce devolveu {onde_comeca_n_juntos([["_", "_", "X"]], 0, 2)}'
assert onde_comeca_n_juntos(sala_exemplo, 3, 3) == 1, f'na fila 3 as tres juntas comecam na poltrona 1; voce devolveu {onde_comeca_n_juntos(sala_exemplo, 3, 3)}'
assert onde_comeca_n_juntos(sala_exemplo, 3, 4) == -1, f'quatro juntas nao cabem na fila 3; voce devolveu {onde_comeca_n_juntos(sala_exemplo, 3, 4)}'
assert onde_comeca_n_juntos(sala_exemplo, 0, 1) == -1, f'na fila 0, que esta lotada, nao cabe nem uma; voce devolveu {onde_comeca_n_juntos(sala_exemplo, 0, 1)}'
assert onde_comeca_n_juntos(sala_exemplo, 4, 8) == 0, f'a fila 4 inteira sao 8 juntas comecando na poltrona 0; voce devolveu {onde_comeca_n_juntos(sala_exemplo, 4, 8)}'
# o par que separa esta funcao da de cima: a fila 1 tem 4 livres...
assert livres_na_fila(sala_exemplo, 1) == 4, 'a fila 1 tem quatro poltronas livres'
# ...e nao tem nem DUAS juntas
assert onde_comeca_n_juntos(sala_exemplo, 1, 2) == -1, f'na fila 1 nem duas estao juntas - se voce devolveu outra coisa, esta contando as livres em vez das SEGUIDAS; voce devolveu {onde_comeca_n_juntos(sala_exemplo, 1, 2)}'
print('Exercicio 5 (onde_comeca_n_juntos): OK')


'''
EXERCICIO

Faca uma funcao onde_sentar(sala, n) que devolve onde uma turma de `n`
pessoas consegue sentar junta: a tupla (fila, primeira poltrona). Devolve
None quando nao ha lugar em fila nenhuma.

Varra as filas da PRIMEIRA pra ultima e devolva a primeira que serve - nao
a melhor da sala. Use a funcao do exercicio anterior.

    >>> onde_sentar([['X', 'X'], ['_', '_']], 2)
    (1, 0)
'''
def onde_sentar(sala, n):
    pass


assert onde_sentar([['X', 'X'], ['_', '_']], 2) == (1, 0), f'a fila 0 nao serve, a fila 1 serve a partir da poltrona 0; voce devolveu {onde_sentar([["X", "X"], ["_", "_"]], 2)}'
assert onde_sentar(sala_exemplo, 2) == (2, 2), f'o primeiro par junto da sessao esta na fila 2, poltrona 2; voce devolveu {onde_sentar(sala_exemplo, 2)}'
assert onde_sentar(sala_exemplo, 3) == (3, 1), f'para tres pessoas, a primeira fila que serve eh a 3; voce devolveu {onde_sentar(sala_exemplo, 3)}'
assert onde_sentar(sala_exemplo, 4) == (4, 0), f'para quatro, so a fila 4; voce devolveu {onde_sentar(sala_exemplo, 4)}'
assert onde_sentar(sala_exemplo, 9) is None, f'ninguem senta nove junto numa fila de oito - devolva None; voce devolveu {onde_sentar(sala_exemplo, 9)}'
print('Exercicio 6 (onde_sentar): OK')


'''
EXPLICACAO

A ultima funcao MUDA a sala, e por isso ela nao devolve nada.

Lista eh MUTAVEL: quando voce escreve `sala[fila][poltrona] = 'X'` dentro
da funcao, quem chamou ve a mudanca - eh a mesma sala, nao uma copia. Eh
por isso que o menu consegue reservar e depois desenhar a sala de novo com
a poltrona ja ocupada.
'''

'''
EXERCICIO

Faca uma funcao reserva(sala, fila, poltrona, quantas) que ocupa `quantas`
poltronas seguidas, a partir de (fila, poltrona).

Ela NAO devolve nada - escreve direto na sala que recebeu.

    >>> s = [['_', '_', '_']]
    >>> reserva(s, 0, 1, 2)
    >>> s
    [['_', 'X', 'X']]
'''
def reserva(sala, fila, poltrona, quantas):
    pass


sala_t = [['_', '_', '_'], ['X', '_', 'X']]
reserva(sala_t, 0, 1, 2)
assert sala_t == [['_', 'X', 'X'], ['X', '_', 'X']], f'as poltronas 1 e 2 da fila 0 viram X, e a fila 1 nao eh tocada; ficou {sala_t}'
assert lugares_livres(sala_t) == 2, f'sobraram duas livres; voce deixou {lugares_livres(sala_t)}'
reserva(sala_t, 1, 1, 1)
assert sala_t == [['_', 'X', 'X'], ['X', 'X', 'X']], f'reservar uma so tambem tem que funcionar; ficou {sala_t}'
print('Exercicio 7 (reserva): OK')


print('\n=== PARABENS! Todos os exercicios completos! ===')


# ===== O menu (ja esta pronto) =====

def main():
    sala = sala_exemplo    # a bilheteria comeca com a sessao das 19h

    while True:
        print()
        print('=== BILHETERIA - O AUTO DA COMPADECIDA, 19h ===')
        print(f'{lugares_livres(sala)} lugares livres | fila mais vazia: {fila_mais_vazia(sala)}')
        print('1. Ver a sala')
        print('2. Procurar N lugares juntos')
        print('3. Quantos lugares livres')
        print('4. Qual a fila mais vazia')
        print('5. Reservar')
        print('6. Sair')
        opcao = input('Opcao: ')

        if opcao == '1':
            print('   poltrona: 01234567')
            print(desenha_sala(sala), end='')

        elif opcao == '2':
            n = int(input('  quantas pessoas: '))
            lugar = onde_sentar(sala, n)
            if lugar is None:
                print(f'  nao ha {n} lugares juntos em fila nenhuma')
            else:
                print(f'  fila {lugar[0]}, a partir da poltrona {lugar[1]}')

        elif opcao == '3':
            print(f'  livres: {lugares_livres(sala)} de {len(sala) * len(sala[0])}')

        elif opcao == '4':
            fila = fila_mais_vazia(sala)
            print(f'  a fila {fila}, com {livres_na_fila(sala, fila)} livres')

        elif opcao == '5':
            fila = int(input('  fila: '))
            poltrona = int(input('  primeira poltrona: '))
            quantas = int(input('  quantas: '))
            if fila < 0 or fila >= len(sala):
                print('  essa fila nao existe')
            elif quantas < 1 or poltrona < 0 or poltrona + quantas > len(sala[fila]):
                print('  essas poltronas nao cabem na fila')
            else:
                # confere as poltronas PEDIDAS, uma a uma - nao adianta a fila
                # ter n juntas em outro lugar
                todas_livres = True
                for i in range(quantas):
                    if sala[fila][poltrona + i] == 'X':
                        todas_livres = False
                if not todas_livres:
                    print('  alguma dessas poltronas ja esta ocupada')
                else:
                    reserva(sala, fila, poltrona, quantas)
                    print(f'  reservado: fila {fila}, poltronas {poltrona} a {poltrona + quantas - 1}')

        elif opcao == '6':
            break

        else:
            print('Opcao invalida')


# Pra rodar a bilheteria, descomente:
# main()
