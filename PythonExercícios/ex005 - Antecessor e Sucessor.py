# DESAFIO 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
print('O antecessor dele é {}.'.format(n-1))
print('O sucessor dele é {}.'.format(n+1))

#ou

a = n-1
s = n+1

print('O número {} é antecedido por {} e sucedido por {}.'.format(n,a,s))

#O ideal é fazer da primeira forma, pois só usarei as variáveis "a" e "s" uma vez. Se precisasse de "a" e "s" mais pra
#frente, valeria a pena usar as variáveis.