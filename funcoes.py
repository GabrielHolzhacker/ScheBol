from random import randint
def rolar_dados (num):
    lista = []
    for numero in range(num):
        lista.append(randint(1, 6))
    return lista

def guardar_dado (a_rolados, a_guara, num):
    a_guara.append(a_rolados[num])
    a_rolados_novo = []
    for i in range (len(a_rolados)):
        if i != num:
            a_rolados_novo.append(a_rolados[i])
    return [a_rolados_novo, a_guara]

def remover_dado(a_rolados, a_guara, num):
    a_rolados.append(a_guara[num])
    a_guara_novo= []
    for i in range (len(a_guara)):
        if i != num:
            a_guara_novo.append(a_guara[i])
    return [a_rolados, a_guara_novo]

def calcula_pontos_regra_simples(a):
    pontos = {i: 0 for i in range(1, 7)}
    for d in a:
        pontos[d] += d
    return pontos

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

def calcula_pontos_regra_avancada(a):
    didi = {'cinco_iguais':0, 'full_house':0, 'quadra':0, 'sem_combinacao':0, 'sequencia_alta':0, 'sequencia_baixa':0}
    didi['cinco_iguais'] = calcula_pontos_quina(a)
    didi['full_house'] = calcula_pontos_full_house(a)
    didi['quadra'] = calcula_pontos_quadra(a)
    didi['sem_combinacao'] = calcula_pontos_soma(a)   
    didi['sequencia_alta'] = calcula_pontos_sequencia_alta(a)
    didi['sequencia_baixa'] = calcula_pontos_sequencia_baixa(a)
    return didi


def faz_jogada(a, b, c):
    num = ['1','2','3','4','5','6']
    if b in num:
        b = int(b)
    if b in c['regra_simples']:
        pontos = calcula_pontos_regra_simples(a)
        c['regra_simples'][b] = pontos[b]
    elif b in c['regra_avancada']:
        pontos = calcula_pontos_regra_avancada(a)
        c['regra_avancada'][b] = pontos[b]
    return c

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)