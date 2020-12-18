# DESAFIO 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas;
#O nome com todas as letras minúsculas;
#Quantas letras ao todo (sem considerar espaços);
#Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))

M = nome.upper()
m = nome.lower()
sp = nome.split() #separa minha string em um vetor com cada palavra separada. elimina os espaços.
tl = len(''.join(sp)) #pega todos os nomes do vetor acima e junta ele numa string só
ln1 = len(sp[0])

#para contar todas as letras também posso fazer:
#print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))), assim contando todos os espaços e os
#subtraindo da contagem

#para contar a quantidade de letras do primeiro nome, posso fazer:
#nome.strip() para tirar os espaços indesejados no começo e no final
#print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) para encontrar o primeiro espaço no nome.
#a casa onde estiver o primeiro espaço será exatamente igual à quantidade de caracteres do primeiro nome.
#teoricamente seria uma casa a mais, mas como em python os vetores começam em 0, então dá certo.


print('''Seu nome completo todo em maiúsculas é: {}
Seu nome completo todo em minúsculas é: {}
Seu nome tem {} letras.
Seu primeiro nome é {} e tem {} letras.'''.format(M,m,tl,sp[0],ln1))