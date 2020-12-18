# DESAFIO 112 - Dentro do pacote utilidadesCeV que criamos no DESAFIO 111, temos um módulo chamado dado. Crie uma função
#leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma VALIDAÇÃO DE DADOS para aceitar apenas
# valores que sejam monetários.

from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dado

#ou from ex112.utilidadesCeV import moeda, dado

#ou import ex112.utilidadesCeV

#preco = 5
preco = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(preco, 35, 22)

#CÓDIGO ESTAVA RODANDO 2X COM O NOME DESSE ARQUIVO COMO __main__.py
#ACHO QUE O PYTHON ESTAVA RODANDO O __main__.py do pacote ex112, QUE INICIAVA O __main__.py DE CADA MÓDULO DE FUNÇÃO.
#ENTRETANTO, CADA FUNÇÃO ESTÁ DENTRO DO ex112. PORTANTO, É COMO SE EU ESTIVESSE RODANDO CADA FUNÇÃO 2X.
#APARENTEMENTE RENOMEAR O __main__.py QUE EU USEI COMO MAIN DO PACOTE PARA QUALQUER OUTRA COISA RESOLVE O PROBLEMA.