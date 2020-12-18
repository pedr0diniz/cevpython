# DESAFIO 095 - Aprimore o DESAFIO 093 para que ele funcione com VÁRIOS JOGADORES, incluindo um sistema de visuali-
#zação de DETALHES DO APROVEITAMENTO de cada jogador.

dicio = {}
partidas = idjog = 1
gols = []
controle = 'S'
jogadores = []

while controle == 'S':
  dicio['nome'] = str(input('Nome do Jogador: '))
  partidas = int(input(f'Quantas partidas {dicio["nome"]} jogou? '))
  for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {i+1}? ')))
  dicio['gols'] = gols.copy()
  dicio['total'] = sum(gols)
  jogadores.append(dicio.copy())
  gols.clear() #se eu não der um clear nos gols, eles irão se acumulando nos termos seguintes
  dicio.clear()
  controle = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  while controle not in 'SN':
    controle = str(input('Opção inválida! \nDigite S ou N: ')).strip().upper()[0]
print('-=' * 40)
print(jogadores)
print('Nº  Nome               Gols               Total')
print('-----------------------------------------------')
for i, jogador in enumerate(jogadores):
  print(f'{i+1:<3} ',end='')
  for v in jogador.values(): #não preciso das keys, posso usar .values() ao invés de .items()
    print(f'{str(v):<18}',end =' ') #precisei converter tudo pra string pra mostrar
                                    #tava dando erro ao tentar espaçar s impressão da lista de gols
  print()
print('-----------------------------------------------')
while 0 < idjog <= len(jogadores) or idjog == 999:
  idjog = int(input('Mostrar dados de qual jogador [999 para parar]? '))
  while idjog < 1 or (idjog > len(jogadores) and idjog != 999):
    print('Jogador não encontrado!')
    idjog = int(input('Mostrar dados de qual jogador [999 para parar]? '))
  if idjog == 999:
    break
  print(f' -- Levantamento do jogador {jogadores[idjog-1]["nome"]}: ')
  for i, gols in enumerate(jogadores[idjog - 1]['gols']):  # ACESSANDO A LISTA DE GOLS DO jogador [idjog-1]
      print(f'    No jogo {i + 1} fez {gols} gols.')          # IMPRIMINDO CADA GOL DENTRO
  print('-----------------------------------------------')    # DA CÉLULA "GOLS" DO JOGADOR NA
print('<< ENCERRADO >>')                                      # CÉLULA[idjog-1] DA LISTA jogadores[]