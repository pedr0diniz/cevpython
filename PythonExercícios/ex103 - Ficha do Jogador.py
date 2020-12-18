# DESAFIO 103 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o NOME de um
#jogador e quantos GOLS ele marcou.

#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(j = "<desconhecido>", g = 0):
    print(f"O jogador {j} fez {g} gol(s).")

jogador = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric(): #verifico se gols é numérico. se não for ou for vazio, gols = 0. assim, sempre vai rodar.
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '': #se o nome do jogador for vazio (ou não) eu chamo a função de qualquer jeito
    ficha(g = gols) #se passei o jogador vazio, declaro a variável g da função como igual a gols (de fora da função)
else:
    ficha(jogador, gols)
