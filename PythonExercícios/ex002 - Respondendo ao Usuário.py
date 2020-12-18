# Desafio 002 - Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

nome = input('Oi, qual é o seu nome? ')
print('Olá {}, é um prazer te conhecer!'.format(nome))

# Dá pra usar essas chaves {} com o .format(<variável>) pra botar as coisas nos cantos.
# Isso simplifica muito a escrita de dados. Me pergunto se dá pra fazer isso com muitas variáveis na mesma linha.