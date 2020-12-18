# DESAFIO 075 - Desenvolva um programa que leia QUATRO VALORES pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

#n0 = int(input('Digite o primeiro número: '))
#n1 = int(input('Digite o segundo número: '))
#n2 = int(input('Digite o terceiro número '))
#n3 = int(input('Digite o quarto número: '))
#numeros = (n0, n1, n2, n3)

numeros = (int(input('Digite o primeiro número: ')),
           int(input('Digite o segundo número: ')),
           int(input('Digite o terceiro número ')),
           int(input('Digite o quarto número: ')))

#index3 = len(numeros)+1
contpares = 0

print(f'O valor 9 apareceu {numeros.count(9)} vezes.')

#for i in range(0, len(numeros)):
    #if index3 == len(numeros)+1 and numeros[i] == 3:
        #index3 = i
#if index3 == len(numeros)+1:
if 3 not in numeros:
    print('O valor 3 não foi digitado em nenhuma posição.')
else:
    print(f'O valor 3 foi digitado pela primeira vez na {index3+1}ª posição.')

print('Os valores pares digitados foram: ', end='')
for i in range(0, len(numeros)):
    if numeros[i] % 2 == 0:
        print(numeros[i], end=' ')
        contpares += 1
if contpares == 0:
    print('\nNenhum número par foi digitado.')