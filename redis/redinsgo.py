import random
import json

import redis

colecaoUsuarios = "usuarios"
colecaoCartelas = "cartelas"
colecaoNumeros = "numerosSorteio"

def gerar_dados():
    for i in numerosParaSorteio:
        r.sadd(colecaoNumeros, i)

    for i in usuarios:
        _nomeCartela = "cartela" + str(i)
        _numerosCartela = random.sample(numerosParaSorteio, 15)
        _cartela = { "nome" : _nomeCartela,
                     "numeros" : _numerosCartela,
                     "pontos" : 0 }

        _nomeUsuario = "usuario" + str(i)
        _usuario = { "nome" : _nomeUsuario,
                     "cartela" : _cartela }
        r.sadd(colecaoUsuarios, json.dumps(_usuario))
        r.sadd(colecaoCartelas, json.dumps(_cartela))

def iniciar_bingo():
    gerar_dados()
    calcular_score()

def calcular_score():
    ganhador = False
    while ganhador is False:
        sorteado = r.spop(colecaoNumeros, 1)
        for i in cart


if __name__ == '__main__':
    r = redis.Redis()
    qtdJogadores = 50
    numerosParaSorteio = range(1, 101)
    usuarios = range(1, 51)
    cartelas = []
    iniciar_bingo()