
# === Helper de verificacao (pode ignorar) ===
# A funcao `verifica` compara o seu valor com a resposta correta (que
# fica escondida em formato de hash). Voce nao precisa entender ela -
# se voce errou, ela imprime "Valor errado: voce colocou X" e o assert
# logo abaixo dispara.
import hashlib
def verifica(valor, codigo):
    valores = [valor]
    if isinstance(valor, list):
        valores = [sorted(valor)]
    elif isinstance(valor, int) and not isinstance(valor, bool):
        valores.append(float(valor))
    elif isinstance(valor, float):
        valores.append(int(valor))
    respostas = [hashlib.sha224(str(valor).encode('utf-8')).hexdigest() == codigo for valor in valores]
    if not any(respostas):
        print(f'Valor errado: voce colocou "{valor}" na variavel')
        return False
    return True
# fim do helper


'''
EXPLICACAO

Bem-vindo ao exercicio Steam! Vamos modelar uma plataforma de jogos
com dois usuarios - Heloisa e Lucas - cada um com sua biblioteca (a
lista de jogos que comprou) e seu computador (com specs diferentes).

NOVIDADE: a maioria das funcoes desse exercicio usa LOOPS ANINHADOS
(for dentro de for). Pra fechar contas como "quanto a Heloisa gastou
no total" voce precisa, pra cada jogo da biblioteca dela, achar o
preco no catalogo - dois loops, um dentro do outro.

ESTRUTURAS

CATALOGO: lista global dos jogos que existem na loja. Cada jogo eh
uma lista de 4 elementos:

    [nome, preco, genero, [ram_min, vram_min, ano_processador_min]]

Por exemplo:

    ["counter-strike", 30, "fps", [4, 1, 2010]]

Repare que o ultimo elemento eh ELE MESMO uma lista de 3 numeros
(as specs minimas de hardware do jogo).

BIBLIOTECA: lista de strings, com os NOMES dos jogos que a pessoa
comprou. Pra saber o preco, genero ou specs de qualquer jogo, voce
PRECISA consultar o catalogo.

    biblioteca_heloisa = ["counter-strike", "the witcher"]

PC: lista de 3 numeros [ram, vram, ano_processador] descrevendo o
computador do usuario. Um jogo roda no PC se as 3 specs do PC sao
maiores ou iguais aas specs minimas do jogo.

    pc_heloisa = [8, 2, 2018]   # 8gb ram, 2gb vram, processador de 2018
'''


# ===== FASE 1 - Aquecimento: lendo o catalogo =====

catalogo = [
    ["counter-strike", 30,  "fps",          [4,  1, 2010]],
    ["civilization",   50,  "estrategia",   [8,  2, 2015]],
    ["the witcher",    80,  "rpg",          [12, 4, 2018]],
    ["minecraft",      25,  "sandbox",      [4,  1, 2012]],
    ["cyberpunk",      100, "rpg",          [16, 6, 2020]],
    ["hollow knight",  40,  "metroidvania", [4,  1, 2012]],
]

'''
EXERCICIO

Considere o catalogo acima.

Preencha as variaveis usando uma EXPRESSAO Python que produz o valor
(em vez de escrever o valor literal direto).

Lembre que catalogo[0] eh a lista do primeiro jogo
(["counter-strike", 30, "fps", [4, 1, 2010]]). E catalogo[0][0] eh so
a string "counter-strike".

Se nao conseguir, pode comecar escrevendo o valor pra ver o teste
passar, mas depois tente escrever a expressao.

1) Qual o nome do primeiro jogo do catalogo? (string)

   Dica: catalogo[0][0] - o primeiro [0] pega a lista do primeiro
   jogo, o segundo [0] pega o primeiro elemento dessa lista (o nome).
'''
nome_do_primeiro = catalogo[0][0]

'''
2) Qual o preco do segundo jogo? (numero)
'''
preco_do_segundo = catalogo[1][1]

'''
3) Qual o genero do terceiro jogo? (string)
'''
genero_do_terceiro = catalogo[2][2]

