# DESAFIO 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
#ele, lendo o nome deles e escrevendo o nome do escolhido.

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

from random import choice

l = [a1, a2, a3, a4]
r = choice(l)

print('O aluno escolhido pelo sistema foi: {}'.format(r))