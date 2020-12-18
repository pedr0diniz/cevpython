# DESAFIO 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite o salário atual: R$'))
ns = s*(1+0.15)
print('Um salário de R${:.2f} sobe para R${:.2f} ao receber um aumento de 15%.'.format(s,ns))

#ou

print('Um salário de R${:.2f} sobe para R${:.2f} ao receber um aumento de 15%.'.format(s,s*(1+0.15)))