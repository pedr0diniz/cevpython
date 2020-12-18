# DESAFIO 053 - Crie um programa que leia uma FRASE qualquer e diga se ela é um PALÍNDROMO, desconsiderando acentos e
# espaços.

#Exemplos: Apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo, anotaram a data da maratona
cont = 0
frase = str(input('Digite uma frase: ')).strip().upper().split()
frase = (''.join(frase))
tam = len(frase)
for letra in range(tam-1, -1, -1):
    if frase[letra] == frase[abs(letra-(tam-1))]:
        cont += 1
print('O inverso de {} é {}'.format(frase, frase[::-1]))
if cont == tam:
    print('\033[34mA frase digitada é um palíndromo!')
else:
    print('\033[31mA frase digitada não é um palíndromo!')



#ou

#inverso = ''
#for letra in range(tam-1, -1, -1):
    #inverso += frase[letra]
#if inverso == frase:
    #print('\033[34mA frase digitada é um palíndromo!')
#else:
    #print('\033[31mA frase digitada não é um palíndromo!')



#ou

#if frase == frase[::-1]:
    #print('\033[34mA frase digitada é um palíndromo!')
#else:
    #print('\033[31mA frase digitada não é um palíndromo!')