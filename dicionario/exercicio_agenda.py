# Lista de exercicios - agenda (dicionario simples)
# Aprender a usar um dicionario `pessoa -> telefone`: ler (agenda[chave],
# len, `in`), entender que dict eh MUTAVEL, testar existencia, e por fim
# CONSTRUIR um dicionario do zero iterando (conta_letras).

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


# A funcao explicar() ajuda nas questoes de multipla escolha (Fases 1, 3 e
# 5). Se voce travar numa questao, descomente a linha `explicar('nome')`
# que aparece logo abaixo dela para ler a discussao das alternativas.
def explicar(questao):
    try:
        from explicacao_agenda import EXPLICACOES
    except ImportError:
        print("Arquivo 'explicacao_agenda.py' nao foi encontrado.")
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

Bem-vindo ao exercicio de AGENDA! Vamos guardar telefones de pessoas
usando um DICIONARIO.

Um dicionario eh muito parecido com uma lista. Lembre da lista
[10, 20, 30]: as POSICOES dela sao 0, 1 e 2. lista[0] vale 10,
lista[1] vale 20, lista[2] vale 30.

A diferenca eh que, num dicionario, as "posicoes" podem ser qualquer
coisa - inclusive strings. Essas "posicoes" do dicionario tem um nome proprio:
sao as CHAVES. Em vez de lista[0], escrevemos
agenda['marcos'].

0 era uma posicao da lista, 'marcos' eh uma CHAVE do dicionario

Na nossa agenda, a CHAVE eh a pessoa e o VALOR eh o telefone dela:

    agenda = {'marcos': 32112232, 'fabio': 988887788}
    #          ^chave   ^valor
    agenda['marcos']   # devolve 32112232 (o telefone do marcos)

    Entao essa agenda acima tem duas chaves (marcos e fabio) cada uma
    com seu valor (a chave marcos tem o valor 32112232, a chave fabio,
    o valor 988887788)

Nesse exercicio,  funcoes NAO acessam
variaveis globais. A agenda entra por parametro, e a funcao trabalha
em cima do que recebeu.
'''


# ===== FASE 1 - Aquecimento: lendo um dicionario =====

'''
EXPLICACAO

O comando `agenda.keys()` da uma 'lista' das CHAVES da agenda 
(as pessoas). 

Com ele, tres operacoes basicas para LER um dicionario:

    agenda['maria']            # o VALOR guardado na CHAVE 'maria' (o telefone)
    len(agenda.keys())         # quantas chaves (pessoas) a agenda tem
    'fabio' in agenda.keys()   # True se 'fabio' eh uma CHAVE da agenda; senao False

Repare bem: o que vai ENTRE COLCHETES eh sempre uma CHAVE. O dicionario
olha as chaves que ele tem e devolve o valor da chave que voce pediu.
'''

agenda_exemplo = {'marcos': 32112232, 'fabio': 988887788, 'maria': 44554455}

'''
EXERCICIO

Considere a agenda_exemplo acima.

Preencha as variaveis usando uma EXPRESSAO Python que produz o valor (em
vez de escrever o valor literal). Se nao conseguir, pode comecar pelo
valor pra ver o teste passar, mas depois tente a expressao.

1) Qual o telefone da maria?      Dica: Veja os comandos disponiveis logo acima.
O dicionario que voce vai usar nesse exercicio chama 'agenda_exemplo'
2) Quantas pessoas tem na agenda? Dica: Veja os comandos disponiveis logo acima
3) 'fabio' esta na agenda?        Dica: Veja os comandos disponiveis logo acima
4) 'joao' esta na agenda?         Dica: Veja os comandos disponiveis logo acima
'''
tel_da_maria = agenda_exemplo['maria']
quantas_pessoas = len(agenda_exemplo)
tem_fabio = 'fabio' in agenda_exemplo
tem_joao = 'joao' in agenda_exemplo

assert verifica(tel_da_maria, '40b00d89b8ee564ea28767bc4e4426bdd98b46898c67ed4056737595', nome_questao='tel_da_maria'), 'tel_da_maria incorreta'
assert verifica(quantas_pessoas, '43961682cfc75e687fa6cb341a015ea1634edbe77b5a0be0b5604cba', nome_questao='quantas_pessoas'), 'quantas_pessoas incorreta'
assert verifica(tem_fabio, '8a66f6f5364fc3c57c22fd67874ed87d2f59c5073ec2d67d98174677', nome_questao='tem_fabio'), 'tem_fabio incorreta'
assert verifica(tem_joao, '60a87bd2b1ae419baf93c06cf7c4d95304d8b6f500223521008cfef9', nome_questao='tem_joao'), 'tem_joao incorreta'
print('Exercicio lendo um dicionario: OK')


'''
EXERCICIO

Tres questoes de multipla escolha sobre o que vai ENTRE COLCHETES. Lembre
da definicao do texto: entre colchetes vai uma CHAVE, e o dicionario
devolve o valor dessa chave.

Cada questao tem 4 alternativas: 'a', 'b', 'c' ou 'd'. Escolha a CORRETA.
Se travar, descomente a linha `explicar(...)` logo abaixo da variavel.

