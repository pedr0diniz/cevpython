#AULA 3.19B - DICIONÁRIOS

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
#print(pessoas[0]) #VAI DAR ERRO, NÃO EXISTE INDICE 0, 1 OU 2
#EXISTEM OS INDICES NOME, SEXO E IDADE
print(pessoas['nome'])
print(pessoas['sexo'])
print(pessoas['idade'])
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos.')
print()

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items()) #IMPRIME ESTILO UMA LISTA COMPOSTA POR 3 TUPLAS
print()

for k in pessoas.keys():
  print(k.title())
print()
for k in pessoas.values():
  if isinstance(k, str): #VERIFICA SE A VARIÁVEL "k" É "string"
    print(k.title())
  else:
    print(k)
print()
for k, v in pessoas.items():
  print(f'{k.title()} = {v}')
print()

#NÃO HÁ ENUMERATE PARA DICIONÁRIOS
del pessoas['sexo']
for k, v in pessoas.items():
  print(f'{k.title()} = {v}')
print()

pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k, v in pessoas.items():
  print(f'{k.title()} = {v}')