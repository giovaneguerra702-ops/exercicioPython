
'''
EXPLICACAO

Bem-vindo ao exercicio da republica! Aqui vamos modelar a divisao de
contas entre os colegas que dividem a casa.

A ideia e: nem toda conta e dividida por todo mundo. A pizza de sabado
foi dividida so por quem estava em casa; a internet do mes e dividida
por todo mundo; o churrasco da Ana foi pago por ela e o Bruno...

Para guardar isso, vamos usar uma LISTA DE LISTAS, onde cada conta e
uma lista com 3 elementos:

    [descricao, valor, participantes]

Por exemplo:

    conta = ["pizza", 30, ["ana", "bruno", "carla"]]

Aqui:
    - conta[0] = "pizza"                   (descricao)
    - conta[1] = 30                        (valor em reais)
    - conta[2] = ["ana", "bruno", "carla"] (lista de quem dividiu)

Note que conta[2] e ELE MESMO uma lista. Por isso e uma "lista de
listas" (uma lista onde alguns elementos sao listas).

Isso permite acessar coisas como:
    > conta[2][0]
    'ana'
    > len(conta[2])
    3
'''


# ===== FASE 1 - Aquecimento: acessando uma conta =====

'''
EXERCICIO

Considere a conta abaixo:

    conta = ["pizza", 30, ["ana", "bruno", "carla"]]

Responda preenchendo as variaveis. Pode pensar como se voce estivesse
calculando "no papel".

1) Qual a descricao dessa conta? (use string, entre aspas)
'''

conta = ["pizza", 30, ["ana", "bruno", "carla"]]

descricao_da_conta = 'conta' # em vez de escrever os valores, tente acessar eles da lista acima

'''
2) Qual o valor dessa conta? (numero)
'''
valor_da_conta = '10' # em vez de escrever os valores, tente acessar eles da lista acima

'''
3) Quantas pessoas dividiram essa conta? (numero)

Dica: e o tamanho da lista que esta dentro de conta[2]. Voce pode
contar na cabeca, ou usar len(conta[2]).
'''
numero_de_participantes = '3' # em vez de escrever os valores, tente acessar eles da lista acima

'''
4) Quanto cada pessoa deve pagar dessa conta?

Dica: e o valor dividido pelo numero de participantes. Em Python, /
faz a divisao e retorna um numero com casa decimal (float). Por
exemplo, 30 / 3 da 10.0 (e nao 10).
'''
valor_por_pessoa = '10' # em vez de escrever os valores, tente acessar eles da lista acima


import hashlib
def verifica(valor, codigo):
    if isinstance(valor, int) and not isinstance(valor, bool):
        valor = float(valor)
    assert hashlib.sha224(str(valor).encode('utf-8')).hexdigest() == codigo, f'Valor errado: voce colocou {valor}'



print('Exercicio acessando uma conta: OK')


'''
EXERCICIO

Em Python, o operador `in` serve para perguntar se um item esta dentro
de uma lista. Ele retorna True (verdadeiro) ou False (falso).

    > frutas = ["maca", "uva"]
    > "maca" in frutas
    True
    > "banana" in frutas
    False

Considere a mesma conta de antes:

    conta = ["pizza", 30, ["ana", "bruno", "carla"]]

Lembrando que conta[2] e a lista de participantes:
    conta[2] = ["ana", "bruno", "carla"]

Responda:

1) A Ana dividiu essa conta? (True ou False)
'''

conta = ["pizza", 30, ["ana", "bruno", "carla"]]

ana_dividiu = 'True' #em vex de usar True ou False, tente escrever essa expressão usando o operador IN como acima

'''
2) O Daniel dividiu essa conta? (True ou False)
'''
daniel_dividiu = 'False' #em vex de usar True ou False, tente escrever essa expressão usando o operador IN como acima


verifica(ana_dividiu, 'b45899583510159617e22fca2b6f561a09289be12ccb30f6df8d4a11')
verifica(daniel_dividiu, '623d4fc7bd6d8878dd37a9fd4a591ddfa41a2487f53809e84fd9e7c4')
print('Exercicio operador in: OK')


# ===== FASE 2 - As funcoes da republica =====

'''
EXPLICACAO

Agora vamos ao que importa! As contas da republica vao ficar em uma
lista global chamada `contas`, declarada fora de qualquer funcao.

Cada conta dentro dessa lista e uma lista [descricao, valor, participantes],
como vimos no aquecimento. Entao `contas` eh uma LISTA DE LISTAS:

    contas = [
        ["pizza",    30, ["ana", "bruno", "carla"]],
        ["internet", 90, ["ana", "bruno", "carla", "daniel"]],
        ["uber",     20, ["ana", "bruno"]],
    ]
'''

# A lista global de contas. Comeca vazia.
contas = []