Q1 - acesso_chave

A agenda_exemplo eh {'marcos': 32112232, 'fabio': 988887788, 'maria': 44554455}.
O que `agenda_exemplo['maria']` retorna?

    a) o telefone da maria (o valor guardado na chave 'maria')
    b) a posicao da maria na agenda
    c) erro, porque 'maria' nao eh um numero
    d) o nome 'maria'
'''
acesso_chave = 'a'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('acesso_chave')

assert verifica(acesso_chave, '4e5946596a00f935719f5ed68ac872d8595a665b1dd63ebf307f8ec6', nome_questao='acesso_chave'), 'acesso_chave incorreta'


'''
EXERCICIO

Q2 - acesso_valor

A agenda_exemplo eh {'marcos': 32112232, 'fabio': 988887788, 'maria': 44554455}.
44554455 eh o TELEFONE da maria. O que acontece com `agenda_exemplo[44554455]`
(o telefone entre colchetes)?

    a) retorna 'maria'
    b) KeyError - 44554455
    c) retorna o telefone da maria
    d) retorna 0

'''
acesso_valor = 'b'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('acesso_valor')

assert verifica(acesso_valor, '23412c0ec2b7e7f57be79d4f70a4fd76445ffdcf9946beb15d61d24f', nome_questao='acesso_valor'), 'acesso_valor incorreta'


'''
EXERCICIO

Q3 - acesso_posicao

A agenda_exemplo eh {'marcos': 32112232, 'fabio': 988887788, 'maria': 44554455}.
Numa LISTA, lista[0] eh o primeiro elemento. E num dicionario? O que
acontece com `agenda_exemplo[0]`?

    a) retorna o telefone do marcos (primeira pessoa)
    b) retorna 'marcos'
    c) KeyError - 0
    d) retorna a agenda inteira
'''
acesso_posicao = 'c'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('acesso_posicao')

assert verifica(acesso_posicao, '73e9ba2feb040e21266f58c3a86bee199f092a1dd94b9545928da753', nome_questao='acesso_posicao'), 'acesso_posicao incorreta'

print('Exercicio acesso por chave/valor/posicao: OK')


# ===== FASE 2 - A funcao consulta =====

'''
EXERCICIO

Faca a funcao consulta(agenda, pessoa) que retorna o telefone da pessoa
na agenda.

Repare: a funcao NAO usa nenhuma agenda global. Ela recebe a agenda por
parametro e devolve o telefone com `return`.

    >>> agenda = {'ana': 111, 'bia': 222}
    >>> consulta(agenda, 'ana')
    111
    >>> consulta(agenda, 'bia')
    222
'''
def consulta(agenda, pessoa):
    telefone = pessoa
    return agenda[telefone]

# a MESMA funcao serve a agendas diferentes (Mirtes e Cicero)
agenda_mirtes_t = {'ana': 111, 'bia': 222}
agenda_cicero_t = {'davi': 333}

assert consulta(agenda_mirtes_t, 'ana') == 111, 'consulta(agenda_mirtes_t, "ana") eh 111'
assert consulta(agenda_mirtes_t, 'bia') == 222, 'consulta(agenda_mirtes_t, "bia") eh 222'
assert consulta(agenda_cicero_t, 'davi') == 333, 'consulta(agenda_cicero_t, "davi") eh 333'
print('Exercicio consulta: OK')


# ===== FASE 3 - A funcao adiciona (dict eh MUTAVEL) =====

'''
EXPLICACAO

Para guardar um telefone novo na agenda:

    agenda['lucas'] = 39774596

Isso CRIA a chave `lucas` (se ainda nao existir) com o valor `39774596`.

Um ponto importante: o dicionario eh MUTAVEL. (tem uma "setinha" no pythontutor)
Quando voce passa a agenda por parametro para uma função
essa funcao altera a MESMA agenda que esta la fora. Por isso a funcao adiciona
NAO precisa retornar nada - ela muta a agenda direto.

    adiciona(agenda_mirtes, 'ana', 555)
    # agenda_mirtes JA mudou - NAO precisa de uma reatribuicao
    # como "agenda_mirtes = adiciona(...)"
'''


'''
EXERCICIO

Faca a funcao adiciona(agenda, pessoa, telefone) que guarda o telefone da
pessoa na agenda (`agenda[pessoa] = telefone`). A funcao NAO retorna nada -
ela muta(mutar = modificar) a agenda que veio por parametro.

    >>> agenda = {}
    >>> adiciona(agenda, 'ana', 555)
    >>> agenda
    {'ana': 555}
    >>> adiciona(agenda, 'bia', 777)
    >>> agenda
    {'ana': 555, 'bia': 777}
    >>> adiciona(agenda, 'ana', 999)   # 'ana' ja existe -> SOBRESCREVE
    >>> agenda
    {'ana': 999, 'bia': 777}
