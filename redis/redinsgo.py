import random
import json

import redis


colecaoNumeros = "numerosSorteio"

def iniciar_bingo():
    gerar_dados()
    calcular_score()

def gerar_dados():
    for i in numerosParaSorteio:
        r.sadd(colecaoNumeros, i)

    #serão 50 jogadores
    for i in range(1, 51):
        _nomeUsuario = "usuario" + str(int(i))
        _nomeCartela = "cartela" + str(i)
        #_numerosCartela = random.sample(numerosParaSorteio, 15)
        _numerosCartelaByte = r.srandmember(colecaoNumeros, 15)
        _numerosCartela = []
        for i in _numerosCartelaByte:
            _numerosCartela.append(int(i))

        _cartela = { "nome" : _nomeCartela,
                     "numeros" : _numerosCartela,
                     "pontos" : 0 }

        _usuario = { "nome" : _nomeUsuario,
                     "cartela" : _cartela }

        usuarios.append(_usuario['nome'])
        r.set(_usuario['nome'], json.dumps(_usuario))
        cartelas.append(_cartela['nome'])
        r.set(_cartela['nome'], json.dumps(_cartela))

def calcular_score():
    ganhadores = []
    ganhador = False
    qtdNumerosSorteados = 0
    while ganhador is False:
        sorteado = int(r.spop(colecaoNumeros, 1)[0])
        qtdNumerosSorteados+=1
        for c in cartelas:
            _c = r.get(c)
            if _c:
                cartela = json.loads(_c)
                if sorteado in cartela['numeros']:
                    cartela['pontos']+=1
                    r.set(cartela['nome'], json.dumps(cartela))
                if cartela['pontos'] >= 15:
                    ganhador = True
                    ganhadores.append(cartela)
                    print('Encontrou um ganhador!')
    
    print(f'Após sortear {qtdNumerosSorteados} números, encontramos os seguintes ganhadores:')

    _usuarios = []
    for u in usuarios:
        _u = r.get(u)
        _usuarios.append(json.loads(_u))
    
    for g in ganhadores:
        print(next((x for x in _usuarios if x['cartela']['nome'] == g['nome']), None)['nome'])

if __name__ == '__main__':
    r = redis.Redis()
    qtdJogadores = 50
    numerosParaSorteio = range(1, 101)
    usuarios = []
    cartelas = []
    iniciar_bingo()