# DESAFIO 052 - Faça um programa que leia um NÚMERO INTEIRO e diga se ele é ou não um NÚMERO PRIMO.
cont = 0
n = int(input('Digite um número: '))
for i in range(1,n):
    if n % i == 0:
        cont += 1
        print('\033[31m{}'.format(i), end=' ')
    else:
        print('\033[30m{}'.format(i), end=' ')
print('\033[31m{}'.format(n))
if cont == 1:
    print('\033[34mO número {} só é divisível por 1 e por ele mesmo, portanto, é primo!'.format(n))
else:
    print('\033[31mO número {} não é primo, pois ele é divisível por {} números.'.format(n, cont))