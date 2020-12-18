# DESAFIO 065 - Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. No final da execução, mostre a MÉDIA
#ENTRE TODOS os valores e qual foi o MAIOR e o MENOR valores lidos. O programa deve perguntar ao usuário se ele quer
#ou não CONTINUAR a digitar valores.

from math import inf
n = soma = cont = maior = 0
menor = inf
controle = 'S'
controle2 = ' '

while controle == 'S':
  n = float(input('Digite um número: '))
  soma += n
  cont += 1
  if n > maior:
    maior = n
  if n < menor:
    menor = n
  controle = str(input('Deseja somar mais números? [S/N] ')).strip().upper()[0]
  controle2 = controle #atualizo o controle2 para ele validar a condição abaixo sem estar preso ao valor da última iteração
  while controle not in 'SsNn' and controle2 not in 'SsNn':
    controle2 = str(input('Opção inválida! Digite S para SIM ou N para NÃO: ')).strip().upper()[0]
  controle = controle2 #atualizo o controle para ele retomar o loop
print('Você digitou {} números e a média entre eles é igual a {}!'.format(cont, soma/cont))
print('O menor e o maior número são, respectivamente, {} e {}.'.format(menor, maior))