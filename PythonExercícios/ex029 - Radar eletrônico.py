# DESAFIO 029 - Escreva um programa que leia a velocidade de um carro.

#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

#A multa vai custar R$ 7,00 por cada km acima do limite.

v = int(input('Qual é a velocidade atual do carro? '))

if v>80:
    m = 7*(v-80)
    print('''O carro foi multado por excesso de velocidade ao trafegar a {}km/h numa via com limite de 80km/h! 
    A multa tem o valor de R${},00.'''.format(v,m))
else:
    print('Tenha um bom dia! Dirija com segurança!')