'''
4) Quantos GB de RAM o segundo jogo (civilization) pede no minimo? (numero)

   Dica: aqui precisa de TRES indices. O primeiro pega a lista do
   jogo no catalogo (catalogo[1]); o segundo pega a lista de specs
   dentro dele (catalogo[1][3]); o terceiro pega o primeiro numero
   dessa lista (catalogo[1][3][0]).
'''
ram_min_do_segundo = catalogo[1][3][0]

'''
5) Quantos GB de VRAM o quarto jogo (minecraft) pede no minimo? (numero)
'''
vram_min_do_quarto = catalogo[3][3][1]

'''
6) Qual o ano minimo de processador do quinto jogo (cyberpunk)? (numero)
'''
ano_min_do_quinto = catalogo[4][3][2]

assert verifica(nome_do_primeiro, 'd3d8c48e727a7b51be150011b5e687145f5ae9b6e3cb811a06554b82'), 'nome_do_primeiro incorreto'
assert verifica(preco_do_segundo, 'f6c43c243da7289c9ecdbf36cabf9c14d55afe6ef8904d9e6ec56945'), 'preco_do_segundo incorreto'
assert verifica(genero_do_terceiro, 'f0b640bff3754b3d8980ba481689c542ed29bc80b78ddcdae2bc05f5'), 'genero_do_terceiro incorreto'
assert verifica(ram_min_do_segundo, '525ab75c928c6fac98a0f62e4da5316b7247ccd704c967ef9142925c'), 'ram_min_do_segundo incorreto'
assert verifica(vram_min_do_quarto, 'e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178'), 'vram_min_do_quarto incorreto'
assert verifica(ano_min_do_quinto, 'b86d4006e465f5ef74e4438b0cb802605e5c7993ac0002a876149c70'), 'ano_min_do_quinto incorreto'
print('Exercicio lendo o catalogo: OK')


# ===== FASE 2 - Calculo a mao =====

'''
EXERCICIO

Calculo a mao. Considere o mesmo catalogo, com as bibliotecas:

    biblioteca_heloisa = ["counter-strike", "the witcher"]
    biblioteca_lucas   = ["civilization", "counter-strike", "minecraft"]

Pra cada nome na biblioteca, voce vai no catalogo, acha o jogo
correspondente, e pega o preco.

1) Quanto a Heloisa gastou no total? (numero)
'''
gasto_heloisa_a_mao = 110

'''
2) Quanto o Lucas gastou no total? (numero)
'''
gasto_lucas_a_mao = 105

'''
3) PC da Heloisa: [8, 2, 2018]. Pra cada jogo da biblioteca dela,
   olhe as specs no catalogo e compare com o PC:

       - counter-strike pede [4, 1, 2010]: 8>=4, 2>=1, 2018>=2010 -> roda
       - the witcher  pede [12, 4, 2018]: 8 NAO eh >= 12 -> NAO roda

   Quais jogos da biblioteca dela rodam no PC dela?
   (responda com uma lista de strings - ex: ["counter-strike"])
'''
jogos_que_rodam_heloisa_a_mao = ['counter-strike']

assert verifica(gasto_heloisa_a_mao, '99d068d846a04c8a18b57e60f88e62e1b9796389607593ea5086b4a3'), 'gasto_heloisa_a_mao incorreto'
assert verifica(gasto_lucas_a_mao, '6f17c8e6d3ccc5beb34089e2cb28b549845a394250cafc588c179ef0'), 'gasto_lucas_a_mao incorreto'
assert verifica(jogos_que_rodam_heloisa_a_mao, '374840c6a733f5ca00925d06745e6716b6f7f86b1b6c7eaa2c9393d0'), 'jogos_que_rodam_heloisa_a_mao incorreto'
print('Exercicio calculo a mao: OK')


# ===== FASE 3 - preco_de (loop simples) =====

