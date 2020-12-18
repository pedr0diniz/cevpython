# DESAFIO 054 - Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS. No final, mostre quantas pessoas ainda
#não atingiram a maioridade e quantas já são maiores.

from datetime import date
menores = 0
atual = date.today().year
for i in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
    if atual - nasc < 18:
        menores += 1
print('Entre as 7 pessoas listadas, temos {} menores e {} maiores de idade.'.format(menores, 7-menores))
