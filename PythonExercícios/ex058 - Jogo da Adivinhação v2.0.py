# DESAFIO 058 - Melhor o jogo do DESAFIO 028 onde o computador vai "pensar" em um NÚMERO ENTRE 0 E 10. Só que agora o
#jogador vai tentar adivinhar até ele acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
n = randint(0, 10)

cont = 0
usuario = 11
print(n)
print('Pensei em um número entre 0 e 10. Tente adivinhar!')
while usuario != n:
    usuario = int(input('Em qual número eu pensei? '))
    if usuario not in range(0, 11): #lembrando que o final do range é desconsiderado
        print('Número inválido! Digite um número entre 0 e 10!')
    elif usuario != n:
        if usuario < n:
            print('Menos... Tente novamente!')
        else:
            print('Menos... Tente novamente!')
        cont += 1
    else:
        cont += 1
        print('''Você adivinhou! Eu tinha pensado no número {}.
Você levou {} tentativas até acertar.'''.format(n,cont))