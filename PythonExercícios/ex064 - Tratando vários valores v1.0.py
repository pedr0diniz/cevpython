# DESAFIO 064 - Crie um programa que leia VÁRIOS NÚMEROS inteiro pelo teclado. O programa só vai parar quando o usuário
#digitar o valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA
#entre eles (desconsiderando o flag).

n = 1
soma = cont = 0
while n != 999:
  n = int(input('Digite um número para ser somado. Se não quiser mais somar, digite 999: '))
  if n == 999:
    soma = soma
  else:
    soma += n
    cont += 1
print('Você digitou {} números e a soma deles é igual a {}.'.format(cont,soma))

#ou

#while n != 999:
  #soma = += n
  #cont += 1
  #n = int(input('Digite um número [999 para parar]: ')) colocando o incremento antes do input, eu já desconsidero o flag.
#print('Você digitou {} números e a soma deles é igual a {}.'.format(cont,soma))