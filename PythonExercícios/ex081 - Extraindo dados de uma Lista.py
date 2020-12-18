# DESAFIO 081 - Crie um programa que vai ler VÁRIOS NÚMEROS e colocar numa lista. Depois disso, mostre:

#A) QUANTOS números foram digitados.
#B) A lista de valores, ordenada de forma DECRESCENTE.
#C) Se o valor 5 foi digitado e está ou não na LISTA.

cont = 0
controle = 'S'
numeros = []
while controle == 'S':
  numeros.append(int(input('Digite um valor: ')))
  cont += 1
  controle = str(input('Deseja digitar mais números? [S/N] ')).strip().upper()[0]
  while controle not in 'SN':
    controle = str(input('Opção inválida! [Sim] ou [Não]? ')).strip().upper()[0]
print(f'Foram digitados {cont} números.')
print(f'Foram digitados {len(numeros)} números.')
print(f'A listagem de números digitados de forma decrescente é: {sorted(numeros)[::-1]}') #numeros organizados de trás pra frente
if 5 in numeros:
  print('O número 5 está entre os números digitados na lista!')
else:
  print('O número 5 não foi digitado na lista.')