'''
EXERCICIO

Antes do aninhado, uma funcao simples (com 1 loop so) que vai servir
de aquecimento.

Faca a funcao preco_de(nome, catalogo) que percorre o catalogo
procurando pelo nome do jogo, e retorna o preco.

Dica: use um for. Pra cada jogo no catalogo, se jogo[0] == nome,
retorne jogo[1] (o preco).

Voce pode assumir que o jogo esta cadastrado.

    >>> preco_de("the witcher", catalogo)
    80
    >>> preco_de("minecraft", catalogo)
    25
'''
def preco_de(nome, catalogo):
    i = 0
    for jogo in catalogo:
        if jogo[0] == nome:
            return jogo[1]
        else:
            i = i + 1
        

assert preco_de("counter-strike", catalogo) == 30, 'preco_de("counter-strike") deveria ser 30'
assert preco_de("the witcher", catalogo) == 80, 'preco_de("the witcher") deveria ser 80'
assert preco_de("minecraft", catalogo) == 25, 'preco_de("minecraft") deveria ser 25'
assert preco_de("hollow knight", catalogo) == 40, 'preco_de("hollow knight") deveria ser 40'

print('Exercicio preco_de: OK')


# ===== FASE 4 - gasto_total (LOOP ANINHADO #1) =====

'''
EXPLICACAO

Agora vem o conceito principal: LOOP ANINHADO (um for dentro de outro
for).

Pra calcular o gasto total da Heloisa, voce tem:

    biblioteca_heloisa = ["counter-strike", "the witcher"]

Pra cada NOME da biblioteca dela (loop externo), voce precisa achar
o JOGO no catalogo (loop interno) e pegar o preco:

    for nome in biblioteca_heloisa:    # 2 iteracoes
        for jogo in catalogo:          # 6 iteracoes
            if jogo[0] == nome:
                # achou - pega o preco

No total, sao 2 x 6 = 12 passos do interpretador (o for interno roda
uma vez completa pra cada item do externo). Isso eh o "for dentro de
for" funcionando.

OBSERVACAO: voce poderia chamar preco_de(nome, catalogo) dentro do
loop externo e fazer a mesma coisa sem precisar escrever o for
interno. Funciona - mas o for interno fica escondido dentro do
preco_de. Pra voce VER o for-dentro-de-for de cara, vamos escrever sem chamar a 
funcao.
'''


'''
EXERCICIO

Faca a funcao gasto_total(biblioteca, catalogo) que retorna o gasto
total de uma biblioteca - a soma dos precos de todos os jogos nela.

Dica: comece com `total = 0`. Use dois fors aninhados como na
explicacao acima. Quando achar o jogo no catalogo (jogo[0] == nome),
some jogo[1] no total. No fim, retorne total.

    >>> gasto_total(["counter-strike", "the witcher"], catalogo)
    110
    >>> gasto_total(["civilization", "counter-strike", "minecraft"], catalogo)
    105
    >>> gasto_total([], catalogo)
    0
'''
def gasto_total(biblioteca, catalogo):
    total = 0
    for nome in biblioteca:
       total = total + preco_de(nome,catalogo)
    return total

assert gasto_total(["counter-strike", "the witcher"], catalogo) == 110, 'gasto_total da Heloisa deveria ser 110'
assert gasto_total(["civilization", "counter-strike", "minecraft"], catalogo) == 105, 'gasto_total do Lucas deveria ser 105'
assert gasto_total([], catalogo) == 0, 'gasto_total de biblioteca vazia deveria ser 0'
assert gasto_total(["hollow knight"], catalogo) == 40, 'gasto_total com 1 jogo'
assert gasto_total(["hollow knight", "hollow knight"], catalogo) == 80, 'comprou o mesmo jogo 2x: paga 2x'

print('Exercicio gasto_total: OK')


# ===== FASE 5 - roda_no_pc (helper sem aninhado) =====

