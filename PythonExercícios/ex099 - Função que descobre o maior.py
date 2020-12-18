# DESAFIO 099 - Faça um programa que tenha uma função maior(), que receba vários PARÂMETROS com valores inteiros.

# Seu programa tem que analisar todos os valores e dizer qual deles é o MAIOR e dizer quantos valores foram informados.

def maior(*num):
    for nu in num:
        numeros.append(nu)
    if printa is True:
        print(f"O maior número entre {numeros} é {max(numeros)}.")
        print(f"Foram digitados {len(numeros)} números.")


numeros = []
printa = False
controle = 'S'

while controle == 'S':
    n = int(input('Digite um número: '))
    controle = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while controle not in 'SN':
        controle = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if controle == 'N':
        printa = True
    maior(n)