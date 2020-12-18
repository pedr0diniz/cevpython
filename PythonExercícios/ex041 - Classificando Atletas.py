# DESAFIO 041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
#mostre sua categoria, de acordo com a idade:

#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 25 anos: SÊNIOR
#Acima: MASTER

from datetime import date

atual = date.today().year

nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - nasc
print()

if idade <= 9:
    print('O atleta nascido em {} tem {} anos e se encaixa na categoria MIRIM!'.format(nasc,idade))
elif idade <= 14:
    print('O atleta nascido em {} tem {} anos e se encaixa na categoria INFANTIL!'.format(nasc,idade))
elif idade <= 19:
    print('O atleta nascido em {} tem {} anos e se encaixa na categoria JUNIOR!'.format(nasc,idade))
elif idade <= 25:
    print('O atleta nascido em {} tem {} anos e se encaixa na categoria SÊNIOR!'.format(nasc,idade))
else:
    print('O atleta nascido em {} tem {} anos e se encaixa na categoria MASTER!'.format(nasc,idade))

#não precisa determinar os intervalos pq se o atleta tiver mais que 9, 14, 19 ou 25 anos,
# o algaritmo pula pra próxima condição automaticamente