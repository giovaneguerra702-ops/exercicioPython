# Exemplo 3 - lista de APIs (viagem): uma conta em varias moedas, com menu.

'''
ENUNCIADO

Faca um programa que controla uma CONTA EM VARIAS MOEDAS.

Por um menu, o usuario pode:

  1) DEPOSITAR: ele escolhe um valor e uma moeda, pelo codigo de 3 letras
     (BRL, EUR, USD, JPY, GBP, ...). Os depositos ficam guardados num
     dicionario, moeda -> quanto tem naquela moeda. Depositar duas vezes
     na mesma moeda soma:

         {'BRL': 1500, 'EUR': 10}      # 1500 reais e 10 euros

  2) PEDIR O SALDO TOTAL em qualquer moeda que ele escolher. Cada moeda da
     conta eh convertida pra moeda pedida com a cotacao de hoje (que vem
     do Frankfurter, a API de cambio da lista), e as partes sao somadas.

  3) SAIR.

Regras:

  - um codigo de moeda que o Frankfurter nao conhece eh recusado na hora,
    e nao vai parar na conta;
  - o saldo total sai arredondado em 2 casas, como dinheiro;
  - uma moeda convertida nela mesma vale 1 (1 euro eh 1 euro), e isso
    nao se pergunta a API.
'''

# Conceitos: um dicionario como o ESTADO do programa (a conta); funcoes
# que recebem esse dicionario por parametro e o modificam (deposito) ou
# so leem (saldo); o par funcao PURA / irma da API, que eh a espinha da
# lista; a API chamada dentro de um laco (uma cotacao por moeda da
# conta); e um menu que repete ate o usuario sair.
#
# Diferente dos outros dois exemplinhos, este esta comentado passo a
# passo - eh pra ser lido, nao so mostrado.
#
# O arquivo, em ordem:
#   1. a conta e o deposito
#   2. o Frankfurter: que moedas existem, e quanto vale uma na outra
#   3. o saldo total (a funcao pura e a irma da API)
#   4. a conferencia, com asserts
#   5. o menu

import requests
import apoio_rede   # rede a prova de sala (timeout, cache, certificado) - nao precisa entender
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ===== 1. A conta e o deposito =====
#
# A conta inteira cabe num dicionario. A chave eh o codigo da moeda, o
# valor eh quanto tem nela:
#
#     conta = {'BRL': 1500, 'EUR': 10}
#
# Nao existe variavel global: a conta nasce dentro do main(), la embaixo,
# e eh passada por parametro pra cada funcao que precisa dela.

def deposita(conta, moeda, valor):
    if moeda not in conta.keys():
        conta[moeda] = valor
    else:
        conta[moeda] = conta[moeda]+ valor
    return conta

# o deposito cria a chave, e o segundo deposito na mesma moeda soma
conta_t = {}
deposita(conta_t, 'BRL', 1000)
deposita(conta_t, 'EUR', 10)
deposita(conta_t, 'BRL', 500)
assert conta_t == {'BRL': 1500, 'EUR': 10}, 'deposito soma na moeda certa'

# ===== 2. O Frankfurter =====

def busca_moedas():
    # O Frankfurter tem um endereco que lista as moedas que ele conhece.
    # Vem um dicionario codigo -> nome:
    #
    #     {'AUD': 'Australian Dollar', 'BRL': 'Brazilian Real', ...}
    #
    # Serve pra recusar um codigo inventado ANTES de ele ir parar na
    # conta: se a gente pedisse a cotacao de 'XYZ', a API responderia
    # com erro em vez de dados.
    return requests.get('https://api.frankfurter.dev/v1/currencies', verify=False).json()


def busca_cambio(moeda_base, moeda_destino, data):
    # A mesma funcao da lista: monta o endereco, baixa, vira dicionario.
    #
    #     >>> busca_cambio('BRL', 'EUR', '2024-07-01')
    #     {'amount': 1.0, 'base': 'BRL', 'date': '2024-07-01', 'rates': {'EUR': 0.16662}}
    #
    # Repare: `moeda_destino` NAO eh uma lista. Eh uma STRING - 'EUR', ou
    # 'EUR,USD,JPY' com os codigos separados por virgula, sem espaco, que
    # eh o formato que o endereco do Frankfurter espera. O nome esta no
    # plural porque na lista ela carrega varios codigos de uma vez:
    #
    #     >>> busca_cambio('BRL', 'EUR,USD', '2024-07-01')['rates']
    #     {'EUR': 0.16662, 'USD': 0.17904}
    #
    # Uma lista Python de verdade NAO funciona: a f-string escreveria
    # to=['EUR', 'USD'] no endereco, com colchetes e aspas, e a API
    # responde 404 "not found". Neste arquivo ela eh sempre chamada com
    # um codigo so (a funcao cotacao_entre é quem chama).
    url = f'https://api.frankfurter.dev/v1/{data}?from={moeda_base}&to={moeda_destino}'
    dic = requests.get(url, verify=False).json()
    return dic


