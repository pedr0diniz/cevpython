# DESAFIO 108 - Adapte o código do DESAFIO 107, criando uma função adicional chamada moeda() que consiga mostrar os valores
#como um valor monetário formatado.

#import moeda

#ou

#import ex107.moeda

#ou

from ex108 import moeda

preco = float(input('Digite o preço: R$'))
print(f'Aumentando 50%, temos R${moeda.moeda(moeda.aumentar(preco, 50))}.') #moeda.moeda vai formatar o resultado das
print(f'Diminuindo 20%, temos R${moeda.moeda(moeda.diminuir(preco, 20))}.') #funções moeda.aumentar/diminuir no
print(f'O dobro de {moeda.moeda(preco)} é R${moeda.dobro(preco):.2f}.')     #seu argumento
print(f'A metade de {moeda.moeda(preco)} é R${moeda.metade(preco):.2f}.')
