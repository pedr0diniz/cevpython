# DESAFIO 050 - Desenvolva um programa que leis SEIS NÚMEROS INTEIROS e mostre a soma apenas daqueles que forem PARES.
#Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for i in range (1,7):
    n = int(input('Digite o {}º número inteiro: '.format(i)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma dos {} números pares listados acima é igual a {}.'.format(cont, soma))