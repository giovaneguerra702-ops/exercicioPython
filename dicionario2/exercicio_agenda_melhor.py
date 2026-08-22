# Lista de exercicios - agenda_melhor (dicionario aninhado)
# Pre-requisito: Lista 1 (agenda). Agora cada valor da agenda eh ELE MESMO
# um dicionario, com 'email' e 'telefones' (uma lista). Aprender: acesso
# aninhado, iterar+filtrar, agregacao, e construir um dict por agregacao
# com loop ANINHADO (conta_ocorrencias).

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


# A funcao explicar() ajuda nas questoes de multipla escolha. Se voce travar
# numa questao, descomente a linha `explicar('nome')` logo abaixo dela para
# ler a discussao das alternativas.
def explicar(questao):
    try:
        from dicionario2.explicacao_agenda_melhor import EXPLICACOES
    except ImportError:
        print("Arquivo 'explicacao_agenda_melhor.py' nao foi encontrado.")
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


'''
EXPLICACAO

Esta eh a continuacao da agenda. Na Lista 1, cada pessoa apontava direto
para um telefone:

    agenda = {'marcos': 32112232}     # pessoa -> telefone

Agora a agenda fica mais rica: cada pessoa aponta para um DICIONARIO, com
um 'email' e uma lista de 'telefones':

    agenda = {
        'lucas': {'email': 'lucas@exemplo.com', 'telefones': [11999888999, 1177788899]},
        'maria': {'email': 'maria@exemplo.com', 'telefones': [84999777444]},
        'marta': {'telefones': [1177788899]},   # repare: a marta NAO tem email!
    }

Ou seja: o VALOR de cada chave eh ele mesmo um dicionario (um "dict dentro
de dict"). Pra chegar no email do lucas, voce desce DOIS niveis:

    agenda['lucas']            # o dict do lucas: {'email': ..., 'telefones': [...]}
    agenda['lucas']['email']   # o email: 'lucas@exemplo.com'

Como na Lista 1, as funcoes NAO acessam variaveis globais: a agenda entra
por parametro.
'''


# ===== FASE 1 - Aquecimento: lendo a agenda aninhada =====

'''
EXPLICACAO

O acesso aninhado eh feito em PASSOS, um colchete por nivel:

    agenda['lucas']                  # 1o passo: o dict interno do lucas
    agenda['lucas']['telefones']     # 2o passo: a lista de telefones dele
    agenda['lucas']['telefones'][0]  # 3o passo: o primeiro telefone

E pra perguntar se um campo existe (sem dar erro), use `in` nas CHAVES do
dict interno - o mesmo `.keys()` da Lista 1, so que um nivel abaixo:

    'email' in agenda['marta'].keys()    # False - a marta nao tem email
'''

agenda_exemplo = {
    'lucas': {'email': 'lucas@exemplo.com', 'telefones': [11999888999, 1177788899]},
    'maria': {'email': 'maria@exemplo.com', 'telefones': [84999777444]},
    'marta': {'telefones': [1177788899]},   # sem email!
}

breakpoint_aqui = 42

# PARE
# Experimente acessar esse dicionario, via pythontutor ou via o REPL
# do vscode (ponha um breakpoint na linha `breakpoint_aqui = 42` acima,
# rode com 'debug python file', use o debug console ou o menu watch)
# digite coisas como print(agenda_exemplo),
# print(agenda_exemplo['lucas'])
# Depois tente usar o dicionario para printar coisas como
# 'lucas@exemplo.com', [11999888999, 1177788899], 84999777444 e depois 1177788899
# -- ou seja, faca os acessos usando esse dicionario para revelar esses valores.
# Se nao conseguir, me chame
# Experimente tambem:
# agenda_exemplo['lucas']['email']
# (agenda_exemplo['lucas'])['email']


'''
EXERCICIO

Considere a agenda_exemplo.

agenda_exemplo = {
    'lucas': {'email': 'lucas@exemplo.com', 'telefones': [11999888999, 1177788899]},
    'maria': {'email': 'maria@exemplo.com', 'telefones': [84999777444]},
    'marta': {'telefones': [1177788899]},   # sem email!
}

Preencha as variaveis usando uma EXPRESSAO Python que produz o valor (em
vez do valor literal). Se nao conseguir, comece pelo valor, mas depois
tente a expressao.

1) Qual o email do lucas?                  Dica: acesse a chave lucas, depois a chave email
2) Qual o PRIMEIRO telefone do lucas?      Dica: ...['telefones'][0]
3) Quantos telefones o lucas tem?          Dica: len(...['telefones'])
4) A marta tem email?                      Dica: 'email' in dicionariozinho_da_marta.keys()
                                                 (o dicionariozinho da marta esta
                                                  dentro da agenda_exemplo)

'''
email_do_lucas     = agenda_exemplo['lucas']['email']
primeiro_tel_lucas = agenda_exemplo['lucas']['telefones'][0]
quantos_tels_lucas = len(agenda_exemplo['lucas']['telefones'])
marta_tem_email    = 'email' in agenda_exemplo['marta'].keys()

