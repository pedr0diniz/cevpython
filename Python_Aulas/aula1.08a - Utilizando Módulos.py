#import <biblioteca> adicionada funcionalidades de uma biblioteca inteira além da linguagem padrão
#from <biblioteca> import <funcao> adiciona uma funcionalidade específica de uma biblioteca

#ceil arredonda pra cima
#floor arredonda pra baixo
#trunc trunca casas decimais após a vírgula
#pow é a potência de um primeiro número com um segundo número
#sqrt tira a raiz quadrada
#factorial calcula o fatorial do número lido

#se eu quiser fazer todas as operações, dou import math
#se eu só quiser, por exemplo, tirar raiz quadrada, e potência coloco from math import sqrt,pow

import math

num = int(input('Digite um número: '))

raiz = math.sqrt(num)

#ao digitar math., eu vejo quais funções aquela biblioteca me disponibiliza

print('A raiz de {} é igual a {}.'.format(num,raiz))

#arredondando pra cima

print('A raiz de {} é igual a {}.'.format(num,math.ceil(raiz)))

#arredondando pra baixo

print('A raiz de {} é igual a {}.'.format(num,math.floor(raiz)))

#limitando as casas decimais

print('A raiz de {} é igual a {:.2f}.'.format(num,raiz))