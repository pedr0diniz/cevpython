# DESAFIO 059 - Crie um programa que leia DOIS VALORES e mostre um MENU na tela:

#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
resposta = 0

from time import sleep

menu = 0
while menu != 5:
    menu = int(input('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    O que você vai fazer? '''))
    print('~' * 30)
    if menu < 1 or menu > 5:
        print('Digite uma opção válida!')
    elif menu == 1:
        resposta = n1 + n2
        print('{} + {} = {}'.center(30, ' ').format(n1,n2,resposta))
    elif menu == 2:
        resposta = n1 * n2
        print('{} x {} = {}'.center(30, ' ').format(n1,n2,resposta))
    elif menu == 3:
        if n1 > n2:
            resposta = n1
            print('{} é maior do que {}.'.center(30, ' ').format(resposta,n2))
        elif n1 < n2:
            resposta = n2
            print('{} é maior do que {}.'.center(30, ' ').format(resposta,n1))
        else:
            print('O primeiro e o segundo valor são iguais!')
    elif menu == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif menu == 5:
        print('Finalizando',end='')
        for i in range(1,4):
            print('.',end='')
            sleep(0.33)
            if i == 3:
                print()
    print('~' * 30)
print('Programa Encerrado!')