assert verifica(email_do_lucas, '333a6b17325de9a29dc9249035264e179504a8b171ba279922036a11'), 'email_do_lucas incorreta'
assert verifica(primeiro_tel_lucas, '835b2b8fcfbd5696b2cc502f73fc93e40d4c6644884d5662c196363d'), 'primeiro_tel_lucas incorreta'
assert verifica(quantos_tels_lucas, '7b13dee61edc12d320a7e9a0816e594ccfbf0c67247b9ae6698aa880', nome_questao='quantos_tels_lucas'), 'quantos_tels_lucas incorreta'
assert verifica(marta_tem_email, '623d4fc7bd6d8878dd37a9fd4a591ddfa41a2487f53809e84fd9e7c4'), 'marta_tem_email incorreta'
print('Exercicio lendo a agenda aninhada: OK')


'''
EXERCICIO

Tres questoes de multipla escolha sobre o "acesso em dois passos".
Se travar, descomente o `explicar(...)`.

Q1 - o_que_retorna_pessoa

A agenda_exemplo tem cada pessoa apontando para um dict com 'email' e
'telefones'. O que `agenda_exemplo['lucas']` retorna?

    a) o email do lucas
    b) um dicionario com 2 chaves
    c) um dicionario com 3 chaves
    d) o primeiro telefone
'''
o_que_retorna_pessoa = 'b'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('o_que_retorna_pessoa')

assert verifica(o_que_retorna_pessoa, 'd77db2f10cb948674f7f430bb6d5b32975d801874747506591af3911', nome_questao='o_que_retorna_pessoa'), 'o_que_retorna_pessoa incorreta'


'''
EXERCICIO

Q2 - parenteses

Os colchetes sao lidos da ESQUERDA para a DIREITA, um de cada vez. A que
`agenda_exemplo['lucas']['email']` equivale?

    a) (agenda_exemplo['lucas'])['email']
    b) agenda_exemplo(['lucas']['email'])
'''
parenteses = 'a'   # 'a' ou 'b'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('parenteses')

assert verifica(parenteses, 'aafeeb8677640d5e9a3a264d67f5adc847d82f487cc7b44c1a690bcb', nome_questao='parenteses'), 'parenteses incorreta'


'''
EXERCICIO

Q3 - posicao_no_dict

O que `agenda_exemplo[0]` faz?

    a) retorna o primeiro contato
    b) da KeyError - 0 nao eh chave da agenda
    c) retorna o lucas, que foi o primeiro adicionado
'''
posicao_no_dict = 'b'   # 'a', 'b' ou 'c'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('posicao_no_dict')

assert verifica(posicao_no_dict, 'bc93f3aa0638643b13a7550176df741cec5dca8301ac5f8149e171c1', nome_questao='posicao_no_dict'), 'posicao_no_dict incorreta'

print('Exercicio acesso aninhado (multipla escolha): OK')


# ===== FASE 2 - A funcao email =====

'''
EXERCICIO

Faca a funcao email(agenda, pessoa) que retorna o email da pessoa.
Eh o acesso aninhado simples: acesse o dict da pessoa, depois o campo 'email'.

    >>> agenda = {'ana': {'email': 'ana@x.com', 'telefones': [111]}}
    >>> email(agenda, 'ana')
    'ana@x.com'
'''
def email(agenda, pessoa):
    email_pessoa = agenda[pessoa]['email']
    return email_pessoa

agenda_mirtes_t = {
    'ana': {'email': 'ana@x.com', 'telefones': [111]},
    'bia': {'email': 'bia@x.com', 'telefones': [222, 333]},
}
agenda_cicero_t = {'davi': {'email': 'davi@y.com', 'telefones': [444]}}

assert email(agenda_mirtes_t, 'ana') == 'ana@x.com', 'email(agenda_mirtes_t, "ana") eh "ana@x.com"'
assert email(agenda_mirtes_t, 'bia') == 'bia@x.com', 'email(agenda_mirtes_t, "bia") eh "bia@x.com"'
assert email(agenda_cicero_t, 'davi') == 'davi@y.com', 'email(agenda_cicero_t, "davi") eh "davi@y.com"'
print('Exercicio email: OK')


# ===== FASE 3 - A funcao telefone_principal =====

