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
    contador_rolagem = 0
    guardados_j1 = []
    rodada_finalizada = 0

    while rodada_finalizada == 0:
        print(f'Dados rolados: {dados_rolados_j1}')
        print(f'Dados guardados: {guardados_j1}')
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()

        if opcao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            if 0 <= indice < len(dados_rolados_j1):
                func = guardar_dado(dados_rolados_j1, guardados_j1, indice)
                dados_rolados_j1 = func[0]
                guardados_j1 = func[1]
            else:
                print("Índice inválido.")

        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            if 0 <= indice < len(guardados_j1):
                func = remover_dado(dados_rolados_j1, guardados_j1, indice)
                dados_rolados_j1 = func[0]
                guardados_j1 = func[1]
            else:
                print("Índice inválido.")

        elif opcao == '3':
            if contador_rolagem >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados_j1 = rolar_dados(len(dados_rolados_j1))
                contador_rolagem += 1

        elif opcao == '4':
            imprime_cartela(cartela)

        elif opcao == '0':
            print("Digite a combinação desejada:")
            combinacao = input()
            dados_totais = dados_rolados_j1 + guardados_j1

            if combinacao in cartela["regra_simples"]:
                numero = int(combinacao)
                if cartela["regra_simples"][numero] == -1:
                    cartela = faz_jogada(dados_totais, combinacao, cartela)
                    rodada_finalizada = "jogada concluida" 
                else:
                    print("Essa combinação já foi utilizada.")
            elif combinacao in cartela["regra_avancada"]:
                if cartela["regra_avancada"][combinacao] == -1:
                    cartela = faz_jogada(dados_totais, combinacao, cartela)
                    rodada_finalizada = "jogada concluida" 
                else:
                    print("Essa combinação já foi utilizada.")
            else:
                print("Combinação inválida. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente.")

    num_rodadas += 1

pontuacao = 0
pontos_regras_simples = 0

for regra, valores in cartela.items():
    for pontos in valores.values():
        if pontos != -1:
            pontuacao += pontos
            if regra == 'regra_simples':
                pontos_regras_simples += pontos

if pontos_regras_simples >= 63:
    pontuacao += 35

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")