# DESAFIO 046 - Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artifício, indo
#de 10 ATÉ 0, com uma pausa de 1 SEGUNDO entre eles.

from time import sleep

for i in range(10,0,-1):
    print(i)
    sleep(1)

print('0! POPOPOPOPOW! POW! BOOM!')