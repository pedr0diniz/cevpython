# DESAFIO 082 - Crie um programa que vai ler VÁRIOS NÚMEROS e colocar em uma LISTA. Depois disso, crie DUAS LISTAS
#EXTRAS que vão conter apenas os valores PARES e os valores ÍMPARES digitados, respectivamente. Ao final, mostre o
#conteúdo das TRÊS LISTAS geradas.

numeros = []
pares = []
impares = []
controle = 'S'

while controle == 'S':
  numeros.append(int(input('Digite um número: ')))
  controle = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
  while controle not in 'SN':
    controle = str(input('Opção inválida! [Sim] ou [Não]: ')).strip().upper()[0]
for i in numeros:
  if i % 2 == 0:
    pares.append(i)
  else:
    impares.append(i)
print(f'A lista de números digitados é: {numeros}.')
print(f'Da lista acima, os números pares foram: {pares}.')
print(f'Da lista acima, os números ímpares foram: {impares}.')