'''
EXERCICIO

Faca a funcao telefone_principal(agenda, pessoa) que retorna o PRIMEIRO
telefone da pessoa. Caminho: dict da pessoa -> lista 'telefones' -> indice 0.

    >>> agenda = {'ana': {'email': 'ana@x.com', 'telefones': [111, 222]}}
    >>> telefone_principal(agenda, 'ana')
    111
'''
def telefone_principal(agenda, pessoa):
    telefono_principal = agenda[pessoa]['telefones'][0]
    return telefono_principal

assert telefone_principal(agenda_mirtes_t, 'ana') == 111, 'telefone_principal(.., "ana") eh 111'
assert telefone_principal(agenda_mirtes_t, 'bia') == 222, 'telefone_principal(.., "bia") eh 222 (o 1o de [222, 333])'
assert telefone_principal(agenda_cicero_t, 'davi') == 444, 'telefone_principal(.., "davi") eh 444'
print('Exercicio telefone_principal: OK')


# ===== FASE 4 - A funcao sem_email =====

'''
EXPLICACAO

Ate aqui voce sempre soube DE QUEM queria o dado: pediu o email do lucas, o
telefone principal da ana. Agora a pergunta muda de forma: "quem, na agenda
inteira, NAO tem email?". Nao da pra saber de antemao quantas pessoas sao,
nem quais.

Duas coisas novas, entao:

  - PERCORRER a agenda, pessoa por pessoa, sem deixar ninguem de fora;
  - FILTRAR: olhar uma pessoa de cada vez e ficar so com as que interessam.

O filtro se apoia num teste que responde True ou False para UMA pessoa. Como
a marta pode nao ter a chave 'email', o que temos que fazer eh
pegar o dicionario da marta, e perguntar com `in` nas CHAVES do dict dela.

Comece treinando esse teste, uma pessoa por vez. Percorrer TODAS elas fica
para a fase ponte, logo depois.
'''

agenda_f4 = {
    'ana':  {'email': 'ana@x.com', 'telefones': [111]},
    'bia':  {'telefones': [222]},
    'davi': {'telefones': [333]},
    'cleo': {'email': 'cleo@x.com', 'telefones': [444]},
}

'''
EXERCICIO

A agenda_f4 esta escrita aqui em cima como codigo Python - pode usar ela
nas respostas

Escreva, para cada pessoa, uma EXPRESSAO que vale True se ela TEM email e
False se ela nao tem.
'''
ana_tem_email  = 'email' in agenda_f4['ana'].keys()
bia_tem_email  = 'email' in agenda_f4['bia'].keys()
davi_tem_email = 'email' in agenda_f4['davi'].keys()
cleo_tem_email = 'email' in agenda_f4['cleo'].keys()

# Travou? Descomente a linha abaixo para ler a dica:
# explicar('quem_tem_email')

assert verifica(ana_tem_email, '4a5766bfad4caecdfac0fa7a3a0988e962b76ddab305c7586f7fff60', nome_questao='ana_tem_email'), 'ana_tem_email incorreta'
assert verifica(bia_tem_email, '0450b56d909851d9eb9300976bfcdf9f723d622acd3d456956f76f13', nome_questao='bia_tem_email'), 'bia_tem_email incorreta'
assert verifica(davi_tem_email, '1f01b6dcce0406d018813cf422bd7e0db24d8a987b707ed29bdcb4a1', nome_questao='davi_tem_email'), 'davi_tem_email incorreta'
assert verifica(cleo_tem_email, '98336843138f818009763417aba5dd1e7dfe9cb27d693f2a8b0de72b', nome_questao='cleo_tem_email'), 'cleo_tem_email incorreta'
print('Exercicio quem tem email: OK')


'''
EXERCICIO

Q - como_testar_email

Voce acabou de escrever o teste. Agora repare no que ele NAO eh: das tres
formas abaixo, qual responde se a marta tem email SEM dar erro?
Alternativas 'a', 'b' ou 'c'. Se travar, use o explicar.

    a) agenda['marta']['email']          - se nao tiver, retorna False
    b) 'email' in agenda['marta'].keys() - retorna True/False
    c) 'email' in agenda.keys()          - retorna True/False
'''
como_testar_email = 'b'   # 'a', 'b' ou 'c'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('como_testar_email')

assert verifica(como_testar_email, 'f2d91671051e214988ea9aa7579fbf7f62da139759ce7da3de0f33e5', nome_questao='como_testar_email'), 'como_testar_email incorreta'