'''
EXERCICIO

Helper sem aninhado pra reusarmos depois.

Faca a funcao roda_no_pc(specs, pc) que recebe duas listas de 3
elementos (ram, vram, ano_processador), e retorna True se o PC roda
o jogo - ou seja, se o PC tem >= em TODAS as 3 specs.

    specs = [4, 1, 2010]  # specs minimas do jogo
    pc    = [8, 2, 2018]  # PC do usuario
    -> roda (8>=4, 2>=1, 2018>=2010)

    specs = [12, 4, 2018]
    pc    = [8, 2, 2018]
    -> nao roda (8 NAO eh >= 12)

Dica: use `and` pra combinar as 3 comparacoes em uma so expressao.

    >>> roda_no_pc([4, 1, 2010], [8, 2, 2018])
    True
    >>> roda_no_pc([12, 4, 2018], [8, 2, 2018])
    False
    >>> roda_no_pc([8, 2, 2018], [8, 2, 2018])
    True   (igual eh OK)
'''
def roda_no_pc(specs, pc):
    for i in range(3): #[0,1,2] == range(3)
        if pc[i] < specs[i]:
            return False
    return True



assert roda_no_pc([4, 1, 2010], [8, 2, 2018]) == True, 'PC potente roda jogo fraco'
assert roda_no_pc([12, 4, 2018], [8, 2, 2018]) == False, 'nao roda por RAM'
assert roda_no_pc([4, 8, 2018], [8, 2, 2018]) == False, 'nao roda por VRAM'
assert roda_no_pc([4, 1, 2025], [8, 2, 2018]) == False, 'nao roda por ANO de processador'
assert roda_no_pc([8, 2, 2018], [8, 2, 2018]) == True, 'specs exatamente iguais: roda'

print('Exercicio roda_no_pc: OK')


# ===== FASE 6 - biblioteca_filtrada (LOOP ANINHADO #2) =====

'''
EXERCICIO

Faca a funcao biblioteca_filtrada(biblioteca, catalogo, pc) que
retorna uma lista com os nomes dos jogos da biblioteca QUE RODAM
no PC.

Vai usar a mesma estrutura do gasto_total - for nome (externo), for
jogo (interno) pra achar no catalogo. So que agora, em vez de somar
o preco, voce usa roda_no_pc(jogo[3], pc) pra decidir se o nome
entra na lista de retorno.

Lembre: jogo[3] eh a lista de specs minimas [ram, vram, ano].

Dica: comece com `rodam = []`. Quando achar o jogo no catalogo E ele
rodar no PC, faca rodam.append(nome). No fim, retorne rodam.

    >>> bib = ["counter-strike", "the witcher"]
    >>> pc  = [8, 2, 2018]
    >>> biblioteca_filtrada(bib, catalogo, pc)
    ["counter-strike"]
    (the witcher pede 12gb de RAM, a Heloisa so tem 8)

    >>> bib = ["civilization", "counter-strike", "minecraft"]
    >>> pc  = [16, 8, 2022]
    >>> biblioteca_filtrada(bib, catalogo, pc)
    ["civilization", "counter-strike", "minecraft"]
    (PC potente, tudo roda)

    >>> biblioteca_filtrada(bib, catalogo, [1, 1, 2000])
    []
    (PC fraquissimo, nao roda nada)
'''
def biblioteca_filtrada(biblioteca, catalogo, pc):
    rodam = []
    for nome in biblioteca:
        for jogo in catalogo:
            if jogo[0] == nome:
                if roda_no_pc(jogo[3], pc):
                    rodam.append(nome)
    return rodam
    

assert biblioteca_filtrada(["counter-strike", "the witcher"], catalogo, [8, 2, 2018]) == ["counter-strike"], 'Heloisa: so counter-strike roda'
assert biblioteca_filtrada(["civilization", "counter-strike", "minecraft"], catalogo, [16, 8, 2022]) == ["civilization", "counter-strike", "minecraft"], 'Lucas: tudo roda'
assert biblioteca_filtrada(["civilization", "counter-strike", "minecraft"], catalogo, [1, 1, 2000]) == [], 'PC fraquissimo: nada roda'
assert biblioteca_filtrada([], catalogo, [16, 8, 2022]) == [], 'biblioteca vazia: lista vazia'

