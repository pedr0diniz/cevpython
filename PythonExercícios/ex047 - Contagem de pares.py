# DESAFIO 047 - Crie um programa que mostre na tela TODOS OS NÚMEROS PARES que estão no intervalo entre 1 e 50.

i = int(input('Digite um número inicial: '))
f = int(input('Digite um número final: '))

for n in range(i,f+1):
    if n % 2 == 0:
        print('{} '.format(n), end='')
print('\nFim! Todos os números pares entre {} e {}.'.format(i,f))

#ou

for m in range(2, 51, 2): #menos processamento envolvido devido a um menor número de iterações
    print(m, end=' ') #sem validações condicionais
print('Acabou!')