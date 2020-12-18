# DESAFIO 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
# usuário tentar descobrir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
n = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
u = int(input('Em qual número eu pensei? '))
print('-=-' * 20)
print('PROCESSANDO...')
print('-=-' * 20)
sleep(3)

if n == u:
    print('Você acertou!')
else:
    print('Você errou! Eu pensei no número {} e não no {}!'.format(n,u))

# ou

print('Você acertou!' if n == u else ('Você errou! Eu pensei no número {} e não no {}!'.format(n,u)))
