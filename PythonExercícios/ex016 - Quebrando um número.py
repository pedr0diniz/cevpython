# DESAFIO 016 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

n = float(input('Digite um número real decimal: '))
print('A parte inteira do número {} é: {:.0f}'.format(n,n))

#ou

from math import trunc

print('A parte inteira do número {} é: {}'.format(n,trunc(n)))

#ou

#import math

#print('A parte inteira do número {} é: {}'.format(n,math.trunc(n)))