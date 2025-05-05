from funcoes import *
#RODADA 1 JOGADOR 1 ///////////
dados_rolados_j1_r1 = rolar_a(5)
guardados_j1_r1 = []
print(f'Dados rolados: {dados_rolados_j1_r1}')
print(f'Dados guardados: {guardados_j1_r1}')

#ESCOLHA DA OPCAO
Opção_j1_r1 = (input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:"))
#CHECA SE A OPCAO Ë VALIDA
if Opção_j1_r1 not in range(-1,5):
    print(f'Opção inválida. Tente novamente.')
    Opção_j1_r1 = int(input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:"))
#FAZ CADA OPCAO
if Opção_j1_r1 == 1:
    print("Digite o índice do dado a ser guardado (0 a 4):")
    guardar_dado(dados_rolados_j1_r1, guardados_j1_r1, )
if Opção_j1_r1 == 2:
if Opção_j1_r1 == 3:
if Opção_j1_r1 == 4:
if Opção_j1_r1 == 0:




lero = 1