'''
EXPLICACAO - FASE PONTE (da ideia para o codigo)

Voce ja sabe testar UMA pessoa. Falta passar por TODAS e juntar os nomes que
passaram no teste. Esse eh o padrao FILTRO, e ele tem tres pecas: uma lista
vazia no comeco, um `for` que visita todo mundo, e um append para cada
pessoa que interessa.

Pseudocodigo:

       resultado = lista vazia
       for cada pessoa da agenda:
           if 'email' not in agenda[pessoa].keys():
               guarde o nome dela no resultado
       retorne resultado

As 3 questoes abaixo perguntam, peca por peca, a traducao. Em cada uma o
pseudocodigo reaparece com a linha em foco marcada com -->. Alternativas
'a', 'b', 'c' ou 'd'. Se travar, use o explicar.
'''


'''
EXERCICIO

Q1 - init_sem_email

Pseudocodigo (linha em foco marcada com -->):

  -->  resultado = lista vazia
       for cada pessoa da agenda:
           if 'email' not in agenda[pessoa].keys():
               guarde o nome dela no resultado
       retorne resultado

Como criar o resultado, ainda vazio, antes do laco comecar?

    a) resultado = {}
    b) resultado = 0
    c) resultado = []
    d) resultado = ['email']
'''
init_sem_email = 'c'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('init_sem_email')

assert verifica(init_sem_email, '54e908f1716075de9f2c9bd1786309a496d53b20cb5821e8f4906470', nome_questao='init_sem_email'), 'init_sem_email incorreta'


'''
EXERCICIO

Q2 - loop_pessoas

Pseudocodigo (linha em foco marcada com -->):

       resultado = []
  -->  for cada pessoa da agenda:
           if 'email' not in agenda[pessoa].keys():
               guarde o nome dela no resultado
       retorne resultado

Como percorrer as pessoas da agenda, uma por vez?

    a) for pessoa in agenda.keys():
    b) for pessoa in agenda.values():
    c) for pessoa in agenda['email']:
    d) for i in range(len(agenda.keys())):
'''
loop_pessoas = 'a'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('loop_pessoas')

assert verifica(loop_pessoas, '479a9b32fdc571cfb3dfcfa3467d5081b38ede4d09dd5916f11c85be', nome_questao='loop_pessoas'), 'loop_pessoas incorreta'


'''
EXERCICIO

Q3 - guarda_o_nome

Pseudocodigo (linha em foco marcada com -->):

       resultado = []
       for pessoa in agenda.keys():
           if 'email' not in agenda[pessoa].keys():
  -->            guarde o nome dela no resultado
       retorne resultado

A pessoa da vez passou no teste (nao tem email). Como guardar o NOME dela
no resultado?

    a) resultado = pessoa
    b) resultado.append(agenda[pessoa])
    c) agenda.append(pessoa)
    d) resultado.append(pessoa)
'''
guarda_o_nome = 'd'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('guarda_o_nome')

assert verifica(guarda_o_nome, '7cc26d3c126a6b5c28485bf3b93bbec243ca7f3be64440795b266014', nome_questao='guarda_o_nome'), 'guarda_o_nome incorreta'

print('Exercicio ponte sem_email: OK')


'''
EXERCICIO

Agora junte as pecas na funcao sem_email(agenda), que retorna uma LISTA com
os nomes das pessoas que NAO tem a chave 'email'. A funcao NAO deve mutar a
agenda.

    >>> agenda = {
    ...   'ana':  {'email': 'ana@x.com', 'telefones': [111]},
    ...   'bia':  {'telefones': [222]},
    ... }
    >>> sem_email(agenda)
    ['bia']
'''
def sem_email(agenda):
    not_email = []
    for pessoa in agenda.keys():
        if 'email' not in agenda[pessoa].keys():
           not_email.append(pessoa)
    return not_email

# 1: misto -> bia e davi
assert type(sem_email(agenda_f4)) == list, "a sua funcao sem email nao esta retornando uma lista"
assert sorted(sem_email(agenda_f4)) == ['bia', 'davi'], f'sem_email misto: {sem_email(agenda_f4)}'

# 2: todos com email -> []
todos_com_email = {
    'ana': {'email': 'a@x.com', 'telefones': [1]},
    'bia': {'email': 'b@x.com', 'telefones': [2]},
}
assert sem_email(todos_com_email) == [], 'sem_email com todos tendo email deveria ser []'

# 3: ninguem com email -> todos
ninguem_com_email = {
    'ana': {'telefones': [1]},
    'bia': {'telefones': [2]},
}
assert sorted(sem_email(ninguem_com_email)) == ['ana', 'bia'], 'sem_email com ninguem tendo email deveria pegar todos'

# 4: nao deve mutar (modificar) a agenda
agenda_antes = {'ana': {'telefones': [1]}, 'bia': {'email': 'b@x.com', 'telefones': [2]}}
sem_email(agenda_antes)
assert agenda_antes == {'ana': {'telefones': [1]}, 'bia': {'email': 'b@x.com', 'telefones': [2]}}, 'sem_email NAO deve mutar a agenda'

