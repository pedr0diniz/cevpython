# DESAFIO 107 - Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().

#Faça também um programa que IMPORTE esse módulo e use algumas dessas funções.

#import moeda

#ou

#import ex107.moeda

#ou

from ex107 import moeda

preco = float(input('Digite o preço: R$'))
print(f'Aumentando 50%, temos R${moeda.aumentar(preco, 50):.2f}.')
print(f'Diminuindo 20%, temos R${moeda.diminuir(preco, 50):.2f}.')
print(f'O dobro de R${preco:.2f} é R${moeda.dobro(preco):.2f}.')
print(f'A metade de R${preco:.2f} é R${moeda.metade(preco):.2f}.')
