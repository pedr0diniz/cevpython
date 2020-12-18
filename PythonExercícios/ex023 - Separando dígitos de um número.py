# DESAFIO 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex: Digite um número: 1834
#Unidade: 4
#Dezena: 3
#Centena: 8
#Milhar: 1

num = int(input('Digite um número de 0 a 9999: '))
#print("""Unidade: {}
#Dezena: {}
#Centena: {}
#Milhar {}""".format(num[3],num[2],num[1],num[0])) -------- sem if, só funciona pra números de 4 algarismos

print('Milhar = {}'.format(num//1000))
print('Centena = {}'.format(num%1000//100))
print('Dezena = {}'.format(num%1000%100//10))
print('Unidade = {}'.format(num%1000%100%10))