print('Exercicio sem_email: OK')


# ===== FASE 5 - conta_telefones (agregacao) + FASE PONTE =====

'''
EXPLICACAO

AGREGACAO: percorrer a agenda e ACUMULAR um numero. Aqui queremos o total de
telefones - somando os tamanhos de todas as listas. Telefones repetidos
CONTAM (se a mesma pessoa tem [111, 111], isso conta 2).
'''


'''
EXERCICIO

Calculo a mao. Conte o TOTAL de telefones (somando todos):

    agenda_ex = {
        'ana': {'telefones': [111, 222]},   # 2 telefones
        'bia': {'telefones': [333]},        # 1 telefone
    }
'''
conta_telefones_a_mao = 3

assert verifica(conta_telefones_a_mao, '0dbd6268859322f66f6c9e5deda5293557c7ac92e03dae4cfb12d982', nome_questao='conta_telefones_a_mao'), 'conta_telefones_a_mao incorreta'


'''
EXERCICIO

Mais um:

    agenda_ex2 = {
        'ana':  {'telefones': [111, 222, 333]},   # 3
        'bia':  {'telefones': [444]},             # 1
        'davi': {'telefones': [555, 666]},        # 2
    }
'''
conta_telefones_a_mao_2 = 6

assert verifica(conta_telefones_a_mao_2, '31da1a042dc910775ed8b487afbdafd929a7afdeaadc660cb963bd26'), 'conta_telefones_a_mao_2 incorreta'
print('Exercicio conta_telefones a mao: OK')


'''
EXPLICACAO - FASE PONTE (da ideia para o codigo)

Voce ja entendeu a ideia (somar os tamanhos das listas). Falta traduzir para
Python. Esta eh a PRIMEIRA agregacao com loop unico (um `for` + um
acumulador) - o mesmo padrao vai voltar, em dobro, na Fase 6.

Pseudocodigo:

       total = 0
       for pessoa in agenda.keys():
           tels  = lista_de_telefones_da_pessoa
           adiciona a quantidade de telefones da pessoa no total
       retorne total

As 2 questoes abaixo perguntam, peca por peca, a traducao. Em cada uma o
pseudocodigo reaparece com a linha em foco marcada com -->. Alternativas
'a', 'b', 'c', 'd', 'e' ou 'f'. Se travar, use o explicar.
'''



'''
EXERCICIO

Q1 - pega_lista_tels

Pseudocodigo (linha em foco marcada com -->):

       total = 0
       for pessoa in agenda.keys():
  -->      tels  = lista_de_telefones_da_pessoa
           adiciona a quantidade de telefones da pessoa no total
       retorne total

Como fica a linha selecionada?

    a) tels = agenda['telefones']
    b) tels = pessoa['telefones']
    c) tels = agenda[pessoa]['telefones']
    d) tels = agenda['telefones'][pessoa]
    e) tels = agenda['telefones']['pessoa']
    f) tels = agenda['pessoa']['telefones']
'''
pega_lista_tels = 'c'   # 'a', 'b', 'c', 'd', 'e' ou 'f'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('pega_lista_tels')

assert verifica(pega_lista_tels, 'b637d135655aa3c00e543422e2b57886eccf835596a0d11286e35818', nome_questao='pega_lista_tels'), 'pega_lista_tels incorreta'


'''
EXERCICIO

Q2 - soma_no_total

Pseudocodigo (linha em foco marcada com -->):

       total = 0
       for pessoa in agenda.keys():
           tels = agenda[pessoa]['telefones']
  -->      adiciona a quantidade de telefones da pessoa no total
       retorne total

Como somar a quantidade de telefones dessa pessoa no total? (lembre:
repetidos CONTAM)

    a) total = total + 1
    b) total = total + tels
    c) total = len(tels)
    d) total = total + len(tels)
'''
soma_no_total = 'd'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('soma_no_total')

assert verifica(soma_no_total, '72a3c1fe25ecf86993d9a64a74a260d148cfe97e7c3377c6632bf4c7', nome_questao='soma_no_total'), 'soma_no_total incorreta'




'''
EXERCICIO

Agora junte as pecas na funcao conta_telefones(agenda), que devolve o total
de telefones (contando repetidos). Tente nao olhar para a explicacao
anterior e puxar pela memoria. Se nao der e tiver passado uns 4 minutos, pode olhar.

    >>> agenda = {'ana': {'telefones': [111, 222]}, 'bia': {'telefones': [333]}}
    >>> conta_telefones(agenda)
    3
'''
def conta_telefones(agenda):
    total = 0
    for pessoa in agenda.keys():
        tels = agenda[pessoa]['telefones']
        total = total + len(tels)
    return total

