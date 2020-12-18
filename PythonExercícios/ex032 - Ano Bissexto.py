# DESAFIO 032 - Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))

from datetime import date
from time import strftime

if ano == 0:
    hoje = date.today() #puxa como string
    ano = int(strftime("%Y")) #preciso definir como int na frente pra ele converter
    #ou ano = date.today().year --------- já pega o ano atual como int



if (ano % 4 == 0):
    if (ano / 100 == ano // 100) and (ano % 400 != 0):
    #ou if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('O ano {} não é bissexto!'.format(ano))
    else:
        print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))