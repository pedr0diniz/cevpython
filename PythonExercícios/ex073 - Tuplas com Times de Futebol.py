# DESAFIO 073 - Crie uma TUPLA preenchida com os 20 PRIMEIROS colocados da Tabela do Campeonato Brasileiro de Futebol,
#na ordem de colocação. Depois mostre:

#A) Apenas os 5 PRIMEIROS colocados.
#B) Os ÚLTIMOS 4 colocados da tabela.
#C) Uma lista com os times em ORDEM ALFABÉTICA.
#D) Em que POSIÇÃO na tabela está o time da Chapecoense.

brasileirao = ['Flamengo', 'Santos', 'Corinthians', 'São Paulo', 'Palmeiras', 'Internacional', 'Atlético Mineiro',
               'Bahia', 'Athlético-PR', 'Botafogo', 'Grêmio', 'Fortaleza', 'Goiás', 'Ceará', 'Vasco da Gama',
               'Cruzeiro', 'Chapecoense', 'Fluminense', 'CSA', 'Avaí']

print('-=' * 20)
print(f'Os 5 primeiros são: {brasileirao[:5]}')
print('-=' * 20)
print(f'Os 4 últimos são: {brasileirao[-4:]}')
print('-=' * 20)
print(f'A lista de times em ordem alfabética é: {sorted(brasileirao)}')
print('-=' * 20)
print(f'A Chapecoense está na {brasileirao.index("Chapecoense")+1}ª posição.') #não pode ter '' dentro das '' da fstring
                                                                               #a solução é buscar o index com "".
#index = brasileirao.index('Chapecoense')
#print(f'A Chapecoense está na {index+1}ª posição.')