print('Exercicio biblioteca_filtrada: OK')


# ===== CHECKPOINT - CLI parcial =====

'''
CHECKPOINT

Com o que voce ja fez (preco_de, gasto_total, roda_no_pc,
biblioteca_filtrada) ja da pra montar um menu funcional do Steam.

Se voce tiver chego no fim da aula ou quiser uma pausa, pare aqui:
o resto eh extra.

Pra rodar o menu, descomente `main_parcial()` no final do bloco
abaixo. Algumas opcoes (Lucas) estao marcadas como [implementar] -
sao espelho das opcoes da Heloisa, pra voce completar.
'''

def main_parcial():
    pc_heloisa = [8, 2, 2018]
    pc_lucas   = [16, 8, 2022]
    biblioteca_heloisa = ["counter-strike", "the witcher"]
    biblioteca_lucas   = ["civilization", "counter-strike", "minecraft"]

    while True:
        print()
        print("=== STEAM (parcial) ===")
        print(f"Heloisa: {biblioteca_heloisa} | PC {pc_heloisa}")
        print(f"Lucas:   {biblioteca_lucas} | PC {pc_lucas}")
        print("1. Heloisa compra jogo")
        print("2. Heloisa: ver gasto total")
        print("3. Heloisa: ver jogos que rodam no PC dela")
        print("4. Lucas compra jogo")
        print("5. Lucas: ver gasto total")
        print("6. Lucas: ver jogos que rodam no PC dele")
        print("7. Sair")
        opcao = input("Opcao: ")

        if opcao == "1":
            nome = input("  Nome do jogo: ")
            biblioteca_heloisa.append(nome)
        elif opcao == "2":
            print(f"  Gasto total Heloisa: {gasto_total(biblioteca_heloisa, catalogo)}")
        elif opcao == "3":
            print(f"  Rodam no PC da Heloisa: {biblioteca_filtrada(biblioteca_heloisa, catalogo, pc_heloisa)}")
        elif opcao == "4":
            print("  [implementar: igual a opcao 1, mas pra Lucas]")
        elif opcao == "5":
            print("  [implementar: igual a opcao 2, mas pra Lucas]")
        elif opcao == "6":
            print("  [implementar: igual a opcao 3, mas pra Lucas]")
        elif opcao == "7":
            break
        else:
            print("Opcao invalida")


# Pra rodar o menu parcial, descomente:
# main_parcial()

# se quiser melhorar esse menu, podemos pensar em login
# duas opcoes para escolher o usuario (lucas ou heloisa)
# e ao as ṕcpes "comprar", "gasto total" e "jogos que rodam" atuam
# para o usuario *logado*

# ===== FASE 7 - jogos_em_comum (LOOP ANINHADO #3, puro) =====

'''
EXERCICIO

Agora um aninhado SEM catalogo no meio - vai ser bem direto.

Faca a funcao jogos_em_comum(bib1, bib2) que retorna uma lista com
os nomes que aparecem nas DUAS bibliotecas.

Pra cada nome da bib1 (loop externo), percorra a bib2 (loop interno)
procurando o mesmo nome. Se achar, append na lista de retorno.

OBSERVACAO: voce poderia escrever `if jogo1 in bib2` em vez do loop
interno - eh a mesma coisa! O `in` esconde um loop como o que voce ta
escrevendo aqui. Como a gente esta praticando aninhado, vamos
escrever os dois fors explicitamente.

    >>> jogos_em_comum(["counter-strike", "the witcher"], ["civilization", "counter-strike"])
    ["counter-strike"]
    >>> jogos_em_comum(["a", "b", "c"], ["c", "b", "a"])
    ["a", "b", "c"]
    >>> jogos_em_comum(["a"], ["b"])
    []
    >>> jogos_em_comum([], ["a", "b"])
    []
'''
def jogos_em_comum(bib1, bib2):
    pass

