# DESAFIO 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A média entre a primeira nota ({}) e a segunda nota ({}) é {:.1f}.'.format(n1,n2,m))

#ou

print('A média entre a primeira nota ({}) e a segunda nota ({}) é {:.1f}.'.format(n1,n2,(n1+n2)/2))

#O python arredonda pra cima os algarismos truncados terminados em 5