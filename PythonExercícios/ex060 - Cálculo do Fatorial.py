# DESAFIO 060 - Faça um programa que leia um número qualquer e mostre o seu FATORIAL.

#Ex: 5! = 5x4x3x2x1 = 120

fatorial = i = 1
n = int(input('Digite o número do qual você quer saber o fatorial: '))
while i <= n:
    fatorial *= i
    i += 1
print('{}! = {}'.format(n, fatorial))