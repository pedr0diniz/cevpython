# DESAFIO 078 - Faça um programa que leia 5 valores numéricos e guarde-os em uma LISTA.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas POSIÇÕES na lista.

numeros = list()
posmax = list()
posmin = list()

for i in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a Posição {i}: ')))
for c, n in enumerate(numeros):
    if n == max(numeros):
        posmax.append(c)
    if n == min(numeros):
        posmin.append(c)

print(f'Você digitou os valores {numeros}.')
print(f'O maior número é {max(numeros)}, que aparece em {posmax}.')
print(f'O menor número é {min(numeros)}, que aparece em {posmin}.')

#ou, do jeito que o professor fez

print()
print(f'O maior número é {max(numeros)}, que aparece em ', end= '')
for indice, valor in enumerate(numeros):
    if valor == max(numeros):
        print(f'{indice}... ', end= '')
print()
print(f'O menor número é {min(numeros)}, que aparece em ', end= '')
for indice, valor in enumerate(numeros):
    if valor == min(numeros):
        print(f'{indice}... ', end= '')
print()