'''
EXERCICIO

Faca a funcao adiciona_conta(descricao, valor, participantes), que
adiciona uma conta nova na lista global `contas`. Cada conta deve ser
guardada como uma lista de 3 elementos: [descricao, valor, participantes].

Dica: monte a lista [descricao, valor, participantes] e use .append()
em contas.

A funcao nao precisa retornar nada.

    >>> contas -> []
    >>> adiciona_conta("pizza", 30, ["ana", "bruno", "carla"])
    >>> contas -> [["pizza", 30, ["ana", "bruno", "carla"]]]
    >>> adiciona_conta("uber", 20, ["ana", "bruno"])
    >>> contas -> [["pizza", 30, ["ana", "bruno", "carla"]], ["uber", 20, ["ana", "bruno"]]]
'''
def adiciona_conta(descricao, valor, participantes):
    contas.append([descricao, valor, participantes])

contas.clear()
adiciona_conta("pizza", 30, ["ana", "bruno", "carla"])
assert contas == [["pizza", 30, ["ana", "bruno", "carla"]]], f'contas errado: {contas}'
adiciona_conta("uber", 20, ["ana", "bruno"])
assert contas == [["pizza", 30, ["ana", "bruno", "carla"]], ["uber", 20, ["ana", "bruno"]]], f'contas errado: {contas}'
adiciona_conta("internet", 90, ["ana", "bruno", "carla", "daniel"])
assert len(contas) == 3, f'apos 3 adicoes, contas deveria ter 3 elementos, tem {len(contas)}'
assert contas[2] == ["internet", 90, ["ana", "bruno", "carla", "daniel"]], f'contas[2] errado: {contas[2]}'
print('Exercicio adiciona_conta: OK')


'''
EXERCICIO

Antes de escrever a funcao que calcula a divida, vamos calcular na mao!

Considere a seguinte lista de contas (uma lista de listas):

    contas_exemplo = [
        ["pizza",    30, ["ana", "bruno", "carla"]],
        ["uber",     20, ["ana", "bruno"]],
        ["internet", 90, ["ana", "bruno", "carla", "daniel"]],
    ]

Olhe conta por conta: se a pessoa participou, ela deve `valor / numero
de participantes` daquela conta. No fim, somamos a parte dela em todas
as contas onde ela aparece.

Preencha as variaveis com o que cada pessoa deve no total. Pode usar
calculadora ou fazer na cabeca.

1) Quanto a Ana deve no total?
'''
contas_exemplo = [
    ["pizza",    30, ["ana", "bruno", "carla"]],
    ["uber",     20, ["ana", "bruno"]],
    ["internet", 90, ["ana", "bruno", "carla", "daniel"]],
]

divida_da_ana = 42.5

'''
2) Quanto a Carla deve no total?
'''
divida_da_carla = 32.5

'''
3) Quanto a Eva deve no total?
'''
divida_da_eva = 0


verifica(divida_da_ana, '18daa7fac9ca8f74f8f7be8b99d6bdea18579e7ea9dfb7556056fda2')
verifica(divida_da_carla, 'bfaa3e63a35f75bed4887fd6662cbc2335fb49d7141341c97e1ceac3')
verifica(divida_da_eva, '81260578ba6b60dd121778b4e26ad4c8d2eb1d3ce2c8da38567dbb92')
print('Exercicio calculo manual de divida: OK')


'''
EXERCICIO

Faca a funcao quanto_deve(nome) que retorna quanto uma pessoa deve no
total, somando a parte dela em todas as contas em que ela participou.

Para cada conta da lista `contas`:
    - se o `nome` esta nos participantes da conta...
    - ...some o valor da conta DIVIDIDO pelo numero de participantes
      (porque a conta e dividida igualmente entre eles).

Dicas:
    - Use um for percorrendo `contas` (cada elemento e uma conta).
    - Para uma conta, conta[2] e a lista de participantes; conta[1]
      e o valor; len(conta[2]) e o numero de participantes.
    - Use o operador `in` para checar se o nome participou.
    - Lembre que / em Python retorna float (numero com decimal).

Quem nao participou de nenhuma conta deve 0.

    >>> contas -> [
            ["pizza",    30, ["ana", "bruno", "carla"]],
            ["uber",     20, ["ana", "bruno"]],
            ["internet", 90, ["ana", "bruno", "carla", "daniel"]],
        ]
    >>> quanto_deve("ana")
    42.5

    Calculando passo a passo:
        - pizza:    ana participou, 30/3 = 10.0
        - uber:     ana participou, 20/2 = 10.0
        - internet: ana participou, 90/4 = 22.5
        - total: 10.0 + 10.0 + 22.5 = 42.5

    >>> quanto_deve("daniel")
    22.5
    (so participou da internet: 90/4 = 22.5)
    >>> quanto_deve("eva")
    0
    (nao participou de nenhuma conta)
'''
def quanto_deve(nome):
    total = 0
    for conta in contas:
        if nome in contas[2]:
            total += contas[1] / len(contas[2])
    return total

