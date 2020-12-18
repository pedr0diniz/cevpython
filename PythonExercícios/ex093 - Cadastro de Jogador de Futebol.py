# DESAFIO 093 - Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL. O programa vai ler o NOME DO
#JOGADOR e QUANTAS PARTIDAS ele jogou. Depois vai ler a QUANTIDADE DE GOLS feitos em CADA PARTIDA. No final, tudo isso
#será guardado e3m um DICIONÁRIO, incluindo o TOTAL DE GOLS feitos durante o campeonato.

dicio = {}
gols = []
temp = []
dicio['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dicio["nome"]} jogou? '))
for i in range (0, partidas):
  gols.append(int(input(f'   Quantos gols na partida {i+1}? ')))
dicio['gols'] = gols.copy() #COLOCANDO UMA LISTA EM UM DICIONÁRIO
dicio['total'] = sum(gols)
print(f'{"-=" * 30}\n{dicio}\n{"-=" * 30}')
for k, v in dicio.items():
  print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {dicio["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(gols):
  print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {sum(gols)} gols.')