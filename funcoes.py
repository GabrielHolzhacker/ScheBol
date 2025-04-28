from random import randint
def rolar_dados (num):
    lista = []
    for numero in range(num):
        lista.append(randint(1, 6))
    return lista