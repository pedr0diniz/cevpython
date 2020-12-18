#AULA 3.22A - MÓDULOS E PACOTES

#Surgiu na década de 60
#Sistemas foram ficando cada vez maiores
#Foco: dividir um programa grande
#Foco: aumentar a legibilidade
#Foco: facilitar a manutenção

#pra as minhas funções e poder acessá-las no software principal, só importar

from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {numeros.dobro(num)}.')
print(f'O triplo de {num} é {numeros.triplo(num)}.')

#POSSO CRIAR UM ARQUIVO PRA JOGAR AS FUNÇÕES LÁ DENTRO

#VANTAGENS

#ORGANIZAÇÃO DE CÓDIGO
#FACILIDADE DE MANUTENÇÃO E REFATORAÇÃO
#OCULTAÇÃO DO CÓDIGO DETALHADO
#REUTILIZAÇÃO EM OUTROS PROJETOS