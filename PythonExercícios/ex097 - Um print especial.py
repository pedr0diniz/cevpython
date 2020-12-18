# DESAFIO 097 - Faça um programa que tenha uma FUNÇÃO chamada escreva(), que receba um texto qualquer como parâmetro e
#mostre uma mensagem com tracinhos no tamanho adaptado da mensagem.

#Ex: escreva('Olá, Mundo!')

#Saída:
#~~~~~~~~~~~~~
# Olá, Mundo!
#~~~~~~~~~~~~~

def escreva(msg):
    print('~' * (len(msg)+4))
    print(msg.center(len(msg)+4)) #já que não consigo fazer formatando, uso o comando center mesmo
    print('~' * (len(msg)+4))
    print()


p1 = 'ziniD'
escreva(p1)
p2 = 'Curso de Python no Youtube'
escreva(p2)
p3 = 'CeV'
escreva(p3)