assert jogos_em_comum(["counter-strike", "the witcher"], ["civilization", "counter-strike"]) == ["counter-strike"], 'em comum: counter-strike'
assert jogos_em_comum(["a", "b", "c"], ["c", "b", "a"]) == ["a", "b", "c"], 'todos em comum (ordem de bib1)'
assert jogos_em_comum(["a"], ["b"]) == [], 'nada em comum'
assert jogos_em_comum([], ["a", "b"]) == [], 'bib1 vazia'
assert jogos_em_comum(["a", "b"], []) == [], 'bib2 vazia'

print('Exercicio jogos_em_comum: OK')


# ===== FASE 8 - Simulacao Heloisa e Lucas =====

biblioteca_heloisa = ["counter-strike", "the witcher"]
biblioteca_lucas   = ["civilization", "counter-strike", "minecraft"]
pc_heloisa = [8, 2, 2018]
pc_lucas   = [16, 8, 2022]

'''
EXERCICIO

Antes de rodar as funcoes, PREVEJA os valores. Estado:

    catalogo (definido la em cima)
    biblioteca_heloisa = ["counter-strike", "the witcher"]
    biblioteca_lucas   = ["civilization", "counter-strike", "minecraft"]
    pc_heloisa = [8, 2, 2018]
    pc_lucas   = [16, 8, 2022]

1) Gasto total da casa toda (Heloisa + Lucas)?
'''
gasto_total_casa_previsto = 'coloque o valor aqui'

'''
2) Quantos jogos rodam no PC da Heloisa? (so o numero, nao a lista)
'''
quantos_rodam_para_heloisa_previsto = 'coloque o valor aqui'

'''
3) Quantos jogos rodam no PC do Lucas?
'''
quantos_rodam_para_lucas_previsto = 'coloque o valor aqui'

'''
4) Quantos jogos eles tem em COMUM?
'''
quantos_jogos_em_comum_previsto = 'coloque o valor aqui'

assert verifica(gasto_total_casa_previsto, '3bc5d385c4bc5447c4dbd13c23022da5e59c53c406b9adda0121868d'), 'gasto_total_casa_previsto incorreto'
assert verifica(quantos_rodam_para_heloisa_previsto, 'e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178'), 'quantos_rodam_para_heloisa_previsto incorreto'
assert verifica(quantos_rodam_para_lucas_previsto, '4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474'), 'quantos_rodam_para_lucas_previsto incorreto'
assert verifica(quantos_jogos_em_comum_previsto, 'e25388fde8290dc286a6164fa2d97e551b53498dcbf7bc378eb1f178'), 'quantos_jogos_em_comum_previsto incorreto'
print('Exercicio previsao da simulacao: OK')

# Agora roda as funcoes e confirma:
gasto_casa = gasto_total(biblioteca_heloisa, catalogo) + gasto_total(biblioteca_lucas, catalogo)
assert gasto_casa == gasto_total_casa_previsto, f'gasto da casa: previsao={gasto_total_casa_previsto}, funcoes deram {gasto_casa}'

rodam_heloisa = biblioteca_filtrada(biblioteca_heloisa, catalogo, pc_heloisa)
assert len(rodam_heloisa) == quantos_rodam_para_heloisa_previsto, f'rodam pra Heloisa: previsao={quantos_rodam_para_heloisa_previsto}, funcao deu {len(rodam_heloisa)}'

rodam_lucas = biblioteca_filtrada(biblioteca_lucas, catalogo, pc_lucas)
assert len(rodam_lucas) == quantos_rodam_para_lucas_previsto, f'rodam pro Lucas: previsao={quantos_rodam_para_lucas_previsto}, funcao deu {len(rodam_lucas)}'

comum = jogos_em_comum(biblioteca_heloisa, biblioteca_lucas)
assert len(comum) == quantos_jogos_em_comum_previsto, f'jogos em comum: previsao={quantos_jogos_em_comum_previsto}, funcao deu {len(comum)}'

print('Exercicio simulacao Heloisa e Lucas: OK')


print('\n=== PARABENS! Todos os exercicios principais completos! ===')