'''
def adiciona(agenda, pessoa, telefone):
    agenda[pessoa] = telefone

# teste 1: adicionar numa agenda vazia
agenda_t = {}
adiciona(agenda_t, 'ana', 555)
assert agenda_t == {'ana': 555}, f'apos adicionar ana, esperado {{"ana": 555}}, obteve {agenda_t}'

# teste 2: varias adicoes
adiciona(agenda_t, 'bia', 777)
assert agenda_t == {'ana': 555, 'bia': 777}, f'apos adicionar bia: {agenda_t}'

# teste 3: sobrescrever chave que ja existe (atualiza, nao duplica)
adiciona(agenda_t, 'ana', 999)
assert agenda_t == {'ana': 999, 'bia': 777}, f'ao re-adicionar ana, deveria SOBRESCREVER: {agenda_t}'
assert len(agenda_t.keys()) == 2, f'a agenda deveria ter 2 chaves (ana nao duplica), tem {len(agenda_t.keys())}'

print('Exercicio adiciona: OK')


'''
EXERCICIO

Questoes de multipla escolha. Cada questao diz quais letras ela aceita.
Se travar, descomente a linha `explicar(...)`.

Q1 - criar_chave_nova

A agenda comeca vazia: agenda = {}. Quero CRIAR a chave 'ana' com o
telefone 555. O que funciona?

    a) agenda['ana'] = 555
    b) agenda.append('ana', 555)
    c) agenda['ana'].append(555)
    d) `agenda['ana'] = 555` e `agenda.append('ana', 555)` funcionam
    e) os tres primeiros comandos funcionam
'''
criar_chave_nova = 'a'   # 'a', 'b', 'c', 'd' ou 'e'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('criar_chave_nova')

assert verifica(criar_chave_nova, 'df4664e90d5010ae4dd27687ffabcced2af96675f48724378995d4e3', nome_questao='criar_chave_nova'), 'criar_chave_nova incorreta'


'''
EXERCICIO

Q2 - precisa_reatribuir

Depois de chamar `adiciona(agenda, 'ana', 555)`, preciso escrever
`agenda = adiciona(agenda, 'ana', 555)` pra agenda realmente mudar?

    a) sim, senao a mudanca se perde
    b) nao, basta chamar adiciona(...)
    c) so se a chave ja existir
'''
precisa_reatribuir = 'b'   # 'a', 'b' ou 'c'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('precisa_reatribuir')

assert verifica(precisa_reatribuir, '6fc63acc6ab0d18aeb6a1fdcf0f1adfd39d41ae702d260eae7f52a3e', nome_questao='precisa_reatribuir'), 'precisa_reatribuir incorreta'


'''
EXERCICIO

Q3 - chave_repetida

'ana' ja esta na agenda com o telefone 555. Depois de
`adiciona(agenda, 'ana', 999)`, quanto vale agenda['ana']?

    a) 555 (o primeiro vence)
    b) 999 e 555 ficam os dois guardados
    c) 999 - sobrescreve o valor antigo
'''
chave_repetida = 'c'   # 'a', 'b' ou 'c'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('chave_repetida')

assert verifica(chave_repetida, 'eaee495fc31d3fdaa8fcec3b18d5c7c1fd020fe08fc33f9f1ced38ac', nome_questao='chave_repetida'), 'chave_repetida incorreta'

print('Exercicio dict mutavel (multipla escolha): OK')


# ===== FASE 4 - A funcao esta_na_agenda =====

'''
EXPLICACAO

E se a gente quiser saber se uma pessoa ESTA na agenda, sem dar erro?

Tentar `agenda[pessoa]` direto eh perigoso: se a pessoa NAO existe, da
KeyError (o programa quebra). Para perguntar com seguranca, use o `in`:

    pessoa in agenda.keys()    # True se 'pessoa' eh uma chave; False se nao eh

'''


'''
EXERCICIO

Faca a funcao esta_na_agenda(agenda, pessoa) que retorna True se a pessoa
eh uma chave da agenda, e False caso contrario.

    >>> agenda = {'ana': 111, 'bia': 222}
    >>> esta_na_agenda(agenda, 'ana')
    True
    >>> esta_na_agenda(agenda, 'zeca')
    False
'''
def esta_na_agenda(agenda, pessoa):
    return pessoa in agenda

agenda_t = {'ana': 111, 'bia': 222}
assert esta_na_agenda(agenda_t, 'ana') == True, 'esta_na_agenda(.., "ana") eh True (presente)'
assert esta_na_agenda(agenda_t, 'bia') == True, 'esta_na_agenda(.., "bia") eh True (presente)'
assert esta_na_agenda(agenda_t, 'zeca') == False, 'esta_na_agenda(.., "zeca") eh False (ausente)'
assert esta_na_agenda({}, 'ana') == False, 'esta_na_agenda numa agenda vazia eh sempre False'
print('Exercicio esta_na_agenda: OK')


# ===== FASE 5 - conta_letras (CONSTRUIR um dicionario) =====

'''
EXPLICACAO

Ate agora a gente LEU e ATUALIZOU dicionarios prontos. Agora vamos
CONSTRUIR um do zero.

Objetivo: dada uma palavra, contar quantas vezes cada letra aparece.

    conta_letras('banana')  ->  {'b': 1, 'a': 3, 'n': 2}

