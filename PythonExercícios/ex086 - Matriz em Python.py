# DESAFIO 086 - Crie um programa que crie uma MATRIZ de DIMENSÃO 3X3 e a preencha com valores lidos pelo teclado.
#No final, mostre a MATRIZ na tela, com a formatação correta.

matriz = [[], [], []]
#matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))
        #matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))

for i in range(0, 3):

    for j in range(0, 3):
        print(f'[ {matriz[i][j]:^5} ]', end='') #formatando com 5 espaços, centralizado, pra tentar manter a simetria
    print()