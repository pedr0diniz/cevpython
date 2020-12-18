# DESAFIO 092 - Crie um programa que leia NOME, ANO DE NASCIMENTO e CARTEIRA DE TRABALHO e cadastre-os (com IDADE)
#em um DICIONÁRIO. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ANO DE CONTRATAÇÃO e o
#SALÁRIO. Calcule e acrescente, além da IDADE, com quantos anos a pessoa vai se APOSENTAR.

#Considere que pra se aposentar, são 35 anos de contribuição

dicio = {}
from datetime import date

dicio['nome'] = str(input('Digite o nome: '))
dicio['nascimento'] = int(input('Digite o ano em que você nasceu: '))
dicio['ctps'] = int(input('Digite o número da carteira de trabalho: '))
print(dicio)

if dicio['ctps'] != 0:
  dicio['contratação'] = int(input('Digite o ano de contratação: '))
  dicio['salario'] = float(input('Digite o valor do salário: R$'))
  dicio['aposentadoria'] = dicio['contratação'] - dicio['nascimento'] + 35

dicio['idade'] =  date.today().year - dicio['nascimento']

for k, v in dicio.items():
  print(f'{k.upper()}: {v}.')