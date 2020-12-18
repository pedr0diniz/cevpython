# DESAFIO 037 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE
#DE CONVERSÃO:

#1 para BINÁRIO
#2 para OCTAL
#3 para HEXADECIMAL

num = int(input('Digite um número inteiro: '))
print()
base = int(input('''Gostaria de converter esse número para uma base numérica diferente?

[ 1 ] para converter o número {} para binário
[ 2 ] para converter o número {} para octal
[ 3 ] para converter o número {} para hexadecimal
Digite outro número para manter o número {} na forma decimal

'''.format(num,num,num,num)))
print()
if base == 1:
    numbin = bin(num)
    print('O número {} convertido para binário é igual a {}.'.format(num,numbin[2:]))
    #as conversões em python sempre deixam um resíduo do tipo "0b", "0o" ou "0h" nos números convertidos, dependendo se
    #a conversão foi feita para binário, octal ou hexadecimal, respectivamente. Para eliminar esse resíduo, eliminamos
    #os dois primeiros elementos do vetor, o 0 na posição [0] e o b, o ou h na posição [1]. Para isso, [2:].
elif base == 2:
    numoct = oct(num)
    print('O número {} convertido para octal é igual a {}.'.format(num,numoct[2:]))
elif base == 3:
    numhex = hex(num)
    print('O número {} convertido para hexadecimal é igual a {}.'.format(num,numhex[2:]))
else:
    print('Você não converteu a base numérica do número {}.'.format(num))
