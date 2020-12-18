#AULA 3.19C - DICIONÁRIOS

#CRIANDO UM DICIONÁRIO DENTRO DE UMA LISTA

brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print()

estado = dict()
brasil = list()
for c in range(0, 3):
  estado['uf'] = str(input('Unidade Federativa: '))
  estado['sigla'] = str(input('Sigla do Estado: '))
  brasil.append(estado.copy())
print(brasil)
cont = 0
for e in brasil:
  print(e) #A IMPRESSÃO É ASSIM PQ CADA ESTADO É UM DICIONÁRIO
  for k, v in e.items():
    print(f'O campo "{k.upper()}" tem valor "{v.title()}".')
  for v in e.values():
    print(v, end=' ')
  print()