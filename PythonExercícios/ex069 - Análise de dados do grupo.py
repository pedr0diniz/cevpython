# DESAFIO 069 - Crie um programa que leia a IDADE e o SEXO de VÁRIAS PESSOAS. A cada pessoa cadastrada, o programa deve-
#rá perguntar se o USUÁRIO quer ou não continuar. No final, mostre:

#A) Quantas pessoas têm mais de 18 ANOS.
#B) Quantos HOMENS foram cadastrados.
#C) Quantas #MULHERES têm menos de 20 ANOS.

idade = mais18 = homens = mulherm20 = 0
sexo = ' '
controle = 'S'

while True:
    if controle == 'S':
        idade = int(input('Digite a idade de uma pessoa: '))
        if idade >= 18:
            mais18 += 1
            sexo = str(input('Digite o sexo de uma pessoa [M/F]: ')).strip().upper()[0]
        while sexo not in 'MF':
            sexo = str(input('Opção Inválida! [M] ou [F}: ')).strip().upper()[0]
        if sexo == 'M':
            homens += 1
        elif idade < 20: #não preciso colocar if sexo == 'F' pq as duas condições acima já peneiraram.
            mulherm20 += 1
        controle = str(input('Deseja acrescentar mais pessoas [S/N]? ')).strip().upper()[0]
    else:
        break
print(f'A) {mais18} pessoas têm mais de 18 anos. \nB) {homens} homens foram cadastrados. '
      f'\nC) {mulherm20} mulheres têm menos de 20 anos.')