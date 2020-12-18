# DESAFIO 090 - Faça um programa que leia NOME e MÉDIA de um aluno, guardando também a SITUAÇÃO em um DICIONÁRIO.
#No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Média do {aluno["nome"]}: '))
if aluno['media'] >= 7.0:
  aluno['status'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
  aluno['status'] = 'em recuperação'
else:
  aluno['status'] = 'reprovado'
info.append(aluno.copy())
print(info)
print()

for k, v in aluno.items():
  print(f'{k.title()} do aluno é: {v}.')