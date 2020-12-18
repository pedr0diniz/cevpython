# DESAFIO 038 - Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:

#O PRIMEIRO VALOR é MAIOR
#O SEGUNDO VALOR é MAIOR
#NÃO EXISTE valor maior, os dois são IGUAIS

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print()

if num1 > num2:
    print('O primeiro valor ({}) é maior do que o segundo ({}).'.format(num1,num2))
elif num1 < num2:
    print('O segundo valor ({}) é maior do que o primeiro ({}).'.format(num2,num1))
else:
    print('Não existe valor maior, os dois são iguais.')