A ideia: comecar com um dicionario vazio e ir percorrendo a palavra
letra por letra, somando 1 na contagem da letra atual. Antes de codar,
vamos calcular algumas contagens A MAO.
'''


'''
EXERCICIO

Calculo a mao. Conte, letra por letra:

    palavra = 'banana'    (b, a, n, a, n, a)

Quantas vezes aparece cada letra?
'''
qtd_b_banana = 1
qtd_a_banana = 3
qtd_n_banana = 2

assert verifica(qtd_b_banana, '74c001857daca3fa3643f2688b1b2d0d1db04d41b071599822fdc87b', nome_questao='qtd_b_banana'), 'qtd_b_banana incorreta'
assert verifica(qtd_a_banana, 'f874e09443b42f5863c2e12b70ce2cbb3a61351629a10b6c102d81b1', nome_questao='qtd_a_banana'), 'qtd_a_banana incorreta'
assert verifica(qtd_n_banana, 'd61116adb3ed2b2aeaa7362304bb351c381085f6d48a5b5b6e40022a', nome_questao='qtd_n_banana'), 'qtd_n_banana incorreta'
print('Exercicio conta_letras a mao: OK')


'''
EXPLICACAO - FASE PONTE (da ideia para o codigo)

Voce ja sabe a IDEIA (contar letra por letra). Falta traduzir para Python.
Esta fase quebra a traducao em pecas pequenas. Veja o pseudocodigo:

       contador = dicionario vazio
       for letra in palavra: # executa varias vezes, uma para cada letra da palavra
           se a letra ainda NAO esta no contador:
               comece o contador dessa letra em zero
           some 1 no contador dessa letra
       retorne a resposta

As 6 questoes abaixo perguntam, peca por peca, qual eh a traducao correta.
Em cada questao o pseudocodigo aparece de novo, com a linha em foco MARCADA
com -->. Alternativas 'a', 'b', 'c' ou 'd'. Se travar, descomente o
`explicar(...)` logo abaixo da variavel.
'''


'''
EXERCICIO

Q1 - init_contador

Pseudocodigo (linha em foco marcada com -->):

  -->  contador = dicionario vazio
       for letra in palavra: # executa varias vezes, uma para cada letra da palavra
           se a letra ainda NAO esta no contador:
               comece o contador dessa letra em zero
           some 1 no contador dessa letra
       retorne a resposta

Como criar o contador inicial (um dicionario vazio)?

    a) contador = {}
    b) contador = []
    c) contador = 0
    d) contador = ['']
'''
init_contador = 'a'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('init_contador')

assert verifica(init_contador, '9c965ecf824f11c54e576c560c6ec1d6d2c2a4dbe8028cf251af5086', nome_questao='init_contador'), 'init_contador incorreta'


'''
EXERCICIO

Q2 - letra_nova

Pseudocodigo (linha em foco marcada com -->):

       contador = {}
       for letra in palavra: # executa varias vezes, uma para cada letra da palavra
           se a letra ainda NAO esta no contador:
    -->        comece o contador dessa letra em zero
           some 1 no contador dessa letra
       retorne a resposta

Quando a letra ainda NAO esta no contador, o que fazer antes de somar 1?

    a) contador[letra] = 1
    b) contador[letra] = 0
    c) contador.append(letra)
    d) contador[0] = letra
'''
letra_nova = 'b'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('letra_nova')

assert verifica(letra_nova, 'c244922f315327f7f04c0aa1db680c7e2182ad8c105f563957703c04', nome_questao='letra_nova'), 'letra_nova incorreta'


'''
EXERCICIO

Q3 - por_que_checar

Pseudocodigo (linha em foco marcada com -->):

       contador = {}
       for letra in palavra: # executa varias vezes, uma para cada letra da palavra
    -->    se a letra ainda NAO esta no contador:
               contador[letra] = 0
           some 1 no contador dessa letra
       retorne a resposta

Por que precisamos dessa checagem? Ou seja: se a gente tirasse ela e fizesse
`contador[letra] = contador[letra] + 1` direto, o que aconteceria?

    a) nada muda, funciona igual
    b) na PRIMEIRA vez que vemos a letra, o contador[letra] "da esquerda" da atribuicao da KeyError (a chave ainda nao existe)
    c) o programa fica lento
    d) conta tudo em dobro
'''
por_que_checar = 'b'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('por_que_checar')

assert verifica(por_que_checar, '01170f69a3ab6ada27a36676f8ed992105435483996bdb2da7b4d32f', nome_questao='por_que_checar'), 'por_que_checar incorreta'


'''
EXERCICIO

Q4 - como_checar

Pseudocodigo (linha em foco marcada com -->):

       contador = {}
       for letra in palavra: # executa varias vezes, uma para cada letra da palavra
    -->    se a letra ainda NAO esta no contador:
               contador[letra] = 0
           some 1 no contador dessa letra
       retorne a resposta

A questao anterior explicou POR QUE essa checagem precisa existir. Agora:
como ela se ESCREVE em Python?

    a) if contador[letra] == 0:
    b) if letra not in contador.values():
    c) if letra not in contador.keys():
    d) if letra not in palavra:
