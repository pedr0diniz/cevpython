# DESAFIO 048 - Faça um programa que calcule a soma entre todos os NÚMEROS ÍMPARES que são MÚLTIPLOS DE TRÊS e que se
#encontrem no intervalo de 1 até 500.

soma = 0
cont = 0
for i in range(3, 501, 6): #passo 6 pra só pegar os ímpares múltiplos de 3
    soma += i
    cont += 1 #introdução a contadores
print('A soma dos {:.0f} valores solicitados é igual a {}.'.format(cont, soma))