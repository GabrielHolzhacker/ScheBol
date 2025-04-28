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

def remover_dado(dados_rolados, dados_guardados, num):
    dados_rolados.append(dados_guardados[num])
    dados_guardados_novo= []
    for i in range (len(dados_guardados)):
        if i != num:
            dados_guardados_novo.append(dados_guardados[i])
    return [dados_rolados, dados_guardados_novo]

def calcula_pontos_regra_simples(lista):
    dicio = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in lista:
        if i in dicio:
            dicio[i] += i
    return dicio

def calcula_pontos_soma(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

def calcula_pontos_sequencia_baixa(lista):
    if (1 in lista and 2 in lista and 3 in lista and 4 in lista):
        return 15
    if (2 in lista and 3 in lista and 4 in lista and 5 in lista):
        return 15
    if (3 in lista and 4 in lista and 5 in lista and 6 in lista):
        return 15
    else:
        return 0
    
def calcula_pontos_sequencia_alta(lista):
    if (1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista):
        return 30
    if (2 in lista and 3 in lista and 4 in lista and 5 in lista and 6 in lista):
        return 30
    else:
        return 0
    
def calcula_pontos_full_house(lista):
    dicio = {}
    for dado in lista:
        if dado in dicio:
            dicio[dado] += 1
        else:
            dicio[dado] = 1
    trio = 0
    dupla = 0
    for valor in dicio.values():
        if valor == 3:
            trio += 1
        if valor == 2:
            dupla += 1
    if trio == 1 and dupla == 1:
        soma = 0
        for dado in lista:
            soma += dado
        return soma
    return 0

def calcula_pontos_quadra(lista):
    dicio = {}
    for dado in lista:
        if dado in dicio:
            dicio[dado] += 1
        else:
            dicio[dado] = 1
    for valor in dicio.values():
        if valor >= 4:
            soma = 0
            for dado in lista:
                soma += dado
            return soma
    return 0

def calcula_pontos_quina(a):
    didi = {}
    for i in a: 
        if i in didi:
            didi[i] +=1
        else:
            didi[i] = 1
    for num in didi.values():
        if num >= 5:
            return 50
    return 0


