# DESAFIO 098 - Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo
#e realize a contagem.

#Seu programa tem de realizar TRÊS CONTAGENS através da função criada:

#a) De 1 até 10, de 1 em 1
#b) De 10 até 0, de 2 em 2
#c) Uma contagem PERSONALIZADA

from time import sleep
def contador(i, f, p):
    if i == 1 and f == 10 and p == 1:
        print('a) De 1 até 10, de 1 em 1: ',end='')
    elif i == 10 and f == 0 and p == 2:
        print('b) De 10 até 0, de 2 em 2: ', end='')
    if p == 0:
        p = 1
    if i > f:
        p = -abs(p)
        f = f-1
    else:
        p = abs(p)
        f = f+1
    for c in range(i, f, p):
        sleep(0.25)
        print(c, end=' ')
    print('FIM!')
    print('-=' * 30)

contador(1, 10, 1)
contador(10, 0, 2)
print('c) Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)