'''
como_checar = 'c'   # 'a', 'b', 'c' ou 'd'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('como_checar')

assert verifica(como_checar, '27abc6fd2bb678f3c959e42633b4d718f8b004195ce8d0bf5460be8e', nome_questao='como_checar'), 'como_checar incorreta'


'''
EXERCICIO

Q5 - incremento

Pseudocodigo (linha em foco marcada com -->):

       contador = {}
       for letra in palavra: # executa varias vezes, uma para cada letra da palavra
           if letra not in contador.keys():
               contador[letra] = 0
    -->    some 1 no contador dessa letra
       retorne a resposta

Como somar 1 na contagem da letra (a chave dela ja existe agora)?

    a) contador[letra] = contador[letra] + 1
    b) contador[letra] = 1
    c) contador = contador + 1
    d) contador.append(letra)
'''
incremento = 'a'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('incremento')

assert verifica(incremento, '0982a3d0dcc0b91bf76c85502554af7d2c0f2e4107572cf43075c266', nome_questao='incremento'), 'incremento incorreta'


'''
EXERCICIO

Q6 - retorno

Pseudocodigo (linha em foco marcada com -->):

       contador = {}
       for letra in palavra: # executa varias vezes, uma para cada letra da palavra
           if letra not in contador.keys():
               contador[letra] = 0
           contador[letra] = contador[letra] + 1
  -->  retorne a resposta

O que a funcao deve retornar no fim?

    a) return letra
    b) return len(contador.keys())
    c) return contador
    d) return palavra
'''
retorno = 'c'

# Travou? Descomente a linha abaixo para ler a explicacao:
# explicar('retorno')

assert verifica(retorno, '4ea094c07bc848fe3169e25185603f19b4b20ea500760f151dcac253', nome_questao='retorno'), 'retorno incorreta'

print('Exercicio ponte conta_letras: OK')


'''
EXERCICIO

Agora junte as pecas na funcao conta_letras(palavra), que devolve um
dicionario `letra -> quantas vezes a letra aparece na palavra`.

       contador = dicionario vazio
       for letra in palavra: # executa varias vezes, uma para cada letra da palavra
           se a letra ainda NAO esta no contador:
               comece o contador dessa letra em zero
           some 1 no contador dessa letra
       retorne a resposta

Tente montar a funcao a partir do pseudocodigo acima, sem ficar olhando as
respostas. Se travar, bata cabeca um pouco antes de espiar.

    >>> conta_letras('banana')
    {'b': 1, 'a': 3, 'n': 2}
    >>> conta_letras('arara')
    {'a': 3, 'r': 2}

O esqueleto ja vem com o `for letra in palavra` pronto (ele percorre a
palavra uma letra por vez - isso eh novo, da pra usar o `for` direto numa
string). Voce so precisa preencher o miolo do laco e o retorno.
'''
def conta_letras(palavra):
    contador = {}
    for letra in palavra:
        if letra not in contador:
            contador[letra] = 1
        else:
            contador[letra] = contador[letra] + 1
    return contador
        

assert conta_letras('banana') == {'b': 1, 'a': 3, 'n': 2}, 'conta_letras("banana") eh {"b":1,"a":3,"n":2}'
assert conta_letras('arara') == {'a': 3, 'r': 2}, 'conta_letras("arara") eh {"a":3,"r":2}'
assert conta_letras('') == {}, 'conta_letras("") eh {} (palavra vazia -> dict vazio)'
assert conta_letras('z') == {'z': 1}, 'conta_letras("z") eh {"z":1} (uma letra so)'
assert conta_letras('aaaaabbbccccccccccaa') == {'a': 7, 'b': 3, 'c': 10}, 'conta_letras com repeticao pesada'
print('Exercicio conta_letras: OK')


# ===== FASE 6 - Simulacao integrada: Mirtes e Cicero =====

'''
EXPLICACAO

Vamos montar as agendas de duas pessoas - Mirtes e Cicero - usando as
funcoes que voce escreveu. Repare como a MESMA funcao (adiciona, consulta,
esta_na_agenda) serve as duas agendas: basta chamar com argumentos
diferentes. E como adiciona MUTA a agenda, nao tem reatribuicao.
'''

agenda_mirtes = {}
agenda_cicero = {}

adiciona(agenda_mirtes, 'ana', 1111)
adiciona(agenda_mirtes, 'bruno', 2222)
adiciona(agenda_cicero, 'ana', 5555)   # mesma "ana", agenda diferente -> nao se mistura

'''
EXERCICIO

Antes de rodar as consultas, PREVEJA os valores abaixo.

