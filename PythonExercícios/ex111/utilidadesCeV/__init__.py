# DESAFIO 111 - Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.

#Transfira todas as funções utilizados nos DESAFIOS 107, 108, 109 e 110 para o primeiro pacote
# e mantenha tudo funcionando.

from ex111.utilidadesCeV import moeda
from ex111.utilidadesCeV import dado

#ou from ex111.utilidadesCeV import moeda, dado

#ou import ex111.utilidadesCeV

preco = float(input('Digite o preço: R$'))
moeda.resumo(preco, 80, 35)
