from random import randint
def rolar_dados (num):
    lista = []
    for numero in range(num):
        lista.append(randint(1, 6))
    return lista

def guardar_dado (dados_rolados, dados_guardados, num):
    dados_guardados.append(dados_rolados[num])
    dados_rolados_novo = []
    for i in range (len(dados_rolados)):
        if i != num:
            dados_rolados_novo.append(dados_rolados[i])
    return [dados_rolados_novo, dados_guardados]