1) Quantas pessoas tem na agenda_mirtes?
2) 'bruno' esta na agenda_cicero?            (True/False)
3) Qual o telefone da ana na agenda_mirtes?
4) Qual o telefone da ana na agenda_cicero?  (sao agendas separadas!)
'''
quantas_mirtes_previsto = len(agenda_mirtes)
tem_bruno_na_cicero_previsto = 'bruno' in agenda_cicero
tel_ana_mirtes_previsto = agenda_mirtes['ana']
tel_ana_cicero_previsto = agenda_cicero['ana']

assert verifica(quantas_mirtes_previsto, '3159f99c23f2a870d627ce2f9587ed1ede531676519c53d6c512cd4d', nome_questao='quantas_mirtes_previsto'), 'quantas_mirtes_previsto incorreta'
assert verifica(tem_bruno_na_cicero_previsto, '036057d77a4b13933a85990e16e46f7270241da4982b2a16556a3738', nome_questao='tem_bruno_na_cicero_previsto'), 'tem_bruno_na_cicero_previsto incorreta'
assert verifica(tel_ana_mirtes_previsto, '56b003bdc84fb30a71129721e30072ee1d6f49ad3f8ca194f9c3ea11', nome_questao='tel_ana_mirtes_previsto'), 'tel_ana_mirtes_previsto incorreta'
assert verifica(tel_ana_cicero_previsto, 'e1c6a616cb618bd1d5ed3428a6aa13b95405c0353a326f71dd170211', nome_questao='tel_ana_cicero_previsto'), 'tel_ana_cicero_previsto incorreta'
print('Exercicio previsao Mirtes e Cicero: OK')

# agora as funcoes confirmam a sua previsao
assert len(agenda_mirtes.keys()) == 2, 'agenda_mirtes deveria ter 2 pessoas'
assert esta_na_agenda(agenda_cicero, 'bruno') == False, 'bruno nao esta na agenda do Cicero'
assert consulta(agenda_mirtes, 'ana') == 1111, 'ana na agenda da Mirtes eh 1111'
assert consulta(agenda_cicero, 'ana') == 5555, 'ana na agenda do Cicero eh 5555 (agendas separadas)'

print('Exercicio simulacao Mirtes e Cicero: OK')


print('\n=== PARABENS! Todos os exercicios completos! ===')


# ===== FASE 7 - INTERFACE CLI (se nao terminar, faca em casa) =====
#
# Menu pra usar a agenda. Para rodar, descomente a linha "main()" no final.
#
# Aqui o menu tambem eh exercicio: em vez de receber o if/elif pronto, cada
# opcao da Mirtes vem com uma DESCRICAO do que deve fazer e as PECAS soltas (os
# input(...), print(...) e as chamadas de funcao). Voce organiza as pecas na
# ordem certa. As opcoes do Cicero ficam como [implementar] - copie a logica das
# da Mirtes depois.



def main():
    agenda_mirtes = {}
    agenda_cicero = {}

    while True:
        print()
        print("=== AGENDA ===")
        print(f"agenda Mirtes: {agenda_mirtes}")
        print(f"agenda Cicero: {agenda_cicero}")
        print("1. Mirtes adiciona contato")
        print("2. Mirtes consulta telefone")
        print("3. Cicero adiciona contato")
        print("4. Cicero consulta telefone")
        print("5. Sair")
        opcao = input("Opcao: ")

        if opcao == "1":
            escolha = input('quem voce ira adicionar?')
            telefono = input('telefone da pessoa')
            adiciona(agenda_mirtes,escolha,telefono)

        elif opcao == "2":
           pessoa_escolhida = input('quem voce quer consultar?')
           consulta(agenda_mirtes,pessoa_escolhida)

        elif opcao == "3":
            escolha2 = input('quem voce ira adicionar?')
            telefono2 = input('telefone da pessoa')
            adiciona(agenda_cicero,escolha2,telefono2)

        elif opcao == "4":
            pessoa_escolhida2 = input('quem voce quer consultar?')
            consulta(agenda_cicero,pessoa_escolhida2)
           
        elif opcao == "5":
            break
        else:
            print("Opcao invalida")


# Para rodar a interface, descomente:
main()


# ===== FASE 8 - DESAFIO (opcional) =====

'''
EXPLICACAO

Voce ja terminou a lista - daqui pra baixo eh desafio, e eh opcional.

Sao tres coisas novas que a agenda ainda nao sabe fazer: TIRAR uma pessoa,
RENOMEAR uma pessoa, e procurar do lado dos TELEFONES em vez do lado das
pessoas.

Os asserts da Fase 8 ficam DESLIGADOS por padrao. Para ligar (e ver "OK"
conforme acerta), mude a flag `desafio` abaixo de False para True. Se nao
quiser fazer o desafio, deixe False e o arquivo continua terminando no
PARABENS.
'''


desafio = True   # ligue o desafio mudando para True


# ----- Sessao 1 - remove -----

'''
EXPLICACAO

Ate agora a agenda so cresceu. Para TIRAR uma pessoa existe o comando `del`:

    agenda = {'marcos': 32112232, 'fabio': 988887788}
    del agenda['fabio']
    # agora agenda eh {'marcos': 32112232}

O `del` apaga a chave E o valor dela, de uma vez. E ele MUTA a agenda, igual
ao `adiciona` - nao precisa reatribuir nada.

Cuidado: `del agenda['zeca']` numa agenda que nao tem o zeca da KeyError,
pelo mesmo motivo que ler `agenda['zeca']` daria.
'''

'''
EXERCICIO

Calculo a mao. Considere:

    agenda_d = {'marcos': 32112232, 'fabio': 988887788, 'maria': 44554455}
    del agenda_d['fabio']

