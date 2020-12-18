# DESAFIO 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
#calcule e mostre o comprimento da hipotenusa.

co = float(input('Digite o valor do cateto oposto do triângulo: '))
ca = float(input('Digite o valor do cateto adjacente do triângulo: '))

print('A hipotenusa do triângulo retângulo composto pelos catetos {} e {} é {}.'.format(co,ca,(co**2+ca**2)**(1/2)))

#ou

from math import sqrt,pow,hypot

p = sqrt(pow(co,2)+pow(ca,2))

h = hypot(co,ca)

#ou

#import math

#p = math.sqrt(pow(co,2)+pow(ca,2))

print('A hipotenusa do triângulo retângulo composto pelos catetos {:.2f} e {:.2f} é {:.2f}.'.format(co,ca,p))

print('A hipotenusa do triângulo retângulo composto pelos catetos {:.2f} e {:.2f} é {:.2f}.'.format(co,ca,h))