ag1 = {
    'a': {'telefones': [1]},
    'b': {'telefones': [2]},
    'c': {'telefones': [3]},
    'd': {'telefones': [4]},
    'e': {'telefones': [5]},
}
assert conta_telefones(ag1) == 5, 'conta_telefones: 5 contatos de 1 tel cada -> 5'

ag2 = {'ana': {'telefones': [11, 22, 33]}, 'bia': {'telefones': [44]}}
assert conta_telefones(ag2) == 4, 'conta_telefones: 3 + 1 -> 4'

# repetidos CONTAM
ag3 = {'ana': {'telefones': [99, 99]}, 'bia': {'telefones': [99]}}
assert conta_telefones(ag3) == 3, 'conta_telefones: telefones repetidos contam -> 3'

ag_vazia = {}
assert conta_telefones(ag_vazia) == 0, 'conta_telefones de agenda vazia -> 0'
print('Exercicio conta_telefones: OK')


# ===== FASE 6 - conta_ocorrencias (CONSTRUIR dict por agregacao) + FASE PONTE =====

'''
EXPLICACAO

Agora juntamos DUAS coisas:
  - CONSTRUIR um dict do zero (igual conta_letras da Lista 1), mas a chave
    eh o TELEFONE e o valor eh quantas vezes ele aparece na agenda toda;
  - um loop ANINHADO: o de FORA anda pelas pessoas, o de DENTRO anda pelos
    telefones de cada pessoa.

    conta_ocorrencias devolve, por exemplo:

        {1122233344: 5, 9999: 1}   # o 1122233344 aparece 5 vezes; o 9999, 1
'''


'''
EXERCICIO

Calculo a mao. Considere:

    agenda_ex = {
        'ana':  {'telefones': [111, 222]},
        'bia':  {'telefones': [111, 333]},
        'davi': {'telefones': [111]},
    }

Olhe telefone por telefone (sao 3 pessoas). Quantas vezes aparece cada um?
'''
vezes_do_111 = 3
vezes_do_222 = 1

assert verifica(vezes_do_111, '99fb5f36cf8170df2876e09dcf0c07d6c0d3711899cf920de6b9768f', nome_questao='vezes_do_111'), 'vezes_do_111 incorreta'
assert verifica(vezes_do_222, 'e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178'), 'vezes_do_222 incorreta'
print('Exercicio conta_ocorrencias a mao (escalares): OK')


'''
EXERCICIO

Agora escreva o DICIONARIO de contagem COMPLETO da mesma agenda:

    agenda_ex = {
        'ana':  {'telefones': [111, 222]},
        'bia':  {'telefones': [111, 333]},
        'davi': {'telefones': [111]},
    }

Eh um dicionario telefone -> quantas vezes aparece. Formato:
{telefone: contagem, ...}. A ordem das chaves nao importa.
'''
contagem_a_mao = {'111':3, '222':1, '333':1}

assert type(contagem_a_mao) == dict, 'contagem a mao deve ser um dict'
#assert verifica(contagem_a_mao, '64eb07edda062b4e7be2269620dc5980c392344cc7afe64cce25b10e'), 'contagem_a_mao incorreta'
print('Exercicio conta_ocorrencias a mao (dict completo): OK')

'''
EXPLICACAO - FASE PONTE (da ideia para o codigo)

Pseudocodigo do conta_ocorrencias:

       contagem = dicionario vazio
       for pessoa in agenda.keys():
           for tel in lista_de_todos_os_telefones_da_pessoa:
               se o tel ainda NAO esta em contagem:
                   comece a contagem desse tel em zero
               some 1 na contagem desse tel
       retorne contagem

As questoes abaixo perguntam peca por peca. Alternativas 'a', 'b', 'c' ou
'd'. Se travar, use o explicar.
'''


'''
EXERCICIO

Q1 - init_ocorr

Pseudocodigo (linha em foco marcada com -->):

  -->  contagem = dicionario vazio
       for pessoa in agenda.keys():
           for tel in lista_de_todos_os_telefones_da_pessoa:
               se o tel ainda NAO esta em contagem:
                   comece a contagem desse tel em zero
               some 1 na contagem desse tel
       retorne contagem

Como criar o dict de contagem inicial (vazio)?

    a) contagem = {}
    b) contagem = []
    c) contagem = 0
    d) contagem = [{}]
'''
init_ocorr = 'a'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('init_ocorr')

assert verifica(init_ocorr, '576fe24fd657a2b501baed16abb165dbf921a40d73777db3a673ec0d', nome_questao='init_ocorr'), 'init_ocorr incorreta'



