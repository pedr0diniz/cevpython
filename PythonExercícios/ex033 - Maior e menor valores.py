# DESAFIO 033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
v3 = int(input('Digite mais um valor: '))

if v1 < v2 and v1 < v3:
    print('O primeiro valor ({}) é o menor dos três ({}, {}, {}).'.format(v1,v1,v2,v3))
elif v2 < v1 and v2 < v3:
    print('O segundo valor ({}) é o menor dos três ({}, {}, {}).'.format(v2,v1,v2,v3))
elif v3 < v1 and v3 < v2:
    print('O terceiro valor ({}) é o menor dos três ({}, {}, {}).'.format(v3,v1,v2,v3))

if v1 > v2 and v1 > v3:
    print('O primeiro valor ({}) é o maior dos três ({}, {}, {}).'.format(v1,v1,v2,v3))
elif v2 > v1 and v2 > v3:
    print('O segundo valor ({}) é o maior dos três ({}, {}, {}).'.format(v2,v1,v2,v3))
elif v3 > v1 and v3 > v2:
    print('O terceiro valor ({}) é o maior dos três ({}, {}, {}).'.format(v3,v1,v2,v3))