# DESAFIO 091 - Crie um programa onde 4 JOGADORES joguem um DADO e tenham resultados ALEATÓRIOS. Guarde esses números
# em um DICIONÁRIO. No final, coloque esse dicionário em ORDEM, sabendo que o VENCEDOR tirou o MAIOR NÚMERO no dado.

from random import randint
from time import sleep
from operator import itemgetter

dicio = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
         'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}

print(dicio)

for k, v in dicio.items():
    sleep(0.66)
    print(f'{k} tirou {v} no dado.')

ranking = sorted(dicio.items(), key=itemgetter(1), reverse=True)
print(ranking)

# CRIEI O NOVO DICIONÁRIO PRA RANKEAR
# DEI O SORTED NOS ITENS DO DICIONÁRIO
# QUERO ORGANIZAR POR KEYS OU POR VALORES?
# KEYS VÊM PRIMEIRO, PORTANTO, SÃO PRIORIZADAS PELO PYTHON NO USO DO sorted()
# PARA ORGANIZARMOS PELOS VALORES, USAMOS O itemgetter()
# AS KEYS SERIAM AS POSIÇÕES [0] DO DICIONÁRIO, PORTANTO, O ARGUMENTO DO
# itemgetter() FICA 1.

# O RESULTADO DO sorted() É DADO EM FORMA DE LISTA, LOGO, POSSO TRATAR A
# VARIÁVEL ranking COMO UMA LISTA

for i, v in enumerate(ranking):
    if i == 0:
        print(f'O {ranking[i][0]} ficou em {i + 1} com o resultado {v[1]} no dado.')
    elif ranking[i - 1][1] == v[1]:
        print(f'O {ranking[i][0]} ficou em {i} com o resultado {v[1]} no dado.')
    else:
        print(f'O {ranking[i][0]} ficou em {i + 1} com o resultado {v[1]} no dado.')