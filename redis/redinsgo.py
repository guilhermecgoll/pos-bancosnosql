import redis


def gerar_cartelas():
    print('gerar as cartelas')

def gerar_usuarios():
    print('gerar usuarios')

def iniciar_bingo():
    gerar_cartelas()
    gerar_usuarios()
    #for...
    print('sorteando numeros')
    calcular_score()

def calcular_score():
    print('score')

if __name__ == '__main__':
    # r = redis.Redis()
    # r.mset({"Croatia": "Zagreb", "Bahamas" : "Nassau"})
    # print(r.get("Bahamas"))
    iniciar_bingo()