# DESAFIO 011 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quanti-
#dade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

l = float(input('Digite a largura da parede em metros: '))
h = float(input('Digite a altura da parede em metros: '))
a = l*h
t = a/2
print('Uma parede de {:.2f}m por {:.2f}m, com área de {:.2f}m², gastará {:.2f}L de tinta na sua pintura.'.format(l,h,a,t))

#ou

print('Uma parede de {:.2f}m por {:.2f}m, com área de {:.2f}m², gastará {:.2f}L de tinta na sua pintura.'.format(l,h,l*h,(l*h)/2))