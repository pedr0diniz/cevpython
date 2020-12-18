# DESAFIO 031 - Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
#cobrando R$ 0,50 por km para viagens até 200km e R$ 0,45 para viagens mais longas.

d = float(input('Qual é a distância da sua viagem em km? '))

print('Você está prestes a fazer uma viagem de {:.1f}km.'.format(d))

if d <= 200:
    p = d*0.5
else:
    p = d*0.45
print('O preço da sua passagem será de R${:.2f}.'.format(p))