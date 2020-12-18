# DESAFIO 109 - Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem um parâmetro a mais, informando
#se o valor retornado ppor elas vai ser ou não formatado pela função moeda(), desenvolvida no DESAFIO 108.

from ex109 import moeda

preco = float(input('Digite o preço: R$'))
print(f'Aumentando 50%, temos {moeda.aumentar(preco, 50, True)}.') #moeda.moeda vai formatar o resultado das
print(f'Diminuindo 20%, temos {moeda.diminuir(preco, 20, True)}.') #funções moeda.aumentar/diminuir no
print(f'O dobro de {moeda.moeda(preco)} é R${moeda.dobro(preco, True)}.')     #seu argumento
print(f'A metade de {moeda.moeda(preco)} é R${moeda.metade(preco, True)}.')
