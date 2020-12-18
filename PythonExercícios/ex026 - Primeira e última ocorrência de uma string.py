# DESAFIO 026 - Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip() #tirar os espaços inúteis no começo e no fim

print('A letra A aparece {} vezes.' .format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.find('A')+1)) #+1 pq a lista começa em [0]
print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1)) #rfind faz a procura ser do fim pro começo