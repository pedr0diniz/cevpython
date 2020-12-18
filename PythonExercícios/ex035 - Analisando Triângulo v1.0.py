# DESAFIO 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
#formar um triângulo.

s1 = float(input('Digite o primeiro segmento de reta: '))
s2 = float(input('Digite o segundo segmento de reta: '))
s3 = float(input('Digite o terceiro segmento de reta: '))

if s1 < s2 + s3 or s2 < s1 + s3 or s3 < s1 + s2:
    print('Os segmentos {}, {} e {} podem formar um triângulo!'.format(s1,s2,s3))
else:
    print('Os segmentos {}, {} e {} não podem formar um triângulo!'.format(s1,s2,s3))