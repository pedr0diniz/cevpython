# DESAFIO 089 - Crie um programa que leia NOME e DUAS NOTAS de vários alunos e guarde tudo em uma LISTA COMPOSTA. No
#final, mostre um BOLETIM contendo a MÉDIA de cada um e permita que o usuário possa mostrar as NOTAS de cada aluno
#individualmente.

from time import sleep

boletim = []
alunos = []
controle = 'S'
naluno = 0

while controle == 'S':
    alunos.append(str(input('Nome: ')))
    n1 = float(input('Nota 1: '))
    while n1 < 0 or n1 > 10:
        n1 = float(input('Nota inválida! Digite a Nota 1: '))
    n2 = float(input('Nota 2: '))
    while n2 < 0 or n2 > 10:
        n2 = float(input('Nota inválida! Digite a Nota 2: '))
    alunos.append([n1, n2])
    alunos.append((alunos[1][0] + alunos[1][1])/2)
    controle = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while controle not in 'SN':
        controle = str(input('Opção inválida! [Sim] ou [Não]: ')).strip().upper()[0]
    boletim.append(alunos[:])
    alunos.clear()
print()
print(f'------------------------------')
print(f'Nº  NOME                 MÉDIA')
print(f'------------------------------')
for indice, aluno in enumerate(boletim):
    print(f'{indice+1}   {aluno[0].title():<20} {aluno[2]:>5.1f}')

while True:
    naluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if naluno == 999:
        break
    while naluno < 1 or (naluno > len(boletim) and naluno != 999):
        print('Aluno não encontrado!')
        naluno = int(input(f'Digite um número entre 1 e {len(boletim)} ou 999 para interromper: '))
        if naluno == 999:
            break
    print(f'As notas de {boletim[naluno-1][0].title()} foram {boletim[naluno-1][1]}.')
    print('------------------------------------------')

print('--------------')
print('FINALIZANDO...')
print('--------------')
sleep(1)
print('VOLTE SEMPRE!!')