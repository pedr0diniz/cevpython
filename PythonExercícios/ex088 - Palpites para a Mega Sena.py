# DESAFIO 088 - Faça um programa que ajude um jogador da MEGA SENA a criar PALPITES. O programa vai perguntar QUANTOS
#JOGOS serão gerados e vai sortear 6 NÚMEROS ENTRE 1 E 60 para cada jogo, cadastrando tudo em uma LISTA COMPOSTA.

from random import randint
from time import sleep

print(f' {"-" * 40}\n {"GERADOR DE JOGOS DA MEGA SENA":^40}\n {"-" * 40}')

numeros = []
jogos = []
njogos = int(input('\nDigite quantos jogos você quer que eu sorteie: '))
print(f'\n{"-=" * 3} SORTEANDO {njogos} JOGOS {"=-" * 3}')

for i in range(0, njogos):
    sleep(0.75)
    print(f'Jogo {i+1}: ',end='')
    for c in range(0, 6):
        n = randint(1, 60)
        while n in numeros:
            n = randint(1, 60)
        numeros.append(n)
    jogos.append(numeros[:])  #preciso que jogos receba uma cópia dos valores de numeros, usando o [:]
    numeros.clear()
    print(sorted(jogos[i]))
print(f'{"-=-" * 3} BOA SORTE!! {"-=-" * 3}')