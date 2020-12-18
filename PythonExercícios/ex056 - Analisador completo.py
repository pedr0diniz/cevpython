# DESAFIO 056 - Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS. No final do programa, mostre:

#A MÉDIA DE IDADE do grupo.
#Qual é o nome do homem MAIS VELHO.
#Quantas mulheres têm MENOS DE 20 anos.

somaidade = 0
idadevelho = 0
nomevelho = ''
contmulheres = 0

for i in range(1,5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input('Nome: ')).strip() #coloquei os strips por causa do professor. não tinha lembrado.
    idade = int(input('Idade: '))
    somaidade += idade
    sexo = str(input('Sexo [H/M]: ')).strip()

    if sexo in 'Hh' and idade > idadevelho: #sexo in 'Hh' ou 'Mm' me faz não ser case-sensitive
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade < 20:
        contmulheres += 1

print('''
A média de idade do grupo é de {} anos.
O homem mais velho tem {} anos e se chama {}.
Das 4 pessoas acimas, {} são mulheres com menos de 20 anos.'''.format(somaidade/4, idadevelho, nomevelho, contmulheres))