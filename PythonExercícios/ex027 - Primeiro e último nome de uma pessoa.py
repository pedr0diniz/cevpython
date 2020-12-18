# DESAFIO 027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
#separadamente.
#Ex: Ana Maria de Souza
#primeiro = Ana
#último = Souza

nome = str(input('Digite o nome completo de uma pessoa: ')).split() #pego o nome completo e separo cada nome
print('O primeiro nome da pessoa é: {}'.format(nome[0])) #o [0] pega o primeiro elemento da lista
print('O último nome da pessoa é: {}'.format(nome[-1])) #o [-1] pega o último elemento de uma lista