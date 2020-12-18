#AULA 3.19A - DICIONÁRIOS

dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])
print()

#COMO FAZER OS ÍNDICES SEREM LITERAIS (NOME, NÚMERO)
#AO INVÉS DE NUMÉRICOS (0, 1)?

#tuplas ()
#listas []
#dicionários {}

dados2 = {}
#ou
#dados2 = dict()

dados2 = {'nome':'Pedro', 'idade':25}
print(dados2['nome'])
print(dados2['idade'])

#APPEND NÃO FUNCIONA

dados2['sexo'] = 'M'
print(dados2)
del dados2['idade']
print(dados2)
print()
filme = {'titulo':'Star Wars',
        'ano':1977,
        'diretor':'George Lucas'}
print(filme)
print(filme.values()) #IMPRIME SÓ OS VALORES DAS CÉLULAS DO DICIONÁRIO
print(filme.keys()) #IMPRIME SÓ AS "TAGS", SÓ OS NOMES DAS CATEGORIAS
print(filme.items())

for k, v in filme.items():
  print(f'O {k} é {v}.')

#TUPLAS, LISTAS E DICIONÁRIOS PODEM ENGLOBAR OUTRAS TUPLAS, LISTAS E DICIONÁRIOS

filme1 = {'titulo':'Avengers',
          'ano':2012,
          'diretor':'Joss Whedon'}

filme2 = {'titulo':'Matrix',
         'ano':1999,
         'diretor':'Wachowski'}

locadora = []
locadora.append(filme)
locadora.append(filme1)
locadora.append(filme2)         #DICIONÁRIO DENTRO DE LISTA

print(locadora)
print()
for i in range(0, len(locadora)):
  for k, v in locadora[i].items():
    print(f'O {k} é {v}.')
  print()