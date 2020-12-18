# DESAFIO 015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de
#dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$0,15 por km
#rodado.

km = float(input('Quantos kilômetros foram rodados? '))
d = int(input('Por quantos dias o carro foi alugado? '))
p = 0.15*km + 60*d

print('O aluguel de um carro que rodou {}km durante {} dias custa R${:.2f}.'.format(km,d,p))

#ou

print('O aluguel de um carro que rodou {}km durante {} dias custa R${:.2f}.'.format(km,d,0.15*km+60*d))