# DESAFIO 045 - Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

print('-=-' * 7)
print('Jokenpo Bot do ziniD')
print('-=-' * 7)
print()
print('''Olá, muito prazer! Eu sou o Jokenpo Bot! Vamos jogar PEDRA, PAPEL E TESOURA?
Para jogar, escolha uma das opções abaixo:

[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
print()
usuario = int(input('Qual é a sua jogada? '))
print()
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
print()
print('-=-' * 10)
pc = randint(0, 2)

if usuario == 0:
    print('Você escolheu PEDRA! \nEu escolhi ', end='')
    if pc == 0:
        print('PEDRA também! \nNós empatamos!')
    elif pc == 1:
        print('PAPEL! \nEu ganhei!')
    else:
        print('TESOURA! \nVocê ganhou!')
elif usuario == 1:
    print('Você escolheu PAPEL! \nEu escolhi ', end='')
    if pc == 0:
        print('PEDRA! \nVocê ganhou!')
    elif pc == 1:
        print('PAPEL também! \nNós empatamos!')
    else:
        print('TESOURA! \nEu ganhei!')
elif usuario == 2:
    print('Você escolheu TESOURA! \nEu escolhi ', end='')
    if pc == 0:
        print('PEDRA! \nEu ganhei!')
    elif pc == 1:
        print('PAPEL! \nVocê ganhou!')
    else:
        print('TESOURA também! \nNós empatamos!')
else:
    print('Opção inválida!')
print('-=-' * 10)