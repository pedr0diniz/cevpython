# DESAFIO 063 - Escreva um programa que leia um NÚMERO N inteiro qualquer e mostre na tela os N primeiros elementos de
#uma SEQUÊNCIA DE FIBONACCI.

#Ex: 0 1 1 2 3 5 8

termos = int(input('Digite quantos termos da Sequência de Fibonacci você quer saber: '))

passado = 0 #defino o primeiro termo
atual = novo = i = 1 #defino o segundo e o terceiro termo
print(passado, atual, end=' ')
while (i+1) <= termos:
    novo = atual + passado #ex: atual = 3, passado = 2. novo = 5         ^>>> atual = 5, passado = 3, novo = 8
    passado = atual        #ex: passado vira 3                           ^    passado vira 5
    atual = novo           #ex: atual vira 5 >>>>>>>>>>>>>>>>>>>>>>>>>>>>^    atual vira 8
    print(atual,end=' ')
    i += 1