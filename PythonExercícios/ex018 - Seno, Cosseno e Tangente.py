# DESAFIO 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
#desse ângulo.

import math

a = int(input('Digite um ângulo em graus: '))

#O python recebe os números em radianos e executa suas funções com os valores em radianos.
#Por isso, é necessário usar a função math.radians(), a fim de converter o valor em graus para radianos.
#Estudar isso aí pra tirar a dúvida.

r = math.radians(a)

print('O seno do ângulo {}º vale {:.3f}.'.format(a,math.sin(r)))
print('O cosseno do ângulo {}º vale {:.3f}.'.format(a,math.cos(r)))
print('A tangente do ângulo {}º vale {:.3f}.'.format(a,math.tan(r)))