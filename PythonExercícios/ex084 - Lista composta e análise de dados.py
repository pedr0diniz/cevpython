# DESAFIO 084 - Faça um programa que leia NOME E PESO de VÁRIAS PESSOAS, guardando tudo em uma LISTA. No final, mostre:

#A) QUANTAS pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais PESADAS.
#C) Uma listagem com as pessoas mais LEVES.

nomepeso = []
dados = []
controle = 'S'
maior = menor = 0

while controle == 'S':
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(nomepeso) == 0:                #não preciso varrer a lista depois de terminá-la para ver o maior e o menor
        maior = menor = dados[1]          #posso fazer isso já enquanto declaro os valores
    elif dados[1] > maior:                #como dados é uma lista simples, os pesos ficam na posição [1]
        maior = dados[1]                  #o ideal é determinar maior/menor durante a declaração
    elif dados[1] < menor:
        menor = dados[1]
    nomepeso.append(dados[:])
    dados.clear()
    controle = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while controle not in 'SN':
        controle = str(input('Opção inválida! [S/N] ')).strip().upper()[0]

print(nomepeso)
print(f'Ao todo, você cadastrou {len(nomepeso)} pessoas.')
print(f'O maior peso foi de {maior}kg, pertencente a: ', end='')
for pessoa in nomepeso:              #como eu já descobri o maior peso lá em cima, aqui embaixo eu varro só pra comparar
    if pessoa[1] == maior:
        print(f'{pessoa[0].title()}', end=' ')
print(f'\nO menor peso foi de {menor}kg, pertencente a: ', end='')
for pessoa in nomepeso:
    if pessoa[1] == menor:
        print(f'{pessoa[0].title()}', end=' ')
