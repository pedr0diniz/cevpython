# DESAFIO 067 - Faça um programa que mostre a TABUADA de VÁRIOS NÚMEROS, um de cada vez, para cada valor digitado pelo
#usuário. O programa será INTERROMPIDO quando o número solicitado for NEGATIVO.

n = 0

while True:
    n = int(input('Digite um número para saber a tabuada dele (#negativo para encerrar): '))
    i = 1 #aqui
    if n < 0:
        break
    else:
        while i <= 10: #se fizer com for não preciso declarar a variável i ali em cima
            print(f'{n} x {i} = {n*i}')
            i += 1
        print('-' * 30)
print('Programa Encerrado!')