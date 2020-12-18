# DESAFIO 077 - Crie um programa que tenha uma tupla com VÁRIAS PALAVRAS (não usar acentos). Depois disso, você deve
#mostrar para cada palavra, quais são as suas VOGAIS.

palavras = ('pátio', 'lua', 'programar', 'linguagem', 'Amanda', 'curso', 'grátis', 'depósito', 'memória', 'mãe')

from unidecode import unidecode #com unicode eu não preciso ignorar os acentos

#for i in range(0, len(palavras)):
   # print(f'\nNa palavra {palavras[i].upper()} temos ', end='')
   # for c in range(0, len(palavras[i])):
   #     if unidecode(palavras[i][c]) in 'aeiou':
        #if unidecode(palavras[i][c]) == 'a' or unidecode(palavras[i][c]) == 'e' or unidecode(palavras[i][c]) == 'i' or unidecode(palavras[i][c]) == 'o' or unidecode(palavras[i][c]) == 'u':
   #         print(palavras[i][c], end=' ')

for p in palavras: #tentar me acostumar a usar os fors assim
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if unidecode(letra) in 'aeiou':
            print(letra, end=' ')