# ===== FASE 9 - DESAFIO (opcional): recomenda =====

'''
DESAFIO (opcional)

Faca a funcao recomenda(bib_amigo, minha_bib, catalogo, meu_pc) que
sugere jogos pra eu comprar. Pra cada jogo da biblioteca do amigo,
incluir na sugestao se:
    - eu AINDA NAO TENHO (`nome not in minha_bib`) E
    - o jogo RODA no meu PC

Eh um aninhado de 2 niveis (igual ao biblioteca_filtrada) mas com a
checagem `not in minha_bib` na frente, antes do loop interno.

    >>> bib_amigo = ["counter-strike", "the witcher", "civilization"]
    >>> minha_bib = ["counter-strike"]
    >>> meu_pc    = [8, 2, 2018]
    >>> recomenda(bib_amigo, minha_bib, catalogo, meu_pc)
    ["civilization"]
    # counter-strike: ja tenho - ignora
    # the witcher: nao tenho mas nao roda (precisa 12gb) - ignora
    # civilization: nao tenho e roda - SUGERE
'''
def recomenda(bib_amigo, minha_bib, catalogo, meu_pc):
    pass

# Se voce fez o desafio, descomente os asserts abaixo pra testar:
# assert recomenda(["counter-strike", "the witcher", "civilization"], ["counter-strike"], catalogo, [8, 2, 2018]) == ["civilization"], 'recomenda basica'
# assert recomenda(biblioteca_lucas, biblioteca_heloisa, catalogo, pc_heloisa) == ["civilization", "minecraft"], 'Lucas tem civilization e minecraft pra recomendar pra Heloisa'
# assert recomenda(biblioteca_heloisa, biblioteca_lucas, catalogo, pc_lucas) == ["the witcher"], 'Heloisa tem the witcher pra recomendar pro Lucas'
# print('Desafio recomenda: OK')


# ===== CLI COMPLETO (pra casa) =====
#
# Menu pra usar o sistema completo. Estende o main_parcial com a opcao
# "Ver jogos em comum". Pra rodar, descomente "main()" no final.

def main():
    pc_heloisa = [8, 2, 2018]
    pc_lucas   = [16, 8, 2022]
    biblioteca_heloisa = ["counter-strike", "the witcher"]
    biblioteca_lucas   = ["civilization", "counter-strike", "minecraft"]

    while True:
        print()
        print("=== STEAM ===")
        print(f"Heloisa: {biblioteca_heloisa} | PC {pc_heloisa}")
        print(f"Lucas:   {biblioteca_lucas} | PC {pc_lucas}")
        print("1. Heloisa compra jogo")
        print("2. Heloisa: ver gasto total")
        print("3. Heloisa: ver jogos que rodam no PC dela")
        print("4. Lucas compra jogo")
        print("5. Lucas: ver gasto total")
        print("6. Lucas: ver jogos que rodam no PC dele")
        print("7. Ver jogos em comum")
        print("8. Sair")
        opcao = input("Opcao: ")

        if opcao == "1":
            nome = input("  Nome do jogo: ")
            biblioteca_heloisa.append(nome)
        elif opcao == "2":
            print(f"  Gasto total Heloisa: {gasto_total(biblioteca_heloisa, catalogo)}")
        elif opcao == "3":
            print(f"  Rodam no PC da Heloisa: {biblioteca_filtrada(biblioteca_heloisa, catalogo, pc_heloisa)}")
        elif opcao == "4":
            print("  [implementar: igual a opcao 1, mas pra Lucas]")
        elif opcao == "5":
            print("  [implementar: igual a opcao 2, mas pra Lucas]")
        elif opcao == "6":
            print("  [implementar: igual a opcao 3, mas pra Lucas]")
        elif opcao == "7":
            print(f"  Jogos em comum: {jogos_em_comum(biblioteca_heloisa, biblioteca_lucas)}")
        elif opcao == "8":
            break
        else:
            print("Opcao invalida")


# Pra rodar o menu completo, descomente:
# main()
