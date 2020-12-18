# DESAFIO 087 - Aprimore o DESAFIO ANTERIOR, mostrando no final:

#A) A SOMA de todos os VALORES PARES digitados.
#B) A SOMA dos valores da TERCEIRA COLUNA.
#C) O MAIOR valor da SEGUNDA LINHA.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somaj2 = 0
from math import inf
maiori1 = -inf

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
        if i == 1 and matriz[i][j] > maiori1:
            maiori1 = matriz[i][j]

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            somapar += matriz[i][j]
        if j == 2:
            somaj2 += matriz[i][j]
    print()
print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {somaj2}.')
print(f'O maior valor da segunda linha é {maiori1}.')