# DESAFIO 051 - Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PA. No final, mostre os 10 primeiros
#termos dessa progressão.

print('=' * 30)
print(' 10 TERMOS DE UMA PA '.center(30, '=')) #escolho minha string, centralizo escolhendo em quantos espaços eu quero
#ocupar e o que eu coloco nos espaços "vazios". nesse caso, preenchi os vazios com ' '
print('=' * 30)
pa = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for n in range (0,10):
    print(pa, end=' → ')
    pa += r
print('FIM DOS DEZ TERMOS DA PA.')