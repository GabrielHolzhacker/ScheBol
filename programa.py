from funcoes import *

cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
num_rodadas = 0

while num_rodadas < 12:
    dados_rolados_j1 = rolar_dados(5)
    guardados_j1 = []
    contador_rolagem = 0

    print(f'Dados rolados: {dados_rolados_j1}')
    print(f'Dados guardados: {guardados_j1}')
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
    Opção_j1 = "inicio"
    while Opção_j1 != 'jogada concluida':
        print(f'Dados rolados: {dados_rolados_j1}')
        print(f'Dados guardados: {guardados_j1}')
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        Opção_j1 = input()

        if Opção_j1 == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            func = guardar_dado(dados_rolados_j1, guardados_j1, indice)
            dados_rolados_j1 = func[0]
            guardados_j1 = func[1]

        elif Opção_j1 == '2':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            func = remover_dado(dados_rolados_j1, guardados_j1, indice)
            dados_rolados_j1 = func[0]
            guardados_j1 = func[1]

        elif Opção_j1 == '3':
            if contador_rolagem >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados_j1 = rolar_dados(len(dados_rolados_j1))
                contador_rolagem += 1

        elif Opção_j1 == '4':
            imprime_cartela(cartela)

        elif Opção_j1 == '0':
            print("Digite a combinação desejada:")
            combinacao = input()
            dados_totais = dados_rolados_j1 + guardados_j1

            if combinacao in cartela["regra_simples"]:
                numero = int(combinacao)
                if cartela["regra_simples"][numero] == -1:
                    cartela = faz_jogada(dados_totais, combinacao, cartela)
                    opcao = "jogada concluida" 
                else:
                    print("Essa combinação já foi utilizada.")
            elif combinacao in cartela["regra_avancada"]:
                if cartela["regra_avancada"][combinacao] == -1:
                    cartela = faz_jogada(dados_totais, combinacao, cartela)
                    opcao = "jogada concluida" 
                else:
                    print("Essa combinação já foi utilizada.")

        else:
            print("Opção inválida. Tente novamente.")
            Opção_j1 = input()
    num_rodadas += 1

pontuacao = 0
pontos__regras_simples = 0

for regra, valores in cartela.items():
    for pontos in valores.values():
        pontuacao += pontos
        if regra == 'regra_simples':
            pontos_regras_simples += pontos

if pontos_regras_simples >= 63:
    pontuacao += 35

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")