def cotacao_entre(moeda, moeda_destino, data):
    # Quanto vale 1 unidade de `moeda` em `moeda_destino`, naquela data
    # ('latest' eh hoje).
    #
    #     >>> cotacao_entre('BRL', 'EUR', '2024-07-01')
    #     0.16662
    #
    # Caso especial: a moeda nela mesma vale 1. Nao eh so atalho - o
    # Frankfurter RECUSA o pedido from=EUR&to=EUR ("bad currency pair").
    if moeda == moeda_destino:
        return 1
    dic = busca_cambio(moeda, moeda_destino, data)
    return dic['rates'][moeda_destino]
 
# e com as cotacoes de um dia que ja passou: em 2024-07-01, 1 real valia
# 0.16662 euros e 1 euro valia 6.0016 reais. Dia passado nao muda mais,
# entao da pra conferir o valor exato
assert cotacao_entre('BRL', 'EUR', '2024-07-01') == 0.16662, 'o euro daquele dia'
assert cotacao_entre('EUR', 'EUR', '2024-07-01') == 1, 'moeda nela mesma vale 1'

# ===== 3. O saldo total =====
#
# Aqui esta o par que a lista inteira usa. A funcao PURA recebe a conta e
# as cotacoes prontas e so faz conta - nao vai a internet, entao da pra
# testar com numeros inventados. A irma da API busca as cotacoes e
# entrega pra pura.

def busca_cotacoes(conta, moeda_destino, data):
    # Uma cotacao por moeda da conta. Devolve um dicionario
    # moeda -> quanto vale 1 unidade dela em moeda_destino:
    #
    #     >>> busca_cotacoes({'BRL': 1500, 'EUR': 10}, 'EUR', '2024-07-01')
    #     {'BRL': 0.16662, 'EUR': 1}
    #
    # Repare que a API eh chamada DENTRO do laco: uma conta com tres
    # moedas faz ate tres perguntas ao Frankfurter.
    dic ={}
    for moeda in conta.keys():
        valor = cotacao_entre(moeda, moeda_destino, data)
        dic[moeda] = valor
    return dic

cotacoes_t = busca_cotacoes(conta_t, 'EUR', '2024-07-01')
assert cotacoes_t == {'BRL': 0.16662, 'EUR': 1}, 'uma cotacao por moeda da conta'

def saldo_total(conta, cotacoes):
    # A PURA: cada parte da conta vezes a cotacao dela, tudo somado.
    #
    #     >>> saldo_total({'BRL': 1500, 'EUR': 10}, {'BRL': 0.16662, 'EUR': 1})
    #     259.93
    #
    #     arredonda com 2 casas decimais. Moeda tem centavo, mas nao milesimo
    valor = 0
    for moeda in conta.keys():
        valor += conta[moeda] * cotacoes[moeda]
    valor = round(valor,2)
    return valor

# a funcao pura, com cotacoes inventadas - nao vai a internet
conta_t = {'BRL': 1500, 'EUR': 10}
assert saldo_total(conta_t, {'BRL': 0.2, 'EUR': 1}) == 310.0, '1500 * 0.2 + 10 * 1'
assert saldo_total(conta_t, cotacoes_t) == 259.93, '1500 * 0.16662 + 10 * 1'
assert saldo_total(conta_t, busca_cotacoes(conta_t, 'BRL', '2024-07-01')) == 1560.02, '1500 * 1 + 10 * 6.0016'


def saldo_total_hoje(conta, moeda_destino):
    # A irma da API: busca as cotacoes de hoje e entrega pra pura somar.
    return saldo_total(conta, busca_cotacoes(conta, moeda_destino, 'latest'))


# ===== 4. Conferindo, antes do menu =====









# ===== 5. O menu =====

def main():
    conta = {}                  # a conta comeca vazia
    moedas = busca_moedas()     # a lista de moedas eh baixada UMA vez, aqui

    while True:
        print()
        print('=== CONTA EM VARIAS MOEDAS ===')
        print(f'conta: {conta}')
        print('1. Depositar')
        print('2. Saldo total numa moeda')
        print('3. Ver os codigos das moedas')
        print('4. Sair')
        opcao = input('Opcao: ')

        if opcao == '1':
            # .upper() aceita 'brl' e 'BRL' - as chaves da conta ficam
            # sempre em maiusculas, iguais as do Frankfurter
            moeda = input('  moeda (codigo de 3 letras): ').upper()
            if moeda not in busca_moedas().keys():
                print(f'  o Frankfurter nao conhece "{moeda}" - veja a opcao 3')
            else:
                # digitar letras no valor derruba o programa (ValueError).
                # Tratar isso eh assunto de outra aula, a de excecoes.
                valor = float(input('  valor: '))
                deposita(conta, moeda,valor)
                print(f'  depositado. A conta agora: {conta}')

        elif opcao == '2':
            moeda = input('  em que moeda? ').upper()
            if moeda not in moedas.keys():
                print(f'  o Frankfurter nao conhece "{moeda}" - veja a opcao 3')
            else:
                print(f'  saldo total: {saldo_total_hoje(conta, moeda)} {moeda}')

        elif opcao == '3':
            print(busca_moedas())

        elif opcao == '4':
            break

        else:
            print('Opcao invalida')


main()
