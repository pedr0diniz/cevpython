# DESAFIO 014 - Escreva um programa que coonverta uma temperatura digitada em ºC para ºF.

c = float(input('Digite a temperatura em ºC: '))
f = ((9*c)/5)+32

print('A temperatura de {}ºC corresponde a {}ºF.'.format(c,f))

#ou

print('A temperatura de {}ºC corresponde a {}ºF.'.format(c,((9*c)/5)+32))