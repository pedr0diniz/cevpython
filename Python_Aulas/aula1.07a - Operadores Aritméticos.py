5+2==7 #Soma
5-2==3 #Subtração
5*2==10 #Multiplicação
5/2==2.5 #Divisão
5**2==25 #Potência
5//2==2 #Divisão inteira
5%2==1 #Resto da divisão inteira

#Ordem de precedência

#1 (), parênteses
#2 **, potências
#3 *, /, //, %, multiplicação, divisão, divisão inteira e resto de divisão
#4 +, -, soma e subtração

#5+3*2==11
#3*5+4**2==15+16==31
#3*(5+4)**2==3*(9)**2==243

# Raízes: **(1/2) - raiz quadrada, **(1/3) - raiz cúbica, **(1/x) - raiz de ordem x

#Operadores podem funcionar com strings

#'Oi' + 'Olá' == 'OiOlá'
#'Oi'*5 == OiOiOiOiOi
#print('='*20) == ====================

#Formatação de texto

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome)) #escreveu o nome em 20 espaços
print('Prazer em te conhecer {:>20}!'.format(nome)) #alinha o nome em 20 espaços à direita
print('Prazer em te conhecer {:<20}!'.format(nome)) #alinha o nome em 20 espaços à esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) #centraliza o nome em 20 espaços no meio
print('Prazer em te conhecer {:=^20}!'.format(nome)) #coloca sinais de = no nome, centralizando-o em 20 espaços

n1 = int(input('Digite um número '))
n2 = int(input('Digite outro número '))
soma = n1+n2
sub1 = n1-n2
sub2 = n2-n1
m = n1*n2
d1 = n1/n2
d2 = n2/n1
di1 = n1//n2
r1 = n1%n2
di2 = n2//n1
r2 = n2%n1
e1 = n1**n2
e2 = n2**n1

#Tudo em uma linha, usando o comando end=' ', que não quebra a linha
#\n quebra a linha em qualquer lugar que eu colocar
print('A soma vale {}, a subtração vale {}, a multiplicação vale {} e a divisão vale {:.5}.'.format(soma,sub1,m,d1), end=' ')

#MUITO útil usar a sintaxe dentro das máscaras {chaves} pra controlar o número de casas decimais

print('A divisão inteira de {} por {} vale {} com resto {}.'.format(n1,n2,di1,r1), end=' ')
print('{} elevado a {} vale {}. Já {} elevado a {} vale {}'.format(n1,n2,e1,n2,n1,e2))

#Em linhas separadas, com os prints normais

print('A soma de {} com {} vale {}. A subtração de {} por {} vale {}, já {} menos {} vale {}.'.format(n1,n2,soma,n1,n2,sub1,n2,n1,sub2))
print('A multiplicação de {} por {} vale {}. A divisão de {} por {} vale {}, já {} dividido por {} vale {}.'.format(n1,n2,m,n1,n2,d1,n2,n1,d2))
print('A divisão inteira de {} por {} vale {} com resto {}.'.format(n1,n2,di1,r1))
print('A divisão inteira de {} por {} vale {} com resto {}'.format(n2,n1,di2,r2))
print('{} elevado a {} vale {}, já {} elevado a {} vale {}.'.format(n1,n2,e1,n2,n1,e2))