'''
EXERCICIO

Q2 - loop_interno

Pseudocodigo (linha em foco marcada com -->):

       contagem = {}
       for pessoa in agenda.keys():
  -->        for tel in lista_de_todos_os_telefones_da_pessoa:
               se o tel ainda NAO esta em contagem:
                   comece a contagem desse tel em zero
               some 1 na contagem desse tel
       retorne contagem

Dentro do laco de pessoas, como percorrer os telefones daquela pessoa?

    a) for tel in agenda['telefones']
    b) for tel in telefones
    c) for tel in agenda[pessoa]['telefones']
    d) for tel in agenda[pessoa].keys()
'''
loop_interno = 'c'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('loop_interno')

assert verifica(loop_interno, 'ed644aa1ecfde3f23ccdcfe46b4822fda5d1c2c99c9bfcc82f226b01', nome_questao='loop_interno'), 'loop_interno incorreta'


'''
EXERCICIO

Q3 - telefone_novo

Pseudocodigo (linha em foco marcada com -->):

       contagem = {}
       for pessoa in agenda.keys():
           for tel in agenda[pessoa]['telefones']:
  -->            se o tel ainda NAO esta em contagem:
                   comece a contagem desse tel em zero
               some 1 na contagem desse tel
       retorne contagem

Quando o tel ainda NAO esta em contagem, o que fazer antes de somar 1?
(igual conta_letras da Lista 1)

    a) contagem[tel] = 1
    b) contagem[tel] = 0
    c) contagem.append(tel)
    d) contagem[0] = tel
'''
telefone_novo = 'b'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('telefone_novo')

assert verifica(telefone_novo, 'e44492a1a30f85b16a080c57e26007042f2dc1ffcd6974a0bccf8aec', nome_questao='telefone_novo'), 'telefone_novo incorreta'


'''
EXERCICIO

Q4 - incremento_ocorrencias

Pseudocodigo (linha em foco marcada com -->):

       contagem = {}
       for pessoa in agenda.keys():
           for tel in agenda[pessoa]['telefones']:
               if tel not in contagem.keys():
                   contagem[tel] = 0
  -->            some 1 na contagem desse tel
       retorne contagem

Como somar 1 na contagem do telefone (a chave dele ja existe agora)?

    a) contagem[tel] = contagem[tel] + 1
    b) contagem[tel] = 1
    c) contagem = contagem + 1
    d) contagem.append(tel)
'''
incremento_ocorr = 'a'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('incremento_ocorr')

assert verifica(incremento_ocorr, '2643fda90586e60a196fbf88f3b01539719db4220a6e5336abb292bb', nome_questao='incremento_ocorr'), 'incremento_ocorr incorreta'

print('Exercicio ponte conta_ocorrencias: OK')


'''
EXERCICIO

Agora complete a funcao conta_ocorrencias(agenda), que devolve um dicionario
`telefone -> quantas vezes o telefone aparece na agenda inteira`.

O esqueleto ja vem com os DOIS `for` escritos (o laco aninhado eh a parte
nova). Voce completa: criar o dict, tratar o telefone novo, somar 1, e
retornar.

    >>> agenda = {'ana': {'telefones': [111, 222]}, 'bia': {'telefones': [111]}}
    >>> conta_ocorrencias(agenda)
    {111: 2, 222: 1}
'''
def conta_ocorrencias(agenda):
    contagem = {}
    for pessoa in agenda.keys():
        for tel in agenda[pessoa]['telefones']:
            if tel not in contagem.keys():
                contagem[tel] = 0
            contagem[tel] = contagem[tel] + 1
    return contagem

# mesmo numero em varios contatos
ag_a = {'ana': {'telefones': [1122233344]}, 'bia': {'telefones': [1122233344]}, 'davi': {'telefones': [1122233344]}}
assert conta_ocorrencias(ag_a) == {1122233344: 3}, f'conta_ocorrencias mesmo numero 3x: {conta_ocorrencias(ag_a)}'

# numeros distintos
ag_b = {'ana': {'telefones': [11, 22]}, 'bia': {'telefones': [33]}}
assert conta_ocorrencias(ag_b) == {11: 1, 22: 1, 33: 1}, f'conta_ocorrencias distintos: {conta_ocorrencias(ag_b)}'

# mistura (repetido dentro de um contato e entre contatos)
ag_c = {'ana': {'telefones': [99, 99]}, 'bia': {'telefones': [99, 77]}}
assert conta_ocorrencias(ag_c) == {99: 3, 77: 1}, f'conta_ocorrencias mistura: {conta_ocorrencias(ag_c)}'

assert conta_ocorrencias({}) == {}, 'conta_ocorrencias de agenda vazia -> {}'
print('Exercicio conta_ocorrencias: OK')


