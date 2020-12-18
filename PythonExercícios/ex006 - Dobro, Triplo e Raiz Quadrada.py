# DESAFIO 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Digite um número para descobrir seu dobro, triplo e raiz quadrada: '))
print('O dobro de {} é {}.'.format(n,2*n))
print('O triplo de {} é {}.'.format(n,3*n))
print('A raiz quadrada de {} é {}.'.format(n,n**(1/2)))

#ou

d = 2*n
t = 3*n
r = n**(1/2)

print('O dobro de {} é {}.'.format(n,d))
print('O triplo de {} é {}.'.format(n,t))
print('A raiz quadrada de {} é {}.'.format(n,r))

