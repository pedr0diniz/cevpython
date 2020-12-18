# DESAFIO 068 - Faça um programa que jogue PAR OU ÍMPAR com o computador. O jogo só será interrompido quando o jogador
#PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

pi = resultado = 'VAMOS JOGAR PAR OU ÍMPAR' #inicio o par ou ímpar com uma mensagem inicial do jogo
tracinhos = '-' * len(pi)
print(f'{tracinhos}\n{pi}\n{tracinhos}')
usuario = vitorias = 0
from random import randint
from unidecode import unidecode

while True:
    usuario = int(input('Diga um número: '))
    pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    while pi not in 'PI':
        pi = str(input('Opção Inválida! Digite P para par ou I para ímpar: ')).strip().upper()[0]
    computador = randint(0, 10)
    if (usuario + computador) % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'ímpar'
    print(f'{tracinhos}\nVocê jogou {usuario} e o computador jogou {computador}.\n{usuario} com {computador} dá '
          f'{usuario + computador}, que é {resultado}.\n{tracinhos}')
    if unidecode(resultado[0]).strip().upper() == pi: #unidecode para ignorar o acento do ímpar
        print('Você ganhou!')
        vitorias += 1
    else:
        print('Você perdeu!')
        break
print(f'GAME OVER! Você venceu {vitorias} vezes.')