# DESAFIO 061 - Refaça o DESAFIO 051, lendo o PRIMEIRO TERMO e a RAZÃO de uma PA, mostrando os 10 PRIMEIROS TERMOS da
#sua progressão usando a estrutura WHILE.

a1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
i = 0
while i < 10:
    print('O {}º termo da PA é igual a: {}'.format(i+1, a1))
    a1 += razao
    i += 1