Depois desse del:

1) Quantas pessoas a agenda_d tem?
2) 'fabio' ainda esta na agenda_d?   (True/False)
'''
quantas_apos_remover = 2
fabio_apos_remover = False

'''
EXERCICIO

Faca a funcao remove(agenda, pessoa) que tira a pessoa da agenda. A funcao
NAO retorna nada - ela muta a agenda que veio por parametro (igual ao
adiciona). Pode assumir que a pessoa ESTA na agenda.

    >>> agenda = {'ana': 111, 'bia': 222}
    >>> remove(agenda, 'ana')
    >>> agenda
    {'bia': 222}
'''
def remove(agendaaa, pessoa):
    del agendaaa[pessoa]



assert verifica(quantas_apos_remover, '9d8aaa3cf20484f3a5e0d4f25a935bc5883fffd5da5e1672de24dbcb', nome_questao='quantas_apos_remover'), 'quantas_apos_remover incorreta'
assert verifica(fabio_apos_remover, 'c764213d521bbd8f0a64deeb61f958d1371305e34a4815a5deca9d42', nome_questao='fabio_apos_remover'), 'fabio_apos_remover incorreta'

    # 1: tirar uma de tres - as outras duas ficam intactas
agenda_d1 = {'marcos': 32112232, 'fabio': 988887788, 'maria': 44554455}
remove(agenda_d1, 'fabio')
assert agenda_d1 == {'marcos': 32112232, 'maria': 44554455}, f'apos remover fabio: {agenda_d1}'
assert len(agenda_d1.keys()) == 2, 'depois de remover, a agenda tem 2 chaves'
assert esta_na_agenda(agenda_d1, 'fabio') == False, 'fabio nao esta mais na agenda'

    # 2: tirar a ultima - a agenda fica vazia
agenda_d2 = {'ana': 111}
remove(agenda_d2, 'ana')
assert agenda_d2 == {}, f'ao remover a ultima pessoa a agenda fica vazia: {agenda_d2}'

    # 3: a funcao MUTA (nao adianta reatribuir) - o retorno eh None
agenda_d3 = {'ana': 111, 'bia': 222}
assert remove(agenda_d3, 'ana') is None, 'remove nao retorna nada - ela muta a agenda'
assert agenda_d3 == {'bia': 222}, 'mesmo sem reatribuir, a agenda mudou'

    # 4: remover e adicionar de novo - a chave volta
adiciona(agenda_d3, 'ana', 999)
assert agenda_d3 == {'bia': 222, 'ana': 999}, 'depois de remover da pra adicionar de novo'

print('Desafio Sessao 1 (remove): OK')


# ----- Sessao 2 - renomeia -----

'''
EXPLICACAO

A ana casou e agora quer ser chamada de aninha. O telefone eh o mesmo - o
que muda eh a CHAVE.

Aqui vem a pegadinha: chave nao se edita. Nao existe "trocar o nome da
chave" em Python. O que existe eh:

    1. guardar o valor que esta na chave antiga
    2. criar a chave nova com esse valor
    3. apagar a chave antiga

A ORDEM importa: se voce apagar a chave antiga antes de guardar o valor,
perdeu o telefone e nao tem como recuperar.
'''

'''
EXERCICIO

Calculo a mao. Considere:

    agenda_r = {'ana': 111, 'bia': 222}
    renomeia(agenda_r, 'ana', 'aninha')

Depois de renomear:

1) Quanto vale agenda_r['aninha']?
2) 'ana' ainda eh uma chave da agenda_r?   (True/False)
3) Quantas pessoas a agenda_r tem agora?
'''
tel_da_aninha = 111
ana_ainda_existe = False
quantas_apos_renomear = 2

'''
EXERCICIO

Faca a funcao renomeia(agenda, antigo, novo) que troca a chave `antigo` pela
chave `novo`, mantendo o telefone. Muta a agenda; nao retorna nada. Pode
assumir que `antigo` esta na agenda.

    >>> agenda = {'ana': 111, 'bia': 222}
    >>> renomeia(agenda, 'ana', 'aninha')
    >>> agenda
    {'bia': 222, 'aninha': 111}

