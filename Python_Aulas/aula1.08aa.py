from math import sqrt

n = int(input('Digite um número: '))
r = sqrt(n)
print('A raiz de {} é igual a {:.2f}.'.format(n,r))

#importando a função diretamente da biblioteca me faz não precisar do prefixo .math antes dela.

#documentação abundante no python.org, na aba docs, em library reference
#tópico 9 apresenta as bibliotecas numéricas