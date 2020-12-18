# DESAFIO 042 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será
#formado:

#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais
#ESCALENO: todos os lados diferentes

print('Digite os comprimentos de três segmentos de retas para verificar se eles podem formar um triângulo.')
print()
s1 = float(input('Digite o primeiro segmento de reta: '))
s2 = float(input('Digite o segundo segmento de reta: '))
s3 = float(input('Digite o terceiro segmento de reta: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os três segmentos {}, {} e {} formam um triângulo '.format(s1,s2,s3), end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO.')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('ISÓSCELES.')
    else:
        print('ESCALENO.')
else:
    print('Os três segmentos {}, {} e {} não formam um triângulo!'.format(s1,s2,s3))