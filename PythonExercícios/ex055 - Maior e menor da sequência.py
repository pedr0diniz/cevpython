# DESAFIO 055 - Faça um programa que leia o PESO de CINCO PESSOAS. No final, mostre qual foi o MAIOR e o MENOR peso
#lidos.
from math import inf
maior = 0
menor = inf
for i in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso é de {:.1f}kg e o menor peso é de {:.1f}kg.'.format(maior,menor))