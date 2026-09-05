# apoio_rede.py - rede a prova de sala de aula. Nao mexa aqui, e nao
# precisa entender: basta que este arquivo esteja na mesma pasta do
# exercicio.
#
# Ele faz tres coisas por baixo do requests.get:
#   1) poe um limite de tempo, pra nenhuma API te deixar pendurado;
#   2) troca os erros crus de rede por mensagens em portugues;
#   3) se a biblioteca requests_cache nao estiver instalada, guarda num
#      arquivo o que ja foi baixado - assim rodar de novo nao pede a
#      mesma coisa pra internet outra vez.
import json, os, sys, time
import requests

ARQUIVO_DE_CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache_api.json')
VALIDADE_EM_HORAS = 12

# se o requests_cache ja esta cuidando do cache, nao fazemos o nosso
USAR_CACHE_PROPRIO = 'requests_cache' not in sys.modules

if USAR_CACHE_PROPRIO:
    try:
        with open(ARQUIVO_DE_CACHE, encoding='utf-8') as _f:
            _cache = json.load(_f)
    except Exception:
        _cache = {}
else:
    _cache = {}

# guarda o get original; o getattr evita capturar uma versao ja trocada,
# caso este modulo seja importado duas vezes
_get_de_verdade = getattr(requests.get, '_original', requests.get)


class _RespostaGuardada:
    status_code = 200
    ok = True
    def __init__(self, dados):
        self._dados = dados
    def json(self):
        return self._dados
    def raise_for_status(self):
        return None
    @property
    def text(self):
        return json.dumps(self._dados, ensure_ascii=False)


def _guarda(url, dados):
    _cache[url] = {'quando': time.time(), 'dados': dados}
    try:
        with open(ARQUIVO_DE_CACHE, 'w', encoding='utf-8') as f:
            json.dump(_cache, f, ensure_ascii=False)
    except Exception:
        pass


def _get(url, *args, **kwargs):
    guardado = _cache.get(url) if USAR_CACHE_PROPRIO else None
    if guardado and time.time() - guardado['quando'] < VALIDADE_EM_HORAS * 3600:
        return _RespostaGuardada(guardado['dados'])

    def _desiste(mensagem):
        if guardado:
            print(f'AVISO: {mensagem.splitlines()[0]}')
            print('       Usando o dado guardado da ultima vez.')
            return _RespostaGuardada(guardado['dados'])
        raise SystemExit(f'\n{mensagem}\nurl: {url}\n')

    kwargs.setdefault('timeout', 15)
    try:
        resposta = _get_de_verdade(url, *args, **kwargs)
    except Exception as erro:
        return _desiste(f'nao consegui falar com a internet ({type(erro).__name__}).\n'
                        'Confira a rede. Se estiver tudo certo por ai, chame o professor.')

    if resposta.status_code in (403, 429):
        return _desiste('a API recusou o pedido (pedidos demais deste computador ou desta rede).\n'
                        'Isso NAO eh erro do seu codigo. Espere alguns minutos, rode de novo,\n'
                        'e avise o professor.')

    if resposta.status_code == 400:
        return _desiste('a API disse que o pedido esta mal formado (400).\n'
                        'Confira se a url ficou igualzinha a do enunciado. Se voce digitou um\n'
                        'CEP no menu, ele precisa ter 8 digitos e so numeros.')

    if resposta.status_code != 200:
        return _desiste(f'a API respondeu com status {resposta.status_code}, e nao com dados.\n'
                        'Provavelmente ela esta fora do ar - avise o professor.')

    try:
        dados = resposta.json()
    except Exception:
        return _desiste('a API respondeu, mas nao com dados em json.\n'
                        'Confira se a url ficou igualzinha a do enunciado.')

    if not USAR_CACHE_PROPRIO:
        return resposta          # o requests_cache ja guardou; devolve a resposta real

    _guarda(url, dados)
    return _RespostaGuardada(dados)


_get._original = _get_de_verdade
requests.get = _get
# fim do apoio_rede