# ===== FASE 7 - Simulacao integrada: Mirtes e Cicero =====

'''
EXPLICACAO

Fecho da lista: as agendas completas de Mirtes e Cicero passam por TODAS as
funcoes. Repare como a mesma funcao serve as duas agendas - so muda o
argumento. Os dados foram escolhidos pra dar resultados diferentes: a Mirtes
tem alguem SEM email e um telefone repetido ENTRE contatos; o Cicero tem
todos com email e um telefone repetido DENTRO de um contato.
'''

agenda_mirtes = {
    'ana':   {'email': 'ana@mail.com',  'telefones': [1111, 2222]},
    'bruno': {'telefones': [1111]},                        # sem email; 1111 repetido entre contatos
    'cleo':  {'email': 'cleo@mail.com', 'telefones': [3333]},
}
agenda_cicero = {
    'davi': {'email': 'davi@mail.com', 'telefones': [4444]},
    'eva':  {'email': 'eva@mail.com',  'telefones': [5555, 5555]},  # 5555 repetido dentro
}

'''
EXERCICIO

Antes de rodar, PREVEJA os valores abaixo (olhe as agendas acima):

1) email da ana (na agenda_mirtes)
2) telefone principal da eva (na agenda_cicero)
3) quem nao tem email na agenda_mirtes (lista de nomes)
4) quem nao tem email na agenda_cicero (lista de nomes)
5) total de telefones da agenda_mirtes (com repetidos)
6) total de telefones da agenda_cicero (com repetidos)
7) quantas vezes o 1111 aparece na agenda_mirtes
8) quantas vezes o 5555 aparece na agenda_cicero
'''
email_da_ana      = agenda_mirtes['ana']['email']
tel_principal_eva = agenda_cicero['eva']['telefones'][0]
sem_email_mirtes  = sem_email(agenda_mirtes)
sem_email_cicero  = sem_email(agenda_cicero)
total_tels_mirtes = conta_telefones(agenda_mirtes)
total_tels_cicero = conta_telefones(agenda_cicero)
vezes_1111_mirtes = 2
vezes_5555_cicero = 2

assert verifica(email_da_ana, '73de7391c3261e2f0bd98cef1cf62eb20d8efad5105df368820d6bd4'), 'email_da_ana incorreta'
assert verifica(tel_principal_eva, '38464042bde8ddb4b61091d9ba473358a262980632131113475c813e'), 'tel_principal_eva incorreta'
assert verifica(sem_email_mirtes, 'da0e1b8df21f06d1d4d022151457818494fcdd2bd333e347931bc677'), 'sem_email_mirtes incorreta'
assert verifica(sem_email_cicero, '23f497f643e37257c3f7e54f049d8829c41103bb29bf8c0ba0d1df0a'), 'sem_email_cicero incorreta'
assert verifica(total_tels_mirtes, '271f93f45e9b4067327ed5c8cd30a034730aaace4382803c3e1d6c2f'), 'total_tels_mirtes incorreta'
assert verifica(total_tels_cicero, '05445e797013527cbc38e162e3ba3f21ed8085ed0e213131fbaf0b04', nome_questao='total_tels_cicero'), 'total_tels_cicero incorreta'
assert verifica(vezes_1111_mirtes, 'c0f79e3c0f9dbe61935fed864f8f2fab81ca16f0aa4a7e29430c5376', nome_questao='vezes_1111_mirtes'), 'vezes_1111_mirtes incorreta'
assert verifica(vezes_5555_cicero, '18af246eb1ebfecfcdf94bf33a1f2fca359080a628421eb88c332c69', nome_questao='vezes_5555_cicero'), 'vezes_5555_cicero incorreta'
print('Exercicio previsao Mirtes e Cicero: OK')

# agora as funcoes confirmam a sua previsao
assert email(agenda_mirtes, 'ana') == 'ana@mail.com', 'email da ana'
assert telefone_principal(agenda_cicero, 'eva') == 5555, 'tel principal da eva'
assert sorted(sem_email(agenda_mirtes)) == ['bruno'], 'sem_email mirtes'
assert sem_email(agenda_cicero) == [], 'sem_email cicero (todos tem email)'
assert conta_telefones(agenda_mirtes) == 4, 'total tels mirtes'
assert conta_telefones(agenda_cicero) == 3, 'total tels cicero'
assert conta_ocorrencias(agenda_mirtes)[1111] == 2, '1111 aparece 2x na mirtes (entre contatos)'
assert conta_ocorrencias(agenda_cicero)[5555] == 2, '5555 aparece 2x na cicero (dentro de um contato)'

print('Exercicio simulacao Mirtes e Cicero: OK')


print('\n=== PARABENS! Todos os exercicios completos! ===')