Dica: os tres passos da explicacao acima, nessa ordem. As duas funcoes que
voce ja tem (adiciona e remove) fazem os passos 2 e 3.
'''
def renomeia(agendaa, antigo, novo):
    antiguidade = agendaa[antigo]
    agendaa[novo] = antiguidade
    remove(agendaa, antigo)


if desafio:
    assert verifica(tel_da_aninha, '384702f02eb0fde8879b1cdc3ff67b105e0a2910d041fb70878ac835', nome_questao='tel_da_aninha'), 'tel_da_aninha incorreta'
    assert verifica(ana_ainda_existe, '7dbcebbece8eb22005a19d705f855863051ef1b17d810bcac99846b8', nome_questao='ana_ainda_existe'), 'ana_ainda_existe incorreta'
    assert verifica(quantas_apos_renomear, 'd334e1939a5acc533ecd19897b5d338686423288afc9efa553c32bb3', nome_questao='quantas_apos_renomear'), 'quantas_apos_renomear incorreta'

    # 1: o telefone acompanha o nome novo, e o nome antigo some
    agenda_r1 = {'ana': 111, 'bia': 222}
    renomeia(agenda_r1, 'ana', 'aninha')
    assert consulta(agenda_r1, 'aninha') == 111, 'o telefone tem que acompanhar o nome novo'
    assert esta_na_agenda(agenda_r1, 'ana') == False, 'a chave antiga tem que sumir'

    # 2: renomear NAO muda o tamanho (nao eh adicionar)
    assert len(agenda_r1.keys()) == 2, 'renomear nao muda quantas pessoas a agenda tem'

    # 3: as outras pessoas ficam intactas
    assert agenda_r1 == {'bia': 222, 'aninha': 111}, f'a bia nao devia ter mudado: {agenda_r1}'

    # 4: renomear a unica pessoa da agenda
    agenda_r2 = {'ana': 111}
    renomeia(agenda_r2, 'ana', 'aninha')
    assert agenda_r2 == {'aninha': 111}, f'renomeando a unica pessoa: {agenda_r2}'

    print('Desafio Sessao 2 (renomeia): OK')


# ----- Sessao 3 - telefone_existe -----

'''
EXPLICACAO

Todas as perguntas ate agora foram do lado das CHAVES: `agenda.keys()` da as
pessoas, e `'fabio' in agenda.keys()` pergunta se o fabio esta la.

Mas da pra olhar do outro lado tambem. `agenda.values()` da os VALORES - os
telefones:

    agenda = {'marcos': 32112232, 'fabio': 988887788}
    agenda.values()                  # os telefones: 32112232 e 988887788
    32112232 in agenda.values()      # True - esse telefone esta guardado
    11111111 in agenda.values()      # False - esse nao

Repare que isso responde "esse telefone esta na agenda?" SEM voce precisar
saber de quem ele eh. Eh a pergunta que a questao acesso_valor da Fase 1
deixou em aberto: entre colchetes so vai CHAVE, entao nao dava pra procurar
um telefone com `agenda[44554455]`. Com `.values()`, da.
'''

'''
EXERCICIO

Considere:

    agenda_v = {'marcos': 32112232, 'fabio': 988887788, 'maria': 44554455}

Preencha usando uma EXPRESSAO Python (o dicionario agenda_v ja existe logo
abaixo, da pra usar ele de verdade).

1) O telefone 988887788 esta guardado em alguem?   (True/False)
2) E o telefone 11111111?                          (True/False)
'''
agenda_v = {'marcos': 32112232, 'fabio': 988887788, 'maria': 44554455}

tel_988887788_existe = 'coloque o valor aqui'
tel_11111111_existe = 'coloque o valor aqui'

'''
EXERCICIO

Faca a funcao telefone_existe(agenda, telefone) que retorna True se ALGUMA
pessoa da agenda tem esse telefone, e False caso contrario.

    >>> agenda = {'ana': 111, 'bia': 222}
    >>> telefone_existe(agenda, 222)
    True
    >>> telefone_existe(agenda, 999)
    False
'''
def telefone_existe(agenda, telefone):
    resposta = telefone in agenda.values()
    return resposta


if desafio:
    #assert verifica(tel_988887788_existe, '3ca423875d9625d9fbb0b1f37ae5731244e973e665d9e73749f82c10', nome_questao='tel_988887788_existe'), 'tel_988887788_existe incorreta'
    #assert verifica(tel_11111111_existe, 'a335a47dcaf1f6a2ffd8d548070aee4ecd4bdb09b4db50c2adb8f86c', nome_questao='tel_11111111_existe'), 'tel_11111111_existe incorreta'

    agenda_v1 = {'ana': 111, 'bia': 222, 'davi': 333}
    # 1: telefone que existe (o primeiro, um do meio e o ultimo)
    assert telefone_existe(agenda_v1, 111) == True, 'o 111 esta na agenda (eh o telefone da ana)'
    assert telefone_existe(agenda_v1, 222) == True, 'o 222 esta na agenda (eh o telefone da bia)'
    assert telefone_existe(agenda_v1, 333) == True, 'o 333 esta na agenda (eh o telefone do davi)'

    # 2: telefone que nao existe
    assert telefone_existe(agenda_v1, 999) == False, 'o 999 nao eh telefone de ninguem'

    # 3: agenda vazia - nao tem telefone nenhum
    assert telefone_existe({}, 111) == False, 'numa agenda vazia nenhum telefone existe'

    # 4: mesmo telefone em duas pessoas (o telefone da casa) - continua True
    agenda_v2 = {'ana': 111, 'bia': 111}
    assert telefone_existe(agenda_v2, 111) == True, 'o mesmo telefone em duas pessoas continua existindo'

    # 5: procurar do lado ERRADO - um NOME nao eh telefone de ninguem
    assert telefone_existe(agenda_v1, 'ana') == False, "'ana' eh CHAVE, nao valor - procurando entre os valores nao aparece"

    print('Desafio Sessao 3 (telefone_existe): OK')

    print('\n=== DESAFIO COMPLETO! ===')
