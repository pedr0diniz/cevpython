# DESAFIO 070 - Crie um programa que leia o NOME e o PREÇO de VÁRIOS PRODUTOS. O programa deverá perguntar se o USUÁRIO
#vai continuar. No final, mostre:

#A) Qual é o TOTAL GASTO na compra.
#B) Quantos produtos custam MAIS de R$1000.
#C) Qual é o NOME do produto mais barato.

from math import inf
menorpreco = inf
total = mais1000 = preco = 0
controle = maisbarato = nome = 'S'

while True:
    if controle == 'S':
        nome = str(input('Digite o nome do produto: '))
        preco = float(input('Digite o valor do produto: R$'))
        total += preco
        if preco > 1000:
            mais1000 += 1
        if preco < menorpreco:
            menorpreco = preco
            maisbarato = nome
        controle = str(input('Deseja acrescentar outro produto? [S/N] ')).strip().upper()[0]
        while controle not in 'SN':
            controle = str(input('Deseja acrescentar outro produto? [S/N] ')).strip().upper()[0]
    else:
        break
print(f'--' * 30,
      f'\nA) O total gasto na compra foi de R${total:.2f}.'
      f'\nB) {mais1000} produtos custam mais de R$1000,00.'
      f'\nC) O produto mais barato foi: {maisbarato}, custando R${menorpreco:.2f}.')