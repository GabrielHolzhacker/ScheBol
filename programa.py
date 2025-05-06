from funcoes import *
dados_rolados_j1 = rolar_dados(5)
guardados_j1 = []
print(f'Dados rolados: {dados_rolados_j1}')
print(f'Dados guardados: {guardados_j1}')

cartela = {'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
'regra_avancada': {'sem_combinacao': -1,'quadra': -1,'full_house': -1,'sequencia_baixa': -1,'sequencia_alta': -1,'cinco_iguais': -1}}

def rodada(cartela, dados_rolados_j1, guardados_j1):
    contador_rolagem = 0

    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    Opção_j1 = input()
    while Opção_j1 != '0':
        if Opção_j1 == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            func = guardar_dado(dados_rolados_j1, guardados_j1, indice)
            dados_rolados_j1 = func[0]
            guardados_j1 = func[1]

            print(f'Dados rolados: {dados_rolados_j1}')
            print(f'Dados guardados: {guardados_j1}')

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            Opção_j1 = input()
        elif Opção_j1 == '2':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            func = remover_dado(dados_rolados_j1, guardados_j1, indice)
            dados_rolados_j1 = func[0]
            guardados_j1 = func[1]

            print(f'Dados rolados: {dados_rolados_j1}')
            print(f'Dados guardados: {guardados_j1}')

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            Opção_j1 = input()
        elif Opção_j1 == '3':
            if contador_rolagem >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados_j1 = rolar_dados(len(dados_rolados_j1))
                contador_rolagem += 1

            print(f'Dados rolados: {dados_rolados_j1}')
            print(f'Dados guardados: {guardados_j1}')

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            Opção_j1 = input()
        elif Opção_j1 == '4':
            imprime_cartela(cartela)

            print(f'Dados rolados: {dados_rolados_j1}')
            print(f'Dados guardados: {guardados_j1}')

            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            Opção_j1 = input()
        else:
            print("Opção inválida. Tente novamente.")
            Opção_j1 = input()


    dados = dados_rolados_j1 + guardados_j1

    print("Digite a combinação desejada:")
    combinação = input()

    acao = verifica_categoria(combinação, cartela)

    while acao == 1 or acao == 0:
        if acao == 1:
            print("Essa combinação já foi utilizada.")
            combinação = input()

        elif acao == 0:
            print("Combinação inválida. Tente novamente.")
            combinação = input()
        acao = verifica_categoria(combinação, cartela)

    faz_jogada(dados, combinação, cartela)
    return cartela