# DESAFIO 074 - Crie um programa que vai gerar CINCO NÚMEROS ALEATÓRIOS e colocar em uma tupla. Depois disso, mostre a
#LISTAGEM DE NÚMEROS gerados e também indique o MENOR e o MAIOR valor que estão na tupla.

from random import randint
#r0 = randint(1, 10)
#r1 = randint(1, 10)
#r2 = randint(1, 10)
#r3 = randint(1, 10)
#r4 = randint(1, 10)
#tupla = (r0, r1, r2, r3, r4)
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram {tupla}.')
#organizada = sorted(tupla) #o sorted também põe números em ordem crescente
#print(f'O menor valor foi o {organizada[0]} e o maior foi {organizada[4]}.')

print(f'O menor valor foi {min(tupla)} e o maior foi {max(tupla)}.')