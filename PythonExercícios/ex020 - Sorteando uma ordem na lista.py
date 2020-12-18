# DESAFIO 020 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

l = [a1, a2, a3, a4]

from random import sample, shuffle

r = sample(l,k=4)

print('A ordem de apresentação da lista será: {}.'.format(r))

#ou

shuffle(l)
print('A ordem de apresentação dos alunos será: {}.'.format(l))