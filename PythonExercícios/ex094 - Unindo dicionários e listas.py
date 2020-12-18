# DESAFIO 094 - Crie um programa que leia NOME, SEXO e IDADE de VÁRIAS PESSOAS, guardando os dados de cada pessoa em
#um DICIONÁRIO e todos os dicionários em uma LISTA. No final, mostre:

#A) Quantas pessoas foram cadastradas
#B) A MÉDIA de idade do grupo.
#C) Uma lista com todas as MULHERES.
#D) Uma lista com todas as pessoas com IDADE acima da MÉDIA.

dicio = {}
pessoas = []
controle = 'S'
somai = mediai = 0
while controle == 'S':
  dicio['nome'] = str(input('Nome: '))
  dicio['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
  while dicio['sexo'] not in 'MF':
    dicio['sexo'] = str(input('ERRO! Por favor, digite apenas M ou F. \nSexo: [M/F] ')).strip().upper()[0]
  dicio['idade'] = int(input('Idade: '))
  somai += dicio['idade']
  controle = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
  while controle not in 'SN':
    controle = str(input(('ERRO! Responda apenas S ou N. \nQuer continuar? [S/N] '))).strip().upper()[0]
  pessoas.append(dicio.copy()) #preciso do copy pra jogar um dicionário numa lista
  dicio.clear()
mediai = somai/len(pessoas)
print('-=' * 30)
print(pessoas)
print(f'A) Ao todo temos {len(pessoas)} cadastradas.')
print(f'B) A média de idade é de {mediai:.2f} anos.')
print('C) As mulheres cadastradas foram:')
for pessoa in pessoas:
  if pessoa['sexo'] == 'F':
    print(f'   - {pessoa["nome"]}')
print('D) Lista das pessoas que estão acima da média de idades:')
for pessoa in pessoas:
  if pessoa['idade'] > mediai:
    for k, v in pessoa.items():
      print(f'{k.title()} = {v}; ', end='')
    print()
print('<< ENCERRADO >>')
#print(f'B) A média de idade é de {sum(pessoas[0:len(pessoas)][2])/len(pessoas)} anos.')