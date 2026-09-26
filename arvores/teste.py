arvore100={'raiz':100,
           'esquerda':{'raiz':30, 
                       'esquerda': {'raiz': 15, 'direita':{}, "esquerda": {}}, 
                       'direita': {}},
           'direita':{'raiz': 110,
                      'esquerda':{'raiz': 103, 'direita':{}, "esquerda": {}},
                      'direita': {'raiz': 150, 'direita':{}, "esquerda": {}} 
                      }
          }

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
    
busca(arvore100,16)