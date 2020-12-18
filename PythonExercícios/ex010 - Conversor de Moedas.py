# DESAFIO 010 - Crie um programa que leia quantos reais uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$1,00 = R$3,27

n = float(input('Quantos R$ você tem na carteira? R$'))
d = n/3.27
di = int(d)

print('Você pode comprar US${:.2f}. Se você não gosta de moedas, você pode comprar US${:.2f}.'.format(d,di))