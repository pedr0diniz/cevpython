# DESAFIO 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o preço do produto: R$'))
pd = p*(1-0.05)
print('Um produto no valor de R${:.2f} sai por R${:.2f} com 5% de desconto.'.format(p,pd))

#ou

print('Um produto no valor de R${:.2f} sai por R${:.2f} com 5% de desconto.'.format(p,p*(1-0.05)))