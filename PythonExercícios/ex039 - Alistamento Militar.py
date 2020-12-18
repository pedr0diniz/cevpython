# DESAFIO 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

#Se ele AINDA VAI SE ALISTAR ao serviço militar.
#Se é a HORA DE SE ALISTAR.
#Se já PASSOU DO TEMPO do alistamento.

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

nasc = int(input('Digite o ano de nascimento: '))
print()

from datetime import date
if (nasc+18) > date.today().year:
    print('Você ainda não tem 18 anos. Você se alistará daqui a {} anos.'.format(nasc+18-date.today().year))
elif (nasc+18) < date.today().year:
    print('Você deveria ter se alistado há {} anos.'.format(date.today().year-(nasc+18)))
else:
    print('Este é o ano para você se alistar!')