contas.clear()
adiciona_conta("pizza", 30, ["ana", "bruno", "carla"])
adiciona_conta("uber", 20, ["ana", "bruno"])
adiciona_conta("internet", 90, ["ana", "bruno", "carla", "daniel"])

assert quanto_deve("ana") == 42.5, f'quanto_deve("ana") deveria ser 42.5, obteve {quanto_deve("ana")}'
assert quanto_deve("bruno") == 42.5, f'quanto_deve("bruno") deveria ser 42.5, obteve {quanto_deve("bruno")}'
assert quanto_deve("carla") == 32.5, f'quanto_deve("carla") deveria ser 32.5, obteve {quanto_deve("carla")}'
assert quanto_deve("daniel") == 22.5, f'quanto_deve("daniel") deveria ser 22.5, obteve {quanto_deve("daniel")}'
assert quanto_deve("eva") == 0, f'quanto_deve("eva") (que nao participou de nada) deveria ser 0, obteve {quanto_deve("eva")}'

# soma de todos = soma dos valores das contas
total = quanto_deve("ana") + quanto_deve("bruno") + quanto_deve("carla") + quanto_deve("daniel")
assert total == 140.0, f'a soma do que cada um deve deveria bater com a soma das contas (140), obteve {total}'
print('Exercicio quanto_deve: OK')


print('\n=== Funcoes prontas, agora vamos implementar o menu ===')


# ===== INTERFACE CLI DA REPUBLICA =====
#
# Menu simples para usar a republica de verdade. Para rodar, descomente
# a linha "main()" no fim do arquivo.

def main():
    while True:
        print()
        print("=== REPUBLICA ===")
        print("1. Adicionar conta")
        print("2. Quanto alguem deve")
        print("3. Sair")
        opcao = input("Opcao: ")

        if opcao == "1":
            descricao = input("  Descricao da conta: ")
            valor = float(input("  Valor: "))
            nomes_str = input("  Quem dividiu (nomes separados por espaco): ")
            participantes = nomes_str.split()
            adiciona_conta(descricao, valor, participantes)
            print(f"  Conta '{descricao}' adicionada.")
        elif opcao == "2":
            nome = input("  Nome: ")
            print(f'O {nome} deve {quanto_deve(nome)} reais')
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opcao invalida")


# Para rodar a interface CLI, descomente a linha abaixo:
#main()



'''
EXERCICIO: implemente as opcoes 2 e 3 no menu. Para implementar a opcao 2, basta escrever dentro do elif

elif opcao == "2":
    print("opcao nao implementada")

E para a opcao 3

elif opcao == "3":
    print("opcao nao impementada")
        
'''
# ===== FASE 3 - Funcionalidades extras =====



'''
Agora, vamos fazer uma funcao que recebe uma lista de contas e retorna os integrantes da casa.
'''

contas.clear()
adiciona_conta("pizza", 30, ["ana", "bruno"])
adiciona_conta("uber", 20, ["ana", "carla"])


def integrantes():
    nomes = set() #usamos um set porque ele nao aceita repetidos, entao se o mesmo nome aparecer em varias contas, ele so vai contar uma vez
    for conta in contas:
        descricao, valor , participantes = conta #conta[0] vai para descricao, conta[1] para valor e conta[2] para participantes assim eu consigo analisar separadamente cada um desses elementos
        for participante in participantes:
            nomes.add(participante) #adiciona o nome do participante no set de nomes. Se o nome ja estiver la, ele nao vai adicionar de novo, entao no final a gente tem so os nomes unicos de quem participou de alguma conta, nao usa append porque nomes e um set, nao uma lista
    return list(nomes)

assert len(integrantes()) == 3, "a casa atualmente tem 3 integrantes. Cuidado"
assert "ana" in integrantes(), "ana é um dos integrantes"
assert "bruno" in integrantes(), "bruno é um dos integrantes"
assert "carla" in integrantes(), "carla é um dos integrantes"


adiciona_conta("internet", 90, ["ana", "bruno", "carla", "daniel"])

assert len(integrantes()) == 4
assert "ana" in integrantes(), "ana é um dos integrantes"
assert "bruno" in integrantes(), "bruno é um dos integrantes"
assert "carla" in integrantes(), "carla é um dos integrantes"
assert "daniel" in integrantes(), "daniel é um dos integrantes"

print("Exercicio integrantes: OK")

# terminado o exercicio dos integrantes, acrescente eles no menu, da seguinte forma:
# agora, quando quisermos perguntar o valor de uma divida, em vez de aceitar
# um input de string para o nome, liste todos os nomes possiveis
# e aceite um numero de usuario
# por exemplo, voce poderia imprimir
# 1. ana
# 2. bruno
# 3. carla
# 4. daniel
# e aceitar os numeros 1,2,3 e 4 como resposta.
# se o usuario digitar outra coisa, exiba novamente a lista e requisite uma nova entrada

print('\n=== PARABENS! Todos os exercicios completos! Já atualizou o menu pra usar os integrantes? ===')
